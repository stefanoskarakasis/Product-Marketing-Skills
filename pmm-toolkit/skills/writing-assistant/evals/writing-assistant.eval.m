---
skill: writing-assistant
test_count: 3
version: 1.0.0
---

# Writing-Assistant Evals

## Test 1: With Brain (Voice Match)

**Setup:** Brain exists with voice="authoritative, data-driven, concise"
**Input:** "Rewrite this: We help companies grow faster with our amazing platform"
**Expected:** Rewritten copy matches "authoritative, data-driven, concise" attributes
**Pass:** Voice attributes applied; jargon removed; data-driven framing used

---

## Test 2: Without Brain (Manual Voice)

**Setup:** No brain
**Input:** "Rewrite this email to be more concise"
**Expected:** Asks for voice preferences (or proceeds with neutral voice)
**Pass:** Copy rewritten 30% shorter; clear improvements shown

---

## Test 3: Explain Changes

**Input:** "Review this copy: [long wordy text]"
**Expected:** Provides rewrite + explains what was removed/reordered/clarified
**Pass:** Before/after comparison shown; changes explained
