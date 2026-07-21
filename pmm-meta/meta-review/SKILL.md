---
name: meta-review
version: 2.0.0
description: >
  Skill quality audit engine with auto-fix mode, trending dashboard, and CI/CD integration.
  Runs after any PMM skill session to score output quality, generate fix recommendations,
  track quality trends over time, compare against tier-specific checklists, and integrate
  with CI/CD pipelines for automated quality gates. Auto-detects skill output type, applies
  quality scoring, flags issues, suggests improvements, and surfaces tier mismatches.
  Trigger on: "review this output", "quality check", "is this good enough", "audit this",
  "run review", "check quality", or any request to validate PMM skill outputs.

metadata:
  author: Stefanos Karakasis
  version_history: "1.0.0 → 2.0.0 (added auto-fix, trending, CI/CD, tier checklists)"
  context: context-agnostic
  quality_gate: true
  phase: "1C"
last_updated: 2026-07-21
---

# Meta-Review v2.0.0

The quality control layer. Every skill output gets scored, compared to tier standards,
trended over time, and validated against automated gates. This ensures consistency,
prevents low-quality launches, and helps every future session learn from quality metrics.

**New in v2.0.0:**
- Auto-fix mode (scoring + recommendation generation)
- Trending dashboard (quality metrics over 30/90 days)
- CI/CD integration (automated quality gates for launches)
- Tier-specific checklists (T1/T2/T3/T4 quality standards)
- Confidence prediction (will this output succeed?)

---

## Trigger

**Auto-Trigger Mode (Primary):**
- After any PMM skill session with output (brief, strategy, deck, etc.)
- Detects: skill name, output type, quality-relevant signals
- Does NOT trigger mid-session or before output complete

**Manual Trigger (Secondary):**
- User says: "review this", "quality check", "is this T1-ready?"
- User provides: skill output (document, brief, decision)

**No Trigger:**
- Sessions with no output (discussion only)
- Skill startup/pre-flight
- Meta-learn sessions (different tool)

---

## Inputs

**Auto-Trigger Detection:**
- Skill name (extracted from execution context)
- Output type (brief, strategy, positioning, etc.)
- Output content (document, text, decisions)
- Launch tier (if applicable: T1/T2/T3/T4)
- Timestamp (for trending)

**Manual Trigger Inputs:**
- Skill output (paste content or upload file)
- Skill name (if not obvious)
- Launch tier (if applicable)

**Context Files (Pre-Flight Load):**
- `/config/quality-scoring.yml` — point system, rubrics
- `/config/tier-checklists.yml` — tier-specific standards (T1-T4)
- `/config/ci-gates.yml` — CI/CD integration rules
- `/context/quality-trends.md` — historical quality metrics
- `/context/meta-patterns.md` — guardrails + alerts
- `/sessions/quality-log.md` — append quality scores

**NOT loaded:** `/foundation/brain.md` (context-agnostic design)

---

## Pre-Flight (Step 0)

1. **Load config files** (quality-scoring.yml, tier-checklists.yml, ci-gates.yml)
2. **Detect output type** (brief, strategy, positioning, retro, etc.)
3. **Detect launch tier** (T1/T2/T3/T4 or N/A if not applicable)
4. **Load historical trends** (context/quality-trends.md for comparison)
5. **Load tier checklist** (config/tier-checklists.yml for applicable tier)
6. **Gate pass:** If no output provided, ask user for it

---

## Steps

### Step 1: Detect Output Type & Tier (30 sec)

**What:** Identify what kind of output this is and what tier (if applicable).

**How:**
- Scan skill name + output content for type clues
- Types: GTM brief, positioning statement, battlecard, retro summary, OKR doc, etc.
- Tier: Extract from skill name or ask user if unclear (T1/T2/T3/T4 or N/A)
- If tier unclear: default to "review for all tiers" (use most demanding checklist)

**Output:**
```
Detected:
  Skill: go-to-market-strategy
  Output type: GTM brief
  Tier: T2 (from skill output metadata)
  Quality audit scope: T2 standards + cross-tier checks
```

---

### Step 2: Load Quality Rubric (1 min)

**What:** Load the scoring rubric for this output type from config/quality-scoring.yml.

**How:**
1. Match output type to scoring rubric (e.g., "GTM brief" → gtm-brief-rubric)
2. Load point system (e.g., 100-point scale)
3. Load scoring dimensions (e.g., clarity, completeness, differentiation, feasibility)
4. For each dimension: load criteria (what earns 5 pts, 10 pts, etc.)

**Output:**
```
Quality Rubric Loaded: GTM-Brief (100 points)
Dimensions:
  - Positioning clarity (20 pts max)
  - Channel strategy (20 pts max)
  - Success metrics (20 pts max)
  - Competitive context (15 pts max)
  - Timeline feasibility (15 pts max)
  - Risk mitigation (10 pts max)
```

