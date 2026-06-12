# experiment-doc-builder.eval.md

Eval test cases for `experiment-doc-builder` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: Formulate Mode — Raw Idea to Validated Experiment

**Input:**
- Mode: Formulate (inferred)
- Idea: "We should make onboarding faster"
- Baseline metric: Unknown
- Hypothesis: Rough ("Faster onboarding = more activation")
- Brain: Exists with ICP (SMB finance), Revenue Levers (activation → trial-to-paid conversion)

**Expected Behavior:**
1. Adaptive tone calibration: User has vague language, no baseline, rough hypothesis → Novice signals
2. Pre-flight loads brain silently (Section 2: ICP, Section 5: Revenue Levers)
3. Interrogation Framework runs (Sections A–E):
   - A. Objective Clarity: "What metric exactly? Activation? Paid conversion? Time-to-value?"
   - User: "Time-to-first-feature-use"
   - Follow-up: "What's the baseline? How many days currently?"
   - User: "~7 days average"
   - B. Hypothesis Rigor: "So your hypothesis is: If we reduce onboarding steps, time-to-first-use will drop to 3 days, because users won't get stuck?"
   - C. Metric Integrity: Primary (time-to-first-use), Secondary (activation), Guardrail (churn doesn't spike)
   - Sample size calculation
   - D. Feasibility: 30-day test window, measure in product analytics
   - E. Risk: Cost of false positive (ship bad flow), cost of false negative (miss 40% faster onboarding)
4. Scoring Rubric applied:
   - Clarity: 20/25 (specific but causal mechanism weak: why would fewer steps help?)
   - Measurability: 23/25 (metrics clear, baseline known)
   - Impact: 16/20 (if we see 50% faster activation, conversion might move 2pp)
   - Feasibility: 18/20 (executable, no major blockers)
   - Learning Value: 8/10 (reduces uncertainty about onboarding friction)
   - **Score: 85/100** → ✅ APPROVED
5. Document generated with Rigor Score shown and all adversarial callout boxes inline

**Success Criteria:**
- Interrogation completed before document (no skip)
- Score shown with rubric breakdown
- Document includes Hypothesis + 3 adversarial challenges
- User knows why they're running this experiment

**Test Pass:** Raw idea becomes rigorous experiment

---

## Test 2: Diagnose Mode — Audit Existing Brief

**Input:**
- Mode: DIAGNOSE
- User pastes draft experiment document:
  - Objective: "Increase conversion" (vague)
  - Hypothesis: "Better UX = more conversion" (not causal)
  - Metrics: "Conversion rate" (primary only, no secondary/guardrail)
  - Sample size: Not calculated
  - Timeline: "Run it for a month" (no power calc)
  - Confounders: Not listed

**Expected Behavior:**
1. Adaptive tone: Intermediate signals (some structure, but weak spots)
2. Scoring Rubric applied:
   - Clarity: 12/25 (objective vague, hypothesis not causal)
   - Measurability: 10/25 (no baselines, no sample size, no measurement method)
   - Impact: 15/20 (conversion improvement is meaningful, but magnitude unknown)
   - Feasibility: 12/20 (timeline too short without power calc, confounders not addressed)
   - Learning Value: 8/10 (reduces uncertainty, but what exactly?)
   - **Score: 57/100** → ❌ REJECTED
3. Output:
   ```
   RIGOR SCORE: 57/100 — ❌ REJECTED
   
   Your experiment needs major work before running.
   
   TOP GAPS:
   1. Objective is vague. "Increase conversion" — by how much? For which cohort?
      → Rewrite: "Increase trial-to-paid conversion rate from baseline 12% to 15%"
   
   2. Hypothesis is not causal. "Better UX = more conversion" — why?
      → Rewrite: "If we reduce checkout form fields from 8 to 4, trial users will complete checkout 40% more, because they'll abandon less due to friction."
   
   3. Missing metrics. Secondary and guardrail missing.
      → Add secondary: "Sign-up completion rate" (leading indicator)
      → Add guardrail: "New user churn >8%" (don't ship if churn spikes)
   
   4. No sample size. How long does this run?
      → Calculate: At 12% baseline, 15% target, 80% power: need ~800 users per variant. At [XXX] signups/day = [Y] days runtime.
   
   5. Confounders? What else could affect conversion in your test window?
      → List: Seasonal pricing changes, parallel product launches, competitor announcement
   
   NEXT STEP: Rewrite objective + hypothesis using Formulate mode, then re-check.
   ```

**Success Criteria:**
- Score is clear with rubric shown
- Gaps are specific (not "be more rigorous")
- Each gap has a rewrite example
- Rejection is firm (not softened)

**Test Pass:** Bad experiments are caught before running

---

## Test 3: Pressure-Test Mode — Adversarial Interrogation

**Input:**
- Mode: PRESSURE-TEST
- User has draft experiment with score 72/100 (passing)
- Hypothesis: "Mobile-optimized checkout reduces bounce from 25% to 20%"
- Assumed user segment: "All mobile users"

**Expected Behavior:**
1. Adversarial prompts deployed:
   - "What data would falsify this hypothesis?"
   - "What alternative explanation fits the evidence?"
   - "Which assumption breaks first?"
   - "What user segment behaves differently?"
2. User: "Well, our conversion varies by traffic source. Organic might respond differently than paid."
3. Follow-up: "That's a critical confounder. Your sample needs to be powered for that split analysis. Does your planned test duration support that?"
4. User: "Hmm, probably not."
5. Score recalculated: Feasibility drops from 18/20 to 12/20 (insufficient sample for segmentation)
6. New score: 78/100 (still passing, but less confident)
7. Recommendation: "You can run this, but you won't get segment insight. Either (a) extend test window to power for segments, or (b) run as all-users test and follow up with segmented analysis post-experiment."

**Success Criteria:**
- Adversarial questions expose weak assumptions
- User is forced to confront them
- Score adjusts based on new insight
- Options are clear (adapt or accept risk)

**Test Pass:** Assumptions are tested before launch

---

## Test 4: Score Mode Only

**Input:**
- /score [experiment brief, already written]
- User wants score only (not full document generation)

**Expected Behavior:**
1. Interrogation Framework not run
2. Scoring Rubric applied to provided document
3. Output:
   ```
   RIGOR SCORE: 81/100
   
   | Category | Score | Note |
   |---|---|---|
   | Clarity | 23/25 | Objective + hypothesis are specific. Causal mechanism is explicit. |
   | Measurability | 24/25 | Baseline, sample size, all metrics defined. Missing: divergence point specificity. |
   | Impact | 18/20 | 40% uplift in conversion is meaningful. Business impact clear. |
   | Feasibility | 16/20 | Executable but 2 confounders need monitoring. |
   | Learning Value | 9/10 | Reduces friction assumption. High strategic relevance. |
   
   VERDICT: ✅ APPROVED — score 81 meets threshold of 70+
   ```

**Success Criteria:**
- Score output is clear
- Rubric breakdown shown
- Pass/fail visible
- No document generated (user asked for score only)

**Test Pass:** Quick scoring for decision-making

---

## Test 5: Evidence vs. False Belief — Black Swan Pattern

**Input:**
- Idea: "We should test using psychology principles to reduce cart abandonment"
- Hypothesis: "Using loss-aversion messaging ('Don't lose access to this price') will reduce checkout abandonment by 30%"
- Knowledge check: `knowledge/false-beliefs/catalog.md` contains:
  ```
  ## Messaging Urgency is Weaker Than Assumed
  - Pattern: Teams assume urgency messaging (scarcity, loss-aversion) drives conversion
  - Observed failure: A/B tests show <5% uplift in hard-commerce, <2% in SaaS
  - Confidence: 12+ experiments, multiple teams, persistent weak effect
  - Implication: Loss-aversion alone is not a strong lever. Requires product friction relief or genuine scarcity.
  ```

**Expected Behavior:**
1. Pre-flight runs knowledge check
2. False belief match found
3. Immediate surface (before interrogation):
   > "⚠️ Pattern match: Your hypothesis assumes loss-aversion messaging is a strong lever. Our knowledge base shows this effect is weak (typically <5% uplift in similar products). This experiment has low expected value. Why not test a stronger lever (e.g., reducing form fields)?"
4. User can:
   - Accept the pattern and pivot to stronger lever
   - Reject the pattern ("Our customers are different") and proceed with caution
   - Run the test anyway but with adjusted confidence
5. If user proceeds: Score includes note: "⚠️ This hypothesis contradicts observed pattern in knowledge base. Expected uplift is lower than user assumes. Feasibility score adjusted down."

**Success Criteria:**
- False belief is surfaced early
- User is aware of pattern
- Score reflects pattern conflict
- User can choose to proceed with eyes open

**Test Pass:** Known weak patterns don't waste time

---

## Test 6: Rejection — Score <70

**Input:**
- Experiment brief:
  - Objective: "Test onboarding" (vague)
  - Hypothesis: "Onboarding changes will improve activation" (not causal, no mechanism)
  - Metrics: None specified
  - Baseline: Unknown
  - Success criteria: Not defined

**Expected Behavior:**
1. Scoring Rubric applied:
   - Clarity: 8/25 (vague objective, vague hypothesis)
   - Measurability: 5/25 (no metrics, no baseline)
   - Impact: 10/20 (activation improvement is meaningful, but unknown what changes will happen)
   - Feasibility: 8/20 (no success criteria, no confounders considered)
   - Learning Value: 6/10 (maybe reduces uncertainty, but what exactly?)
   - **Score: 37/100** → ❌ REJECTED
2. Output:
   ```
   RIGOR SCORE: 37/100 — ❌ REJECTED
   
   This is not ready to test. Before running anything, you need:
   
   1. SPECIFIC OBJECTIVE: "Test onboarding" is too vague.
      → Define: What metric? What's the baseline? What's the target?
      → Example: "Reduce time-to-first-feature-use from 7 days to 4 days"
   
   2. CAUSAL HYPOTHESIS: "Onboarding changes" — what changes, and why would they help?
      → Define: If we [specific intervention], then [metric] changes, because [user behavior changes]
      → Example: "If we skip 'company info' form, users reach first feature 40% faster because they face fewer form fields"
   
   3. METRICS: You didn't name any.
      → Primary: time-to-first-use (from above)
      → Secondary: activation, sign-up completion
      → Guardrail: don't increase churn
   
   4. BASELINE: You need current state before testing new state.
      → How many days currently? Pull this from analytics before the test.
   
   5. SUCCESS CRITERIA: When do you ship this? When do you kill it?
      → Define: "If time-to-first-use ≤4 days, ship. If >5 days, kill."
   
   NEXT STEP: Run Interrogation Framework (Formulate mode) before building the document again.
   ```
3. No document is generated
4. Rejection is not softened

**Success Criteria:**
- Score clearly below 70
- Rejection is explicit
- Top gaps are listed (not generic)
- Each gap has a fix example
- Next step is clear

**Test Pass:** Rigor prevents bad experiments from shipping

---

## Test 7: Learning Mode — Pattern Capture

**Input:**
- Experiment document generated and scored 75/100
- Session complete
- Learning close runs at end

**Expected Behavior:**
1. Step 1 (unstructured): "Is there anything you want to say out loud before we close?"
   User: "I'm realizing we always assume faster onboarding is better, but we never measure user satisfaction post-onboarding."
2. Capture: Pattern identified (satisfaction gap in onboarding metrics)
3. Step 2 (structured): Three questions
   - "Was there a risk that surprised you?" → User: "Yeah, we didn't think about international user behavior."
   - "What assumption breaks first?" → User: "Probably the 7-day baseline — that's just our English-speaking cohort."
4. Step 3 (proposal): "Here's what I'm proposing to add to the knowledge base:
   - New pattern: "Onboarding metrics focus on speed, not satisfaction or localization"
   - Confirmed observation: "English-speaking cohort ≠ global average"
   - Location: `knowledge/craft/patterns.md` + `knowledge/false-beliefs/catalog.md`
   - Approve?"
5. User: "Yes"
6. Session logged to `knowledge/sessions/log.md`:
   - What was produced: Formulate mode, onboarding experiment, score 75
   - What got pushback: User's assumption about baseline (adjusted for localization)
   - Pattern: Satisfaction metrics missing from onboarding tests

**Success Criteria:**
- Unstructured prompt runs first
- Patterns captured
- Updates proposed (never silent)
- Approval required
- Session logged
- Learning is explicit

**Test Pass:** Experiments become learnings; knowledge compounds
