---
name: competitive-battlecard
version: 1.0.0
description: >
  Builds a one-page competitor battlecard a seller can skim in 60 seconds before a call and quote mid-call, tailored to role, GTM motion, buyer persona, deal stage and the competitor's status in the deal. Reads the brain and the alternatives map; proposes field notes back to Section 3. Trigger on: "battlecard for [competitor]", "how do we beat [competitor]", "[competitor] is in my deal", "what do I say against [competitor]", "counter this objection". Related: alternatives-map, signal-monitor, proof-points.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-12
---

# Competitive Battlecard

A battlecard is read once, five minutes before a call, and quoted from memory in the call. This skill builds that one page for one competitor in one deal: what to say first, what to ask, what to say when the buyer pushes back, when to lean in and when to walk away. It does not research the market or map alternatives; it takes the alternatives map and the proof registry already in your brain, adds fresh evidence about the named competitor, tailors the result to who is selling to whom at what stage, and proposes what it learned back into brain Section 3 for you to confirm.

## Trigger

- **When:** A seller or PMM needs a competitor-specific play for a live or upcoming deal, or a refresh of an existing card.
- **Not for:** Mapping who buyers compare you to → `alternatives-map`. A weekly read on what changed → `signal-monitor`. Registering or checking a claim → `proof-points`. A feature-level handoff doc with one comparison → `product-messaging-playbook`. Persona cards and a competitive playbook as part of a positioning build → `positioning-messaging` (SALES-ENABLEMENT mode). A multi-skill competitive program → `workflow-orchestrator`.
- **Example prompts:**
  - "Battlecard for [competitor]"
  - "How do we beat [competitor] with a CFO in the evaluation stage?"
  - "[Competitor] is in my deal, what do I say?"
  - "They say [claim]. How do I counter it?" (edge: one objection, answered from the card's blocks)
  - "Refresh the [competitor] card" (edge: compares with the last saved card)

## Inputs

- **Args:** The competitor (required; doing nothing or a spreadsheet counts). Optional: role, GTM motion, the competitor's status in the deal, buyer persona, deal stage, segment and region, what the buyer actually said, delivery format (Google Doc or HTML). Missing items are asked once in Step 2.
- **Defaults:** Role account executive, buyer general, stage evaluation, competitor a challenger alongside us, delivery Google Doc. A skipped answer is stated as an assumption on the card.
- **Context keys:**
  - `/foundation/brain.md` (optional, sharper with it): Sections 1 to 8, see the contract.
  - `/foundation/me.md` (optional): format and detail only.
  - `/foundation/gaps.md` (append only).
  - `/context/battlecards/` (earlier cards for this competitor), `/context/signals/` (recent `signal-monitor` runs), `/context/meta-patterns.md` (guardrails).
  - `~~CRM`, `~~call recordings`, `~~competitive intelligence`, `~~win/loss`, `~~team chat`, `~~reviews`, `~~market data`, `~~company data`, `~~knowledge base`, `~~cloud storage`, or pasted material.
  - **Brain contract:** Reads: Section 1 (permitted claims, offerings, glossary), 2 (persona, economic buyer, champion, pains, triggers), 3 (alternatives, status quo, why they leave, unique capabilities, and the Alternatives Map block for this competitor), 4 (language preferences, forbidden phrases), 5 (why now), 6 (approved metrics, approved quotes, forbidden claims), 7 (priorities), 8 (prohibited, approvals, stakeholders). Writes: Section 3 only, as one appended Battlecard Field Notes block or a one-line stub, after you confirm the exact text. Never writes to: Sections 1, 2, 4, 5, 6, 7, 8.

## Connectors (Optional)

| Connector | What it adds |
|---|---|
| `~~CRM` | Closed-won and closed-lost deals naming this competitor, loss reasons, account type, contract end date |
| `~~call recordings` | Objections as buyers said them, and what moved the deal after |
| `~~team chat` | Field intel and pricing claims reps reported (rank 5, soft) |
| `~~competitive intelligence` | The cards, win/loss stories and profiles your CI team already keeps (rank 3, current internal strategy). Read first so the card never contradicts them; a conflict with a public page is shown as a question |
| `~~win/loss` | Buyer interviews on why deals were won or lost (rank 2, customer-spoken) |
| `~~company data` | Funding, headcount and hiring moves for the competitor (rank 4) |
| `~~reviews` | Public review themes about the competitor (paste export) |
| `~~market data` | Competitor traffic and audience shifts |
| `~~knowledge base` | Internal positioning and product notes |
| `~~cloud storage` | Existing decks, battlecards and win/loss logs |

> **No connectors?** Paste the material and I'll work from that. The output has the same shape.
> Pulled facts are drafts: each is tagged with category, tool and date, and nothing is written until you confirm.

## Pre-flight

- Load `/foundation/brain.md`. Read Sections 3 and 6 first: Section 3 decides what is already known about the competitor, Section 6 decides what we are allowed to claim. Then 1, 2, 4, 5, 7 and 8.
- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times in earlier battlecard sessions.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): if `/foundation/me.md` exists, read it for format and detail only (length, shape, how blunt). It may shorten the card, never lengthen it past one page. Never take a company fact or the seller's role from it.
- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll build from five quick answers and hold them for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask all five in the Step 2 message, then wait: (1) what we sell, in one sentence; (2) the best-fit buyer and the pain that pushes them to act; (3) up to three things we do better than this competitor, each with the source for it; (4) two honest weaknesses against this competitor; (5) one proof point we can source. Use the answers as stand-ins for Sections 1, 2, 3 and 6 for this session only. Label the card "Built from Quick-Brain answers" and mark unsourced items `[Rep-stated]`.
- **Competitor not in Section 3:** surface once, non-blocking: "[Competitor] isn't in your alternatives map. I'll build from what we gather now; run `alternatives-map` (in `pmm-positioning`, a separate plugin) so later cards start from researched ground." The write-back step offers a stub.
- **Freshness** (limits in `product-marketing-context/references/brain-schema.md`): a loaded section past its limit (Section 3, 2, 8: 180 days; Section 5, 7: 90 days; Section 6: 12 months per claim) goes into Check before use. A section marked 🔴 Placeholder is flagged before proceeding.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If the named competitor, or comparing against competitors at all, is prohibited, stop: show the entry and ask the user how to proceed. Do not build around it.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a brain field this card needs is empty, stale or untagged and the answer would change it (most often Section 3 `why_leaving` or Section 6 `approved_metrics`), ask one question: the question, one line on why it matters, "answer or skip". Answer: use it for this run and offer it as a brain update. Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run.