---

### Step 3: Score Output Against Rubric (3 min)

**What:** Grade the output point-by-point against the rubric.

**How:**
1. For each dimension, read output content
2. Compare to rubric criteria: is positioning clear (5 pts) / somewhat clear (3 pts) / vague (0 pts)?
3. Assign points honestly (don't inflate)
4. Note evidence for each score (quotes or examples)
5. Track: total points, % complete, strengths, gaps

**Output format:**
```
Quality Score: GTM Brief

Dimension 1: Positioning Clarity (20 pts max)
  Score: 14/20 (70%)
  Evidence: "Positioning statement is clear vs. incumbent positioning. However, differentiation
            feels incremental — messaging could be bolder. Missing unique value angle."
  Flagged: ⚠️ MEDIUM PRIORITY (missing bold differentiation)

Dimension 2: Channel Strategy (20 pts max)
  Score: 18/20 (90%)
  Evidence: "Channel mix is realistic for T2 launch. PR + sales enablement + paid digital.
            Timeline is feasible. Only missing: regional prioritization by motion."
  Flagged: ✓ (minor gap, not critical)

[... all dimensions ...]

TOTAL: 78/100 (78%)
Grade: B- (Acceptable for T2, below T1 standards)
```

---

### Step 4: Compare to Tier Standards (2 min)

**What:** Check if output meets tier-specific quality gates.

**How:**
1. Load tier checklist from config/tier-checklists.yml (e.g., T2 standard = 75+ points)
2. Compare actual score (78) to tier minimum (75)
3. Identify gaps: does output pass T2? Would it pass T1? Would it fail T3?
4. Flag mismatches (e.g., "This is T2 output, but was scoped as T3")

**Output:**
```
Tier Comparison:

Output Score: 78/100 (78%)

T1 Standard: 90+ points required
  Status: ❌ BELOW (78 < 90)
  Gap: 12 points (missing bold positioning + regional details)

T2 Standard: 75+ points required
  Status: ✅ PASSES (78 > 75)
  Confidence: MEDIUM (only 3 points above threshold)

T3 Standard: 60+ points required
  Status: ✅ PASSES EASILY (78 > 60)

T4 Standard: 40+ points required
  Status: ✅ PASSES EASILY (78 > 40)

Recommendation: Output is T2-appropriate. Would need ~12 more points (bolder positioning)
to be T1-ready. Current tier scoping: CORRECT.
```

---

### Step 5: Generate Fix Recommendations (2 min)

**What:** For each gap identified in scoring, suggest specific improvements.

**How:**
1. For each dimension that scored <90%: generate fix
2. Fix must be: specific (not vague), actionable (user can do it), evidence-based (tied to scoring)
3. Prioritize fixes by impact: which fixes would increase score most?
4. Surface: quick wins (5 min) vs. deep work (1+ hour)

**Output:**
```
Auto-Fix Recommendations (Priority Order)

FIX 1: Strengthen Positioning Differentiation [HIGH IMPACT]
  Current: "We're like incumbent but faster and cheaper"
  Problem: Incremental, not bold. Doesn't own unique value.
  
  Suggested fix: Reframe around "[Value Angle Incumbent Doesn't Own]"
  Example: "We're the only platform that [does X the incumbent can't]"
  Estimated impact: +5 points (moves positioning clarity to 19/20)
  Effort: 30 min (requires messaging reframe)
  
FIX 2: Add Regional Prioritization to Channel Plan [MEDIUM IMPACT]
  Current: "PR + sales enablement + digital across all regions"
  Problem: Lacks geographic focus. Spreads resources thin.
  
  Suggested fix: Specify: "Primary region (60% budget) | Secondary (30%) | Awareness (10%)"
  Example: "Focus on Nordics (primary) + Germany (secondary) + EU awareness"
  Estimated impact: +2 points (moves channel strategy to 20/20)
  Effort: 15 min (add regional layers to existing plan)
  
FIX 3: Add Success Metric Success Criteria [LOW IMPACT]
  Current: "Target: 500 new leads in Q3"
  Problem: Missing: what happens if we miss? What's success range?
  
  Suggested fix: Add confidence band: "Target 500 (100%), Success range 350-600 (75-125%)"
  Estimated impact: +1 point
  Effort: 5 min (add confidence ranges)

Quick Wins Summary: 3 fixes, 50 min total effort, +8 points (78 → 86, would push to T1 territory)
```

---

### Step 6: Trend Analysis (1 min)

**What:** Compare this output's score to historical quality trends.

**How:**
1. Load context/quality-trends.md (scores from past 30/90 days)
2. Calculate: average score, trend direction (improving/stable/declining), volatility
3. Compare: is this output above/below user's average? Above/below skill baseline?
4. Surface: "Your GTM briefs are improving 2 points/month" or "This is your highest-scoring positioning yet"

**Output:**
```
Quality Trends (GTM Brief Skill, Past 90 Days)

Historical Scores:
  2026-05-21: 71/100 (First brief, learning phase)
  2026-06-04: 74/100 (+3 points, incrementally better)
  2026-06-18: 76/100 (+2 points, steady improvement)
  2026-07-01: 77/100 (+1 point, plateau)
  2026-07-21: 78/100 (today, +1 point)

Trend Analysis:
  Average (90 days): 75.2/100
  Today's score: 78/100 (+3.8 points above average)
  Trend: ↗️ IMPROVING (avg +1.5 pts/month, consistent trajectory)
  Volatility: Low (never below 71, never above 78 — steady)
  
Benchmark:
  Your avg (GTM brief): 75/100
  Skill baseline (all GTM briefs): 74/100
  Today: Above both (78 > 75 > 74)
  
Insight: "Your GTM briefs are improving consistently. This one is your best yet (+3.8
points above your average). Keep pushing on the messaging/positioning — that's your
highest-impact lever for the next 5-10 points."
```

---

### Step 7: Predict Tier Success (1 min)

**What:** Estimate confidence: will this output succeed at its intended tier?

**How:**
1. Use historical data: "GTM briefs scoring 78 have succeeded X% of the time at T2"
2. Factor in: output confidence + guardrails loaded + execution quality
3. Confidence band: Low (0-40%), Medium (40-70%), High (70-90%), Very High (90%+)
4. Flag risks: if confidence is low, what needs to improve?

**Output:**
```
Tier Success Prediction: T2 Launch

Confidence: 72% (MEDIUM-HIGH)

Reasoning:
  Output quality: 78/100 (meets T2 minimum)
  Historical data: T2 briefs scoring 75-80 succeed 70% of the time
  Guardrails loaded: Champion alignment rule active (medium-high impact)
  Execution risk: Medium (depends on sales enablement quality)

Success Probability: 72% (will hit T2 targets) ± 12%
  Low end: 60% (if sales enablement weak, champion misaligned)
  High end: 84% (if sales nails execution, champion is ally)

Risk Factors:
  🔴 Positioning still feels incremental (may not land in market)
  🟡 Regional focus missing (could spread resources thin)
  🟢 Metrics are solid (will know quickly if working)

Recommendation:
  → Proceed with T2 launch (confidence is solid)
  → Use Fix 1 (messaging) to improve confidence to 80%+
  → Monitor region performance weekly (early signal of regional gaps)
```

---

### Step 8: CI/CD Gate Decision (1 min)

**What:** Should this output pass automated quality gates (e.g., for CI/CD pipeline)?

**How:**
1. Load config/ci-gates.yml (gate rules by skill + tier)
2. Check: does output meet gate criteria?
   - Gate 1: Score ≥ tier minimum? (78 ≥ 75 for T2)
   - Gate 2: No critical gaps? (none marked 🔴 critical here)
   - Gate 3: Trend acceptable? (improving or stable, not declining)
3. If all gates pass: output clears CI/CD (can deploy)
4. If any gate fails: output blocked (needs fixes before deploy)

**Output:**
```
CI/CD Gate Evaluation (T2 GTM Brief)

Gate 1: Quality Score Threshold
  Required: ≥75 for T2
  Actual: 78
  Status: ✅ PASS

Gate 2: No Critical Gaps
  Critical issues found: 0
  Blocking issues: 0
  Status: ✅ PASS

Gate 3: Quality Trend Acceptable
  Trend: Improving (+1.5 pts/month)
  Volatility: Low (stable)
  Status: ✅ PASS (not declining)

Gate 4: Guardrail Checks
  Active guardrails: 2 (champion alignment, messaging clarity)
  Violations: 0
  Status: ✅ PASS

Overall: ✅ ALL GATES PASS

Decision: OUTPUT APPROVED FOR DEPLOYMENT (T2 GTM launch can proceed)
Next step: Deploy brief to sales team, monitor regional performance
```

---

### Step 9: Tier Enforcement (1 min)

**What:** If output doesn't match its assigned tier, flag mismatch and recommend tier change.

**How:**
1. Assigned tier (from skill/brief metadata): T2
2. Output quality suggests tier: T2 (78 points = T2 appropriate)
3. Match? YES → no flag
4. If mismatch (e.g., assigned T3, quality is T1): flag and recommend reassignment

**Output:**
```
Tier Enforcement Check

Assigned tier: T2 (from GTM strategy skill metadata)
Quality suggests: T2 (78/100 = T2-appropriate output)
Mismatch: ❌ NO (tier assignment correct)

Recommendation: Proceed with T2 launch scope.
Confidence: MEDIUM-HIGH (72%, as calculated above)
```

---

### Step 10: Surface Guardrail Hits (1 min)

**What:** Check if any loaded guardrails were triggered by this output.

**How:**
1. Load active guardrails from /context/meta-patterns.md
2. Scan output for guardrail keywords/patterns
3. If hit: surface alert + recommended action

**Output:**
```
Guardrail Hits:

🟡 MEDIUM PRIORITY: "Positioning Clarity" guardrail triggered
  Rule: "Positioning must own unique value, not just iteration on incumbent"
  Why it triggered: Output says "faster + cheaper" but doesn't own unique angle
  Impact: Reduces success confidence from 75% to 72%
  Action: Run Fix 1 (reframe positioning) to clear this guardrail

✓ PASSED: "Champion Alignment" guardrail
  Rule: "Brief must include champion alignment assumptions"
  Check: ✅ Output includes "Champion consensus: CTO + VP Sales aligned on positioning"
  Status: Clear (no action needed)
```

---

### Step 11: Close & Recommend Next Action (1 min)

**What:** Summarize everything, show what changed, suggest next step.

**How:**
1. Recap: quality score + tier match + confidence + gates + guardrails
2. Recommend: proceed, fix + retry, or escalate
3. Link to meta-learn: "Quality insight logged, meta-learn will compound this data"

**Output:**
```
✓ Quality Review Complete

Summary:
  Quality Score: 78/100 (B-, acceptable for T2)
  Tier Match: ✅ CORRECT (T2 output, assigned T2)
  CI/CD Gates: ✅ ALL PASS (deployment approved)
  Guardrails: 1 hit (messaging clarity), easy fix
  Success Confidence: 72% ± 12% (medium-high)

Recommendation:
  → PRIMARY: Deploy to sales as T2 brief (gates pass, confidence solid)
  → SECONDARY: Run Fix 1 (messaging reframe) in parallel to boost confidence to 80%+
  → MONITOR: Track regional performance weekly (early indicator of regional gaps)

Quality logged to /sessions/quality-log.md (trends updated)
Guardrail hit logged for meta-learn (compounding to "messaging clarity" pattern)

Next step: Sales enablement begins. Monitor deal velocity vs. prediction (72% success).
```

---

## Operating Rules

1. **Score honestly, not generously.** Quality control only works if scoring is rigorous. Don't inflate points.

2. **Tier standards are minimums.** T2 requires 75+, but 75 is barely passing. Aim for 80+ for confidence.

3. **Fixes are ranked by impact, not effort.** User might prefer quick wins, but surface impact-ranked first.

4. **Confidence prediction compounds over time.** Early predictions are rough; after 20+ data points, predictions get accurate.

5. **Guardrail hits are alerts, not blocks.** A hit reduces confidence but doesn't automatically kill output (unless critical).

6. **CI/CD gates are binary.** Gates pass or fail; no middle ground. If any gate fails, output is blocked from deployment.

7. **Trends matter as much as snapshots.** A 78 that's improving is better than a 78 that's declining.

8. **Tier reassignment is rare.** Only recommend if quality is 2+ tiers away (e.g., assigning T3 but output is T1-quality).

9. **Quality scores are not opinions.** They're rooted in rubric criteria. Show evidence for every point.

10. **Meta-learn gets quality data.** This review is logged. Meta-learn compounds insights (e.g., "GTM briefs improve when messaging is bold").

---

## Quality Gate

Before finalizing any review, verify:

- [ ] Output type detected correctly (brief type, skill name)
- [ ] Launch tier identified (T1/T2/T3/T4 or N/A)
- [ ] Quality rubric loaded (correct scoring dimensions)
- [ ] All dimensions scored (no dimension left blank)
- [ ] Tier standards checked (score vs. minimum)
- [ ] Fix recommendations specific and actionable
- [ ] Confidence prediction explained (with reasoning)
- [ ] CI/CD gates evaluated (all 4 gates checked)
- [ ] Guardrails scanned (no missed patterns)
- [ ] Historical trends consulted (comparison to average)
- [ ] Session logged (quality trends updated)

---

## Related Files

- `/config/quality-scoring.yml` — Point system, rubrics by output type
- `/config/tier-checklists.yml` — Tier-specific quality standards (T1-T4)
- `/config/ci-gates.yml` — CI/CD gate rules
- `/context/quality-trends.md` — Historical quality metrics
- `/context/meta-patterns.md` — Active guardrails
- `/sessions/quality-log.md` — Quality score history
