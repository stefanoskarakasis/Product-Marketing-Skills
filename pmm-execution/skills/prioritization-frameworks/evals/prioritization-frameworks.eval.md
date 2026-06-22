---
name: prioritization-frameworks.eval
version: 2.0.0
description: >
  Comprehensive eval suite for prioritization-frameworks skill. Tests: guardrail surfacing,
  brain context loading, framework selection accuracy, scoring integrity, Quality Gate enforcement,
  tier assignment accuracy, confidence score honesty, logging accuracy,
  and pattern detection for meta-synthesis. 8 scenarios covering real prioritization scenarios and edge cases.
---

# Prioritization-Frameworks — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior scoring sessions (if testing pattern detection)
4. Runs prioritization-frameworks skill for given decision scenario
5. Validates outputs: framework selection, scoring quality, Quality Gate enforcement, tier assignment accuracy, session logging

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "RICE without customer Confidence data has inflated Impact by 2 points on average in 3 prior sessions → Always pull win/loss before Impact scoring". User triggers framework skill to tier a new launch without sharing win/loss data. Skill should surface guardrail before intake.

**Test Data:**
```yaml
# /context/meta-patterns.md
guardrail_1:
  text: "RICE without customer Confidence data inflates Impact"
  trigger: "Framework selection for tier decision without win/loss evidence"
  action: "Recommend pulling win/loss data before Impact scoring"
  status: ACTIVE

# /context/skill-sessions.md
skill: prioritization-frameworks
session_date: 2026-06-10
decision_type: "tier"
framework_selected: "RICE"
confidence_inflation_detected: true
gate_failures: 1

skill: prioritization-frameworks
session_date: 2026-06-12
decision_type: "tier"
framework_selected: "RICE"
confidence_inflation_detected: true
gate_failures: 1

skill: prioritization-frameworks
session_date: 2026-06-15
decision_type: "tier"
framework_selected: "RICE"
confidence_inflation_detected: true
gate_failures: 1
```

**Expected Output - Guardrail Surfaced:**
```
🔁 PATTERN FROM PRIOR SCORING SESSIONS

I've seen RICE scoring without customer win/loss data inflate Impact scores 3 times.
Examples: [Initiative names from prior sessions]

Quick check: Do you have win/loss data or customer research for this launch?
- If YES → We'll build it into the Confidence scoring
- If NO → I'll recommend lightweight framework or validation sprint first
```

**Pass Criteria:**
- Guardrail surfaces before Step 1 intake
- Pattern count accurate (3 prior occurrences)
- User can acknowledge or skip guardrail
- Guardrail logged in Step 7 (guardrails_triggered field)

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` exists with populated ICP (§2), Positioning (§3), Revenue Levers (§5). Skill should load silently and reference during framework selection and tier translation.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Primary: Mid-market B2B SaaS, 50-500 employees, ops teams
Secondary: Enterprise ops teams (500+), lower growth trajectory

## Section 3: Positioning
Unique angle: "For ops leaders who measure impact, not activity"
Key differentiator: Outcome-first analytics, not output metrics

## Section 5: Revenue Levers
Lever 1: Time-to-value (setup speed) — $10K ACV impact
Lever 2: Outcome visibility (customer success metric) — $5K ACV impact
Lever 3: Team collaboration (multiple stakeholder adoption) — $15K ACV impact
```

**Expected Output - Context Referenced:**
```
✓ Brain context loaded:
  - ICP: Mid-market ops teams (grounding Reach in this segment)
  - Positioning: Outcome-first analytics (defining Impact scope)
  - Revenue Levers: Team collaboration as highest ACV lever (weighing Impact)

Reach interpretation: [Pre-filled with mid-market + enterprise segments]
Impact definition: [Weighted by revenue lever alignment]
```

**Pass Criteria:**
- Brain sections loaded silently at pre-flight
- ICP anchors Reach definition
- Positioning informs Impact interpretation
- Revenue Levers weight the scoring (e.g., if initiative drives Lever 3, Impact is higher)

---

## Eval 3: Framework Selection Accuracy (Decision-Type Specific)

