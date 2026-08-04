---
name: meta-verify
version: 2.0.0
description: Predicts success confidence for GTM outputs, scores collaboration readiness (ownership/shareability/learnings), suggests scope expansion (T2→T1), and calibrates predictions over time—enabling multiplayer adoption and self-improving GTM systems.
metadata:
  phase: 1D
  frameworks: ["Positioning rigor", "2026 GTM adoption lens", "Multiplayer Claude framework"]
  last_updated: 2026-08-04
---

# Meta-Verify

Closes the compounding loop. Predicts success confidence, scores collaboration readiness, suggests scope expansion, calibrates predictions over time.

---

## When to Use

**Trigger:** After quality review completes. Use meta-verify to:
- Predict success confidence (will this output hit targets at its tier?)
- Score collaboration readiness (is this shareable? will team adopt?)
- Suggest scope expansion (should we upgrade T2 to T1?)
- Track calibration (are our predictions improving?)

**Manual trigger:** User says "verify this", "will this succeed?", "check collaboration", "should we go T1?"

---

## Input

From quality review output:
- Skill output (brief, positioning, beachhead, pre-mortem, etc.)
- Quality score (0-100)
- Launch tier (T1/T2/T3/T4)
- Guardrails triggered (count, severity)
- Team learnings applied (yes/no)

Context files (pre-flight load):
- `/config/confidence-model.yml` — Base confidences, quality adjustments, guardrail penalties
- `/config/collaboration-signals.yml` — Ownership/shareability/learnings patterns
- `/sessions/quality-learnings.md` — Team insights
- `/sessions/collaboration-log.md` — Adoption tracking
- `/context/skill-sessions.md` — Execution history

---

## Output

**Confidence Prediction:**
```
Success confidence: 72% ± 12% (60-84% range)
Reasoning: Base T2 (70%) + Quality (78>75: +2%) - Guardrail hit (-3%) + Team strong (+3%)
Recommendation: Proceed with launch
```

**Collaboration Readiness:**
```
Collaboration score: 78% (35/45 points)
  Ownership clarity: 12/15 (owner explicit, handoff clear)
  Skill-shareability: 13/15 (modular, evals exist, interface mostly clear)
  Learnings hooks: 10/15 (meta-learn can extract patterns, partially updates quality-learnings)
Recommendation: SHAREABLE — push to GitHub with minor fixes
```

**Scope Expansion:**
```
Current: T2 at 78 quality, 72% confidence
T1 thresholds: 90 quality (gap: -12), 75% confidence (gap: -3)
Recommendation: Stay T2. Fix now, resubmit for T1 evaluation in 30 days.
```

---

## Steps (14 Total)

### STEP 0: PRE-FLIGHT (Load Context)

Load: confidence-model.yml, collaboration-signals.yml, quality-learnings.md, collaboration-log.md, confidence-log.md, skill-sessions.md

Gate check: If no output provided, ask user for quality review output.

---

### STEP 1: Load Historical Predictions (1 min)

Load `/sessions/confidence-log.md` (last 30 days). Calculate % of predictions within ±10% of actual. Check for calibration drift.

---

### STEP 2: Assess Output Quality + Context (2 min)

Load: quality score, tier, guardrails triggered, team learnings applied, team track record.

---

### STEP 3: Predict Success Confidence (3 min)

Load confidence model. Base T2 confidence: 70%. Adjustments: Quality +/-2-5%, Guardrails -3% each, Team capability ±3%. Result: 72% ± 12%.

---

### STEP 4: Suggest Scope Expansion (2 min)

Check: quality vs. T1 min (90), confidence vs. T1 min (75%), collaboration vs. T1 min (65). Decision: Upgrade to T1 / On fence / Stay current.

---

### STEP 5: Assess Collaboration Readiness (3 min)

