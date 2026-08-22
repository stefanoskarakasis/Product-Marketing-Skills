# meta-learn.eval.md

Eval test cases for `meta-learn` skill.

---

## Test 1: Real Pattern Captured and Logged

**Input:**

- Session just closed: `pre-mortem` produced a risk assessment for a T2
  launch.
- User answers: Surprised — "it flagged the champion risk before I even
  mentioned sales was worried." Wrong — "nothing." Missing — "nothing."

**Expected Behavior:**

1. All three questions asked in one message
2. The "surprised" answer is restated as a falsifiable claim: "pre-mortem
   identified champion-risk as a factor without the user first surfacing
   sales concern about it"
3. Log entry shown for confirmation before writing:
   `skill: pre-mortem, session_date: [date], pattern: [claim], source: surprised`
4. User confirms; entry appended to `/context/skill-sessions.md`

**Success Criteria:**

- Pattern statement is specific enough to be checked later, not vague
- Nothing is written before the Step 4 confirmation is shown and approved
- Log entry lands in the correct file with correct YAML shape

**Test Pass:** One falsifiable pattern logged, with explicit confirmation
before the write

---

## Test 2: Clean Close — Nothing to Extract (Edge Case)

**Input:**

- Session closed: `retro` produced a standard post-launch summary.
- User answers all three questions with "nothing" / "nothing" / "nothing."

**Expected Behavior:**

1. All three questions still asked — never skipped even if the answer is
   predictable
2. Skill does not manufacture a pattern to appear productive
3. Skips directly to Step 5 — logs a clean-close entry
   (`pattern: none, source: n.v.t.`) without a confirmation gate, since
   there's nothing to approve
4. Session is still logged — a clean session is a real, useful data point
   for `meta-synthesis` later (it's part of the denominator)

**Success Criteria:**

- No fabricated pattern appears in the log
- The session is still recorded, not silently dropped
- No confirmation prompt is shown for an entry with nothing to confirm

**Test Pass:** Clean close logged accurately, no invented insight

---

## Test 3: Vague Answer Can't Be Sharpened

**Input:**

- Session closed: `positioning-messaging` produced a BUILD-mode output.
- User answers "wrong": "the tone just felt off, hard to say exactly why."

**Expected Behavior:**

1. Skill attempts to sharpen the answer into a falsifiable statement (Step 3)
2. Recognizes it can't be sharpened without forcing false precision
3. Logs it as a loose observation rather than inventing a specific claim
   the user didn't actually make: `pattern: "tone felt off (unspecified) —
   insufficient detail to state as a testable claim"`
4. Does not silently drop the observation, but also does not fabricate
   specificity that isn't there

**Success Criteria:**

- The logged entry honestly reflects the vagueness rather than inventing
  precision
- The user isn't asked to keep refining indefinitely — one attempt to
  sharpen, then log honestly either way

**Test Pass:** Honest logging of a genuinely vague signal, no false
precision invented

---

## Test 4: Skill Name Not Obvious

**Input:**

- User says "log this session" with no skill name and no immediate prior
  context in the conversation.

**Expected Behavior:**

1. Skill asks which skill session this is closing out, rather than guessing
2. Does not proceed to the three extraction questions until the skill name
   is confirmed

**Success Criteria:**

- No log entry is created with a guessed or blank skill name
- User is asked a direct, specific question

**Test Pass:** Skill blocks on missing skill name instead of guessing
