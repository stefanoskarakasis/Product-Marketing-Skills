---
skill: pmm-resume
test_count: 3
version: 1.0.0
---

# PMM-Resume Evals

## Test 1: Full Tailor

**Setup:** User provides baseline resume + job description
**Input:** "Tailor my resume for this Senior PMM role at Stripe"
**Expected:** 
- Classifies company type (Payments/Fintech)
- Scores all bullets
- Rebuilds resume with top-ranked bullets
- Generates "Why Stripe" block
**Pass:** Complete tailored resume + bullet ranking table

---

## Test 2: Company Classification

**Input:** JD from AI-native startup
**Expected:** Correctly identifies company type as "AI-Native"
**Pass:** Classification shown; resume adapts accordingly

---

## Test 3: Bullet Scoring Transparency

**Input:** Baseline resume with 20 bullets
**Expected:** Scores each bullet (category fit + keywords + cultural)
**Pass:** Ranking table shows all scores; top bullets selected
