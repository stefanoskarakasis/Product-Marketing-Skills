---
name: competitor-deep-dive
version: 1.1.0
description: >
  Builds a long-form, fully sourced deep-dive on one competitor for a named decision
  (strategy call, RFP, pricing change, roadmap bet), with dated reviews, deal evidence, a
  head-to-head per offering and where they win. In a Slack thread it posts a short summary and builds the full document. Triggers: "deep-dive on [competitor]",
  "full competitor write-up", "what do users really say about [competitor]", "teardown of
  [competitor]". Related: competitive-battlecard, competitive-profile, signal-monitor.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-25
---

# Competitor Deep-Dive

A deep-dive is read before a decision and checked when a claim is challenged. This skill builds that document for one competitor and one decision: what they sell, what changed, what buyers and customers actually say, where we beat them, where they beat us, and what each audience should do about it. It does not keep profiles current (that is `competitive-profile`), does not build the one-page sales card (that is `competitive-battlecard`), and does not map alternatives (that is `alternatives-map`). It takes what those hold, adds fresh dated evidence, and proposes what it learned back into brain Section 3 for you to confirm.

## Trigger

- **When:** A PMM, product lead or exec needs the long, sourced view of one competitor behind a named decision, or a refresh of an earlier deep-dive.
- **Not for:** The one-page sales card → `competitive-battlecard`. Keeping five competitors' profiles current and the roster → `competitive-profile`. A weekly read on what changed → `signal-monitor`. Mapping who buyers compare you to → `alternatives-map`. Registering or checking a claim → `proof-points`. A multi-skill competitive program → `workflow-orchestrator`.
- **Example prompts:**
  - "Deep-dive on [competitor] for our pricing review"
  - "Deep dive on [competitor] before the RFP response"
  - "What do users really say about [competitor]?" (edge: reviews and deal evidence weigh most)
  - "Refresh the [competitor] deep-dive" (edge: compares with the last saved deep-dive)

## Inputs

- **Args:** The competitor (required). Optional: the decision this supports, the main audience (sales, product, exec), delivery format, depth. Missing items are asked once in Step 2.
- **Notation:** `Section N` always means a brain section; `Part N` means the numbered part of the deep-dive document (Part 4 Pricing, Part 6 Deal evidence, Part 12 Brain check).
- **Defaults:** Decision "general reference", audience PMM, depth standard (about 2,500 body words), delivery Google Doc. A skipped answer is stated as an assumption in Check before use.
- **Context keys:**
  - `/foundation/brain.md` (optional, sharper with it): Sections 1 to 8, see the contract.
  - `/foundation/me.md` (optional): format and detail only.
  - `/foundation/gaps.md` (append only).
  - `/context/competitor-profiles/` (newest record for this competitor, if `competitive-profile` keeps one), `/context/deep-dives/` (earlier deep-dives), `/context/battlecards/`, `/context/signals/` (last 90 days), `/context/meta-patterns.md` (guardrails).
  - `~~CRM`, `~~call recordings`, `~~win/loss`, `~~competitive intelligence`, `~~reviews`, `~~company data`, `~~market data`, `~~team chat`, `~~knowledge base`, `~~cloud storage`, or pasted material.
  - **Brain contract:** Reads: Section 1 (our offerings, permitted claims, glossary), 2 (persona, pains, triggers), 3 (alternatives, status quo, why they leave, unique capabilities, `alt_shortfalls`, `switching_forces`, `objections`, and the Alternatives Map block for this competitor), 4 (language preferences, forbidden phrases), 5 (why now), 6 (approved metrics, approved quotes, forbidden claims), 7 (priorities), 8 (prohibited, approvals, stakeholders). Writes: Section 3 only, as one appended Deep-Dive Field Notes block or a one-line stub, after you confirm the exact text. Never writes to: Sections 1, 2, 4, 5, 6, 7, 8.

## Connectors (Optional, but Part 4 and Part 6 depend on them)

Every skill in this repo works without connectors, but a deep-dive is only as strong as its pricing and deal sources. This skill checks which are connected before it researches, and asks once (see Connector readiness in Pre-flight and Step 2).

