# Evals — experiment-doc-builder skill v2.2.0

Testing user onboarding, statistical literacy, and rigorous gatekeeping. Does the skill teach users what they need to know before building an experiment?

---

## Test Case 1: Complete Novice — Full Discovery Flow

**Input:**
User: "I'm a product manager at a B2B SaaS company. I have an idea — I think we should test increasing the size of our 'Try Free' button. It's currently small. I think it will get more clicks."

No baseline provided. No hypothesis about causation. No mention of sample size.

**Expected output includes:**

**Step 1 (Role Discovery):**
- Skill confirms: "You're a PM. Got it. You're testing a conversion hypothesis."
- Follow-up: "What's your current conversion rate for new visitors? Where's that number from?"

**User responds:** "It's 3.2%. From Amplitude, last 30 days."

**Step 1 continues:**
- "Good. So your metric is: visitors who click 'Try Free' and land on signup page."
- "Your hypothesis is: bigger button = more clicks. Why do you think that's true?"
- "Is it because: (a) people notice it more, (b) they perceive it as more important, or (c) something else?"

**User responds:** "Probably (a). Bigger = more noticeable."

**Step 2 (Statistical Significance Teaching):**

Skill educates:
> "Here's the reality. You want to move from 3.2% to, let's say, 3.8% (0.6pp). 
> That requires ~19,000 users per variant to detect with 80% power.
> If you get 500 new visitors per day, that's 38 days for one variant alone.
> 76 days total (control + treatment), or 2.5 months.
> 
> Is a bigger button worth testing if it takes 2.5 months to know? Let's think about that."

**User:** "Hmm, that's longer than I expected. What if we aimed higher — like 4.5%?"

**Step 2 continues:**
> "1.3pp absolute lift. That requires ~8,500 per variant.
> 17 days for one variant. 34 days total. Much better.
> But is a 1.3pp lift realistic for a bigger button? That seems optimistic."

**Step 3 (Pressure-Test):**
- "Let's reality-check this. Have you tested button size before?"
- "What's your evidence that button size drives perceived importance?"
- "What happens if it doesn't work? Do you ship a bigger button that looks worse?"
- "What other metrics matter? (e.g., Does bigger button create mobile friction?)"

**User:** "Actually, I haven't tested this before. And now that you mention it, bigger might look bad on mobile."

**Step 4 (Feasibility):**
- "Mobile is a problem. Is mobile in your addressable pool?"
- "If yes: we need to exclude mobile or test mobile separately. That cuts your daily traffic."
- "New timeline: 40–60 days. Still worth it?"

**User:** "Actually, 60 days feels too long. And I'm not sure about the mobile impact. Maybe we should do user research first?"

**Expected output excludes:**
- No brief generated (score <70 due to unclear mechanism, untested assumption)
- No gatekeeping bypass

**Next Step:** "Before we test, do 5–10 user interviews. Ask: Do you notice button size? Does it affect your decision to try the product? Then come back with real evidence."

**Session logged:** 
```
Role: Product Manager
Metric: CTA button click-through rate
Decision: REJECTED — No evidence for mechanism, mobile impact unclear
Score: 42/100 (Clarity 12/25: unclear causation; Measurability 15/25: scale OK but timeline too long; Impact 8/20: 1.3pp is aggressive estimate; Feasibility 7/20: mobile contamination)
Recommendation: Conduct user research to validate causation before testing
```

**Pass condition:**
User learns: (1) statistical significance requires real sample sizes, (2) their timeline, (3) their assumptions are tested, (4) rejection is OK if idea isn't ready.

---

## Test Case 2: Growth Marketer — Email Subject Line (Low-Lift Idea)

**Input:**
User: "I'm a growth marketer. I want to test email subject line variations. Something like emoji vs. no emoji in the subject line. We send 100k emails per week."

Baseline open rate: 18% (from email platform).

**Expected output includes:**

**Step 1:** Skill confirms role, clarifies metric = open rate (18%).

**Step 2 (Scale Teaching):**
> "You want to test emoji vs. no emoji. That's probably a 0.5–1pp lift best case.
> 100k emails per week = 50k per variant per week.
> For 0.5pp lift: you need ~30,000 opens per variant to be significant.
> 50k emails × 18% open rate = 9k opens.
> 
> You'd need 3–4 weeks to reach statistical power.
> Is that timeline OK?"

**User:** "Yeah, 3–4 weeks is fine."

