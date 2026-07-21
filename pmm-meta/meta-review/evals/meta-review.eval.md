---
name: meta-review.eval
version: 2.0.0
description: >
  Comprehensive eval suite for meta-review v2.0.0. Tests: quality scoring mechanics,
  tier-specific validation, trending analysis, CI/CD gate logic, auto-fix recommendations,
  confidence prediction, and guardrail triggering. 10 scenarios covering all output types
  (GTM brief, positioning, beachhead, pre-mortem, retro) and all tiers (T1-T4).
---

# Meta-Review v2.0.0 — Eval Suite

## Setup (Universal)

Each eval:
1. Simulates a skill session output (GTM brief, positioning, etc.)
2. Specifies output type, tier, and content
3. Triggers meta-review (auto-detect)
4. Evaluates: scoring → tier match → trend analysis → CI/CD gates → recommendations → logging
5. Validates outputs: quality score, grade, gate results, fixes, confidence

---

## Eval 1: Quality Scoring (GTM Brief, T2)

**Scenario:** GTM brief output, assigned T2. Meta-review scores it against GTM brief rubric.

**Test Data:**
```
Skill: go-to-market-strategy
Output type: GTM brief
Tier: T2
Content: 
  - Clear positioning vs. 2 competitors
  - Channel strategy: PR + paid digital + sales enablement
  - Success metrics: 500 new leads (T2 target)
  - Timeline: 90 days, feasible resources
  - Risks: 3 identified, 2 with mitigation plans
```

**Expected Output:**
```
Quality Score: GTM Brief (100 pts)

Positioning Clarity (20 pts): 15/20
  Evidence: "Positioning is clear vs. incumbents, owns a value angle (faster + cheaper).
            Slightly incremental, could be bolder."
  
Channel Strategy (20 pts): 18/20
  Evidence: "Channels are prioritized (PR primary, digital secondary). Timeline is realistic.
            Minor gap: no regional breakdowns."

Success Metrics (20 pts): 18/20
  Evidence: "Metrics include target (500 leads) and success ranges (350-600). Missing: 
            leading indicators (e.g., opps by week)."

Competitive Context (15 pts): 12/15
  Evidence: "References 2 key competitors + status quo. Good vs/then language. 
            Could add one more alternative."

Timeline & Resources (15 pts): 14/15
  Evidence: "90-day plan is realistic. Resources allocated. Minor: one dependency
            not fully owned."

Risk Mitigation (10 pts): 8/10
  Evidence: "3 risks identified, 2 have mitigation plans. One risk (sales adoption)
            lacks detailed mitigation."

TOTAL: 85/100 (B+, 85%)
```

**Pass Criteria:**
- All 6 dimensions scored (no missing scores)
- Points awarded honestly (not inflated)
- Evidence-based (quotes/examples from output)
- Final score calculated correctly (85/100)
- Grade assigned (B+) correct for score

---

## Eval 2: Tier Comparison (T2 Brief Scoring 85)

**Scenario:** Output scores 85/100. Compare to T1/T2/T3/T4 standards.

**Test Data:**
```
Output score: 85/100
Assigned tier: T2
```

**Expected Output:**
```
Tier Comparison:

T1 Standard (90+ required): ❌ BELOW (85 < 90)
  Gap: 5 points (would need bolder positioning)

T2 Standard (75+ required): ✅ PASSES (85 > 75)
  Status: ABOVE threshold
  Confidence: MEDIUM (85 is above minimum, but only 10 points above)

T3 Standard (60+ required): ✅ PASSES EASILY
T4 Standard (50+ required): ✅ PASSES EASILY

Tier Assessment: ✅ T2 is correct tier
Recommendation: Output is T2-appropriate. Would need ~5 more points (bold positioning) 
for T1 readiness.
```

**Pass Criteria:**
- Tier minimums checked correctly (T1: 90+, T2: 75+, T3: 60+, T4: 50+)
- Gap calculation accurate (85 vs. each tier minimum)
- Tier recommendation correct (T2 appropriate)
- Confidence level assessed (MEDIUM for T2)

---

## Eval 3: Trending Analysis (User's 90-Day History)

**Scenario:** This GTM brief scores 85/100. User's historical GTM brief scores: 74, 76, 77, 78. Detect trend.