**Scenario:** User presents a decision scenario. Skill recommends the right framework for the decision type, not just any framework.

**Test Data - Scenario A: Tier a single launch**
```
Input: "We're launching a new feature next month. What tier does it warrant?"
Data available: Customer research (3 conversations), internal confidence, competitive signal
Available frameworks: Opportunity Score, ICE, RICE, Risk vs Reward

Expected selection: RICE or ICE
NOT: Eisenhower, MoSCoW, Weighted Decision Matrix
Reasoning: Single-launch tier decision with moderate data → RICE (if defending to leadership) or ICE (if quick triage)
```

**Test Data - Scenario B: Evaluate new market entry**
```
Input: "Should we enter the Australian market? We have no local data."
Data available: Macro trends, internal confidence (low), no win/loss data
Available frameworks: RICE, Risk vs Reward, Weighted Decision Matrix

Expected selection: Risk vs Reward + Confidence check
NOT: RICE (will inflate without local data), Opportunity Score (no customer data)
Reasoning: High uncertainty, high cost of being wrong → explicit Risk mapping required
```

**Test Data - Scenario C: Prioritize roadmap backlog with team**
```
Input: "We have 12 feature ideas and 60 minutes with the team. How do we prioritize?"
Data available: Internal scoring (rough), no customer research yet
Available frameworks: Impact vs Effort, RICE, Weighted Decision Matrix

Expected selection: Impact vs Effort (rapid rough sort) → hand off to RICE for rigor
NOT: Opportunity Score (no customer data yet), MoSCoW (not a prioritization tool)
Reasoning: Workshop scenario with limited data → lightweight first, then rigorous
```

