"""SKILL-SPEC v3.0.0: every skill has the core sections and stays inside the word budget."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUDGET = 3000
LINE_LIMIT = 500

# Skills that were over budget when v3.0.0 landed. A ceiling may only go DOWN.
# When a skill is slimmed under BUDGET, delete its line: the test fails if a
# listed skill is already inside the budget, so the list can only shrink.
LEGACY_CEILING = {}


# Pre-spec layout (Five jobs / Route first / Workflow) with no core sections and no version.
# Named here so it is visible, not silently skipped. Fix: restructure under the core sections.
CORE_EXEMPT = set()


def skills():
    for p in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in p.parts:
            continue
        name = p.parent.name if p.parent.parent.name == "skills" else p.parent.name
        yield name, p, p.read_text(encoding="utf-8")


def frontmatter_flag(text, key):
    m = re.search(rf"^\s*{key}:\s*(\S+)", text, re.M)
    return m.group(1).lower() if m else None


class TestSkillSize(unittest.TestCase):
    def test_word_budget_with_legacy_ceilings(self):
        over = []
        for name, p, text in skills():
            words = len(text.split())
            limit = LEGACY_CEILING.get(name, BUDGET)
            if words > limit:
                over.append(f"{name}: {words} words, limit {limit}")
        self.assertEqual(over, [], "Skill over its word budget. Move detail to references/ (SKILL-SPEC Section 2).")

    def test_legacy_list_only_shrinks(self):
        stale = [n for n, p, t in skills() if n in LEGACY_CEILING and len(t.split()) <= BUDGET]
        self.assertEqual(stale, [], "Skill is inside the budget now: delete it from LEGACY_CEILING.")
        names = {n for n, p, t in skills()}
        self.assertEqual([n for n in LEGACY_CEILING if n not in names], [], "LEGACY_CEILING names a skill that does not exist.")

    def test_line_limit(self):
        over = [f"{n}: {t.count(chr(10))} lines" for n, p, t in skills() if t.count("\n") > LINE_LIMIT]
        self.assertEqual(over, [])

    def test_core_sections_present(self):
        bad = []
        for name, p, text in skills():
            if name in CORE_EXEMPT:
                continue
            heads = set(re.findall(r"^## (.+?)\s*$", text, re.M))
            need = ["Trigger", "Inputs", "Steps", "Outputs"]
            if frontmatter_flag(text, "quality_gate") == "true":
                need.append("Quality Gate")
            for h in need:
                if not any(x == h or x.startswith(h) for x in heads):
                    bad.append(f"{name}: missing ## {h}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
