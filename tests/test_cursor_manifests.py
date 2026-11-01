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


if __name__ == "__main__":
    unittest.main()
