---
skill: product-marketing-context
version: 3.0.0
eval_version: 2.0.0
last_updated: 2026-10-14
author: Stefanos Karakasis
---

# Evals — product-marketing-context

Scenario-based eval file for `product-marketing-context`, testing the skill's
real 5-step flow: detect brain state, run the wizard, write the brain file,
run a health audit, and route without naming unverified downstream skills.

**How to use this file:**
1. Set up the starting condition (file state, prior messages) as described.
2. Send the input to a Claude session with this skill active.
3. Check the output against the Pass criteria. Every criterion must be met.
4. Mark ✅ PASS or ❌ FAIL. Log failures with the observed output.

**Scoring threshold:** 15/17 scenarios must pass (88%) for the skill to be
considered production-ready. Below that, identify the failing category and
fix the operating rule or step that governs it.

---

## Category A — Brain State Detection (Step 1) (4 scenarios)

### A1 — No brain: explains value in one line before the wizard starts
**ID:** `state-no-brain-first-run`
**Starting condition:** `/foundation/brain.md` does not exist. No `.agents/` or `.claude/` legacy files.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Response explains in one line what the brain does for downstream skills
- [ ] Wizard starts from Section 1 in the same response or immediately after
- [ ] No fabricated "downstream skill" is named unless the skill has genuinely verified it reads this brain's section structure (per Operating Rule 4)

---

### A2 — Brain exists: offers view/edit/audit, doesn't restart
**ID:** `state-brain-exists`
**Starting condition:** `/foundation/brain.md` exists and all 6 sections are populated.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Existing sections are loaded silently, not re-asked
- [ ] Offers [View current] [Edit a section] [Run health audit]
- [ ] Wizard does not auto-launch from Section 1

---

### A3 — Legacy files detected and offered for migration
**ID:** `state-legacy-detected`
**Starting condition:** No `/foundation/brain.md`. `.agents/icp.md` exists.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Legacy file is named specifically, not just "old files found"
- [ ] Offers to migrate, showing each extracted value before writing anything
- [ ] Does not write `/foundation/brain.md` until extracted values are confirmed
- [ ] Legacy file itself is not deleted after migration

---

### A4 — Audit trigger loads silently, doesn't restart wizard
**ID:** `state-audit-trigger`
**Starting condition:** `/foundation/brain.md` exists.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] Skill loads brain silently
- [ ] Runs the Step 4 health audit rather than starting the wizard
- [ ] Does not re-ask any already-answered question

---

## Category B — The Wizard (Step 2) (5 scenarios)

### B1 — Section confirmation gate
**ID:** `wizard-section-confirm-before-next`
**Starting condition:** No brain. User has answered all 5 Section 1 (Product Context) questions.
**Input:** Product name, description, stage, target market, value proposition.
**Pass criteria:**
- [ ] Skill shows all 5 answers back in a summary
- [ ] Asks "Look good? (yes / edit / skip)" or equivalent
- [ ] Does not proceed to Section 2 until the user confirms

---

### B2 — Vague ICP company size rejected
**ID:** `wizard-vague-company-size-rejected`
**Starting condition:** Wizard is on Section 2 (ICP), company size question.
**Input:** `"Small to medium businesses"`
**Pass criteria:**
- [ ] Skill does not accept and store this answer
- [ ] Pushes back asking for specific numbers (employee count or ARR range)
- [ ] Does not move to the next question until a specific answer is given

---

### B3 — Vague value proposition rejected
**ID:** `wizard-vague-value-prop-rejected`
**Starting condition:** Wizard is on Section 1, value proposition question.
**Input:** `"We help companies grow faster"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Prompts the user to use the structure: "[Product] helps [target market] to __ so they can __"
- [ ] Does not advance until the structure is followed

---

### B4 — Vague alternatives rejected, named products required
**ID:** `wizard-vague-alternatives-rejected`
**Starting condition:** Wizard is on Section 3 (Alternatives & Positioning).
**Input:** `"The big CRMs and some spreadsheets"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Asks for named products buyers actually compare the user to (e.g. "Salesforce, HubSpot, Pipedrive")
- [ ] Once named, alternatives are stored as-is — not normalised into a category label

---

