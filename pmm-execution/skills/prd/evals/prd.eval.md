---
name: prd.eval
version: 2.3.0
description: >
  Comprehensive eval suite for prd skill. Tests: guardrail surfacing,
  brain context loading, intake quality, Solution Story generation, PRD structure completeness,
  PM+PMM collaboration checkpoints, logging accuracy, and pattern detection for meta-synthesis.
  8 scenarios covering real PRD workflows and edge cases.
---

# PRD — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 4, 5, 7)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior PRD sessions (if testing pattern detection)
4. Runs prd skill for given scenario
5. Validates outputs: Solution Story quality, PRD completeness, session logging, guardrail triggers

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "Success metrics undefined in 2 prior PRDs → Ask baseline + target upfront". User triggers PRD skill without specifying success metrics. Skill should surface guardrail before intake.

**Test Data:**
```yaml
# /context/meta-patterns.md
guardrail_1:
  text: "Success metrics undefined in 2 prior PRDs"
  trigger: "PRD intake without success metric clarity"
  action: "Ask baseline + target in Round 1"
  status: ACTIVE

# /context/skill-sessions.md
skill: prd
session_date: 2026-06-10
feature_name: "User Dashboard"
success_metrics_defined: false

skill: prd
session_date: 2026-06-15
feature_name: "Analytics Export"
success_metrics_defined: false
```

**Expected Output - Guardrail Surfaced:**
```
🔁 PATTERN DETECTED FROM PRIOR PRDS

I've seen success metrics undefined in 2 prior PRDs this cycle.
Examples: "User Dashboard", "Analytics Export"

Quick check: Do you have a baseline and target metric in mind?
- If YES → proceed to intake
- If NO → we'll define this first
```

**Pass Criteria:**
- Guardrail surface before Step 1 intake
- Pattern count accurate (2 prior occurrences)
- User can approve/skip guardrail

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` exists with populated Positioning (§3), ICP (§2), Personas (§4), Revenue Levers (§5). Skill should load silently and reference during intake.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Primary: Mid-market B2B SaaS, 50-500 employees, marketing ops teams

## Section 3: Positioning
Unique angle: "For ops leaders who want to measure impact, not just activity"
Key differentiator: Outcome-first analytics, not output metrics

## Section 4: Personas
Primary: Sarah, VP Marketing Ops, 15 years experience, frustrated with visibility

## Section 5: Revenue Levers
Lever 1: Time-to-value (setup speed)
Lever 2: Outcome visibility (customer success metric)
Lever 3: Team collaboration (multiple stakeholders)
```

**Expected Output - Context Referenced:**
```
✓ Brain context loaded:
  - ICP: Mid-market B2B SaaS (pre-filling target customer)
  - Positioning: Outcome-first analytics (anchor for Solution Story)
  - Personas: Sarah, VP Marketing Ops (primary user in PRD)
  - Revenue: Setup speed as lever (feature should accelerate)

Target customer from brain ICP: [pre-filled from Section 2]
Success metric inspiration from Revenue Levers: [pre-filled from Section 5]
```

**Pass Criteria:**
- Brain sections loaded silently at pre-flight
- ICP pre-fills target customer field
- Positioning anchors Solution Story framing
- Revenue Levers inform feature alignment check

---

## Eval 3: Intake Quality (Conversational, Two Rounds)

**Scenario:** User provides no existing notes, triggers PRD skill from scratch. Skill should run conversational intake (Round 1 → Round 2), avoid all-at-once questions, detect role.

**Test Data:**
User input: "I want to write a PRD for a new feature but I'm not sure where to start."

**Expected Output - Conversational Intake:**
```
Round 1 response (4 questions grouped):
1. What's the feature or initiative name?
2. Who is the target customer? [Note: Based on your brain ICP, I'm thinking mid-market ops leaders — does that fit?]
3. What problem does it solve? (Rough answer is fine)
4. What's the one outcome you most want to achieve?

[Wait for answers]

[After Round 1 answered]

Round 2 response (5 questions):
5. What evidence do you have the problem is real?
6. Who's on the team? (PM, PMM, Design, etc.)
7. Timeline or key dates?
8. Is this an experiment or direct rollout?
9. What's the announcement level? (P1 Major / P2 Notable / P3 Improvement / P4 Minor)
```

**Pass Criteria:**
- Round 1 and Round 2 separated (not all 9 at once)
- Questions are conversational (not robotic lists)
- Brain context referenced where relevant (ICP, personas)
- Placeholders offered if user is impatient

---

## Eval 4: Solution Story Generation Quality

