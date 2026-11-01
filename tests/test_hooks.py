"""The send-guard hook: it asks before sends, stays out of the way otherwise, and both copies match."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPIES = [ROOT / "pmm-competitive-intelligence" / "hooks", ROOT / "hooks"]


def run(tool_name, tool_input=None, env=None):
    import os
    e = {k: v for k, v in os.environ.items() if not k.startswith("PMM_GUARD")}
    e.update(env or {})
    p = subprocess.run(
        [sys.executable, "-I", str(COPIES[0] / "guard_external_send.py")],
        input=json.dumps({"tool_name": tool_name, "tool_input": tool_input or {}}),
        capture_output=True, text=True, env=e,
    )
    return p.returncode, p.stdout.strip()


class TestSendGuard(unittest.TestCase):
    def test_both_copies_identical(self):
        for name in ("guard_external_send.py", "hooks.json"):
            a, b = [(c / name).read_bytes() for c in COPIES]
            self.assertEqual(a, b, f"{name} differs between the plugin and the repo root")

    def test_hooks_json_points_at_a_real_script(self):
        for c in COPIES:
            cfg = json.loads((c / "hooks.json").read_text(encoding="utf-8"))
            cmd = cfg["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
            self.assertIn("${CLAUDE_PLUGIN_ROOT}/hooks/guard_external_send.py", cmd)
            self.assertTrue((c / "guard_external_send.py").is_file())

    def test_slack_send_asks(self):
        rc, out = run("mcp__slack__slack_send_message", {"channel": "C123", "text": "hi"})
        self.assertEqual(rc, 0)
        d = json.loads(out)["hookSpecificOutput"]
        self.assertEqual(d["permissionDecision"], "ask")
        self.assertIn("channel=C123", d["permissionDecisionReason"])

    def test_gmail_send_and_post_ask(self):
        for name in ("mcp__gmail__send_email", "mcp__claude_ai_Slack__post_message", "mcp__outlook__reply_to_email"):
            rc, out = run(name)
            self.assertIn("ask", out, name)

    def test_reading_and_drafting_never_ask(self):
        for name in ("mcp__slack__slack_read_channel", "mcp__gmail__search_threads",
                     "mcp__gmail__create_draft", "mcp__slack__get_thread_replies", "Bash", "mcp__asana__create_task"):
            rc, out = run(name)
            self.assertEqual((rc, out), (0, ""), name)

    def test_off_and_allow_switches(self):
        self.assertEqual(run("mcp__slack__send_message", env={"PMM_GUARD": "off"})[1], "")
        self.assertEqual(run("mcp__slack__send_message", env={"PMM_GUARD_ALLOW": "slack"})[1], "")
        self.assertIn("ask", run("mcp__gmail__send_email", env={"PMM_GUARD_ALLOW": "slack"})[1])

    def test_bad_input_does_nothing(self):
        p = subprocess.run([sys.executable, "-I", str(COPIES[0] / "guard_external_send.py")],
                           input="not json", capture_output=True, text=True)
        self.assertEqual((p.returncode, p.stdout.strip()), (0, ""))


if __name__ == "__main__":
    unittest.main()
