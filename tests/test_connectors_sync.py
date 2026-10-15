"""Connector catalog checks.

connectors.json is the single source of truth for which connector servers
each plugin ships. These tests fail if a generated file (a .mcp.json, a
connector list or table) has drifted from it, or if the catalog could leak
a credential. Fix drift with:
    python3 scripts/generate_connectors.py --write
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "generate_connectors.py"
CATALOG = ROOT / "connectors.json"


class ConnectorCatalog(unittest.TestCase):
    def test_generated_files_match_catalog(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_brain_plugin_wires_every_server(self):
        cat = json.loads(CATALOG.read_text(encoding="utf-8"))
        brain = json.loads((ROOT / cat["foundation"] / ".mcp.json").read_text(encoding="utf-8"))["mcpServers"]
        for s in cat["servers"]:
            self.assertIn(s["name"], brain, f"{s['name']} is missing from the {cat['foundation']} .mcp.json")
        for p in cat["plugins"]:
            mine = json.loads((ROOT / p / ".mcp.json").read_text(encoding="utf-8"))["mcpServers"]
            self.assertTrue(set(mine) <= set(brain), f"{p} wires a server the brain plugin does not")

    def test_every_wired_category_is_listed_in_plugin_connectors(self):
        cat = json.loads(CATALOG.read_text(encoding="utf-8"))
        for p in cat["plugins"]:
            text = (ROOT / p / "CONNECTORS.md").read_text(encoding="utf-8")
            for s in cat["servers"]:
                if p == cat["foundation"] or p in s.get("plugins", []):
                    for c in [x.strip() for x in s["category"].split(",")]:
                        self.assertIn(f"`~~{c}`", text,
                                      f"{p}/CONNECTORS.md needs a row for `~~{c}` ({s['name']} is wired there)")

    def test_root_mcp_json_has_every_server(self):
        cat = json.loads(CATALOG.read_text(encoding="utf-8"))
        root = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))["mcpServers"]
        self.assertEqual(sorted(root), sorted(s["name"] for s in cat["servers"]))
        for name, cfg in root.items():
            self.assertEqual(sorted(cfg), ["type", "url"], f"{name}: only type and url are allowed in .mcp.json")

    def test_catalog_has_no_secrets(self):
        raw = CATALOG.read_text(encoding="utf-8").lower()
        for bad in ("api_key", "apikey", "bearer ", "authorization", "client_secret", "password", "token="):
            self.assertNotIn(bad, raw, f"connectors.json must not contain '{bad}'")


if __name__ == "__main__":
    unittest.main()
