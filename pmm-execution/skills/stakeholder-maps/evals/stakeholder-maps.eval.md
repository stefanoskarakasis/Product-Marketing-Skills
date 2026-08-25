---
name: stakeholder-maps.eval
version: 2.4.0
description: >
  Comprehensive eval suite for stakeholder-maps skill. Tests: guardrail surfacing,
  brain context loading, inversion check quality, Power × Interest classification accuracy,
  political role assignment rigor, conflict mapping completeness, silent blocker identification,
  sprint card execution clarity, and Learning Close accuracy against the skill's real
  four-field session-log shape. 9 scenarios covering real GTM initiative types and
  stakeholder political dynamics.
---

# Stakeholder-Maps — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior stakeholder-maps rows in the skill's real four-field shape (if testing Step 0 guardrail recall)
4. Runs stakeholder-maps skill for given initiative
5. Validates outputs: inversion check rigor, classification accuracy, role assignment, conflict mapping, Learning Close accuracy

---

## Eval 1: Guardrail Surfacing (Step 0)

**Scenario:** `/context/meta-patterns.md` exists with guardrail "Product launches without Sales Manage Closely engagement and written commitment have failed 3 times → Always surface Sales Performer risk". User triggers stakeholder skill for a product launch without mentioning Sales alignment. Skill should surface guardrail before intake.

**Test Data:**
```yaml
# /context/meta-patterns.md
guardrail_1:
  text: "Product launches without Sales Manage Closely engagement fail"
  trigger: "Product launch stakeholder map"
  action: "Surface Sales Performer risk before mapping"
  status: ACTIVE
  confirmation_count: 3

# /context/skill-sessions.md (3 prior product launch maps, real shape)
skill: stakeholder-maps
session_date: 2026-06-10
pattern: "Product launch stakeholder map — Sales VP was a Performer (verbal yes, no written enablement commitment), launch slipped"
source: wrong

skill: stakeholder-maps
session_date: 2026-06-12
pattern: "Same Sales Performer pattern recurred on a second product launch — verbal commitment without enablement follow-through"
source: wrong

skill: stakeholder-maps
session_date: 2026-06-15
pattern: "Third consecutive product launch where an unwritten Sales commitment preceded a launch delay"
source: wrong
```

**Expected Output - Guardrail Surfaced:**
```
🔁 PATTERN FROM PRIOR STAKEHOLDER MAPS

I've seen product launches without Sales Manage Closely engagement fail 3 times.
Watch for Sales Performers — folks who say yes in the room but don't commit in writing.

Quick check: Do you have written Sales VP buy-in on this launch?
- If YES → We'll build Sales enablement tracking into Watch For signals
- If NO → Let's identify the Sales hold-up before mapping
```

**Pass Criteria:**
- Guardrail surfaces before Step 1 intake
- Pattern count accurate (3 prior occurrences)
- User can acknowledge or skip
- Session logged at Step 7 per the skill's real Learning Close shape — see Eval 7

---

## Eval 2: Brain Context Loading (Pre-flight)

**Scenario:** `/foundation/brain.md` exists with populated ICP (§2), Positioning (§3), GTM Motion (§5). Skill should load and inform which stakeholders matter and what their power is.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Primary: Mid-market ops teams, 50-500 employees
Secondary: Enterprise ops, 500+ employees (lower growth)

## Section 3: Positioning
Unique angle: "For ops leaders who measure impact, not activity"
GTM narrative: Outcome-first analytics

