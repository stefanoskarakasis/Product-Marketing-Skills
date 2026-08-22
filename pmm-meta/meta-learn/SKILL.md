---
name: meta-learn
version: 3.0.0
description: >
  Captures what a completed skill session actually taught you — asks three
  extraction questions (what surprised you, what was wrong, what was missing),
  turns real answers into specific, falsifiable pattern statements, and logs
  the session to /context/skill-sessions.md so meta-synthesis can detect
  repeats later. Trigger on: "capture what we learned", "log this session",
  "save the learnings", "what did we learn", or any request to encode
  insights from a completed skill session.
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-08-22
---

# meta-learn

Closes out a completed skill session by asking what it actually taught the
user — not what the skill's output said, but what surprised them, what they
disagreed with, or what was missing. Turns real answers into a specific,
falsifiable statement and logs the session. That log is the only input
`meta-synthesis` reads to detect patterns across sessions later — this skill
exists to make sure that log has something worth reading.

## Trigger

- **When:** A skill session just produced output and is closing — right
  after a brief, positioning statement, retro, or any other skill's output
  is delivered and the user is ready to move on.

- **Not for:** Auditing a `SKILL.md`'s structure → use `meta-review`.
  Checking whether a skill's output itself is correct → use `meta-verify`.
  Detecting patterns across multiple sessions or proposing guardrails → use
  `meta-synthesis`, which reads what this skill logs.

- **Example prompts:**
  - "Capture what we learned from that retro"
  - "Log this session"
  - "What surprised you about that positioning run?"
  - "Save the learnings before we close"

## Inputs

- **Args:** The completed session's skill name and a short description of
  its output. `n.v.t.` if invoked immediately after a skill session in the
  same conversation — infer both from context.
- **Defaults:** If the skill name isn't obvious, ask for it before proceeding.
- **Context keys:** `/context/skill-sessions.md` — appended to, created if
  it doesn't exist yet.

## Pre-flight

- This skill is context-agnostic. Do not load `/foundation/brain.md` and do
  not let prior company context shape what counts as a pattern — extraction
  comes from the user's answers alone.
- If there's no completed session to close out (skill hasn't produced output
  yet), stop and say so — this isn't a mid-session check-in.

## Steps

### Step 1: Confirm the Session Closed

Confirm which skill just ran and what it produced, in one line:

> "Closing out [skill-name] — produced [one-line description of output].
> Three quick questions before we log this."

### Step 2: Ask the Three Extraction Questions

Ask all three in one message. Wait for complete answers before proceeding.

> "1. **What surprised you?** Something unexpected the skill surfaced that
> you hadn't considered.
>
> 2. **What was wrong or off?** Any recommendation you pushed back on or
> felt missed the mark. Be specific: what, and why?
>
> 3. **What was missing?** Context the skill didn't have, a question it
> didn't ask, an output it should have produced but didn't."

If all three come back as "nothing," skip to Step 5 — log a clean close, no
pattern extraction needed.

### Step 3: Make Each Answer Falsifiable

For any answer with real content, restate it as a specific, testable
statement — not a vague impression.

- ❌ Vague: "communication could be better"
- ✅ Falsifiable: "when the launch timeline slips more than 10 days, the
  brief didn't flag which stakeholders needed to be renotified"

If an answer can't be sharpened into something falsifiable, it isn't a
pattern yet — note it as a loose observation rather than forcing it into a
false-precision statement.

### Step 4: Show What Will Be Logged

Before writing, show the user the exact log entry:

```
🔁 SESSION LEARNING

Skill: [name]
Date: [date]
Pattern: [falsifiable statement, or "none — clean session"]
Source: [surprised / wrong / missing]

Log this? (yes / edit / skip)
```

Never log a pattern without this confirmation. A clean close (no pattern)
logs automatically without this gate — there's nothing to approve.

### Step 5: Append to the Session Log

Append one row to `/context/skill-sessions.md` (create the file with a
header row if it doesn't exist yet):

```yaml
skill: [name]
session_date: [YYYY-MM-DD]
pattern: [falsifiable statement, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

This is the only file this skill writes to. `meta-synthesis` is what reads
across many of these rows later to find what repeats — this skill's only
job is making sure each individual row is worth reading.

## Outputs

- **Files written:** `/context/skill-sessions.md` — one appended row per
  session, per Step 5.
- **Chat output format:** The three questions (Step 2), the falsifiable
  restatement if applicable (Step 3), and the logged-entry confirmation
  (Step 4).
- **External side effects:** n.v.t.

## Verification

- The session log entry exists in `/context/skill-sessions.md` with today's
  date and the correct skill name.
- If a pattern was captured, it's stated as a specific, falsifiable claim —
  not a vague impression.
- Nothing was written without the Step 4 confirmation, except a clean close
  with no pattern.

## Do Not Use For

- **meta-review** — auditing a `SKILL.md`'s own structure against the spec
- **meta-verify** — checking whether a skill's output itself is correct
  before it goes out
- **meta-synthesis** — detecting patterns across 2+ logged sessions and
  proposing guardrails; this skill only produces the raw log rows
  meta-synthesis later reads

## Operating Rules

- **Extract from the user's real answer, not from the skill's own output.**
  The skill already said what it produced. This is about what the user
  noticed that it didn't say.
- **Falsifiable or nothing.** A pattern statement that can't be proven wrong
  isn't useful to `meta-synthesis` later — sharpen it or log it as a loose
  observation, don't force false precision.
- **Never force a pattern.** If the user says "nothing surprised me," accept
  that and log a clean close. Don't manufacture insight to seem thorough.
- **One log, one format.** Every session appends to
  `/context/skill-sessions.md` in the same YAML shape — `meta-synthesis`
  depends on consistent structure to scan across sessions.
- **Nothing writes without the confirmation gate**, except the automatic
  clean-close log entry when there's genuinely nothing to approve.
- **This skill doesn't decide what's a repeating pattern.** That's
  `meta-synthesis`'s job, reading across many logged sessions. This skill's
  job ends at logging one session well.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| All three questions asked | Surprised / wrong / missing, in one message | Yes |
| Pattern is falsifiable | Specific claim, not a vague impression | Yes or n.v.t. (clean close) |
| Confirmation shown before write | Exact log entry shown, user confirmed | Yes or n.v.t. (clean close) |
| Log entry appended | `/context/skill-sessions.md` has the new row | Yes |
| Clean closes handled | "Nothing" answers don't force a fake pattern | Yes |