**Step 3 (Pressure-Test):**
- "Emoji in subject lines: what evidence says this works?"
- "For your audience specifically? (Not general benchmarks, but your users.)"
- "What's the failure mode? If emoji backfires, what happens to trust?"
- "What would you NOT expect to change? (e.g., click-through rate, conversion downstream — just opens?)"

**User:** "Good point. I've seen emoji work in B2C. We're B2B. Our users are IT directors. Emoji might look unprofessional."

**Step 4 (Feasibility):**
- "That's a real risk. Are you willing to contaminate professional perception for 0.5pp lift?"
- "Alternative: test among a B2B segment that's more casual, not directors."
- "Or: test something that's less risky. What about subject line length? That's more obviously professional."

**User:** "Yeah, emoji feels risky. Let's test subject line length instead. Short vs. long."

**Expected output includes:**
- Hypothesis revised: "If we shorten subject lines, opens stay the same or go up, because [user provides mechanism]"
- Pressure-test surfaces emoji risk → user changes idea
- New scoring based on revised hypothesis

**Pass condition:** User discovers their own idea was risky, changes direction, lesson learned before any experiment ran.

---

## Test Case 3: Product Manager — Pricing Test (High-Impact, High-Risk)

**Input:**
User: "I'm a PM. We want to test price. Current: $99/month. We want to try $79/month. Our LTV is $600. We get 50 new customers per month."

Baseline: 50 customers/month at $99 = $4,950 MRR from new cohort.

**Expected output includes:**

**Step 1:** Role confirmed. Metric = conversions and revenue.

**Step 2 (Scale Teaching):**
> "You get 50 new customers/month = ~1.7/day.
> To measure a conversion lift from price change: you need ~1,500–2,000 users per variant.
> At 1.7/day: that's 900–1,200 days per variant.
> That's 2.5–3+ YEARS.
> 
> This is not testable with A/B testing at your scale.
> Alternative: (a) pilot with one cohort for 3 months, (b) use qualitative research, (c) competitive pricing analysis."

**User is shocked:** "Oh wow. So we just... can't test this?"

**Step 2 continues:**
> "Not with an A/B test. But you CAN:
> - Launch at $79 with cohort 1 for 3 months, measure NPS/churn/LTV
> - Stay at $99 with other segments as quasi-control
> - Use that data to decide future cohorts
> That's not statistically perfect, but it's honest about your constraints."

**Step 3 (Pressure-Test):**
- "Risk: What's the downside if $79 is wrong?"
  - Lost revenue: 50 customers × $20 = $1,000/month
  - That's -$12k/year per cohort
- "Do you have 3 months of runway to absorb that?"
- "What metrics tell you to stop if it's going badly?"

**User:** "Yeah, I can absorb that. I'd want to watch churn and NPS closely."

**Expected output:**
- NOT an A/B test brief (scale prohibits it)
- Instead: Pilot launch brief with guardrail metrics
- Decision point: after 3 months, choose full rollout or revert

**Pass condition:** User learns their idea isn't testable as designed, but gets a realistic alternative that still answers the question.

---

## Test Case 4: Designer — Conversion-Rate Hypothesis (Weak Causation)

**Input:**
User: "I'm a designer. I've redesigned our product onboarding. It looks better and is more intuitive. I think users will complete onboarding faster and be more likely to activate. Can we test it?"

Baseline activation rate: 42% (users who complete onboarding and use the product).

**Expected output includes:**

**Step 1:** Skill clarifies: "Designer testing product change. Metric = activation rate (42%)."
- "Your hypothesis: better UX → faster completion → more activation."
- "Is it: (a) intuitive design is easier to use, (b) better visual design makes users feel confident, or (c) both?"

**User:** "Both, probably. The design is cleaner and the flow is simpler."

**Step 2 (Scale Teaching):**
> "Your baseline is 42%. Let's say you expect 48% (6pp lift).
> That requires ~800 users per variant.
> If you get 200 sign-ups per day, that's 4 days per variant, 8 days total.
> Sample size: easily achievable."

**Step 3 (Pressure-Test):**
- "What specifically makes the new design more intuitive?"
- "Have any users seen both designs? Can you get qualitative feedback?"
- "What if the lift is just novelty effect? (Users click around because it's new, not because it's better.)"
- "Secondary metric: time spent in onboarding. If users rush through, is that good?"
- "Guardrail metric: bounce rate. Does new design inadvertently hide the value prop?"

**User:** "Hmm, I haven't thought about novelty effect. And we should definitely track bounce rate. What about task completion time?"

