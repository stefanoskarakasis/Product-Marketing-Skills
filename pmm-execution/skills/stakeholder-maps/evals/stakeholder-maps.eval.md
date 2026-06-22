---
name: stakeholder-maps.eval
version: 2.3.0
description: >
  Comprehensive eval suite for stakeholder-maps skill. Tests: guardrail surfacing,
  brain context loading, inversion check quality, Power × Interest classification accuracy,
  political role assignment rigor, conflict mapping completeness, silent blocker identification,
  sprint card execution clarity, logging accuracy, and pattern detection for meta-synthesis.
  8 scenarios covering real GTM initiative types and stakeholder political dynamics.
---

# Stakeholder-Maps — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3, 5)
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Populates `/context/skill-sessions.md` with prior stakeholder maps (if testing pattern detection)
4. Runs stakeholder-maps skill for given initiative
5. Validates outputs: inversion check rigor, classification accuracy, role assignment, conflict mapping, logging

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

# /context/skill-sessions.md (3 prior product launch maps)
skill: stakeholder-maps
session_date: 2026-06-10
initiative_type: "product launch"
sales_performer_count: 1
outcome: "launch delayed"

skill: stakeholder-maps
session_date: 2026-06-12
initiative_type: "product launch"
sales_performer_count: 1
outcome: "launch delayed"

skill: stakeholder-maps
session_date: 2026-06-15
initiative_type: "product launch"
sales_performer_count: 1
outcome: "launch delayed"
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
- Guardrail logged in Step 7 (guardrails_triggered field)

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
- Quality score reflects whether inversion was run and quality of blocker identification

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

## Eval 8: End-to-End Stakeholder Mapping with Pattern Detection

**Scenario:** User runs stakeholder map end-to-end: intake → inversion check → classification → conflict mapping → silent blocker scan → output → logging. Test detects patterns (Watch For signals useful? Inversion checks catching risks?).

**Test Data:**
```yaml
# /context/skill-sessions.md (3 prior stakeholder maps)
Session 1 (product launch): Sales Performer identified, Watch For signal fired (stopped initiating contact) → caught early
Session 2 (pricing change): Finance Gatekeeper as Keep Satisfied → silent blocker emerged Day 3 → should have been Manage Closely
Session 3 (GTM pivot): Inversion check named 3 potential blockers; 2 materialized; 1 was red herring

# Current session (campaign launch):
Inversion check → identifies 4 potential blockers
Classification → places them in quadrants
Conflict mapping → 2 conflicts identified
Silent blocker scan → flags Legal for contract review
Logging → all steps captured
```

**Expected Output - Pattern Recognition:**
```
✓ Session completed: Campaign launch stakeholder map
✓ Quality score: 88/100
✓ Inversion check run: 4 blockers named and placed in map
✓ Watch For patterns extracted: 2 patterns identified (Sales Performers going dark, Finance gatekeepers hiding)

🔁 PATTERN FOR META-SYNTHESIS:

Inversion check accuracy tracking (last 3 sessions):
  - Blockers named: average 3.3 per session
  - Blockers that materialized: ~67% accuracy
  - False alarms: ~33% (red herrings that never moved)

Watch For signal effectiveness:
  - Sales Performer silence signal: 100% accuracy (when signal fires, they've shifted)
  - Finance Gatekeeper hiding signal: 50% accuracy (signal sometimes indicates nothing, sometimes indicates blocker)

Emerging pattern: Finance stakeholders should be Manage Closely if >$100K budget impact.
Proposed rule: "If Finance controls >$50K, move from Keep Satisfied to Manage Closely."

Guardrail recommendation: Keep "Sales Performer risk" ACTIVE. Downgrade "Finance hidden blocker" to conditional (add budget threshold).
```

**Pass Criteria:**
- Full workflow completes (intake → inversion → classification → conflicts → silent blockers → output → log)
- Quality score reflects rigor (inversion check run? All roles assigned? Conflicts resolved?)
- Inversion check resulted in named blockers (not abstract risks)
- Watch For signals captured in Sprint Cards
- Session logged to `/context/skill-sessions.md` with all metadata
- Stakeholder counts accurate
- Brain updates proposed (if pattern suggests ICP or GTM Motion shifts needed)
- Pattern signals extracted (Watch For effectiveness, inversion accuracy, role distributions)

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
| 8 | End-to-end workflow | Intake→Inversion→Classification→Conflicts→Silent blockers→Output→Log, patterns detected |

---

## Running Evals

```bash
# Run all evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke stakeholder-maps with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke stakeholder-maps with eval N test data]
# [validate against eval N pass criteria]
```

---

## Changelog

### v2.3.0 — 2026-06-22
Major refactor for MCP-ready architecture: Added Step 0 guardrail loading from `/context/meta-patterns.md`. Added Step 7 session logging to `/context/skill-sessions.md` with 15+ metadata fields (stakeholder counts, role distributions, Watch For patterns, confidence assessment). Integrated brain context loading (Sections 2, 3, 5). Consolidated Operating Rules and Self-Improvement Loop into logging layer. Weight-cut from v2.2.0 (~850 lines) to ~550 lines while preserving visual-first output architecture. Added 8 comprehensive evals covering guardrail surfacing, inversion check quality, classification accuracy, conflict mapping, silent blocker identification, Sprint Card clarity, logging, and pattern detection. Full 19/19 SKILL-SPEC compliance.

### v2.2.0 — 2026-06-11
Spec compliance update: added Trigger, Inputs, Pre-flight, Outputs, Verification sections.

### v2.1.0 — 2026-04-17
Visual-first architecture introduced. HTML widget with Power × Interest grid, stakeholder chips, communication table, conflict map cards.

### v2.0.0 — 2026-04-17
Two-phase output: Map + Sprint Card as separate documents. Five-field Sprint Card format. Watch For observations wired to knowledge/ learning loop.

### v1.0.0 — 2026-04-17
Initial build.
