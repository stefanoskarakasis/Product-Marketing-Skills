---
name: competitive-battlecard
version: 1.4.1
description: >
  Builds a one-page competitor battlecard a seller can skim in 60 seconds before a call,
  tailored to role, GTM motion, buyer persona, deal stage and the competitor's status in
  the deal. In a Slack thread it posts the card in the thread. Also lists your saved cards by roster tier and logs deal outcomes. Trigger on: "battlecard for [competitor]", "how do we beat [competitor]",
  "[competitor] is in my deal", "counter this
  objection", "set of cards", "we won against [competitor]", "that reply worked". Related: alternatives-map, signal-monitor, proof-points. Not for the leadership brief (competitive-briefing), a competitor Q&A (competitive-profile), the scheduled sweep (media-monitoring) or a public vs page (comparison-page-brief).
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-11-02
---

# Competitive Battlecard

A battlecard is read once, five minutes before a call, and quoted from memory in the call. This skill builds that one page for one competitor in one deal: what to say first, what to ask, what to say when the buyer pushes back, when to lean in and when to walk away. It does not map alternatives; it takes the alternatives map and proof registry in your brain, adds fresh evidence about the named competitor, tailors to who sells to whom at what stage, and proposes what it learned back into brain Section 3 for you to confirm.

## Trigger

