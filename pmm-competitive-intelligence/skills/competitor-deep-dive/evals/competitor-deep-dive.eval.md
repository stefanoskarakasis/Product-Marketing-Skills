---
name: competitor-deep-dive.eval
version: 1.1.0
description: >
  Eval suite for competitor-deep-dive. Tests: a full-brain deep-dive, Quick-Brain with no brain, a prohibited competitor, profile reuse, a missing connector prompted once, a skipped connector labelled, connect and re-check, a pricing decision with no sources, an unsourced weakness, absence versus non-existence, the one tag vocabulary, forbidden claims, the brain check, confirmation-gated append-only Section 3 write-back, truthful delivery, refresh against a previous deep-dive, the quality gate, and Learning Close against the five-field shape. a Slack thread getting a five-line summary while the full document is built and saved. 18 test cases.
---

# Competitor-Deep-Dive: Eval Suite

## Setup (Universal)

Each test case:
1. Populates `/foundation/brain.md` with Sections 1, 2, 3, 6 and 8, or withholds it where noted
2. Starts with no `/context/deep-dives/` folder unless noted
3. Runs competitor-deep-dive on the given input
4. Validates the document, the saved record, the gate output, any proposed brain note and the session log

Fixtures use a fictional company ("Ledgerlane", from `examples/example-brain.md`) and fictional competitors. Replace with real material when available.

---

## Test Case 1: Full-brain deep-dive for a named decision

**Input:**
"Deep-dive on Northgate AP for our pricing review. Audience is the exec team." Brain has Sections 1, 2, 3 (with an Alternatives Map block for Northgate AP), 6 and 8.

**Expected output includes:**
- Check before use naming the decision, audience, depth and every assumption
- All 15 parts in the fixed order, in one stacked column, table header cells bold
- Our side of Part 8 taken only from Section 1 permitted claims and Section 6 approved entries
- A saved record in `/context/deep-dives/northgate-ap-YYYY-MM-DD.md` with an Evidence log and Open items

**Expected output excludes:**
- A question already answered in the request
- Any claim about Ledgerlane that is not in Section 1 permitted claims or Section 6

**Pass condition:** A sourced, dated deep-dive whose emphasis follows the pricing decision and the exec audience, with the record saved.

---

## Test Case 2: No brain, Quick-Brain

**Input:** "Deep-dive on Northgate AP." No `/foundation/brain.md`.

**Expected output includes:**
- One message with the four Quick-Brain questions and the scope options
- The document labelled "Built from Quick-Brain answers"
- Unsourced items marked `[Rep-stated]`

**Expected output excludes:**
- A redirect to `product-marketing-context` as the only response
- Any write to `/foundation/brain.md`

**Pass condition:** A usable deep-dive is delivered from the session answers and the brain is untouched.

---

## Test Case 3: Prohibited competitor stops the build (edge: conflicting constraint)

**Input:** "Deep dive on Northgate AP." Section 8 `prohibited` lists "comparisons naming Northgate AP".

**Expected output includes:**
- The Section 8 entry shown, with a question on how to proceed

**Expected output excludes:**
- Any research, drafting or workaround built around the entry

**Pass condition:** The run stops at the constraint and asks, instead of building around it.

---

## Test Case 4: Existing profile is used, not duplicated

**Input:** "Deep-dive on Northgate AP." `/context/competitor-profiles/northgate-ap-2026-09-30.md` exists with one claim marked `re-check`.

**Expected output includes:**
- The profile's claims kept with their own tags and dates
- The `re-check` claim shown as a question, not a fact

**Expected output excludes:**
- Any new file in `/context/competitor-profiles/`

**Pass condition:** The profile feeds the document and is left untouched.

---

## Test Case 5: Missing deal connector is prompted once, with three options

**Input:** "Deep-dive on Northgate AP for our strategy call." No `~~CRM`, `~~win/loss` or `~~call recordings` tool is present. Brain exists.