**Scenario:** User completes Round 1 intake with clear problem statement. Skill generates Solution Story with writing rules applied (status quo first, causal logic, customer outcome focus).

**Test Data:**
User answers:
- Feature: "Bulk User Imports"
- Target: "Operations teams managing 500+ users"
- Problem: "Manual CSV import is error-prone and takes 8 hours per cycle"
- Outcome: "Reduce onboarding time from 8 hours to 30 minutes"

**Expected Output - Solution Story:**
```
## Solution Story — Bulk User Imports

### Feature Identity
- Feature Name: Bulk User Imports
- Tagline: Faster onboarding
- Short Value Description: Reduce manual user setup from 8 hours to 30 minutes with error-free bulk imports
- Announcement Level: P2 Notable — solves recurring ops bottleneck for 40% of user base

### The One-Paragraph Pitch
[Opens with status quo]: "Right now, ops teams manually import hundreds of users through a CSV interface that flags errors row-by-row, forcing them to fix and re-import. This process takes 8 hours per major onboarding cycle and introduces human error — 2-3% of imports fail validation.

[Solution]: Our new Bulk User Importer validates the entire CSV before importing, highlights errors in-place, and auto-retries valid rows. Imports run in parallel.

[Benefit]: Teams can onboard 500+ users in under 30 minutes, zero manual rework."

### Press Paragraph
[3–4 sentences, press-ready]

### Customer Proof Points
1. Automation reduces ops friction — "We went from dreading user onboarding cycles to shipping in 30 mins flat" (Customer testimonial)
2. Error prevention saves hours — Data: 2-3% of manual imports fail validation; this eliminates that category entirely
3. Ops alignment — Reduces hand-offs between product and customer success teams
```

**Pass Criteria:**
- Opens with broken status quo (not "Introducing…")
- Names pain specifically (8 hours, 2-3% failure rate)
- Solution sentence feels inevitable
- Closes on customer outcome (30 mins, zero rework)
- 4-6 sentences, read naturally (no press-release speak)

---

## Eval 5: Full PRD Structure Completeness

**Scenario:** User approves Solution Story. Skill generates full PRD with all 10 sections, clear ownership, placeholders labeled, no silent blanks.

**Expected Output - Full PRD:**
```
✓ Document Header (name, author, date, version, status)
✓ Section 00 — Team (roles, names, responsibilities table)
✓ Section 01 — Solution Story Summary (tagline + pitch + proof points)
✓ Section 02 — Problem & Background (2.1 statement, 2.2 market, 2.3 personas)
✓ Section 03 — Goals & Success Metrics (output + input metrics, non-goals, alignment)
✓ Section 04 — Requirements & User Stories (high-level solution, milestones, user stories table, open questions)
✓ Section 05 — User Experience (Figma, design principles, journey, accessibility)
✓ Section 06 — Technical Requirements (stack, architecture, integrations, security, performance, scalability)
✓ Section 07 — Launch Plan (experiment design, rollout phases, rollback criteria, GTM)
✓ Section 08 — Milestones & Risks (key dates, risk table)
✓ Section 09 — Sign-Off (approval roles and dates)

Every placeholder labeled: [TO FILL — hint about what goes here]
No silent blanks (every section either filled or labeled)
```

**Pass Criteria:**
- All 10 sections present
- Clear ownership (PM, PMM, Design, Engineering)
- No blank sections
- Every placeholder labeled with hint
- Markdown format, copy-paste ready

---

## Eval 6: PM + PMM Collaboration Checkpoints

**Scenario:** Full PRD generated with checkpoints surfaced at §01, §04, §07. Checkpoints clearly mark when PM + PMM should sync.

**Expected Output - Checkpoints Surfaced:**
```
🤝 PM + PMM Checkpoint #1 (After §01 — Solution Story)
Run a 30-min kick-off sync before filling §02–§04.
PM confirms: Is the pitch technically accurate? Are we missing constraints?
PMM flags: Does messaging land? Any customer objections we should anticipate?

[Output is locked until PM + PMM confirm alignment]

🤝 PM + PMM Checkpoint #2 (After §04 — User Stories)
Before engineering kickoff, review P0 user stories together.
PMM question: Can I build launch messaging from these stories alone?
Gap check: Are there promises we've made to customers that aren't captured?

[Engineering doesn't start until both approve §04]

🤝 PM + PMM Checkpoint #3 (At §07 — Launch Plan)
GTM handoff meeting (1 hour).
PM brings: Final scope + experiment design + rollout plan
PMM brings: Draft launch copy + sales enablement outline
Align on: Go/no-go criteria + success definitions
```

