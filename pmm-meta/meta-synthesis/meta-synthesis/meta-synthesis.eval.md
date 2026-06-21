---
name: meta-synthesis.eval
version: 1.0.0
description: >
  Comprehensive eval suite for meta-synthesis skill. Tests: pattern detection accuracy,
  cross-skill signal correlation, guardrail proposal logic, brain update gating, confidence
  calibration trending, stale guardrail detection, logging completeness, and output format compliance.
  8 scenarios covering real compounding loops and edge cases.
---

# Meta-Synthesis Eval Suite

## Setup (Universal)
Each eval:
1. Populates `/context/skill-sessions.md` with test data (8 execution skill sessions)
2. Populates `/foundation/brain.md` with baseline state (Sections 1-7)
3. Populates `/context/meta-patterns.md` with prior guardrails (if testing guardrail drift)
4. Runs meta-synthesis skill for given analysis period or session count
5. Validates outputs: `/context/meta-patterns.md`, brain Section updates, approval gates

---

## Eval 1: Cross-Skill Signal Detection (3+ Occurrences)
**Scenario:** "Champion alignment gap" appears in 2 retros + 2 pre-mortems. Skill should detect HIGH-CONFIDENCE pattern and rank it for brain update.

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: retro
session_date: 2026-06-01
output: "retro notes mention champion alignment gap, -48 hours"

skill: retro
session_date: 2026-06-08
output: "same champion alignment gap flagged again"

skill: pre-mortem
session_date: 2026-06-10
output: "tiger risk: IT/champion alignment not secured"

skill: pre-mortem
session_date: 2026-06-15
output: "tiger risk: same IT/champion alignment risk flagged"
```

**Expected Output:**
```
HIGH-CONFIDENCE PATTERN: Champion alignment gap (4 occurrences across 2 skill domains)
- Retro: 2 occurrences
- Pre-mortem: 2 occurrences
- Impact: 4 launches delayed by 48 hours
- Proposed guardrail: "Add champion alignment owner to launch checklist"
```

**Pass Criteria:**
- Pattern detected and ranked HIGH-CONFIDENCE
- Cross-skill count correct (4 total, 2 domains)
- Impact quantified
- Guardrail proposal explicit
- Ranked above single-domain patterns

---

## Eval 2: Domain-Specific Pattern Deepening (2 Occurrences)
**Scenario:** "Baseline metrics missing" appears in 2 experiment-doc sessions. Skill should identify MEDIUM-CONFIDENCE pattern but flag as WATCH (not yet proposal stage).

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: experiment-doc
session_date: 2026-06-05
output: "experiment brief rejected: baseline metrics undefined"

skill: experiment-doc
session_date: 2026-06-12
output: "same issue: baseline metrics not provided by user"
```

**Expected Output:**
```
MEDIUM-CONFIDENCE PATTERN: Baseline metrics missing (2 occurrences in experiment-doc)
- Impact: 2 experiments rejected, rigor compromised
- Status: WATCH (insufficient evidence for guardrail, but pattern emerging)
- Recommendation: Monitor next 2 experiments. If 3rd occurrence, propose guardrail.
```

**Pass Criteria:**
- Pattern detected and ranked MEDIUM-CONFIDENCE
- Status correctly marked WATCH (not promoted to guardrail)
- Threshold for promotion explicit (3 occurrences)
- No guardrail injected (yet)

---

## Eval 3: Confidence Calibration Audit & Trending
**Scenario:** 3 consecutive OKR quarters with confidence predictions vs. actual achievement. Skill should calculate delta trend and recommend confidence range adjustment.

**Test Data:**
```yaml
# /context/skill-sessions.md (OKRs only)
skill: pmm-okrs
session_date: 2026-03-31
output: "predicted 70% confidence, actually achieved 65%"
confidence_calibration_delta: -5

skill: pmm-okrs
session_date: 2026-06-30
output: "predicted 75% confidence, actually achieved 78%"
confidence_calibration_delta: +3

skill: pmm-okrs
session_date: 2026-09-30
output: "predicted 72% confidence, actually achieved 74%"
confidence_calibration_delta: +2
```

