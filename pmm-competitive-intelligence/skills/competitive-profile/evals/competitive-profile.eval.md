---
name: competitive-profile.eval
version: 1.0.0
description: >
  Eval suite for competitive-profile. Tests: setup from a full brain, the five-competitor cap, Quick-Brain with no brain, no invented roster, delta-only refresh, unchanged pages keeping their dates, unsourced weaknesses as questions, mechanism-not-adjective and roadmap-versus-shipped checks, append-only confirmed brain write-back, conflicts with confirmed values, a single honest schedule proposal, an unattended scheduled run, v2 intake with n of 2, v2 roster upkeep, and Learning Close against the five-field shape. 16 test cases.
---

# Competitive-Profile: Eval Suite

## Setup (Universal)

Each test case:
1. Populates `/foundation/brain.md` with Sections 1, 2, 3, 6, 7 and 8, or withholds it where noted
2. Starts with no `/context/competitor-profiles/` folder unless noted
3. Runs competitive-profile on the given input
4. Validates the profile files, the status board, any proposed brain note, the schedule proposal and the session log

Fixtures use a fictional company ("Ledgerlane", from `examples/example-brain.md`) and fictional competitors. Replace with real material when available.

---

## Test Case 1: Setup with full brain, roster of five

**Input:** "Set up my competitive profiles." Brain has Sections 1, 2, 3 (six named competitors plus status quo and DIY), 6, 7 and 8.

**Expected output includes:**
- The market line (category, market type, segment) read from the brain
- A roster of five or fewer taken from Section 3 `alternatives`, ranked by Section 7 priority when no CRM is connected
- Status quo and DIY left in Section 3, not profiled
- One profile file per rostered competitor in `/context/competitor-profiles/<slug>-YYYY-MM-DD.md`
- A schedule proposal at the end

**Expected output excludes:**
- A seventh or sixth profile
- Any competitor not named in Section 3 or by the user this run

**Pass condition:** Five or fewer dated, tagged profiles from named competitors, with the schedule proposed.

---

## Test Case 2: Roster cap: user asks for twelve (edge)

**Input:** "Track all twelve competitors."

**Expected output includes:**
- The cap of five stated once with the reason
- A question: which competitors stay, and which one leaves if a sixth is wanted
- The other seven left in Section 3 unchanged

**Expected output excludes:**
- Twelve profiles
- Any deletion of competitors from Section 3

**Pass condition:** The roster stays at five and nothing is removed from the brain.

---

## Test Case 3: No brain, Quick-Brain

**Input:** "Who are my key competitors?" No `/foundation/brain.md`.

**Expected output includes:**
- One message with the five Quick-Brain questions
- Profiles labelled "Built from Quick-Brain answers"
- Unsourced items tagged `[A]`
- No brain file created

**Expected output excludes:**
- A redirect to `product-marketing-context` as the only response
- Any write to `/foundation/brain.md`

**Pass condition:** A usable roster and profiles from session answers, with the brain untouched.

---

## Test Case 4: Brain has no named competitors (no invented roster)

**Input:** "Set up my competitive profiles." Section 3 holds only status quo and DIY.

**Expected output includes:**
- A statement that no direct competitor is named
- A hand-off to `alternatives-map`
- No profile built

**Expected output excludes:**
- Competitor names from model memory
- A roster the user did not give

**Pass condition:** The skill stops and routes to `alternatives-map` rather than guessing.

---

## Test Case 5: Delta refresh, only stale lines re-read

**Input:** "Refresh the Northgate AP profile." The newest record is 70 days old: pricing line dated 70 days ago, positioning 70 days, market and buyer 70 days.

**Expected output includes:**
- Pricing re-read (past 60 days)
- Positioning, product and market lines carried forward with original dates (inside 90 and 180)
- A new dated file with a `previous:` link
- The Carried forward section listing the unchanged lines

**Expected output excludes:**
- Every line re-researched
- Original dates moved forward for unchanged lines

**Pass condition:** Only the pricing line is refreshed, and the unchanged lines keep their dates.

---

## Test Case 6: Re-reading an unchanged page is not a new fact

**Input:** Refresh run; the competitor's pricing page reads exactly as recorded.

**Expected output includes:**
- The line kept with its original date and a note "re-read, unchanged" in Sources
- The row still marked `re-check` if past its window until a source changes it

**Expected output excludes:**
- The "as of" date moved to today as if the fact were new

**Pass condition:** The date records when the fact was established, not when the page was last opened.

---

## Test Case 7: Unsourced weakness becomes a question

**Input:** The user says "Northgate has terrible support." No source.

**Expected output includes:**
- The line placed under Open questions for the field, tagged `[A]`
- Nothing under Where they lose

**Expected output excludes:**
- "Terrible support" stated as a fact
- An invented review or quote

**Pass condition:** An unsourced weakness is a question, never a statement.

---

