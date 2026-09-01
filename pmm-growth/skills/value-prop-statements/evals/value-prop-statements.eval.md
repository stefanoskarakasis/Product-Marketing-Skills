---
name: value-prop-statements.eval
version: 1.0.0
description: >
  Eval suite for value-prop-statements skill. Tests: hard block with no
  canonical positioning, buyer-personas segment inheritance, segment/channel
  specificity, drift trace-check flagging, the 3+-drift escalation
  threshold, and Learning Close accuracy against the skill's real
  four-field session-log shape. 6 scenarios covering real variant-generation
  sessions and edge cases.
---

# Value-Prop-Statements — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with a canonical positioning statement (Section 3) and ICP (Section 2), or withholds it to test the hard block
2. Populates `/context/skill-sessions.md` with a recent buyer-personas session if testing segment inheritance
3. Runs value-prop-statements skill for the given scenario
4. Validates outputs: block enforcement, specificity, trace-check accuracy, escalation threshold, confirmation gating

---

## Eval 1: Hard Block With No Canonical Positioning

**Scenario:** No `/foundation/brain.md` exists, and no positioning statement is pasted. User asks directly for value-prop variants.

**Expected Output — Block, Not a Guessed Positioning:**
```
No positioning statement found. This skill fans out an existing
positioning into variants — it doesn't build one from scratch. Run
positioning-messaging first, then come back.
```

**Pass Criteria:**
- Skill does not invent a positioning statement to proceed anyway
- Block message explicitly names `positioning-messaging` as the correct next step
- Skill does not generate any variants until a real positioning statement is confirmed

---

## Eval 2: Buyer-Personas Segment Inheritance

**Scenario:** A canonical positioning exists, and a recent `buyer-personas` session named committee roles (Economic Buyer, Champion, Technical Evaluator). Skill offers those instead of asking the user to name segments from scratch.

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: buyer-personas
session_date: 2026-08-29
pattern: "Champion and Economic Buyer were the same person — smaller org."
source: surprised
# (committee roles referenced in that session's chat output: Economic Buyer/Champion, Technical Evaluator)
```

**Expected Output — Offered, Not Re-Asked:**
```
Found a recent buyer-personas session — want variants for those committee
roles (Economic Buyer/Champion combined, Technical Evaluator), or a
different segment list?
```

**Pass Criteria:**
- Skill checks for a recent `buyer-personas` session before asking the user to name segments from scratch
- If found, offers those roles rather than re-deriving segments
- If not found, falls back to asking directly — doesn't stall

---

## Eval 3: Segment/Channel Specificity Enforcement

**Scenario:** A draft statement that could apply to any audience — no named segment, no audience-specific language.

**Test Data:**
```
Draft: "Our product helps teams work more efficiently and save time."
```

**Expected Output — Rejected as Too Generic:**
```
This doesn't name who it's for or use language that segment would
recognize — it could be pasted onto any B2B product's homepage. Which
segment is this for, and what does "efficient" actually mean to them
specifically?
```

**Pass Criteria:**
- A generic, audience-agnostic statement is not delivered as a finished variant
- Skill requires the specific segment/channel to be named within the statement itself, not just as an external label
- Rewritten statement uses language specific to the named audience, not generic B2B phrasing

---

## Eval 4: Drift Trace-Check Flagging

**Scenario:** Canonical positioning names a specific differentiator (e.g., "the only tool that syncs with async standups without a live meeting"). A draft variant introduces a new claim not present in the canonical statement (e.g., claims real-time video features the canonical positioning never mentioned).

**Test Data:**
```
Canonical positioning: "For distributed eng teams, [Product] is the async
standup tool that removes the live meeting entirely, unlike Geekbot which
still requires a scheduled sync."
Draft variant: "[Product] gives your team real-time video huddles alongside
async updates for maximum flexibility."
```

**Expected Output — Flagged, Not Delivered Silently:**
```
[DRIFT — doesn't trace to canonical positioning] This variant introduces
real-time video, which contradicts the canonical differentiator (removing
the live meeting entirely). Either this is a new capability the positioning
hasn't caught up to, or this variant shouldn't ship as-is.
```

**Pass Criteria:**
- A variant introducing a claim absent from or contradicting the canonical positioning is explicitly flagged, not delivered as validated
- The flag names specifically what contradicts or drifts, not a generic "this seems off"
- Flagged variants are not silently corrected without surfacing the drift to the user first

---

## Eval 5: The 3+-Drift Escalation Threshold

**Scenario:** A batch of 5 requested variants; 3 of them fail the trace-check for various reasons (new claims, contradicted differentiators, or vague audience language that couldn't be traced either way).

**Expected Output — Escalation Surfaced, Not Just Individual Flags:**
```
3 of the 5 variants in this batch drifted from the canonical positioning
— that's not just this batch's problem, it's a sign the canonical
positioning itself may be stale or too narrow for how you're actually
trying to use it. Worth running positioning-messaging in AUDIT mode
before generating more variants, rather than me patching around a
positioning that isn't holding.
```

**Pass Criteria:**
- At 3+ flagged statements in one batch, skill surfaces a `positioning-messaging` AUDIT recommendation explicitly — not just individually flagging each one and moving on
- Below the 3-statement threshold, individual flagging happens but no escalation recommendation is forced
- Escalation language explains why (systemic signal, not one-off drift) rather than a bare "run an audit"

---

## Eval 6: Learning Close and No Brain Write

**Scenario:** Full session completes — 4 variants generated for 4 segments, 1 flagged for drift and corrected after user confirmation.

**Expected Output — Session Log:**
```yaml
skill: value-prop-statements
session_date: 2026-09-01
pattern: "The Procurement-facing variant kept drifting toward compliance
  language not present in the canonical positioning — worth checking
  whether Procurement needs its own positioning angle, not just a
  reworded variant of the primary one."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly four fields — no separate memory or decisions file written
- No brain write attempted at any point in the session — variants exist only in chat output
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Hard block, no canonical positioning | Never invents positioning; routes to positioning-messaging |
| 2 | Buyer-personas segment inheritance | Recent committee session offered, not re-derived |
| 3 | Segment/channel specificity | Generic, audience-agnostic statements rejected |
| 4 | Drift trace-check flagging | Statements contradicting canonical positioning explicitly flagged |
| 5 | 3+-drift escalation threshold | Systemic drift triggers an explicit AUDIT recommendation |
| 6 | Learning Close, no brain write | Real four-field session-log row; no durable brain write |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke value-prop-statements with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke value-prop-statements with eval N test data]
# [validate against eval N pass criteria]
```
