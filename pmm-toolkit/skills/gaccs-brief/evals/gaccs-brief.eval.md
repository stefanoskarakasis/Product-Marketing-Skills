---
skill: gaccs-brief
test_count: 3
version: 1.0.0
---

# GACCS-Brief Evals

## Test 1: With Brain (Pre-filled)

**Setup:** Brain exists with ICP, Voice, Market Context
**Input:** "Create GACCS brief for Q4 product launch"
**Expected:** 
- Pre-fills Audience section from brain ICP
- Uses brain voice/tone for Creative direction
- Uses brain market context for Goals
**Pass:** Brain data applied; no redundant questions asked

---

## Test 2: Without Brain (Manual)

**Setup:** No brain
**Input:** "Help me write a campaign brief"
**Expected:** Asks for Goals, Audience, Creative, Channels, Stakeholders
**Pass:** All 5 sections completed; structured brief output

---

## Test 3: Adversarial Callouts

**Input:** Vague brief: "Goals: Increase awareness. Audience: Everyone."
**Expected:** 
- Challenges "increase awareness" (not measurable)
- Challenges "everyone" (too broad)
- Asks for specifics before generating
**Pass:** Weak sections flagged; specific follow-ups asked
