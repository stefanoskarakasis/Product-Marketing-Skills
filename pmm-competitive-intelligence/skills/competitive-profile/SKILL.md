---
name: competitive-profile
version: 1.0.0
description: >
  Keeps a roster of your five key competitors with a dated, sourced profile each,
  refreshes only what has gone stale, and always offers a weekly scheduled refresh.
  Trigger on: "who are my key competitors", "set up my competitive profiles", "refresh my
  competitor profiles", "what's stale", "competitive roster". Related: alternatives-map,
  signal-monitor, competitive-battlecard.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-13
---

# Competitive Profile

A battlecard is only as good as the facts under it, and competitor facts decay: pricing pages change in weeks, a launch or an acquisition changes the story overnight. This skill keeps five competitors current. It does not research the whole market and it does not draw the alternatives map. It takes the competitors your brain already names, holds a dated and sourced profile for each, refreshes only the lines that have gone stale, and proposes what it learned back to brain Section 3 for you to confirm. Every competitive skill (`competitive-battlecard`, `signal-monitor`, `positioning-messaging`) then reads one fresh source instead of re-researching.

## Trigger

- **When:** Setting up or reviewing which competitors matter and what market you play in; refreshing profiles; checking what has gone stale; folding signals, battlecard debriefs or deal data into the profiles.
- **Not for:** Mapping who buyers compare you to, status quo and DIY included → `alternatives-map`. A weekly read on what changed across the market → `signal-monitor`. A one-page card for a live deal → `competitive-battlecard`. Registering or verifying your own claims → `proof-points`. Building the brain itself → `product-marketing-context`.
- **Example prompts:**
  - "Set up my competitive profiles."
  - "Who are my five key competitors, and what's stale?"
  - "Refresh the Stripe profile."
  - "Review my roster against last quarter's deals." (v2: uses `~~CRM` counts)
  - "Fold this week's signals into the profiles." (v2)
  - "Track all twelve competitors." (edge: capped at five; the other seven stay in Section 3 as they are)

## Inputs

- **Args:** A mode (below) and optionally a competitor name. With no mode, the skill picks one: `setup` if no roster exists, otherwise `status`.
- **Modes:**

| Mode | Scope | What it does |
|---|---|---|
| `setup` | v1 | Confirms your market, picks the roster of up to five, builds first profiles, proposes a schedule |
| `refresh` | v1 | Refreshes only stale lines for one competitor or the whole roster |
| `status` | v1 | Freshness board: what is stale, what changed, what is missing |
| `review` | v1 | Shows proposed brain notes as exact text and writes them on your yes |
| `intake` | v2 | Folds `/context/signals/`, `/context/battlecards/` and `~~CRM` or `~~call recordings` evidence into profile proposals |
| `roster` | v2 | Quarterly check of who really shows up in deals; proposes a swap, never forces one |

- **Defaults:** Roster of five (a hard cap). Sources: only those named in this run. Unattended runs (scheduled) use `refresh` and `status` only.
- **Context keys:** `/foundation/brain.md`, `/foundation/evidence.md`, `/foundation/gaps.md`, `/foundation/me.md` (format only), `/context/signals/`, `/context/battlecards/`, `/context/competitor-profiles/`, `/context/skill-sessions.md`, `/context/meta-patterns.md`, `~~CRM`, `~~call recordings`, `~~competitive intelligence`, `~~win/loss`, `~~company data`, `~~market data`, `~~reviews`, `~~knowledge base`, `~~team chat`, `~~cloud storage`, or pasted material.
  - **Brain contract:** Reads: Section 1 (offerings, permitted claims, target market), 2 (geography, company size, persona), 3 (alternatives, status quo, category, market type, unique capabilities, any Alternatives Map block), 5 (why now), 6 (approved proof, forbidden claims), 7 (priorities), 8 (prohibited, approvals). Writes: Section 3 only, as one appended Competitor Roster and Profile Notes block, after you confirm the exact text. Never writes to: Sections 1, 2, 4, 5, 6, 7, 8.

## Connectors (Optional)

| Connector | What it adds |
|---|---|
| `~~competitive intelligence` | The cards and profiles your CI team already keeps. Read first (rank 3); a conflict with a public page is shown as a question |
| `~~CRM` | Competitor field on closed-won and closed-lost deals: who actually shows up (v2 roster), loss reasons, deal sizes |
| `~~call recordings` | Objections and competitor mentions as buyers said them |
| `~~win/loss` | Buyer interviews on why deals were won or lost |
| `~~company data` | Funding, headcount and hiring moves |
| `~~market data` | Traffic and audience shifts |
| `~~reviews` | Public review themes (paste export) |
| `~~knowledge base` | Internal competitor notes |
| `~~team chat` | Competitor mentions and pricing claims reps reported (v2 `intake`) |
| `~~cloud storage` | Existing decks, win/loss logs and CI exports |