**Expected Output:**
```
CONFIDENCE CALIBRATION AUDIT:
Q1: -5% (under-predicted)
Q2: +3% (over-predicted)
Q3: +2% (over-predicted)

Average delta: 0% (WELL-CALIBRATED)
Trend: Improving (was -5%, now +3% to +2%)
Recommendation: "User is well-calibrated. Maintain confidence range 72-76%."

Brain update proposal: Section 5 (Revenue Levers) → "OKR confidence range: 72-76% (based on 3-quarter calibration data)"
```

**Pass Criteria:**
- Delta calculated correctly for all 3 quarters
- Average delta computed (0%)
- Trend identified (improving)
- Recommendation explicit and specific
- Brain update proposed (if applicable)
- Section 5 target identified

---

## Eval 4: Guardrail Drift Detection (Stale Guardrails)
**Scenario:** `/context/meta-patterns.md` contains a guardrail that hasn't been triggered in 60+ days. Skill should flag as STALE and propose archiving.

**Test Data:**
```yaml
# /context/meta-patterns.md (prior guardrails)
guardrail_1:
  text: "Button color tested 2x. Recommend refining isolation."
  first_triggered: 2026-04-15
  last_triggered: 2026-04-28
  triggered_count: 2
  status: ACTIVE (from prior meta-synthesis run)

# /context/skill-sessions.md (current sessions)
# No triggers for guardrail_1 in past 60 days (data from 2026-05-21 onwards)
```

**Expected Output:**
```
GUARDRAIL DRIFT ASSESSMENT:
Guardrail #1: "Button color tested 2x. Recommend refining isolation."
- Last triggered: 2026-04-28 (53 days ago)
- Triggers in past 60 days: 0
- Status: STALE (no recent activity)
- Recommendation: Archive but retain for historical reference

Action: Move to archived-guardrails section
```

**Pass Criteria:**
- Stale guardrail identified (no triggers in 60+ days)
- Last triggered date correct
- Recommendation explicit (archive)
- Retention policy clear (historical reference kept)

---

## Eval 5: Brain Update Proposal with Approval Gate
**Scenario:** Pattern detected (champion alignment gap, 4 occurrences). Skill proposes Section 7 update and surfaces approval gate. User approves. Skill writes to brain.

**Test Data:**
```yaml
# /context/skill-sessions.md
[4 champion alignment gap occurrences across retro + pre-mortem]

# /foundation/brain.md Section 7 (baseline)
"Launch timelines: Standard 2-week GTM cycle. Watch for external dependencies."
```

**Expected Output - Approval Gate:**
```
BRAIN UPDATE PROPOSAL

Section 7 (Meta-Learnings)

Should we update with:
"Launch assumption: +48 hours for champion + IT alignment. Assign dedicated owner."

Evidence: 4 occurrences (2 retros, 2 pre-mortems), dates [list], impact: 48-hour delays
Downstream: Affects pre-mortem guardrails, launch checklists, stakeholder-maps inputs

Approve? (Y/N)
```

**If Approved:**
```
✅ Brain Section 7 updated:
"Launch timelines: Standard 2-week GTM cycle. Watch for external dependencies.
→ LEARNING 2026-Q2: Champion + IT alignment requires +48 hours. Assign dedicated owner."

Updated: 2026-06-21
```

**Pass Criteria:**
- Approval gate surfaced with evidence
- Downstream impact stated
- If Y: Brain written with timestamp
- If N: Rejection logged to `/context/skill-sessions.md`
- No silent writes

---

## Eval 6: Anti-ICP Discovery via Cross-Skill Interview Signals
**Scenario:** "Procurement cycles 60+ days" flagged in 4 interview-summary sessions + stored as anti-ICP signal in interview logs. Meta-synthesis detects, proposes Section 2 update.

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: interview-summary
session_date: 2026-06-02
anti_signals: ["Procurement cycles 60+ days"]

skill: interview-summary
session_date: 2026-06-09
anti_signals: ["Procurement cycles 60+ days"]

skill: interview-summary
session_date: 2026-06-16
anti_signals: ["Procurement cycles 60+ days"]

