# Run sheet: competitive-battlecard 1.4.0

Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.

## Test Case 1: Full-brain card, tailored

**Input:**
"Battlecard for Northgate AP. I am an AE, they are the incumbent, I am talking to the CFO, evaluation stage, mid-market logistics, UK." Brain has Sections 1, 2, 3 (with an Alternatives Map block for Northgate AP) and 6.

**Pass condition:** A one-page card whose emphasis follows the stated persona, stage and status, with the record saved.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 2: No brain, Quick-Brain

**Input:** "Battlecard for Northgate AP." No `/foundation/brain.md`.

**Pass condition:** A usable card is delivered from the session answers and the brain is untouched.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 6: Forbidden claim and prohibited item (edge: conflicting constraints)

**Input:** Brain Section 6 forbidden claims: "Any named competitor comparison without legal review." Section 8 prohibited: "Do not mention Harbor Ledger in any material." The rep asks for a card on Northgate AP, then on Harbor Ledger.

**Pass condition:** Constraints are checked before writing, and a prohibited competitor stops the build.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 8: Write-back never overwrites a confirmed value (edge: conflict)

**Input:** Section 3 `why_leaving` is confirmed as "the ERP module cannot route exceptions". Three closed-lost deals from `~~CRM` (n=3, 90 days) say Northgate AP won on price. The user says yes to the proposed note.

**Pass condition:** The write is append-only, tagged, confirmed, and limited to Section 3.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 10: Stale and past-dated claims

**Input:** A pasted competitor pricing note dated 2026-05-02, and a roadmap line "Northgate AP will ship exception routing in Q3 2026". Today is 2026-10-12.

**Pass condition:** A claim older than about 90 days is marked for re-check and a past-dated roadmap item is never stated as fact.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 20: Pack: an index, nothing rebuilt

**Input:** "Set of cards for my roster." The roster has five competitors: three with current cards (one built for an AE talking to a CFO), one card past its `Re-check by`, one with no card.

**Pass condition:** All five competitors are listed, no card was built or changed, and the Learning Close row is written.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---


# Run sheet: competitive-profile 1.4.0

Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.

## Test Case 1: Setup with full brain, roster of five

**Input:** "Set up my competitive profiles." Brain has Sections 1, 2, 3 (six named competitors plus status quo and DIY), 6, 7 and 8.

**Pass condition:** Five or fewer dated, tagged profiles from named competitors, with the schedule proposed.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 2: Roster cap: user asks for twelve (edge)

**Input:** "Track all twelve competitors."

**Pass condition:** The roster stays at five and nothing is removed from the brain.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 9: Roadmap is not a capability

**Input:** The user says "we also have auto-matching, shipping next quarter." Not in Section 1.

**Pass condition:** Roadmap and shipped stay apart.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 13: Unattended scheduled run

**Input:** A scheduled `refresh` and `status` run starts in a fresh session with the prompt from `references/profile-format.md`. One named connector is unavailable.

**Pass condition:** The run completes read-only for the brain and leaves its decisions waiting for the user.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 17: ask: pricing line inside its window (Slack)

**Input:** In a Slack thread: "What does Brightwire charge for the entry plan?" The newest Brightwire profile has a pricing line read 20 days ago (window 60).

**Pass condition:** The answer comes from the profile, is dated, thread-sized, and nothing past rung 1 was used.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---


# Run sheet: competitor-deep-dive 1.3.0

Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.

## Test Case 1: Full-brain deep-dive for a named decision

**Input:**
"Deep-dive on Northgate AP for our pricing review. Audience is the exec team." Brain has Sections 1, 2, 3 (with an Alternatives Map block for Northgate AP), 6 and 8.

**Pass condition:** A sourced, dated deep-dive whose emphasis follows the pricing decision and the exec audience, with the record saved.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 2: No brain, Quick-Brain

**Input:** "Deep-dive on Northgate AP." No `/foundation/brain.md`.

