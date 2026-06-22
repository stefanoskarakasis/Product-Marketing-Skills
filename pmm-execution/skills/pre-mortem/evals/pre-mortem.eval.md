---
name: pre-mortem.eval
version: 2.3.0
description: >
  Comprehensive eval suite for pre-mortem skill. Tests: guardrail surfacing,
  brain context loading, failure scenario generation quality, Tiger/Paper Tiger/Elephant classification accuracy,
  Tiger triage completeness (owner + signal + action plan), PMM recommendation clarity, logging accuracy,
  and pattern detection for meta-synthesis. 8 scenarios covering real initiative types and edge cases.
---

# Pre-Mortem — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior pre-mortem sessions (if testing pattern detection)
4. Runs pre-mortem skill for given initiative
5. Validates outputs: risk classification quality, Tiger triage completeness, recommendation clarity, session logging

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "Pricing changes without competitive posture analysis have failed 2 prior times → Always run comp posture check pre-launch". User triggers pre-mortem for a pricing initiative. Skill should surface guardrail before intake.

**Test Data:**
```yaml
# /context/meta-patterns.md
guardrail_1:
  text: "Pricing changes without competitive posture analysis"
  trigger: "Pre-mortem on pricing initiative"
  action: "Require competitive posture check before risk triage"
  status: ACTIVE

# /context/skill-sessions.md
skill: pre-mortem
session_date: 2026-06-10
initiative_name: "Price Optimization Q2"
recommendation: "Hold"
tigers_count: 4

skill: pre-mortem
session_date: 2026-06-15
initiative_name: "Enterprise Tier Launch"
recommendation: "Hold"
tigers_count: 3
```

**Expected Output - Guardrail Surfaced:**
```
🔁 PATTERN FROM PRIOR PRE-MORTEMS

I've seen pricing changes without competitive posture analysis fail 2 prior times.
Examples: "Price Optimization Q2", "Enterprise Tier Launch"

Quick check: Are you aware of this risk?
- If YES → We'll dig into competitive response during Tiger triage
- If NO → Let's add it to our failure scenarios
```

**Pass Criteria:**
- Guardrail surfaces before Step 1 intake
- Pattern count accurate (2 prior occurrences)
- User can approve/skip guardrail
- Guardrail logged in Step 7 (guardrails_triggered field)

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` exists with populated ICP (§2), Positioning (§3), Revenue Levers (§5). Skill should load silently and reference during intake and scenario generation.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Primary: Mid-market B2B SaaS, 50-500 employees, ops teams
Pain points: Manual processes, lack of visibility, team coordination friction

## Section 3: Positioning
Unique angle: "For ops leaders who measure impact, not activity"
Key differentiator: Outcome-first analytics

## Section 5: Revenue Levers
Lever 1: Time-to-value (setup speed)
Lever 2: Outcome visibility (customer success metric)
Lever 3: Team collaboration (multiple stakeholder adoption)
```

**Expected Output - Context Referenced:**
```
✓ Brain context loaded:
  - ICP: Mid-market ops teams (grounding failure scenarios in this segment)
  - Positioning: Outcome-first analytics (informing messaging risks)
  - Revenue: Team collaboration as lever (adding adoption friction scenario)

Target customer from brain ICP: [Pre-filled — mid-market ops leaders]
Risk angle: If adoption slower than expected, teams won't unlock the collaboration lever
```

**Pass Criteria:**
- Brain sections loaded silently at pre-flight
- ICP informs target customer in intake
- Positioning anchors messaging-related failure scenarios
- Revenue Levers inform adoption/friction scenarios

---

## Eval 3: Failure Scenario Generation (Initiative-Specific)

**Scenario:** User completes intake for a feature launch. Skill generates 8-12 failure scenarios specific to the initiative type, rooted in brain context (ICP, competitive positioning).

**Test Data - Feature Launch:**
User input:
- Initiative: "Bulk User Imports"
- Target: Mid-market ops teams (from brain ICP)
- Timeline: 6 weeks
- Tier: P2 Notable
- Team readiness: Sales prepped, docs in progress

**Expected Output - Failure Scenarios:**
```
Market/Competitive:
1. Competitor ships bulk import faster / with better UX
2. Market shifted; ops teams deprioritized user management (macro headwind)

Go-To-Market:
3. Sales team didn't understand the value story — didn't position it as "time-to-value lever"
4. Launch messaging focused on technical features, not outcome ("saves 8 hours per cycle")

Product/Adoption:
5. Bulk import has bugs in production; customers can't use it
6. Integration complexity higher than expected; customers abandon it
7. Adoption slower than expected; ops teams prefer manual CSV (familiarity bias)

Internal/Execution:
8. Team alignment broke; product wanted different scope than marketing promised
9. Rollback decision took 3 weeks; customer churn started Day 7
```