| Connector | What it adds | Feeds section |
|---|---|---|
| `~~CRM` | Closed-won and closed-lost deals naming this competitor: loss reasons, amounts, account type, n | 4, 6 |
| `~~win/loss` | Buyer interviews on why deals were won or lost (rank 2, customer-spoken) | 6 |
| `~~call recordings` | Objections as buyers said them, pricing as buyers heard it, with verbatim quotes | 4, 6, 10 |
| `~~competitive intelligence` | The cards, stories and profiles your CI team already keeps (rank 3). Read first so the deep-dive never contradicts them; a conflict with a public page is shown as a question | 3, 4, 6, 9 |
| `~~company data` | Funding, headcount and hiring moves (rank 4) | 3, 4 |
| `~~reviews` | Public review pages and exports for this competitor | 7 |
| `~~market data` | Traffic and audience shifts | 3 |
| `~~team chat` | Field intel and pricing claims reps reported (rank 5, soft, labelled secondhand) | 4, 6 |
| `~~knowledge base`, `~~cloud storage` | Internal positioning notes, earlier decks and win/loss logs | 8, 10 |

**What each dependent section does without its connectors**

| Section | Needs | Without it |
|---|---|---|
| Part 4 What they sell and what it costs | Public pricing page (always); `~~CRM`, `~~call recordings` or `~~competitive intelligence` for deal pricing | List price only, labelled indicative; no deal pricing |
| Part 6 Deal evidence | Any one of `~~CRM`, `~~win/loss`, `~~call recordings` | "No deal evidence available". Nothing is inferred from reviews |

> **No connectors?** Paste the material (a closed-won and closed-lost export for this competitor, call excerpts, pricing notes) and I'll work from that. The output has the same shape.
> Pulled facts are drafts: each is tagged with category, tool and date, and nothing is written to the brain until you confirm. Connectors are read-only.

## Pre-flight

- Load `/foundation/brain.md`. Read Sections 3, 6 and 8 first: Section 3 says what is already known, Section 6 says what we may claim, Section 8 says what we may not do. Then 1, 2, 4, 5 and 7.
- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times in earlier deep-dive sessions.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): if `/foundation/me.md` exists, read it for format and detail only. It may shorten the deep-dive, never lengthen it past the ceiling. Never take a company fact from it.
- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll build from four quick answers and hold them for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask in the Step 2 message: (1) each product or offering we sell to compare, one sentence each; (2) what each is documented to do, with the source; (3) two honest weaknesses against this competitor; (4) one proof point we can source. Use them as stand-ins for Sections 1, 3 and 6 for this session only. Label the document "Built from Quick-Brain answers" and mark unsourced items `[Rep-stated]`. Our side of the head-to-head carries only what the user sourced.
- **Competitor not in Section 3:** surface once, non-blocking: "[Competitor] isn't in your alternatives map. I'll build from what we gather now; run `alternatives-map` (in `pmm-positioning`, a separate plugin) so later work starts from researched ground." The write-back step offers a stub.
- **Freshness:** a loaded brain section past its limit (Section 3, 2, 8: 180 days; Section 5, 7: 90 days; Section 6: 12 months per claim) goes into Check before use. A section marked 🔴 Placeholder is flagged before proceeding. For competitor facts use the `competitive-profile` windows: price 60 days; product, positioning and moves 90 days; buyer-side facts 180 days; reviews 90 days for the rating, any age for a dated quote.
- **Connector readiness.** Before researching, find out which categories in the table above are connected in this session. A category counts as connected only if a tool for it is present and answers; this plugin's `.mcp.json` lists what is wired, not what you are signed in to, so never infer connection from it. Record the result as a readiness table (Section, categories needed, status: connected with tool name / pasted / not connected). It goes in the Step 2 message, and a not-connected result for Part 4 deal pricing or Part 6 is prompted there, once. Never claim to have pulled anything from a category that is not connected.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If the named competitor, or comparing against competitors at all, is prohibited, stop: show the entry and ask how to proceed. Do not build around it.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a brain field this deep-dive needs is empty, stale or untagged and the answer would change it, ask one question: the question, one line on why it matters, "answer or skip". Answer: use it for this run and offer it as a brain update. Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run.

## Steps

### Step 1: Load Context

