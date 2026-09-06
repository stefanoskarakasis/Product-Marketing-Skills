---
name: positioning-ideas.eval
version: 1.0.0
description: >
  Eval suite for positioning-ideas skill. Tests: alternatives hard block
  (3+ required), segment confirmation from prior sessions, per-alternative
  gap mapping, divergence self-check (redundant options flagged, not
  hidden), pre-gate handoff framing, and Learning Close accuracy. 6
  scenarios covering real pre-commitment positioning sessions and edge
  cases.
---

# Positioning-Ideas — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with Sections 1 (Product), 2 (ICP),
   3 (Alternatives) — or leaves Section 3 thin/absent to test the hard
   block
2. Populates `/context/skill-sessions.md` with a recent `beachhead-segment`
   or `buyer-personas` session, or omits it to test direct asking
3. Runs positioning-ideas skill for the given scenario
4. Validates outputs: gate enforcement, divergence, gap-specificity,
   handoff framing

---

## Eval 1: Alternatives Hard Block (Pre-flight)

**Scenario:** Brain Section 3 has only 2 named alternatives (no status
quo named). Skill must hard-block rather than generating options against
an incomplete competitive set.

**Expected Output — Block, Not a Guessed Set:**
```
Positioning options only mean something against real alternatives. Run
hs-alternatives-map first to name at least 3, including status quo, then
come back.
```

**Pass Criteria:**
- Skill does not proceed to Step 1 or any generation with fewer than 3
  named alternatives, or without status quo among them
- Block message explicitly names `hs-alternatives-map` as the next step
- A brain with exactly 3 alternatives including status quo does NOT
  block — only genuinely thin data (fewer than 3, or missing status quo)
  triggers the hard stop

---

## Eval 2: Segment Pulled From Prior Session, Not Re-Asked

**Scenario:** A `beachhead-segment` session exists in
`/context/skill-sessions.md` naming a confirmed segment. User asks for
positioning options without naming a segment.

**Test Data:**
```yaml
skill: beachhead-segment
session_date: 2026-08-20
pattern: "none"
source: n.v.t.
# (segment context: mid-market B2B SaaS, 50-200 employees, confirmed beachhead)
```

**Expected Output — Segment Offered, Not Re-Asked From Scratch:**
```
Using the confirmed beachhead from your last session — mid-market B2B
SaaS, 50-200 employees — as the target segment for these options unless
you want a different one.
```

**Pass Criteria:**
- Skill offers the prior session's segment rather than asking blind
- User can override it, but the default path doesn't force a repeat
  question when a real answer already exists
- If no prior session exists, skill asks directly instead of guessing

---

## Eval 3: Per-Alternative Gap Mapping, Not Generic Differentiation

**Scenario:** Brain Section 3 names 3 alternatives: a manual/status-quo
process, an enterprise-focused competitor, and an in-house build option.

**Test Data:**
```
Alternatives: Manual spreadsheets (status quo), Competitor X (enterprise
IT buyer focus, complex procurement), Building in-house
```

**Expected Output — Specific Gaps, Not "We're Better":**
```
Manual spreadsheets: can't claim real-time visibility — inherently
static once exported.
Competitor X: can't credibly claim self-serve simplicity without
abandoning its own enterprise-procurement positioning.
In-house build: can't claim ongoing vendor investment — whatever gets
built is frozen at whatever the team had time for.
```

**Pass Criteria:**
- Each alternative gets a distinct, concrete gap tied to something that
  alternative structurally cannot claim — not a generic "we're faster/
  easier" for all three
- No gap is phrased as an unqualified superiority claim without a
  structural reason behind it

---

## Eval 4: Divergence Self-Check Catches Near-Duplicates

**Scenario:** Of 5 generated options, two both center on "ease of use"
against the same competitor, differing only in wording.

**Test Data:**
```
Option 2: "The only [category] simple enough for a non-technical team to
run without IT."
Option 4: "The only [category] built for teams without a dedicated IT
resource."
```

**Expected Output — Redundancy Flagged, Not Hidden:**
```
Option 4 flagged: [REDUNDANT — same territory as Option 2]. Both claim
"no IT dependency" against the same alternative — these are one option
in two phrasings, not two real choices.
```

**Pass Criteria:**
- The redundant pair is explicitly caught and flagged, not delivered as
  if they were 2 of 5 genuinely distinct choices
- The flag names which earlier option it duplicates
- Skill either collapses them into one or clearly marks the weaker one —
  it does not silently pad the count to hit "5 options"

---

## Eval 5: Handoff States Pre-Gate Status Explicitly

**Scenario:** Full session completes — 5 options generated, one clear
strongest candidate identified by the user.

**Expected Output — Explicit Non-Shippable Framing:**
```
Option 3 is the strongest fit. Next step: run it through
positioning-messaging's BUILD mode — this list is meant to help you
choose a direction, none of these options have passed the 7-point
verification gate that makes positioning copy actually shippable.
```

**Pass Criteria:**
- The handoff explicitly states the chosen option is not yet shippable
- `positioning-messaging` BUILD mode is named as the required next step,
  not treated as optional
- The skill does not imply its own output can be used directly as final
  copy anywhere in the response

---

## Eval 6: Learning Close Accuracy

**Scenario:** Full session completes — no redundancy issues this round,
segment pulled cleanly from a prior session, nothing notable happened.

**Expected Output — Session Log:**
```yaml
skill: positioning-ideas
session_date: 2026-09-06
pattern: "none"
source: n.v.t.
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly four
  fields, even when nothing notable happened — `pattern: none` is
  written explicitly, the row is never skipped
- No separate knowledge/decisions file written — matches this repo's
  single compounding mechanism used by every other skill
- No brain write attempted at any point — options are disposable, only
  a gated `positioning-messaging` output earns durability

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Alternatives hard block | 3+ named incl. status quo required before any generation |
| 2 | Segment from prior session | Confirmed beachhead/persona segment offered, not re-asked |
| 3 | Per-alternative gap mapping | Each alternative gets a distinct, structural gap, not generic |
| 4 | Divergence self-check | Redundant options flagged with the specific duplicate named |
| 5 | Pre-gate handoff framing | Explicit statement that BUILD mode's gate still applies |
| 6 | Learning Close | Real four-field row; no brain write; `pattern: none` never skipped |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke positioning-ideas with eval N test data]
  # [validate against eval N pass criteria]
done

# Run single eval
# [invoke positioning-ideas with eval N test data]
# [validate against eval N pass criteria]
```
