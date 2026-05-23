---
skill: positioning-messaging
test_count: 5
version: 1.0.0
---

# Positioning-Messaging Evals

## Test 1: With Brain (Pre-filled Discovery)

**Setup:** Brain exists with complete Sections 1, 2, 3, 5
**Input:** "Generate positioning in BUILD mode"
**Expected:** 
- Skips discovery questions (data loaded from brain)
- Generates full 4-layer messaging doc
- Positioning statement uses brain ICP + alternatives
**Pass criteria:** No discovery questions asked; output references brain data

---

## Test 2: Without Brain (Manual Discovery)

**Setup:** No brain exists
**Input:** "Generate positioning"
**Expected:** 
- Asks discovery questions (Product, Buyer, Alternatives, Outcome)
- Runs full Dunford sequence
- Generates positioning based on manual input
**Pass criteria:** All 4 hard-floor questions asked; positioning generated

---

## Test 3: Save to Brain

**Setup:** Brain exists
**Input:** "Generate positioning" → complete discovery → "yes, save to brain"
**Expected:** 
- Output saved to brain Section 7
- Field `last_positioning_output` contains full positioning
- Field `last_positioning_date` = timestamp
**Pass criteria:** Check brain Section 7 updated with positioning

---

## Test 4: Self-Verification Gate

**Input:** Positioning with weak differentiators (2/4 on stress-test)
**Expected:** 
- Self-verification fails
- Returns to Phase 5
- Removes weak differentiators
- Re-runs verification
**Pass criteria:** Only 4/4 differentiators appear in final output

---

## Test 5: Multiple Modes

**Input:** "Generate positioning in HOMEPAGE mode"
**Expected:** 
- Runs Phases 1-5
- Packages as HOMEPAGE mode output
- Delivers hero headline <8 words, subhead <20 words, 3 pillars
- No placeholders
**Pass criteria:** Output is production-ready homepage copy, not messaging doc
