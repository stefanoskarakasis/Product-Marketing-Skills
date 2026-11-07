"""Directory policy preflight for pmm-positioning.

The Claude plugin directory refuses a version when a skill, command, agent or output style
carries a frontmatter key outside its allowed list (error LOCAL_CODE_FRONTMATTER_KEY), unless
the organization is Verified. Each refused version costs a scheduled-check cycle, so this test
runs the same check before you push. Widen ALLOWED only after reading the directory docs.
Internal metadata (version, context, quality_gate, last_updated) lives in skills.meta.json.
"""
import re
import unittest
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent / "pmm-positioning"
ALLOWED = {"name", "description"}


def frontmatter_lines(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1).split("\n") if m else []


class TestDirectoryFrontmatter(unittest.TestCase):
    def test_only_allowed_keys_and_no_nesting(self):
        files = list(PLUGIN.glob("skills/*/SKILL.md")) + list(PLUGIN.glob("commands/*.md"))
        self.assertTrue(files, "no skill or command files found")
        bad = []
        for f in files:
            in_block = False
            for line in frontmatter_lines(f.read_text(encoding="utf-8")):
                if not line.strip():
                    continue
                if line.startswith((" ", "\t", "-")):
                    if not in_block:  # folded or literal scalar continuation is fine
                        continue
                    bad.append(f"{f.relative_to(PLUGIN)}: nested value under a key")
                    continue
                key = line.split(":", 1)[0].strip()
                in_block = line.rstrip().endswith(":") and not line.rstrip().endswith((">:", "|:"))
                if key not in ALLOWED:
                    bad.append(f"{f.relative_to(PLUGIN)}: key '{key}' is not in the allowed list")
        self.assertEqual(bad, [], "Frontmatter the directory will refuse. Move it to skills.meta.json.")

    def test_privacy_policy_url_set(self):
        import json
        manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest.get("privacyPolicyUrl", "").startswith("https://"))


if __name__ == "__main__":
    unittest.main()
