---
name: meta-verify
version: 3.0.0
description: >
  Runs a second-pass quality check on a skill's output before it goes out —
  re-checks it against the originating skill's own Quality Gate and
  Operating Rules, and returns specific fixes rather than a pass/fail
  verdict alone. Trigger on: "verify this", "check this before I send it",
  "second-pass this brief", "did that pass quality gate", or any request to
  re-check a skill's output before it's delivered externally.
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-08-22
---

# meta-verify

A second pair of eyes on a skill's output, applying the exact standard the
originating skill already committed to — its own `## Quality Gate` table and
`## Operating Rules`. Catches what the first pass missed, especially when
the same session that produced the output is also the one that's about to
mark it done.

This isn't a second opinion using a different, invented rubric — it's a
faithful re-application of the standard that skill already declared for
itself. If a skill's own Quality Gate is weak, that's a `meta-review`
finding against that skill's `SKILL.md`, not something this skill
compensates for by inventing its own scoring.

## Trigger

- **When:** A skill has produced output and it's about to be delivered
  externally (sent to sales, shared with leadership, published) — a second
  pass before it leaves the building.

- **Not for:** Auditing a `SKILL.md`'s own structure → use `meta-review`.
  Extracting learnings from a completed session → use `meta-learn`.
  Detecting patterns across sessions → use `meta-synthesis`.

- **Example prompts:**
  - "Check this positioning brief before I send it"
  - "Verify the last GTM strategy output"
  - "Did this retro actually pass its own quality gate?"
  - "Second-pass this before it goes to leadership"

## Inputs

- **Args:** The output to verify, and which skill produced it. `n.v.t.` if
  invoked immediately after that skill's own session — infer both from
  context.
- **Defaults:** If the originating skill isn't obvious from the output
  itself, ask.
- **Context keys:** The originating skill's own `SKILL.md` — specifically
  its `## Quality Gate` and `## Operating Rules` sections. No brain context
  needed beyond what the originating skill itself required.

## Pre-flight

- Load the originating skill's `SKILL.md`. If it doesn't exist or doesn't
  declare `quality_gate: true`, say so — there's no standard to re-check
  against, and this skill isn't the place to invent one on the spot.
- This skill is context-agnostic. It applies the originating skill's own
  declared standard; it does not load `/foundation/brain.md` independently.

## Steps

### Step 1: Load the Originating Standard

Read the originating skill's `## Quality Gate` table and `## Operating
Rules` in full. These are the only standard this pass applies — not a
generic rubric, not this skill's own opinion of what "good" looks like.

### Step 2: Re-run Every Quality Gate Check

For each row in the originating skill's Quality Gate table, check the actual
output against it independently — don't trust that the first pass marked it
correctly. Mark each pass/fail with the specific evidence.

```markdown
## Second-Pass Verification — [skill-name] output

| Check (from [skill-name]'s own Quality Gate) | Pass? | Evidence |
|---|---|---|
| [Check name] | ✅ / ❌ | [Specific quote or observation] |
```

### Step 3: Spot-Check Operating Rules

Operating Rules aren't a checklist — they're standing constraints. Scan the
output against each rule from the originating skill and flag any it appears
to violate, even if the Quality Gate table doesn't have a matching row for
it.

### Step 4: Report

```markdown
## meta-verify — [skill-name] output

**Quality Gate:** [N]/[total] passed
**Operating Rules:** [clean / N flagged]

### Failed checks
- [Check] — [specific evidence of the gap, and what would fix it]

### Rule flags
- [Rule] — [where the output appears to violate it]

### Verdict
[CLEARS SECOND PASS / NEEDS FIXES BEFORE DELIVERY] — [one sentence]
```

If everything passes, say so plainly. Don't invent soft findings to seem
thorough — a clean pass is a legitimate, useful result.

## Outputs

- **Files written:** n.v.t. — this skill produces a report only.
- **Chat output format:** The verification report from Step 4.
- **External side effects:** n.v.t.

## Verification

- Every row of the originating skill's actual Quality Gate table was
  re-checked, not assumed passed from the first run.
- Operating Rules were scanned even where no Quality Gate row corresponds
  to them.
- Every failed check has specific evidence, not a generic "doesn't meet
  standard."

## Do Not Use For

- **meta-review** — when the task is auditing the *skill file itself*
  (`SKILL.md` structure) rather than one piece of output it produced
- **meta-learn** — when the task is capturing what the session taught the
  user, not re-checking output correctness
- **meta-synthesis** — when the task is finding a pattern across multiple
  sessions, not a single output's quality

## Operating Rules

- **Apply the originating skill's own standard — never a substitute one.**
  This skill has no independent rubric. If the originating skill's Quality
  Gate is thin, that's a finding for `meta-review` against that skill, not
  something to paper over here with invented criteria.
- **Re-check independently, don't trust the first pass.** The value of a
  second pass is that it doesn't inherit the first pass's blind spots.
- **Evidence, not adjectives.** Every fail cites the specific text or gap —
  "positioning statement absent" not "positioning could be stronger."
- **Operating Rules matter even without a matching gate row.** A skill's
  rules are binding regardless of whether its own Quality Gate table
  happens to test each one.
- **A clean pass is a real result.** Don't manufacture findings to justify
  having run. If nothing failed, report that plainly.
- **No skill has a quality gate → no verification possible.** If
  `quality_gate: false` or the section is missing, say clearly that there's
  no standard to check against rather than inventing one.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Originating skill loaded | `SKILL.md` and its own Quality Gate read before scoring | Yes |
| Every gate row re-checked | No row skipped or assumed from first pass | Yes |
| Operating Rules scanned | Checked even without a matching gate row | Yes |
| Evidence specific | Every fail cites the actual gap, not a vague label | Yes |
| Verdict stated plainly | Clear pass/needs-fixes call, not just a score | Yes |
