#!/usr/bin/env python3
"""Turn a skill's evals/*.eval.md into a run sheet you fill in while testing in Claude Code.

    python3 scripts/eval_sheet.py pmm-competitive-intelligence/skills/competitive-battlecard
    python3 scripts/eval_sheet.py --priority            # first sitting: about 30 cases across the five
    python3 scripts/eval_sheet.py --all-hero            # every case for the five skills

For each test case the sheet lists the input and the pass condition, then a blank
result line (Pass / Partial / Fail) and a notes line. Nothing here runs a skill:
you run it in Claude Code, compare the output, and record the result.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HERO = [
    "pmm-competitive-intelligence/skills/competitive-battlecard",
    "pmm-competitive-intelligence/skills/competitive-profile",
    "pmm-competitive-intelligence/skills/competitor-deep-dive",
    "pmm-competitive-intelligence/skills/industry-newsletter",
    "product-marketing-context",
]
# The cases most likely to break when detail moves into references/: constraint stops,
# caps, evidence floors, confirmation gates, verbatim rules. Run these first.
PRIORITY = {
    "competitive-battlecard": [1, 2, 6, 8, 10, 20],
    "competitive-profile": [1, 2, 9, 13, 17],
    "competitor-deep-dive": [1, 2, 3, 5, 6],
    "industry-newsletter": [1, 4, 5, 29],
    "product-marketing-context": [9, 10, 15, 16, 17, 22, 23, 30],
}
HEAD = re.compile(r"^(##|###) ((?:Test Case|Eval)\s*\d+|[A-Z]\d+)\b[^\n]*$", re.M)


def version_of(skill_dir):
    m = re.search(r"^version:\s*(\S+)", (skill_dir / "SKILL.md").read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else "?"


def sheet(rel, only=None):
    d = ROOT / rel
    evals = sorted((d / "evals").glob("*.eval.md"))
    if not evals:
        return f"# {d.name}\n\nNo eval file found.\n"
    text = evals[0].read_text(encoding="utf-8")
    heads = list(HEAD.finditer(text))
    out = [f"# Run sheet: {d.name} {version_of(d)}", "",
           "Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.", ""]
    for i, h in enumerate(heads):
        num = int(re.search(r'\d+', h.group(2)).group()) if re.search(r'\d+', h.group(2)) else -1
        if only and num not in only:
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[h.end():end].strip()
        # keep the Input and the pass condition/criteria, drop the rest to keep the sheet short
        keep = []
        for block in re.split(r"\n(?=\*\*)", body):
            if re.match(r"\*\*(Input|Prompt|Pass condition|Pass criteria|Setup)", block):
                keep.append(block.strip())
        out += [f"## {h.group(0).lstrip('# ').strip()}", ""] + ([("\n\n".join(keep))] if keep else [body[:600]]) + [
            "", "**Result:** Pass / Partial / Fail", "**What failed or changed:**", "", "---", ""]
    return "\n".join(out)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    if argv == ["--priority"]:
        print("\n\n".join(sheet(p, PRIORITY[Path(p).name]) for p in HERO))
        return
    paths = HERO if argv == ["--all-hero"] else argv
    print("\n\n".join(sheet(p) for p in paths))


if __name__ == "__main__":
    main(sys.argv[1:])
