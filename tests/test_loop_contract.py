"""A skill that runs on a schedule follows the run contract in docs/loop-contract.md."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ("Cadence", "Acts when", "Purpose", "Skills used", "Loop body", "Self-check", "State", "Stop", "Output")


class TestLoopContract(unittest.TestCase):
    def test_doc_defines_all_nine_parts(self):
        text = (ROOT / "docs" / "loop-contract.md").read_text(encoding="utf-8")
        missing = [p for p in PARTS if f"**{p}" not in text]
        self.assertEqual(missing, [], "docs/loop-contract.md must define every part")

    def test_spec_points_to_the_doc(self):
        spec = (ROOT / "SKILL-SPEC.md").read_text(encoding="utf-8")
        self.assertIn("docs/loop-contract.md", spec)
        self.assertIn("Scheduled skills", spec)


if __name__ == "__main__":
    unittest.main()