Score three dimensions:
- **A. Ownership Clarity (0-15 pts):** Owner explicit? Handoff clear? Maintenance plan?
- **B. Skill-Shareability (0-15 pts):** Modular? Evals exist? Interface clear?
- **C. Learnings Hooks (0-15 pts):** Meta-learn hook? Will quality-learnings update? Structure consistent?

Total: 0-45 pts (0-100%).

---

### STEP 6: Assess Context-Engineering Rigor (2 min)

Check: Does skill pull from MCPs? Update /foundation/brain.md? Become guardrail material? Score: 0-15 pts.

---

### STEP 7: Assess Multiplayer Adoption Curve (2 min)

Score three adoption dimensions:
- **A. Multiplayer Reach (0-15 pts):** 8-10 people (14-15), 4-7 people (10-13), 1-3 people (5-9), just creator (0-4)
- **B. Skill Multiplier (0-15 pts):** 3+ skills (15), 1-2 skills (5-10), 0 skills (0)
- **C. Model Fit (0-15 pts):** Team GitHub + packaged + adoption pattern (15), partial (9-14), none (0-8)

Total: 0-45 pts (0-100%).

---

### STEP 8: Benchmark Comparison (1 min)

Compare quality, confidence, collaboration to T2 averages. Flag if above/below.

---

### STEP 9: Flag Calibration Drift (1 min)

Check 30-day calibration trends. Calculate over-prediction %, under-prediction %. Flag if drift > 5%.

---

### STEP 10: Surface Risk Factors + Opportunities (1 min)

Review guardrails. Identify what pushes confidence down (to 60%) and up (to 84%).

---

### STEP 11: Recommend Next Action (1 min)

If confidence > 75%: "Proceed with launch". If 60-74%: "Proceed with monitoring" or "Consider fixes". If < 60%: "Block and fix". If collaboration < 65: "Fix before sharing" or "Push as-is, flag for rework".

---

### STEP 12: Update Calibration Model (1 min)

When actual outcome known: Update confidence-log.md and collaboration-log.md. Model improves 1-2% accuracy/week.

---

### STEP 13: Feed Back to Meta-Learn (1 min)

Log prediction to confidence-log.md and collaboration-log.md. Will update when outcome known.

---

### STEP 14: Close + Link to Meta-Learn (1 min)

Summarize: confidence, collaboration, scope, adoption. Next action: launch/monitor/fix. Re-verify in 30 days.

---

## Operating Rules

1. Confidence is probabilistic, not point estimate.
2. Calibration improves with data.
3. Each guardrail ≈ 3% penalty.
4. Strong team → +3%, weak → -3%.
5. Quality below tier minimum → confidence capped.
6. Scope expansion requires quality 85+, confidence 75+, collaboration 65+.
7. Collaboration independent of confidence (high quality ≠ high adoption).
8. Ownership explicit required (no owner → collab capped at 50%).
9. Multiplayer adoption compounds (3+ skills = flywheel).
10. Context-engineering rigor feeds the brain.
11. Predictions feed meta-learn for continuous improvement.
12. Collaboration model calibrates (35+ → 80%+ adoption, <25 → <30%).

---

## Quality Gate

Before finalizing, verify all 15 checkpoints: quality loaded, tier identified, guardrails assessed, team capability considered, confidence calculated, confidence band set, scope expansion logic applied, collaboration scored, context rigor assessed, adoption curve evaluated, calibration drift checked, risk factors surfaced, collaboration history reviewed, meta-learn linkage made, next action clear.

---

## Related Files

- `/config/confidence-model.yml` — Prediction model with tier baselines
- `/config/collaboration-signals.yml` — Ownership/shareability/learnings rubrics
- `/context/quality-trends.md` — Quality baseline by tier
- `/context/skill-sessions.md` — Execution log
- `/sessions/quality-learnings.md` — Team insights
- `/sessions/confidence-log.md` — Predictions + actual outcomes
- `/sessions/collaboration-log.md` — Adoption tracking
