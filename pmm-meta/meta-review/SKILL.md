---
name: meta-review
version: 2.0.0
description: >
  Skill quality audit engine with auto-fix mode, trending dashboard, and CI/CD integration.
  Scores PMM skill outputs (GTM briefs, positioning, beachhead, etc.) against quality rubrics
  informed by Pawel Huryn's positioning rigor (unique value clarity) and 2026 GTM best practices
  (adoption curves, cross-functional alignment, enablement timing). Auto-detects output type,
  applies tier-specific quality gates, generates fix recommendations, tracks quality trends,
  and logs persistent learnings for team-wide calibration. Trigger on: "review this output",
  "quality check", "is this good enough", "audit this", or any request to validate PMM outputs.

metadata:
  author: Stefanos Karakasis
  version_history: "1.0.0 → 2.0.0 (added auto-fix, trending, CI/CD, tier checklists, Pawel positioning rigor, 2026 GTM learnings)"
  inspired_by: "Pawel Huryn (positioning clarity), Ramp GTM playbook (adoption curves, enablement timing), 2026 GTM trends (cross-functional alignment)"
  context: context-agnostic
  quality_gate: true
  phase: "1C"
  persistent_memory: true
  learning_log_path: "/sessions/quality-learnings.md"
last_updated: 2026-07-21
---

# Meta-Review v2.0.0

The quality control layer. Every skill output gets scored against clarity + feasibility standards,
compared to tier benchmarks, trended over time, and validated against automated gates. Unique to v2.0.0:
Pawel Huryn's **positioning rigor** (unique value clarity test) + 2026 **GTM adoption learnings**
(cross-functional handoffs, enablement timing, propensity-based segmentation).

**New in v2.0.0:**
- Auto-fix mode (scoring + recommendation generation)
- Trending dashboard (quality metrics over 30/90 days)
- CI/CD integration (automated quality gates for launches)
- Tier-specific checklists (T1/T2/T3/T4 quality standards)
- **Pawel positioning rigor** (unique value clarity test on every positioning output)
- **2026 GTM adoption lens** (adoption curve assessment, enablement timing validation, cross-functional handoff clarity)
- **Persistent learning logging** (team-wide quality insights compound across all users)

---

## Trigger

**Auto-Trigger Mode (Primary):**
- After any PMM skill session with output (brief, strategy, deck, etc.)
- Detects: skill name, output type, quality-relevant signals
- Does NOT trigger mid-session or before output complete

**Manual Trigger (Secondary):**
- User says: "review this", "quality check", "is this T1-ready?"
- User provides: skill output (document, brief, decision)

---

## Inputs

**Auto-Trigger Detection:**
- Skill name (extracted from execution context)
- Output type (brief, strategy, positioning, etc.)
- Output content (document, text, decisions)
- Launch tier (if applicable: T1/T2/T3/T4)
- Timestamp (for trending)

**Context Files (Pre-Flight Load):**
- `/config/quality-scoring.yml` — point system, rubrics (with Pawel positioning rigor)
- `/config/tier-checklists.yml` — tier-specific standards (T1-T4)
- `/config/ci-gates.yml` — CI/CD integration rules
- `/config/adoption-lens.yml` — 2026 GTM adoption curve framework
- `/context/quality-trends.md` — historical quality metrics
- `/context/meta-patterns.md` — guardrails + alerts
- `/sessions/quality-learnings.md` — persistent team-wide quality insights (NEW)

---

## Pre-Flight (Step 0)

1. **Load config files** (quality-scoring.yml, tier-checklists.yml, ci-gates.yml, adoption-lens.yml)
2. **Detect output type** (brief, strategy, positioning, retro, etc.)
3. **Detect launch tier** (T1/T2/T3/T4 or N/A if not applicable)
4. **Load historical trends** (context/quality-trends.md for comparison)
5. **Load tier checklist** (config/tier-checklists.yml for applicable tier)
6. **Load team learnings** (sessions/quality-learnings.md — what has the team learned about quality in this skill?)
7. **Gate pass:** If no output provided, ask user for it

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

### Step 2: Load Quality Rubric + Team Learnings (1 min)

**What:** Load the scoring rubric for this output type + prior team learnings on this skill.

