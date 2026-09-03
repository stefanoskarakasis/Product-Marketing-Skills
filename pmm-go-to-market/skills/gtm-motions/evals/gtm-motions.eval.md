---
name: gtm-motions.eval
version: 1.0.0
description: >
  Eval suite for gtm-motions skill. Tests: brain hard-block enforcement,
  single-round intake discipline, all-7-motions scoring before gating,
  blocking-gate enforcement (ABM ACV floor, PLG self-serve requirement,
  outbound SDR capacity), single-primary/max-one-secondary selection,
  numeric kill-criterion enforcement, and Learning Close accuracy. 6
  scenarios covering real motion-selection sessions and edge cases.
---

# GTM-Motions — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with Sections 2 (ICP), 3 (Positioning), 4 (Competitive), or omits it to test the hard block
2. Populates `/context/meta-patterns.md` with a guardrail that has fired 2+ times, if testing guardrail surfacing
3. Provides ACV, sales-cycle, and current-motion data, or withholds parts to test the intake sequence
4. Runs gtm-motions skill for the given scenario
5. Validates outputs: gate enforcement, scoring completeness, selection discipline, kill-criterion presence

---

## Eval 1: Brain Hard Block (Step 0 / Pre-flight)

**Scenario:** No `/foundation/brain.md` exists, or Section 2 (ICP) is empty. Skill must hard-block rather than scoring motions against guessed deal economics.

**Expected Output — Block, Not a Guessed Score:**
```
Brain not found. Run product-marketing-context first — motion fit is
scored against ICP deal size, buyer type, and self-serve capability.
```

**Pass Criteria:**
- Skill does not proceed to Step 1 intake or any scoring without brain Section 2 present
- Block message explicitly names `product-marketing-context` as the next step
- A brain with Section 2 present but Sections 3/4 empty does NOT block — only Section 2's absence is a hard stop, per the skill's own Pre-flight rule

---

## Eval 2: Single-Round Intake Discipline

**Scenario:** User asks "which motion should we use?" with no deal economics stated. Skill must ask all four intake questions in one message, not drip-feed them, and must not score before all are answered.

**Expected Output — One Message, Not Sequential:**
```
1. Segment or initiative? (uses confirmed beachhead if one exists)
2. ACV / deal size band?
3. Target sales-cycle length?
4. Current motion, if any — working or not?
```

**Pass Criteria:**
- All 4 questions appear in a single message, not asked one at a time across multiple turns
- Skill does not begin Step 2 scoring until ACV and sales-cycle length are both answered — per the skill's own Inputs default ("if ACV and sales-cycle length are both unknown, block scoring")
- If a confirmed `beachhead-segment` exists, question 1 offers it instead of asking blind

---

## Eval 3: All 7 Motions Scored Before Any Gate Applied

**Scenario:** A deal profile where ACV ($15K) would obviously fail the ABM gate ($25K floor). Test that the skill still scores ABM on all 4 signals before excluding it — not skipping the score because the outcome seems predetermined.

**Test Data:**
```
ACV: $15,000. Sales cycle: 45 days. No dedicated SDR/BDR. Self-serve trial exists.
```

**Expected Output — Scored First, Then Gated:**
```
ABM scored: Deal economics fit 1/5, Buyer reachability 2/5, Team/tool readiness 2/5, Time-to-signal 2/5 — total 7/20.
Gate check: ACV ($15K) < $25K floor → ABM excluded regardless of score.
```

**Pass Criteria:**
- ABM (and all other 6 motions) receive numeric scores on all 4 signals BEFORE the gate check section — scoring is never skipped because a gate seems certain to fire
- The gate exclusion is stated as a separate step from scoring, per Step 2 → Step 3 sequencing
- Every one of the 7 motions (Inbound, Outbound, Paid Digital, Community, Partner, ABM, PLG) appears with a score, not just the ones that survive

---

## Eval 4: Blocking Gate Enforcement (Never Averaged Away)

**Scenario A:** PLG scores well on 3 of 4 signals but no self-serve signup exists and none is planned in 90 days.
**Scenario B:** Outbound scores highest overall but there's no dedicated SDR/BDR capacity.