## Steps

### Step 1: Load Context

Read the brain as above. Then read `/context/battlecards/` for the most recent card on this competitor (to show what changed since) and the last 30 days of `/context/signals/` for any opportunity that names this competitor (a move to weigh, tagged with its original confidence). Say in one line what was found: "Brain: Sections 1 to 8 present, Section 5 stale. Last card: 2026-08-14. Two recent signals."

### Step 2: Establish the Deal

Tailoring is the point of this skill. Fill the variables below in this order of trust: (1) already stated in the request or earlier in the conversation, (2) a connector (CRM: account type, contract end date, employee count, contact roles), (3) ask. Ask once, in one combined message, with tappable options if the interface supports them, and only for what is still unknown. Confirm a connector inference in one line instead of asking.

| Variable | Options | If skipped |
|---|---|---|
| Competitor | A named rival, a DIY build, or doing nothing | Required |
| Your role | Account executive · SDR/BDR · Solutions engineer · CSM/account manager · Partner/channel · Sales leader · PMM | Account executive |
| GTM motion | New logo (outbound or ABM) · Inbound-led · PLG to enterprise · Expansion · Renewal · Partner/channel | Take it from `gtm-motions` output or Section 7 if present, else new logo |
| Competitor's status | Incumbent · Challenger alongside us · In the final two · Status quo / DIY | Challenger alongside us |
| Buyer persona | Economic buyer · Champion · Technical evaluator · Security/compliance · Procurement/legal · Exec sponsor · End user | General buyer |
| Deal stage | Prospecting · Discovery · Evaluation/POC · Negotiation · Renewal | Evaluation |
| Segment and region | Mid-market · Enterprise · Strategic; country or region | Section 2 company size and geography |
| Optional | Deal size, the CRM competitor field, what the buyer actually said | Do not ask again |
| Delivery | Google Doc (paste-ready, shown here in chat) · HTML page | Always ask; Google Doc if unanswered |

