---
name: signal-monitor
version: 1.0.2
description: >
  Turns the signals you name into at most five opportunities, each tied to a brain field
  and a Section 7 priority, with evidence, a confidence label and one suggested next move;
  it never edits your brain. Trigger on: "what changed this week", "weekly opportunities",
  "signal monitor", "what should we act on", "competitor moves this week", "scan these
  signals". Related: alternatives-map, positioning-messaging, pmm-okrs,
  workflow-orchestrator.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-12
---

# Signal Monitor

Most weekly "market scans" produce a long list and no decision. This skill does the opposite. It reads only the signals you name, throws away anything that touches nothing in your brain, and returns at most five opportunities, each tied to a brain field and to what you said matters this quarter.

## Trigger

- **When:** A weekly or ad hoc read on what changed (competitor pages, search and traffic shifts, win/loss notes, news you paste) and what to do about it.
- **Not for:** A competitor battlecard for a live deal → `competitive-battlecard`. Keeping five competitor profiles current → `competitive-profile` (it reads your saved lists). Running a multi-skill program → `workflow-orchestrator`. Re-mapping alternatives → `alternatives-map`. Rewriting positioning → `positioning-messaging`. Setting quarterly goals → `pmm-okrs`.
- **Example prompts:**
  - "Here is what changed on two competitor pricing pages: [paste]. What matters for us?"
  - "Weekly opportunities, please."
  - "Use my connectors for this week's search and traffic shifts."
  - "We lost three deals to the same competitor. What should we do?" (edge: win/loss notes only)
  - "Scan the whole internet for anything about us." (edge: declined; it reads only sources you name)

## Inputs

- **Args:** The signals, named by you: pasted text, files, URLs you list, or "use my connectors". Optional: the period covered (default: the last 7 days) and the quarter's priority if the brain has none.
- **Defaults:** Max five opportunities. Period: 7 days. Sources: only those named in this run.
- **Context keys:** `/foundation/brain.md` (optional), `/foundation/me.md` (optional, format and detail only), `/context/signals/` (earlier runs), `~~market data`, `~~SEO`, `~~company data`, `~~web research`, pasted material.
  - **Brain contract:** Reads: Section 2 (who matters), 3 (alternatives, positioning), 5 (market context), 6 (approved proof), 7 (priorities), 8 (prohibited). Writes: none. Never writes to: Sections 1 to 8. A suggested brain change is handed to `product-marketing-context`.

## Pre-flight

- Load the brain. Read Sections 3 and 7 first, because they decide what counts as relevant.
- **Brain absent: Quick-Brain.** Ask at most three questions and hold the answers for the session: the three alternatives buyers compare you with (including doing nothing), the one priority this quarter, and who your best-fit buyer is. Label the output as built from them. Do not write them to the brain.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if Section 7 `priorities` is empty or older than 90 days and the answer would change the ranking, ask one question: the question, one line on why it matters, "answer or skip". Answer: use it for this run and offer it as a brain update. Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run. This is the only write to `/foundation/gaps.md`.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): if `/foundation/me.md` exists, read it for format and detail only. Never take a company fact from it.
- Read earlier files in `/context/signals/` to avoid repeating an opportunity already listed in the last four runs. A repeat is shown only if the evidence changed.
- If you named no source and have no connector, ask for signals. Do not search on your own.

## Steps

### Step 1: Name the sources

List the sources you will read this run, back to the user in one line, and confirm. Sources are only what the user pasted, uploaded, listed as URLs, or pulled through `~~market data`, `~~SEO`, `~~company data` or `~~web research`. If a URL cannot be read, say so and ask for the text. Never fill a gap from memory.

### Step 2: Extract signals

Pull atomic signals: one change per item, with source, date and a quote or figure. Drop greetings, opinion with no owner, and anything older than the period unless it explains a recent change. Connector pulls are drafts and are tagged with category, tool and date. Leave out names, emails and phone numbers of individuals.

### Step 3: Match to the brain

