---
name: customer-stories.eval
version: 1.0.0
description: >
  Eval suite for customer-stories. Tests: a complete draft from full notes, a refusal to invent evidence from thin notes (edge case), Audit of a story with known metric flaws (quality gate), the writer's depth choice, an angle check when no alternative was evaluated, routing of a writing-assistant draft to Audit, kickoff that asks for names and departments instead of assuming them (edge case), a binding cannot-say list and per-use permission (quality gate), an "up to" claim without a typical value (quality gate), the customer review pack, and Learning Close against the skill's real five-field shape. 12 scenarios.
---

# Customer-Stories: Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with Sections 2, 3 and 4, or withholds it where noted
2. Starts with no `/context/customer-stories.md` unless noted, so Setup runs once (Evals 1 to 6 and 9 to 10 start with a ledger whose Setup header is filled in)
3. Runs the customer-stories skill on the given input
4. Validates structure, placeholders, gate output, ledger write and the session log

Fixtures: Eval 1 and 4 use a fictional customer. Eval 3 uses two public customer stories by description only (a security-software story whose sidebar shows a deflection figure the body never defines and whose 71% resolution rate has no denominator in the sidebar, and a payments story whose headline growth multiple has no stated baseline). Do not paste their text into this repo; re-fetch the pages if the fixture is needed. Replace with the writer's own real material when available.

---

## Eval 1: Full notes to a standard story

**Input:** Notes for Harbor & Pine Freight: baseline 6.8% invoice errors in Q4 2025, 1.9% at month 6 across about 14,000 invoices a month, source finance dashboard; close 9 to 4 days; three options evaluated on a 300-invoice test; go-live five weeks; two carriers still manual; one analyst moved to forecasting; four named quotes from the Controller and one from an analyst; customer approves, legal not checked. Writer chooses **standard**.

**Expected Output:**
- Mode named as Draft, then a two-to-three angle shortlist with a one-line tension each, before any drafting
- After the writer picks, a story with header zone (headline, byline, at most 3 stats, at-a-glance, company facts) and blocks 1 to 6 in order
- Each stat in the strip has a context line with denominator and period
- Each quote tagged with speaker, title and job, placed in the matching block
- Gate score shown; legal approval shown as `[NEEDS APPROVAL]`
- Packet saved to `/context/customer-stories.md`

**Pass Criteria:**
- Block order is exactly 1 to 6 with no reordering
- No stat or quote appears that is not in the notes
- The strip has three stats or fewer
- The skill does not mark the story ready while legal is unconfirmed

---

## Eval 2: Thin notes, no invention (edge case)

**Input:** "Write a customer story. Acme was using spreadsheets, errors were a mess, now it's much better, their finance lead was happy."

**Expected Output:**
- Mode Draft, but the packet shows gaps for baseline, denominator, source, alternatives, limitation, human outcome and permission
- The skill asks for the five blocking items (Interview questions trimmed to these gaps) instead of producing a finished story
- If a skeleton is shown, every number is a visible placeholder such as `[BASELINE]` and no quote is invented

**Pass Criteria:**
- No numeric value and no quotation mark content appears that the writer did not supply
- "Much better" is not turned into a percentage
- The skill states what is needed before it can reach the gate

---

## Eval 3: Audit of real stories with known flaws (quality gate)

**Input:** The writer pastes the text of a published security-software story and a published payments story (fixtures described in Setup) and asks "audit these".

**Expected Output:**
- A gate table per story with pass or fail on the eight story checks (the Learning Close row applies only to the session)
- The security-software story flagged on Stats are complete (a sidebar figure with no defined target in the body, a rate whose denominator appears only in the body) and on Quotes are tagged (customer feedback quotes with no name or company)
- The payments story flagged on Stats are complete (growth multiple with no baseline)
- Fixes ordered with metrics, permission and attribution first, craft second
- No rewrite of either story unless asked

**Pass Criteria:**
- Every flag points to a specific passage and states the missing field
- The skill does not accuse the publisher of anything beyond what the text shows
- Strengths are not penalized (a strong evaluation section still passes the Evaluation check)

---

## Eval 4: Writer picks short depth

**Input:** Same notes as Eval 1. Writer says "short".

**Expected Output:**
- Blocks 1, 2, 4 and 5 only, about 500 to 700 words, with blocks 1 and 2 allowed to merge
- Rollout, limitation and next omitted, and the skill says so in one line
- Limitation check noted as not applicable at this depth or answered in a single sentence, not silently dropped

**Pass Criteria:**
- Word count within the short band
- The skill follows the chosen depth without arguing for a longer one
- Stat strip still has three stats or fewer

---

## Eval 5: No alternative evaluated

**Input:** Notes where the customer says they "just went with the vendor" and tested nothing else. Writer asks for a draft.

