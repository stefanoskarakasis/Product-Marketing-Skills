---
name: beachhead-segment.eval
version: 2.1.0
description: >
  Comprehensive eval suite for beachhead-segment skill. Tests: guardrail surfacing,
  brain context loading, candidate decomposition, four-dimension scoring accuracy,
  blocking gate enforcement, assumption flagging, expansion pathway completeness,
  elimination documentation, and Learning Close accuracy against the skill's real
  four-field session-log shape. 8 scenarios covering real beachhead decisions and
  edge cases.
---

# Beachhead-Segment — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior beachhead rows in the skill's real four-field shape (if testing Step 0 guardrail recall)
4. Runs beachhead-segment skill for given decision scenario
5. Validates outputs: scoring accuracy, gate enforcement, assumption handling, Learning Close accuracy

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "Segments with Burning Pain <3 have never sustained beachhead status past 18 months → Surface Pain floor risk before scoring". User runs /score on three segments without stating their pain levels. Skill should surface guardrail before scoring.

**Test Data:**
```yaml
# /context/meta-patterns.md
guardrail_1:
  text: "Low Burning Pain segments do not sustain beachhead"
  trigger: "Beachhead scoring session"
  action: "Surface Pain floor risk before scoring begins"
  status: ACTIVE
  confirmation_count: 2

# /context/skill-sessions.md
skill: beachhead-segment
session_date: 2026-06-10
pattern: "Segment recommended with Burning Pain 2 never scaled past initial rollout"
source: wrong

skill: beachhead-segment
session_date: 2026-06-15
pattern: "Same pattern recurred — low-Pain segment recommended, churned in year 2"
source: wrong
```

**Expected Output - Guardrail Surfaced:**
```
🔁 PATTERN FROM PRIOR BEACHHEAD DECISIONS

I've seen segments with low Burning Pain fail to sustain status.
Examples: [prior segment names from 2+ sessions]

Quick check: Do your candidates have acute pain signals?
- If YES → We'll validate during scoring
- If NO → Watch this closely; we may re-evaluate mid-year
```

**Pass Criteria:**
- Guardrail surfaces before scoring starts
- Pattern count accurate (2+ prior occurrences)
- User can acknowledge or skip
- Session logged at Step 6 per the skill's real Learning Close shape — see Eval 7

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` exists with populated Sections 2, 3, 4, 5. Skill loads silently and references during scoring.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Current: "Mid-market B2B SaaS, 50–500 employees"

## Section 3: Positioning
Angle: "For ops leaders measuring impact, not activity"

## Section 4: Competitive landscape
Fintech: Dominated by Stripe, Square — high switching costs
Healthcare: Fragmented, 3–4 mid-tier players — moderate switching costs
Logistics: Nascent, no dominant player — low switching costs

## Section 5: Proof points
Fintech: 5 customers, all from fintech vertical. $2M ARR.
Healthcare: 2 customers, mixed health/medtech. $400K ARR.
```

**Expected Output - Context Referenced:**
```
✓ Brain context loaded:
  - ICP: Mid-market SaaS (grounding segment candidates)
  - Positioning: Outcome-first (informs feature-fit signals)
  - Competitive: Fintech dominated (informs Winnability), Logistics nascent (informs Winnability)
  - Proof points: Fintech best-validated (informs Burning Pain + WTP)

Winnability signals by segment:
  - Fintech: Low (Stripe/Square entrenched)
  - Healthcare: Medium (moderate competitive fragmentation)
  - Logistics: High (nascent, no dominant player)
```

**Pass Criteria:**
- Brain sections loaded silently
- ICP informs candidate relevance
- Competitive landscape informs Winnability scoring
- Proof points informs Burning Pain + WTP scoring

---

## Eval 3: Gate 1 (Pain Floor) Enforcement

**Scenario:** Three segments scored. Segment A scores Burning Pain=2, Segment B=4, Segment C=3. Skill applies Gate 1 before producing recommendation.

**Test Data:**
```
Segment A (Enterprise): Burning Pain = 2
  - Long procurement cycles, problem is chronic transformation, not acute
  - Expected: Eliminated by Gate 1

Segment B (Mid-market): Burning Pain = 4
  - Active inbound, budget exists, problem is top 2 priority
  - Expected: Passes Gate 1

Segment C (SMB): Burning Pain = 3
  - Problem acknowledged, competes for budget, some urgency
  - Expected: Passes Gate 1
```

**Expected Output - Gate 1 Applied:**
```
Gate 1 — Pain floor (≥3):
✅ [Segment B]: Burning Pain 4 — PASS
✅ [Segment C]: Burning Pain 3 — PASS
❌ [Segment A]: Burning Pain 2 — ELIMINATED

Reason for elimination: "Chronic problem, not acute. Long sales cycles. Low GTM urgency."

Recommendation proceeds from Segments B and C only.
```