**Test Data:**
```
Historical scores (GTM brief, past 90 days):
  2026-05-21: 71/100
  2026-06-04: 74/100
  2026-06-18: 76/100
  2026-07-01: 77/100
  2026-07-21: 85/100 (today)

Average: 76.6/100
Today: 85/100
Gap: +8.4 points above average
Trend: ↗️ Improving (+3.5 pts/month average)
```

**Expected Output:**
```
Quality Trends (GTM Brief, Past 90 Days)

Historical scores: 71 → 74 → 76 → 77 → 85
Average: 76.6/100
Today's score: 85/100
Gap from average: +8.4 points

Trend: ↗️ IMPROVING
  Rate: +3.5 points per month (consistent trajectory)
  Volatility: Low (never below 71, steady climb)

Benchmark:
  Your GTM brief average: 76.6/100
  Today: 85/100 (best score yet)
  
Insight: "GTM briefs are improving steadily. This is your highest score yet, +8.4 
points above your average. Keep pushing on positioning clarity — that's your 
leverage for the next 5-10 points to T1 territory."
```

**Pass Criteria:**
- Historical scores loaded correctly
- Average calculated (76.6)
- Gap calculated (85 - 76.6 = 8.4)
- Trend detected (improving, not declining)
- Trend rate estimated (+3.5 pts/month)
- Benchmark comparison made (above average, personal best)

---

## Eval 4: Auto-Fix Recommendations (Priority-Ranked)

**Scenario:** Output scores 85, tier T2. Generate specific, actionable fixes ranked by impact.

**Test Data:**
```
Low scores identified:
  - Positioning Clarity: 15/20 (gap: positioning feels incremental)
  - Risk Mitigation: 8/10 (gap: sales adoption risk lacks mitigation)
```

**Expected Output:**
```
Auto-Fix Recommendations (Impact Order)

FIX 1: Sharpen Positioning Differentiation [HIGH IMPACT]
  Current: "Faster and cheaper than incumbent"
  Problem: Incremental, doesn't own unique value
  Suggested fix: Reframe as "Only platform that [owns unique angle incumbent can't]"
  Impact: +5 points (positions → 20/20)
  Effort: 30 min
  Result if fixed: 85 → 90 (enters T1 territory)

FIX 2: Detail Sales Adoption Mitigation [MEDIUM IMPACT]
  Current: "Sales adoption risk identified but no plan"
  Problem: One of top 3 risks, lacks mitigation detail
  Suggested fix: Add specific steps: (1) Enablement timeline, (2) Success metrics, (3) Escalation path
  Impact: +2 points (risk mitigation → 10/10)
  Effort: 15 min
  Result if fixed: 85 → 87

Quick Wins: 2 fixes, 45 min total, +7 points (85 → 92, T1-ready)
```

**Pass Criteria:**
- Fixes ranked by impact (high first)
- Fixes are specific, not vague
- Each fix includes: current state, problem, fix, impact, effort
- Estimated impact realistic (tied to scoring rubric)
- Total effort and result shown (45 min, +7 points)

---

## Eval 5: CI/CD Gate Evaluation (T2 Output, Score 85)

**Scenario:** T2 output scores 85/100. Run all 5 CI/CD gates. Should it be approved for deployment?

**Test Data:**
```
Output score: 85/100
Tier: T2
Critical gaps: 0
Active guardrails for T2: champion_alignment, messaging_clarity, metric_rigor
Guardrail status:
  - champion_alignment: PASS (champion identified + aligned)
  - messaging_clarity: HIT (positioning feels incremental)
  - metric_rigor: PASS (metrics have confidence bands)
Trend: Improving (+3.5 pts/month)
Confidence prediction: 72%
```

