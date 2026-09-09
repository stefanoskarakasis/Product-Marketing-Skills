# skill-sessions.md — Canonical Format

Read by every skill's own Learning Close step before writing, and by `meta-synthesis`
before parsing. This file defines the one true format — do not improvise a different
one in an individual skill.

## Format: sequential YAML blocks, not a markdown table

`/context/skill-sessions.md` is a sequence of fenced YAML blocks, appended in
chronological order, separated by a blank line. It is NOT a markdown table — despite
"row" and "header row" language used loosely in some skills' Learning Close
instructions, there is no single shared header. Each block is self-contained.

If the file doesn't exist yet, create it with this file-level header (once, not per
entry):

    # Skill Sessions Log

    Append-only. Each session is one fenced YAML block below. Do not edit prior entries.

Then append entries below that header, oldest first.

## Two entry types

Type A — execution session (written by any T1/T2 skill after Learning Close):

    type: execution
    skill: [skill-name]
    session_date: [YYYY-MM-DD]
    pattern: [one falsifiable statement, or "none"]
    source: [surprised / wrong / missing / n.v.t.]

Type B — synthesis run (written only by meta-synthesis):

    type: synthesis
    skill: meta-synthesis
    session_date: [YYYY-MM-DD]
    sessions_analyzed: [count]
    timeframe: [all / last N days]
    patterns_found:
      high_confidence: [count]
      medium_confidence: [count]
    guardrails_proposed: [count]
    guardrails_approved: [count]
    brain_updates_proposed: [count]
    brain_updates_approved: [count]

The `type` field is the only addition to either existing schema. It's what lets a
reader (a skill, or a human) tell the two apart without guessing from field names.

## For any skill writing a Type A entry

Add `type: execution` as the first field. Nothing else about your Learning Close
instructions changes.

## For meta-synthesis specifically

- When reading the log (Step 1), only process blocks where `type: execution`.
  Skip `type: synthesis` blocks — they're your own prior output, not raw material.
- When writing your own session (Step 4), use `type: synthesis` as specified above.
- This means meta-synthesis's own history is preserved in the same file (useful for
  auditing how synthesis runs have gone over time) without contaminating future
  pattern detection with its own previously-synthesized output.