### B5 — Skip accepted without pushback
**ID:** `wizard-skip-accepted`
**Starting condition:** Wizard is on Section 4 (Voice & Tone) confirmation.
**Input:** `"Skip for now"`
**Pass criteria:**
- [ ] Skill accepts the skip without guilt or repeated prompting
- [ ] Section is marked incomplete, not silently filled with a placeholder
- [ ] Skill continues to Section 5

---

## Category C — Writing the Brain File (Step 3) (3 scenarios)

### C1 — Brain written only after confirmation, using the real template
**ID:** `write-only-after-confirm`
**Starting condition:** Wizard running. User has just confirmed Section 6 (Proof Points), the last required section. Section 7 (Strategy) is offered next and may be skipped.
**Input:** `"Yes, that looks good"`
**Pass criteria:**
- [ ] `/foundation/brain.md` is written using `templates/brain-template.md`
- [ ] All confirmed sections have real values — no `[Needs input]` left in a section the user completed
- [ ] Any `.brain-draft.md` marker from a prior partial session is cleared

---

### C2 — Partial exit leaves a usable partial brain, not a blocked state
**ID:** `write-partial-on-exit`
**Starting condition:** Wizard running. User has confirmed Sections 1 and 2.
**Input:** `"Stop for now, I'll come back later"`
**Pass criteria:**
- [ ] Skill confirms progress is saved and names how to resume
- [ ] A partial, usable brain (or draft marker) exists for the confirmed sections
- [ ] Skill does not write incomplete/unconfirmed sections as if they were final

---

### C3 — Resume picks up from the correct section
**ID:** `write-resume-from-draft`
**Starting condition:** A draft/partial state exists with Sections 1–2 confirmed, stopped before Section 3.
**Input:** `"Build my brain"` (new session)
**Pass criteria:**
- [ ] Skill detects the partial state and offers to resume, not restart
- [ ] Names the section where the user left off
- [ ] Does not re-ask Section 1 or 2 questions

---

## Category D — Health Audit (Step 4) (3 scenarios)

### D1 — All 6 sections scored, with concrete fixes for gaps
**ID:** `audit-full-scoring`
**Starting condition:** Brain exists with a mix of specific and generic answers across sections.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] All 6 sections (Product Context, ICP, Alternatives & Positioning, Voice & Tone, Market Context, Proof Points) are scored 0–100
- [ ] Sections scoring below 50 get one concrete, specific fix — not "needs more detail"
- [ ] Skill offers to jump straight into editing the weakest section

---

### D2 — Generic field flagged even if technically non-empty
**ID:** `audit-generic-field-flagged`
**Starting condition:** Brain exists. ICP company size field literally contains "businesses of various sizes."
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] This field is flagged as a gap despite being non-empty
- [ ] Score reflects genericness, not just presence of a value
- [ ] Fix suggested asks for a specific number/range

---

### D3 — Unquantified proof point flagged
**ID:** `audit-unquantified-proof-point`
**Starting condition:** Brain exists. Section 6 contains "High customer retention rate" with no number or source.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] Proof Points section score reflects the missing quantification
- [ ] Fix suggests a specific number with a source (e.g. "89% retention, internal dashboard Q4 2025")

---

## Category E — Routing and Downstream Naming (Step 5) (2 scenarios)

### E1 — Downstream skill named only if genuinely verified (Edge case)
**ID:** `routing-only-mapped-skills-named`
**Starting condition:** Full brain build just completed.
**Input:** Brain confirmation accepted (`"Yes"`)
**Pass criteria:**
- [ ] Skill states plainly that the brain is ready and other skills will read from it
- [ ] Names a next skill only if it appears in the "After product-marketing-context" entry of `.claude-plugin/next-skill-map.md` — per Operating Rule 4
- [ ] If no skill is named, that's a pass, not a gap — a name from memory is a broken promise, not a helpful suggestion

---

### E2 — Wrong-skill request routed without brain wizard hijacking it
**ID:** `routing-wrong-skill-request`
**Starting condition:** Any state.
**Input:** `"Help me build a competitive battlecard"`
**Pass criteria:**
- [ ] The brain wizard does not start in response to this request
- [ ] Skill does not claim to handle competitive battlecard output itself

---

## Eval Log

Use this table to track runs. Update after each eval session.

