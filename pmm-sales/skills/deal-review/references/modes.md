# Modes

## since (and debrief)

Open with the last review's next steps and whether each happened. A pasted transcript is a debrief: five lines: what became validated, what slipped, the new risk, the updated next step, the date of the next touch. No prior record: say "no earlier record" and run a short review.

## ask

One question about one deal, thread-sized: the answer, its source and date, one next move.

## prep

Moved to `discovery-call-prep`, which reads this skill's last record for the open-deal short form.

## queue

Moved to `pipeline-digest`, which reads the whole open pipeline of a person or a team, lists deals only and asks for any CRM field it is missing. This skill keeps one deal.

## mine

A private mirror of the seller's own habits. Off until the seller says yes once. Then each review appends to `_mine.md` the date, deal slug and any review question left unanswered. A habit is shown to the seller, privately and in their own thread, when the same gap appears in at least three of their last five reviews. `_mine.md` is the seller's file: never read by `pipeline-digest`, `sales-research-digest`, `meta-synthesis` or any proposal, never shown in a channel, never written when the seller is unknown. Say how to delete it.

## log:

`log: won`, `log: lost: no budget`, `log: stalled`, then a deal. Append `_outcomes.md`. Grade each gap the last review named: hit if the outcome matches the gap, miss if not; update hits and total in `_gaps.md`. Show a rate only at 10 or more deals for that gap; below that, counts only. Won: offer `customer-context` with the record as its baseline.

## Files in /context/deals/

| File | Holds |
|---|---|
| `<slug>-YYYY-MM-DD-HHMM.md` | A review, dated, append-only, with `retain_until` |
| `_config.md` | `emea_mode`, `home_region`, `sales_cycle` (days per segment, asked), `stale_days` and `quiet_days` (from the cycle; 30 and 14 if unknown), `approver`, `brain_source`, `usage_identity`, `retain_days` (180). Defaults are labelled and editable |
| `_gaps.md` | Gap types, the play each triggers, hits and total |
| `_patterns.md` | Appended only by review and since (never ask). Logged runs: date, deal slug, segment, stage, gap types, play, buyer roles |
| `_outcomes.md` | `log:` outcomes |
| `_mine.md` | The seller's own, private |
