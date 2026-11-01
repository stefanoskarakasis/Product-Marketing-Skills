#!/usr/bin/env python3
"""Move files from staged/ into their real places, turning "dot-" into ".".

Why this exists: Finder hides folders that start with a dot (.claude-plugin,
.cursor-plugin), so drag-and-drop uploads silently skip them. Upload them
under visible names instead and let this script put them back:

    staged/pmm-growth/dot-claude-plugin/plugin.json
      becomes
    pmm-growth/.claude-plugin/plugin.json

Any folder or file name that starts with "dot-" gets a "." in its place.
Files are moved (overwriting), so staged/ is empty afterwards.

Usage:  python3 scripts/apply_staged.py [repo_root]
"""
import sys
from pathlib import Path


def target_of(rel: Path) -> Path:
    parts = [("." + p[4:]) if p.startswith("dot-") and len(p) > 4 else p for p in rel.parts]
    return Path(*parts)


def apply(root: Path) -> list:
    staged = root / "staged"
    moved = []
    if not staged.is_dir():
        return moved
    for src in sorted(p for p in staged.rglob("*") if p.is_file()):
        rel = src.relative_to(staged)
        if rel.name.lower() == "readme.md" and len(rel.parts) == 1:
            continue
        dest = root / target_of(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        src.unlink()
        moved.append(str(target_of(rel)))
    for d in sorted((p for p in staged.rglob("*") if p.is_dir()), reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass
    return moved


if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    done = apply(root)
    print(f"Moved {len(done)} file(s) out of staged/.")
    for m in done:
        print("  " + m)
