"""The agent map writer, the two helper scripts, and the doc counts that used to drift."""
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "product-marketing-context" / "scripts"
BRAIN = ROOT / "examples" / "example-brain.md"


def py(script, *args, cwd=None):
    return subprocess.run([sys.executable, "-I", str(SCRIPTS / script), *args],
                          capture_output=True, text=True, cwd=cwd)


def project(tmp):
    p = Path(tmp)
    (p / "foundation").mkdir()
    (p / "foundation" / "brain.md").write_text(BRAIN.read_text(encoding="utf-8"), encoding="utf-8")
    return p


class TestAgentMap(unittest.TestCase):
    def test_writes_once_then_no_op_and_keeps_user_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = project(tmp)
            (p / "AGENTS.md").write_text("# Mine\nkeep me\n", encoding="utf-8")
            (p / "CLAUDE.md").write_text("# Mine\nuse tabs\n", encoding="utf-8")
            r = py("write_agents_map.py", "--project", str(p))
            self.assertEqual(r.returncode, 0, r.stderr)
            a = (p / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("keep me", a)
            self.assertIn("<!-- pmm-skills:map start", a)
            self.assertIn("Section 8 Execution", a)
            self.assertIn("@AGENTS.md", (p / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertTrue((p / "foundation" / "tools" / "lint_draft.py").is_file())
            again = py("write_agents_map.py", "--project", str(p))
            self.assertIn("Unchanged", again.stdout)
            self.assertEqual(a, (p / "AGENTS.md").read_text(encoding="utf-8"))

    def test_map_is_short(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = project(tmp)
            py("write_agents_map.py", "--project", str(p))
            a = (p / "AGENTS.md").read_text(encoding="utf-8")
            block = a[a.index("<!-- pmm-skills:map start"):]
            self.assertLess(len(block.split()), 320)

    def test_no_brain_exits_2_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = py("write_agents_map.py", "--project", tmp)
            self.assertEqual(r.returncode, 2)
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = project(tmp)
            r = py("write_agents_map.py", "--project", str(p), "--dry-run")
            self.assertIn("Would change", r.stdout)
            self.assertFalse((p / "AGENTS.md").exists())

    def test_brain_section(self):
        r = py("brain_section.py", "6", "--brain", str(BRAIN))
        self.assertEqual(r.returncode, 0)
        self.assertIn("Forbidden Claims", r.stdout)
        self.assertNotIn("Section 5", r.stdout)
        self.assertEqual(py("brain_section.py", "9", "--brain", str(BRAIN)).returncode, 1)

    def test_lint_flags_and_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad, ok = Path(tmp) / "bad.md", Path(tmp) / "ok.md"
            bad.write_text("A seamless close. It eliminates invoice errors and saves 40%. [NEEDS PROOF]\n", encoding="utf-8")
            ok.write_text("Month-end close went 9 days to 4 days.\n", encoding="utf-8")
            r = py("lint_draft.py", str(bad), "--brain", str(BRAIN))
            self.assertEqual(r.returncode, 1)
            for needle in ('"seamless"', "40%", "[NEEDS PROOF]"):
                self.assertIn(needle, r.stdout)
            self.assertEqual(py("lint_draft.py", str(ok), "--brain", str(BRAIN)).returncode, 0)


class TestDocCounts(unittest.TestCase):
    def disk_counts(self):
        plugins = len([d for d in ROOT.iterdir() if (d / ".claude-plugin" / "plugin.json").is_file()])
        skills = len([p for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts])
        schema = (ROOT / "product-marketing-context" / "references" / "brain-schema.md").read_text(encoding="utf-8")
        sections = len(set(re.findall(r"^\|\s*(\d+)\s*\|", schema, re.M)))
        return plugins, skills, sections

    def test_agents_md_counts_match_disk(self):
        plugins, skills, sections = self.disk_counts()
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(f"{skills} skills in {plugins} plugins", text)
        self.assertIn(f"the brain has {sections} sections", text)

    def test_quick_start_count_matches_disk(self):
        plugins, skills, _ = self.disk_counts()
        text = (ROOT / "QUICK-START.md").read_text(encoding="utf-8")
        self.assertIn(f"{skills} skills across {plugins} plugins", text)

    def test_claude_md_is_only_the_import(self):
        self.assertEqual((ROOT / "CLAUDE.md").read_text(encoding="utf-8").strip(), "@AGENTS.md")


if __name__ == "__main__":
    unittest.main()
