# Method

Read before every run. Output says each check in plain words and never names a framework.

## Scope

`my`: the asker's open deals (CRM owner is the asker). `team`: open deals whose owner reports to the asker, or the owners named in `_config.md`. A CSV or paste is the scope as given. Closed deals are out. Deals only: no seller name, no per-seller count and no ranking of people in any output. Owner shows as a role.

## Thresholds

Order: brain Section 2 `sales_cycle` for the deal's segment if under 180 days old; else the CRM; else ask once. The segment comes from the CRM field named in `_config.md` as `crm_segment_field`; ask once which field it is.

- `stale_days` = cycle ÷ 6, no lower than 14 and no higher than 60. `quiet_days` = half of `stale_days`.
- With stage history, read the median days in each stage for won deals of the same segment over 12 to 18 months and say so. A stage older than 1.2× its median reads "slow for this stage", 1.4× "stalled for this stage".
- No stage history: a deal older than 1.5× the cycle reads "older than your usual cycle", 2× "stagnant".
- These ratios are defaults from vendor sources: label them as such. Unanswered: 30 and 14 days, labelled "defaults, cycle unknown".
- When the CRM median differs from the brain value by more than 25%, say so in one line and propose the new value to the approver for `ideal-customer-profile` to write. Never write it.

## Checks

Each check is a count of deals, "x of N". A share shows only at 10 or more deals.

| Icon | Check | Counts a deal when |
|---|---|---|
| 📅 | Close date passed | Open and the close date is before today |
| 🕰️ | Quiet | No activity for `quiet_days` or more |
| 🐌 | Slow in stage | Older than 1.2× the stage median |
| 👤 | Only one person | One contact role on the deal |
| 📝 | Next Step empty | The Next Step field is blank |

Activity is the CRM's last activity date plus the latest logged task or event. Call, email and calendar tools add dates only where connected; otherwise write "not queried". A meeting counts as booked only when a future-dated event is on the deal or its account.

## Missing fields

A check needs a field. If the field is blank, the deal is "not checked" for that check and the question goes to the deal owner. The skill never reads a blank as a pass or fills it from memory.

| Field | Needed for | Question to the owner |
|---|---|---|
| Contact role | Only one person | Who is the main contact, and what is their role in the decision? |
| Amount | Size band, forecast | What is the expected amount? |
| Stage history | Slow in stage | Cannot be asked: say "not checked" |
| Close date | Past due | Required in Salesforce; in a CSV or other CRM, ask |
| Segment | Thresholds | Ask once, in `_config.md` |

If every deal in scope lacks the same field, ask the approver once ("none of your N deals has a contact role: is the field used?") and do not draft a DM per deal. The check stays off until answered.

## CRM fields to fix

Counts by field, per deal, with the exact field name as the CRM shows it: Next Step empty, Amount empty or zero, no contact role, close date moved twice or more in 60 days, an early stage held more than 30 days (Discovery or the first stage), close date more than 90 days away with no update. The skill never edits the CRM. Show "issues on N deals", where the issue total and deal total are both counted.

## Dead weight

A deal with no activity for `stale_days` or more and no future-dated meeting is named a **candidate** for closing, with the days and the reason. Name it; never close it. Say that "no meeting booked" means no meeting in the sources read.

## Five deals

Rank by where attention changes the outcome, not by size: a buyer-dated event within 14 days, a close date inside 14 days with an empty Next Step, a close date passed, quiet or slow deals with one person, then the rest. A buyer-dated event is a date the buyer gave (board date, renewal, launch, audit). Quarter end is not one. Never invent urgency. Fewer than five qualify: list them and say so; none: "nothing needs attention".

Each deal: icon flags, stage and segment, why it is here (one fact per line), owner as a role, one action starting with a verb, a date, and "Watch out" (one line). Source in words, then one short link from the connector ("Open in Salesforce"). Never guess a URL.

## Evidence words

Mark each claim by its source: `CRM` (a field), `activity` (a dated task or event) or `not found in [sources]`. A claim only the seller wrote in a CRM text field is a claim, not evidence. Absence is stated only for sources queried.

## Since last digest

Count deals created, won, lost, moved forward, moved back and with close dates moved later, from stage and date history. Check that open then plus created minus closed equals open now; if it does not, say the difference and its likely cause (a deal reopened or reassigned). No earlier digest: say "no earlier digest" and skip the section.

## Carried actions

Read last digest's five actions. A deal with new activity after its date is shown "done (my reading from activity)"; otherwise "still open". Open ones are listed first.

## Reading the evidence, not forecasting

A digest never gives a probability, a forecast number or a sum of amounts. It ends "A read of the evidence, not a forecast."

## Boundaries and ties

- **Rounding:** keep half days as they are (7.5 means 8 days or more). Never round a threshold to change a count.
- **Exactly on the line:** "older than" and "slower than" are strict (greater than); "no activity for N days or more" is inclusive. A deal exactly on a strict line is not counted; say so under "borderline, not counted".
- **Only the current stage date:** run slow-in-stage from the age in the current stage and say so under "How sure I am". Without that date, mark the check ➖ not checked.
- **A buyer date only the seller wrote** (a Next Step like "board signs Thu") may open the list only if the deal also has a second signal; otherwise it ranks below a close date that has passed.
- **Ties inside a tier:** rank by days since the close date passed, then days of silence, then the number of weak fields. A sixth deal with the same flag goes in one line "Not in the five, but the same flag".
- **Owner title unknown:** write "deal owner" with the segment and ask once for titles. Never put a seller's name in the digest or in a heading.
- **Zero is missing** for Amount.
