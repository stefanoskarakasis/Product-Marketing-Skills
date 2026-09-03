---
skill: gaccs-brief
test_count: 7
version: 3.4.0
---

# GACCS-Brief — Eval Suite

Rewritten against the current skill (v3.4.0, `quality_gate: true`, 7-row
Quality Gate). The prior 3-test version predated the Quality Gate,
DRI-naming requirement, and Learning Close — none of those were covered.
This version keeps the original 3 tests' scenarios where still valid and
adds the coverage the skill's own Quality Gate table requires.

## Test 1: With Brain (Pre-filled)

**Setup:** Brain exists with ICP, Voice, Market Context
**Input:** "Create GACCS brief for Q4 product launch"
**Expected:**
- Pre-fills Audience section from brain ICP
- Uses brain voice/tone for Creative direction
- Uses brain market context for Goals
**Pass:** Brain data applied; no redundant questions asked

---

## Test 2: Without Brain (Manual, Mode Detection)

**Setup:** No brain
**Input:** "Help me write a campaign brief"
**Expected:** Mode is detected (Conversational, since no brain-dump context was pasted) BEFORE any question is asked, then asks for Goals, Audience, Creative, Channels, Stakeholders
**Pass:** Mode stated explicitly first, matching Quality Gate's "Mode detected" row; all 5 sections completed; structured brief output

---

## Test 3: Adversarial Callouts

**Input:** Vague brief: "Goals: Increase awareness. Audience: Everyone."
**Expected:**
- Challenges "increase awareness" (not measurable)
- Challenges "everyone" (too broad)
- Asks for specifics before generating
**Pass:** Weak sections flagged; specific follow-ups asked; challenges placed inline after each weak section (2-3 per section), not batched at the end

---

## Test 4: Section Scoring Threshold — Blocks Below 4 Strong

**Setup:** User provides input where only 3 of 5 GACCS sections score Strong after adversarial challenge (e.g., Goals and Audience are sharpened to Strong, but Creative, Channels, and Stakeholders remain Weak with no DRI named).

**Input:** Partial brief — specific goal and audience given, but "we'll figure out creative and channels later, whoever's free can own it."

**Expected Output — Generation Blocked:**
```
3 of 5 sections are Strong right now (Goals, Audience) — the brief
generates at 4+. Creative, Channels, and Stakeholders are still Weak.
"Whoever's free" isn't a DRI — I need one named owner before Stakeholders
can score Strong.
```

**Pass Criteria:**
- Brief is NOT generated with only 3 strong sections — the skill's own Quality Gate requires 4+ before generation
- The specific missing sections are named, not a generic "needs more detail"
- "Whoever's free" / "the team" is explicitly rejected as a DRI — matches the Quality Gate's "DRI named" row exactly

---

## Test 5: DRI Named, Not "The Team"

**Scenario:** User names a DRI vaguely ("the marketing team will own this") after being asked directly.

**Expected Output — Pushback, Not Acceptance:**
```
"The marketing team" isn't a DRI — if this brief has a problem in week 2,
who gets the Slack message? I need one name.
```

**Pass Criteria:**
- A team/department-level answer is not accepted as satisfying the Stakeholders section
- Skill asks specifically for one named individual, not a broader group
- Once a real name is given, Stakeholders section scores Strong and generation can proceed if other sections also clear the bar

---

## Test 6: Every Response Ends With a Next Step

**Scenario:** Mid-session response (not the final brief) — e.g., after Test 4's block, or after a section is sharpened but before the full brief is ready.

**Expected Output — Next Step Present Even Mid-Session:**
```
[response content]

✅ Next Step: Name a DRI for Stakeholders, then I can generate the brief.
```

**Pass Criteria:**
- The `✅ Next Step` line appears on every response, not just the final delivered brief — matches the Quality Gate's "Next Step present" row applying to "every response," not just completion
- The stated next step is specific to what's actually blocking progress, not a generic "let me know if you have questions"

---

## Test 7: Learning Close

**Scenario:** Full session completes — brief generated at 5/5 Strong sections, no adversarial pushback needed this time (unusually clean input).

**Expected Output — Session Log:**
```yaml
skill: gaccs-brief
session_date: 2026-09-01
pattern: "none"
source: n.v.t.
```

**Pass Criteria:**
- Session logged to `/context/skill-sessions.md` with exactly four fields, even when nothing notable happened — `pattern: none` is written explicitly, the row is never skipped
- No separate knowledge or decisions file written — matches this repo's single compounding mechanism used by every other skill
- Learning Close runs regardless of whether the session needed adversarial pushback — it's not conditional on friction having occurred

---

## Eval Test Coverage Matrix

| Test | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain pre-fill | ICP/Voice/Market Context applied, no redundant questions |
| 2 | Mode detection before questions | Mode stated first, matches Quality Gate row |
| 3 | Adversarial callouts | Inline, 2-3 per section, not batched |
| 4 | 4+ strong sections threshold | Generation blocked below threshold, missing sections named |
| 5 | DRI named, not "the team" | Vague ownership rejected, one name required |
| 6 | Next Step on every response | Present mid-session, not just at completion |
| 7 | Learning Close | Real four-field row, `pattern: none` written when nothing notable happened |

---

## Running Evals

```bash
# Run all evals
for i in {1..7}; do
  echo "Running test $i..."
  # [invoke gaccs-brief with test data]
  # [validate outputs against pass criteria]
done

# Run single test
# [invoke gaccs-brief with test N data]
# [validate against test N pass criteria]
```
