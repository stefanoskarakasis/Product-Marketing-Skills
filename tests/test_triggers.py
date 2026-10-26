"""Trigger collision checks for the Product-Marketing-Skills repo.

Run manually with:
    python3 -m unittest tests/test_triggers.py -v

Claude chooses a skill from its name and description only. The body (including
"Do Not Use For") is read after the choice, so overlap has to be removed in the
description. This file is a lexical guard, not a model of how Claude routes:
it catches the collisions a script can catch, and `docs/routing-checks.md` is
the by-hand battery for the rest.

What this locks in:
- no quoted trigger phrase is claimed by two skills;
- inside the competitive family, no skill's phrase is a word-subset of another
  skill's phrase (a short phrase hidden inside a longer one is claimed by both);
- no skill claims a generic phrase that belongs to nobody
  ("competitive update", "competitive brief", "what are our competitors doing");
- every competitive-family description has a "Not for" clause naming the
  skill a request would belong to instead;
- every competitive-family skill opens Pre-flight with a Route check.
"""

import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FAMILY = {
    "competitive-briefing", "competitive-profile", "competitive-battlecard",
    "competitor-deep-dive", "signal-monitor",
}
FAMILY_WIDE = FAMILY | {"alternatives-map", "workflow-orchestrator"}

# phrases no skill may claim as a trigger: they fit several skills equally
GENERIC = {
    "competitive update", "competitor update", "competitive brief",
    "competitive briefing", "competitive newsletter", "ci update", "ci report",
    "what are our competitors doing", "competitive landscape update",
}

STOP = set(
    "the a an of to for and or on in is are we our us my me i you your what how "
    "do does with about this that it be as at by from build make give show".split()
)


def skills():
    out = {}
    for path in ROOT.rglob("SKILL.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        fm = m.group(1)
        d = re.search(r"^description:\s*>?\s*\n?(.*?)(?=^\w+:|\Z)", fm, re.S | re.M)
        if not d:
            continue
        desc = " ".join(d.group(1).split())
        out[path.parent.name] = {
            "desc": desc,
            "phrases": [p.strip().lower() for p in re.findall(r'"([^"]{4,90})"', desc)],
            "body": text,
        }
    return out


def tokens(phrase):
    return {w for w in re.findall(r"[a-z0-9]+", phrase.lower()) if w not in STOP}


class TestTriggerCollisions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills()

    def test_family_skills_found(self):
        for name in FAMILY:
            self.assertIn(name, self.skills, f"{name} not found")

    def test_no_phrase_claimed_by_two_skills(self):
        seen, bad = {}, []
        for name, s in self.skills.items():
            for p in s["phrases"]:
                key = " ".join(re.findall(r"[a-z0-9\[\]']+", p))
                if key in seen and seen[key] != name:
                    bad.append(f"'{p}' in {seen[key]} and {name}")
                seen.setdefault(key, name)
        self.assertEqual(bad, [])

    def test_no_generic_phrase_is_claimed(self):
        bad = []
        for name, s in self.skills.items():
            for p in s["phrases"]:
                if p in GENERIC:
                    bad.append(f"{name}: '{p}'")
        self.assertEqual(bad, [], "a generic phrase fits several skills; add an audience or an object")

    def test_no_subset_phrases_inside_the_family(self):
        bad = []
        items = [(n, p) for n in FAMILY_WIDE if n in self.skills for p in self.skills[n]["phrases"]]
        for (a, pa), (b, pb) in itertools.combinations(items, 2):
            if a == b:
                continue
            ta, tb = tokens(pa), tokens(pb)
            if len(ta) >= 2 and len(tb) >= 2 and (ta <= tb or tb <= ta):
                bad.append(f"{a}: '{pa}' vs {b}: '{pb}'")
        self.assertEqual(bad, [])

    def test_not_for_clause_names_the_briefing(self):
        bad = []
        for name in FAMILY - {"competitive-briefing"}:
            desc = self.skills[name]["desc"]
            if not re.search(r"Not for[^.]*competitive-briefing", desc):
                bad.append(name)
        self.assertEqual(bad, [], "description needs a 'Not for ... (competitive-briefing)' clause")

    def test_briefing_not_for_names_its_siblings(self):
        desc = self.skills["competitive-briefing"]["desc"]
        m = re.search(r"Not for(.*)$", desc)
        self.assertIsNotNone(m, "competitive-briefing description needs a 'Not for' clause")
        for sib in ("competitive-profile", "competitive-battlecard", "competitor-deep-dive", "signal-monitor"):
            self.assertIn(sib, m.group(1), f"'Not for' clause should name {sib}")

    def test_route_check_opens_pre_flight(self):
        bad = []
        for name in FAMILY:
            body = self.skills[name]["body"]
            m = re.search(r"## Pre-flight\n\n(.*?)\n", body)
            if not m or "Route check" not in m.group(1):
                bad.append(name)
        self.assertEqual(bad, [], "Pre-flight must open with a Route check bullet")


if __name__ == "__main__":
    unittest.main()