If the user says "just give it to me", build the neutral card (account executive, general buyer, evaluation), state the assumptions in one line on the card, and offer to tailor. If the user pasted a buyer objection or a competitor claim, it becomes the first entry in 🔄 Reframe their strengths, answered directly, and is treated as the buyer's claim, not fact: unsourced, it is answered with a question and marked `[A]`.

### Step 3: Name Sources and Gather Evidence

List back, in one line, the sources you will use this run: pasted material, files, connector pulls, and public pages about the named competitor only (its site, pricing page, release notes, newsroom, public review pages). Do not scan beyond them; if a page cannot be read, say so and ask for the text. Never fill a gap from memory.

Source order: your confirmed brain values (rank 0), then `~~CRM`, `~~win/loss` and `~~call recordings` (ranks 1 and 2), then `~~competitive intelligence` (rank 3: the team's own cards, read only and never written back), then public and third-party material (rank 4), then chat (rank 5). Ranks follow `product-marketing-context/references/evidence-format.md`; a fact older than 12 months drops one rank. Newer evidence that disagrees with a value you confirmed is shown as a question, never used to replace it. If a profile record kept by `competitive-profile` exists at `/context/competitor-profiles/<competitor-slug>-YYYY-MM-DD.md`, read the newest one and treat each claim with that record's own tag and date, never as a confirmed brain value; a line marked `re-check` is shown as a question. If none exists, carry on without it and never ask for it.

Web rules: read the target market and language, disambiguate company names with the category, check that each result is about the right company, and write "no data" rather than widening a search until something fits. A competitor's own pages prove only what it said. Read the complaint inside a positive review: it is where the best reframes live. A rebrand, acquisition or pivot is often the most useful single fact. Treat a vendor-authored comparison as opinion and say so.

Tag every claim with the evidence tags in `references/card-format.md`. Pulled facts are drafts until confirmed. Leave out names, emails and phone numbers of individuals.

### Step 4: Check Constraints

Before writing, test each candidate line.

- **Our side:** a claim about us goes into 💎 only if it is a Section 1 permitted claim or a Section 6 approved metric or approved quote (or, in Quick-Brain mode, a user-sourced item). Anything else is `[NEEDS PROOF]` and stays off the card; it goes to Open items for `proof-points`. A customer name or quote without approval is `[NEEDS APPROVAL]`.
- **Their side:** a weakness is stated as fact only if it is sourced. An unsourced weakness becomes a ❓ question. Absence is written "no public evidence of X", never "they don't have X".
- **Forbidden:** a line matching Section 6 `forbidden_claims`, or touching Section 8 `prohibited`, is removed and named in Check before use with the entry that caught it. If either list requires legal review for named-competitor comparisons, say so in Check before use and mark the card internal only.
- **Dates:** date every competitor claim "as of [Mon YYYY]". Add "re-check" past about 90 days. Treat a roadmap or launch date already past today as unconfirmed.
- **Concede what they own.** If the competitor documents something we usually win on, shade it 🟢 in their column, drop it from 💎 and build the card on what actually separates us for this competitor. Attack structure (an architectural, durable gap), not quality.

### Step 5: Tailor

Apply four lenses from `references/card-format.md`: persona (what to lead with), stage (the 🧭 move), competitor status × deal type (defend or displace, which blocks get the most room), role and motion (what the card emphasizes). The layout and order never change; emphasis does. A status quo or DIY competitor uses only the hidden costs in Section 3 `status_quo`; never invent a figure.

### Step 6: Build the Card

Fill the template in `references/card-format.md`: about 350 words, hard ceiling 450 (counted from Check before use to Next move, without the deal line, tags, sources and footer), caps per block. Both formats use the same headers in the same order, as one stacked column (no side-by-side blocks). Write 🏆 and 🎤 last, after the data has shaped them. Apply Section 4 voice (language preferences, forbidden phrases) silently. Real strengths are acknowledged out loud: the first clause of every reply is true and generous. Write as though the competitor will read it: factual, dated, defensible; never mocking; never a guess about intent. If a previous card exists, add one line, "Changed since [date]", with at most three differences.

### Step 7: Gate Your Own Card

Run the Quality Gate before delivery. Fix what the evidence allows; cut a line that cannot pass. Show the score and any failed rows only.

### Step 8: Deliver and Save

Deliver in the format chosen in Step 2. Always save the record to `/context/battlecards/<competitor-slug>-YYYY-MM-DD.md` (format in `references/card-format.md`; never overwrite an earlier file). If files cannot be written, show the file and say it was not saved; never claim a save or a build that did not happen.

- **Google Doc (first-class):** show the full card in chat as clean markdown in the exact order of the template in `references/card-format.md`: headings, tables, no HTML, no code fence around it, so the user can select it and paste it into a Google Doc with headings and tables intact. Say that in one line. Do not claim a Google Doc was created, shared or saved to Drive unless a connector actually did it. With a `~~cloud storage` connector that can create a Doc, offer it and ask before writing.
- **HTML page:** copy `templates/battlecard.html`, fill every `{{placeholder}}`, remove unused rows, and save as `Battlecard-<competitor-slug>-YYYY-MM-DD.html` beside the record. One self-contained file, no external dependencies, one stacked column with the same headers as the Doc. If a browser or PDF tool is available, print it and confirm one page; if not, say the page count was not verified.
- **Anything else** (Word, PDF, slides): say it is not built here and offer the two formats above.
- When the HTML file was chosen, the chat reply is the 🏆, 🎤 and 🧭 sections plus the file, not a second copy of the card.

### Step 9: Propose Brain Write-Back

Propose a write only if this run produced something the map lacks: (a) the competitor is missing from Section 3, (b) a dated competitor fact the Alternatives Map block does not hold (pricing model, packaging, an acquisition), (c) field evidence on why deals are lost or won (from `~~CRM` or `~~call recordings`, with n), or (d) a conflict between the map and fresh evidence. At most three lines.

Show the exact text as the "Proposed Section 3 note" in `references/card-format.md`, with a source tag on each line, and ask: "Add this to Section 3? Existing content stays unchanged." On yes, append it to `/foundation/brain.md` under Section 3. Rules: append only; never edit existing text; a value you confirmed is never overwritten (show both and ask); competitor website copy never becomes a `why_leaving` entry; if no brain exists, do not create one from a battlecard run unless the user asks (Quick-Brain answers are offered to `product-marketing-context` instead). If the note implies the map itself needs rework, say so and name `alternatives-map`. If files cannot be written, show the block and say it was not saved. Record the outcome (confirmed, declined, none proposed) in the saved card's Open items.

Never write Sections 1, 2, 4, 5, 6, 7 or 8. Our-side claims that lacked proof are handed to `proof-points`, not registered here.

### Step 10: Hand Off

Offer, never perform, the next move from `product-marketing-context/.claude-plugin/next-skill-map.md` ("After competitive-battlecard"). Name only skills listed there.

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

- **Files written:** `/context/battlecards/<competitor-slug>-YYYY-MM-DD.md` (the card, evidence log and open items), plus `Battlecard-<competitor-slug>-YYYY-MM-DD.html` if HTML was chosen. `/foundation/brain.md` Section 3: one appended Battlecard Field Notes block or stub, only after confirmation. `/context/skill-sessions.md`: one entry per session. Possibly one appended `skipped` block in `/foundation/gaps.md`.
- **Chat output format:** the full card as paste-ready Google Doc markdown (or, when HTML was chosen, 🏆 🎤 🧭 and the file), then the Gate score with failed rows only, the proposed brain note if any, and one hand-off line.

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

## Verification

- The card fits one page (about 350 body words, 450 at most, counted as in `references/card-format.md`) and keeps the fixed header order in a single stacked column.
- The header names role, motion, the competitor's status, persona, stage and segment, and lists every assumption.
- Every competitor claim carries an evidence tag and an "as of" date; none older than about 90 days lacks "re-check".
- No weakness is stated as fact without a source; no 💎 line is `[NEEDS PROOF]`.
- Section 6 `forbidden_claims` and Section 8 `prohibited` were checked and the result is on the card.
- The saved record exists in `/context/battlecards/`; any brain write was shown as exact text and confirmed first.
- The session was logged to `/context/skill-sessions.md`.

## Do Not Use For

- **`alternatives-map`**: building or refreshing the map of who buyers compare you to. Run it first when the competitor is missing from Section 3.
- **`competitive-profile`**: keeping five competitors' profiles current and the roster itself. The card reads the profile; it does not maintain it.
- **`signal-monitor`**: a weekly read on what changed. Its output feeds this card; it does not replace it.
- **`proof-points`**: registering, verifying or auditing the claims a card relies on.
- **`product-messaging-playbook`**: a Sales/CS handoff for one feature, with a single named comparison.
- **`positioning-messaging`**: positioning, messaging hierarchy, or persona cards and a competitive playbook in SALES-ENABLEMENT mode.
- **`workflow-orchestrator`**: a multi-skill competitive program rather than one card.

---

## Operating Rules

- **Section 3 is the competitive source of truth.** Never create a separate profile or competitor file. Notes append under Section 3 on confirmation; the saved card is an output, not a second brain.
- **Ask once.** One combined intake message. Delivery format is always asked; everything else is asked only if unknown.
- **Our side comes only from permitted and approved claims.** Anything else is `[NEEDS PROOF]` and stays off the card.
- **Their side comes only from named sources, dated.** A competitor's own claim proves only that it said it. A vendor-authored comparison is opinion.
- **An unsourced weakness is a question, never a statement.** Absence is "no public evidence of X".
- **Concede what they own.** Build the card on what separates us for this competitor, not on a standard list of differentiators.
- **One page.** Cut the weakest row; never shrink type below 9 pt or telegraph every line.
- **Tailor the emphasis, never the order.** Persona, stage, status, role and motion change what gets room, not where it sits.
- **Check constraints before writing.** Section 6 forbidden claims and Section 8 prohibited items are tested on every line, and the result is shown.
- **Pulled facts are drafts.** Tag category, tool and date; connectors are read-only; no external writes.
- **Brain writes need exact text and a yes.** Append only; a confirmed value is never overwritten.
- **Internal use only.** Every card carries the footer; legal review is flagged when Sections 6 or 8 require it.

## Quality Gate

Runs after the card is built, before delivery. Surface failures before delivering, never after.

| Check | Standard | Pass = |
|---|---|---|
| One page | Body words and block caps respected | 450 body words or fewer, caps held, prints on one page |
| Deal stated | Header shows role, motion, status, persona, stage, segment; assumptions listed | Yes |
| Claims tagged and dated | Every competitor claim has a tag and "as of"; "re-check" past ~90 days | Yes |
| Weakness sourced | No unsourced weakness stated as fact | Yes |
| Our side approved | 💎 holds only permitted or approved items | Yes |
| Constraints checked | Section 6 `forbidden_claims` and Section 8 `prohibited` tested, result shown | Yes |
| Walk-away present | 🛑 Walk away lists 3 signals, one about the champion or incumbent relationship | Yes |
| Write-back honest | Brain note shown as exact text and confirmed, or "none proposed" | Yes |
| Delivery truthful | Delivery asked; no Doc, file or page count claimed that was not made or checked | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

## Gotchas

- **A buyer's claim is not evidence.** "They're cheaper" is answered with a question and marked `[A]` until it is sourced.
- **A competitor's customer is not your proof.** A logo both vendors serve is not a win against the other; keep it off 💎.
- **Third-party "comparison" posts are often vendor-authored.** Say which, and never repeat an unsourced percentage from one.
- **Pricing pages change.** A list price is indicative unless the page says otherwise; custom pricing is quoted by sales.
- **A past-dated roadmap item is a rumor.** Do not promise it on a call.