| Run date | Version | Scenarios passed | Scenarios failed | Failed IDs | Notes |
|---|---|---|---|---|---|
| 2026-08-22 | v3.0.0 | — | — | — | Eval file fully rewritten against the real 5-step SKILL.md — the prior 37-scenario version tested a first-run-hook/wizard/migration/Step-9-routing design that no longer exists in SKILL.md, and used skill names from an old naming convention throughout |

---

## Known Gaps (add as discovered)

| Gap ID | Description | Scenario to add | Priority |
|---|---|---|---|
| — | — | — | — |

## Eval 1 — Connector present: pulled facts are tagged drafts

**Setup:** The `call recordings` connector is available and returns relevant material.

**Prompt:** "Build my brain and pre-fill the ICP from our calls."

**Expect:** Facts are pulled and each is shown tagged with category, tool and date. Nothing is written to the brain or any external tool until the user confirms. Pulled quotes and proof points are marked unverified.

## Eval 2 — No connectors: paste fallback, same output shape

**Setup:** No connectors are available.

**Prompt:** "Build my brain."

**Expect:** The skill asks the user to paste the material, then produces the same output format as with a connector. It does not claim to have pulled anything.

## Eval 3 — Cold-start brain: recognised, not treated as complete

**Setup:** `/foundation/brain.md` exists with the header `🟡 Cold start — built via alternatives-map on [date]` and holds only Section 3 (Alternatives & Positioning). Sections 1, 2, 4, 5 and 6 are absent.

**Prompt:** "Build my brain."

**Expect:** The skill says in one line that another skill started the brain and lists Section 3 as filled and the other five as missing. It offers to build the missing sections, expand Section 3, or run the audit. It does not restart the wizard from Section 1 as if no brain existed, does not rewrite Section 3 unprompted, and does not ask for fields Section 3 already holds. If the user then runs the audit, Section 3 is scored on its content and the five absent sections score 0. After all six sections are confirmed, the `🟡 Cold start` line is removed.

## Eval 4 — Provenance tag written with every confirmed value

**Setup:** No brain exists. The user answers Section 1 and confirms.

**Prompt:** "Yes, that looks good."

**Expect:** Each written value carries a tag in the form `[src: ... | YYYY-MM-DD | stated | confirmed]` as defined in `references/brain-schema.md`. User-typed answers are `stated`.

## Eval 5 — Legacy brain with no tags loads silently

**Setup:** `/foundation/brain.md` exists with all six sections and no provenance tags.

**Prompt:** "Audit my brain."

**Expect:** The brain loads without re-asking anything. The audit reports provenance coverage as 0 percent untagged (legacy), does not mark any field stale solely for lacking a tag, and does not rewrite any field.

## Eval 6 — Section 7 questions reject vague answers

**Setup:** A complete Sections 1 to 6 brain. The user asks to add strategy.

**Prompt:** "Our goal is to grow revenue."

**Expect:** The skill asks for metric, baseline, target and date before storing anything in Section 7. Nothing is written until the user confirms the before/after.

## Eval 7 — Stale field flagged with one concrete fix

**Setup:** A brain whose Section 5 tag is dated more than 90 days ago.

**Prompt:** "Check brain health."

**Expect:** Section 5 is reported as stale against its limit in `references/brain-schema.md`, with one concrete fix. A brain with no Section 7 reports it as "not built", not as a gap and not as 0.

## Eval 8 — Missing Section 7 does not make a complete brain incomplete

**Setup:** A brain with Sections 1 to 6 confirmed and no `🟡 Cold start` line.

**Prompt:** "Build my brain."

**Expect:** The skill offers View, Edit a section and Run audit. It does not treat the brain as cold-start and may offer Section 7 once, as optional.

## Eval 9 — A confirmed value is never overwritten by newer evidence

**Setup:** The brain has `persona: Controller` confirmed by the user last month. New call notes say the buyer is "the VP of Finance."

**Prompt:** "Update my brain from these notes."

**Expect:** The skill shows both values with their sources and dates and asks which is right. It does not change `persona` until the user answers. The old value stays until the user confirms the change.

## Eval 10 — Refresh lists only stale fields and asks one at a time

**Setup:** A brain with Section 5 dated 120 days ago (limit 90) and every other field within its limit.

**Prompt:** "Refresh my brain."

**Expect:** The skill lists only the Section 5 fields as stale, with age and limit. It asks "Still true? [yes / changed / drop]" for one field at a time and writes nothing until the user confirms.

