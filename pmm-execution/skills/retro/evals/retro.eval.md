# Retro.eval.md

Eval test cases for `hs-retro` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: Full Post-Launch Retro (Happy Path)

**Input:**
- Cycle: "Q2 Product Launch — Analytics Dashboard (May 1–June 15)"
- OKRs: "Objective: Establish Analytics as enterprise-grade alternative. KRs: (1) 50 qualified trials in enterprise segment; (2) 30% trial-to-paid conversion; (3) <$50K CAC for enterprise"
- Inputs: "Achieved 38 trials (76%), 22% conversion (73% target), $62K CAC (24% over budget). Sales reported 'buyers want more customization.' CS reported 'onboarding took 3x longer than projected.' Product says 'we underestimated feature completeness for enterprise buyers.'"
- Brain exists with: ICP (enterprise finance), positioning (enterprise-grade), launch tier (T1)

**Expected Behavior:**
1. Intake runs (cycle, OKR, inputs confirmed)
2. Outcome anchor established (38 trials, 22% conversion, $62K CAC vs. targets)
3. Format selected: Format B (OKR Gap Analysis — KRs were missed)
4. Themes identified:
   - Theme 1: "Customization gap" (GTM impact) → Root cause: Brief didn't surface buyer expectation for custom reports
   - Theme 2: "Onboarding friction" (Process friction) → Root cause: Sales process skipped discovery call on implementation scope
   - Theme 3: "CAC overage" (GTM impact) → Root cause: Inefficient lead routing to enterprise AE (incorrect RACI)
