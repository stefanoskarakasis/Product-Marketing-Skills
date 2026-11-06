# meta-synthesis.eval.md

Eval test cases for `meta-synthesis` skill.

---

## Test 1: Cross-Skill Pattern Reaches High Confidence

**Input:**

- `/context/skill-sessions.md` has 4 rows: 2 from `retro`, 2 from
  `pre-mortem`, all describing the same underlying pattern in different
  words ("champion alignment gap flagged late").

**Expected Behavior:**

1. Step 1 groups these 4 rows as one cross-skill pattern (spans 2 skills)
2. Step 2 classifies it High confidence (4 occurrences, ≥3 threshold)
3. Step 3 surfaces it in the proposal message with the exact guardrail text
   that would be written, and asks for approval
4. On approval, Step 4 appends the guardrail to `/context/meta-patterns.md`
   with pattern text, occurrence count, and date
5. Session log entry is appended to `/context/skill-sessions.md` for this
   meta-synthesis run itself

**Success Criteria:**

- Cross-skill patterns are correctly prioritized over same-skill-only ones
- Nothing is written to `/context/meta-patterns.md` before the approval
  gate is shown and confirmed
- The written guardrail text matches exactly what was shown for approval

**Test Pass:** One guardrail correctly proposed, gated, and written with
matching text

---

## Test 2: Single Occurrence Produces No Proposal (Edge Case)

**Input:**

- `/context/skill-sessions.md` has 1 row from `positioning-messaging`
  describing a pattern that hasn't appeared anywhere else in the log.

**Expected Behavior:**

1. Step 2 classifies this as Low confidence (1 occurrence)
2. Per the ranking table, Low confidence patterns are noted only — not
   proposed as a guardrail or brain update
3. Step 3's proposal message does not include this pattern as something to
   approve or reject
4. The session close still mentions it as "worth watching" per Step 4's
   closing summary

**Success Criteria:**

- No guardrail is proposed or written for a single occurrence
- The observation isn't silently dropped — it's still surfaced as a
  low-confidence note in the close

**Test Pass:** No premature guardrail from insufficient evidence, but the
single occurrence isn't lost either

---

## Test 3: Durable Signal Routed to Brain, Not Guardrail

**Input:**

- 3 sessions across different skills all surface the same finding: a
  specific buying trigger keeps appearing in customer conversations that
  isn't yet reflected in the brain's ICP section.

**Expected Behavior:**

1. Step 2 recognizes this as a durable business fact, not a process gap
2. Proposes it as a brain update to Section 2 (ICP), not a guardrail —
   naming the exact section per Step 2's rule
3. Step 3's proposal message shows this as a brain update line item,
   distinct from the guardrail line items
4. On approval, Step 4 writes to `/foundation/brain.md` Section 2 with an
   exact before/after shown, using the same confirmation standard as any
   other skill that writes to the brain

**Success Criteria:**

- The pattern is correctly routed to a brain update rather than a
  guardrail
- The named section (2, ICP) is accurate to where the content actually
  belongs
- Before/after is shown, not just a description of the change

**Test Pass:** Correct routing to brain vs. guardrail, with an explicit
before/after shown before the write

---

## Test 4: Empty Session Log Blocks Cleanly

**Input:**

- `/context/skill-sessions.md` doesn't exist yet, or exists with zero rows.

**Expected Behavior:**

1. Step 0 detects this at pre-flight
2. Skill stops immediately and tells the user there's nothing to
   synthesize yet — does not proceed to Step 1
3. No guardrail or brain-update proposal is generated from nothing

**Success Criteria:**

- Clean, explicit stop rather than a confusing "no patterns found" after
  pretending to scan
- No file is written

**Test Pass:** Skill blocks at pre-flight with a clear, honest message

---

## Test 5: Rejected Pattern Is Logged, Not Silently Dropped

**Input:**

- A Medium confidence pattern is proposed; user responds "reject" for
  that specific item during the Step 3 approval gate.

**Expected Behavior:**

1. That pattern is not written to `/context/meta-patterns.md`
2. The rejection and its reason (if given) are logged so the same pattern
   isn't re-proposed next run without new occurrences
3. Other approved items in the same batch are still written normally

**Success Criteria:**

- A rejected item doesn't block approved items in the same run
- A rejected item doesn't silently reappear next run with no new evidence

**Test Pass:** Partial approval handled correctly; rejection is durable

---

## Test: Reads a domain ledger, not only the session log

**Input:** `/context/learning-sources.md` lists `/context/battlecards/_outcomes.md` and `/context/prospects/_outcomes.md`. Three different accounts lost to the same competitor after the same block was used. `skill-sessions.md` has no row about it.

**Expected output includes:**
- The pattern found from the ledgers, with n=3 distinct accounts and the ledger names
- A proposal labelled seller-reported, with the exact guardrail text
- No hit rate (fewer than 10 outcomes)

**Pass condition:** Evidence from a ledger alone can produce a proposal, and nothing is written without approval.

---

## Test: Weekly mode, unattended

**Input:** A scheduled run in weekly mode.

**Expected output includes:**
- An adoption table of sessions per skill for the last 7 days, with quiet skills listed
- A promotion queue saved to `/context/promotion-queue.md`
- No guardrail and no brain edit written
- On the next interactive run, an opening line that a queue is waiting

**Pass condition:** The unattended run proposes and saves, and never writes.

---

## Test: Brain edit below the threshold

**Input:** A durable signal seen at 2 accounts.

**Expected output includes:**
- A note, not a brain-edit proposal
- A statement that 3 distinct accounts are needed

**Pass condition:** The brain-edit threshold is 3, and 2 stays a note.
