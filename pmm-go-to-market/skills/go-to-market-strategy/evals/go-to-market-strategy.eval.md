---
name: go-to-market-strategy.eval
version: 2.3.0
description: >
  Comprehensive eval suite for go-to-market-strategy skill. Tests: guardrail surfacing,
  brain context loading, four-signal tier assignment accuracy, proof point gap detection,
  leading indicator presence, channel specificity, competitive context completeness, and
  Learning Close accuracy against the skill's real four-field session-log shape.
  8 scenarios covering real launch decisions and calibration edge cases.
---

# Go-to-Market-Strategy — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5, 7)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior GTM sessions in the skill's real four-field shape (if testing Step 0 guardrail recall)
4. Runs go-to-market-strategy skill for given initiative
5. Validates outputs: tier accuracy, signal application, brief quality, Learning Close accuracy

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "T2 launches with launch readiness <0.5 underperformed 80% of the time → Surface launch readiness before tier assignment". User requests GTM brief for a feature launch with moderate resource commitment. Skill should surface guardrail before tier assignment.

**Expected Output:**
```
🔁 PATTERN FROM PRIOR GTM BRIEFS

I've seen T2 launches with low launch readiness underperform 80% of the time.
Examples: [prior launch names from 2+ sessions]

Quick check: Is your team launch-ready for this initiative?
- If YES → We'll validate readiness during brief
- If NO → We may recommend T3 to reduce risk
```

**Pass Criteria:**
- Guardrail surfaces before tier assignment
- Pattern linked to specific tier (T2) and metric (launch readiness <0.5)
- User can acknowledge or skip
- Session logged at Step 5 per the skill's real Learning Close shape — see Eval 7

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` fully populated (Sections 2–7). Skill loads silently and applies context during tier assignment and brief generation.

**Expected:** All four tier signals reasoned through using brain data:
- Market impact grounded in Section 3 (positioning) + Section 4 (competitive)
- Revenue potential grounded in Section 2 (ICP deal size) + Section 5 (proof points)
- Competitive urgency grounded in Section 4 (competitive landscape)
- Resource requirement grounded in Section 5 (launch history actuals)

**Pass Criteria:** Brain context loaded and referenced without narration.

---

## Eval 3: Four-Signal Tier Assignment Accuracy

**Scenario:** Initiative with mixed signals:
- Market impact: Medium (feature for existing segment)
- Revenue potential: High (strong ROI case)
- Competitive urgency: Low (no immediate competitor threat)
- Resource requirement: Low (1 PM, PMM, marketing)

**Expected:** T2 assignment (not T1, not T3)
- Reasoning: Strong revenue signal + existing segment + low competitive pressure + moderate resource = T2
- Rationale: "Meaningful revenue opportunity in validated segment without urgent competitive need"

**Pass Criteria:** 
- All four signals explicitly reasoned
- Tier assignment grounded in signal combination (not any single signal)
- Tier rationale stated one sentence before brief

---

## Eval 4: Proof Point Gap Detection

**Scenario:** Brief requires ROI claim ("Reduces operational overhead by 30%") but brain Section 5 has no proof point for this claim.

**Expected Output:**
```
### Proof Points
- Faster onboarding: "Cuts setup time from 8 hours to 30 minutes" (Customer interview, Q2)
- Cost reduction: [MISSING PROOF POINT]