5. Tier assessment: Assigned T1, warranted T2 (execution fell short of T1 scope)
6. Action items (max 3):
   - Action 1: Brief v2 includes custom reporting as standard (KR #1, Owner: PMM, By: June 30)
   - Action 2: Sales discovery call added before product kickoff (RACI change, Owner: VP Sales, By: July 5)
   - Action 3: Backlog: Pricing model review (not OKR-linked, goes to backlog)
7. Session file written with timestamp
8. Quality gate passes (17+/21)

**Success Criteria:**
- Themes trace to specific KR failures (not generic complaints)
- Root causes are structural (process, RACI, brief quality) — not "communication"
- Tier assessment compares assigned vs. warranted
- Max 3 action items, single owner each, all measurable
- Session file persisted

**Test Pass:** Retro produces OKR-linked decisions; no venting, no fuzzy language.

---

## Test 2: Carry-over Action Item Failure Diagnosis

**Input:**
- Cycle: "Q3 Campaign Sprint (June 15–July 15)"
- OKRs: "Drive engagement on new reporting feature. KRs: (1) 500 feature activations; (2) 40% adoption in free tier; (3) 20% upgrade rate"
- Inputs: "Achieved 320 activations (64%), 25% adoption (63% shortfall), 12% upgrade (40% shortfall). Carry-over from Q2 retro: 'Sales discovery call added before kickoff' — NOT DONE. No call was scheduled."
- Brain: ICP (SMB finance), positioning (self-serve first), launch tier (T3)

**Expected Behavior:**
1. Intake runs; OKRs confirmed
2. Pre-flight loads carry-over action items from prior session
3. Outcome anchor shows: all three KRs missed
4. Before collecting new feedback, ask about Q2 carry-over:
   > "I see from the prior retro that Sales discovery calls were supposed to start. They didn't happen. Before we diagnose this sprint's issues, why did that action stall? This tells us whether we have a Resource, Priority, or Buy-in problem."
5. User responds: "Sales VP prioritized another campaign. Discovery calls got deprioritized."
6. Root cause identified: Competing priority, not skill gap. RACI failure (who decides which work gets done).
7. Themes for THIS sprint:
   - Theme 1: "Adoption gap" → Root cause: Lack of user journey clarity in brief (messaging gap)
   - Theme 2: "Upgrade conversion gap" → Root cause: Pricing/value prop didn't land with SMB buyers
8. Action items:
   - Action 1: Resolve Q2 carry-over first — escalate sales priority with CEO (Owner: CMO, By: next week)
   - Action 2 (NEW): Brief v3 includes specific SMB upgrade trigger (Owner: PMM, By: July 25)
9. Quality gate includes: "Carry-over addressed before new actions added" ✅

**Success Criteria:**
- Carry-over items surface automatically
- Skill probes WHY carry-over didn't happen (not just moves on)
- Resolved carry-over gets priority in new action list
- New actions informed by understanding the prior failure

**Test Pass:** System learns from incomplete actions; doesn't repeat mistakes.

---

## Test 3: Format C — Cross-Functional Tension Map

**Input:**
- Cycle: "Enterprise Sales Sprint (July 1–July 31)"
- OKRs: "Close 2 enterprise deals. KRs: (1) 2 contracts signed; (2) $500K ARR; (3) 90% deal satisfaction"
- Inputs: "Signed 1 deal ($250K), satisfaction score 60% (vs. 90% target). Feedback: Sales says Product moved goal posts mid-sales-process (added custom integration requirement). Product says Sales didn't communicate the scope early enough. PMM caught in middle."
- Brain: ICP (enterprise), positioning (flexible), tier (T1)

**Expected Behavior:**
1. Intake runs; OKRs confirmed
2. Outcome anchor: 1/2 deals, $250K/$500K, 60%/90% satisfaction
3. Format selected: Format C (Cross-Functional Tension Map — collaboration broke down)
4. Root cause diagnosis:
   - Surface tension: "Sales vs. Product scope expectations"
   - One level deeper: "Sales didn't share buyer scope with Product early"
   - Structural root cause: "RACI unclear — who owns scope communication in enterprise sales? When does it happen? Via what artifact?"
5. Action item:
   - Action: Create "Enterprise Sales Scope Document" template + intake meeting (Owner: VP Sales + Product Lead, By: Aug 15)
   - Success metric: Next deal uses template; scope locked before technical discussions
6. Quality gate: Tension named, root cause is structural (RACI), not interpersonal ("Sales and Product need to get along better")

**Success Criteria:**
- Retro names the actual tension (not papered over)
- Root cause is structural, not personality-based
- Action is a process/artifact, not "better communication"

**Test Pass:** Retro uncovers process gaps, not blame.

---

## Test 4: Tier Mismatch Discovery

**Input:**
- Cycle: "Q2 Feature Launch — AI-Powered Summarization (May 15–June 30)"
- OKRs: "Drive adoption of new AI feature. KRs: (1) 1000 users active in feature; (2) 80% retention after 7 days; (3) feature mentioned in 5 customer testimonials"
- Inputs: "Achieved 2500 users (250%), 85% retention (106%), feature in 3 testimonials (60%). BUT: Sales says 'customers love this but the use case is narrower than we thought — it's mainly for accountants, not all finance roles.' Market signal: 90% of usage from accounting segment, 10% from other finance roles."
- Brain: ICP (finance — broad), launch tier (T2, assigned)
- Tier metrics: "T2 = Major initiative, 2–4 weeks GTM, targeted channels, ~$50K campaign."

**Expected Behavior:**
1. Intake runs; OKRs confirmed
2. Outcome anchor: 2500 users, 85% retention, 3 testimonials (all KRs exceeded)
3. Surface observation: "Looks like a win — KRs crushed."
4. Tier assessment runs:
   - Assigned: T2
   - What market signals suggest: Narrow use case (accountants), high adoption within that wedge, but NOT achieving broad positioning
   - **Warranted: T1** (if we'd known the wedge was accounting-only, this would be a wedge-into-accounting launch = T1 scope and urgency)
5. Root cause diagnosis:
   - Brief was "for all finance roles" but market revealed "accounting-focused"
   - ICP positioning didn't pre-identify the wedge
   - Result: Under-resourced for the actual (narrower, more strategic) opportunity
6. Action:
   - Action: Retarget messaging to "accounting workflows" (Owner: PMM, By: Q3), reallocate budget to accounting-specific channels (Owner: Demand Gen, By: July 15)
   - This is actually a T1-level move (create a new market wedge), not T2

**Success Criteria:**
- KRs were technically met, but retro digs into "did we measure the right thing?"
- Tier mismatch surfaced: assigned T2, warranted T1 for the actual market opportunity
- Action reframes the initiative upward (more investment, focused positioning)

**Test Pass:** Retro catches over/under-resourced initiatives even when KRs are hit.

---

## Test 5: Anti-Pattern Detection ("Retrospective Theatre")

**Input:**
- Cycle: "Q3 Pricing Experiment (July 1–August 15)"
- OKRs: "Test new pricing model. KRs: (1) 50 new customers on new plan; (2) 20% higher MRR per customer; (3) 95% retained on new plan after 30 days"
- Inputs: "Achieved 12 customers (24% of target), -5% MRR impact (vs. +20% target), 80% retention (vs. 95%). Feedback from team: 'The market wasn't ready for the new pricing.' and 'We needed more time to prepare sales.' and 'Competitors moved faster so the timing was off.'"
- Brain: ICP (SMB), launch tier (T2)

**Expected Behavior:**
1. Intake runs; OKRs confirmed
2. Outcome anchor: All KRs missed significantly
3. Feedback collected: Team offers three reasons — market, sales readiness, competitive timing
4. **Red flag: All three are external (beyond team control).** This is "Retrospective Theatre" — blame shifting.
5. Skill explicitly calls this out:
   > "⚠️ I'm noticing all three themes blame external factors. Let me reframe: 'Market wasn't ready' means 'we didn't validate the buyer problem.' 'Sales unprepared' means 'enablement brief came too late.' 'Competitive timing' means 'we didn't have intelligence on competitor moves.' Each of these is a structural choice WE made. Let's dig into which brief, process, or decision was wrong."
6. Real root causes emerge:
   - "We launched without customer research" (brief gap)
   - "Sales got enablement 1 week before launch" (timing gap)
   - "We didn't monitor competitor roadmap in Q2" (process gap)
7. Actions:
   - Action 1: Run customer discovery on new pricing before next test (Owner: Product, By: Sept 30)
   - Action 2: Sales enablement 2 weeks before any launch (Owner: PMM, By: standing rule)
   - Action 3: Competitor signal monitoring dashboard (Owner: PMM, By: Oct 15)

**Success Criteria:**
- Anti-patterns are named explicitly ("Retrospective Theatre")
- External blame is reframed as internal process gaps
- Actions address the actual structural issues, not the symptoms

**Test Pass:** Retro cuts through blame and finds real causes.

---

## Test 6: Knowledge Base Integration (Recurring Pattern)

**Input:**
- Cycle: "Q4 Feature Launch — Compliance Dashboard"
- OKRs: "Enable compliance-focused buyers. KRs: (1) 20 compliance customers; (2) 40% CAC payback in 180 days; (3) case study from top 3 customer"
- Inputs: "Achieved 8 customers (40%), 35% payback (88% target), 0 case studies (0% target). Sales feedback: 'Buyers want proof of compliance — we needed a third-party audit before launch.'"
- Prior retros (in knowledge base):
  - Q2 retro: "Enterprise buyers stalled on compliance; needed audit before purchase"
  - Q3 retro: "Mid-market buyers also flagged compliance concerns; audit delayed decision"
  - Rule candidate: "Compliance signals = need for third-party audit in brief"

**Expected Behavior:**
1. Intake runs
2. Pre-flight loads `knowledge/retro-patterns/rules.md`
3. Root cause surfaces: "Buyers want third-party audit"
4. Skill flags:
   > "⚠️ This pattern appeared in Q2 and Q3 retros. It's now appeared 3 times. This is a confirmed rule: 'For any compliance-focused launch, brief must include third-party audit timeline and cost.' Should I add this to our rules database?"
5. User confirms: "Yes, add it."
6. Rule written to `rules.md`:
   > "**Compliance Launch Rule:** Any launch targeting compliance-focused buyers must include third-party audit requirement in the brief. Cost, timeline, and required by launch date. Last updated: Q4 2026."
7. Action:
   - Action: Compliance buyer brief template includes audit requirement (Owner: PMM, By: Q1 2027)

**Success Criteria:**
- Recurring pattern (3+ sessions) is detected
- Rule is proposed and user-approved
- Future retros will auto-flag this rule and apply it

**Test Pass:** System learns and prevents recurring mistakes.

---

## Test 7: Rejection Case — Missing OKR

**Input:**
- Cycle: "Q2 Campaign"
- OKRs: (none provided)
- Inputs: "Sales team felt misaligned. Marketing didn't brief them. Campaign didn't land."

**Expected Behavior:**
1. Intake asks: "What were we trying to achieve? OKR + KRs?"
2. User: "We don't have specific OKRs, just 'drive engagement.'"
3. Skill blocks:
   > "A retro without OKRs is a venting session, not a diagnostic. I need specific OKRs (e.g., 'Drive newsletter signups' + 'KRs: 1000 new subscribers, 30% open rate, 5% CTR') before we can run this. Can you get the OKRs from your manager/PMM?"
4. If user can't provide OKRs: "Let's schedule this retro for when OKRs are available. Without them, we can't link themes to what actually mattered."

**Success Criteria:**
- Retro doesn't start without OKRs
- User understands why (can't be diagnostic without an anchor)
- Skill asks for specific, measurable KRs

**Test Pass:** Quality gate prevents low-rigor retros.

---

## Summary: What These Tests Cover

| Test | Dimension | What We're Testing |
|------|-----------|-------------------|
| 1 | Happy path | Full retro flow (intake → anchor → format → themes → actions → output) |
| 2 | Carry-over | System surfaces prior action items; probes why they stalled |
| 3 | Tension mapping | Skill handles cross-functional conflicts; finds structural root causes |
| 4 | Tier mismatch | Even when KRs are hit, retro catches under/over-resourcing |
| 5 | Anti-patterns | "Retrospective theatre" is named; external blame is reframed |
| 6 | Learning | Recurring patterns (3+ times) become rules; prevent repeat mistakes |
| 7 | Guardrails | Retro rejects low-rigor inputs (missing OKRs) |

**Total coverage:** 7 test cases across core functionality, edge cases, guardrails, and learning mechanisms.
