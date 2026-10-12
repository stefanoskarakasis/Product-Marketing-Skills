---
name: competitive-battlecard.eval
version: 1.0.0
description: >
  Eval suite for competitive-battlecard. Tests: a full-brain card, Quick-Brain with no brain, ask-once intake with delivery always asked, an unsourced buyer claim, an unapproved our-side claim kept off the card, prohibited and forbidden-claim checks, a competitor missing from Section 3, confirmation-gated and append-only Section 3 write-back, refresh against a previous card, stale and past-dated claims, the one-page gate, truthful delivery, a CI-platform card that disagrees with a public page, and Learning Close against the five-field shape. 14 test cases.
---

# Competitive-Battlecard: Eval Suite

## Setup (Universal)

Each test case:
1. Populates `/foundation/brain.md` with Sections 1, 2, 3, 6 and 8, or withholds it where noted
2. Starts with no `/context/battlecards/` folder unless noted
3. Runs competitive-battlecard on the given input
4. Validates the card, the saved record, the gate output, any proposed brain note and the session log

Fixtures use a fictional company ("Ledgerlane", from `examples/example-brain.md`) and fictional competitors. Replace with real material when available.

---

## Test Case 1: Full-brain card, tailored

**Input:**
"Battlecard for Northgate AP. I am an AE, they are the incumbent, I am talking to the CFO, evaluation stage, mid-market logistics, UK." Brain has Sections 1, 2, 3 (with an Alternatives Map block for Northgate AP) and 6.

**Expected output includes:**
- Header naming role, motion, the competitor's status, persona, stage, segment and region
- All blocks in the fixed order, within the caps
- 💎 items taken only from Section 6 approved entries
- A 🧭 Next move for the evaluation stage, and a 🎤 line written for a CFO
- A saved record in `/context/battlecards/northgate-ap-YYYY-MM-DD.md`

**Expected output excludes:**
- A question already answered in the request
- Any claim about Ledgerlane that is not in Section 1 permitted claims or Section 6

**Pass condition:** A one-page card whose emphasis follows the stated persona, stage and status, with the record saved.

---

## Test Case 2: No brain, Quick-Brain

**Input:** "Battlecard for Northgate AP." No `/foundation/brain.md`.

**Expected output includes:**
- One message with the five Quick-Brain questions and the deal-context options
- The card labelled "Built from Quick-Brain answers"
- Unsourced items tagged `[Rep-stated]`
- No brain file created

**Expected output excludes:**
- A redirect to `product-marketing-context` as the only response
- Any write to `/foundation/brain.md`

**Pass condition:** A usable card is delivered from the session answers and the brain is untouched.

---

## Test Case 3: Ask once, delivery always asked (edge: user skips)

**Input:** "Battlecard for Northgate AP, just give it to me."

**Expected output includes:**
- No more than one question round
- The delivery format asked (Google Doc or HTML), Google Doc used if unanswered
- A neutral card (account executive, general buyer, evaluation) with the assumptions stated in one line on the card
- An offer to tailor

**Expected output excludes:**
- A second round of intake questions
- Assumptions stated as facts

**Pass condition:** The card ships with its assumptions listed and a tailoring offer.

---

## Test Case 4: Unsourced buyer claim

**Input:** "The buyer says Northgate is 30% cheaper. What do I say?"

**Expected output includes:**
- The claim as the first 🔄 entry, answered with a question
- The claim marked `[A]` (unverified claim)
- No restatement of "30% cheaper" as a fact in the snapshot

**Pass condition:** An unsourced buyer claim is answered with a question and never repeated as fact.

---

## Test Case 5: Our-side claim without approval stays off the card

**Input:** The rep pastes "we cut invoice errors by 80% at a customer" with no source. Brain Section 6 has no such entry.

**Expected output includes:**
- The claim absent from 💎
- The claim listed under Open items as `[NEEDS PROOF]`
- A hand-off line naming `proof-points`

**Expected output excludes:**
- The 80% figure anywhere on the card
- A write to Section 6

**Pass condition:** Only registered, approved claims reach 💎, and the rest is routed to `proof-points`.

---

## Test Case 6: Forbidden claim and prohibited item (edge: conflicting constraints)

**Input:** Brain Section 6 forbidden claims: "Any named competitor comparison without legal review." Section 8 prohibited: "Do not mention Harbor Ledger in any material." The rep asks for a card on Northgate AP, then on Harbor Ledger.

**Expected output includes:**
- On Northgate AP: the card, with Check before use stating that legal review is required before customer-facing use, and the footer
- On Harbor Ledger: no card; the Section 8 entry shown and the user asked how to proceed

