#!/usr/bin/env python3
"""
CI structural check for the Product-Marketing-Skills marketplace repo.

Fails (non-zero exit) if:
  1. marketplace.json's plugin list doesn't match what's actually on disk
     (a plugin folder with a .claude-plugin/plugin.json in it).
  2. Any plugin.json's "skills" field points at a path that doesn't exist.
  3. Any SKILL.md or command file references another skill by name
     (via a `pmm-x:y` style, or a bare backticked skill-style name like
     `some-skill-name`, in a "Related Skills" / "Uses the X skill" /
     "Do Not Use For" line) that doesn't resolve to a real skill folder
     anywhere in the repo.
  4. The root .claude-plugin/plugin.json's "skills" field is missing any
     plugin directory that actually exists on disk with its own
     .claude-plugin/plugin.json (i.e. every real plugin must be
     reachable from the root manifest, not just from marketplace.json).

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

# ---- Check 1b: root plugin.json's "skills" field covers every plugin ------
# (NEW — closes the hole that let pmm-growth go missing from the root
# manifest undetected: check 1 above only validates marketplace.json, never
# the root .claude-plugin/plugin.json's own "skills" array against disk.)

root_pj, root_pj_err = load_json(".claude-plugin/plugin.json")
if root_pj_err:
    problems.append(root_pj_err)
    root_pj = {"skills": []}

root_skills_field = root_pj.get("skills", [])
if isinstance(root_skills_field, str):
    root_skills_field = [root_skills_field]

root_skills_clean = {str(s).lstrip("./").split("/")[0] for s in root_skills_field}

for plugin_dir in sorted(on_disk_plugin_dirs):
    if plugin_dir not in root_skills_clean:
        problems.append(
            f".claude-plugin/plugin.json: plugin directory '{plugin_dir}' "
            f"exists on disk and is listed in marketplace.json, but is not "
            f"referenced anywhere in the root plugin.json's 'skills' field"
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

# Scan every SKILL.md and commands/*.md for `pmm-x:y` style references OR
# any backticked/bold name carrying a known dead-namespace prefix, and flag
# ones that don't match any real skill name.
#
# Two checks now (was one — the single `pmm-x:y` pattern silently missed
# every bare `hs-something` reference, which is exactly how the dead
# `hs-alternatives-map` / `hs-competitive-battlecard` references went
# undetected across multiple review passes — including one written in
# **bold**, not backticks, which the colon pattern also can't see).
#
# Deliberately scoped to known dead/retired namespace prefixes rather than
# "any hyphenated backticked word" — the broader version flagged real
# compound terms like `at-risk` or `metric-first` as false positives.
# DEAD_PREFIXES is the one place to extend this list if another naming
# migration happens later (e.g. repo renames `pmm-` to something else).
colon_ref_pattern = re.compile(r"`pmm-[a-z-]+:([a-z][a-z0-9-]*)`")
DEAD_PREFIXES = ("hs-",)
dead_prefix_pattern = re.compile(
    r"[`*]{1,2}(" + "|".join(re.escape(p) for p in DEAD_PREFIXES) + r"[a-z0-9-]+)[`*]{1,2}"
)

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

        seen_on_this_line = set()

        for m in colon_ref_pattern.finditer(content):
            ref_name = m.group(1)
            seen_on_this_line.add(ref_name)
            if ref_name not in real_skill_names:
                problems.append(
                    f"{rel}: references '{ref_name}' via `{m.group(0)}` "
                    f"but no skill folder named '{ref_name}' exists"
                )

        for m in dead_prefix_pattern.finditer(content):
            ref_name = m.group(1)
            if ref_name in seen_on_this_line or ref_name in real_skill_names:
                continue
            seen_on_this_line.add(ref_name)
            problems.append(
                f"{rel}: references `{ref_name}` (dead namespace prefix "
                f"{[p for p in DEAD_PREFIXES if ref_name.startswith(p)][0]!r}) "
                f"but no skill folder named '{ref_name}' exists — this "
                f"naming convention was retired repo-wide; update the "
                f"reference to the real current skill name, or remove it"
            )

# ---- Check 5: connector placeholders ------------------------------------
# Every `~~category` used in a plugin's SKILL.md files must be listed in that
# plugin's CONNECTORS.md; every category there must exist in the root
# CONNECTORS.md; every .mcp.json server needs type + url and must be named
# in the plugin's CONNECTORS.md.

placeholder_pattern = re.compile(r"`(~~[A-Za-z][A-Za-z -]*[A-Za-z])`")


def read_text(rel):
    with open(os.path.join(ROOT, rel), "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


root_cats = set()
if not os.path.isfile(os.path.join(ROOT, "CONNECTORS.md")):
    problems.append("CONNECTORS.md: root connector registry is missing")
else:
    root_cats = set(placeholder_pattern.findall(read_text("CONNECTORS.md")))

for plugin_dir in sorted(on_disk_plugin_dirs):
    used = set()
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, plugin_dir)):
        for fn in files:
            if fn == "SKILL.md":
                used |= set(placeholder_pattern.findall(
                    read_text(os.path.relpath(os.path.join(dirpath, fn), ROOT))))
    mcp_rel = f"{plugin_dir}/.mcp.json"
    mcp_data, mcp_err = load_json(mcp_rel)
    has_mcp = os.path.isfile(os.path.join(ROOT, mcp_rel))
    if has_mcp and mcp_err:
        problems.append(mcp_err)
        mcp_data = None
    conn_rel = f"{plugin_dir}/CONNECTORS.md"
    has_conn = os.path.isfile(os.path.join(ROOT, conn_rel))
    if (used or has_mcp) and not has_conn:
        problems.append(f"{conn_rel}: missing, but {plugin_dir} uses connector placeholders or ships a .mcp.json")
        continue
    if not has_conn:
        continue
    conn_text = read_text(conn_rel)
    listed = set(placeholder_pattern.findall(conn_text))
    for ph in sorted(used - listed):
        problems.append(f"{conn_rel}: placeholder `{ph}` is used in a SKILL.md but not listed here")
    for ph in sorted(listed - root_cats):
        problems.append(f"{conn_rel}: placeholder `{ph}` is not in the root CONNECTORS.md registry")
    if mcp_data is not None:
        for name, cfg in (mcp_data.get("mcpServers") or {}).items():
            if not isinstance(cfg, dict) or "type" not in cfg or "url" not in cfg:
                problems.append(f"{mcp_rel}: server '{name}' needs both 'type' and 'url'")
            if name.lower() not in conn_text.lower():
                problems.append(f"{conn_rel}: server '{name}' is in .mcp.json but not named here")

# ---- Check 6: no credentials in .mcp.json files ------------------------
# Each product marketer signs in with their own account. A .mcp.json must
# never carry keys, tokens, passwords, headers or env values. (oauth clientId
# is a public identifier and is allowed.)

FORBIDDEN_KEYS = {"headers", "env", "token", "apikey", "api_key", "secret",
                  "password", "authorization", "bearer", "accesstoken"}
FORBIDDEN_URL_BITS = ("key=", "token=", "apikey=", "secret=", "password=")


def _scan_mcp(node, where, rel):
    if isinstance(node, dict):
        for k, v in node.items():
            if str(k).lower() in FORBIDDEN_KEYS:
                problems.append(f"{rel}: '{k}' found at {where or 'top level'}; "
                                f"credentials must not be stored in .mcp.json")
            elif k == "url" and isinstance(v, str) and any(b in v.lower() for b in FORBIDDEN_URL_BITS):
                problems.append(f"{rel}: url at {where or 'top level'} looks like it carries a credential")
            _scan_mcp(v, f"{where}.{k}" if where else str(k), rel)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _scan_mcp(v, f"{where}[{i}]", rel)


for plugin_dir in sorted(on_disk_plugin_dirs):
    mcp_rel = f"{plugin_dir}/.mcp.json"
    if os.path.isfile(os.path.join(ROOT, mcp_rel)):
        data6, err6 = load_json(mcp_rel)
        if data6 is not None:
            _scan_mcp(data6, "", mcp_rel)

# ---- Report -----------------------------------------------------------

if problems:
    print(f"FAIL — {len(problems)} structural problem(s) found:\n")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
else:
    print("PASS — marketplace.json, root plugin.json, all plugin.json "
          "skills paths, all skill cross-references and connector files are consistent.")
    sys.exit(0)