⚠️ Brief requires "30% operational overhead reduction" claim but no proof point exists.
Recommend: Gather evidence before launch or reframe claim to one you can substantiate.
```

**Pass Criteria:**
- Missing proof point explicitly flagged
- Flag appears in brief output before delivery
- Recommendation given (gather evidence vs. reframe)

---

## Eval 5: Leading Indicator Requirement

**Scenario:** Tier T1 launch. Primary metric: "100K new customers by end of Q2." Skill should generate ≥1 leading indicator for early signal.

**Expected Output:**
```
### Success Metrics
| Metric | Type | Target | Timeframe | Measurement |
|---|---|---|---|---|
| New customers | Lagging | 100K | Q2 end | Billing system |
| Signups per day | Leading | 1200 | Week 2 | Analytics | 
| Sales demos booked | Leading | 500 | Week 1 | CRM |
```

**Pass Criteria:**
- ≥1 leading indicator present (not just lagging metric)
- Leading indicators tied to lagging metric with causal logic
- All indicators have specific targets and measurement source

---

## Eval 6: Channel Specificity (ICP-Grounded)

**Scenario:** ICP from brain Section 2: "Enterprise ops leaders, Fortune 500, 5-year cycle, committee buying."

**Expected Output:**
```
### Channel Strategy
| Channel | Why | Tactic | Owner |
|---|---|---|---|
| Account-based marketing | F500 buyers use intent data + buyer committees | Target 50 accounts with LinkedIn/direct mail combo | Demand Gen |
| Industry conferences | Ops leaders network at APAC Summit | Sponsor speaking slot, booth, post-brief meetings | PMM |
| Sales direct outreach | Existing pipeline warm to new features | Sales brief + 1:1 demos to top 20 accounts | Sales |
| Product-led trial | NOT RECOMMENDED for this ICP | Enterprise procurement requirements prohibit free trials | PMM |
```

**Pass Criteria:**
- Every channel grounded in ICP characteristics (not generic "email, LinkedIn, webinar")
- Channels rejected if not ICP-fit (not just included)
- Specific tactic named per channel
- Owner assignment clear

---

## Eval 7: Learning Close Accuracy (Step 5)

**Scenario:** Go-to-market-strategy skill session completes with four-signal reasoning → tier assignment → full 7-section GTM brief. Skill logs to `/context/skill-sessions.md` per its Step 5 Learning Close.

**Expected Output - Session Log:**
```yaml
skill: go-to-market-strategy
session_date: 2026-06-21
pattern: "T1 tier assigned on strong revenue + competitive urgency signals despite moderate launch readiness — worth watching whether readiness undercuts this tier call, as it has on prior T1 launches."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly these four fields — `skill`, `session_date`, `pattern`, `source` — matching Step 5's template in `SKILL.md` verbatim. No additional fields.
- `pattern` is a single falsifiable statement about what happened this session, or the literal string `"none"` if nothing notable occurred — not a multi-field summary object.
- `source` is one of `surprised / wrong / missing / n.v.t.`
- The row is written directly, without asking the user for permission — this is a separate, mechanical write from anything the skill asks the user's go-ahead on (like where to save the GTM brief, per Outputs).
- If nothing notable happened this session, the row is still written with `pattern: none` — the log entry is never skipped.
- The tier assignment, four-signal reasoning, and full GTM brief are delivered in chat only (Steps 3-4) — none of that detail is duplicated into the session-log row.

---

## Eval 8: End-to-End GTM Brief, Full Workflow

**Scenario:** User runs go-to-market-strategy end-to-end: intake → brain context → four-signal tier assignment → full 7-section brief → Learning Close.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior go-to-market-strategy rows, real shape)
skill: go-to-market-strategy
session_date: 2026-05-02
pattern: "T1 assigned with launch readiness ~0.6 — launch slipped 4 weeks"
source: wrong

skill: go-to-market-strategy
session_date: 2026-05-20
pattern: "T2 assigned with launch readiness ~0.4 — launched on time but under-resourced"
source: wrong

skill: go-to-market-strategy
session_date: 2026-06-08
pattern: "T1 assigned with launch readiness ~0.8 — launched on schedule, no rework"
source: surprised

# Current session:
Initiative: New market entry (healthcare) → four signals applied → T2 assigned → full brief generated
```

**Expected Output - Full Workflow:**
```
✓ Tier assigned: T2 (New market, moderate resource, strong ROI signal)
✓ Four signals applied with reasoning (Step 3)
✓ Full 7-section GTM brief delivered (Step 4), including:
  - Leading indicators: 2 present (Week 1 pilot signups, Week 2 sales meetings)
  - Proof points: 1 gap flagged (ROI in healthcare untested)
✓ Session logged (Step 5):
  skill: go-to-market-strategy
  session_date: 2026-06-21
  pattern: "Third consecutive session where launch readiness below 0.7 tracked with either delay or under-resourcing at the assigned tier — worth watching as a candidate guardrail."
  source: surprised
```

Note that pattern-across-sessions detection (comparing this session's row against the three prior rows to spot a recurring readiness/tier theme) is the job of `meta-synthesis`, run separately against the full `/context/skill-sessions.md` log — go-to-market-strategy's own Step 5 only ever writes its own single row. This skill does not itself detect or report cross-session patterns; it just logs an honest, falsifiable observation about this one session.

**Pass Criteria:**
- Full workflow completes (intake → brain context → four signals → tier → brief → Learning Close)
- Guardrails surfaced at Step 0 (if `/context/meta-patterns.md` has an applicable, 2+-occurrence pattern)
- Tier assignment, four-signal reasoning, and full 7-section brief are delivered in chat only
- Session logged to `/context/skill-sessions.md` with the real four-field shape — not a richer schema
- The skill does not attempt cross-session pattern synthesis itself — that's `meta-synthesis`'s job, not go-to-market-strategy's

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, linked to tier/metric, user can skip |
| 2 | Brain context loading (pre-flight) | All sections loaded, all signals grounded in brain |
| 3 | Four-signal tier assignment | All signals reasoned, tier justified by signal combo |
| 4 | Proof point gap detection | Missing claims flagged explicitly in brief |
| 5 | Leading indicator presence | ≥1 leading indicator per brief, tied to lagging metric |
| 6 | Channel specificity | Every channel grounded in ICP, generic tactics rejected |
| 7 | Learning Close accuracy | Real four-field row (`skill`/`session_date`/`pattern`/`source`) logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Intake→Signals→Tier→Brief→Learning Close, no cross-session synthesis attempted by this skill |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke go-to-market-strategy with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke go-to-market-strategy with eval N test data]
# [validate against eval N pass criteria]
```