## Eval 11 — Refresh "drop" removes only after confirmation

**Setup:** The same stale brain.

**Prompt:** "Drop it" for a stale `macro_forces` field.

**Expect:** The skill shows exactly what will be removed, asks for confirmation, and only then removes it. It does not touch any other field.

## Eval 12 — Refresh with nothing stale stops in one line

**Setup:** A brain where every field is within its limit.

**Prompt:** "What's stale in my brain?"

**Expect:** One line saying nothing is stale. No questions asked. No file written.

## Eval 13 — Gaps: skipped gap is quiet for 30 days

**Setup:** `/foundation/gaps.md` holds an `open` gap and a gap whose newest block is `skipped` 10 days ago.

**Prompt:** "Answer my brain gaps."

**Expect:** Only the `open` gap is offered. The skipped one is not shown. Answering appends an `answered` block and writes the answer to the brain with a `stated` tag after the user confirms the exact before/after.

## Eval 14 — Gaps file is append-only

**Setup:** A gap `G-003` is `open`. The user answers it.

**Prompt:** "It's the VP of Finance."

**Expect:** A new block with `gap_id: G-003` and `status: answered` is appended. The earlier `open` block is not edited or deleted.


## Eval 15 — Ingest: URL seed fetch fails, falls back to paste

**Setup:** No brain. The user gives a website URL that cannot be fetched.

**Prompt:** "Build my brain from https://example.com."

**Expect:** The skill says the page could not be read, makes no claims about the site, and asks the user to paste the homepage and pricing page text. It does not guess from the domain name.

## Eval 16 — Ingest: website copy is not proof

**Setup:** The only source is the company homepage, which says "Trusted by 500 teams" and "cuts reporting time by 60%".

**Prompt:** "Ingest this page."

**Expect:** Those lines are extracted as evidence with the lowest authority (public marketing) and are not filed as proof points. The Brain Diff does not put them in Section 6 as confirmed.

## Eval 17 — Ingest: conflicts are shown, never auto-resolved

**Setup:** The pricing page says "from $49 per seat"; a customer call transcript says "we pay a flat $2,000 per month".

**Prompt:** "Ingest both."

**Expect:** Both versions appear side by side with their sources. The skill asks which is right and writes nothing until the user answers.

## Eval 18 — Ingest: a single source is tagged inferred

**Setup:** A claim appears in exactly one document.

**Prompt:** "Ingest this."

**Expect:** The proposed field carries an `inferred` tag and `draft` status. Two or more agreeing sources are tagged `pulled`.

## Eval 19 — Ingest: empty or unreadable input

**Setup:** The user attaches an empty file and an image-only PDF.

**Prompt:** "Add these to my brain."

**Expect:** The skill reports that no text could be read from either, proposes no brain changes, and asks for a text version.

## Eval 20 — Ingest: over the cap

**Setup:** The user pastes 40 documents.

**Prompt:** "Ingest all of these."

**Expect:** The skill takes the first batch within the cap (about 10 documents or 5 transcripts), says what was left out, and offers to continue in a next round.

## Eval 21 — Ingest: personal data is not stored

**Setup:** A call transcript contains an email address and a phone number.

**Prompt:** "Ingest this call."

**Expect:** Neither value appears in the evidence file or the brain. Only the business fact is stored.

## Eval 22 — Ingest: a confirmed value is never overwritten

**Setup:** The brain has a confirmed `buyer_title` of "VP Finance". New evidence says "CFO".

**Prompt:** "Ingest this call."

**Expect:** The skill shows both, asks first, and leaves the confirmed value in place until the user decides.

## Eval 23 — Ingest: Brain Diff needs approval per section

**Setup:** Ingest produces changes for Sections 1, 2 and 3.

**Prompt:** "Looks good, apply it all."

**Expect:** The skill still confirms section by section, or states that one yes covers all three and lists them, before writing. Fields it could not support go to the gaps queue.

## Eval 24 — My context asks only about format

**Setup:** No `/foundation/me.md`.

**Prompt:** "Set up my context."

**Expect:** At most six short questions about length, detail, shape, bluntness and phrases to avoid, each with a default. It asks nothing about the product, customers or numbers, shows the exact file, and writes only after a yes.

## Eval 25 — My context redirects company facts

**Setup:** During Step 9 the user says "we sell to CFOs at mid-size banks".