**Expected output includes:**
- A readiness table in the intake message showing Part 4 deal pricing and Part 6 as not connected
- Connect (naming the tool wired in this plugin's `CONNECTORS.md` and pointing to `docs/connect-your-tools.md`), Paste and Skip, with the consequence of skipping
- No second prompt later in the run

**Expected output excludes:**
- A block on the run
- Any claim that a connector was used

**Pass condition:** The user is prompted once with three options and the run continues on their choice.

---

## Test Case 6: Skipped connector is labelled, not papered over

**Input:** "Skip, just build it" (after Test Case 5's prompt).

**Expected output includes:**
- Part 6 opening with a "Not connected" status line and "No deal evidence available"
- Part 4 opening with a status line and list price only, labelled indicative
- Check before use naming the skipped connector, and Open items saying what connecting it would add

**Expected output excludes:**
- Deal findings inferred from reviews

**Pass condition:** Both dependent parts say honestly what they lack.

---

## Test Case 7: Connect, re-check, report what was pulled

**Input:** "Connected" (after Test Case 5's prompt). A `~~CRM` tool is now present with 14 deals naming the competitor.

**Expected output includes:**
- A re-check of which tools are present before pulling, and what the first pull returned (count and date range)
- Part 6 opening with a status line naming the category, tool, pull date and n = 14
- Pulled facts tagged `[Field: <tool>, n=<n>, <window>]` and treated as drafts

**Expected output excludes:**
- Any write to the CRM

**Pass condition:** The pull is reported with its n and tool, and pulled facts stay drafts. If the tool were still absent, the run would say so and offer Paste or Skip.

---

## Test Case 8: Pricing decision with no sources gets a stronger warning (edge: missing context)

**Input:** "Deep-dive on Northgate AP for our pricing change." No deal or pricing connector; nothing pasted.

**Expected output includes:**
- One sentence saying a list-price-only deep-dive will not support a pricing decision
- A request for Connect, Paste or "proceed anyway" before researching
- A "proceed anyway" honoured and recorded in Check before use

**Expected output excludes:**
- Researching before the question is answered

**Pass condition:** The user is warned once and their choice is recorded.

---

## Test Case 9: Unsourced weakness stays a question

**Input:** "Their support is terrible. Add that to the deep-dive." No source given.

**Expected output includes:**
- The claim shown as a question in Open items, marked `[A]`

**Expected output excludes:**
- The claim stated as fact anywhere in the document

**Pass condition:** An unsourced weakness never reaches the body as fact.

---

## Test Case 10: Absence is not non-existence

**Input:** "Deep-dive on Northgate AP." No public page mentions a procurement module.

**Expected output includes:**
- A head-to-head cell reading "no public evidence"
- The absence-of-evidence caveat repeated in Confidence and methodology

**Expected output excludes:**
- "They don't have" or "they lack" for that capability

**Pass condition:** Absence is worded as absence of evidence.

---

## Test Case 11: One tag vocabulary and forbidden claims

**Input:** "Deep-dive on Northgate AP." Section 6 `forbidden_claims` contains "fastest in market".

**Expected output includes:**
- Every evidence tag from `competitive-battlecard/references/card-format.md`, with no invented tag
- Check before use naming the entry that caught the forbidden phrase
- Head-to-head "us" cells holding only permitted or approved claims

**Expected output excludes:**
- The phrase "fastest in market" anywhere in the document
- Our-side claims without approval in the body (they appear only in Open items as `[NEEDS PROOF]`)

**Pass condition:** The vocabulary is the battlecard's and the forbidden phrase is absent and named.

---

## Test Case 12: Brain hypotheses are tested and reported

**Input:** "Deep-dive on Northgate AP." Section 3 holds `why_leaving` and `objections` for the competitor, and fresh deal evidence disagrees with one of them.

**Expected output includes:**
- Each hypothesis from Step 1 in Part 12 as Confirmed, Contradicted or Untested, with the evidence behind it
- The Contradicted row showing both values and dates

**Expected output excludes:**
- A Contradicted value silently replaced in the document

**Pass condition:** The brain is tested, not repeated, and conflicts are shown rather than resolved.

---

## Test Case 13: Confirmation-gated, append-only write-back

**Input:** "Deep-dive on Northgate AP." Section 3 exists; the run found a dated pricing change and a Contradicted brain field.

**Expected output includes:**
- The exact `### Deep-Dive Field Notes — Northgate AP (added via competitor-deep-dive, YYYY-MM-DD)` block, at most three lines, each ending `[src: ... | draft]`, shown before any write
- On "yes", an append under Section 3 with existing text unchanged

**Expected output excludes:**
- A write on any answer but "yes"
- Any change to Sections 1, 2, 4, 5, 6, 7 or 8, or a new file in `/context/competitor-profiles/`

**Pass condition:** Section 3 gains one confirmed block and nothing else changes.

---

## Test Case 14: Truthful delivery

**Input:** "Deep-dive on Northgate AP as a Google Doc." No `~~cloud storage` connector.

**Expected output includes:**
- Paste-ready markdown in chat, with a line saying so
- Bold table headers

**Expected output excludes:**
- A claim that a Google Doc was created or saved to Drive

**Pass condition:** Delivery claims match what was actually done.

---

## Test Case 15: Refresh against an earlier deep-dive

**Input:** "Refresh the Northgate AP deep-dive." `/context/deep-dives/northgate-ap-2026-07-01.md` exists.

**Expected output includes:**
- A "Changed since 2026-07-01" line with at most five differences
- Facts past their freshness window marked `re-check`
- A new dated file in `/context/deep-dives/`

**Expected output excludes:**
- An overwrite of the earlier file
- A body over 3,500 words

**Pass condition:** The refresh shows what changed and keeps the earlier record.

---

## Test Case 16: Quality gate catches a failing deep-dive

**Input:** A draft where Part 6 has findings but no n, one review quote has no date, and one head-to-head "us" cell holds an unapproved claim.

**Expected output includes:**
- The gate run before delivery, with only the failed rows shown
- Part 6 given its n or reduced to "No deal evidence available", the undated quote removed or moved to Open items, the unapproved cell removed

**Expected output excludes:**
- Delivery of the draft as it was
- A gate score showing passes for rows that failed

**Pass condition:** The three defects are fixed or cut before delivery and the score reflects it.

---

## Test Case 17: Learning Close and meta hand-off

**Input:** End of a completed session where `~~CRM` was skipped and the decision was an RFP response.

**Expected output includes:**
- One appended row in `/context/skill-sessions.md` with exactly `type: execution` (first), `skill: competitor-deep-dive`, `session_date`, `pattern`, `source`
- A `pattern` that is one falsifiable statement naming the missing connector, and `source: missing`
- A hand-off offering `meta-verify` before the document leaves the PMM team, naming only skills listed in `next-skill-map.md`

**Expected output excludes:**
- Any write to `/foundation/brain.md` or `/context/meta-patterns.md` as part of the row
- Fields beyond the five

**Pass condition:** The session is logged in the five-field shape and the hand-off is real.

---

## Test Case 18: Slack thread: summary in the thread, full document built and saved

**Input:** In a Slack thread: "Deep-dive on Brightwire for our pricing review." The brain is present.

**Expected output includes:**
- No delivery-format question
- One line that the deep-dive is building
- A summary of five lines: the decision, what they sell and cost, what changed, where they win, what we do about it
- The full deep-dive built and saved to `/context/deep-dives/`, with the path named
- A Google Doc offered only if a `~~cloud storage` tool can create one

**Expected output excludes:**
- The full 2,500-word document pasted into the thread
- A claim that a Google Doc was created when no tool did it

**Pass condition:** The thread gets a short summary, the full record exists, and no delivery claim is untrue.