**Step 4 (Feasibility):**
- "Yes, time-to-completion is important. Add as secondary metric."
- "Can you measure both completion AND activation? (Not everyone who completes activates.)"
- "Any risk of users who saw old design seeing new design mid-flow? (Reload bugs?)"

**User:** "Good questions. We can exclude mid-flow, and yes, we'll measure both."

**Step 5 (Scoring):**
- Clarity: 20/25 (hypothesis clear but mechanism includes multiple factors — hard to isolate)
- Measurability: 22/25 (baseline clear, sample size OK, metrics defined)
- Impact: 18/20 (6pp is meaningful, but novelty risk reduces confidence)
- Feasibility: 18/20 (technical clean, but design changes can leak to control)
- Learning Value: 10/10 (answers critical question about UX)
- **Total: 88/100** ✅ APPROVED

**Brief generated:** Includes guardrails for novelty effect and bounce rate.

**Pass condition:** Designer learns to think causally, adds guardrails, reaches approval through iterative refinement.

---

## Test Case 5: Multiple Experiments — Pattern Detection

**Input:**
Three consecutive experiments, all rejected for same reason:

1. **Session A:** Marketing: "Test email send time. Weekday vs. weekend."
   - No baseline: "I think Monday works best"
   - Rejected: 28/100 — "No baseline open rate or click rate provided"

2. **Session B:** Product: "Test call-to-action copy. Variant A vs. Variant B."
   - No baseline: "Currently people click sometimes"
   - Rejected: 35/100 — "No baseline CTR or volume"

3. **Session C:** Growth: "Test landing page headline. Short vs. long."
   - No baseline: "We get signups currently"
   - Rejected: 22/100 — "No baseline conversion rate"

**Pattern detected:** Users don't bring baseline metrics.

**Expected output:**
- After Session C, skill surfaces pattern:
  ```
  🔁 PATTERN DETECTED
  I've rejected 3 experiments this month for missing baseline metrics.
  All three: "What's your current rate?" → User didn't have it ready.
  
  Proposal: In future sessions, I'll ask for baseline BEFORE discussing the idea.
  This saves everyone time. 
  
  Approve?
  ```

**User approves.**

**Session 4 (New User):**
Skill loads rule from context: "Baseline metrics are mandatory."

New user: "I want to test..."