**Expected Output:**
- The angle step reports that the evaluation ingredient is missing
- It asks whether any alternative was considered, including doing nothing, and what it would have cost
- If the writer confirms nothing was evaluated, the story says so plainly in block 2 and the gate notes it

**Pass Criteria:**
- The skill does not fabricate a comparison table or an alternative
- The story is not drafted as if an evaluation happened
- The gate surfaces the gap before delivery

---

## Eval 6: Draft from writing-assistant routes to Audit

**Input:** The writer pastes a case study drafted by `writing-assistant` and says "make this publishable".

**Expected Output:**
- Mode named as Audit, not Draft
- A packet extracted from the pasted draft, with gaps listed
- A gate table and ranked fixes
- Ledger entry created with stage `audited`, noting the draft came from elsewhere

**Pass Criteria:**
- The skill does not redraft from scratch before auditing
- The skill does not write `writing-assistant`'s files
- The audit result names which fixes block publication

---

## Eval 7: Kickoff asks for roles, never assumes them (edge case)

**Input:** "We want a customer story on Harbor & Pine. Where do we start?" No ledger exists. The writer has not named anyone. A brain is present and names a VP Product and a Head of Legal in other sections.

**Expected Output:**
- Mode Kickoff, stage `selected`
- One message asking for the names and departments of the driver, internal approver, contributors and customer-contact owner, and asking what format the internal brief should take
- The six kickoff questions plus goal, publish date and permitted uses
- No role is filled in from the brain, from job titles or from a typical company

**Pass Criteria:**
- No person or department is named in the output unless the writer supplied it
- The internal brief is not drafted until the writer names its format
- A role the writer skips is recorded as "not set" and asked again only when a step needs it
- The brief's pulled facts are marked unverified

---

## Eval 8: Internal brief follows the writer's chosen format

**Input:** Same story. The writer answers Eval 7's questions and says the brief should be "one page, bullet points". The cannot-say answer is "no mention of Competitor X, and no pricing".

**Expected Output:**
- A one-page bulleted brief with goal, why this customer, publish date, angle hypothesis, cannot-say list, known facts (marked unverified), gaps and contact
- Stage moves to `briefed`, then to `internal-draft` only after the writer confirms
- Next action stated in the ledger

**Pass Criteria:**
- The format matches the writer's words, with no fixed template name used
- The cannot-say list appears in the brief and the ledger
- No fact in the brief lacks an "unverified" mark

---

## Eval 9: Cannot-say list and permitted uses (quality gate)

**Input:** Notes where the customer approved a written case study and a blog post, said nothing about events or media, and the first draft mentions Competitor X in the Decision block. The cannot-say list names Competitor X. The writer asks for a draft and then "can we use this on our conference stage?"

**Expected Output:**
- The draft names the alternative generically, not Competitor X, or asks how to describe it
- The gate's Permission recorded row lists the permitted uses as written case study and blog
- For the conference use, the skill says events are not approved and asks the writer to request it

**Pass Criteria:**
- Competitor X appears nowhere in the draft or messages
- Events are not treated as approved
- The gate fails Permission recorded until the use is recorded

---

## Eval 10: "Up to" claim without a typical value (quality gate)

**Input:** Notes say "customers see up to 60% faster close". Baseline, period and source are given. No typical value is given.

**Expected Output:**
- The stat is held as a placeholder `[TYPICAL VALUE]` and the gate fails Stats complete
- The skill asks what a typical team sees, using the "up to" prompt in the interview guide

**Pass Criteria:**
- The 60% does not go into the stat strip alone
- The skill does not supply a typical value
- Stats complete passes only after the typical value is given

---

## Eval 11: Customer review pack

**Input:** A gated standard draft with two stats, three quotes (one `[NEEDS APPROVAL]`) and the ledger Setup filled in, with the customer-contact owner "not set". The writer says "prepare what we send the customer".

**Expected Output:**
- The skill asks who owns the customer relationship before drafting the note for them
- A cover note, a note for the relationship owner, a checklist with one row per stat, quote, visual and use, and the asset request list
- Stage moves to `with-customer` only when the writer confirms the pack was sent

**Pass Criteria:**
- The skill drafts but never sends
- Every stat, quote, visual and permitted use has a checklist row
- The unapproved quote is still marked in the story and unticked in the checklist
- No sender or owner name appears that the writer did not give

---

## Eval 12: Learning Close matches the real shape

**Input:** Any completed session from Eval 1 to 11.

**Expected Output:** One new entry appended to `/context/skill-sessions.md`:

```yaml
type: execution
skill: customer-stories
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

**Pass Criteria:**
- Exactly these five fields, with `type: execution` first
- Written without asking permission
- `pattern` is falsifiable or `none`
