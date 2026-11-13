"""Shape checks for evals/triggers/prompts.json: every skill has its three prompts.

The prompts are for checking, by hand or with a runner, that the right skill answers. This test
cannot tell you how Claude routes. It only guarantees the set stays complete as skills are added.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "evals" / "triggers" / "prompts.json").read_text(encoding="utf-8"))
KINDS = {"direct", "indirect", "near-miss"}


def skill_names():
    return {p.parent.name for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts}


class TestTriggerPrompts(unittest.TestCase):
    def test_every_skill_has_one_of_each_kind(self):
        have = {}
        for row in DATA["prompts"]:
            have.setdefault(row["skill"], []).append(row["kind"])
        missing = [f"{s}: {sorted(KINDS - set(have.get(s, [])))}" for s in sorted(skill_names()) if set(have.get(s, [])) != KINDS]
        self.assertEqual(missing, [], "each skill needs one direct, one indirect and one near-miss prompt")

    def test_no_unknown_skill_and_no_duplicate_rows(self):
        names = skill_names()
        self.assertEqual([r["skill"] for r in DATA["prompts"] if r["skill"] not in names], [])
        keys = [(r["skill"], r["kind"]) for r in DATA["prompts"]]
        self.assertEqual(len(keys), len(set(keys)))

    def test_expectations_make_sense(self):
        names, bad = skill_names(), []
        for r in DATA["prompts"]:
            if r["kind"] == "near-miss":
                if r["skill"] in r["expect"] or not r["expect"] or any(e not in names for e in r["expect"]):
                    bad.append(f"{r['skill']} near-miss")
            elif r["expect"] != [r["skill"]]:
                bad.append(f"{r['skill']} {r['kind']}")
        self.assertEqual(bad, [])

    def test_prompts_carry_their_own_material(self):
        bad = [r["prompt"][:50] for r in DATA["prompts"] + DATA["non_pmm"] if len(r["prompt"]) < 25 or "[" in r["prompt"] or "TODO" in r["prompt"]]
        self.assertEqual(bad, [], "a prompt with a placeholder makes the model ask for the material and scores as a miss")
        every = [r["prompt"] for r in DATA["prompts"] + DATA["non_pmm"]]
        self.assertEqual(len(every), len(set(every)), "duplicate prompt text")

    def test_non_pmm_prompts_expect_no_skill(self):
        self.assertGreaterEqual(len(DATA["non_pmm"]), 10)
        self.assertTrue(all(r["expect"] == [] for r in DATA["non_pmm"]))


if __name__ == "__main__":
    unittest.main()
