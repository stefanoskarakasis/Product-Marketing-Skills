"""Cursor manifests mirror the Claude plugin manifests.

.cursor-plugin/marketplace.json lists the same plugins as .claude-plugin/marketplace.json,
and each plugin's .cursor-plugin/plugin.json points at skills that exist. Cursor manifests
carry no version on purpose, so a release has nothing extra to bump.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CursorManifests(unittest.TestCase):
    def test_marketplace_matches_claude_marketplace(self):
        claude = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        cursor = json.loads((ROOT / ".cursor-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(p["name"] for p in claude["plugins"]), sorted(p["name"] for p in cursor["plugins"]))
        for p in cursor["plugins"]:
            self.assertNotIn("..", p["source"])
            self.assertFalse(p["source"].startswith("/"))

    def test_each_plugin_manifest_points_at_real_skills(self):
        cursor = json.loads((ROOT / ".cursor-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        for p in cursor["plugins"]:
            d = ROOT / p["source"]
            man = json.loads((d / ".cursor-plugin" / "plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(man["name"], p["name"])
            self.assertNotIn("version", man, "Cursor manifests carry no version, so releases do not drift")
            for s in ([man["skills"]] if isinstance(man["skills"], str) else man["skills"]):
                self.assertTrue((d / s).exists(), f"{p['name']}: skills path {s} does not exist")

    def test_manifest_keys_match_cursor_schema(self):
        """cursor/plugins schemas/plugin.schema.json: author takes only name and email; no extra top-level keys."""
        allowed = {"name", "displayName", "description", "version", "minClientVersions", "author", "publisher",
                   "homepage", "repository", "license", "logo", "keywords", "category", "tags", "commands",
                   "agents", "skills", "rules", "hooks", "variables", "mcpServers"}
        for f in ROOT.glob("*/.cursor-plugin/plugin.json"):
            man = json.loads(f.read_text(encoding="utf-8"))
            self.assertLessEqual(set(man), allowed, f"{f.parent.parent.name}: key not in Cursor schema")
            self.assertLessEqual(set(man.get("author", {})), {"name", "email"},
                                 f"{f.parent.parent.name}: Cursor author allows only name and email")

    def test_shared_fields_match_claude_manifest(self):
        """A Cursor manifest says the same thing as its Claude twin, so a plugin change cannot reach one side only.

        Fields compared: name, description, license, homepage, repository, skills and author name.
        Cursor carries no version, displayName or keywords on purpose; the schema allows keywords,
        so adding them later is a choice, not a fix.
        """
        for f in sorted(ROOT.glob("*/.cursor-plugin/plugin.json")):
            d = f.parent.parent
            cursor = json.loads(f.read_text(encoding="utf-8"))
            claude = json.loads((d / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
            for key in ("name", "description", "license", "homepage", "repository", "skills"):
                self.assertEqual(cursor.get(key), claude.get(key),
                                 f"{d.name}: Cursor {key} differs from the Claude manifest. Copy it across.")
            self.assertEqual(cursor.get("author", {}).get("name"), claude.get("author", {}).get("name"),
                             f"{d.name}: Cursor author name differs from the Claude manifest")

    def test_every_claude_plugin_has_a_cursor_manifest(self):
        for f in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
            self.assertTrue((f.parent.parent / ".cursor-plugin" / "plugin.json").exists(),
                            f"{f.parent.parent.name}: no .cursor-plugin/plugin.json")


if __name__ == "__main__":
    unittest.main()