**Pass Criteria:**
- 8-12 scenarios, not fewer
- Scenarios grounded in ICP (mid-market ops teams, time-to-value lever)
- Scenarios span all 4 categories (Market, GTM, Product, Execution)
- Scenarios feel specific, not generic ("sales didn't prep" not vague)
- Failure narratives are concrete ("churn >15% in first 30 days" not "adoption slow")

---

## Eval 4: Tiger/Paper Tiger/Elephant Classification Accuracy

**Scenario:** User classifies failure scenarios. Skill should help distinguish between deal-blockers (Tigers), loud but manageable (Paper Tigers), and accepted trade-offs (Elephants).

**Test Data:**
```
Scenario 1: "Competitor ships bulk import faster with better UX"
  → Expected classification: Tiger (deal-blocking if competitor wins adoption)

Scenario 2: "Sales team didn't understand the value story"
  → Expected classification: Tiger (directly impacts launch if sales doesn't sell)

Scenario 3: "Some customers confused by new bulk import UI"
  → Expected classification: Paper Tiger (manageable with docs/support, improves over time)

Scenario 4: "We're launching without the "auto-retry" feature"
  → Expected classification: Elephant (known trade-off, accepted to hit timeline)

Scenario 5: "Rollback decision took 3 weeks; customer churn started"
  → Expected classification: Tiger (slow decision-making blocks recovery)
```

**Pass Criteria:**
- Classification aligns with user's risk appetite (Tigers = must-mitigate, Paper Tigers = monitor, Elephants = accept)
- Skill asks clarifying question if ambiguous: "Is this deal-blocking, or manageable?"
- User can reclass if disagree ("Actually, that's an Elephant — we decided to accept it")
- Classification count logged in Step 7 (tigers_count, paper_tigers_count, elephants_count)

---

## Eval 5: Tiger Triage Completeness (Owner + Signal + Action)

**Scenario:** For each Tiger, user provides or skill elicits: owner (named person), signal (measurable proof), and action plan (mitigation or rollback trigger).

**Test Data - Tiger 1:**
```
Tiger: "Sales team didn't understand the value story"

Skill generates / elicits:
- Owner: "Sarah (VP Sales) owns sales enablement"
- Signal: "Sales adoption measured by: ≥80% of AE ramp in first 2 weeks. Signals failure: <60% ramp."
- Action: "Pre-brief sales 3 weeks pre-launch. Weekly competitive positioning stand-ups. Rollback trigger: If <50% of AE ramp after 3 weeks, pause launch to rework training materials."
```

**Test Data - Tiger 2:**
```
Tiger: "Adoption slower than expected — ops teams prefer manual CSV"

Skill generates / elicits:
- Owner: "Marcus (VP Product) owns adoption friction reduction"
- Signal: "Target: ≥40% of eligible customers adopt within 30 days. Signal of failure: <20% adoption by Day 30."
- Action: "Run weekly adoption analytics. Day 20 check-in: if trending <20%, ship UX patch (1-week sprint). Rollback: If Day 30 <20%, pause feature, invest in onboarding workflow redesign (2-week sprint)."
```

**Pass Criteria:**
- All Tigers have named owners (person + role, not "team")
- All Tigers have measurable signals (e.g., "churn >15%", "<50% adoption")
- All Tigers have mitigation or rollback actions (not "hope it doesn't happen")
- Actions are specific enough to execute (owner knows what to do)
- Signal + Action logged in Step 7

---

## Eval 6: PMM Recommendation Clarity (Go / Conditional Go / Hold)

**Scenario:** After Tiger triage, skill delivers a clear recommendation: Go, Conditional Go, or Hold.

**Test Data:**
```
Input: Feature launch, 5 Tigers identified
- Tiger 1: Owner assigned, signal clear, action plan defined ✓
- Tiger 2: Owner assigned, signal clear, action plan defined ✓
- Tiger 3: Owner assigned, signal clear, action plan defined ✓
- Tiger 4: Owner assigned, signal clear, action plan defined ✓
- Tiger 5: No owner assigned, action plan vague ✗

Expected recommendation: Conditional Go
Condition: "Go if Tiger 5 (exec alignment) gets an owner and decision by Friday. If not, hold."
```

**Pass Criteria:**
- Recommendation is one of: Go, Conditional Go, Hold (not wishy-washy)
- If Go: All Tigers have owners, signals, actions
- If Conditional Go: Explicit condition stated ("if X happens by Y date")
- If Hold: Clear reason given ("unmitigated Tigers: X, Y, Z")
- Recommendation is 1-2 paragraphs max (clear, direct)
- Recommendation logged in Step 7

---

## Eval 7: Session Logging Accuracy (Step 7)

**Scenario:** Pre-mortem skill session completes with failure scenarios → classification → Tiger triage → recommendation. Skill logs to `/context/skill-sessions.md`.

