"""Every plugin command carries the frontmatter the docs promise.

Rule (AGENTS.md, CONTRIBUTING.md): a command has `description`, plus
`argument-hint` when it takes arguments. pmm-positioning is the exception: the plugin
directory refuses extra frontmatter keys there, and test_directory_frontmatter.py
guards that. A command that takes no arguments goes on NO_ARGS. Standard library only.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRECTORY_PLUGINS = {"pmm-positioning"}
NO_ARGS = {
    "product-marketing-context/commands/agents-map.md",
    "product-marketing-context/commands/brain-gaps.md",
    "product-marketing-context/commands/my-context.md",
}


def keys(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return set()
    return {ln.split(":", 1)[0].strip() for ln in m.group(1).split("\n")
            if ln and not ln.startswith((" ", "\t", "-")) and ":" in ln}


def commands():
    return sorted(ROOT.glob("*/commands/*.md"))


class TestCommandFrontmatter(unittest.TestCase):
    def test_found_commands(self):
        self.assertTrue(commands(), "no commands found")

    def test_description_everywhere(self):
        bad = [str(p.relative_to(ROOT)) for p in commands() if "description" not in keys(p)]
        self.assertEqual(bad, [], "commands without a description")

    def test_argument_hint_outside_directory_plugins(self):
        bad = []
        for p in commands():
            rel = p.relative_to(ROOT).as_posix()
            if p.parts[-3] in DIRECTORY_PLUGINS or rel in NO_ARGS:
                continue
            if "argument-hint" not in keys(p):
                bad.append(rel)
        self.assertEqual(bad, [], "commands without argument-hint. Add one, or list the "
                                  "command in NO_ARGS if it takes no arguments")

    def test_no_args_list_is_current(self):
        for rel in NO_ARGS:
            self.assertTrue((ROOT / rel).is_file(), f"NO_ARGS lists {rel}, which does not exist")
            self.assertNotIn("argument-hint", keys(ROOT / rel),
                             f"{rel} has an argument-hint, so remove it from NO_ARGS")


if __name__ == "__main__":
    unittest.main()