skill: interview-summary
session_date: 2026-06-20
anti_signals: ["Procurement cycles 60+ days"]

# /foundation/brain.md Section 2 (baseline)
"Anti-ICP: Startup, <50 employees, no procurement process"
```

**Expected Output:**
```
CROSS-SKILL SIGNAL: Procurement blocker pattern emerging

Pattern: "Procurement cycles 60+ days" (4 interview-summaries, 4 occurrences)
Buyer impact: 4 deals stalled by procurement timeline
Proposed anti-ICP: "Long procurement cycles (60+ days)"

Brain update proposal:
Section 2 (Anti-ICP) → "Startup, <50 employees, no procurement process
→ WATCH 2026-Q2: Procurement cycles 60+ days = deal-stall risk. Qualify early."

Approve? (Y/N)
```

**Pass Criteria:**
- Interview pattern detected (4 occurrences)
- Anti-signal aggregated correctly
- Section 2 target identified
- Wording appended to existing anti-ICP (not replaced)
- Approval gate surfaced

---

## Eval 7: Pre-Mortem Accuracy Correlation (Retro + Pre-Mortem Cross-Reference)
**Scenario:** Pre-mortem predicted 3 tiger risks. Retro run 3 weeks later shows 2 of 3 risks materialized, 1 did not. Skill calculates accuracy score and recommends confidence adjustment.

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: pre-mortem
session_date: 2026-05-15
tiger_risks:
  - "Champion alignment gap"
  - "Post-sales prep underestimation"
  - "Procurement blockers"

skill: retro
session_date: 2026-06-01
output: "retro notes"
risks_materialized:
  - "Champion alignment gap" (YES, -48 hours)
  - "Post-sales prep underestimation" (YES, -72 hours)
  - "Procurement blockers" (NO, not encountered)
pre_mortem_correlation:
  accuracy: 0.67
  risks_predicted: 3
  risks_materialized: 2
```

**Expected Output:**
```
PRE-MORTEM ACCURACY CORRELATION

Pre-mortem date: 2026-05-15 (3 weeks prior)
Tiger risks predicted: 3
Risks that materialized: 2/3 (67% accuracy)

Materialized:
✅ Champion alignment gap (predicted, materialized)
✅ Post-sales prep underestimation (predicted, materialized)
❌ Procurement blockers (predicted, did NOT materialize)

Accuracy score: 67% (GOOD)
Recommendation: "Pre-mortem calibration is strong. User predicted 2/3 correctly. Continue process."

Next step: Log accuracy trend over time. If 3+ pre-mortems with 60%+ accuracy, guardrail: "Pre-mortem process is reliable."
```

**Pass Criteria:**
- Accuracy calculated correctly (2/3 = 67%)
- Materialized risks matched to predictions
- Unmaterialized risks noted
- Recommendation explicit (GOOD)
- Trend tracking offered (if 3+ cycles exist)

---

## Eval 8: Complete Meta-Synthesis Output & Compounding Loop
**Scenario:** Full end-to-end run. 12 sessions across 8 skills over 1 month. Skill detects 3 HIGH-confidence patterns, 2 MEDIUM patterns, proposes 2 guardrails + 2 brain updates, gates approvals, logs session.

**Test Data:**
```yaml
# /context/skill-sessions.md (12 rows, synthesized from evals 1-7)
experiment-doc: 4 sessions (baseline metrics issue recurring)
interview-summary: 3 sessions (procurement pattern + anti-ICP signals)
retro: 2 sessions (champion alignment + post-sales prep)
pmm-okrs: 2 sessions (confidence calibration data)
pre-mortem: 1 session (tiger risk predictions)
```

**Expected Output - Full Report Structure:**