**Expected Output:**
```
CI/CD Gate Evaluation (T2 Brief)

Gate 1: Quality Score Minimum
  Rule: T2 requires 75+
  Output: 85
  Check: 85 >= 75? YES ✓
  Result: PASS

Gate 2: Critical Issues
  Rule: Must have 0 critical gaps
  Found: 0
  Check: 0 == 0? YES ✓
  Result: PASS

Gate 3: Guardrail Compliance
  Active guardrails: champion_alignment, messaging_clarity, metric_rigor
  
  champion_alignment: ✅ PASS
  messaging_clarity: ⚠️ HIT (positioning incremental)
  metric_rigor: ✅ PASS
  
  Check: All pass? NO ⚠️
  Result: FAIL (messaging_clarity hit)

Gate 4: Quality Trend (WARNING ONLY, NON-BLOCKING)
  Rule: Trend should not be declining
  Trend: Improving ↗️
  Result: WARN PASS (no decline)

Gate 5: Confidence Prediction (WARNING ONLY)
  Rule: T2 requires 60%+ confidence
  Confidence: 72%
  Check: 72% >= 60%? YES ✓
  Result: PASS

OVERALL: ❌ BLOCKED (Gate 3 failed)

Decision: Deployment BLOCKED
Reason: Guardrail "messaging_clarity" triggered (positioning feels incremental)
Options: (a) Run Fix 1 (reframe positioning), (b) Request guardrail exception, (c) Downgrade tier

Next: Fix 1 estimated to take 30 min, boost score to 90, clear guardrail.
```

**Pass Criteria:**
- All 5 gates evaluated (none skipped)
- Gate 1 pass/fail correct (85 >= 75)
- Gate 2 pass/fail correct (0 critical gaps)
- Gate 3 evaluates all active guardrails
- Gate 3 correctly identifies messaging_clarity as HIT
- Gates 4-5 are warnings (non-blocking)
- Overall decision is BLOCKED (Gate 3 failed)
- Clear action recommended (Fix 1, request exception, or downgrade)

---

## Eval 6: Guardrail Hit Scenario (Messaging Clarity Triggered)

**Scenario:** Positioning output triggers "messaging_clarity" guardrail. Understand why and surface alert.

**Test Data:**
```
Output: Positioning statement "We're faster and cheaper than competitor X"
Guardrail: messaging_clarity
  Rule: "Positioning must own unique value angle, not iterate incumbent"
```

**Expected Output:**
```
Guardrail Hit Alert:

🟡 MEDIUM PRIORITY: "Messaging Clarity" Guardrail Triggered

Rule: "Positioning must own unique value angle, not iterate incumbent"

Why triggered: Output says "faster + cheaper" but doesn't own a unique value angle.
  Status quo position: "We're like them but better on price/speed"
  Weak point: No unique angle the incumbent can't copy (e.g., unique technology,
              unique business model, unique customer segment ownership)

Impact: Reduces success confidence from 75% to 72% (3 point penalty)

What to do:
  1. Identify unique angle incumbent doesn't own (technology, go-to-market, vertical focus, etc.)
  2. Reframe positioning around that angle
  3. Re-run meta-review (guardrail should clear)

Example reframe:
  Current: "We're faster and cheaper"
  Reframed: "We're the only platform built for [vertical] workflows, with 2x faster 
            setup than [incumbent], enabling ROI in [timeframe]"
```

