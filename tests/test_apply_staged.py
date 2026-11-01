import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import apply_staged  # noqa: E402


class ApplyStaged(unittest.TestCase):
    def test_dot_prefix_is_restored_and_staged_is_emptied(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            a = root / "staged" / "pmm-growth" / "dot-claude-plugin" / "plugin.json"
            b = root / "staged" / "dot-cursor-plugin" / "marketplace.json"
            for f in (a, b):
                f.parent.mkdir(parents=True)
                f.write_text("{}", encoding="utf-8")
            (root / "pmm-growth" / ".claude-plugin").mkdir(parents=True)
            (root / "pmm-growth" / ".claude-plugin" / "plugin.json").write_text("old", encoding="utf-8")
            moved = apply_staged.apply(root)
            self.assertEqual(sorted(moved), [".cursor-plugin/marketplace.json", "pmm-growth/.claude-plugin/plugin.json"])
            self.assertEqual((root / "pmm-growth" / ".claude-plugin" / "plugin.json").read_text(), "{}")
            self.assertTrue((root / ".cursor-plugin" / "marketplace.json").exists())
            self.assertFalse((root / "staged").exists() and any((root / "staged").rglob("*.json")))

    def test_stray_dot_folders_without_staged_parent_are_fixed(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            f = root / "pmm-toolkit" / "dot-cursor-plugin" / "plugin.json"
            f.parent.mkdir(parents=True)
            f.write_text("{}", encoding="utf-8")
            keep = root / "pmm-toolkit" / "README.md"
            keep.write_text("x", encoding="utf-8")
            moved = apply_staged.apply(root)
            self.assertEqual(moved, ["pmm-toolkit/.cursor-plugin/plugin.json"])
            self.assertTrue(keep.exists())
            self.assertFalse(f.exists())

    def test_no_staged_folder_is_fine(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(apply_staged.apply(Path(t)), [])


if __name__ == "__main__":
    unittest.main()