> **No connectors?** Paste the material and I'll work from that. The output has the same shape.
> Pulled facts are drafts: each is tagged with category, tool and date, and nothing is written to your brain until you confirm.

## Pre-flight

Context is loaded in a fixed order so the right facts come from the right place. Paths and field keys are defined in `product-marketing-context/references/brain-schema.md`; evidence ranks in `product-marketing-context/references/evidence-format.md`.

| Load | From | Why |
|---|---|---|
| Section 3 first | `/foundation/brain.md` | The roster starts here: `alternatives`, `status_quo`, `category`, `market_type`, `unique_capabilities`, and any Alternatives Map block |
| Sections 1, 2 | same | Your market: `target_market`, `offerings`, `geography`, `company_size`; the profile is always read against who you sell to |
| Section 6, 8 | same | What you may claim, and what you may not research or compare (`prohibited`) |
| Section 5, 7 | same | Why-now and this quarter's priorities decide which competitor gets deep attention |
| Earlier profiles | `/context/competitor-profiles/` | The newest record per competitor is the baseline; a refresh is a delta against it |
| Debriefs | `/context/battlecards/`, `/context/signals/` | v2 `intake` only |
| Guardrails | `/context/meta-patterns.md` | Surface any guardrail fired 2+ times in earlier competitive-profile sessions |
| Format | `/foundation/me.md` | Length and shape only. Never a company fact |

- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll work from five quick answers and hold them for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask all five in one message: (1) what you sell, in one sentence; (2) the market and the buyer you sell to; (3) the up to five competitors that show up in deals; (4) where you honestly lose to each; (5) where your deal data lives. Use them as stand-ins for Sections 1 to 3. Label every profile "Built from Quick-Brain answers" and mark unsourced items `[Rep-stated]`. Do not write to a brain that does not exist.
- **No named competitors in Section 3:** do not invent a roster. Say so and route to `alternatives-map`; offer to start with the competitors the user names now, tagged `[Rep-stated]`.
- **Freshness** (limits in `brain-schema.md`): a loaded section past its limit goes into Check before use. A roster older than 90 days is flagged for `roster`.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If a named competitor, or competitor research itself, is prohibited, stop on that competitor and show the entry.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a field this run needs is empty or stale and the answer would change the profile (most often Section 3 `unique_capabilities` or `why_leaving`), ask one question: the question, one line on why it matters, "answer or skip". Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run. None in unattended runs.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): `/foundation/me.md` is read for format and detail only.

## Steps

### Step 1: Pick the Mode

State the mode and the competitors in scope in one line. With no mode: `setup` if there is no roster record, otherwise `status`. A scheduled run is `refresh` followed by `status`, with no questions.

### Step 2: Confirm the Market and the Roster (setup, roster)

Show the market in one block built from the brain: category, market type, target market, geography and size, and your value-promise axis if Section 3 holds one (for example breadth vs. depth). Ask the user to confirm or correct it; a correction is offered as a note for `product-marketing-context`, not written here.

