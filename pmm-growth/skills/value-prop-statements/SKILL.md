---
name: value-prop-statements
version: 1.0.0
description: >
  Fans an existing positioning statement out into segment- and
  channel-specific value-prop copy variants for marketing, sales, and
  onboarding — fast iteration on already-set positioning, not a new
  positioning process. Trigger with "write value prop statements for
  [segment]", "adapt our positioning for [channel]", "sales copy for
  this persona", or any request for segment-specific messaging variants
  once a canonical positioning statement already exists.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-01
---

# Value Prop Statements

## How This Works

`positioning-messaging` builds the canonical positioning statement once,
through a full 6-phase Dunford process — that's expensive, deliberate,
and shouldn't be re-run every time a new segment or channel needs copy.
This skill is the fast sibling: it takes that already-set positioning
(or brain Section 3's alternatives-anchored gap statement) as fixed
input and rapidly produces multiple segment- or channel-specific value
proposition statements from it — the growth team's tool for cranking out
testable copy variants without re-litigating positioning each time.
Every statement it produces must trace back to the canonical positioning
— if a variant contradicts or drifts from it, that's a signal to escalate
back to `positioning-messaging`, not something this skill quietly
resolves on its own.

**Step 0** — Load the canonical positioning statement (brain Section 1
product context, Section 3 alternatives/gap statement, or a
freshly-pasted positioning statement from `positioning-messaging` output)
and brain Section 2 (ICP) if present.

**Step 1** — Confirm the source positioning. Block if none exists or is
only a vague product description — this skill fans out an existing
positioning, it doesn't invent one.

**Step 2** — Identify target segments/channels for this batch (from
`buyer-personas` output if a recent session exists, brain ICP, or direct
ask).

**Step 3** — Generate one value-prop statement per segment/channel:
benefit, feature/capability that makes it possible, audience-specific
language.

**Step 4** — Trace-check every statement back to the canonical
positioning — flag any that drift or contradict it rather than silently
delivering them.

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** You already have a set positioning statement and need it
  translated into segment-specific, channel-specific, or persona-specific
  value-prop copy for marketing, sales, or onboarding.

- **Not for:** Building the canonical positioning statement itself from
  scratch, or the full messaging hierarchy → `positioning-messaging`
  (pmm-positioning), run that first if no positioning exists yet.
  Generating raw, pre-positioning campaign ideas → `experiment-ideas`
  (pmm-growth), run that first if you're brainstorming what to try, not
  rewriting something already decided. Mapping who's in the buying
  committee before writing to them → `buyer-personas` (pmm-positioning).

- **Example prompts:**
  - "Write value prop statements for our Enterprise segment"
  - "Adapt our positioning for a LinkedIn ad"
  - "Give me onboarding copy that matches our positioning"
  - "Sales deck value props for the Champion persona"
  - "We need 3 variants of our value prop for an A/B test"

---

## Inputs

- **Args:** The canonical positioning statement (pasted, or loaded from
  brain), target segments/channels, number of variants wanted.
- **Defaults:** If no positioning statement is available anywhere, block
  and direct to `positioning-messaging`. If segments aren't specified,
  ask, or pull from a recent `buyer-personas` session if one exists.
- **Context keys:**
  - `/foundation/brain.md` — read Section 1 (Product), Section 2 (ICP),
    Section 3 (Alternatives/gap statement) if present. Never written to
    — variants are fast-iteration output, not a durable brain fact.
  - `/context/skill-sessions.md` — check for a recent `buyer-personas`
    session to pull real committee segments instead of guessing.

---

## Pre-flight

- Check for a canonical positioning statement: brain Section 3's gap
  statement, or ask the user to paste one from a recent
  `positioning-messaging` session. If neither exists: **hard block** —
  "No positioning statement found. This skill fans out an existing
  positioning into variants — it doesn't build one from scratch. Run
  `positioning-messaging` first, then come back."
- If a recent `buyer-personas` session exists in
  `/context/skill-sessions.md`, offer to use its committee roles as the
  segment list instead of asking from scratch.

---

## Steps

**Step 1 — Confirm the source positioning.**
State back the positioning statement being used as the fixed input.
Block if it's missing or is only a generic product description ("we help
teams work better" is not a positioning statement — it has no named
alternative or differentiator). Ask the user to run
`positioning-messaging` first if so.