**Pass Criteria:**
- Segment A explicitly eliminated with specific score and reason
- Segments B and C proceed to Gate 2
- No segment <3 passes through Gate 1

---

## Eval 4: Assumption Flagging and Confidence Capping

**Scenario:** Top-scoring segment has 3 of 4 dimensions marked `[A]` (assumption). Skill flags this and caps confidence.

**Test Data:**
```
Segment: Healthcare ops teams

Burning Pain: 4 (evidence: 2 customer conversations)
Willingness to Pay: 3 [A] (no proof point on ROI, customer budget unknown)
Winnability: 2 [A] (competitive landscape untested in healthcare)
Referral Potential: 3 [A] (no data on healthcare ops community tightness)

Assumption count: 3 of 4 = exceeds threshold of 2
```

**Expected Output - Confidence Capped:**
```
🟡 CONDITIONAL RECOMMENDATION

Assumptions flagged: 3 of 4 dimensions
- [A] Willingness to Pay: No proof point on healthcare ROI
- [A] Winnability: Competitive position untested in healthcare
- [A] Referral Potential: Community structure unknown

Confidence capped at 🟡 (Medium)

Validation needed before GTM investment:
1. Interview 5 healthcare ops leaders on budget authority and ROI frame
2. Audit competitive landscape in healthcare ops vertical
3. Research healthcare ops community / peer networks

Recommend: Run a 2-week discovery sprint before committing GTM budget.
```

**Pass Criteria:**
- All `[A]` marks visible on scorecard
- Confidence capped at 🟡 (not 🟢)
- Specific validation actions named (not vague "gather more data")

---

## Eval 5: Expansion Pathway Completeness

**Scenario:** Beachhead recommended. Skill produces expansion pathway with at least two stages beyond beachhead.

**Test Data:**
```
Recommended Beachhead: Mid-market ops teams (50–200 employees)

Expansion candidates:
- Adjacent 1: Enterprise ops teams (500+ employees)
- Adjacent 2: SMB ops teams (20–50 employees)
- Adjacent 3: Healthcare ops specialization

Triggers for stage progression:
- Beachhead → Adjacent 1: 5 reference customers in mid-market + analyst coverage
- Adjacent 1 → Adjacent 2: Enterprise deal closes + proof of complex integration
- Adjacent 2 → Adjacent 3 (future): SMB motion proves repeatable, team bandwidth exists
```

**Expected Output - Pathway Shown:**
```
## Expansion Pathway

**Stage 1 — Beachhead (Now):** Mid-market ops teams (50–200 employees)
  Why: Acute pain (process standardization), moderate budget, lower switching costs

**Stage 2 — Adjacent (Q2 2027):** Enterprise ops teams (500+ employees)
  Why: Beachhead proof validates enterprise ROI case; enterprise budgets larger
  Trigger: 5 mid-market reference customers + analyst coverage

**Stage 3 — Secondary (Q4 2027):** SMB ops teams (20–50 employees)
  Why: SMB motion repeatable after enterprise playbook proven; high volume
  Trigger: Enterprise motion scaling and predictable; team bandwidth available

Risk: If enterprise adoption slower than expected, push SMB to Q2 2028.
```

**Pass Criteria:**
- At least 2 stages beyond beachhead (3 total)
- Each stage has "why" rationale
- Explicit triggers for moving between stages
- Risk callout included

---

## Eval 6: Eliminated Segments Documentation

**Scenario:** Five segments scored. Two eliminated by gates, one marked as "future roadmap". Skill documents all eliminations with specific reasons.

**Test Data:**
```
Scored segments:
1. Enterprise (eliminated by Gate 1: Pain 2)
2. Mid-market (recommended beachhead)
3. Healthcare (eliminated by Gate 2: Winnability 2)
4. SMB (flagged as future roadmap: Winnability 2)
5. Logistics (conditional: high assumptions, score 14/20)
```

**Expected Output - Eliminations Shown:**
```
## Eliminated Segments

| Segment | Gate | Score | Reason |
|---|---|---|---|
| Enterprise | Gate 1 — Pain floor | Pain 2, WTP 4, Win 4, Referral 3 (13/20) | Chronic problem, not acute. Long procurement cycles mean GTM lag. |
| Healthcare | Gate 2 — Winnability floor | Pain 4, WTP 3, Win 2, Referral 3 (12/20) | Incumbent [CompetitorX] owns 65% market. Switching costs prohibitive. |

## Future Roadmap
SMB (Winnability 2) — Monitor for competitive shifts. Revisit if [CompetitorY] exits market.

## Recommendation
Proceed with: Mid-market (15/20, confidence 🟢)
Conditional: Logistics (14/20, confidence 🟡 — validate assumptions first)
```

**Pass Criteria:**
- Every eliminated segment has specific reason (not "didn't score well")
- Gate applied is named (Gate 1, Gate 2, or decision-based)
- Score shown alongside reason
- Future roadmap segments segregated from eliminated ones

