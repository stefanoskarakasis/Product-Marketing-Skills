# hs-pre-mortem.eval.md

Eval test cases for `hs-pre-mortem` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: Full Pre-Mortem — Product Launch

**Input:**
- Initiative: "Analytics dashboard for mid-market finance (product launch)"
- Type: Product Launch
- Success definition: "500 qualified trials in 90 days"
- Decision gates: Feature freeze (Week 2), beta launch (Week 4), GA (Week 6)
- Team in session: PMM, Product, Sales, CS
- Brain exists with ICP (finance), positioning (self-serve), and GTM motion (sales + community)

**Expected Behavior:**
1. Intake runs (initiative, success, gates, team composition)
2. Thesis interrogation: "What would have to be true for this initiative to be the wrong move entirely?" (e.g., "If self-serve doesn't work in finance because they need handholding…")
3. Failure scenario calibration: "What would failure unambiguously look like to your CEO?" (e.g., "<100 trials by Week 12 = failure")
4. Failure frame set: "Imagine it's Week 12. You have <100 trials. What did you know that you ignored?"
5. Risk generation across 5 lenses:
   - 🔍 Lens 1 (Market & Customer): ICP fit assumptions, buyer awareness gap, willingness to pay
   - 🔍 Lens 2 (Competitive & Strategic): Competitor response risk, positioning drift, cannibalization
   - 🔍 Lens 3 (GTM & Execution): Sales readiness (will sellers bring this up unprompted?), message-market fit, activation path clarity
   - 🔍 Lens 4 (Organisational & Stakeholder): Sales VP alignment, Sales compensation (does comp incentivize new product?), resource commitment
   - 🔍 Lens 5 (Data & Measurement): Success metric defined?, leading indicators (adoption velocity in Week 2–3?), attribution (can we isolate dashboard impact from other changes?)