**Pass Criteria:**
- Guardrail identified correctly (messaging_clarity)
- Rule explained clearly (unique value angle)
- Why it triggered articulated (doesn't own unique angle)
- Impact shown (confidence -3 points)
- Specific recommendation given (identify + reframe)
- Example reframe provided

---

## Eval 7: Confidence Prediction (Will This Launch Succeed?)

**Scenario:** T2 GTM brief scores 85/100. Predict success probability at T2.

**Test Data:**
```
Output score: 85/100
Tier: T2
Guardrails: 1 hit (messaging), 2 pass
Historical data: T2 outputs scoring 80-90 succeed 70% of the time
Current trend: Improving
Execution risk: Medium (depends on sales enablement)
```

**Expected Output:**
```
Tier Success Prediction: T2 Launch

Confidence: 72% ± 10%

Reasoning:
  Quality score: 85/100 (good for T2, above minimum)
  Historical baseline: T2 outputs scoring 80-90 have 70% success rate
  Guardrail hits: 1 hit (messaging clarity) → -2% confidence penalty
  Execution risk: Medium (sales enablement quality will matter)
  Team capability: Strong (historical trend is improving)

Success probability: 72% (will hit T2 targets in ±20% range)
  Low end: 62% (if sales enablement weak, positioning doesn't land)
  High end: 82% (if sales nails execution, positioning resonates)

Risk factors:
  🔴 (none critical)
  🟡 Positioning feels incremental (guardrail hit) — medium risk
  🟢 Metrics are solid and measurable
  🟢 Team has improving track record

Recommendation:
  → Proceed with T2 launch (72% confidence is acceptable for T2)
  → Fix #1 (reframe positioning) to boost confidence to 78%+
  → Monitor deal velocity vs. prediction (early signal of success/failure)
```

**Pass Criteria:**
- Confidence % calculated (72%)
- Confidence range shown (±10%)
- Historical baseline referenced (70%)
- Penalty applied for guardrail hit (-2%)
- Low/high scenarios shown (62-82%)
- Risk factors assessed (none critical, 1 medium)
- Recommendation clear (proceed, fix messaging, monitor)

---

## Eval 8: Tier Reassignment (Assigned T3, Quality is T1)

**Scenario:** Output assigned T3, but scores 92/100 (T1 quality). Flag mismatch.

**Test Data:**
```
Assigned tier: T3 (minor feature)
Output score: 92/100 (excellent quality)
T1 standard: 90+
Mismatch: Significant (output is 2 tiers above assignment)
```

**Expected Output:**
```
Tier Mismatch Alert: QUALITY > ASSIGNED TIER

Assigned: T3 (minor update)
Output quality suggests: T1 (premium/strategic)
Gap: 2 tiers (92/100 > 90 T1 minimum)

Interpretation: Output is over-engineered for T3 scope.

Options:
  1. Upgrade scope to T1 (give output T1 visibility + budget)
     → Leverage high quality for maximum impact
     → Appropriate if strategic value is high
  
  2. Accept T3 (proceed with T3 launch plan)
     → Output is more than sufficient for T3
     → Excess quality won't hurt, just unused

  3. Dial back quality to match T3 (optional, not recommended)
     → T3 only requires 60+
     → Why reduce quality if achieved 92?

Recommendation: Upgrade to T1 scope if strategic value justifies.
Otherwise: Accept T3 launch, enjoy over-quality buffer.
```

**Pass Criteria:**
- Mismatch detected (assigned T3, quality T1)
- Gap calculated correctly (2 tiers)
- Options presented (upgrade, accept, dial back)
- Recommendation clear (upgrade if strategic value warrants)
- Not forcing a tier change, just surfacing the mismatch

---

## Eval 9: Multi-Output Trending (Spot Patterns Across Skills)

**Scenario:** Review quality scores across 5 skill outputs over 1 month. Identify patterns.

**Test Data:**
```
Outputs (past 30 days):
  1. GTM brief (T2): 78/100 (2026-07-01)
  2. Positioning (T1): 88/100 (2026-07-08)
  3. Pre-mortem (T3): 65/100 (2026-07-15)
  4. Beachhead analysis (T2): 82/100 (2026-07-18)
  5. GTM brief (T2): 85/100 (2026-07-21)

Aggregate trend: 78 → 88 → 65 → 82 → 85
Average: 79.6/100
```

**Expected Output:**
```
Quality Trending (Multi-Skill, Past 30 Days)

Outputs: 5 reviews across 3 skills
Average quality: 79.6/100 (solid performance)

Skill breakdown:
  GTM brief (2 outputs): 78, 85 → avg 81.5 (improving)
  Positioning (1 output): 88 → excellent
  Pre-mortem (1 output): 65 → below average (watch)
  Beachhead (1 output): 82 → good

Pattern 1: GTM brief quality improving (+7 points, 78 → 85)
  Insight: "Getting better at GTM briefs. Keep pushing on positioning."

Pattern 2: Pre-mortem scores lower than other skills (65 vs. 81.5 avg)
  Insight: "Pre-mortem outputs are weaker. Consider: skill gaps? Different reviewer
            standard? More risky initiatives being pre-mortemed?"

Recommendation:
  → Continue GTM brief work (trajectory is strong)
  → Debug pre-mortem (why lower scores? Skill issue or harder projects?)
  → Maintain positioning quality (88 is excellent)
```

**Pass Criteria:**
- Average calculated correctly (79.6)
- Skill-level averages calculated (GTM 81.5, positioning 88, etc.)
- Trends identified (GTM improving, pre-mortem lower)
- Patterns surfaced (not just raw scores)
- Recommendations actionable (continue X, debug Y)

---

## Eval 10: End-to-End Workflow (Score → Gates → Fix → Resubmit)

**Scenario:** User submits GTM brief. Score 78 (T2, but close to minimum). Gates block on guardrail. User fixes. Resubmit → passes.

**Cycle 1 (Initial Submission):**
```
Output: GTM brief, assigned T2
Score: 78/100 (C+, acceptable but weak)
Gate 1: ✅ PASS (78 >= 75)
Gate 2: ✅ PASS (0 critical gaps)
Gate 3: ❌ FAIL (messaging_clarity guardrail hit)
Decision: BLOCKED

Recommendation:
  Fix 1: Reframe positioning (30 min, +5 points → 83)
  OR: Request guardrail exception
```

**Fix Applied:**
```
User runs Fix 1 (reframe positioning)
New positioning: "The only platform purpose-built for [segment], enabling [outcome]
                 in [timeframe]. [Incumbent] requires [workaround]."
Resubmit to meta-review.
```

**Cycle 2 (After Fix):**
```
Output: Same GTM brief, updated positioning
Score: 83/100 (B, good)
Gate 1: ✅ PASS (83 >= 75)
Gate 2: ✅ PASS (0 critical gaps)
Gate 3: ✅ PASS (messaging_clarity now passes, positioning owns unique angle)
Gate 4: ✅ PASS (trend improving)
Gate 5: ✅ PASS (confidence 75% > 60% minimum)

Decision: ✅ ALL GATES PASS → Deployment Approved

Quality Summary:
  Score progression: 78 → 83 (+5 points)
  Time to fix: 30 min
  Result: T2-ready for launch
  Confidence: 75% (good for T2)
```

**Expected Output:**
```
Quality Review Workflow Complete

Submission 1 (2026-07-21 10:00 UTC):
  Score: 78/100 (C+)
  Gates: BLOCKED (messaging_clarity guardrail hit)
  Recommendation: Run Fix 1

Submission 2 (2026-07-21 10:35 UTC):
  Score: 83/100 (B)
  Gates: ✅ ALL PASS
  Decision: Deployment Approved

Summary:
  Score improvement: +5 points (78 → 83)
  Effort: 30 min
  Result: T2 launch approved
  Next: Deploy to sales team
  Monitor: Deal velocity vs. 75% success prediction
```

**Pass Criteria:**
- Initial score calculated (78)
- Gates evaluated (3 gates, 1 fail: messaging)
- Auto-fix recommended (Fix 1 with impact)
- Fixed positioning generated (new version)
- Score recalculated after fix (83)
- Gates re-evaluated (all pass)
- Final approval decision (proceed)
- Workflow shows iteration loop clearly

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|---|---|---|
| 1 | Quality scoring | All dimensions scored, evidence-based, total correct |
| 2 | Tier comparison | Tier minimums checked, tier recommendation correct |
| 3 | Trending analysis | Historical avg calculated, trend detected, benchmark comparison |
| 4 | Auto-fix recommendations | Fixes ranked by impact, specific + actionable, effort/result shown |
| 5 | CI/CD gates | All 5 gates evaluated, overall decision correct (pass/fail) |
| 6 | Guardrail hits | Guardrail rule explained, why triggered, impact shown, fix recommended |
| 7 | Confidence prediction | Confidence % calculated with range, risk factors assessed |
| 8 | Tier reassignment | Mismatch detected, options presented, recommendation clear |
| 9 | Multi-skill trending | Aggregate stats calculated, patterns identified, insights actionable |
| 10 | End-to-end workflow | Cycle 1 → block → fix → Cycle 2 → pass, progression clear |

---

## Running the Evals

```bash
# Run all 10 evals
for i in {1..10}; do
  echo "Running eval $i..."
  # [invoke meta-review v2.0.0 with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke meta-review v2.0.0 with eval N test data]
# [validate against eval N pass criteria]

# Run end-to-end (Eval 10 in isolation)
# [Cycle 1: submit output, run gates, verify block]
# [User applies fix]
# [Cycle 2: resubmit, run gates, verify approval]
```

---

## Changelog

### v2.0.0 — 2026-07-21
Comprehensive eval suite for meta-review v2.0.0:
- 10 scenarios covering all new features
- Quality scoring with rubrics
- Tier-specific validation
- Trending analysis and prediction
- CI/CD gate logic
- Auto-fix recommendations
- Guardrail hit detection
- Confidence prediction
- Tier mismatch detection
- End-to-end workflow with iteration
- 100% coverage of v2.0.0 SKILL.md features