**Pass condition:** A usable deep-dive is delivered from the session answers and the brain is untouched.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 3: Prohibited competitor stops the build (edge: conflicting constraint)

**Input:** "Deep dive on Northgate AP." Section 8 `prohibited` lists "comparisons naming Northgate AP".

**Pass condition:** The run stops at the constraint and asks, instead of building around it.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 5: Missing deal connector is prompted once, with three options

**Input:** "Deep-dive on Northgate AP for our strategy call." No `~~CRM`, `~~win/loss` or `~~call recordings` tool is present. Brain exists.

**Pass condition:** The user is prompted once with three options and the run continues on their choice.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 6: Skipped connector is labelled, not papered over

**Input:** "Skip, just build it" (after Test Case 5's prompt).

**Pass condition:** Both dependent parts say honestly what they lack.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---


# Run sheet: industry-newsletter 1.1.0

Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.

## Test Case 1: Full weekly issue in the locked order (Google Doc)

**Input:**
"Write this week's industry newsletter for AP automation in EMEA." Platform saved as Google Doc. Sources for the period are retrieved: Northgate AP launched a usage-based tier (pricing page, changelog), a regulator published a draft e-invoicing rule, Paystream posted a SOC 2 report.

**Pass condition:** A verdict-first issue in the exact section order, every row linked and scored, saved with its evidence log and no brain write.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 4: Evidence floor stops the build

**Input:**
"Send the newsletter." No brain, no roster, no category, nothing retrieved or pasted.

**Pass condition:** No issue without a category, a competitor and a source.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 5: Quiet week still carries the required blocks

**Input:**
Nothing crossed the bar this week: no dated competitor move, no regulatory item, no watchlist trigger.

**Pass condition:** A quiet week is a short issue, not a skipped one.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Test Case 29: Internal inputs are leads, never the claim

**Input:**
Gong shows 6 calls naming Northgate AP's price; Slack has a rep post that Brightfold cut prices; a Klue card says "no change" for Brightfold. Only the Northgate AP page is public and confirms the move.

**Pass condition:** Only a public page makes a claim.

---

**Result:** Pass / Partial / Fail
**What failed or changed:**

---


# Run sheet: product-marketing-context 3.6.0

Fresh Claude Code session per case. Set up the fixture the eval's Setup describes, paste the input, compare with the pass condition, then fill the result.

## Eval 9 — A confirmed value is never overwritten by newer evidence

**Setup:** The brain has `persona: Controller` confirmed by the user last month. New call notes say the buyer is "the VP of Finance."

**Prompt:** "Update my brain from these notes."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 10 — Refresh lists only stale fields and asks one at a time

**Setup:** A brain with Section 5 dated 120 days ago (limit 90) and every other field within its limit.

**Prompt:** "Refresh my brain."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 15 — Ingest: URL seed fetch fails, falls back to paste

**Setup:** No brain. The user gives a website URL that cannot be fetched.

**Prompt:** "Build my brain from https://example.com."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 16 — Ingest: website copy is not proof

**Setup:** The only source is the company homepage, which says "Trusted by 500 teams" and "cuts reporting time by 60%".

**Prompt:** "Ingest this page."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 17 — Ingest: conflicts are shown, never auto-resolved

**Setup:** The pricing page says "from $49 per seat"; a customer call transcript says "we pay a flat $2,000 per month".

**Prompt:** "Ingest both."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 22 — Ingest: a confirmed value is never overwritten

**Setup:** The brain has a confirmed `buyer_title` of "VP Finance". New evidence says "CFO".

**Prompt:** "Ingest this call."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 23 — Ingest: Brain Diff needs approval per section

**Setup:** Ingest produces changes for Sections 1, 2 and 3.

**Prompt:** "Looks good, apply it all."

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

## Eval 30 — A customer phrase with no source is not stored

**Setup:** A brain with Sections 1 to 6.

**Prompt:** "Add a customer phrase: 'it just works'." No source given.

**Result:** Pass / Partial / Fail
**What failed or changed:**

---