**Expected Output - Session Log:**
```yaml
skill: pre-mortem
session_date: 2026-06-21
initiative_name: "Bulk User Imports Feature"
initiative_tier: P2
quality_score: 88
tigers_count: 5
paper_tigers_count: 3
elephants_count: 2
guardrails_triggered:
  - "Sales alignment risk" (pre-flagged from prior pre-mortems)
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2) — mid-market ops teams"
  - "Positioning (Section 3) — outcome-first analytics"
  - "Revenue Levers (Section 5) — time-to-value"
brain_updates_proposed:
  - "Section 5: Emerging pattern — feature launches without sales alignment have 80% Tiger materialization. Recommend 3-week sales prep minimum."
  - "Section 2: Anti-ICP signal — ops teams without process maturity churn 2x post-launch. Tighten ICP on process sophistication."
recommendation: "Conditional Go — proceed if Tiger 2 (adoption friction) has owner assigned by Friday"
decision: "approved"
risks_materialized_count: null
output_path: "/artifacts/pre-mortem/bulk-imports-tiger-summary-v1.md"
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md`
- All metadata fields populated (initiative name, tier, counts, quality score, guardrails)
- Tigers/Paper Tigers/Elephants accurately counted
- Guardrails triggered listed (if any)
- Brain context loaded and sections referenced
- Brain updates proposed (for meta-synthesis)
- Recommendation field matches Step 5 output
- Quality score reflects Tiger completeness (90+ = all Tigers have owners + signals + actions)

---

## Eval 8: End-to-End Pre-Mortem with Pattern Detection

**Scenario:** User runs pre-mortem end-to-end: intake → failure scenarios → classification → Tiger triage → recommendation → logging. Test detects patterns (guardrails useful? Tigers materialized in follow-up?).

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior pre-mortems)
Session 1: Feature launch, 4 Tigers, recommendation "Go"
  → Follow-up 3 months later: 3 of 4 Tigers materialized (accuracy: 75%)
Session 2: Pricing change, 5 Tigers, recommendation "Hold"
  → User proceeded anyway; 4 Tigers materialized immediately (accuracy: 80%)
Session 3: GTM pivot, 3 Tigers, recommendation "Conditional Go"
  → Condition met; 1 Tiger materialized (accuracy: 67%)

# Current session:
Feature launch intake → 6 Tigers identified → owners assigned → signals clear → recommendation "Go"
```

**Expected Output - Pattern Recognition:**
```
✓ Session completed: Feature launch pre-mortem
✓ Quality score: 87/100 (all Tigers have owners + signals + actions)
✓ Guardrails triggered: 2 ("Sales alignment", "Adoption friction")

🔁 PATTERN FOR META-SYNTHESIS:

Pre-mortem accuracy tracking (last 3 sessions):
  - Tiger materialization rate: 75–80% (model is well-calibrated)
  - "Sales alignment" Tigers have 100% materialization (strong signal)
  - "Adoption friction" Tigers have 67% materialization (less predictive)

Guardrail recommendation: Keep "Sales alignment" ACTIVE. Downgrade "Adoption friction" (false alarm rate too high).

Emerging pattern: Pre-mortems with named owners have 85% Tiger mitigation success.
Proposed learning for Section 7 (Meta-Learnings): "Named owner accountability in pre-mortem action plans drives 85% execution success vs. 40% when ownership is vague."
```

**Pass Criteria:**
- Full workflow completes (intake → scenarios → triage → recommendation → log)
- Quality score calculated and reflects Tiger completeness
- Guardrails surfaced at Step 0 (if applicable)
- Guardrails triggered count matches usage in session
- Session logged to `/context/skill-sessions.md` with all metadata
- Brain updates proposed for meta-synthesis
- Pattern signals extracted for pattern detection (if follow-up session exists, compare predicted vs. materialized Tigers)
- Output path recorded

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, user warned, can approve/skip |
| 2 | Brain context loading (pre-flight) | ICP, positioning, revenue levers inform scenarios |
| 3 | Failure scenario generation | 8-12 scenarios, initiative-specific, rooted in ICP |
| 4 | Risk classification | Tigers/Paper Tigers/Elephants aligned with risk appetite |
| 5 | Tiger triage completeness | All Tigers have named owner, signal, action plan |
| 6 | PMM recommendation clarity | Go / Conditional Go / Hold with clear reasoning |
| 7 | Session logging accuracy | Complete metadata logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Intake→Scenarios→Triage→Recommendation→Log, patterns detected |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke pre-mortem with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke pre-mortem with eval N test data]
# [validate against eval N pass criteria]
```

---

## Changelog

### v2.3.0 — 2026-06-22
Initial release: 8 comprehensive scenarios covering guardrail surfacing, brain context loading, failure scenario generation (initiative-specific), Tiger/Paper Tiger/Elephant classification, Tiger triage completeness (owner + signal + action), PMM recommendation clarity, logging accuracy, and end-to-end pattern detection for meta-synthesis.

Tests guardrail pre-flight, brain context integration, logging to `/context/skill-sessions.md`, and pattern signals for meta-synthesis monthly cycle. Includes pre-mortem accuracy tracking (comparing predicted vs. materialized Tigers) for calibration.

