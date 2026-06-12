# hs-stakeholder-maps.eval.md

Eval test cases for `hs-stakeholder-maps` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: Fresh Stakeholder Map (Happy Path)

**Input:**
- Initiative: "Pricing change on core product (increasing by 15%)"
- Success: "No customer churn >5% in Q3"
- Timeline: "Announcement in 2 weeks, go-live in 4 weeks"
- Stakeholders: CFO (champion, owns pricing), VP Sales (concerned), CS (worried about churn), Product (neutral)

**Expected Behavior:**
1. Intake runs: initiative, success, timeline, champions, blockers, decision gates all captured
2. Inversion check: "Who could sink this? Finance could if churn exceeds tolerance."
3. Power × Interest grid populated:
   - CFO: High Power, High Interest → Manage Closely (Champion)
   - VP Sales: High Power, High Interest → Manage Closely (Floating Voter, worried about pipeline)
   - CS VP: High Power, Low Interest → Keep Satisfied (frozen, hasn't engaged)
   - Product Lead: Low Power, High Interest → Keep Informed (supporter)
4. Political roles assigned:
   - CFO = 🏆 Champion
   - VP Sales = 🌊 Floating Voter
   - CS VP = 🧊 Frozen
   - Product = 🏆 Champion
5. Conflicts identified: CFO wants to move fast; CS wants data on churn tolerance first
6. Communication plan built:
   - CFO: Weekly sync, key message "This increases ARR 18% while maintaining retention", next action "QBR review by [date]"
   - VP Sales: Bi-weekly, key message "Pricing anchors us as premium; here's the new value narrative for sales", next action "Sales kickoff by [date]"
   - CS VP: Biweekly update, key message "We're running churn analysis in parallel. Here's the threshold we're protecting", next action "Share churn data by [date]"
7. Sprint Cards generated (5-field format per stakeholder)
8. Confidence assessment: 🟢 High (champion coverage strong, frozen voter identified, conflict mapped)

**Success Criteria:**
- Both Map and Sprint Card files generated
- HTML widget rendered before markdown
- Political roles are specific (not just quadrant placement)
- Conflicts have resolution owners + dates
- Watch For signals included in Sprint Cards
- Confidence score reflects reality (not overstated)

**Test Pass:** Map is actionable; PMM knows what to do next week

---

## Test 2: Silent Blocker Discovery

**Input:**
- Initiative: "GTM pivot from sales-led to self-serve"
- Stakeholders named: CEO, VP Product, VP Sales
- Stakeholder not named in intake: RevOps (they control pricing page, billing system, product configuration)

**Expected Behavior:**
1. Intake completes
2. Inversion check asks "Who could sink this?"
3. User doesn't name RevOps
4. Mapping step reveals: RevOps has high power (controls billing system) but low interest initially
5. Conflict map identifies: "If RevOps isn't aligned, self-serve checkout can't scale"
6. Silent blockers section flags: "RevOps — controls billing + pricing page — recommend alignment call before full GTM announcement"
7. Sprint Card includes "RevOps" in Week 1 actions: "Brief RevOps on self-serve motion before CEO announcement"

**Success Criteria:**
- Silent blocker surfaced during mapping, not after launch
- Specific power/interest stated
- Action assigned before the issue compounds

**Test Pass:** Structural risks are caught early

---

## Test 3: Floating Voter to Champion Path

**Input:**
- Prior map: VP Sales is Floating Voter (undecided)
- User reports: "VP Sales has been running a pilot with 2 customers and likes the results"
- New iteration: /update [initiative] — "VP Sales has moved from skeptical to supporter based on pilot results"

**Expected Behavior:**
1. /update command runs
2. Map reloads previous state
3. Stakeholder (VP Sales) quadrant/role updated: Floating Voter → Champion
4. Watch For signal noted: "Pilot success → role shift"
5. New Sprint Card reflects champion status: higher-frequency touchpoints, ask for help (e.g., "Can you speak at the launch event?")
6. New version saved with metadata: "v2 — VP Sales moved to Champion after pilot"

**Success Criteria:**
- Map is updatable (not static)
- Role shift is tracked
- Next steps adjust to new role
- Learning is logged (pilot success → champion conversion)

**Test Pass:** Map evolves with political reality

---

## Test 4: Frozen Voter Investigation

**Input:**
- Initiative: "New market entry into healthcare"
- Stakeholder: Legal (Frozen — hasn't engaged)
- Intake notes: "Legal hasn't said yes or no"

**Expected Behavior:**
1. Mapping identifies Legal as Frozen
2. Deep-dive insight: "Why frozen? Legal typically raises compliance concerns. Our healthcare entry likely triggers data residency questions."
3. Recommendation: Schedule 30-min call before announcement to surface actual concerns
4. Pre-filled Sprint Card for Legal:
   - Touchpoint: "30-min discovery call to surface regulatory concerns"
   - Send: "1-pager on healthcare data handling + compliance approach"
   - Need by: "Go/no-go decision by [date]"
   - Watch For: "If Legal goes silent after initial call, escalate to General Counsel"
5. Action owner named: "PMM to schedule + prepare 1-pager"

**Success Criteria:**
- Frozen voter doesn't stay frozen (investigation happens)
- Specific ask structured
- Watch For signal is concrete

**Test Pass:** Frozen voters aren't treated as aligned

---

## Test 5: Performer Detection

**Input:**
- Prior sprint card: VP Finance verbally committed "We're all in on this"
- Follow-up: One week later, VP Finance hasn't approved budget
- User reports via /update: "VP Finance said yes in the alignment meeting but hasn't signed off on budget commitment"

**Expected Behavior:**
1. Skill flags: "Verbal yes without written follow-through = Performer"
2. Political role updated: Champion → Performer
3. Rule applied from Operating Rules: "Name the Performers. Verbal yes with no follow-through is the most common stakeholder failure mode. Written commitment or it didn't happen."
4. Next action: "Send budget approval request (email) instead of relying on verbal. Confirmation by [date] or escalate."
5. Watch For signal: "Budget approval by [deadline]. If silent, escalate to CFO."

**Success Criteria:**
- Performer behavior is named
- Requires written action (not another conversation)
- Escalation path clear

**Test Pass:** Verbal commitments don't derail plans

---

## Test 6: Conflict Mapping and Resolution

**Input:**
- Initiative: "Product pricing change"
- Stakeholders:
  - CFO: wants maximum price (revenue optimization)
  - VP Sales: wants lower price (market competitiveness)
  - Customer Success: worried about churn from price increase

**Expected Behavior:**
1. Mapping identifies conflict: CFO vs VP Sales (revenue vs. competitive positioning)
2. Second-order risk: "If unresolved, sales team gets confused messaging. VP Sales may torpedo internally."
3. Resolution block: "Before announcement: CFO and VP Sales align on value narrative. Product positions 15% price increase as 'premium tier, enterprise-grade support.' Sales uses narrative for upsell, not discount negotiation."
4. Resolution owner: "CFO + VP Sales co-lead narrative workshop"
5. Resolution due date: "Before sales kickoff on [date]"
6. Sprint Card includes both as "Manage Closely" with Watch For: "Are CFO and VP Sales using the same narrative in customer calls?"

**Success Criteria:**
- Conflict is named and specific
- Second-order risk is clear
- Resolution is concrete (not vague)
- Owner and date assigned
- Watch For is measurable

**Test Pass:** Conflicts don't become launch disasters

---

## Test 7: Weekly Map Health Check (/check Command)

**Input:**
- /check [initiative]
- Map is 2 weeks old
- Stakeholder "Director of Ops" hasn't been contacted in 8 days
- Watch For signal from prior sprint: "Finance will escalate churn concerns by [date]" — signal hasn't fired yet
- Sprint Card outdated (last updated 12 days ago)

**Expected Behavior:**
1. /check output surfaces:
   - "Stakeholder silent: Director of Ops hasn't been contacted in 8 days. Recommend touchpoint this week."
   - "Watch For pending: Finance escalation signal due in [2] days. Prepare response now."
   - "Sprint Card stale: Not updated in 12 days. Recommend /update before next week."
   - "Map age: 2 weeks old. Recommend running /update if any alignment conversations happened."
2. Confidence score may drop from 🟢 to 🟡 due to staleness
3. Recommendations are specific actions

**Success Criteria:**
- Stale maps are flagged
- Silent stakeholders are surfaced
- Pending Watch Fors are visible
- Recommendations are actionable

**Test Pass:** Map health is monitored; staleness doesn't go unnoticed
