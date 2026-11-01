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


def _skip(rel: Path) -> bool:
    return rel.parts[0] in (".git", "node_modules") or "__pycache__" in rel.parts


def apply(root: Path) -> list:
    """Move every file under staged/ AND any stray file whose path has a
    "dot-" folder or file name (for example a staged folder dragged in
    without its "staged" parent) to the dotted path."""
    moved = []
    for src in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = src.relative_to(root)
        if _skip(rel):
            continue
        in_staged = rel.parts[0] == "staged"
        body = Path(*rel.parts[1:]) if in_staged else rel
        if in_staged and len(rel.parts) == 1:
            continue
        if in_staged and len(rel.parts) == 2 and rel.name.lower() == "readme.md":
            continue
        has_dot = any(p.startswith("dot-") and len(p) > 4 for p in body.parts)
        if not (in_staged or has_dot):
            continue
        dest = root / target_of(body)
        if dest == src:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        src.unlink()
        moved.append(str(target_of(body)))
    for d in sorted((p for p in root.rglob("*") if p.is_dir() and not _skip(p.relative_to(root))), reverse=True):
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