**Test Data:**
```
Scenario A: PLG — Deal economics 4/5, Buyer reachability 4/5, Readiness 1/5 (no self-serve, none planned), Time-to-signal 4/5. Sum: 13/20 — would rank highest among survivors if not gated.
Scenario B: Outbound — Deal economics 5/5, Buyer reachability 4/5, Readiness 4/5, Time-to-signal 3/5. Sum: 16/20 — highest raw score, but no SDR/BDR capacity.
```

**Expected Output — Gates Fire Regardless of Score:**
```
PLG: 13/20 raw score, but no self-serve signup and none planned in 90 days → excluded by gate, regardless of score.
Outbound: 16/20 raw score, but no dedicated SDR/BDR → excluded as PRIMARY (secondary still allowed only if a founder/PMM runs it part-time, flagged as a constraint).
```

**Pass Criteria:**
- PLG's high raw score does not override its gate failure — it's excluded, full stop, per "never average a gate failure away"
- Outbound's highest-raw-score status does not make it primary given the SDR/BDR gate — it's excluded as primary specifically, with the secondary exception correctly applied only if explicitly flagged as founder/PMM part-time capacity
- Both exclusions are stated with the specific gate that fired, not a generic "didn't make the cut"

---

## Eval 5: Single Primary, Max One Secondary, Funnel-Distinct

**Scenario:** Three motions survive gating with scores 18/20, 16/20, and 15/20. The second-highest (16/20) targets the same top-of-funnel stage as the primary; the third (15/20) is funnel-distinct (expansion-stage).

**Test Data:**
```
Survivors: Paid Digital 18/20 (top-of-funnel), Inbound 16/20 (top-of-funnel, same stage as Paid), Community 15/20 (expansion-stage, funnel-distinct)
```

**Expected Output — Correct Secondary Selection:**
```
Primary: Paid Digital — 18/20.
Secondary: Community — 15/20. Chosen over Inbound (16/20, higher score) because
Inbound fights the same top-of-funnel stage as Paid Digital — a secondary must
be funnel-distinct, not just close in score.
Rejected: Inbound — 16/20, within 3 points of primary, but not funnel-distinct from it.
```

**Pass Criteria:**
- Exactly one primary is selected, never more
- Secondary selection is NOT simply "next-highest score" — it's checked against BOTH the within-3-points rule AND funnel-distinctness, and a higher-scoring but funnel-redundant motion is correctly passed over
- Every rejected motion (including the higher-scoring but funnel-redundant one) gets a one-sentence stated reason

---

## Eval 6: Kill-Criterion Enforcement and Learning Close

**Scenario:** Full session completes — primary motion selected, 90-day activation plan drafted without a numeric kill criterion in the first draft.

**Expected Output — Plan Rejected Until Kill Criterion Added:**
```
This 90-day plan has milestones but no kill criterion — a plan without a
number to cut it by week 13 is a calendar, not a plan. What metric, and
what threshold, ends this motion if unmet?
```

**Expected Output — Session Log:**
```yaml
skill: gtm-motions
session_date: 2026-09-01
pattern: "First activation draft had milestones but no kill criterion —
  worth checking whether Step 5's template should require the number
  before the draft is shown at all, not after."
source: surprised
```

**Pass Criteria:**
- A 90-day plan without a stated numeric kill criterion is not delivered as final — the skill catches this per its own Quality Gate row, not just relies on the template
- The activation plan covers ONLY the selected primary (and secondary, if any) — never includes rejected motions, per "a plan covering rejected motions signals the rejection wasn't real"
- Session logged to `/context/skill-sessions.md` with exactly four fields, no brain write attempted (the stack is explicitly never written to `/foundation/brain.md` per Operating Rules)

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain hard block (Pre-flight) | No ICP → hard stop, never guesses; other sections thin doesn't block |
| 2 | Single-round intake | 4 questions in one message; scoring blocked until ACV + cycle length answered |
| 3 | All 7 motions scored before gating | Every motion scored on all 4 signals before any exclusion |
| 4 | Blocking gate enforcement | Gate failures exclude regardless of raw score — never averaged away |
| 5 | Single primary, funnel-distinct secondary | Secondary chosen by funnel-distinctness + score proximity, not score alone |
| 6 | Kill-criterion + Learning Close | Numeric kill criterion required; real four-field session-log row; no brain write |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke gtm-motions with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke gtm-motions with eval N test data]
# [validate against eval N pass criteria]
```