For each signal, find the brain field it touches (for example: a competitor repackages, which touches Section 3 `alternatives`; a rising query, which touches Section 5 `why_now`). A signal that touches no field is dropped and counted. Say how many were dropped; do not list them.

If a signal contradicts a value the user confirmed in the brain, show both and ask. Do not call either one wrong.

### Step 4: Rank

Rank what is left: the Section 7 priority it serves first (a signal that serves none is capped at `medium`), then confidence, then recency. Confidence rules are in `references/signal-format.md`. Cut to five. Say how many were cut.

### Step 5: Shape each opportunity

For each of the top five, fill the block in `references/signal-format.md`: signal, evidence with tag, brain field, priority served, confidence with a one-line reason, one suggested next move with an owner role, and a brain change to consider if there is one. Check each against Section 8 `prohibited`: a suggested move that runs into a prohibited item is shown with that conflict and not recommended.

### Step 6: Gate your own list

Run the Quality Gate before showing the list. Fix what the evidence allows; drop an opportunity that cannot pass. Show the score and the failed rows only.

### Step 7: Save and hand off

Write the list to `/context/signals/YYYY-MM-DD.md` (never overwrite a file). If files cannot be written, show the file and say it was not saved. Offer, never perform: `alternatives-map` for an alternatives change, `positioning-messaging` for a messaging change, `pmm-okrs` for a goal change, `product-marketing-context` for a brain update. Name only skills from `.claude-plugin/next-skill-map.md`.

### Step 8: Learning Close

Append to `/context/skill-sessions.md` (create it if missing), in the format of `product-marketing-context/.claude-plugin/skill-sessions-format.md`. Write it directly, without asking.

```yaml
type: execution
skill: signal-monitor
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement, or "none"]
source: [surprised / wrong / missing / N/A]
```

## Outputs

- **Files written:** `/context/signals/YYYY-MM-DD.md` (the list), `/context/skill-sessions.md` (one entry per session). Possibly one appended `skipped` block in `/foundation/gaps.md`.
- **Chat output format:**

```
# Signals — [date]
Sources: [list] · Dropped: [n] · Cut: [n]
## O-1 [title]
Signal · Evidence [tag] · Brain field · Priority served · Confidence · Next move · Brain change to consider
... (max 5)
Gate: n of 6 · open questions
```

- **External side effects:** None. It reads what you name and writes the two files above.

## Verification

- At most five opportunities, each with evidence that has a source and a date.
- Every opportunity names a brain field; none is listed that touches no field.
- `high` confidence appears only with two independent sources.
- Nothing in the list came from a source the user did not name in this run.
- No claim from a company's own marketing is presented as proven.
- The brain was not written; the session log has a new entry.

## Do Not Use For

- **`workflow-orchestrator`**: a multi-skill program such as a launch or a quarterly cycle.
- **`alternatives-map`**: building or refreshing the map of alternatives.
- **`positioning-messaging`**: writing or auditing positioning.
- **`pmm-okrs`**: turning priorities into OKRs.

---

## Operating Rules

- **Read only what the user names.** Open-ended scanning produces noise and unverifiable claims.
- **No evidence, no opportunity.** Each item carries a source, a date and a quote or figure.
- **Five at most.** A longer list is a reading list, not a decision.
- **No brain field, no item.** A signal that touches nothing in the brain is dropped and counted.
- **One source is at most medium.** High needs two independent sources.
- **A company's own claims prove only that it said them.** Website copy and press lines are never proof.
- **Never write the brain.** Suggest, then hand off. A confirmed value is never called wrong; show both and ask.
- **Pulled facts are drafts.** Tag category, tool and date, and treat them as unverified until the user confirms.
- **Store no personal data.** Roles and company names only.

## Quality Gate

Runs before the list is shown.

| Check | Standard | Pass = |
|---|---|---|
| Five or fewer | Count of opportunities | 5 or fewer |
| Evidence complete | Source, date and quote or figure on each | Yes |
| Brain field named | Each item names a section and field key | Yes |
| Confidence honest | `high` only with two independent sources | Yes |
| Prohibited items respected | No recommended move conflicts with Section 8 `prohibited` | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new entry | Yes |