Skill stops them immediately:
> "Before we talk about the idea, I need one number: What's your current [metric] rate?
> (Where's it from? When? What segment?)"

User brings baseline first → interrogation starts faster.

**Pass condition:** Pattern detected, rule created, prevents same mistake in future.

---

## Test Case 6: Statistical Significance — User Realizes Idea Isn't Viable

**Input:**
User: "I'm a product manager. We have a mobile app. I want to test a notification optimization. Different notification times."

Current metric: Notifications are opened 35% of the time.  
Daily active users: 2,000  
Hypothesis: Optimized time = 40% open rate (5pp lift)

**Expected output:**

**Step 2 (Scale Reality Check):**
> "You have 2,000 DAU. For a 5pp lift from 35% to 40%:
> You need ~14,000 opens per variant.
> 2,000 users × 35% = 700 opens/day.
> To reach 14,000: you need 20 days per variant.
> 40 days total to be significant.
> 
> That's doable. Let's continue."

**User proceeds to Step 3.**

**Step 3 (Pressure-Test):**
- "What evidence says notification time affects opens?"
- "Have you surveyed users about preferred notification times?"
- "Are you testing globally or by timezone?"

**User:** "Actually, I haven't researched this. I just thought different times might be better. And yeah, timezone is a problem. We're global."

**Step 4 (Feasibility Revised):**
- "Timezone is a blocker. If you segment by timezone, each segment has ~200 DAU."
- "For a 5pp lift in a 200-user segment: you'd need 40 days per variant per timezone."
- "That's months of testing, and you'd need to run separate experiments per timezone."
- "Is this still worth it?"

**User:** "No. That's too complex. But what if we just test US timezone only?"

**Feasibility recalculated:**
- US only: 500 DAU (rough estimate)
- 5pp lift: 3,500 opens per variant needed
- 500 × 35% = 175 opens/day
- 20 days per variant = 40 days total
- **Timeline: still 1.5 months**

**User realizes:** "OK, 1.5 months for a feature I'm not even sure will work. Maybe I should do user research first, validate that time-of-day matters at all."

**Expected output:**
- Score drops: Clarity 8/25 (no evidence mechanism is real)
- **Total: <70** ❌ REJECTED
- **Next Step:** "Validate with user research: survey 20 users about notification preferences. If 80%+ say 'yes, time matters,' come back with a hypothesis."

**Session logged:** 
```
Role: Product Manager  
Metric: Notification open rate
Decision: REJECTED — Untested assumption, global timezone complexity
Score: 32/100
Recommendation: User research validation before experiment
```

**Pass condition:** User learns to validate assumptions before testing, realizes sample size requirement made idea unfeasible.

---

## Test Case 7: Brain Dependency — ICP Informs Audience Scope

**Input:**
User: "I'm a marketer. We want to test homepage messaging. Change from 'Get Started' to 'Start Your Free Trial.' We're testing with all visitors."

Brain.md shows: **ICP = Mid-market SaaS (50–500 seats), IT/DevOps buyers.**

**Expected output:**

**Step 1:** Skill loads ICP from brain.
- "Your ICP is mid-market IT/DevOps."
- "Testing 'all visitors' includes: free-tier hobbyists, enterprise >500 seats, solo developers."
- "Most of those aren't your customer. Should we scope to your ICP?"

**User:** "Good point. We care about mid-market. Let's exclude <50 and >500."

**Step 2 (Revised Scale):**
> "Scoping to ICP reduces addressable pool by ~40%.
> Your baseline CTR changes from 8% (all) to 6% (ICP only).
> New sample size calculation based on actual customer segment."

**Session logged:** "Audience scope informed by ICP definition."

**Pass condition:** ICP informs experiment design upfront. Prevents wasted testing on out-of-scope segments.

---

## Test Case 8: Guardrail Violation — Confounder Blocks Test

**Input:**
User: "I want to test a new checkout flow. We're launching it Wednesday."

Baseline conversion: 4.2%  
Addressable traffic: 5k/week  
Expected lift: 0.5pp

Problem: "New payment processor integration is launching Wednesday too."

**Expected output:**

**Step 4 (Feasibility):**
- Skill flags: "You have a confounder. New payment processor = uncontrolled variable."
- "Can you isolate? (i.e., launch checkout flow solo, payment processor next week?)"

**User:** "No, payment processor is non-negotiable. It has to be Wednesday."

**Step 4 (Guardrail Enforced):**
> "Then this experiment is invalid. You can't measure checkout impact when payment processing changes simultaneously.
> 
> Option A: Delay checkout test to next week (wait for payment processor to stabilize)
> Option B: Don't test, just ship checkout at same time
> Option C: Run pilot with one segment, check conversion, but accept it's not statistically clean
> 
> Which do you choose?"

**User:** "We need payment processor Wednesday. Let's do Option C — pilot with one segment."

**Expected output:**
- No A/B test brief generated (invalid design)
- Instead: **Pilot Launch Brief** with guardrail metrics
- Document conversion tracking but acknowledge statistical ambiguity
- Decision point: after 1 week, decide on rollout

**Pass condition:** Confounder caught, invalid design rejected, realistic alternative offered.

---

## Verification Checklist

After running all 8 test cases:

- [ ] TC1: Novice user learns statistical significance, timeline, rejects weak idea
- [ ] TC2: Marketer discovers own idea is risky, pivots, learns before testing
- [ ] TC3: PM learns their idea isn't testable with A/B, gets pilot alternative
- [ ] TC4: Designer adds guardrails through pressure-test, reaches approval
- [ ] TC5: Pattern detected (missing baselines), rule created, prevents mistakes
- [ ] TC6: User realizes sample size makes idea unfeasible, defers to research
- [ ] TC7: ICP informs audience scope, improves experiment design
- [ ] TC8: Confounder caught, invalid test design rejected, pilot alternative offered

**All 8 passing = skill teaches users statistical literacy + gatekeeping.**

---

## Success Criteria

**User understands:**
- Their role and how it shapes their experiment
- What statistical significance means
- How to calculate sample size (rough, not precise)
- Why baselines matter
- Why confounders invalidate tests
- When an idea isn't ready for testing

**Skill rejects:**
- Experiments with no baseline
- Ideas with untested causal mechanisms
- Tests with uncontrolled confounders
- Designs requiring impossible sample sizes

**Skill approves:**
- Ideas with clear baselines, realistic lift, feasible timeline, controlled confounders

---

## Estimated Runtime

~25 minutes for all 8 cases (some cases are fast rejections, which is the point).