**Step 2 — Identify segments and channels for this batch.**
If a recent `buyer-personas` session named committee roles, offer them.
Otherwise ask which segments/channels need variants (marketing, sales,
onboarding, or a specific persona/channel combination) and how many
variants total.

**Step 3 — Generate one statement per segment/channel.**
Each statement:
- Names the specific segment or channel it's for
- States the primary benefit and outcome in that audience's language
- Names the feature/capability that makes the benefit real (not just
  asserted)
- Is a rewrite of the canonical positioning's differentiator for this
  audience — not a new claim invented for this statement alone

**Step 4 — Trace-check against canonical positioning.**
For each statement, verify: does this still say what the canonical
positioning says, just in different words for a different audience? Or
does it introduce a new claim, contradict the canonical differentiator,
or overpromise beyond what the product does today? Flag any statement
that fails this check as `[DRIFT — doesn't trace to canonical positioning]`
rather than delivering it silently. Three or more flagged statements in
one batch is a signal the canonical positioning itself may be stale —
surface that directly rather than continuing to patch variants around it.

**Step 5 — Learning Close.**
Append a row to `/context/skill-sessions.md`:

```yaml
skill: value-prop-statements
session_date: {{date}}
pattern: "{{what surprised you, a recurring drift pattern, or 'none' if
  nothing notable happened — never skip the row}}"
source: {{surprised/wrong/missing/n.v.t.}}
```

---

## Outputs

- One value-prop statement per requested segment/channel, delivered in
  chat only — this skill writes no output file of its own
- Session logged to `/context/skill-sessions.md`
- If 3+ statements were flagged for drift: an explicit note recommending
  a `positioning-messaging` AUDIT pass
- **External side effects:** n.v.t.
- **Next skill:** check `next-skill-map.md` for "After value-prop-statements"
  and surface that prompt.

---

## Verification

- A canonical positioning statement was confirmed before any statement
  was generated — never invented from scratch mid-skill
- Every statement names its specific segment/channel, not left generic
- Every statement traces to the canonical positioning's actual
  differentiator, or is explicitly flagged as drift
- A drift rate of 3+ in one batch triggers a surfaced recommendation, not
  silent continuation
- Session logged with all four fields, `pattern: none` written explicitly
  if nothing notable happened — the row is never skipped

---

## Do Not Use For

- **positioning-messaging** (pmm-positioning) — when the task is building
  the canonical positioning statement or full messaging hierarchy from
  scratch, not fanning out an existing one. Run that skill first if no
  positioning exists yet, then this one.

- **experiment-ideas** (pmm-growth) — when the task is generating raw,
  pre-positioning campaign or channel ideas, not rewriting an
  already-decided positioning into variants.

- **buyer-personas** (pmm-positioning) — when the task is mapping who's
  in the buying committee, not writing copy for roles already known.

---

## Operating Rules

1. **Never invent a positioning statement.** If none exists, block and
   route to `positioning-messaging` — this skill fans out, it doesn't
   originate.
2. **Every variant traces to the canonical differentiator.** A statement
   that introduces a new claim isn't a variant, it's drift — flag it.
3. **Name the specific segment or channel in every statement.** A
   generic value prop that could apply to any audience has failed this
   skill's actual job.
4. **3+ flagged statements means escalate, not patch.** Recommend a
   `positioning-messaging` AUDIT rather than continuing to generate
   around a stale positioning.
5. **Write nothing to the brain.** Variants are fast-iteration copy, not
   a durable company fact.
6. **Pull real committee segments when available.** Check for a recent
   `buyer-personas` session before asking the user to name segments from
   scratch.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Canonical positioning confirmed | Stated back before generation; blocked if absent | Yes |
| Segment/channel named per statement | No generic, audience-agnostic statements | Yes |
| Trace-check run | Every statement checked against canonical differentiator | Yes |
| Drift flagged, not hidden | Any statement failing trace-check marked explicitly | Yes |
| Escalation triggered at 3+ drift | AUDIT recommendation surfaced, not silently absorbed | Yes |
| Learning Close complete | Four-field row appended, never skipped | Yes |

---

## Commands

### /variants [segment or channel list]
Generate one value-prop statement per named segment/channel from the
confirmed canonical positioning.

### /audit-drift
Re-run the trace-check against a batch of previously generated
statements — useful after a positioning refresh, to see which existing
variants now drift from the new canonical statement.