**Pass Criteria:**
- Framework recommended fits the decision type
- Framework matches the data available (don't recommend RICE without Reach data)
- If multiple frameworks valid, skill explains trade-offs
- Skill surfaces when data is insufficient (e.g., "No customer data → recommend validation before full RICE scoring")

---

## Eval 4: Scoring Integrity & Confidence Honesty

**Scenario:** Skill scores an initiative using selected framework. Quality Gates catch Confidence inflation, missing evidence, and assumption misstatements.

**Test Data:**
```
Initiative: Feature launch
Framework: RICE
Scoring:
  - Reach: 500 customers (from ICP segment)
  - Impact: 8/10 (internal estimate, no customer validation)
  - Confidence: 85% (self-assessed, no win/loss data)
  - Effort: 3 person-months

Quality Gate checks:
  - Gate 1 (Signal integrity): Impact 8/10 with NO customer evidence → 🔴 FAIL
  - Gate 2 (Confidence honesty): 85% without win/loss data → 🔴 FAIL (recommend 50-60%)
  - Gate 3 (Framework fit): RICE OK for tier decision → 🟢 PASS
  - Gate 4 (Tier consistency): Output aligns with tier definitions → 🟢 PASS
  - Gate 5 (Actionability): Output includes next step → depends on content
```

**Expected Output - Gate Failures Surfaced:**
```
⚠️ QUALITY GATE FAILURES DETECTED

Gate 1 — Signal integrity FAILED
Impact scored 8/10 but no customer evidence cited.
Recommendation: Lower to 5/10 (assumption-based) or run customer validation before scoring.

Gate 2 — Confidence honesty FAILED
Confidence 85% but no win/loss data, no prior deployments.
Recommendation: Lower to 50-60% (baseline assumption confidence).

TIER REVISION:
Original: T1 (score 3,400)
Revised: T2 (score 1,500 with corrected Impact + Confidence)
```

**Pass Criteria:**
- Quality Gates run automatically after scoring
- Gate failures caught before tier delivery
- Confidence inflations flagged with specific corrections
- Tier adjusted before output (don't deliver inflated tier, then correct it later)
- Skill surfaces "validation needed before GTM investment" when Confidence <7

---

## Eval 5: Tier Assignment Accuracy (Ratio-Based)

**Scenario:** Skill assigns tier (T1–T4) based on framework output. Tier must align with tier criteria (High/Strong/Moderate/Low signal).

**Test Data:**
```
Scenario A: High Opportunity Score (8/9), 600 customer segment, RICE score 4,200
Expected tier: T1 (High signal across dimensions)
Acceptable: T2 if Confidence <70%

Scenario B: Strong Opportunity Score (7/9), 150 customer segment, RICE score 1,800
Expected tier: T2 (Strong signal but limited reach)
Acceptable: T1 if strategic urgency high (competitive threat)

Scenario C: Moderate Opportunity Score (5/9), 80 customer segment, RICE score 680
Expected tier: T3 (Validated problem, narrow reach)
Acceptable: T2 if Confidence >80% and revenue lever impact high

Scenario D: Low signal across all dimensions, early-stage hypothesis
Expected tier: T4 (No GTM investment yet)
Acceptable: T3 if customer research is in flight
```

**Pass Criteria:**
- Tier assignment aligns with scoring output (no T1 from low scores)
- Tier rationale is one-sentence and specific (not "strong signal")
- Confidence score stated and influences tier (Confidence <7 caps tier at T2)
- Tier includes "next step" (validation, data gathering, GTM readiness)
- Tier logged in Step 7 with all supporting scores

---

## Eval 6: Framework Application Consistency

**Scenario:** Skill applies framework rules consistently across all dimensions.

**Test Data - ICE Framework:**
```
Initiative 1: I=400, C=8, E=6 → Score 19,200
Initiative 2: I=300, C=9, E=8 → Score 21,600

Skill should:
1. Calculate both correctly (no arithmetic errors)
2. Note that Initiative 2 scores higher despite lower I (due to higher C and E)
3. Flag if C=8 and C=9 are both justified by evidence (avoid arbitrary scoring)

Quality issue to catch:
- If Initiative 1 has no customer evidence but C=8, flag it
- If Initiative 2 has strong evidence but the 1-point Confidence diff seems wrong, pressure-test it
```

**Pass Criteria:**
- Formulas applied correctly
- Scoring consistent across all initiatives (same evidence standard for all)
- Confidence scores pressure-tested on weak data (not just rubber-stamped)
- Scoring table includes Source column (so user can see where each number came from)

---

## Eval 7: Session Logging Accuracy (Step 7)

**Scenario:** Framework skill session completes with framework selected → scoring → tier assigned → Quality Gates passed. Skill logs to `/context/skill-sessions.md`.

**Expected Output - Session Log:**
```yaml
skill: prioritization-frameworks
session_date: 2026-06-21
decision_type: "tier"
initiatives_scored: 1
framework_selected: "RICE"
frameworks_used: ["RICE"]
quality_score: 87
tier_assignments:
  - initiative: "Bulk User Imports Feature"
    tier: "T2"
    confidence: 7
guardrails_triggered:
  - "RICE without customer data" (addressed by recommending win/loss pull)
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2) — mid-market ops teams"
  - "Positioning (Section 3) — outcome-first analytics"
  - "Revenue Levers (Section 5) — time-to-value"
brain_updates_proposed:
  - "Section 7: Emerging pattern — T2 assignments with Confidence <7 have 60% GTM churn rate. Recommend validation sprint before full motion."
confidence_inflation_detected: true
gate_failures: 1
validation_recommended: true
recommendation: "Proceed with T2, but recommend customer validation on Impact before committing full GTM resources"
output_path: "/artifacts/prioritization/bulk-imports-tier-card-v1.md"
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md`
- All metadata fields populated (framework, tiers, confidence, quality score)
- Guardrails triggered listed (if any)
- Brain context loaded and sections referenced
- Brain updates proposed (for meta-synthesis)
- Confidence inflation detection logged (true/false + count)
- Gate failures tracked
- Recommendation field reflects Quality Gate outcomes (not ideal tier, but realistic one)
- Quality score reflects gate passes (90+ = all gates passed)

---

## Eval 8: End-to-End Prioritization with Pattern Detection

**Scenario:** User runs prioritization end-to-end: intake → framework selection → scoring → Quality Gates → tier assignment → logging. Test detects patterns (guardrails useful? tier assignments accurate after validation?).

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior scoring sessions)
Session 1: RICE without win/loss data, Confidence inflated 3 points → Tier revised down after validation
Session 2: ICE framework applied, all gates passed → Tier held up post-launch
Session 3: Risk vs Reward for new market, no local knowledge → Recommended validation sprint (followed advice)

# Current session:
Framework selection → Scoring with Quality Gates → Tier assignment → Logging
```

**Expected Output - Pattern Recognition:**
```
✓ Session completed: Prioritization scoring
✓ Quality score: 85/100
✓ Guardrails triggered: 1 ("RICE without customer data")
✓ Gate failures: 1 (Confidence inflation caught and corrected)

🔁 PATTERN FOR META-SYNTHESIS:

Tier assignment accuracy tracking (last 3 sessions):
  - T1 assignments: 100% accuracy (1 of 1 validated as T1+)
  - T2 assignments: 80% accuracy (1 of 1 held, 1 revised down post-validation)
  - T3 assignments: Not yet tested

Framework effectiveness:
  - RICE with good data: High accuracy, requires win/loss pull
  - ICE for quick triage: 100% accuracy, lower confidence ceiling
  - Risk vs Reward for high-uncertainty: Accuracy pending validation

Guardrail recommendation: Keep "RICE without customer data" ACTIVE.
New hypothesis to track: "T2 with Confidence <7 needs validation before GTM motion" (seen in 2 sessions).

Proposed learning for Section 7: "Framework selection determines data requirements. Running RICE without Reach validation costs 2 weeks of iteration post-launch; pulling data upfront costs 3 days."
```

**Pass Criteria:**
- Full workflow completes (intake → selection → scoring → gates → tier → log)
- Quality score reflects gate enforcement (no inflated tiers delivered)
- Guardrails surfaced at Step 0 (if applicable)
- Framework selected matches decision type
- Quality Gates caught issues before tier delivery
- Session logged to `/context/skill-sessions.md` with all metadata
- Brain updates proposed for meta-synthesis
- Pattern signals extracted (tier accuracy, framework effectiveness, guardrail usefulness)
- Output includes next step (validation, data gathering, GTM readiness)

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, user warned, can acknowledge/skip |
| 2 | Brain context loading (pre-flight) | ICP, positioning, revenue levers inform framework selection + tier |
| 3 | Framework selection accuracy | Right framework for decision type + data available |
| 4 | Scoring integrity & Confidence honesty | Quality Gates catch inflation, missing evidence, assumptions |
| 5 | Tier assignment accuracy | Tier aligns with scoring output, Confidence <7 caps tier |
| 6 | Framework application consistency | Formulas correct, scoring consistent, evidence standards aligned |
| 7 | Session logging accuracy | Complete metadata logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Intake→Selection→Scoring→Gates→Tier→Log, patterns detected |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke prioritization-frameworks with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke prioritization-frameworks with eval N test data]
# [validate against eval N pass criteria]
```

---

## Changelog

### v2.0.0 — 2026-06-22
Major refactor: Consolidated knowledge architecture (Blocks 1–3) into Step 7 logging. Removed `/workshop` and `/learn` commands (feature-rich but non-core). Added full MCP-ready architecture: Step 0 guardrail loading, Step 7 session logging to `/context/skill-sessions.md`, brain context integration (ICP, positioning, revenue levers). Added 8 comprehensive evals covering guardrail surfacing, framework selection, scoring integrity, Quality Gate enforcement, confidence honesty, tier assignment accuracy, logging, and pattern detection. Weight-cut framework reference (removed verbose prose, kept formula + PMM Use + Tier Signal). Quality score now reflects gate enforcement. All 19/19 SKILL-SPEC compliant.

### v1.0.0 — 2026-06-05
Initial build: 9 frameworks with formulas, PMM interpretation, tier output logic (T1–T4). Commands: /score, /tier, /compare, /audit. Knowledge architecture (Blocks 1–3) with persistent files for rules, hypotheses, decisions. Quality Gate with 5 independent checks.

