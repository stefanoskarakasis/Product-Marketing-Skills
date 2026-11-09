"""Counts written in prose must match what is on disk.

test_consistency.py checks the "## Available Skills (N Total)" header and each
plugin README's section headers. This file checks the sentences around them:
"47 skills", "47 workflows", "55 commands" and "Ten plugins" in README.md,
QUICK-START.md and AGENTS.md. Standard library only.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
FILES = ["README.md", "QUICK-START.md", "AGENTS.md"]


def skills_on_disk():
    skip = {".git", "tests", "examples", "docs"}
    return sum(1 for p in ROOT.rglob("SKILL.md")
               if not skip & set(p.relative_to(ROOT).parts))


def commands_on_disk():
    return len(list(ROOT.glob("*/commands/*.md")))


def plugins_on_disk():
    return sum(1 for p in ROOT.iterdir()
               if p.is_dir() and (p / ".claude-plugin" / "plugin.json").is_file())


class TestProseCounts(unittest.TestCase):
    def test_skill_counts(self):
        want = skills_on_disk()
        for name in FILES:
            text = (ROOT / name).read_text(encoding="utf-8")
            for m in re.finditer(r"\b(\d+) (?:skills|workflows)\b", text):
                self.assertEqual(int(m.group(1)), want,
                                 f"{name}: '{m.group(0)}' but {want} skills are on disk")

    def test_command_counts(self):
        want = commands_on_disk()
        for name in FILES:
            text = (ROOT / name).read_text(encoding="utf-8")
            for m in re.finditer(r"\b(\d+) commands\b", text):
                self.assertEqual(int(m.group(1)), want,
                                 f"{name}: '{m.group(0)}' but {want} commands are on disk")

    def test_plugin_counts(self):
        want = plugins_on_disk()
        for name in FILES:
            text = (ROOT / name).read_text(encoding="utf-8")
            for m in re.finditer(r"\b(\d+|[A-Za-z]+) plugins\b", text, re.I):
                raw = m.group(1).lower()
                n = int(raw) if raw.isdigit() else WORDS.get(raw)
                if n is None:
                    continue  # e.g. "other plugins"
                self.assertEqual(n, want,
                                 f"{name}: '{m.group(0)}' but {want} plugins are on disk")


if __name__ == "__main__":
    unittest.main()