**Prompt:** (the sentence above)

**Expect:** The skill does not store it in `me.md`. It says that belongs in the brain and offers to add it there after confirmation.

## Eval 26 — My context works without a brain

**Setup:** No `/foundation/brain.md`.

**Prompt:** "My context."

**Expect:** The skill still runs, writes only `/foundation/me.md` after confirmation, and offers to build the brain afterwards.

## Eval 27 — Wizard offers Section 8 as recommended

**Setup:** A confirmed brain with Sections 1 to 6.

**Prompt:** "Edit a section" then "Execution".

**Expect:** The skill asks about stakeholders, approvals, prohibited items, channels and cadence, roles first. It does not ask for personal details, and the audit afterwards reports Section 8 as built or "not built", never as a gap.

## Eval 28 — Refresh covers Section 8 on its 180-day limit

**Setup:** Section 8 dated 200 days ago, all other sections fresh.

**Prompt:** "What's stale in my brain?"

**Expect:** Only the Section 8 fields are listed as stale, with age 200 days and limit 180 days.

## Eval 29 — Wizard asks the deal-reality fields in the right sections

**Setup:** No brain. The user has no material to share.

**Prompt:** "Build my brain."

**Expect:** Business model is asked in Section 1. Jobs to be done, cost of the problem, anti-persona and standing buying-committee roles are asked in Section 2. Per-alternative shortfalls, the four switching forces and objections are asked in Section 3. Customer language is asked in Section 4. Conversion action is asked in Section 7. No new section number appears. "Subscription" alone is challenged as a business model.

## Eval 30 — A customer phrase with no source is not stored

**Setup:** A brain with Sections 1 to 6.

**Prompt:** "Add a customer phrase: 'it just works'." No source given.

**Expect:** The skill asks who said it and where. If the user cannot say, nothing is written to `customer_phrases`; a gap block is appended to `/foundation/gaps.md` instead.

## Eval 31 — Ingest keeps customer words verbatim

**Setup:** A pasted call transcript where a customer says: "We live in the inbox and a spreadsheet, and month-end is a fire drill."

**Prompt:** "Add material" and paste the transcript.

**Expect:** The evidence block holds the exact words as `quote`, supports `4.customer_phrases`, and carries the call as `source`. The Brain Diff proposes the phrase exactly as spoken, not tidied or shortened. Phrases are not merged with similar ones. A number the customer mentioned is routed toward Section 6 as a draft, not into `customer_phrases`.

## Eval 32 — An existing brain without the ten fields stays complete

**Setup:** A confirmed brain with Sections 1 to 6 and none of the deal-reality fields.

**Prompt:** "Run health audit."

**Expect:** Section scores are the same as before the fields existed. The audit reports "Deal-reality fields captured: 0 of 10" and names the one that would help most. It is never listed as a gap, never lowers a score, and the brain is not called incomplete.

## Eval 33 — An objection with no approved response is recorded, not invented

**Setup:** A brain with Sections 1 to 6.

**Prompt:** Edit Section 3. The user gives the objection "We already have an ERP module" and says there is no agreed response.

**Expect:** The objection is stored with who raises it and the response left open. A gap block for the response is appended. The skill does not write a response of its own.

## Eval 34 — All four switching forces, or the missing ones become gaps

**Setup:** Edit Section 3. The user gives push and pull only.

**Prompt:** "That's all I have."

**Expect:** Push and pull are stored after the exact before/after is confirmed. Habit and anxiety are not invented. They are added to the gaps file as open blocks.

## Eval 35 — Committee roles are defaults; buyer-personas still writes nothing

**Setup:** A brain with `committee_roles` filled in Section 2.

**Prompt:** "Map the buying committee for this deal" (run through `buyer-personas`).

**Expect:** `buyer-personas` starts from the stored roles, adjusts them for the deal in chat, and writes nothing to the brain. If the user wants a change to the standing roles, the skill hands it to `product-marketing-context`.

## Eval 36 — Pricing page feeds business model and conversion action as pulled

**Setup:** The user gives a website and pricing page URL. Fetching works.

**Prompt:** "Build my brain from my website."

**Expect:** `business_model` and `conversion_action` are proposed in the Brain Diff as `pulled`, rank 4, with the page as source. The button text on the site is read as the conversion action only as a proposal. Nothing is written until the user approves that section.
