# Modes

## weekly (default)

The whole open pipeline in scope against the last digest. Delivery: a Slack card in the thread you asked in, the full digest saved to `/context/pipeline/`, an optional Doc copy (ask before saving to Drive). Weekly, scheduled once the user approves it, or on request; offer once, in one line: "Want this every Monday?". On a yes, create the scheduled task with `scope`, `digest_channel` and the day, and say so.

Unattended: save the file, post the summary to `digest_channel`, draft DMs and send none, propose nothing, write nothing but `/context/pipeline/` and `/context/skill-sessions.md`. A quiet week says "nothing needs attention", the counts and the CRM fields to fix. A rerun on the same day reads the saved digest, posts nothing twice and drafts no DM for a field already asked in the last 7 days (`_gaps.md`). Stop: no CRM answer and no paste means the run says so and ends.

This mode owns the weekly list of deals that need attention. It was `queue` in `deal-review`.

## hygiene

The CRM-fields section only (`method.md`): counts by field, then the deals, each with the exact field to fix. Never edits the CRM. Missing fields become questions and drafted DMs as in `weekly`. Ends with the one field that clears the most issues if fixed.

## forecast

Prepares a forecast call. For each open deal in the forecast categories the CRM uses for commit and best case (read the live labels; ask once if unclear): the evidence behind its category in dated words (`CRM` or `activity`), each place the category is stronger than the activity, and the one question a manager would ask. A deal whose category is stronger than its evidence reads "category looks high: ask the owner why". No probability, no sum of amounts, no forecast number. Deals only. Amounts stay in the CRM. Ends "A read of the evidence, not a forecast."

## since [date]

What changed between a date (default: the last digest) and now: created, won, lost, moved forward, moved back, close dates moved later, and which of last digest's actions look done. No earlier digest: "no earlier digest" and a short weekly.

## log:

`log: won`, `log: lost: no budget`, `log: stalled`, then a deal. Append `_outcomes.md` (date, deal slug, segment, stage, outcome, labelled seller-reported). Does not grade a verdict, because the digest gives none.

## Files in /context/pipeline/

| File | Holds |
|---|---|
| `<YYYY-MM-DD-HHMM>.md` | A digest, dated, append-only, with `retain_until` |
| `_config.md` | `scope`, `crm_scope`, `crm_segment_field`, `sales_cycle` (days per segment, asked), `stale_days` and `quiet_days` (from the cycle; 30 and 14 if unknown), `emea_mode`, `home_region`, `approver`, `brain_source`, `digest_channel`, `retain_days` (180). Defaults are labelled and editable |
| `_patterns.md` | Appended by weekly and since runs: date, deal slug, segment, stage, flags. No names, amounts or quotes |
| `_gaps.md` | Missing-field questions asked, and how many were filled by the next run, by field |
| `_outcomes.md` | `log:` outcomes, seller-reported |
