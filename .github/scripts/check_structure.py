#!/usr/bin/env python3
"""
CI structural check for the Product-Marketing-Skills marketplace repo.

Fails (non-zero exit) if:
  1. marketplace.json's plugin list doesn't match what's actually on disk
     (a plugin folder with a .claude-plugin/plugin.json in it).
  2. Any plugin.json's "skills" field points at a path that doesn't exist.
  3. Any SKILL.md or command file references another skill by name
     (via a `pmm-x:y` style or bare skill-name mention in a "Related
     Skills" / "Uses the X skill" line) that doesn't resolve to a real
     skill folder anywhere in the repo.

Prints one line per problem found, then a final PASS/FAIL summary.
Exit code 0 = clean, 1 = at least one problem found.
"""
import json
import os
import re
import sys

ROOT = os.getcwd()
problems = []


def load_json(path):
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        return None, f"missing file: {path}"
    try:
        with open(full, "r", encoding="utf-8") as f:
            return json.load(f), None
    except json.JSONDecodeError as e:
        return None, f"invalid JSON in {path}: {e}"


def resolve(base_dir, rel_path):
    return os.path.normpath(os.path.join(ROOT, base_dir, rel_path))


# ---- Check 1: marketplace.json plugin list vs disk ------------------------

marketplace, err = load_json(".claude-plugin/marketplace.json")
if err:
    problems.append(err)
    marketplace = {"plugins": []}

listed_plugin_dirs = set()
for p in marketplace.get("plugins", []):
    src = p.get("source", "")
    name = p.get("name", "<unnamed>")
    src_clean = src.lstrip("./")
    if not src_clean:
        problems.append(f"marketplace.json: plugin '{name}' has empty source")
        continue
    listed_plugin_dirs.add(src_clean)
    plugin_json_path = os.path.join(src_clean, ".claude-plugin", "plugin.json")
    if not os.path.isfile(os.path.join(ROOT, plugin_json_path)):
        problems.append(
            f"marketplace.json lists '{name}' at '{src}' but "
            f"{plugin_json_path} does not exist"
        )

on_disk_plugin_dirs = set()
for entry in os.listdir(ROOT):
    full = os.path.join(ROOT, entry)
    if not os.path.isdir(full):
        continue
    if os.path.isfile(os.path.join(full, ".claude-plugin", "plugin.json")):
        on_disk_plugin_dirs.add(entry)

for extra in sorted(on_disk_plugin_dirs - listed_plugin_dirs):
    problems.append(
        f"'{extra}' has a .claude-plugin/plugin.json on disk but is not "
        f"listed in marketplace.json"
    )

# ---- Check 2: each plugin.json's "skills" field points at a real path -----

skill_dirs_by_plugin = {}

for plugin_dir in sorted(on_disk_plugin_dirs):
    pj_path = f"{plugin_dir}/.claude-plugin/plugin.json"
    pj, err = load_json(pj_path)
    if err:
        problems.append(err)
        continue
    skills_field = pj.get("skills")
    if skills_field is None:
        problems.append(f"{pj_path}: missing 'skills' field")
        continue
    if isinstance(skills_field, str):
        candidates = [skills_field]
    elif isinstance(skills_field, list):
        candidates = skills_field
    else:
        problems.append(f"{pj_path}: 'skills' field is neither a string nor an array")
        continue

    resolved_dirs = []
    for c in candidates:
        target = resolve(plugin_dir, c)
        if not os.path.isdir(target):
            problems.append(
                f"{pj_path}: skills path '{c}' resolves to "
                f"'{os.path.relpath(target, ROOT)}', which does not exist"
            )
        else:
            resolved_dirs.append(target)
    skill_dirs_by_plugin[plugin_dir] = resolved_dirs

# ---- Check 3: skill-name cross-references resolve to real skills ---------

# Build the set of every real skill name in the repo (folder containing a
# SKILL.md, name taken from the folder itself).
real_skill_names = set()
for plugin_dir, dirs in skill_dirs_by_plugin.items():
    for d in dirs:
        for entry in os.listdir(d):
            sub = os.path.join(d, entry)
            if os.path.isdir(sub) and os.path.isfile(os.path.join(sub, "SKILL.md")):
                real_skill_names.add(entry)
        # flat-structure plugins (skills field resolves directly to a dir
        # that itself has subfolders with SKILL.md one level down, OR is
        # itself a single skill folder)
        if os.path.isfile(os.path.join(d, "SKILL.md")):
            real_skill_names.add(os.path.basename(d))

# Scan every SKILL.md and commands/*.md for `pmm-x:y` or bare skill-name
# references, and flag ones that don't match any real skill name.
ref_pattern = re.compile(r"`pmm-[a-z-]+:([a-z][a-z0-9-]*)`")

for dirpath, dirnames, filenames in os.walk(ROOT):
    if "/.git" in dirpath:
        continue
    for fname in filenames:
        if fname != "SKILL.md" and not (dirpath.endswith("/commands") and fname.endswith(".md")):
            continue
        fpath = os.path.join(dirpath, fname)
        rel = os.path.relpath(fpath, ROOT)
        with open(fpath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        for m in ref_pattern.finditer(content):
            ref_name = m.group(1)
            if ref_name not in real_skill_names:
                problems.append(
                    f"{rel}: references '{ref_name}' via `{m.group(0)}` "
                    f"but no skill folder named '{ref_name}' exists"
                )

# ---- Report -----------------------------------------------------------

if problems:
    print(f"FAIL — {len(problems)} structural problem(s) found:\n")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
else:
    print("PASS — marketplace.json, all plugin.json skills paths, and all "
          "skill cross-references are consistent.")
    sys.exit(0)