```
# META-SYNTHESIS REPORT
Analysis Period: 2026-05-21 to 2026-06-21
Sessions Analyzed: 12
Execution Skills: experiment-doc (4), interview-summary (3), retro (2), pmm-okrs (2), pre-mortem (1)

---
## HIGH-CONFIDENCE PATTERNS (3+ occurrences)

1. Champion Alignment Gap
   - Occurrences: 4 (2 retros, 2 pre-mortems)
   - Impact: 4 launches delayed 48 hours
   - Proposed guardrail: "Add champion alignment owner to launch checklist"
   - Status: ACTIVE

2. Post-Sales Prep Underestimation
   - Occurrences: 3 (2 retros, 1 interview)
   - Impact: Support docs missed pre-launch deadlines
   - Proposed guardrail: "Support docs deadline -7 days pre-launch"
   - Status: ACTIVE

3. Procurement Blockers
   - Occurrences: 5 (4 interviews, 1 anti-ICP signal)
   - Impact: 5 deals stalled 60+ days
   - Proposed anti-ICP: "Long procurement cycles (60+ days)"
   - Status: NEW PATTERN

---
## MEDIUM-CONFIDENCE PATTERNS (2 occurrences)

1. Baseline Metrics Missing
   - Occurrences: 2 (experiment-doc)
   - Status: WATCH (monitor for 3rd occurrence)
   - Proposed action: Surface guardrail if 3rd occurrence

---
## CROSS-SKILL SIGNALS (2+ domains)

1. Champion alignment impacts both retros (outcomes) and pre-mortems (risk prediction)
   - Implication: Process gap, not random event
   - Recommendation: Dedicated pre-launch champion alignment check

---
## CONFIDENCE CALIBRATION (OKRs)

Quarters analyzed: 3
Average delta: 0% (well-calibrated)
Trend: Improving
Recommendation: Maintain 72-76% confidence range

---
## BRAIN UPDATE PROPOSALS

1. Section 7: Add "Launch assumption: +48 hours for champion alignment. Assign owner."
   - Evidence: 4 occurrences
   - Downstream: Pre-mortem guardrails, launch checklists
   - Approve? [Y/N gate]

2. Section 2: Add anti-ICP "Long procurement cycles (60+ days)"
   - Evidence: 4 interview + 1 anti-signal
   - Downstream: ICP qualification, sales process
   - Approve? [Y/N gate]

---
## GUARDRAIL STATUS

Active: 8 guardrails (all triggered in past 60 days)
Stale: 1 guardrail (archived, historical reference kept)
New: 2 guardrails (proposed this cycle)

---
## NEXT ACTIONS

1. Approve brain updates (2 gates)
2. Approve new guardrails (2 gates)
3. Monitor: Baseline metrics pattern (watch for 3rd occurrence)
4. Scheduled: Next meta-synthesis run 2026-07-21
```

**Pass Criteria:**
- 3 HIGH-confidence patterns identified
- 2 MEDIUM patterns identified with WATCH status
- Cross-skill signals ranked by impact
- Confidence calibration completed (3 quarters)
- 2 brain updates proposed with gating
- Guardrail status assessed (active, stale, new)
- Output format matches specification
- Session logged to `/context/skill-sessions.md`
- Next actions explicit

---

## Eval Test Coverage Matrix
| Eval | Feature | Pass Criteria |
|---|---|---|
| 1 | Cross-skill signal detection (3+) | HIGH-CONFIDENCE pattern ranked, impact quantified |
| 2 | Domain-specific patterns (2) | MEDIUM confidence, WATCH status, promotion threshold |
| 3 | Confidence calibration trending | Delta calculated, average computed, trend identified |
| 4 | Guardrail drift detection | Stale guardrails identified, 60-day threshold applied |
| 5 | Brain update gating | Approval gate surfaced, approval/rejection logged |
| 6 | Anti-ICP discovery | Section 2 update proposed, interview signals aggregated |
| 7 | Pre-mortem accuracy | Correlation calculated, materialized risks tracked |
| 8 | Full pipeline | 12 sessions, 3 HIGH patterns, 2 updates gated, logging complete |

---

## Running Evals
```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke meta-synthesis with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke meta-synthesis with eval N test data]
```

---

## Changelog
### v1.0.0 — 2026-06-21
Initial release: 8 comprehensive scenarios covering cross-skill signal detection, pattern confidence scoring, guardrail drift, brain update gating, calibration trending, anti-ICP discovery, pre-mortem accuracy correlation, and full end-to-end compounding loop.