---

## Eval 7: Learning Close Accuracy (Step 6)

**Scenario:** Beachhead-segment skill session completes with four-dimension scoring → gates → recommendation → (optional) brain write. Skill logs to `/context/skill-sessions.md` per its Step 6 Learning Close.

**Expected Output - Session Log:**
```yaml
skill: beachhead-segment
session_date: 2026-06-21
pattern: "Mid-market ops teams scored 4/4/4/3 and passed both gates cleanly — Referral Potential (3, not the top dimension) still carried the recommendation over a higher-Winnability segment, worth watching whether that trade-off holds."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly these four fields — `skill`, `session_date`, `pattern`, `source` — matching Step 6's template in `SKILL.md` verbatim. No additional fields.
- `pattern` is a single falsifiable statement about what happened this session, or the literal string `"none"` if nothing notable occurred — not a multi-field summary object.
- `source` is one of `surprised / wrong / missing / n.v.t.`
- The row is written directly, without asking the user for permission — this is a separate, mechanical write from the brain Section 2 write (Step 5), which does require explicit user confirmation.
- If nothing notable happened this session, the row is still written with `pattern: none` — the log entry is never skipped.

---

## Eval 8: End-to-End Beachhead Decision, Full Workflow

**Scenario:** User runs full beachhead session: candidate identification → four-dimension scoring → gates → recommendation → brain write (on confirmation) → Learning Close.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior beachhead rows, real shape)
skill: beachhead-segment
session_date: 2026-05-05
pattern: "Enterprise rejected at Gate 1 (Pain 2); Mid-market chosen (Pain 4) — segment expanded successfully 18 months later"
source: n.v.t.

skill: beachhead-segment
session_date: 2026-05-20
pattern: "Fintech rejected at Gate 2 (Winnability 2); SMB chosen (Winnability 4) — SMB motion stalled at 12 months despite passing gates"
source: wrong

skill: beachhead-segment
session_date: 2026-06-05
pattern: "Healthcare chosen with 3 of 4 dimensions marked [A] — struggled with adoption friction in first 6 months, consistent with the assumption-density warning"
source: surprised

# Current session:
Segments: Fintech vs Healthcare vs Logistics
Scores generated → Gates applied → Recommendation made → Brain write confirmed → Learning Close
```

**Expected Output - Full Workflow:**
```
✓ Session completed: Beachhead decision (Fintech vs Healthcare vs Logistics)
✓ Gates applied: Pain floor (1 eliminated), Winnability floor (0 flagged), Assumption density (passed)
✓ Recommendation: Logistics (14/20, confidence 🟢)
✓ Brain Section 2 updated (confirmed)
✓ Session logged (Step 6):
  skill: beachhead-segment
  session_date: 2026-06-21
  pattern: "Third consecutive session where the passing segment had a Winnability score below the highest-scored alternative on other dimensions — worth watching as a candidate guardrail."
  source: surprised
```

Note that pattern-across-sessions detection (comparing this session's row against the three prior rows to spot a recurring theme) is the job of `meta-synthesis`, run separately against the full `/context/skill-sessions.md` log — beachhead-segment's own Step 6 only ever writes its own single row. This skill does not itself detect or report cross-session patterns; it just logs an honest, falsifiable observation about this one session. The rich scoring output (four dimensions, gates, elimination reasons, expansion pathway) is delivered in chat per Step 4's template — none of that detail is duplicated into the session log.

**Pass Criteria:**
- Full workflow completes (candidates → scoring → gates → recommendation → brain write on confirmation → Learning Close)
- Guardrails surfaced at Step 0 (if `/context/meta-patterns.md` has an applicable, 2+-occurrence pattern)
- Session logged to `/context/skill-sessions.md` with the real four-field shape — not a richer schema
- The skill does not attempt cross-session pattern synthesis itself — that's `meta-synthesis`'s job, not beachhead-segment's

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, user warned, can acknowledge/skip |
| 2 | Brain context loading (pre-flight) | ICP, positioning, competitive, proof points inform scoring |
| 3 | Gate 1 (Pain floor) enforcement | Segments <3 eliminated with specific reason |
| 4 | Assumption flagging & confidence | `[A]` marks visible, confidence capped at 🟡 if >2 assumptions |
| 5 | Expansion pathway completeness | ≥2 stages beyond beachhead, explicit triggers |
| 6 | Elimination documentation | Every eliminated segment has specific gate + reason |
| 7 | Learning Close accuracy | Real four-field row (`skill`/`session_date`/`pattern`/`source`) logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Candidates→Scoring→Gates→Recommendation→Brain write→Learning Close, no cross-session synthesis attempted by this skill |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke beachhead-segment with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke beachhead-segment with eval N test data]
# [validate against eval N pass criteria]
```