**How:**
1. Match output type to scoring rubric (e.g., "GTM brief" → gtm-brief-rubric)
2. Load point system (e.g., 100-point scale)
3. Load scoring dimensions (informed by Pawel rigor + 2026 GTM lens)
4. **NEW:** Load team learnings for this skill from quality-learnings.md
   - What has worked well? (e.g., "GTM briefs score higher when regional prioritization included")
   - What gaps keep appearing? (e.g., "Positioning outputs miss unique value angle")
   - What should I watch for? (guardrails from prior reviews)

**Output:**
```
Quality Rubric Loaded: GTM-Brief (100 points)
Dimensions:
  - Positioning clarity & unique value (Pawel rigor) (20 pts max)
  - Adoption curve & enablement timing (2026 lens) (20 pts max)
  - Cross-functional alignment (2026 lens) (20 pts max)
  - Success metrics (20 pts max)
  - Risk mitigation (10 pts max)
  - Timeline feasibility (10 pts max)

Team Learnings (GTM Brief Skill, Past 90 days):
  ✅ Strength: Regional prioritization in channel plan → +2 pts avg
  ⚠️ Gap: Enablement timeline often vague (when do reps get trained?) → -1.5 pts avg
  ⚠️ Gap: Sales handoff unclear (who owns ramp? CS or sales?) → missing from 40% of briefs
```

---

### Step 3: Score Output Against Rubric (3 min)

**What:** Grade the output point-by-point against the rubric.

**How:**
1. For each dimension, read output content
2. Compare to rubric criteria: is positioning clear (5 pts) / somewhat clear (3 pts) / vague (0 pts)?
3. **NEW Pawel test (positioning outputs only):** Does positioning own a unique value angle the incumbent can't claim?
   - YES (clear, bold, defensible): 20/20 pts
   - SOMEWHAT (clear but iterative): 15/20 pts
   - NO (features + incumbent framing): 5/20 pts
4. **NEW adoption lens (GTM/launch outputs):** Is enablement timing explicit and realistic?
   - YES (reps trained by launch day, timeline mapped): +2 pts bonus
   - VAGUE (training mentioned but no dates): -1 pt penalty