Then fix the roster. Candidates come from Section 3 `alternatives` (direct competitors only; status quo and DIY stay in Section 3 and are not profiled). Rank them by deal presence (`~~CRM` competitor field if connected, otherwise the user's judgment), then by Section 7 priority. Cap the roster at five. If the user wants a sixth, ask which one leaves; the leaver stays in Section 3 unchanged.

### Step 3: Check Your Own Side Against the Market (setup)

A profile compares a competitor with you, so check the "us" side once, for up to three differentiators from Section 3 `unique_capabilities`. For each, ask for a named mechanism, not an adjective ("approvals route by contract value" passes; "intuitive" does not). Then ask: "what question would expose this if it were hollow?" A differentiator with no good answer, or no proof in Section 6, is marked `[NEEDS PROOF]` and handed to `proof-points`. Keep shipped and roadmap apart: anything not in Section 1 `offerings` or `permitted_claims` is listed as roadmap and never enters a profile as a capability. Show the result; write nothing.

### Step 4: Build or Refresh the Profiles

For each competitor in scope, fill the record in `references/profile-format.md`: market and buyer, product and packaging, pricing and terms, positioning and axis, recent moves, where they win, where they lose, and sources. Every line carries an evidence tag and an "as of" date. Rules:

- **Delta only on refresh.** Read the newest record for that competitor. Compare each line's age with its window (table in `references/profile-format.md`). Refresh only lines past their window or named in a signal. Carry unchanged lines forward with their original date: re-reading a page that did not change is not a new fact.
- **Source order:** confirmed brain values (rank 0), then `~~CRM`, `~~win/loss` and `~~call recordings` (ranks 1 and 2), then `~~competitive intelligence` (rank 3: your CI team's cards, read only and never written back), then public and third-party material (rank 4), then chat (rank 5). A fact older than 12 months drops one rank. Newer evidence that disagrees with a confirmed value is shown as a question.
- **Web rules:** only the sources the user named plus public pages about the named competitor (its site, pricing, release notes, newsroom, review pages). Disambiguate company names with the category; check that each result is about the right company; write "no data" rather than widening a search until something fits. A competitor's own claims prove only that it said them. A vendor-authored comparison is opinion; say so. Never fill a gap from memory.
- **No unsourced weakness.** A weakness without a source is written as a question for the field, never as a statement.
- **No personal data.** Roles and company names only; no names, emails or phone numbers of individuals.

### Step 5: Intake From Signals, Battlecards and Deals (intake)

Read `/context/signals/` (last four runs), `/context/battlecards/` records and open items, and `~~CRM` or `~~call recordings` evidence the user names. Turn each item into at most one proposed profile change, tagged with its source. Two rules protect the profile from noise: (a) one data point stays a `note`; a loss reason or objection is proposed as "where they win" only when it appears at least twice (n of 2 or more, with the window stated); (b) a signal that touches none of the five competitors is dropped and counted. A change that conflicts with a value you confirmed in the brain is shown with both values and the question, not applied.

### Step 6: Roster Upkeep (roster)

Once a quarter, count how often each competitor appears in the `~~CRM` competitor field (or the user's deal list) for the last 90 days. Propose, never force: promote a competitor that shows in at least three deals and is not on the roster, and demote one that has been absent for two checks in a row. Say what each swap costs: a new profile to build, an old profile frozen at its last date. If nobody connected a CRM, say the check ran on the user's own recollection and mark it `[A]`.

### Step 7: Freshness Board (status)

Show one table: competitor, last profile date, number of lines past their window, the oldest line, what changed since the last record, and open `[NEEDS PROOF]` items. Mark 🟢 current, 🟡 some lines stale, 🔴 pricing or product stale, ⚪ no profile yet. End with the single most useful next action.

### Step 8: Gate Your Own Output

Run the Quality Gate before saving. Fix what the evidence allows; cut a line that cannot pass. Show the score and any failed rows only.

### Step 9: Save

Write each profile to `/context/competitor-profiles/<competitor-slug>-YYYY-MM-DD.md` (never overwrite; the newest file is the current profile) and the board or roster check to `/context/competitor-profiles/_status-YYYY-MM-DD.md`. A pulled fact is `draft` until you confirm it. If files cannot be written, show the file and say it was not saved; never claim a save that did not happen.

### Step 10: Propose Brain Write-Back (review)

Propose a write only if the run produced something Section 3 lacks: (a) the roster itself, (b) a dated competitor fact the map does not hold, (c) a "where they win" or "where they lose" supported by n of 2 or more, or (d) a conflict between the map and fresh evidence. At most five lines, each with a source tag. Show the exact text as the "Roster and profile note" in `references/profile-format.md` and ask: "Add this to Section 3? Existing content stays unchanged." On yes, append it to `/foundation/brain.md` under Section 3. Rules: append only; never edit existing text; a confirmed value is never overwritten; competitor website copy never becomes a `why_leaving` entry. Never write Sections 1, 2, 4, 5, 6, 7 or 8. Corrections to the market go to `product-marketing-context`; unproven claims go to `proof-points`; a map that needs rework goes to `alternatives-map`. Unattended runs never write the brain: they leave the proposal in the saved record for the next `review`.

### Step 11: Propose the Schedule

Every completed interactive run ends here, because a profile that is not refreshed is a snapshot, not a profile. Say in one short block what the schedule would do and ask once: "Schedule this? Weekly refresh of stale lines, a quarterly roster check." If a scheduling tool is available and the user says yes, create the task. If not, show the paste-ready prompt from `references/profile-format.md`. A scheduled task starts a fresh session, so the prompt must name the folder that holds the brain and every source it may read, and it must state that the run saves records and never changes the brain. If the user declines, do not ask again in this session.

### Step 12: Hand Off

Offer, never perform, the next move from `product-marketing-context/.claude-plugin/next-skill-map.md` ("After competitive-profile"). Name only skills listed there.

### Step 13: Learning Close

End every completed session by appending one row to `/context/skill-sessions.md` (create the file with a header row if it doesn't exist yet):

```yaml
type: execution
skill: competitive-profile
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / N/A]
```

Write this row directly, without asking. In an unattended run use `source: N/A`. If a pattern repeats across sessions, for example "pricing lines were stale again after under 60 days", it is surfaced for `meta-synthesis`, which proposes any change to the refresh windows for you to confirm. The windows in this skill do not change on their own.

## Outputs

- **Files written:** `/context/competitor-profiles/<competitor-slug>-YYYY-MM-DD.md` (one per competitor per run), `/context/competitor-profiles/_status-YYYY-MM-DD.md`, `/context/skill-sessions.md` (one row per session). `/foundation/brain.md` Section 3: one appended Roster and Profile Notes block, only after confirmation, and never from an unattended run. Possibly one appended `skipped` block in `/foundation/gaps.md`.
- **Chat output format:**

```
# Competitive profiles: [date]
Market: [category · market type · segment]   Roster: [n of 5]   Mode: [mode]
| Competitor | Profile | Stale lines | Changed since | Open |
Gate: n of 8 · proposed brain note (exact text) or "none proposed"
Schedule: [proposed / accepted / declined]
```

- **External side effects:** None, except a scheduled task you approve. Connectors are read-only; nothing is written to a CRM or a CI platform.

## Verification

- The roster has five competitors or fewer, each named in Section 3 or by you this run, tagged accordingly.
- Every profile line has an evidence tag and an "as of" date; carried-forward lines keep their original date.
- On a refresh, only lines past their window or named in a signal were re-researched, and the rest were carried forward.
- No weakness is stated as fact without a source; no roadmap item appears as a capability.
- Section 6 `forbidden_claims` and Section 8 `prohibited` were checked and the result is shown.
- The brain was written only after the exact text was shown and confirmed, and never by an unattended run.
- The schedule was proposed once.
- The session was logged to `/context/skill-sessions.md`.

## Do Not Use For

- **`alternatives-map`**: building or refreshing the map of who buyers compare you to, including status quo and DIY. Run it first when Section 3 holds no named competitors.
- **`signal-monitor`**: the weekly read on what changed across the market. Its saved lists feed `intake`; it does not replace it.
- **`competitive-battlecard`**: a one-page card for a live deal. It reads the profiles this skill keeps.
- **`proof-points`**: registering, verifying or auditing the claims a profile relies on.
- **`positioning-messaging`**: positioning, messaging hierarchy, or persona cards and a competitive playbook.
- **`workflow-orchestrator`**: a multi-skill competitive program rather than keeping five profiles current.

---

## Operating Rules

- **Section 3 is the competitive source of truth.** The profile records are dated outputs; the roster and confirmed notes live in Section 3. Never create a second competitor file the other skills read as truth.
- **Five at most.** More than five stale profiles is a reading list, not a program. A sixth competitor replaces one.
- **Ask once.** One combined intake message; at most one gap question per run; no questions in unattended runs.
- **Their side comes only from named sources, dated.** A competitor's own claim proves only that it said it. A vendor-authored comparison is opinion.
- **Our side comes only from permitted and approved claims.** Anything else is `[NEEDS PROOF]` and goes to `proof-points`.
- **An unsourced weakness is a question, never a statement.** Absence is "no public evidence of X".
- **Delta, not rebuild.** Carry unchanged lines forward with their original date. "As of" is the date a source was read, not proof the fact is still true.
- **One data point is a note.** A pattern needs n of 2 or more before it becomes a "where they win".
- **Propose, never push.** Brain writes need exact text and a yes, append only, Section 3 only. A confirmed value is never overwritten.
- **Pulled facts are drafts.** Tag category, tool and date; connectors are read-only; nothing is written to an external tool.
- **Scheduled runs are read-only for the brain.** They save records and a status board, nothing else.
- **Always offer the schedule.** A profile that is not refreshed decays quietly.

## Quality Gate

Runs after the profiles are built, before saving. Surface failures before saving, never after.

| Check | Standard | Pass = |
|---|---|---|
| Roster capped | Five competitors or fewer, none invented | Yes |
| Claims tagged and dated | Every line has a tag and an "as of"; "re-check" past its window | Yes |
| Delta honest | Unchanged lines carry their original date; only stale or signalled lines were re-read | Yes |
| Weakness sourced | No unsourced weakness stated as fact; no roadmap shown as capability | Yes |
| Constraints checked | Section 6 `forbidden_claims` and Section 8 `prohibited` tested, result shown | Yes |
| Write-back honest | Brain note shown as exact text and confirmed, or "none proposed"; none from an unattended run | Yes |
| Schedule proposed | Offered once with the task named, or already in place | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

## Gotchas

- **Re-reading is not refreshing.** A page that did not change gives the same fact and the same date; do not move the date forward.
- **Roster drift is silent.** Sellers keep using a card for a competitor that no longer shows in deals. The `roster` check exists for that.
- **A competitor's customer is not your proof.** A logo both vendors serve is not a win; keep it out of the profile's "where we win".
- **Pricing is the shortest-lived line.** A list price is indicative unless the page says otherwise; custom pricing is quoted by sales. Its window is 60 days.
- **A past-dated roadmap item is a rumor.** Record it as unconfirmed and never as a capability.
- **A scheduled run cannot ask.** If a source is missing, it records the gap in the status board and moves on.