- **When:** A seller or PMM needs a competitor-specific play for a live or upcoming deal, or a refresh of an existing card.
- **Not for:** A single question about a competitor with no deal to tailor to (a price, a launch, why we lose) → `competitive-profile` (`ask` mode). A request that names a role, buyer or stage stays here. Mapping who buyers compare you to → `alternatives-map`. A weekly read on what changed → `signal-monitor`. Registering or checking a claim → `proof-points`. A feature-level handoff doc with one comparison → `product-messaging-playbook`. Persona cards and a competitive playbook inside a positioning build → `positioning-messaging` (SALES-ENABLEMENT mode). A multi-skill program → `workflow-orchestrator`. The scheduled sweep of public pages → `media-monitoring` (its findings feed this card). A weekly leadership brief across the roster → `competitive-briefing`. The long document behind a decision → `competitor-deep-dive` (read here when one exists).
- **Example prompts:**
  - "Battlecard for [competitor]"
  - "How do we beat [competitor] with a CFO in the evaluation stage?"
  - "They say [claim]. How do I counter it?" (edge: one objection, answered from the card's blocks)
  - "Refresh the [competitor] card" (edge: compares with the last card)
  - "Set of cards for my five competitors" (pack: an index of saved cards, nothing rebuilt)
  - "We lost to [competitor], the price reply did not land" (outcome: one row in the log)

## Inputs

- **Args:** The competitor (required; doing nothing or a spreadsheet counts). Optional: the deal variables in Step 2, what the buyer actually said, delivery format. Missing items are asked once in Step 2.
- **Defaults:** Role account executive, buyer general, stage evaluation, competitor a challenger alongside us, delivery Google Doc. A skipped answer is stated as an assumption on the card.
- **Context keys:**
  - `/foundation/brain.md` (optional, sharper with it): Sections 1 to 8, see the contract.
  - `/foundation/me.md` (optional): format and detail only.
  - `/foundation/gaps.md` (append only).
  - `/context/battlecards/` (earlier cards for this competitor, and `_outcomes.md`), `/context/competitor-profiles/` (`roster_position`), `/context/signals/` (recent `signal-monitor` runs), `/context/meta-patterns.md` (guardrails).
  - The `~~` connector categories in `references/connectors.md` (`~~CRM`, `~~call recordings`, `~~competitive intelligence`, `~~win/loss`, `~~team chat`, `~~cloud storage` and others), or pasted material.
  - **Brain contract:** Reads Sections 1 to 8. Writes Section 3 only, as one appended Battlecard Field Notes block or a one-line stub, after you confirm the exact text. Never writes Sections 1, 2, 4, 5, 6, 7, 8. Field-level detail: `references/brain-contract.md`.

## Connectors (Optional)

The `~~` connectors this skill can read, and what each adds, are in `references/connectors.md`. Pulled facts are drafts: each is tagged with category, tool and date, and nothing is written until you confirm. No connectors? Paste the material; the output has the same shape.

## Pre-flight

- **Route check (first).** No deal and a leadership audience → name `competitive-briefing`; one question about a competitor → `competitive-profile`; a long write-up → `competitor-deep-dive`. One line, then ask whether to continue here.
- Load `/foundation/brain.md`. Read Sections 3 and 6 first: Section 3 decides what is already known about the competitor, Section 6 decides what we are allowed to claim. Then 1, 2, 4, 5, 7 and 8.
- **Brain absent: Quick-Brain, don't block.** Say once that no brain was found, ask the five questions in `references/quick-brain.md` in the Step 2 message, and label the card "Built from Quick-Brain answers".
- **Competitor not in Section 3:** say once, non-blocking, that it isn't in the alternatives map and that `alternatives-map` (in `pmm-positioning`, a separate plugin) gives later cards researched ground. The write-back step offers a stub.
- **Also read `references/preflight-details.md`:** meta-patterns, personal context (`/foundation/me.md`, format only), freshness limits (a stale section goes into Check before use) and gap capture (one question at most).
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If the named competitor, or comparing against competitors at all, is prohibited, stop: show the entry and ask the user how to proceed. Do not build around it.

## Steps

Three request types. A **card** request runs Steps 1 to 11. A **pack** request ("set of cards", "all five competitors") runs none of them: read the roster and the newest saved card per roster competitor, post the index in `references/pack-format.md`, then write the Learning Close row. Nothing is rebuilt. An **outcome** report ("we won against [competitor]", "that reply worked") follows `references/outcome-log.md`: one question at most, one appended row in `/context/battlecards/_outcomes.md`, then the Learning Close row.

### Step 1: Load Context

Read the brain as above. Then read the most recent card in `/context/battlecards/` for this competitor (to show what changed), the newest `/context/deep-dives/<competitor-slug>-*.md` if one exists (its Card feed block and Brain check; each claim keeps its own tag and date, and a `re-check` line is shown as a question), and the last 30 days of `/context/signals/` for any opportunity that names this competitor (a move to weigh, tagged with its original confidence), and, at a prospecting stage, the newest `/context/prospects/<slug>-*.md` for the account, and the rows for this competitor in `/context/battlecards/_outcomes.md` from the last 180 days (seller-reported, rank 5). Say in one line what was found.

### Step 2: Establish the Deal

Fill the variables below in this order of trust: (1) already stated in the request or earlier in the conversation, (2) a connector (CRM: account type, contract end date, employee count, contact roles), (3) ask. Ask once, in one combined message, with tappable options if the interface supports them, and only for what is still unknown. Confirm a connector inference in one line.

The variables (competitor, role, GTM motion, competitor's status, buyer persona, deal stage, segment and region, optional extras, delivery), their options and the default for each if skipped are in `references/deal-variables.md`. Read it now. Delivery is always asked, except in Slack.

**In Slack** (`competitive-profile/references/slack-mode.md` sections 7 and 11): do not ask for a delivery format; ask the remaining questions in one message, or state the assumptions on the card.

If the user says "just give it to me", build the neutral card (account executive, general buyer, evaluation), state the assumptions on the card, and offer to tailor. If the user pasted a buyer objection or a competitor claim, it becomes the first entry in 🔄 Reframe their strengths, answered directly, and is treated as the buyer's claim, not fact: unsourced, it is answered with a question and marked `[A]`.

### Step 3: Name Sources and Gather Evidence

List back, in one line, the sources for this run: pasted material, files, connector pulls, and public pages about the named competitor only (site, pricing, release notes, newsroom, public reviews). Do not scan beyond them; if a page cannot be read, ask for the text. Never fill a gap from memory.

Source order: your confirmed brain values (rank 0), then `~~CRM`, `~~win/loss` and `~~call recordings` (ranks 1 and 2), then `~~competitive intelligence` (rank 3: the team's own cards, read only and never written back), then public and third-party material (rank 4), then chat (rank 5). Ranks: `product-marketing-context/references/evidence-format.md`; a fact older than 12 months drops one rank. Newer evidence that disagrees with a confirmed value is shown as a question, never used to replace it. If a profile record kept by `competitive-profile` exists at `/context/competitor-profiles/<competitor-slug>-*.md`, read the newest one (by date, then time; older records have no time in the name) and treat each claim with that record's own tag and date, never as a confirmed brain value; a line marked `re-check` is shown as a question. Its front matter `roster_position` gives the Roster cell (`references/card-format.md`, "Roster tier and Re-check by"). If none exists, carry on without it, write "not on roster" and never ask for it.

Web rules (`references/research-rules.md`): check each result is about the right company; write "no data" rather than widening a search; a vendor-authored comparison is opinion.

Tag every claim with the evidence tags in `references/card-format.md`. Pulled facts are drafts until confirmed. Leave out names, emails and phone numbers of individuals.

### Step 4: Check Constraints

Before writing, test each candidate line.

- **Our side:** a claim about us goes into 💎 only if it is a Section 1 permitted claim or a Section 6 approved metric or approved quote (or, in Quick-Brain mode, a user-sourced item). Anything else is `[NEEDS PROOF]` and stays off the card; it goes to Open items for `proof-points`. A customer name or quote without approval is `[NEEDS APPROVAL]`.
- **Their side:** a weakness is stated as fact only if it is sourced. An unsourced weakness becomes a ❓ question. Absence is written "no public evidence of X", never "they don't have X".
- **Forbidden:** a line matching Section 6 `forbidden_claims`, or touching Section 8 `prohibited`, is removed and named in Check before use with the entry that caught it. If either list requires legal review for named-competitor comparisons, say so in Check before use and mark the card internal only.
- **Dates:** date every competitor claim "as of [Mon YYYY]". Add "re-check" past about 90 days. Treat a roadmap or launch date already past today as unconfirmed.
- **Concede what they own.** If the competitor documents something we usually win on, shade it 🟢 in their column, drop it from 💎 and build the card on what actually separates us for this competitor. Attack structure (an architectural, durable gap), not quality.

### Step 5: Tailor

Apply four lenses from `references/card-format.md`: persona (what to lead with), stage (the 🧭 move), competitor status × deal type (defend or displace), role and motion (emphasis). Layout and order never change; emphasis does. A status quo or DIY competitor uses only the hidden costs in Section 3 `status_quo`; never invent a figure.

### Step 6: Build the Card

Fill the template in `references/card-format.md`: about 350 words, hard ceiling 450 (counted from Check before use to Next move, without the deal line, tags, sources and footer), caps per block. Both formats use the same headers in the same order, as one stacked column (no side-by-side blocks). Write 🏆 and 🎤 last, after the data has shaped them. Apply Section 4 voice (language preferences, forbidden phrases) silently. Real strengths are acknowledged out loud: the first clause of every reply is true and generous. Write as though the competitor will read it: factual, dated, defensible, never mocking. If a previous card exists, add one line, "Changed since [date]", with at most three differences. Fill the Roster and Re-check by cells from the oldest displayed claim (`references/card-format.md`). If `_outcomes.md` holds two or more outcomes for this competitor in the last 180 days, add one line to Check before use with the counts, marked seller-reported; one outcome stays silent.

### Step 7: Gate Your Own Card

Run the Quality Gate before delivery. Fix what the evidence allows; cut a line that cannot pass. Show the score and any failed rows only.

### Step 8: Deliver and Save

Deliver in the format chosen in Step 2. Always save the record to `/context/battlecards/<competitor-slug>-YYYY-MM-DD.md` (format in `references/card-format.md`; never overwrite an earlier file). If files cannot be written, show the file and say it was not saved; never claim a save or a build that did not happen.

Format rules for the Google Doc, the HTML page, the Slack thread and anything else are in `references/delivery.md`. Read it now. Never claim a Doc, file or page count that was not made or checked.

### Step 9: Propose Brain Write-Back

Propose a write only if this run produced something the map lacks: (a) the competitor is missing from Section 3, (b) a dated competitor fact the Alternatives Map block does not hold (pricing model, packaging, an acquisition), (c) field evidence on why deals are lost or won (from `~~CRM` or `~~call recordings`, with n, or two or more outcomes logged for this competitor in the last 180 days, see `references/outcome-log.md`), or (d) a conflict between the map and fresh evidence. At most three lines.

Show the exact text as the "Proposed Section 3 note" (`references/card-format.md`), a source tag on each line, and ask "Add this to Section 3? Existing content stays unchanged." On yes, append. Append-only rules and the no-brain and not-saved cases: `references/brain-writeback.md`. Record the outcome in the saved card's Open items.

Never write Sections 1, 2, 4, 5, 6, 7 or 8. Our-side claims that lacked proof are handed to `proof-points`, not registered here.

### Step 10: Hand Off

Offer, never perform, the next move from `product-marketing-context/.claude-plugin/next-skill-map.md` ("After competitive-battlecard"); name only skills listed there.

### Step 11: Learning Close

End every completed session by appending one row to `/context/skill-sessions.md`
(create the file with a header row if it doesn't exist yet):

```yaml
type: execution
skill: competitive-battlecard
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / N/A]
```

Write this row directly — do not ask the user for permission. This is an
observational log entry, not a content write to `/foundation/brain.md` or
`/context/meta-patterns.md`, which still require explicit approval elsewhere
in this skill or in `meta-synthesis`. If nothing notable happened this
session, still write the row with `pattern: none` — a consistent log beats
a sparse one `meta-synthesis` can't trust.

## Outputs

- **Files written:** `/context/battlecards/<competitor-slug>-YYYY-MM-DD.md` (the card, evidence log and open items), plus `Battlecard-<competitor-slug>-YYYY-MM-DD.html` if HTML was chosen. `/foundation/brain.md` Section 3: one appended Battlecard Field Notes block or stub, only after confirmation. `/context/battlecards/_outcomes.md`: one appended row per reported outcome. `/context/skill-sessions.md`: one entry per session. Possibly one appended `skipped` block in `/foundation/gaps.md`.
- **Chat output format:** the card as paste-ready Google Doc markdown (or, for HTML, 🏆 🎤 🧭 and the file), the Gate score with failed rows only, any proposed brain note, one hand-off line.

```markdown
# [Us] vs. [Competitor]  (BATTLECARD · INTERNAL USE ONLY)
[Role] · [Motion] · [Status] · [Persona] · [Stage] · [Segment, Region]
## ⚠️ Check before use
## 🏆 Win condition
## 🎤 Say this first
## 🔍 Competitor snapshot (5 rows)
## ❓ Discovery questions
## 🔄 Reframe their strengths
## 🚦 Win vs. walk away
## 💎 Proof to use
## 🧭 Next move
```

- **External side effects:** None. Connectors are read-only; nothing is written to a CRM or any other external tool.

## Operating Rules

The claim, constraint, tailoring and connector rules live in Steps 2 to 5 and are tested in the Quality Gate. These five are stated only here.

- **Section 3 is the competitive source of truth.** Never create a separate profile or competitor file. Notes append under Section 3 on confirmation; the saved card is an output, not a second brain.
- **One page.** Cut the weakest row; never shrink type below 9 pt.
- **Brain writes need exact text and a yes.** Append only; a confirmed value is never overwritten.
- **Internal use only.** Every card carries the footer; legal review is flagged when Sections 6 or 8 require it.
- **Outcomes are append-only and seller-reported.** One row per report in `_outcomes.md`, roles only, never edit a saved card; a brain note needs two or more outcomes, exact text and a yes.

## Quality Gate

Runs after the card is built, before delivery.

| Check | Pass = |
|---|---|
| One page | 450 body words or fewer, caps held, prints on one page |
| Deal stated | Header shows role, motion, status, persona, stage, segment; assumptions listed |
| Claims tagged and dated | Every competitor claim has a tag and "as of"; "re-check" past ~90 days |
| Weakness sourced | No unsourced weakness stated as fact |
| Our side approved | 💎 holds only permitted or approved items |
| Constraints checked | Section 6 `forbidden_claims` and Section 8 `prohibited` tested, result shown |
| Walk-away present | 🛑 Walk away lists 3 signals, one about the champion or incumbent relationship |
| Write-back honest | Brain note shown as exact text and confirmed, or "none proposed" |
| Re-check date set | Deal block shows Roster and Re-check by, computed from the oldest displayed claim |
| Delivery truthful | Delivery asked, or posted in the Slack thread with no table and no delivery question; no Doc, file or page count claimed that was not made or checked; the record exists in `/context/battlecards/` |
| Pack and outcome modes | A pack lists every roster competitor, rebuilds nothing and says so; an outcome report appended exactly one row and edited no card; field results show only at n of 2 or more, marked seller-reported, never as the win rate |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session |

## Gotchas

Seven traps (buyer claims, competitor customers, vendor comparisons, pricing changes, past-dated roadmaps, outcomes versus win rate, packs as indexes): `references/gotchas.md`.
