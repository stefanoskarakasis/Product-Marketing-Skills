---
name: prioritization-frameworks.eval
version: 3.0.0
description: >
  Comprehensive eval suite for prioritization-frameworks skill. Tests: guardrail surfacing,
  brain context loading, framework selection accuracy, scoring integrity, Quality Gate enforcement,
  tier assignment accuracy, confidence score honesty, and Learning Close accuracy against the
  skill's real four-field session-log shape (Step 7 — new as of this skill version; the skill
  previously had no Learning Close step). 8 scenarios covering real prioritization scenarios and
  edge cases.
---

# Prioritization-Frameworks — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior prioritization-frameworks rows in the skill's real four-field shape (if testing Step 0 guardrail recall)
4. Runs prioritization-frameworks skill for given decision scenario
5. Validates outputs: framework selection, scoring quality, Quality Gate enforcement, tier assignment accuracy, Learning Close accuracy

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
pattern: "RICE scoring without win/loss data inflated Impact — Confidence corrected down from 85% to 55% during Quality Gates"
source: wrong

skill: prioritization-frameworks
session_date: 2026-06-12
pattern: "Same RICE-without-evidence Confidence inflation recurred on a second launch tier decision"
source: wrong

skill: prioritization-frameworks
session_date: 2026-06-15
pattern: "Third consecutive session where RICE Confidence was inflated absent win/loss data"
source: wrong
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
- Session logged at Step 7 per the skill's real Learning Close shape — see Eval 7

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
- Tier Assignment Card and Scoring Table appear in the chat-delivered Step 6 output — the Step 7 Learning Close row is a separate, minimal log entry, not a place these scores are duplicated

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

## Eval 7: Learning Close Accuracy (Step 7)

**Scenario:** Prioritization-frameworks skill session completes with framework selection → scoring → Quality Gates → tier translation → audit. Skill logs to `/context/skill-sessions.md` per its Step 7 Learning Close.

**Expected Output - Session Log:**
```yaml
skill: prioritization-frameworks
session_date: 2026-06-21
pattern: "RICE Confidence was self-assessed at 85% with no win/loss data — Quality Gate 2 caught the inflation and the tier was revised from T1 to T2."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly these four fields — `skill`, `session_date`, `pattern`, `source` — matching Step 7's template in `SKILL.md` verbatim. No additional fields.
- `pattern` is a single falsifiable statement about what happened this session, or the literal string `"none"` if nothing notable occurred — not a multi-field summary object.
- `source` is one of `surprised / wrong / missing / n.v.t.`
- The row is written directly, without asking the user for permission — this is a separate, mechanical write from anything the skill asks the user's go-ahead on (like where to save the Tier Assignment Card, Scoring Table, or Tier Rationale, per Outputs).
- If nothing notable happened this session, the row is still written with `pattern: none` — the log entry is never skipped.
- Neither the Quality Gate results, the tier assignment, nor the scoring table are duplicated into the log row — those live in the Step 6 chat output only.

---

## Eval 8: End-to-End Prioritization, Full Workflow

**Scenario:** User runs prioritization-frameworks end-to-end: intake → framework selection → scoring → Quality Gates → tier translation → audit → Learning Close.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior prioritization-frameworks rows, real shape)
skill: prioritization-frameworks
session_date: 2026-06-10
pattern: "RICE without win/loss data inflated Confidence — tier revised down from T1 to T2 after Quality Gates"
source: wrong

skill: prioritization-frameworks
session_date: 2026-06-12
pattern: "ICE framework applied with full evidence trail — all Quality Gates passed on first pass"
source: n.v.t.

skill: prioritization-frameworks
session_date: 2026-06-15
pattern: "Risk vs Reward used for new-market entry with no local data — recommended a validation sprint before scoring"
source: surprised

# Current session:
Feature launch intake → RICE selected → Confidence self-assessed 85% with no win/loss data →
Quality Gate 2 flags inflation → tier revised T1 → T2
```

**Expected Output - Full Workflow:**
```
✓ Session completed: Feature launch prioritization
✓ Framework: RICE
✓ Quality Gates: Gate 1 and Gate 2 failed, corrected before delivery
✓ Tier: T2 (revised down from T1 after Confidence correction)
✓ Session logged (Step 7):
  skill: prioritization-frameworks
  session_date: 2026-06-21
  pattern: "Third consecutive session where RICE Confidence needed correction absent win/loss data — recommend surfacing this as a candidate guardrail."
  source: surprised
```

Note that pattern-across-sessions detection (comparing this session's row against the three prior rows to spot a recurring theme) is the job of `meta-synthesis`, run separately against the full `/context/skill-sessions.md` log — prioritization-frameworks' own Step 7 only ever writes its own single row. This skill does not itself detect or report cross-session patterns; it just logs an honest, falsifiable observation about this one session.

**Pass Criteria:**
- Full workflow completes (intake → selection → scoring → gates → tier → audit → Learning Close)
- Guardrails surfaced at Step 0 (if `/context/meta-patterns.md` has an applicable, 2+-occurrence pattern)
- Quality Gates caught issues before tier delivery (Step 3), tier revised before Step 4 output
- Session logged to `/context/skill-sessions.md` with the real four-field shape — not a richer schema
- The skill does not attempt cross-session pattern synthesis itself — that's `meta-synthesis`'s job, not prioritization-frameworks'

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
| 7 | Learning Close accuracy | Real four-field row (`skill`/`session_date`/`pattern`/`source`) logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Intake→Selection→Scoring→Gates→Tier→Audit→Learning Close, no cross-session synthesis attempted by this skill |

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
