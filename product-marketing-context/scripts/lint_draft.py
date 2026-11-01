#!/usr/bin/env python3
"""Check a draft against your brain before it goes anywhere.

Flags:
  FORBIDDEN  a phrase from Section 4 (Forbidden Phrases), a claim from Section 6
             (Forbidden Claims) or a topic from Section 8 (Prohibited) found in the draft
  NUMBER     a percentage, money figure or multiple in the draft that does not appear
             in Section 6 (Approved Metrics) or Section 1 (permitted claims)
  PLACEHOLDER a leftover [NEEDS PROOF], [NEEDS APPROVAL] or similar marker

Usage:
    python3 lint_draft.py draft.md
    python3 lint_draft.py draft.md --brain path/to/brain.md --strict

Exit code: 0 clean (warnings allowed), 1 a FORBIDDEN hit (or any hit with --strict),
2 could not run. Matching is a plain, case-insensitive text search, so read each hit
in context: a phrase allowed "in a specific feature" still shows up.
Plain Python 3, no installs. Generated copies live in foundation/tools/.
"""
import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^##\s+Section\s+(\d+)\s*:")
ANY_H2 = re.compile(r"^##\s+")
LABEL = re.compile(r"^\*\*[^*]+\*\*")
QUOTED = re.compile(r"[\"\u201c]([^\"\u201d]{2,80})[\"\u201d]")
NUMBER = re.compile(r"(?:[$\u20ac\u00a3]\s?\d[\d,.]*\s?[kKmMbB]?\b|\b\d[\d,.]*\s?(?:%|x\b|\u00d7))")
PLACEHOLDER = re.compile(r"\[(?:NEEDS[^\]]*|your [^\]]*|TBD|TODO)\]", re.I)


def find_brain(arg):
    for c in ([Path(arg)] if arg else [Path("foundation/brain.md"), Path("brain.md")]):
        if c.is_file():
            return c
    return None


def split_sections(text):
    out, cur = {}, None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            cur = int(m.group(1))
            out[cur] = []
        elif ANY_H2.match(line):
            cur = None
        elif cur is not None:
            out[cur].append(line)
    return out


def block(lines, label_regex):
    """Lines under the bold label matching label_regex, up to the next bold label."""
    grab, got = False, []
    for line in lines:
        if LABEL.match(line.strip()):
            grab = re.search(label_regex, line, re.I) is not None
            if grab:
                rest = re.sub(r"^\*\*[^*]+\*\*:?", "", line.strip()).strip()
                if rest:
                    got.append(rest)
            continue
        if grab:
            got.append(line)
    return got


def phrases(lines, bullets_first_quote=False):
    found = []
    for line in lines:
        qs = QUOTED.findall(line)
        if qs:
            found.extend(qs[:1] if bullets_first_quote else qs)
    return found


def prohibited_topics(lines):
    found = []
    for line in lines:
        found.extend(QUOTED.findall(line))
    return found


def hit_lines(draft_lines, phrase):
    rx = re.compile(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", re.I)
    return [i for i, l in enumerate(draft_lines, 1) if rx.search(l)]


def main(argv=None):
    p = argparse.ArgumentParser(description="Lint a draft against the brain.")
    p.add_argument("draft")
    p.add_argument("--brain")
    p.add_argument("--strict", action="store_true", help="exit 1 on any hit")
    a = p.parse_args(argv)

    brain = find_brain(a.brain)
    if brain is None:
        print("No brain found. Run the product-marketing-context skill first.", file=sys.stderr)
        return 2
    draft_path = Path(a.draft)
    if not draft_path.is_file():
        print(f"Draft not found: {a.draft}", file=sys.stderr)
        return 2

    secs = split_sections(brain.read_text(encoding="utf-8"))
    draft_lines = draft_path.read_text(encoding="utf-8").splitlines()

    forbidden = []
    forbidden += [("Section 4", x) for x in phrases(block(secs.get(4, []), r"forbidden"))]
    forbidden += [("Section 6", x) for x in phrases(block(secs.get(6, []), r"forbidden"), True)]
    forbidden += [("Section 8", x) for x in prohibited_topics(block(secs.get(8, []), r"prohibited"))]

    hits, warns = [], []
    seen = set()
    for src, ph in forbidden:
        if (src, ph.lower()) in seen:
            continue
        seen.add((src, ph.lower()))
        for ln in hit_lines(draft_lines, ph):
            hits.append(f'FORBIDDEN  line {ln}: "{ph}" ({src})')

    approved_text = "\n".join(
        block(secs.get(6, []), r"approved metrics") + block(secs.get(1, []), r"permitted claims")
    )
    approved_nums = {re.sub(r"\s", "", m).lower() for m in NUMBER.findall(approved_text)}
    for i, line in enumerate(draft_lines, 1):
        for m in NUMBER.findall(line):
            if re.sub(r"\s", "", m).lower() not in approved_nums:
                warns.append(f"NUMBER     line {i}: {m.strip()} is not in Section 6 approved metrics or Section 1 permitted claims")
        for m in PLACEHOLDER.findall(line):
            warns.append(f"PLACEHOLDER line {i}: {m}")

    for h in hits + warns:
        print(h)
    if not hits and not warns:
        print("Clean: no forbidden phrases, unapproved numbers or placeholders found.")
    else:
        print(f"\n{len(hits)} forbidden hit(s), {len(warns)} warning(s). Read each in context.")
    if hits or (a.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
