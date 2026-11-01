#!/usr/bin/env python3
"""Print one or more sections of the brain, so an agent reads only what it needs.

Usage:
    python3 brain_section.py 3
    python3 brain_section.py 1,4,6
    python3 brain_section.py 3 --brain path/to/brain.md

Finds the brain at foundation/brain.md (or brain.md) when --brain is not given.
Plain Python 3, no installs. Generated copies live in foundation/tools/.
"""
import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^##\s+Section\s+(\d+)\s*:\s*(.*)$")
ANY_H2 = re.compile(r"^##\s+")


def find_brain(arg):
    candidates = [Path(arg)] if arg else [Path("foundation/brain.md"), Path("brain.md")]
    for c in candidates:
        if c.is_file():
            return c
    return None


def sections(text):
    """Return {number: (name, body_lines)} for every '## Section N:' block."""
    out, current = {}, None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            current = int(m.group(1))
            out[current] = (m.group(2).strip(), [line])
        elif ANY_H2.match(line):
            current = None
        elif current is not None:
            out[current][1].append(line)
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="Print brain sections.")
    p.add_argument("numbers", help="Section number or comma list, e.g. 3 or 1,4,6")
    p.add_argument("--brain", help="Path to brain.md")
    a = p.parse_args(argv)

    brain = find_brain(a.brain)
    if brain is None:
        print("No brain found. Run the product-marketing-context skill first.", file=sys.stderr)
        return 2
    try:
        wanted = [int(n) for n in a.numbers.split(",") if n.strip()]
    except ValueError:
        print("Section numbers must be digits, for example 3 or 1,4,6.", file=sys.stderr)
        return 2

    found = sections(brain.read_text(encoding="utf-8"))
    missing = [n for n in wanted if n not in found]
    for n in wanted:
        if n in found:
            print("\n".join(found[n][1]).rstrip() + "\n")
    if missing:
        print("Not in this brain: Section " + ", ".join(map(str, missing)), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
