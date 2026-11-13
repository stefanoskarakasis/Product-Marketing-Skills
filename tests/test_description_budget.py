"""The skill listing has a budget: every description counts, and the budget is shared.

Claude Code sends the model a skill listing capped at roughly 30,000 characters, shared with every
other skill the user has installed. A skill past the cap shows as a bare name with no description,
so it stops triggering. coreyhaines31/marketingskills measured this on Claude Code 2.1.319
(evals/triggers/README.md in that repo) and cut its descriptions from 42,105 to 18,662 characters.

This file locks the repo under a ceiling. To add a skill, shorten another description first.
Routing reads only the name and description, so a cut must keep the "Not for" clause.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOTAL_CEILING = 20_000   # all descriptions together
ONE_CEILING = 800        # one description


def descriptions():
    out = {}
    for p in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^description:\s*(?:[>|][-+]?\s*\n((?:[ \t]+.*\n?)+)|(.+))", text, re.M)
        raw = (m.group(1) or m.group(2)) if m else ""
        out[p.parent.name] = len(" ".join(raw.split()).strip("\"'"))
    return out


class TestDescriptionBudget(unittest.TestCase):
    def test_total_is_under_the_ceiling(self):
        d = descriptions()
        total = sum(d.values())
        self.assertLessEqual(
            total, TOTAL_CEILING,
            f"{total} description characters across {len(d)} skills; ceiling {TOTAL_CEILING}. "
            "Shorten a description (keep the trigger phrases and the 'Not for' clause) before adding more.",
        )

    def test_no_single_description_is_long(self):
        over = [f"{n}: {c}" for n, c in descriptions().items() if c > ONE_CEILING]
        self.assertEqual(over, [], f"description over {ONE_CEILING} characters")

    def test_every_skill_has_a_description(self):
        self.assertEqual([n for n, c in descriptions().items() if c < 40], [])


if __name__ == "__main__":
    unittest.main()