5. Assign points honestly (don't inflate)
6. Note evidence for each score (quotes or examples)
7. Track: total points, % complete, strengths, gaps

**Output format:**
```
Quality Score: GTM Brief

Dimension 1: Positioning Clarity & Unique Value (Pawel Rigor) (20 pts max)
  Score: 14/20 (70%)
  Evidence: "Positioning statement is clear vs. competitor X. However, feels iterative
            (faster + cheaper). Missing unique value angle only we can own."
  Pawel test: ❌ FAIL (doesn't own unique angle, incumbent could claim same positioning)
  Flagged: 🔴 CRITICAL (unique value test failed)

Dimension 2: Adoption Curve & Enablement Timing (2026 Lens) (20 pts max)
  Score: 16/20 (80%)
  Evidence: "Brief includes 'sales enablement' but no timeline. When do reps get trained?
            By launch day or weeks after? Unclear. CS handoff timing missing."
  2026 lens: ⚠️ VAGUE (enablement timing not explicit, -1 pt penalty applied)
  Flagged: 🟡 MEDIUM (enablement timing needs specificity)

Dimension 3: Cross-Functional Alignment (2026 Lens) (20 pts max)
  Score: 18/20 (90%)
  Evidence: "Brief clearly states: Sales owns ramp-up for first 30 days, CS takes over
            at 35 days. Marketing supports launch week. Clean handoff."
  2026 lens: ✅ PASS (cross-functional owners and handoff dates clear)

[... all dimensions ...]

TOTAL: 78/100 (78%)
Grade: B- (Acceptable for T2, below T1 standards)

Team Learnings Applied:
  ✅ Regional prioritization: Present (+2 pts noted)
  ⚠️ Enablement timing: Vague (-1 pt deducted per team learning)
  ✅ Sales/CS handoff: Clear (no deduction)
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
  Gap: 12 points (missing unique value angle, vague enablement timing)

T2 Standard: 75+ points required
  Status: ✅ PASSES (78 > 75)
  Confidence: MEDIUM (only 3 points above threshold)

Recommendation: Output is T2-appropriate. Would need ~12 more points (unique value
positioning + explicit enablement timeline) to be T1-ready.
```

---

### Step 5: Generate Fix Recommendations (2 min)

**What:** For each gap identified in scoring, suggest specific improvements.

**How:**
1. For each dimension that scored <90%: generate fix
2. Fix must be: specific (not vague), actionable (user can do it), evidence-based (tied to scoring)
3. Prioritize fixes by impact + team learning insights
4. Surface: quick wins (5 min) vs. deep work (1+ hour)

**Output:**
```
Auto-Fix Recommendations (Priority Order, with Team Learning Insights)

FIX 1: Own Unique Value Angle (Pawel Rigor) [CRITICAL]
  Current: "Faster and cheaper than incumbent"
  Problem: Incremental. Incumbent could claim same thing. Fails Pawel unique value test.
  Team insight: "50% of positioning outputs miss unique angle. Those that own one score +5 pts avg."
  
  Suggested fix: Identify one value dimension incumbent doesn't own (e.g., vertical focus,
               business model, implementation approach) and reframe:
               "Only platform purpose-built for [vertical], enabling [outcome] in [timeframe]"
  Estimated impact: +6 points (positioning → 20/20)
  Effort: 30 min
  
FIX 2: Make Enablement Timing Explicit (2026 Lens) [HIGH IMPACT]
  Current: "Sales enablement TBD"
  Problem: Vague. When do reps train? Before or after launch? Unclear.
  Team insight: "Enablement timing specificity matters. Briefs with explicit training
                dates on launch timeline score +1.5 pts avg."
  
  Suggested fix: Add: "Sales training: [date], delivered via [format]. CS begins
                handoff: [date]. Post-launch monitoring window: [days]"
  Estimated impact: +2 points
  Effort: 15 min

Quick Wins Summary: 2 fixes, 45 min total effort, +8 points (78 → 86, enters T1 range)
```

---

### Step 6: Adoption Curve Assessment (1 min)

**What:** For GTM/launch outputs: assess if adoption curve is realistic and enablement timing is right.

**How:**
1. Load adoption-lens.yml (2026 framework: sales ramp curve, CS handoff window, expansion trigger)
2. Check: Does brief account for sales ramp-up time (typically 30-60 days)?
3. Check: Does brief specify CS handoff (when does customer success take primary ownership)?
4. Check: Are expansion triggers defined (when do we try to upsell)?
5. Flag: If enablement happens post-launch (risky), if handoff is undefined, if expansion triggers missing

**Output:**
```
Adoption Curve Assessment (2026 GTM Lens)

Sales Ramp-Up:
  Brief states: "Sales ramp 30 days"
  Assessment: ✅ REALISTIC (30 days is standard for T2)
  Note: Brief includes training timeline + success criteria for ramp completion

CS Handoff:
  Brief states: "CS takes primary ownership at day 35"
  Assessment: ✅ CLEAR (handoff date is explicit)
  Note: Sales/CS handoff is clean, no overlap or gap

Expansion Triggers:
  Brief states: "Expansion upsell kicks in at 60 days (post-stability window)"
  Assessment: ✅ DEFINED (expansion is intentional, not reactive)

Overall: ✅ ADOPTION CURVE IS REALISTIC (brief accounts for standard sales ramp + handoff)
```

---

### Step 7: Trend Analysis (1 min)

**What:** Compare this output's score to historical quality trends.

**How:**
1. Load context/quality-trends.md (scores from past 30/90 days)
2. Calculate: average score, trend direction (improving/stable/declining), volatility
3. Load team learnings: what does the team know about this skill's quality trajectory?
4. Surface: "Your GTM briefs are improving 2 points/month" or "This is your highest-scoring positioning yet"

**Output:**
```
Quality Trends (GTM Brief Skill, Past 90 Days)

Historical Scores:
  2026-05-21: 71/100 (First brief, learning phase)
  2026-06-04: 74/100 (+3 points)
  2026-06-18: 76/100 (+2 points)
  2026-07-01: 77/100 (+1 point)
  2026-07-21: 78/100 (today, +1 point)

Trend Analysis:
  Average (90 days): 75.2/100
  Today's score: 78/100 (+3.8 points above average)
  Trend: ↗️ IMPROVING (avg +1.5 pts/month)
  
Team Learning: "GTM briefs improve fastest when team focuses on (1) unique positioning,
               (2) explicit enablement timing. Those two levers account for +4 pts avg improvement."

Insight: "Your GTM briefs are improving steadily. This one is your best yet. Keep pushing
         on unique value angle — that's your highest-impact lever for next 5-10 points."
```

---

### Step 8: Predict Tier Success (1 min)

**What:** Estimate confidence: will this output succeed at its intended tier?

**How:**
1. Use historical data: "GTM briefs scoring 78 have succeeded X% of the time at T2"
2. Factor in: output confidence + guardrails loaded + execution quality + team calibration
3. Confidence band: Low (0-40%), Medium (40-70%), High (70-90%), Very High (90%+)
4. Flag risks: if confidence is low, what needs to improve?

**Output:**
```
Tier Success Prediction: T2 Launch

Confidence: 72% (MEDIUM-HIGH)

Reasoning:
  Output quality: 78/100 (meets T2 minimum)
  Historical data: T2 briefs scoring 75-80 succeed 70% of the time
  Team calibration: Team has improved by +3.8 pts on average (confidence improving)
  Guardrails loaded: Positioning clarity rule active (medium-high impact)
  Execution risk: Medium (enablement timing vague, could slip)

Success Probability: 72% (will hit T2 targets) ± 12%
  Low end: 60% (if enablement delayed, unique positioning doesn't land)
  High end: 84% (if enablement sharp, positioning resonates)

Risk Factors:
  🔴 Positioning still incremental (may not land in market)
  🟡 Enablement timing vague (could slip post-launch)
  🟢 CS/sales handoff is clear (will know quickly if working)

Recommendation:
  → Proceed with T2 launch (confidence is solid)
  → Use Fix 1 & 2 to improve confidence to 80%+
  → Monitor enablement ramp (early signal of success/failure)
```

---

### Step 9: CI/CD Gate Decision (1 min)

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
  Critical issues found: 1 (positioning unique value test failed)
  Blocking issues: 0 (critical is flagged but not blocking, fixable)
  Status: ⚠️ CONDITIONAL (Fix 1 required, then resubmit)

Gate 3: Quality Trend Acceptable
  Trend: Improving (+1.5 pts/month)
  Volatility: Low (stable)
  Status: ✅ PASS

Gate 4: Guardrail Checks
  Active guardrails: 2 (unique value clarity, enablement timing)
  Violations: 1 (unique value clarity hit)
  Status: ⚠️ CONDITIONAL (same as Gate 2)

Overall: ⚠️ CONDITIONAL APPROVAL

Decision: OUTPUT NEEDS FIX #1 BEFORE DEPLOYMENT
  Critical gap: Positioning doesn't own unique value angle (Pawel test failed)
  Fix: Reframe positioning to own unique dimension (est. 30 min)
  Next: Resubmit for re-scoring, should clear gates with +6 point boost

Or: Skip fix, deploy as-is (if timeline pressure warrants risk)
```

---

### Step 10: Log Learnings for Team (1 min)

**What:** Record quality insights from this review that help future team members improve.

**How:**
1. Append to `/sessions/quality-learnings.md` (persistent team knowledge)
2. Format: skill, output type, what worked, what didn't, guardrail hit (if any)
3. These learnings feed back into Step 2 for future reviews (team knowledge compounds)

**Output (logged to quality-learnings.md):**
```markdown
## 2026-07-21 | GTM Brief Quality Review

Skill: go-to-market-strategy
Output Type: GTM brief
Tier: T2
Quality Score: 78/100
Outcome: CONDITIONAL (needs unique value positioning fix)

What Worked Well:
  ✅ Sales/CS handoff was crystal clear (date + handoff owner specified)
  ✅ Regional prioritization included (leveraging team learning from prior reviews)
  ✅ Cross-functional alignment clear (no ambiguity on who owns what)

What Didn't Work:
  ❌ Positioning felt incremental (incumbent could claim same "faster + cheaper")
  ⚠️ Enablement timeline vague (when exactly do reps train? No date)

Guardrail Hit:
  🔴 CRITICAL: Positioning unique value test (Pawel rigor) FAILED
     Rule: Positioning must own unique value angle incumbent doesn't
     Why: "Faster + cheaper" is not unique to us
     Fix: Identify one value dimension we own (vertical focus, implementation model, etc.)
          and reframe around that unique angle

Leverage for Next Team Member:
  → When reviewing GTM briefs, run the Pawel unique value test EARLY
  → If test fails, it's a show-stopper (Pawel rigor score can drop 6+ points)
  → Explicit enablement dates matter (affects adoption curve assessment)
  → Regional prioritization + clear sales/CS handoff are key strengths to build on

Confidence if Fixed: 80%+ (would move into T1 territory)
```

---

### Step 11: Close & Recommend Next Action (1 min)

**What:** Summarize everything, show what changed, suggest next step.

**How:**
1. Recap: quality score + tier match + confidence + gates + learnings logged
2. Recommend: proceed, fix + retry, or escalate
3. Link to meta-learn: "Quality insight logged, meta-learn will compound this data"
4. Link to team: "This learning is in quality-learnings.md for your team"

**Output:**
```
✓ Quality Review Complete

Summary:
  Quality Score: 78/100 (B-, acceptable for T2)
  Tier Match: ✅ CORRECT (T2 output, assigned T2)
  Pawel Positioning Test: ❌ FAILED (incremental, doesn't own unique angle)
  Adoption Curve: ✅ REALISTIC (sales/CS handoff clear, enablement timing vague)
  CI/CD Gates: ⚠️ CONDITIONAL (Fix #1 required, then resubmit)
  Success Confidence: 72% ± 12% (medium-high, improvable to 80%+)

Recommendation:
  → PRIMARY: Run Fix 1 (own unique positioning angle) in parallel to launch prep
  → SECONDARY: Run Fix 2 (explicit enablement dates) to sharpen execution
  → MONITOR: Track sales ramp curve vs. 30-day plan (early signal of success)
  → TEAM: This review's learnings logged to quality-learnings.md (helps team improve)

Quality logged to /sessions/quality-log.md (trends updated)
Team insights logged to /sessions/quality-learnings.md (team knowledge compounds)
Guardrail hit logged for meta-learn (unique value positioning pattern tracked)

Next step: Fix and resubmit, or proceed as-is with risk noted.
```

---

## Operating Rules

1. **Pawel rigor is non-negotiable for positioning.** Unique value clarity test is a gate, not optional.

2. **2026 adoption lens is required for launches.** Sales ramp + CS handoff + expansion triggers must be explicit.

3. **Team learnings compound.** Every review adds insights that make next reviews sharper. Use them.

4. **Score honestly, not generously.** Quality control only works if scoring is rigorous.

5. **Tier standards are minimums.** 75 is barely passing. Aim for 80+.

6. **Fixes are ranked by impact.** Prioritize unique value clarity + enablement timing (highest-impact levers).

7. **Enablement timing specificity matters.** Vague enablement timelines correlate with launch delays.

8. **Cross-functional handoffs prevent chaos.** If sales/CS handoff is undefined, output fails adoption curve test.

9. **Trends matter as much as snapshots.** A 78 that's improving beats a 78 that's declining.

10. **Learning is persistent.** Team knowledge is logged. Use it to help each other improve.

---

## Quality Gate

Before finalizing any review, verify:

- [ ] Output type detected correctly
- [ ] Launch tier identified
- [ ] Quality rubric loaded (with Pawel rigor + adoption lens)
- [ ] All dimensions scored with evidence
- [ ] Pawel unique value test run (positioning outputs only)
- [ ] Adoption curve assessed (launch/GTM outputs only)
- [ ] Tier standards checked
- [ ] Fix recommendations specific + ranked by impact
- [ ] Team learnings applied (prior insights referenced)
- [ ] Confidence prediction explained
- [ ] CI/CD gates evaluated
- [ ] Learnings logged to quality-learnings.md
- [ ] Session logged to quality-log.md

---

## Related Files

- `/config/quality-scoring.yml` — Point system, rubrics (with Pawel positioning rigor, 2026 adoption lens)
- `/config/tier-checklists.yml` — Tier-specific quality standards (T1-T4)
- `/config/ci-gates.yml` — CI/CD gate rules
- `/config/adoption-lens.yml` — 2026 GTM adoption curve framework (NEW)
- `/context/quality-trends.md` — Historical quality metrics
- `/context/meta-patterns.md` — Active guardrails
- `/sessions/quality-log.md` — Quality score history
- `/sessions/quality-learnings.md` — Persistent team-wide quality insights (NEW, compounds across all users)

---

## Sources

The enhanced meta-review v2.0.0 integrates learnings from:

- [Pawel Huryn - The Product Compass](https://www.productcompass.pm/) — Positioning rigor framework (unique value clarity test)
- [Pawel Huryn - AI PM Learning Program](https://www.productcompass.pm/p/ai-pm-learning-program) — Decision-making quality standards
- 2026 GTM trends: Cross-functional alignment, adoption curve timing, enablement specificity
- Ramp GTM learnings: Sales ramp curves, CS handoff windows, expansion trigger design