6. Risk classification:
   - 🐯 Tigers (real risks): Sales compensation misaligned (no incentive to sell), message-market fit unvalidated (sales can't explain it)
   - 📄 Paper Tigers (acknowledged, not acted on): Competitor response (we're first-mover in this category)
   - 🐘 Elephants (investigation needed): Willingness to pay (is 40% of ICP willing to adopt?), Investigator: Sales, Due: Week 1 sales call
7. Tiger triage:
   - 🚨 Launch-Blocking: Sales compensation, message-market fit
   - ⚡ Fast-Follow: Product doc quality, CS onboarding readiness
8. Action plans for Launch-Blocking Tigers:
   ```
   ### 🚨 Tiger: Sales Compensation Misaligned
   
   **What breaks:**
   - Sales ignores new product in prospect calls
   - Pipeline to new product stalls after Week 2
   
   **Why it's real:**
   - Sales comp only incentivizes legacy products
   - Sales manager said "My reps won't lead with this"
   
   **Mitigation:**
   - Add $X spiff for each trial sign-up
   - Co-design sales comp with VP Sales by [date]
   
   **Owner:** VP Sales + Finance
   
   **Due date:** Before Week 4 beta
   
   **Confidence:** 🟢 Credible — VP Sales has budget authority
   ```
9. PMM Recommendation:
   - 🟡 Conditional Go — "Go if sales comp is fixed before Week 4 beta. If not fixed by [date], reverts to No-Go."
10. Confidence score: 🟡 Medium — Tigers are credible but mitigation is in progress

**Success Criteria:**
- All 5 lenses covered (at least one risk per lens)
- Tigers are evidence-based (not worry)
- Elephants have investigators + due dates + upgrade conditions
- Launch-Blocking Tigers have full action plans
- Mitigations have confidence scores (🟢/🟡/🔴)
- PMM Recommendation is explicit (Go/Conditional/No-Go)
- If any 🔴 mitigation on launch-blocker → Recommendation is not 🟢 Go

**Test Pass:** Pre-mortem changes execution plan; risks are owned

---

## Test 2: Elephant Upgrade (Avoidance Rule)

**Input:**
- Initiative: "New market entry (healthcare vertical)"
- Risk surfaced: "Do healthcare buyers have budget for this?" (Willingness to pay)
- Classification attempt: Elephant (unspoken, needs investigation)
- BUT: Sales has done 3 healthcare pilot calls; willingness to pay could have been asked but wasn't

**Expected Behavior:**
1. Elephant rule triggered: "Avoidance upgrades Elephants to Tigers"
2. Diagnostic: "You have access to the evidence (you can ask pilot customers directly), and you chose not to gather it. That's not uncertainty — that's avoidance."
3. Risk reclassified: 🐯 Tiger (real risk, launch-blocking until resolved)
4. Action plan required immediately:
   ```
   ### 🚨 Tiger: Willingness to Pay Not Validated
   
   **What breaks:**
   - Launch fails if healthcare buyers won't spend enough
   
   **Why it's real:**
   - Healthcare has unique budget cycles (annual purchasing)
   - Pilot calls didn't ask about budget/buying process
   - Evidence is accessible but untested
   
   **Mitigation:**
   - Call 5 pilot participants + ask budget + procurement process
   - Report findings by [date]
   
   **Owner:** Sales
   
   **Due date:** Before [date] (before market entry announcement)
   
   **Confidence:** 🟡 Partial — Sales owns this but may not prioritize
   ```
5. Recommendation drops to 🔴 No-Go until avoidance is resolved

**Success Criteria:**
- Avoidance is named (not soft-pedaled)
- Elephant automatically becomes Tiger
- Action plan has named owner + deadline
- Recommendation reflects unresolved risk

**Test Pass:** Known unknowns don't hide in Elephant classification

---

## Test 3: Paper Tiger Integrity Check

**Input:**
- Risk surfaced: "Competitor responds to our launch"
- Classification attempt: Paper Tiger ("We're first-mover in this category, so competitor response is low-probability")

**Expected Behavior:**
1. Paper Tiger integrity rule applies: "A PMM's confidence in their existing customer relationship, brand strength, or internal alignment is never sufficient evidence to classify a commercial, competitive, or perception risk as a Paper Tiger."
2. Pushback: "Familiarity is not validation. Confidence is not data. What evidence shows competitor won't respond in 2 weeks?"
3. If no evidence: "This needs to stay as Tiger with mitigation plan: (1) monitor competitor announcements, (2) if competitor responds, execute talk track with sales by [date]."
4. If evidence exists (e.g., "Competitor is in acquisition process for 3 months"), then Paper Tiger classification holds with stated reason

**Success Criteria:**
- PMM confidence alone doesn't downgrade risks
- Paper Tiger classification requires evidence
- Reasoning is explicit

**Test Pass:** Optimism bias doesn't hide risks

---

## Test 4: New Market Entry — Local Knowledge Audit

**Input:**
- Initiative: "Expand into Southeast Asia market"
- Risk generation would run Lenses 1 + 2 (Market & Competitive)
- Question before risk generation: "Do you have anyone in this session with on-the-ground knowledge of Southeast Asia?"
- Answer: "No — we're relying on secondary research and vendor data"

**Expected Behavior:**
1. Local knowledge audit flags: "All Market & Customer and Competitive & Strategic risks for this market entry are assumption-based — not evidence-based. Every risk in those two lenses is flagged 🔴 confidence until local validation exists."
2. Additional checks run:
   - Does beachhead segment (from brain) conflict with this new market?
   - Are ICP assumptions being translated or assumed to carry over unchanged?
   - Full regulatory surface area in this market identified?
   - Local competitive dynamic that doesn't exist in home market?
   - GTM team structurally equipped (language, network, local knowledge)?
   - Defined beachhead (one city/region, one subsegment) before outbound begins?
   - Country Manager decision trigger with go/no-go date?
3. Risk generation produces high number of 🔴 confidence Tigers
4. Recommendation: 🟡 Conditional Go — "Go if we hire local market expert by [date]. If not, reverts to No-Go."

**Success Criteria:**
- Local knowledge gap is surfaced upfront
- Confidence scores reflect assumption-based risk
- Checks are comprehensive
- Entry point is defined before scaling

**Test Pass:** Market entry risks are grounded in reality, not assumptions

---

## Test 5: GTM Pivot — Organisational Lens First

**Input:**
- Initiative: "Sales-led to self-serve GTM pivot"
- Modification: GTM Pivot initiative type triggers Lens 4 (Organisational) first
- Additional checks for pivot:
  - Has Sales leadership been briefed before the announcement?
  - Is there a compensation model defined for self-serve motion before go-live?
  - Is there a playbook for how Sales uses self-serve in live deals?
  - Has the CEO mandate been translated into explicit resource commitment?

**Expected Behavior:**
1. Lens 4 (Organisational) runs first, not last
2. Risks surfaced:
   - 🚨 Sales leadership blindsided by announcement (not briefed in advance)
   - 🚨 Sales comp still incentivizes old motion (no self-serve incentives)
   - 🚨 Sales playbook undefined (how do reps use self-serve for enterprise deals?)
3. All rated 🚨 Launch-Blocking (motion pivot fails if sales is unaligned)
4. Action plans required before proceeding to other lenses
5. Additional check: "What is the opportunity cost of pivoting away from sales-led? Are we leaving revenue on the table during transition?"
6. Recommendation: 🔴 No-Go unless Lens 4 risks are resolved

**Success Criteria:**
- Lens 4 executed first
- All three checks run
- Organisational failures are flagged as launch-blockers
- Opportunity cost is explicit

**Test Pass:** GTM pivots fail on internal misalignment, not market conditions

---

## Test 6: No-Go Delivery (Leadership Reframing)

**Input:**
- Pre-mortem complete
- Multiple 🚨 Launch-Blocking Tigers with 🔴 confidence (unresolved)
- Recommendation: 🔴 No-Go
- Context: Initiative has CEO directive + conference commitment

**Expected Behavior:**
1. Recommendation is stated clearly: "Not ready. The risk to [revenue/positioning/market perception] outweighs the benefit of launching on schedule."
2. For politically complex situations, PMM reframes: "We ran a pre-mortem. The recommendation is a [X]-day validation sprint before full launch — because that's how we make [initiative name] work, not how we slow it down."
3. Validation sprint structure offered:
   - "Here's what we validate: [specific Tiger mitigations]"
   - "Here's the go/no-go condition at the end of the sprint: [threshold]"
   - "Here's what we announce now vs. what we hold: [phased launch]"
4. This reframes delay as diligence, not resistance

**Success Criteria:**
- No-Go is not softened with caveats
- Leadership reframe offered if politically needed
- Validation sprint gives decision point (not endless delay)
- PMM is protected from "person who said no to growth" narrative

**Test Pass:** Bad launches are stopped; good leaders listen

---

## Test 7: Learning Close — Hypothesis Capture

**Input:**
- Pre-mortem session complete
- Closing questions asked:
  1. "Is there anything you want to say out loud before we close?"
  2. "Was there a risk that surprised you?"
  3. "Was there a Tiger I flagged that you think is actually a Paper Tiger?"
  4. "Was there an Elephant the team already knew about but hadn't named?"

**Expected Behavior:**
1. Step 1: User says "Honestly, I'm worried that Sales won't prioritize this — but we've never had that problem before"
2. Skill captures: "That's a Tiger being avoided, not an Elephant."
3. Learning close extracts:
   - Pattern: "Sales prioritization assumptions based on past launches"
   - Proposed rule: "Sales prioritization is not guaranteed across new product launches. Always validate readiness before go-live."
   - Proposed addition to `knowledge/gtm/rules.md`
4. Step 2: User: "Yes, competitor response surprised us — we've been first-mover so long, we forgot they exist."
5. Capture: Pattern learned; added to `knowledge/gtm/hypotheses.md`
6. Final offer: "Log this session? I'll extract patterns and update the knowledge base."
7. No file is written without explicit approval

**Success Criteria:**
- Unstructured prompt runs first (captures deepest insights)
- Pattern capture happens
- Rule/hypothesis updates are proposed (not silent)
- Approval required before encoding

**Test Pass:** Learning compounds; future pre-mortems are sharper
