"""Run from the repo root: python3 -I strip_frontmatter.py
Strips version, last_updated and the nested metadata block from every pmm-positioning
SKILL.md, removes argument-hint from every pmm-positioning command, and writes
pmm-positioning/skills.meta.json. Safe to re-run: it does nothing on a clean file."""
import json, re
from pathlib import Path

base = Path("pmm-positioning")
meta_file = base / "skills.meta.json"
meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}

for p in sorted(base.glob("skills/*/SKILL.md")):
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"No frontmatter in {p}")
    fm, out, info, i = m.group(1).split("\n"), [], {}, 0
    while i < len(fm):
        line = fm[i]
        if line.startswith("version:"):
            info["version"] = line.split(":", 1)[1].strip(); i += 1
        elif line.startswith("last_updated:"):
            info["last_updated"] = line.split(":", 1)[1].strip(); i += 1
        elif line.startswith("metadata:"):
            i += 1
            while i < len(fm) and fm[i].startswith("  "):
                k, v = fm[i].strip().split(":", 1)
                v = v.strip()
                info[k] = (v == "true") if v in ("true", "false") else v
                i += 1
        else:
            out.append(line); i += 1
    if info:  # only rewrite files that still had the keys
        p.write_text("---\n" + "\n".join(out) + "\n---\n" + text[m.end():], encoding="utf-8")
        meta[p.parent.name] = {k: info[k] for k in ("version", "author", "context", "quality_gate", "last_updated")}

meta_file.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

for p in sorted(base.glob("commands/*.md")):
    t = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"^argument-hint:.*\n", "", t, count=1, flags=re.M), encoding="utf-8")
print("done")
