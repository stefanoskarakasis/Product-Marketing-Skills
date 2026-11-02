---
name: competitor-deep-dive
version: 1.3.1
description: >
  Builds a long-form, fully sourced deep-dive on one competitor for a named decision
  (strategy call, RFP, pricing change, roadmap bet), with dated reviews, deal evidence, a
  head-to-head per offering and where they win. In a Slack thread it posts a short summary and builds the full document. Triggers: "deep-dive on [competitor]",
  "full competitor write-up", "what do users really say about [competitor]", "teardown of
  [competitor]". Related: competitive-battlecard, competitive-profile, signal-monitor. Not for a weekly leadership read (competitive-briefing), the scheduled competitor sweep (media-monitoring) or a public vs page (comparison-page-brief).
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-11-02
---

# Competitor Deep-Dive

A deep-dive is read before a decision and checked when a claim is challenged. This skill builds that document for one competitor and one decision: what they sell, what changed, what buyers and customers actually say, where we beat them, where they beat us, and what each audience should do about it. It does not keep profiles current (that is `competitive-profile`), does not build the one-page sales card (that is `competitive-battlecard`), and does not map alternatives (that is `alternatives-map`). It takes what those hold, adds fresh dated evidence, and proposes what it learned back into brain Section 3 for you to confirm.

## Trigger

- **When:** A PMM, product lead or exec needs the long, sourced view of one competitor behind a named decision, or a refresh of an earlier deep-dive.
- **Not for:** The one-page sales card → `competitive-battlecard`. Keeping five competitors' profiles current and the roster → `competitive-profile`. A weekly read on what changed → `signal-monitor`. Mapping who buyers compare you to → `alternatives-map`. Registering or checking a claim → `proof-points`. A multi-skill competitive program → `workflow-orchestrator`. The scheduled sweep of public pages → `media-monitoring` (feeds this). Positioning and messaging hierarchy → `positioning-messaging`. The weekly leadership brief → `competitive-briefing` (offer this deep-dive when a decision needs the long evidence).
- **Example prompts:**
  - "Deep-dive on [competitor] for our pricing review"
  - "Deep dive on [competitor] before the RFP response"
  - "What do users really say about [competitor]?" (edge: reviews and deal evidence weigh most)
  - "Refresh the [competitor] deep-dive" (edge: compares with the last saved deep-dive)

## Inputs

- **Args:** The competitor (required). Optional: the decision this supports, the main audience (sales, product, exec), delivery format, depth. Missing items are asked once in Step 2.
- **Notation:** `Section N` always means a brain section; `Part N` means the numbered part of the deep-dive document (Part 4 Pricing, Part 6 Deal evidence, Part 12 Brain check).
- **Defaults:** Decision "general reference", audience PMM, depth standard (about 2,500 body words), delivery Google Doc. A skipped answer is stated as an assumption in Check before use.
- **Context keys:** the brain (`/foundation/brain.md`, `me.md` for format only, `gaps.md` append only), the `/context/` records (`competitor-profiles`, `deep-dives`, `battlecards`, `signals` last 90 days, `meta-patterns.md`) and the `~~` connectors in `references/connectors.md`, or pasted material.
  - **Brain contract:** Reads Sections 1 to 8. Writes Section 3 only, as one appended Deep-Dive Field Notes block or a one-line stub, after you confirm the exact text. Never writes Sections 1, 2, 4, 5, 6, 7, 8. Field detail: `references/inputs-detail.md`.

## Connectors (Optional, but Part 4 and Part 6 depend on them)

Which `~~` connectors this skill reads, what each feeds, and what Part 4 and Part 6 do without them: `references/connectors.md`. A deep-dive is only as strong as its pricing and deal sources, so Pre-flight checks which are connected and asks once. No connectors? Paste the material; the output has the same shape. Pulled facts are drafts, tagged with category, tool and date; connectors are read-only.

## Pre-flight

- **Route check (first).** If the request is a weekly or recurring read across the roster, or is for the board without a named decision, name `competitive-briefing`; a one-page card for a live deal, `competitive-battlecard`; one factual question, `competitive-profile`. One line, then ask whether to continue here.
- Load `/foundation/brain.md`: Sections 3, 6 and 8 first, then 1, 2, 4, 5, 7. The rest of Pre-flight (meta-patterns, personal context, Quick-Brain when the brain is absent, competitor not in Section 3, freshness windows, connector readiness, gap capture) is in `references/preflight-details.md`; read it now. Never claim a pull from a connector that is not connected.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If the named competitor, or comparing against competitors at all, is prohibited, stop: show the entry and ask how to proceed. Do not build around it.

## Steps

### Step 1: Load Context