**Pass Criteria:**
- 3 checkpoints surfaced at correct sections (§01, §04, §07)
- Each checkpoint names what PM and PMM must discuss
- Checkpoints create deliberate sync points, not suggestions
- Outcome of checkpoint is explicit (approval before next step)

---

## Eval 7: Session Logging Accuracy (Step 7)

**Scenario:** PRD skill session completes with full PRD generated, Solution Story approved, 2 collaboration checkpoints surfaced, brain context loaded. Skill logs to `/context/skill-sessions.md`.

**Expected Output - Session Log:**
```yaml
skill: prd
session_date: 2026-06-21
feature_name: "Bulk User Imports"
prd_sections_completed: 10
solution_story_generated: true
quality_score: 85
guardrails_triggered:
  - "Success metrics undefined" (addressed in intake Round 1)
brain_context_loaded: true
brain_sections_referenced:
  - "Positioning (Section 3)"
  - "ICP (Section 2)"
  - "Revenue Levers (Section 5)"
brain_updates_proposed:
  - "Section 7: New pattern — announcement-level clarity in Round 1 improves PRD focus"
pm_pmm_collaboration: true
collaboration_checkpoints_surfaced: 3
checkpoints_approved: 2
output_path: "/artifacts/prd/bulk-user-imports-v1.0.md"
decision: "approved"
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md`
- All metadata fields populated (feature name, sections, quality score, guardrails, brain refs)
- Guardrails triggered listed
- Brain updates proposed
- Collaboration checkpoints counted
- Output path recorded
- Decision field shows "approved" or "draft"

---

## Eval 8: End-to-End PRD Workflow with Pattern Detection

**Scenario:** User runs PRD skill end-to-end: scratch intake → Solution Story → Full PRD → Collaboration checkpoints → Logging. Test detects that guardrails surfaced were useful, and logs pattern for meta-synthesis.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior PRD sessions)
Session 1: Success metrics undefined → surfaced guardrail, user fixed in intake
Session 2: Problem statement vague → surfaced guardrail, user sharpened
Session 3: Missing rollback criteria → NOT surfaced, discovered in review

# Current session:
Step 0: Guardrail surfaces 2 matches
Step 2: Intake runs, addresses both guardrails
Step 7: Log session with pattern signals
```

**Expected Output - Pattern Recognition:**
```
✓ Session completed: Bulk User Imports PRD
✓ Quality score: 85/100
✓ Guardrails triggered: 2 (success metrics, problem statement)
✓ Both guardrails useful: User proactively addressed before Session Review

🔁 PATTERN FOR META-SYNTHESIS:
Guardrail "Success metrics undefined" has fired 3x this cycle.
Guardrail "Problem statement vague" has fired 2x this cycle.
Recommendation: Keep both ACTIVE for next quarter.

Emerging pattern: When guardrails surface early (pre-flight), PRD quality improves 12-15 points.
Proposed learning: "Guardrail intake is worth 1-2 hours of rework later"
```

**Pass Criteria:**
- Full workflow completes (scratch → Story → PRD → Checkpoints → Log)
- Quality score calculated and logged
- Guardrails surfaced at Step 0
- Guardrails triggered count matches usage in session
- Session logged to `/context/skill-sessions.md` with all metadata
- Pattern signals extracted for meta-synthesis
- Output path recorded

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, user warned, can proceed/skip |
| 2 | Brain context loading (pre-flight) | ICP, positioning, personas, revenue pre-fill + anchor |
| 3 | Intake quality (conversational) | Round 1 + Round 2 separated, no all-at-once |
| 4 | Solution Story generation | Status quo first, causal logic, outcome-focused |
| 5 | Full PRD structure | 10 sections, clear ownership, labeled placeholders |
| 6 | PM + PMM checkpoints | 3 checkpoints surfaced, explicit approval gates |
| 7 | Session logging accuracy | Complete metadata logged to `/context/skill-sessions.md` |
| 8 | End-to-end workflow | Scratch→Story→PRD→Checkpoints→Log complete, patterns detected |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke prd with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke prd with eval N test data]
# [validate against eval N pass criteria]
```

---

## Changelog

### v2.3.0 — 2026-06-21
Initial release: 8 comprehensive scenarios covering guardrail surfacing, brain context loading, conversational intake, Solution Story quality, PRD completeness, PM+PMM checkpoints, logging accuracy, and end-to-end pattern detection for meta-synthesis.

Tests guardrail pre-flight, brain context integration, logging to `/context/skill-sessions.md`, and pattern signals for meta-synthesis monthly cycle.