Read the brain as above. Then read, in this order: the newest `/context/competitor-profiles/<competitor-slug>-*.md` (each claim keeps that record's own tag and date; a line marked `re-check` is shown as a question), the newest `/context/deep-dives/<competitor-slug>-*.md` (to show what changed), `/context/battlecards/` for this competitor (so the deep-dive never contradicts a card in use), and the last 90 days of `/context/signals/` for anything naming this competitor. If no profile exists, carry on and never block on it. Then take the brain's standing beliefs about this competitor (Section 3 `why_leaving`, `alt_shortfalls`, `switching_forces`, `objections`; Section 4 `customer_phrases`) as hypotheses to test, not facts to repeat. Each one is carried into Part 12 (Brain check) and ends as confirmed, contradicted or untested. This is how the deep-dive learns from the brain and how the brain later learns from the deep-dive. Say in one line what was found: "Brain: Sections 1 to 8 present, Section 5 stale. Profile: 2026-09-30. Last deep-dive: none. Three recent signals. Six hypotheses to test."

### Step 2: Establish Scope

Fill in this order of trust: (1) already stated in the request, (2) a connector, (3) ask. Ask once, in one combined message, and only for what is unknown.

| Variable | Options | If skipped |
|---|---|---|
| Competitor | A named rival (a DIY build or doing nothing is a status-quo study, not a deep-dive: route to `alternatives-map`) | Required |
| Decision this supports | Strategy call · RFP response · Pricing change · Roadmap bet · Battlecard source · General reference | General reference |
| Main audience | Sales · Product · Exec · PMM | PMM |
| Depth | Standard (about 2,500 body words) · Short (about 1,500) · Long (up to 3,500) | Standard |
| Delivery | Google Doc (paste-ready, shown here in chat) | Always ask; Google Doc if unanswered. Not asked in Slack: a summary is posted and the Doc is the full document |
| Pricing and deal sources | Connect · Paste · Skip, one choice per not-connected row of the readiness table | Skip, stated in Check before use |

The decision line shapes emphasis, never section order.

**Connector prompt (same message, once).** Show the readiness table, then for each row that is not connected give three options and name the consequence:
1. **Connect.** Name the tool this plugin wires for the category (see "Wired today" in this plugin's `CONNECTORS.md`) and point to `docs/connect-your-tools.md` for sign-in steps. Wait for "connected", re-check which tools are present, and say what the first pull returned (for example "14 deals naming [competitor], Jan 2025 to Oct 2026"). If the tool still is not present, say so and offer Paste or Skip; never pretend.
2. **Paste.** Ask for the smallest useful thing: a closed-won and closed-lost export for this competitor, call excerpts that mention them, or the pricing notes. Pasted material is rank 5 unless it is a hard record the user confirms.
3. **Skip.** The section is built from what exists and carries its status line (see the template). Skipping is always allowed.

Do not nag: one prompt per run, no second reminder. The one exception: if the decision is Pricing change or RFP response and both Part 4 deal pricing and Part 6 would be empty, say in one sentence that a list-price-only deep-dive will not support that decision, and ask for Connect, Paste or "proceed anyway" before researching. A "proceed anyway" is honoured and recorded in Check before use. If the user says "just give it to me", use the defaults, state them in Check before use, and offer to tailor.

### Step 3: Name Sources and Gather Evidence

List back, in one line, the sources you will use this run: pasted material, files, connector pulls, and public pages about the named competitor only (its site, pricing page, release notes, newsroom, public review pages, filings). Do not scan beyond them. Follow `references/deep-dive-format.md` for what to extract from each. If a page cannot be fetched, say so, link it for the reader, and mark the fact "could not be confirmed"; never work around a blocked fetch with another method and never fill a gap from memory.

Tag every claim with the evidence tags in `competitive-battlecard/references/card-format.md`: `[Field: <tool>, n=<n>, <window>]`, `[Brain S<n>]`, `[Internal <Mon YYYY>]`, `[Public <Mon YYYY>]`, `[Third-party <Mon YYYY>]`, `[A]` and `[NEEDS PROOF]`. This skill defines no tags of its own. The two flags outside that table are used as the sibling skills use them: `[Rep-stated]` for an unsourced Quick-Brain answer and `[NEEDS APPROVAL]` for a customer name or quote without approval (a Section 6 flag, not an evidence tag). Pulled facts carry category, tool and date. Source order follows `product-marketing-context/references/evidence-format.md`: confirmed brain values (rank 0), then `~~CRM`, `~~win/loss`, `~~call recordings` (ranks 1 and 2), then `~~competitive intelligence` (rank 3, read only), then public and third-party material (rank 4), then chat (rank 5). A fact older than 12 months drops one rank; older than 24 months, two. Newer evidence that disagrees with a confirmed value is shown as a question, never used to replace it.

Rules that carry most of the weight:
- **Date everything.** Every external claim carries a source, a link where one exists, and "as of [Mon YYYY]". Date every review. When the same complaint appears in old and new reviews, that is the finding: say how long it has run.
- **Say when you don't know.** "No public evidence of X" is not "X doesn't exist". Use the first unless you have verified the second.
- **Reviews have no permalink.** Link the product review page and say once, in Confidence, that the page is the closest available reference.
- **Review dates from rendered pages are approximate.** Say so; if one date is wildly out of pattern, omit that review and say you did.
- **Internal intel is secondhand.** Pricing from a deal recap in chat is useful and unverified: cite the thread, label it secondhand, link the vendor page beside it.
- **A rebrand, acquisition or pivot is often the most useful single fact.** Put what changed and what did not side by side.
- **Vendor-authored comparisons are opinion.** Say so. A competitor's own pages prove only what it said.
- Leave out names, emails and phone numbers of individuals.
- **Status line per dependent section.** Part 4 and Part 6 open with one line saying where their evidence came from: "Source: `~~CRM` (tool), pulled [date], n = X", "Source: pasted by user, [date]", or "Not connected: [what is missing]". The line is never omitted and never optimistic.

### Step 4: Check Constraints

Before writing, test each candidate line.

- **Our side:** a claim about us is stated only if it is a Section 1 permitted claim or a Section 6 approved metric or approved quote (or a user-sourced item in Quick-Brain mode). Anything else is `[NEEDS PROOF]`, stays out of the document and goes to Open items for `proof-points`. A customer name or quote without approval is `[NEEDS APPROVAL]`.
- **Their side:** a weakness is stated as fact only if it is sourced. An unsourced weakness becomes a question in Open items. Absence is "no public evidence of X".
- **Forbidden:** a line matching Section 6 `forbidden_claims`, or touching Section 8 `prohibited`, is removed and named in Check before use with the entry that caught it. If either list requires legal review for named-competitor comparisons, say so and mark the document internal only.
- **Concede what they own.** Part 9 is not optional. If the competitor documents something we usually win on, say so and build on what actually separates us.
- **Write as though the competitor will read it:** factual, dated, defensible; no mockery, no guesses about intent.

### Step 5: Build the Deep-Dive

Fill the template in `references/deep-dive-format.md`, in its fixed order, as one stacked column. Budget: about 2,500 body words, hard ceiling 3,500 (Short 1,500; counted as in the reference file). Tables are capped by rows, not words. Write the Summary and Decision sections last, after the evidence has shaped them. Apply Section 4 voice silently. If an earlier deep-dive exists, add one line, "Changed since [date]", with at most five differences, and list each fact that is now past its freshness window as `re-check`.

### Step 6: Gate Your Own Deep-Dive

Run the Quality Gate before delivery. Fix what the evidence allows; cut a line that cannot pass. Show the score and failed rows only.

### Step 7: Deliver and Save

Always save the record to `/context/deep-dives/<competitor-slug>-YYYY-MM-DD.md` (never overwrite an earlier file). If files cannot be written, show the document and say it was not saved; never claim a save or a build that did not happen.

- **Google Doc (first-class, default):** show the full deep-dive in chat as clean markdown in the exact order of the template: headings, tables, no HTML, no code fence around it, so the user can select it and paste it into a Google Doc with headings and tables intact. Table header cells are bold. Say that in one line. Do not claim a Google Doc was created, shared or saved to Drive unless a connector actually did it. With a `~~cloud storage` connector that can create a Doc, offer it and ask before writing.
- **Slack thread:** never post the full deep-dive in the thread (`competitive-profile/references/slack-mode.md` section 11). Post one line that it is building, then a five-line summary: the decision, what they sell and cost, what changed, where they win, what we do about it. The full document is still built and saved as above, and the Doc is offered if a `~~cloud storage` tool can create one.
- **Anything else** (Word, PDF, slides, HTML): say it is not built in this version and offer the Google Doc.

### Step 8: Propose Brain Write-Back

Propose a write only if this run produced something Section 3 lacks: (a) the competitor is missing, (b) a dated competitor fact the Alternatives Map block does not hold (pricing model, packaging, rebrand, acquisition), (c) deal evidence on why deals are lost or won, with n, or (d) a conflict between the map and fresh evidence. At most three lines.

Show the exact text as the "Proposed Section 3 note" in `references/deep-dive-format.md`, with a source tag on each line, and ask: "Add this to Section 3? Existing content stays unchanged." On yes, append it to `/foundation/brain.md` under Section 3 as one block headed `### Deep-Dive Field Notes — [Competitor] (added via competitor-deep-dive, [YYYY-MM-DD])`, each line ending `[src: <where> | <YYYY-MM-DD> | <pulled|inferred|stated> | draft]`. Rules: append only; never edit existing text; a confirmed value is never overwritten (show both and ask); competitor website copy never becomes a `why_leaving` entry; if no brain exists, do not create one. If the note implies the map needs rework, say so and name `alternatives-map`. If files cannot be written, show the block and say it was not saved. Record the outcome (confirmed, declined, none proposed) in the saved record's Open items. Never write Sections 1, 2, 4, 5, 6, 7 or 8, and never create a competitor profile file: the profile belongs to `competitive-profile`.

### Step 9: Hand Off

Offer, never perform, the next move from `product-marketing-context/.claude-plugin/next-skill-map.md` ("After competitor-deep-dive"). Name only skills listed there. That entry includes `meta-verify` (a second quality gate, offered before the deep-dive leaves the PMM team for an exec, RFP or pricing decision) and `meta-learn` (a deeper capture of what this session taught). If a connector was skipped, the offer includes finishing it and refreshing Part 4 and Part 6.

### Step 10: Learning Close

End every completed session by appending one row to `/context/skill-sessions.md` (create the file with a header row if it doesn't exist yet):

```yaml
type: execution
skill: competitor-deep-dive
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / N/A]
```

The `pattern` is where `meta-synthesis` learns from this skill, so make it specific and falsifiable, and include the connector state and the brain check when they mattered: "Section 6 was empty because ~~CRM was not connected", "brain `why_leaving` was contradicted by 5 of 8 deal notes". Use `source: missing` when a connector or brain field was absent. Write this row directly; do not ask the user for permission. This is an observational log entry, not a content write to `/foundation/brain.md` or `/context/meta-patterns.md`. If nothing notable happened, still write the row with `pattern: none`.

## Outputs

- **Files written:** `/context/deep-dives/<competitor-slug>-YYYY-MM-DD.md` (the document, evidence log, brain check and open items). `/foundation/brain.md` Section 3: one appended Deep-Dive Field Notes block or stub, only after confirmation. `/context/skill-sessions.md`: one entry per session. Possibly one appended `skipped` block in `/foundation/gaps.md`.
- **Chat output format:** the full deep-dive as paste-ready Google Doc markdown (header outline below; full template in `references/deep-dive-format.md`), then the Gate score with failed rows only, the proposed brain note if any, and one hand-off line.

```markdown
# [Competitor] Deep-Dive (INTERNAL USE ONLY)
## Check before use
## 1. Decision and bottom line
## 2. Summary by audience
## 3. Company and moves
## 4. What they sell and what it costs
## 5. Recent signals
## 6. Deal evidence
## 7. What reviewers say
## 8. Head-to-head
## 9. Where they genuinely win
## 10. Talking points
## 11. Card feed
## 12. Brain check
## 13. Open items
## 14. Confidence and methodology
## 15. Sources
```
- **External side effects:** None. Connectors are read-only; nothing is written to a CRM or any other external tool.

## Verification

- Body is within budget (2,500 target, 3,500 ceiling; Short 1,500) and the fixed section order is kept in a single stacked column.
- Check before use names the decision, audience, every assumption, every stale section and every fact marked `re-check`.
- Every competitor claim carries a source, a link where one exists, and an "as of" date; every review quote carries its own date.
- No weakness is stated as fact without a source; absence is worded "no public evidence of".
- Section 6 `forbidden_claims` and Section 8 `prohibited` were checked and the result is shown.
- Our side of every head-to-head row is a permitted or approved claim, or the row is left out.
- Where They Win is present and names at least two real strengths.
- Part 4 and Part 6 each open with a status line naming their source and date, or "Not connected"; nothing is claimed as pulled that was not.
- Every brain hypothesis taken in Step 1 appears in Part 12 as confirmed, contradicted or untested.
- Every evidence tag used is defined in `competitive-battlecard/references/card-format.md`; no other tag appears except `[Rep-stated]` and `[NEEDS APPROVAL]`.
- The record exists in `/context/deep-dives/`; any brain write was shown as exact text and confirmed first; no profile file was created.
- The session was logged to `/context/skill-sessions.md`.

## Do Not Use For

- **`competitive-battlecard`**: the one-page card a seller reads before a call. It reads this deep-dive's Card feed block; this skill does not build the card.
- **`competitive-profile`**: keeping five competitors' profiles current and the roster itself. The deep-dive reads the newest record; it does not maintain it.
- **`signal-monitor`**: a weekly read on what changed. Its output feeds Part 5; it does not replace it.
- **`alternatives-map`**: building or refreshing the map of who buyers compare you to. Run it first when the competitor is missing from Section 3.
- **`proof-points`**: registering, verifying or auditing the claims a document relies on.
- **`positioning-messaging`**: positioning and messaging hierarchy.
- **`workflow-orchestrator`**: a multi-skill competitive program rather than one document.

---

## Operating Rules

- **Section 3 is the competitive source of truth.** The deep-dive record is an output, not a second brain and not a profile. Notes append under Section 3 on confirmation.
- **Ask once.** One combined intake message. Delivery is always asked (not in Slack, where a summary is posted); everything else only if unknown.
- **Name the decision.** A deep-dive without a decision is an encyclopedia; the decision sets emphasis, never order.
- **Our side comes only from permitted and approved claims.** Anything else is `[NEEDS PROOF]` and stays out.
- **Their side comes only from named, dated sources.** A competitor's own claim proves only that it said it.
- **An unsourced weakness is a question, never a statement.** Absence is "no public evidence of X".
- **Concede what they own.** Where They Win is non-negotiable.
- **Deal evidence outranks reviews.** When `~~CRM` or `~~win/loss` data exists, Part 6 leads and reviews support it.
- **Prompt for missing connectors once, never block.** A not-connected Part 4 or Part 6 is offered Connect, Paste or Skip, with the consequence named; the user's choice is honoured and recorded.
- **The brain is a hypothesis, not a source.** Standing beliefs are tested against fresh evidence and reported in Brain check; contradictions are shown, never silently resolved.
- **One tag vocabulary.** Tags come from `competitive-battlecard/references/card-format.md`; never invent a second set.
- **Budget the length.** Cut the weakest paragraph before raising the ceiling.
- **Check constraints before writing.** Section 6 forbidden claims and Section 8 prohibited items are tested on every line, and the result is shown.
- **Pulled facts are drafts.** Tag rank, source type and date; connectors are read-only; no external writes.
- **Brain writes need exact text and a yes.** Append only; a confirmed value is never overwritten.
- **Internal use only.** Every document carries the footer; legal review is flagged when Sections 6 or 8 require it.

## Quality Gate

Runs after the deep-dive is built, before delivery. Surface failures before delivering, never after.

| Check | Standard | Pass = |
|---|---|---|
| Decision named | Check before use states the decision and audience | Yes |
| Length held | Body words within budget; table row caps held | 3,500 or fewer (Short 1,500) |
| Claims sourced and dated | Every competitor claim has source and "as of"; review quotes dated; "re-check" past the window | Yes |
| Weakness sourced | No unsourced weakness stated as fact; absence worded "no public evidence" | Yes |
| Our side approved | Head-to-head "us" cells hold only permitted or approved items | Yes |
| Constraints checked | Section 6 `forbidden_claims` and Section 8 `prohibited` tested, result shown | Yes |
| They win | Where They Win names at least two real strengths | Yes |
| Deal evidence honest | Part 6 shows n and source, or says "no deal evidence available" | Yes |
| Write-back honest | Brain note shown as exact text and confirmed, or "none proposed"; no profile file created | Yes |
| Delivery truthful | Delivery asked (or, in Slack, a summary posted with the record path); no Doc, file or link claimed that was not made or checked | Yes |
| Connector status honest | Part 4 and Part 6 carry a status line; skipped or missing connectors are named; no pull claimed that did not happen | Yes |
| Brain check done | Each hypothesis from Step 1 is confirmed, contradicted or untested | Yes |
| One tag vocabulary | Every evidence tag exists in `card-format.md` | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

## Gotchas

- **Review sites block automated fetching.** Link the page, mark the fact unconfirmed, and do not substitute a guess.
- **A competitor's customer is not your proof.** A logo both vendors serve is not a win against the other.
- **Third-party "comparison" posts are often vendor-authored.** Say which, and never repeat an unsourced percentage from one.
- **Pricing pages change.** A list price is indicative; custom pricing is quoted by sales; deal pricing from chat is secondhand.
- **A past-dated roadmap item is a rumor.** Do not promise it in a document people will quote.
- **Contradicting reviews are a finding.** Praise and complaints about the same feature, years apart, deserve a sentence, not a quiet cut.