## Section 5: GTM Motion & Growth Loops
Primary motion: Sales-led (enterprise), PLG (mid-market)
Key stakeholders: VP Sales (motion authority), VP Product (platform dependency)
Revenue Levers: Time-to-value, outcome visibility, team collaboration
```

**Expected Output - Context Referenced:**
```
✓ Brain context loaded:
  - ICP: Mid-market primary, enterprise secondary (shapes who's in room)
  - GTM Motion: Sales-led + PLG (Sales VP is Manage Closely, Product VP is critical)
  - Revenue Levers: Time-to-value (Eng stakeholder power), outcome visibility (CS stakeholder power)

Inferred stakeholder power:
  - Sales VP: High Power, High Interest (sales-led motion authority)
  - Product VP: High Power, Medium Interest (platform dependency)
  - CS VP: Medium Power, High Interest (outcome visibility lever owner)
```

**Pass Criteria:**
- Brain sections loaded silently at pre-flight
- ICP shapes Manage Closely stakeholder scope
- GTM Motion informs which function owns which decision
- Revenue Levers inform which stakeholders can block

---

## Eval 3: Inversion Check Quality

**Scenario:** User completes intake for a product launch. Skill runs inversion check: "Who could sink this from inside?"

**Test Data - Scenario A:**
```
Initiative: "Launch customer analytics dashboard"
User struggles to name who could sink it.

Expected inversion response: "If you can't name who could sink this, the political map is assumed — not validated. Let's do this first before we build the map."

Result: User identifies "Finance (if they see this as feature bloat without ROI)" + "Sales (if enablement isn't ready)"
```

**Test Data - Scenario B:**
```
Initiative: "Pricing change from per-user to value-based"
User immediately names: "Finance owns margin model validation" + "CS owns customer comms risk" + "Legal owns contract wording"

Expected: Skill validates these as load-bearing. Adds them to Manage Closely for mapping.
```

**Pass Criteria:**
- Inversion check surfaces concrete stakeholders (not generic "leadership")
- Skill surfaces flag if user can't name blockers
- Named blockers flow into Manage Closely quadrant in mapping step

---

## Eval 4: Power × Interest Classification + Political Role Accuracy

**Scenario:** Skill places stakeholders on 2×2 grid and assigns political roles.

**Test Data:**
```
Stakeholder 1: Sales VP
- Power: High (authority over sales enablement, can refuse to sell)
- Interest: High (revenue-dependent, directly impacted)
- Expected quadrant: 🔴 Manage Closely
- Political role: Champion (advocates for faster launches) OR Blocker (if CRO mandates slow rollout)
- Expected role assessment: "Look for signs: is she pushing launch forward or holding back?"

Stakeholder 2: Finance Controller
- Power: High (budget owner, can halt spend)
- Interest: Low (approval-level interest, not day-to-day)
- Expected quadrant: 🟡 Keep Satisfied
- Political role: Gatekeeper (controls budget release, not the launch decision itself)
- Expected role assessment: "Never bypass. Earn trust first, then get expedited approval."

Stakeholder 3: Marketing manager (peer)
- Power: Low (no authority over launch, can't block)
- Interest: High (wants to co-own campaign messaging)
- Expected quadrant: 🟢 Keep Informed
- Political role: Floating Voter (undecided, could amplify or dampen momentum)
- Expected role assessment: "Bring early win from a Champion to move them."

Stakeholder 4: CEO
- Power: High (can kill any initiative)
- Interest: Low (executive bandwidth limited, approves direction only)
- Expected quadrant: 🟡 Keep Satisfied
- Political role: Performer (said yes in board meeting, but availability uncertain for detail work)
- Expected role assessment: "Validate commitment with CEO's direct report, not CEO. Written approval required."
```

**Pass Criteria:**
- Power assessment grounded in initiative context (not just job title)
- Interest assessment grounded in initiative impact (not just function)
- Political role assigned with behavioral signal (Champion = advocates unprompted; Performer = says yes verbally but no follow-through)
- Role assessment includes Watch For signal (what would indicate this person shifted quadrant or role)

---

## Eval 5: Conflict Mapping Completeness

**Scenario:** Skill identifies stakeholder conflicts, defines second-order risks, and assigns resolution owners.

**Test Data - Conflict 1:**
```
Stakeholder A: VP Sales
vs.
Stakeholder B: VP Product

Conflict: "Sales wants faster launch timeline. Product wants more QA time."

Skill-generated conflict map:
- Conflict description: "Sales argues launch-ready by Q3. Product needs Q4 for stability testing."
- Second-order risk: "If unresolved by decision gate (June 15), launch will slip. Sales will blame Product for missing committed date. Trust erodes for next 3 launches."
- Resolution owner: "PMM owns alignment on mutual success definition. Specific move: joint demo to executive sponsor (CEO) to force priority decision by June 10."
- Follow-up: "If Sales wins (Q3), Product gets post-launch support budget. If Product wins (Q4), Sales gets 4-week head-start on pre-selling."
```

**Pass Criteria:**
- Every conflict has two named stakeholders
- Conflict description is 2 sentences (specific, not abstract)
- Second-order risk named (what breaks downstream, not just what they do)
- Resolution owner assigned (not "alignment happens")
- Resolution owner deadline (not "before launch")
- Conflict-resolution trade-off explicit (what Sales gives up if Product wins, vice versa)

---

## Eval 6: Silent Blocker Identification

**Scenario:** Skill scans for functions not in the room but could kill the launch.

**Test Data - Product Launch Initiative:**
```
Initiative: "Bulk user import feature"
Stakeholders named: Sales VP, Product VP, Engineering Lead, PMM

Silent functions scan:
- Finance: Pricing implications? No → Not a blocker
- Legal: Contract implications? No → Not a blocker
- CS: Customer-facing operational change? Yes → Brief timing: 2 weeks pre-launch, owner: PMM
- Security: Data import security review needed? Yes → Brief timing: 3 weeks pre-launch, owner: Engineering Lead
- HR: No implications → Not a blocker

Output:
```
Silent blockers — functions not in the room:
CS — Must brief on support playbook for bulk import edge cases — 2 weeks pre-launch — PMM owns outreach
Security — Must review data import validation security — 3 weeks pre-launch — Eng Lead owns
```
```

**Pass Criteria:**
- Silent function identified (not just in the room)
- Implication stated (why they could block)
- Brief timing specific (not "eventually")
- Owner named (who reaches out)
- Question-driven (Does this function have a say in this decision?)

---

## Eval 7: Sprint Card Execution Clarity

**Scenario:** Skill generates Sprint Card with five fields per stakeholder.

**Test Data:**
```
[🏆 Champion] Sales VP — Ramini Velasquez
📅 Next touchpoint: Tuesday, June 18 · 30-min sync
  _(Execution note: Cannot slip past this — need written confirmation on enablement timeline by EOD)_
📝 Send before touchpoint: Pre-launch sales readiness deck (9 slides: timeline, talking points, objection handling, first-week support)
  _[2 hours to build. Send by Monday, June 17, 5pm.]_
🎯 What you need from them, by when: Written confirmation of sales availability for 4-week pre-launch sprint. Deadline: EOD Tuesday.
  _If no response by EOD Wednesday: escalate to CRO with timeline implications._
🗣️ The one sentence that has to land: "We hit the Q3 timeline because Sales is ready, not because Product rushes. Let's prove that with enablement."
  _(If she pushes back on timeline: "The Q4 alternative costs us [X customer deals]. This is the financial choice, not just a nice-to-have.")_
🚨 Watch for: "Ramini stops initiating asks. Delegates details to her manager. Stops showing up to optional syncs."
  → If this fires: call her directly; diagnose the shift (concerns about enablement? CEO pressure? Something else?); don't assume silence = approval.
```

**Pass Criteria:**
- Five fields: touchpoint + prep work + ask + one-liner + Watch For (no six fields, no paragraphs)
- Execution note: specific what-cannot-slip (not general "important meeting")
- Prep artefact: named, not vague ("pre-launch readiness deck" not "an update")
- Ask: explicit, deadline explicit, non-response plan explicit
- One-liner: speaks to her frame, not generic positioning
- Watch For: behavioral signal (not "if she disagrees")
- Immediate action: what to do if signal fires (not "follow up")

---

## Eval 8: Learning Close Accuracy (Step 7)

**Scenario:** Stakeholder-maps skill session completes with intake → inversion check → classification → conflict mapping → silent blocker scan → output. Skill logs to `/context/skill-sessions.md` per its Step 7 Learning Close.

**Expected Output - Session Log:**
```yaml
skill: stakeholder-maps
session_date: 2026-06-21
pattern: "Finance Controller was classified Keep Satisfied but behaved like a silent blocker once budget scope became clear — worth watching across future pricing-change maps."
source: surprised
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly these four fields — `skill`, `session_date`, `pattern`, `source` — matching Step 7's template in `SKILL.md` verbatim. No additional fields.
- `pattern` is a single falsifiable statement about what happened this session, or the literal string `"none"` if nothing notable occurred — not a multi-field summary object.
- `source` is one of `surprised / wrong / missing / n.v.t.`
- The row is written directly, without asking the user for permission — this is a separate, mechanical write from anything the skill asks the user's go-ahead on (like where to save the HTML widget, markdown diagnostic, or Sprint Cards, per Outputs).
- If nothing notable happened this session, the row is still written with `pattern: none` — the log entry is never skipped.

---

## Eval 9: End-to-End Stakeholder Mapping, Full Workflow

**Scenario:** User runs stakeholder map end-to-end: intake → inversion check → classification → conflict mapping → silent blocker scan → output → Learning Close.

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior stakeholder-maps rows, real shape)
skill: stakeholder-maps
session_date: 2026-05-12
pattern: "Product launch — Sales Performer said yes verbally, no written enablement commitment; launch slipped"
source: wrong

skill: stakeholder-maps
session_date: 2026-06-01
pattern: "Pricing change — Finance Gatekeeper classified Keep Satisfied, silent blocker emerged Day 3; should have been Manage Closely"
source: wrong

skill: stakeholder-maps
session_date: 2026-06-15
pattern: "GTM pivot — inversion check named 3 potential blockers; 2 materialized, 1 was a red herring"
source: n.v.t.

# Current session:
Campaign launch intake → inversion check names 4 blockers → classification → 2 conflicts mapped → silent blocker scan flags Legal for contract review
```

**Expected Output - Full Workflow:**
```
✓ Session completed: Campaign launch stakeholder map
✓ Inversion check run: 4 blockers named and placed on the grid
✓ Every stakeholder classified with quadrant + political role
✓ Conflict mapping: 2 conflicts, each with second-order risk + resolution owner
✓ Silent blocker scan: Legal flagged for contract review
✓ Session logged (Step 7):
  skill: stakeholder-maps
  session_date: 2026-06-21
  pattern: "Third consecutive session where an unwritten Sales or Finance commitment was the highest-risk stakeholder signal — recommend surfacing this as a candidate guardrail."
  source: surprised
```

Note that pattern-across-sessions detection (comparing this session's row against the three prior rows to spot a recurring theme, or tracking Watch For signal effectiveness across sessions) is the job of `meta-synthesis`, run separately against the full `/context/skill-sessions.md` log — stakeholder-maps' own Step 7 only ever writes its own single row. This skill does not itself detect or report cross-session patterns; it just logs an honest, falsifiable observation about this one session.

**Pass Criteria:**
- Full workflow completes (intake → inversion → classification → conflicts → silent blockers → output → Learning Close)
- Guardrails surfaced at Step 0 (if `/context/meta-patterns.md` has an applicable, 2+-occurrence pattern)
- Session logged to `/context/skill-sessions.md` with the real four-field shape — not a richer schema
- The skill does not attempt cross-session pattern synthesis itself — that's `meta-synthesis`'s job, not stakeholder-maps'

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Guardrail surfacing (Step 0) | Pattern detected, user warned, can acknowledge/skip |
| 2 | Brain context loading (pre-flight) | ICP, GTM Motion, Revenue Levers inform stakeholder power assessment |
| 3 | Inversion check quality | Named concrete blockers (not generic); skill flags if user can't name |
| 4 | Power × Interest + political role | Grid placement grounded in initiative context; role assigned with Watch For signal |
| 5 | Conflict mapping completeness | Every conflict has second-order risk + resolution owner + deadline |
| 6 | Silent blocker identification | Functions identified with implication + brief timing + owner |
| 7 | Sprint Card execution clarity | Five fields, no exceptions; execution notes, asks, Watch For all explicit |
| 8 | Learning Close accuracy | Real four-field row (`skill`/`session_date`/`pattern`/`source`) logged to `/context/skill-sessions.md` |
| 9 | End-to-end workflow | Intake→Inversion→Classification→Conflicts→Silent blockers→Output→Learning Close, no cross-session synthesis attempted by this skill |

---

## Running Evals

```bash
# Run all evals
for i in {1..9}; do
  echo "Running eval $i..."
  # [invoke stakeholder-maps with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke stakeholder-maps with eval N test data]
# [validate against eval N pass criteria]
```