Read the brain as above. Then read, in this order: the newest `/context/competitor-profiles/<competitor-slug>-*.md` (each claim keeps that record's own tag and date; a line marked `re-check` is shown as a question), the newest `/context/deep-dives/<competitor-slug>-*.md` (to show what changed), `/context/battlecards/` for this competitor (so the deep-dive never contradicts a card in use), and the last 90 days of `/context/signals/` for anything naming this competitor. If no profile exists, carry on and never block on it. Then take the brain's standing beliefs about this competitor (Section 3 `why_leaving`, `alt_shortfalls`, `switching_forces`, `objections`; Section 4 `customer_phrases`) as hypotheses to test, not facts to repeat. Each one is carried into Part 12 (Brain check) and ends as confirmed, contradicted or untested. Say in one line what was found, e.g. "Profile: 2026-09-30. Last deep-dive: none. Three signals. Six hypotheses to test."

### Step 2: Establish Scope

Fill in this order of trust: (1) already stated in the request, (2) a connector, (3) ask. Ask once, in one combined message, and only for what is unknown.

Ask for what is unknown, one message: the decision this supports (strategy call, RFP, pricing change, roadmap bet, battlecard source, general reference; default general reference), main audience (sales, product, exec, PMM; default PMM), depth (standard about 2,500 body words, short 1,500, long up to 3,500), delivery (always asked, Google Doc if unanswered, not asked in Slack), and for each not-connected row of the readiness table Connect, Paste or Skip (default Skip, stated in Check before use). A DIY build or doing nothing is a status-quo study: route to `alternatives-map`. The decision shapes emphasis, never order. The one-time connector prompt, its three options and the Pricing/RFP exception: `references/step-details.md`.

### Step 3: Name Sources and Gather Evidence

List back, in one line, the sources you will use this run: pasted material, files, connector pulls, and public pages about the named competitor only (its site, pricing page, release notes, newsroom, public review pages, filings). Do not scan beyond them. Follow `references/deep-dive-format.md` for what to extract from each. If a page cannot be fetched, say so, link it for the reader, and mark the fact "could not be confirmed"; never work around a blocked fetch with another method and never fill a gap from memory.

Tag every claim with the tags in `competitive-battlecard/references/card-format.md` (plus `[Rep-stated]` and `[NEEDS APPROVAL]`, never a second set). Source order: `product-marketing-context/references/evidence-format.md`; a fact older than 12 months drops one rank, 24 months two; newer evidence that disagrees with a confirmed value is a question. Date everything; say "no public evidence of X", never "X doesn't exist"; vendor-authored comparisons are opinion; internal intel is secondhand; no names, emails or phone numbers. Part 4 and Part 6 each open with a status line (source, date, n, or "Not connected"). All rules: `references/research-rules.md`.

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

- **Google Doc (default):** show the deep-dive in chat as clean markdown in template order, no HTML or code fence, ready to paste; never claim a Doc was created unless a connector did it.
- **Slack thread:** never post the full document; post a one-line "building" note and a five-line summary. Still build and save the record.
- **Anything else** (Word, PDF, slides, HTML): not built in this version; offer the Google Doc. Detail: `references/delivery.md`.

### Step 8: Propose Brain Write-Back

Propose a write only if this run produced something Section 3 lacks: (a) the competitor is missing, (b) a dated competitor fact the Alternatives Map block does not hold (pricing model, packaging, rebrand, acquisition), (c) deal evidence on why deals are lost or won, with n, or (d) a conflict between the map and fresh evidence. At most three lines.

Show the exact text as the "Proposed Section 3 note" (`references/deep-dive-format.md`), a source tag on each line, and ask "Add this to Section 3? Existing content stays unchanged." On yes, append as one Deep-Dive Field Notes block; never overwrite, never create a profile file, never write other sections. Record the outcome in Open items. Block format and cases: `references/brain-writeback.md`.

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

`meta-synthesis` learns from the `pattern`, so make it specific and falsifiable, naming the connector state or brain check when it mattered; use `source: missing` when a connector or brain field was absent. Write this row directly; do not ask the user for permission. This is an observational log entry, not a content write to `/foundation/brain.md` or `/context/meta-patterns.md`. If nothing notable happened, still write the row with `pattern: none`.

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

## Operating Rules

The claim, constraint and connector rules live in Steps 2 to 4 and are tested in the Quality Gate. These are stated only here.

- **Section 3 is the competitive source of truth.** The deep-dive record is an output, not a second brain and not a profile.
- **Name the decision.** Without one it is an encyclopedia; the decision sets emphasis, never order.
- **Deal evidence outranks reviews.** When `~~CRM` or `~~win/loss` data exists, Part 6 leads.
- **The brain is a hypothesis, not a source.** Standing beliefs are tested and reported in Brain check; contradictions are shown, never silently resolved.
- **Budget the length.** Cut the weakest paragraph before raising the ceiling.
- **Internal use only.** Every document carries the footer; legal review is flagged when Sections 6 or 8 require it.

## Quality Gate

Runs after the deep-dive is built, before delivery.

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
| Check before use complete | Names the decision, audience, every assumption, every stale section and every `re-check` fact | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

## Gotchas

Six traps (review sites block fetching, competitor customers, vendor-authored comparisons, pricing pages, past-dated roadmaps, contradicting reviews): `references/gotchas.md`.