## Test Case 8: Our side: adjective fails, mechanism passes

**Input:** Setup. Section 3 `unique_capabilities`: "intuitive approvals" and "approvals route by contract value".

**Expected output includes:**
- "Intuitive" flagged and a named mechanism asked for
- The mechanism line accepted
- A hollow-test question for each kept differentiator
- Items without Section 6 proof marked `[NEEDS PROOF]` and handed to `proof-points`

**Expected output excludes:**
- An adjective written into a profile as a capability
- A write to Section 6

**Pass condition:** Only mechanisms enter the "our side" and unproven ones route to `proof-points`.

---

## Test Case 9: Roadmap is not a capability

**Input:** The user says "we also have auto-matching, shipping next quarter." Not in Section 1.

**Expected output includes:**
- The item listed under Roadmap
- Not listed as a shipped capability anywhere in the profile

**Expected output excludes:**
- Roadmap shown in a comparison as a capability

**Pass condition:** Roadmap and shipped stay apart.

---

## Test Case 10: Brain write-back is append-only and confirmed

**Input:** Review after a setup run. Section 3 has an existing `why_leaving` value and an Alternatives Map block.

**Expected output includes:**
- The exact Roster and Profile Notes text shown, five lines or fewer, each tagged
- The question "Add this to Section 3? Existing content stays unchanged."
- On yes, an appended block only

**Expected output excludes:**
- Any edit of existing Section 3 text
- A write to Sections 1, 2, 4, 5, 6, 7 or 8
- A write without the exact text shown first

**Pass condition:** The brain gains one appended block after confirmation and nothing else changes.

---

## Test Case 11: Conflict with a confirmed brain value

**Input:** Brain Section 3 (confirmed) says the competitor sells only to enterprise. A pricing page read today shows a self-serve tier.

**Expected output includes:**
- Both values and both dates shown
- The conflict phrased as a question
- The confirmed value unchanged

**Expected output excludes:**
- The brain value overwritten
- One of the two stated as the answer

**Pass condition:** A confirmed value is never overwritten by newer, lower-ranked evidence; the conflict is a question.

---

## Test Case 12: Schedule proposed once, with a paste-ready prompt

**Input:** Any completed interactive run. No scheduling tool available in the session.

**Expected output includes:**
- A short block saying what the schedule does
- The weekly refresh prompt from `references/profile-format.md` naming the brain folder and every source
- A statement that the scheduled run saves records and never changes the brain
- The schedule not proposed a second time after the user declines

**Expected output excludes:**
- A claim that a task was created when none was
- A scheduled prompt that allows brain writes

**Pass condition:** The schedule is offered once, honestly, with a prompt that cannot change the brain.

---

## Test Case 13: Unattended scheduled run

**Input:** A scheduled `refresh` and `status` run starts in a fresh session with the prompt from `references/profile-format.md`. One named connector is unavailable.

**Expected output includes:**
- Profiles and a status board saved
- The missing source recorded as a gap on the board
- Any brain proposal left in the saved record under "Waiting for you"
- Learning Close row with `source: N/A`

**Expected output excludes:**
- Any question to the user
- Any brain write
- A gap question

**Pass condition:** The run completes read-only for the brain and leaves its decisions waiting for the user.

---

## Test Case 14: v2 intake: n of 2 before 'where they win'; deal data and signals

**Input:** "Fold this week's signals into the profiles." `/context/signals/` holds three items (two about the same competitor, one about a company not on the roster). `~~CRM` shows one loss to Northgate citing price and a second citing implementation time.

**Expected output includes:**
- The off-roster signal dropped and counted
- Each rostered item turned into at most one proposed change with its source
- The single price loss kept as a note
- A "where they win" proposal only for a reason that appears twice within 180 days

**Expected output excludes:**
- A pattern claimed from one data point
- Names, emails or phone numbers of individuals

**Pass condition:** One data point stays a note; a pattern needs n of 2 or more.

---

## Test Case 15: v2 roster check proposes, never forces

**Input:** "Review my roster against last quarter's deals." `~~CRM` shows a competitor not on the roster in four deals and a rostered one absent for two checks in a row.

**Expected output includes:**
- A proposed promotion and a proposed demotion with the cost of each
- The roster unchanged until the user confirms
- `[A]` marking if no CRM was connected

**Expected output excludes:**
- An automatic swap
- A roster larger than five

**Pass condition:** The roster check suggests swaps with their cost and changes nothing unasked.

---

## Test Case 16: Learning Close

**Input:** Any completed session.

**Expected output includes:**
- One block appended to `/context/skill-sessions.md` with exactly `type: execution`, `skill: competitive-profile`, `session_date`, `pattern`, `source`

**Expected output excludes:**
- Any additional field
- A request for permission before writing the row
- A change to a refresh window

**Pass condition:** The entry matches the five-field shape in `SKILL-SPEC.md`.
