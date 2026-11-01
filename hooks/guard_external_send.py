#!/usr/bin/env python3
"""PreToolUse hook: ask the user before anything is sent to a person or a channel.

The skills already say "show the draft and wait for the user's yes". A skill is only
an instruction, and an agent can skip an instruction. This hook is the lock: when a
connector tool looks like it sends, posts, replies to or forwards a message through
Slack, Gmail, Outlook, Teams or similar, Claude Code stops and asks you first.

It never blocks reading, searching or drafting. It only adds a confirmation.

Settings (environment variables):
    PMM_GUARD=off              turn the guard off completely
    PMM_GUARD_ALLOW=slack,gmail   do not ask for these services (for example for a
                                  scheduled run you have already approved)

Plain Python 3, no installs. Any error means "do nothing": the guard never breaks a run.
"""
import json
import os
import re
import sys

SERVICES = ("slack", "gmail", "mail", "outlook", "teams", "discord", "whatsapp", "sms")
SEND_WORDS = re.compile(r"(?:^|[_\-\s])(send|post|reply|forward|publish|broadcast)(?:$|[_\-\s])", re.I)
SCHEDULE = re.compile(r"schedule[_\-]?(message|send|email|post)", re.I)
WHERE_KEYS = ("channel", "channel_id", "to", "recipient", "recipients", "cc", "thread_ts", "subject")


def service_of(tool_name):
    low = tool_name.lower()
    for s in SERVICES:
        if s in low:
            return "gmail" if s in ("mail",) else s
    return None


def looks_like_send(tool_name):
    return bool(SEND_WORDS.search(tool_name) or SCHEDULE.search(tool_name))


def where(tool_input):
    if not isinstance(tool_input, dict):
        return ""
    bits = []
    for k in WHERE_KEYS:
        v = tool_input.get(k)
        if v:
            bits.append(f"{k}={str(v)[:60]}")
    return ", ".join(bits)


def decide(event, env):
    if env.get("PMM_GUARD", "").lower() == "off":
        return None
    name = str(event.get("tool_name", ""))
    svc = service_of(name)
    if not svc or not looks_like_send(name):
        return None
    allowed = {x.strip().lower() for x in env.get("PMM_GUARD_ALLOW", "").split(",") if x.strip()}
    if svc in allowed:
        return None
    detail = where(event.get("tool_input"))
    reason = (
        f"PMM guard: this would send a message through {svc} ({name})"
        + (f" [{detail}]" if detail else "")
        + ". Nothing leaves your company until you say yes. "
        "To stop these questions, set PMM_GUARD_ALLOW or PMM_GUARD=off."
    )
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }


def main():
    try:
        event = json.load(sys.stdin)
        out = decide(event, os.environ)
        if out:
            print(json.dumps(out))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
