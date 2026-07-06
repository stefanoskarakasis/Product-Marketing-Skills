---
name: go-to-market-strategy.eval
version: 2.2.0
description: >
  Comprehensive eval suite for go-to-market-strategy skill. Tests: guardrail surfacing,
  brain context loading, four-signal tier assignment accuracy, proof point gap detection,
  leading indicator presence, channel specificity, competitive context completeness,
  brain Section 7 updates, logging accuracy, and pattern detection for meta-synthesis.
  8 scenarios covering real launch decisions and calibration edge cases.
---

# Go-to-Market-Strategy — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5, 7)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior GTM briefs (if testing pattern detection)
4. Runs go-to-market-strategy skill for given initiative
5. Validates outputs: tier accuracy, signal application, brief quality, logging

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
- Guardrail logged in Step 6

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

## Eval 7: Brain Section 7 Write and Logging

**Scenario:** Brief generated and confirmed by user. Skill should update brain Section 7 and log session to `/context/skill-sessions.md`.

**Expected Brain Write:**
```markdown
## Launch: SSO Integration Feature
- **Date planned:** 2026-Q3
- **Tier assigned:** T1
- **Tier rationale:** Closes feature gap vs Okta, high revenue potential in enterprise segment
- **Primary metric:** 200 net-new enterprise customers by Q3 end
- **Status:** Planned
- **Actuals:** [Updated after retro]
```

**Expected Session Log (Step 6):**
```yaml
skill: go-to-market-strategy
session_date: 2026-06-21
decision_type: "new brief"
initiative_name: "SSO Integration Feature"
initiative_type: "product launch"
quality_score: 89
tier_assigned: "T1"
four_signals:
  - "Market impact: Enterprise ops leaders, existing strong segment"
  - "Revenue potential: High (customer research shows strong ROI)"
  - "Competitive urgency: Closes gap vs Okta (3 competitive threats)"
  - "Resource requirement: Full team investment, 12 weeks"
confidence_score: 🟢
guardrails_triggered: []
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2): Enterprise ops"
  - "Positioning (Section 3): Security + ease"
  - "Competitive (Section 4): Okta dominance"
  - "Proof points (Section 5): 30% ROI, 8-hour setup"
  - "Launch history (Section 7): Prior T1 enterprise launches"
leading_indicators_count: 2
proof_point_gaps: 0
brain_write_executed: true
```

**Pass Criteria:**
- Brain Section 7 write asked before executing
- Session logged to `/context/skill-sessions.md` with all metadata
- Quality score reflects signal rigor
- Confidence level matches signal quality
- All four signals documented with reasoning

---

## Eval 8: End-to-End Brief Generation with Pattern Detection

**Scenario:** Full GTM brief session end-to-end. Test detects if guardrails are useful and whether tier calibration is improving over time.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior GTM briefs)
Session 1: T1 assigned with readiness 0.6 → Launch delayed 4 weeks
Session 2: T2 assigned with readiness 0.4 → Launch on time but under-resourced
Session 3: T1 assigned with readiness 0.8 → Launch on schedule

# Current session:
Initiative: New market entry (healthcare)
Signals applied → Tier assigned → Brief generated → Logged
```

**Expected Output - Pattern Recognition:**
```
✓ Session completed: Healthcare market entry GTM brief
✓ Quality score: 87/100
✓ Tier assigned: T2 (New market, moderate resource, strong ROI signal)
✓ Four signals applied with reasoning
✓ Leading indicators: 2 present (Week 1 pilot signups, Week 2 sales meetings)
✓ Proof points: 1 gap flagged (ROI in healthcare untested)

🔁 PATTERN FOR META-SYNTHESIS:

Tier calibration accuracy (last 3 sessions):
  - T1 with readiness >0.7: 100% on-schedule delivery
  - T1 with readiness 0.5–0.7: 0% on-schedule (delayed 3–4 weeks)
  - T2 with readiness <0.5: 100% under-resourced

Guardrail recommendation: Keep "Launch readiness <0.5 underperforms" ACTIVE.
Add new pattern: "T1 requires readiness >0.7 or risk delays."

Emerging pattern: Proof point gaps in new markets correlate with rework + messaging delays.
Proposed learning for brain Section 7: "New market launches need pre-brief proof point audit."
```

**Pass Criteria:**
- Full workflow completes (intake → four signals → tier → brief → log)
- Quality score reflects signal rigor + proof point gap handling
- Guardrails surfaced and proven useful or not
- Tier calibration patterns detected (readiness vs. on-time delivery)
- Brain updates proposed for meta-synthesis
- Proof point gaps handled explicitly

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
| 7 | Brain Section 7 + logging | Write confirmed, session logged with all metadata |
| 8 | End-to-end workflow | Intake→Signals→Tier→Brief→Log, patterns detected |

---

## Changelog

### v2.2.0 — 2026-06-22
Major refactor for MCP-ready architecture: Added Step 0 guardrail loading from `/context/meta-patterns.md`. Added Step 6 session logging to `/context/skill-sessions.md` with 20+ metadata fields (signals reasoning, readiness score, proof gaps, brain updates). Integrated four-signal tier assignment with explicit reasoning for each signal. Weight-cut from v2.1.0 (~600 lines) to ~450 lines. Updated description to 1 sentence. Added 8 comprehensive evals covering guardrail surfacing, four-signal accuracy, proof point detection, leading indicators, channel specificity, brain writes, and pattern detection. Full 19/19 SKILL-SPEC compliance.

### v2.1.0 — 2026-06-12
Spec compliance audit. Brain-missing now triggers onboarding. First-run check added.

### v2.0.0 — 2026-06-06
Full rebuild to SKILL-SPEC v2.0.0.

### v1.0.0 — 2026-04-01
Initial build.
