"""Shape checks for evals/triggers/heldout.json and the run sheet built from the prompt files.

The held-out set is not blind (see its readme). These tests keep it complete, self-contained and
free of copied trigger phrases. They cannot tell you how Claude routes.
"""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HELD = json.loads((ROOT / "evals" / "triggers" / "heldout.json").read_text(encoding="utf-8"))
MAIN = json.loads((ROOT / "evals" / "triggers" / "prompts.json").read_text(encoding="utf-8"))
KINDS = {"situation", "judgement"}


def skill_files():
    return [p for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts]


def skill_names():
    return {p.parent.name for p in skill_files()}


def quoted_phrases():
    """Quoted trigger phrases of three or more words, taken from each description."""
    out = []
    for p in skill_files():
        m = re.search(r"^description:\s*(.+?)(?=^\w[\w-]*:|\n---)", p.read_text(encoding="utf-8"), re.M | re.S)
        text = m.group(1) if m else ""
        for q in re.findall(r"[\"“]([^\"”]{8,80})[\"”]", text):
            if len(q.split()) >= 3:
                out.append((p.parent.name, q.strip().lower().rstrip(".,")))
    return out


class TestHeldoutPrompts(unittest.TestCase):
    def test_every_skill_has_both_kinds(self):
        have = {}
        for r in HELD["prompts"]:
            have.setdefault(r["skill"], []).append(r["kind"])
        bad = [s for s in sorted(skill_names()) if sorted(have.get(s, [])) != sorted(KINDS)]
        self.assertEqual(bad, [], "each skill needs one situation and one judgement prompt")

    def test_expectations_are_real_skills(self):
        names = skill_names()
        for r in HELD["prompts"]:
            self.assertTrue(r["expect"] and all(e in names for e in r["expect"]), r["skill"])
            self.assertIn(r["kind"], KINDS)

    def test_no_duplicates_and_not_in_main_set(self):
        texts = [r["prompt"].strip().lower() for r in HELD["prompts"] + HELD["non_pmm"]]
        self.assertEqual(len(texts), len(set(texts)))
        main = {r["prompt"].strip().lower() for r in MAIN["prompts"] + MAIN["non_pmm"]}
        self.assertEqual(set(texts) & main, set())

    def test_prompts_carry_their_own_material(self):
        for r in HELD["prompts"] + HELD["non_pmm"]:
            p = r["prompt"]
            self.assertGreaterEqual(len(p), 60, p)
            self.assertNotIn("[", p)
            self.assertNotIn("TODO", p)

    def test_non_pmm_rows(self):
        self.assertGreaterEqual(len(HELD["non_pmm"]), 10)
        self.assertTrue(all(r["expect"] == [] for r in HELD["non_pmm"]))

    def test_prompts_do_not_echo_description_phrases(self):
        phrases = quoted_phrases()
        hits = []
        for r in HELD["prompts"] + HELD["non_pmm"]:
            low = r["prompt"].lower()
            hits += [f"{r['skill']} echoes {s}: {q}" for s, q in phrases if q in low]
        self.assertEqual(hits, [])

    def test_run_sheet_is_in_sync(self):
        out = subprocess.run([sys.executable, str(ROOT / "scripts" / "routing_sheet.py"), "--stdout"],
                             capture_output=True, text=True, check=True).stdout
        self.assertEqual((ROOT / "evals" / "triggers" / "run-sheet.md").read_text(encoding="utf-8"), out,
                         "run: python3 scripts/routing_sheet.py --write")


if __name__ == "__main__":
    unittest.main()
