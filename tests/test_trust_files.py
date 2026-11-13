"""Trust files exist: security policy, conduct, issue forms and a pull request template."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestTrustFiles(unittest.TestCase):
    def test_security_policy_says_no_credentials(self):
        text = (ROOT / "SECURITY.md").read_text(encoding="utf-8").lower()
        self.assertIn("no credentials", text)
        self.assertIn("report a vulnerability", text)

    def test_code_of_conduct_exists(self):
        self.assertTrue((ROOT / "CODE_OF_CONDUCT.md").is_file())

    def test_issue_forms_and_pr_template(self):
        gh = ROOT / ".github"
        for f in ("PULL_REQUEST_TEMPLATE.md", "ISSUE_TEMPLATE/config.yml", "ISSUE_TEMPLATE/bug.yml", "ISSUE_TEMPLATE/skill-request.yml"):
            self.assertTrue((gh / f).is_file(), f".github/{f} is missing")

    def test_connect_doc_starts_read_only(self):
        text = (ROOT / "docs" / "connect-your-tools.md").read_text(encoding="utf-8")
        self.assertIn("## Start read-only", text)


if __name__ == "__main__":
    unittest.main()
