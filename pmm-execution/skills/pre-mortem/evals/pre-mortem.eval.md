---
name: pre-mortem.eval
version: 2.4.0
description: >
  Comprehensive eval suite for pre-mortem skill. Tests: guardrail surfacing,
  brain context loading, failure scenario generation quality, Tiger/Paper Tiger/Elephant classification accuracy,
  Tiger triage completeness (owner + signal + action plan), PMM recommendation clarity, and Learning Close
  accuracy against the skill's real four-field session-log shape. 8 scenarios covering real initiative types
  and edge cases.
---

# Pre-Mortem — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior pre-mortem rows in the skill's real four-field shape (if testing Step 0 guardrail recall)
4. Runs pre-mortem skill for given initiative
5. Validates outputs: risk classification quality, Tiger triage completeness, recommendation clarity, Learning Close accuracy

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
pattern: "Pricing initiative without a competitive posture check surfaced a Tiger that could have been caught earlier"
source: wrong

skill: pre-mortem
session_date: 2026-06-15
pattern: "Same pattern recurred on Enterprise Tier Launch — pricing pre-mortems keep missing competitive posture until Tiger triage"
source: wrong
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
- Session logged at Step 7 per the skill's real Learning Close shape — see Eval 7

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
- Classification counts appear in the chat-delivered Tiger triage output (not in the session log — the Learning Close row logged at Step 7 carries only `skill`, `session_date`, `pattern`, `source`, not per-session counts)

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
- Owner + Signal + Action appear in the chat-delivered Tiger triage output — the Step 7 Learning Close row is a separate, minimal log entry, not a place this detail is duplicated

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
- Recommendation is delivered in chat as part of the triage output; the Step 7 Learning Close row does not duplicate it

---

## Eval 7: Learning Close Accuracy (Step 7)

**Scenario:** Pre-mortem skill session completes with failure scenarios → classification → Tiger triage → recommendation. Skill logs to `/context/skill-sessions.md` per its Step 7 Learning Close.

**Expected Output - Session Log:**
```yaml
skill: pre-mortem
session_date: 2026-06-21
pattern: "Feature launches without a named sales-alignment owner correlated with Tiger risks materializing in this session's triage — worth watching across future launches."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly these four fields — `skill`, `session_date`, `pattern`, `source` — matching Step 7's template in `SKILL.md` verbatim. No additional fields.
- `pattern` is a single falsifiable statement about what happened this session, or the literal string `"none"` if nothing notable occurred — not a multi-field summary object.
- `source` is one of `surprised / wrong / missing / n.v.t.`
- The row is written directly, without asking the user for permission — this is a separate, mechanical write from anything the skill asks the user's go-ahead on (like where to save the Tiger triage output, per Outputs).
- If nothing notable happened this session, the row is still written with `pattern: none` — the log entry is never skipped.

---

## Eval 8: End-to-End Pre-Mortem, Full Workflow

**Scenario:** User runs pre-mortem end-to-end: intake → failure scenarios → classification → Tiger triage → recommendation → Learning Close.

**Test Data:**
```yaml
# /context/skill-sessions.md (2 prior pre-mortem rows, real shape)
skill: pre-mortem
session_date: 2026-05-10
pattern: "Feature launch pre-mortem — sales-alignment Tiger was under-scoped, materialized as a launch blocker"
source: wrong

skill: pre-mortem
session_date: 2026-06-01
pattern: "Pricing-change pre-mortem — same sales-alignment Tiger pattern recurred"
source: wrong

# Current session:
Feature launch intake → 6 Tigers identified → owners assigned → signals clear → recommendation "Go"
```

**Expected Output - Full Workflow:**
```
✓ Session completed: Feature launch pre-mortem
✓ Tiger triage: 6 Tigers, all with named owner + measurable signal + action plan
✓ Recommendation: Go
✓ Session logged (Step 7):
  skill: pre-mortem
  session_date: 2026-06-21
  pattern: "Third consecutive session where sales-alignment was the highest-risk Tiger — recommend surfacing this as a candidate guardrail."
  source: surprised
```

Note that pattern-across-sessions detection (comparing this session's row against the two prior rows to spot a recurring theme) is the job of `meta-synthesis`, run separately against the full `/context/skill-sessions.md` log — pre-mortem's own Step 7 only ever writes its own single row. This skill does not itself detect or report cross-session patterns; it just logs an honest, falsifiable observation about this one session.

**Pass Criteria:**
- Full workflow completes (intake → scenarios → triage → recommendation → Learning Close)
- Guardrails surfaced at Step 0 (if `/context/meta-patterns.md` has an applicable, 2+-occurrence pattern)
- Session logged to `/context/skill-sessions.md` with the real four-field shape — not a richer schema
- The skill does not attempt cross-session pattern synthesis itself — that's `meta-synthesis`'s job, not pre-mortem's

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
| 7 | Learning Close accuracy | Real four-field row (`skill`/`session_date`/`pattern`/`source`) logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Intake→Scenarios→Triage→Recommendation→Learning Close, no cross-session synthesis attempted by this skill |

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