**Expected output excludes:**
- A card that works around the prohibited entry
- Any suggestion to share the Northgate AP card with a customer

**Pass condition:** Constraints are checked before writing, and a prohibited competitor stops the build.

---

## Test Case 7: Competitor missing from Section 3

**Input:** "Battlecard for Fieldstone Pay." Brain Section 3 does not name it.

**Expected output includes:**
- A one-time, non-blocking note that it is not in the alternatives map, naming `alternatives-map` as a separate plugin
- A card built from the gathered evidence
- A proposed one-line stub for Section 3, shown as exact text and not yet written

**Expected output excludes:**
- A write before the user confirms
- A full alternatives-map entry invented by this skill

**Pass condition:** The card ships, the stub is proposed only, and nothing is written without a yes.

---

## Test Case 8: Write-back never overwrites a confirmed value (edge: conflict)

**Input:** Section 3 `why_leaving` is confirmed as "the ERP module cannot route exceptions". Three closed-lost deals from `~~CRM` (n=3, 90 days) say Northgate AP won on price. The user says yes to the proposed note.

**Expected output includes:**
- Both the confirmed value and the new field evidence shown, with the conflict named
- The note appended under Section 3 as a Battlecard Field Notes block with source tags and n
- Existing Section 3 text unchanged

**Expected output excludes:**
- Any edit to the confirmed `why_leaving` text
- A write to Sections 1, 2, 4, 5, 6, 7 or 8

**Pass condition:** The write is append-only, tagged, confirmed, and limited to Section 3.

---

## Test Case 9: Refresh against a previous card

**Input:** "Refresh the Northgate AP card." `/context/battlecards/northgate-ap-2026-08-14.md` exists. Two recent `signal-monitor` lists name Northgate AP.

**Expected output includes:**
- A "Changed since 2026-08-14" line with at most three differences
- The recent signals reflected with their original confidence label
- A new file with today's date; the earlier file untouched

**Pass condition:** The new card shows what changed and no earlier record is overwritten.

---

## Test Case 10: Stale and past-dated claims

**Input:** A pasted competitor pricing note dated 2026-05-02, and a roadmap line "Northgate AP will ship exception routing in Q3 2026". Today is 2026-10-12.

**Expected output includes:**
- The pricing claim tagged with its date and "re-check"
- The roadmap item treated as unconfirmed and named in Check before use
- No line on the card promising the feature

**Pass condition:** A claim older than about 90 days is marked for re-check and a past-dated roadmap item is never stated as fact.

---

## Test Case 11: Quality gate, one page

**Input:** A request that produces a first draft of about 700 words with six ❓ questions and five 🔄 entries.

**Expected output includes:**
- The draft cut to 450 words or fewer, 4 ❓ and 4 🔄 at most
- The weakest rows removed, not every line shortened
- A gate line showing the score and no failed rows after the fix

**Pass condition:** The delivered card passes the One page check without shrinking type below 9 pt.

---

## Test Case 12: Truthful delivery (edge: Word requested, no Doc connector)

**Input:** "Word please." The environment has no .docx builder and no Google Drive connector.

**Expected output includes:**
- A plain statement that Word is not built here
- An offer of the two supported formats: Google Doc (paste-ready in chat) and HTML
- The record still saved to `/context/battlecards/`

**Expected output excludes:**
- Any claim that a .docx or a Google Doc was created or saved to Drive
- Any claim of a verified page count that was not checked

**Pass condition:** The skill never claims a file, Doc or page count it did not produce.

---

## Test Case 13: Learning Close

**Input:** Any completed session.

**Expected output includes:** One block appended to `/context/skill-sessions.md` with exactly these fields: `type: execution`, `skill: competitive-battlecard`, `session_date`, `pattern`, `source`.

**Expected output excludes:** Any additional field, and any request for permission before writing the row.

**Pass condition:** The entry matches the five-field shape in `SKILL-SPEC.md` Section 5.1.

---

## Test Case 14: CI-platform card disagrees with a public page (edge: connector read-only)

**Input:** A card pulled from a connected `~~competitive intelligence` tool says the competitor's entry price is $20 per seat (dated 4 months ago). The competitor's pricing page, read today, says $29.

**Expected output includes:**
- The platform card read first and tagged `[Internal <Mon YYYY>]` with its own date
- The disagreement shown as a question or a "re-check" note on the Price and terms row, with both values and both dates
- The platform value not silently replaced by the public one (or the reverse)
- No write of any kind back to the CI platform

**Expected output excludes:**
- A single price stated as fact
- Any claim that the CI platform was updated

**Pass condition:** Both values and dates are visible, the conflict is a question, and nothing is written to the external tool.
