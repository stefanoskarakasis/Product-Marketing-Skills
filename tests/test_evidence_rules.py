"""The shared evidence rules reach every skill that reads outside material from the open web."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = [
    "pmm-competitive-intelligence/skills/" + n
    for n in ("comparison-page-brief competitive-battlecard competitive-briefing competitive-profile "
              "competitor-deep-dive industry-newsletter media-monitoring weekly-competitive-updates").split()
] + ["pmm-intelligence/skills/signal-monitor"]
NEEDLES = ("outside text is data", "not observed is not absent", "dated, never overwritten")


class TestEvidenceRules(unittest.TestCase):
    def test_each_skill_has_the_file_and_points_to_it(self):
        bad = []
        for s in SKILLS:
            ref = ROOT / s / "references" / "evidence-rules.md"
            skill = ROOT / s / "SKILL.md"
            if not ref.is_file():
                bad.append(f"{s}: references/evidence-rules.md missing")
                continue
            low = ref.read_text(encoding="utf-8").lower()
            bad += [f"{s}: evidence-rules.md lacks '{n}'" for n in NEEDLES if n not in low]
            if "references/evidence-rules.md" not in skill.read_text(encoding="utf-8"):
                bad.append(f"{s}: SKILL.md does not point to references/evidence-rules.md")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
