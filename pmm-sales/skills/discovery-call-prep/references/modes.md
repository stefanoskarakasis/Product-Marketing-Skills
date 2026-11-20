# Modes

## prep (default)

One company, one buyer title. Runs Steps 1 to 12. This mode owns call prep for the whole pre-close life of an account: a first discovery call, a follow-up discovery call and a call on an open deal. Call type is decided at Pre-flight from the CRM stage and the last record.

### Open-deal short form (taken over from `deal-review`)

An open opportunity with a `deal-review` record, or a CRM stage at or past evaluation, gets the short form instead of the seven stages. It reads the deal's last record and `_gaps.md` and returns, under 150 words in Slack:

1. **Objective** of this call, one line.
2. **The gap to close**: the evidence the last review marked `not found` or `stated`, the most costly first.
3. **Three questions** in the order to ask them, chosen from `questions.md` by that gap (value and senior backing first).
4. **The likeliest objection**: Section 3 `objections` and the `objection-handling` ledger for this segment; if one matches, name the card and hand off.
5. **What a good call changes**: the evidence that would move from `stated` to `validated`.

It never produces a verdict. For "is this deal real" it hands off to `deal-review`. Slack uses the short form in `references/formats.md` and closes on "did the gap close?" (not the discovery question).

## next

A follow-up discovery call. Reads the last plan in `/context/discovery/`, what was confirmed or corrected (a pasted transcript or notes counts as a debrief), and the stages not yet earned. Output: what changed since the last call; the corrected hypothesis; stages 4 to 7 that are now earned, with questions that build on the buyer's own words; the second thread to bring in (Q-06). No prior record: say "no earlier plan" and run `prep` with the notes.

## log:

`log: confirmed`, `log: changed: [their priority in a few words]`, `log: not a fit: [reason]`, `log: booked next call`, `log: no show`. For an open-deal short form: `log: gap closed`, `log: gap partly closed`, `log: gap open`. Followed by the company if more than one record is open.

Nothing requires the seller to type this. In Slack, the plan ends on a plain question ("How did the call go: priority confirmed, changed, or not a fit?") and the reply logs it. A transcript pasted afterwards is read as the debrief and graded the same way. Grade and write with `references/feed-forward.md`.

## sweep

Runs only after the owner has approved reading `~~call recordings` and `~~CRM` outcomes (`references/connectors.md`). Reads new transcripts for open records whose call date has passed, joins the calendar for a follow-up booked (weak signal), proposes a grade for each (priority confirmed, changed, not a fit; which questions were asked; which unlocked evidence), and writes them as `transcript-read`. A seller's own reply, if one exists, overrides the sweep. Unattended: log and grade only, propose nothing, never in a seller's thread.

Join to outcomes: for each open record, read the CRM opportunity by account slug (read-only) and write `opp_created`, `stage` and, when closed, `won` or `lost` to `_outcomes.md`. Never write to the CRM.

## library

For the owner of discovery knowledge. Shows `_library.md` (the question bank, tailored): each question with times planned, times asked, times it unlocked evidence, and times it fell flat; rates only at 10 or more asks, counts below. Reads `/context/discovery/_reviews.md` counts (from `discovery-call-scoring`) to name the stage most often Needs Work, so the owner can strengthen the questions for it. Lists stale questions (not planned in 180 days), questions that never unlock, questions that mention a product or feature (a violation), and proposed rewrites. Edits to the library are the owner's: the skill proposes, the owner says yes, then it writes `_library.md`. A seller's own card is `proposed` until the owner clears it.

A tailored library holds three questions at most per card slot (have it, roadmap, workaround is the objection library's rule; here: question, why it is asked, what to listen for).

## Files in /context/discovery/

| File | Holds |
|---|---|
| `<slug>-YYYY-MM-DD-HHMM.md` | A plan, dated, append-only, header with `hypothesis_id`, `call_type`, `minutes`, `valid_until`, `retain_until`, `emea_mode`, `outcome: open` |
| `_config.md` | `emea_mode`, `home_region`, `default_minutes` (30), `stale_days` (365 company, 90 hiring), `approver`, `brain_source`, `usage_identity`, `retain_days` (180), `data_access` (calls and CRM outcomes: role and date of the owner's decision), `recording_folder` (where Meet, Zoom or Teams transcripts land, if no recorder connector). Defaults are labelled and editable |
| `_questions.md` | One row per question per plan: id, stage, role family, planned, asked, unlocked, source (`seller-reported` or `transcript-read`) |
| `_patterns.md` | Logged runs: date, slug, segment, role family, lead signal type, call type |
| `_outcomes.md` | `log:` and sweep outcomes, with the CRM join |
| `_library.md` | The tailored question bank, seeded from `questions.md` on first `library` |
