# Method

Read before a `review`, `since` or `prep`. Output never names a framework or a gate; say the decision in plain words.

## Evidence

Rank high to low: the buyer's own words in a dated transcript; a buyer email; a seller note; a CRM field. Each claim is `validated` (buyer-sourced), `stated` (seller or CRM only) or `not found`. Quote only an exact line from a supplied transcript, with date and role, never spliced with an ellipsis; never reconstruct or recall one. Speaker unknown: `stated`. Evidence older than `stale_days` (default 30) is marked stale and cannot raise a trajectory. Absence ("no reply", "no senior") is claimed only from queried sources: write "not found in [sources]". Quote short, with role and date. List every CRM or seller claim the calls do not back, with both sources. Notes only, no transcript or buyer email: confidence low, one assumption line, one question, and still next steps.

## Worksheet

Each box: status (`validated`, `stated`, `not found`), trajectory (up, flat, down, or new on a first run), one evidence line. Trajectory needs the last record; a first run says "new".

| Box | Validated when |
|---|---|
| Why do anything | The buyer named the problem and what doing nothing costs, with a number or consequence |
| Why us | The buyer said what we do that the alternative does not, on something they prioritised |
| Why now | A buyer-dated event pulls the deal (board date, renewal, launch, audit). Quarter end is not one |
| Who we talk to | Roles seen on calls or email; count distinct buyer roles |
| Who we should | Roles in Section 2 `committee_roles` not yet seen |
| Exec connections | One of our execs and one of theirs have spoken, or a meeting is booked |
| Senior backing | Someone senior called it a priority or owns the budget, in their words |
| Paper process | Legal, security and procurement steps named, each with an owner and a date |
| In person | Only when size or stage warrants; ask, never assume |

## Five buyer decisions

Made, shaky or not made, each as a sentence about the buyer. Check the first two before the rest; if value is unquantified or nobody senior has validated it, that is the headline whatever the CRM stage. Internal check, never named: metrics tied to the pain and to what we influence; the economic buyer engaged, not just listed; the decision process shaped by us, not just documented; criteria carrying our differentiators; the contact being developed into a champion.

1. Is the problem worth solving? "No one has said what this costs them, so there is no reason to act."
2. Is someone inside willing and able to push? "No one inside is both motivated and able."
3. Has someone senior called it a priority and put budget behind it? "Nobody senior has said so."
4. Is the upside worth the risk of changing? "The risk of switching still outweighs the gain in their mind."
5. Do they know how they would buy? "Who signs, the steps and the dates are unknown."

## Verdict and momentum

Print the verdict as exactly one of these four labels, with no qualifier added. Close-date history is listed oldest first; trend words must match the evidence shown (up, flat, down, new). Verdict, one of: qualified and progressing; qualified but stuck (wrong person); not qualified; at risk. Priority validated but access stuck means the wrong person: widen, do not walk. Momentum: improving, holding or slipping, and for how long; on a first run with no dated direction, "new". At risk beats stuck when momentum slips, a close date moved twice or the CRM overstates the calls; stuck is for holding momentum. Pushback is not evidence: change a verdict only on new evidence. A verdict is a read of the evidence, never a forecast or a probability. Close date moved, buyer silent and next step without a date all count against it.

Close every review with **Most likely reason this dies** (one line from the gaps and `_gaps.md` history) and **What would change my mind** (one observable thing).

## Champion

Motivated (a personal win), enabled (can reach senior people and budget), risk-aware (has named what could go wrong), equipped (can retell the value to others). One buyer controlling all contact is single-threaded: widen first.

## Red flags and alternatives

- No velocity: next steps slip or have no date.
- No concerns raised: usually no real consideration.
- No alternative named: the status quo is the competitor; argue the cost of inaction and the risk of change.
- DIY: argue the hidden cost and ceiling, not features.
- A named rival: tie our edge to what this buyer prioritised, then offer `competitive-battlecard`.

## Context asked, never assumed

Deal size, stage, buyer role, region and the typical sales cycle change what counts as enough evidence. The cycle varies by company, from weeks to 12 months or more, so it is learned from this company, never assumed. Order: brain Section 2 `sales_cycle` for the deal's segment if it is under 180 days old; else the CRM; else ask once. It sets what is stale or quiet. With a CRM, read the median days in stage for won deals of the same segment over 12 to 18 months and say so. Otherwise use the stated cycle: `stale_days` = cycle ÷ 6 (14 to 60), `quiet_days` = half of that. A stage older than 1.2× its median reads "slow for this stage", 1.4× "stalled for this stage". With no stage history, a deal older than 1.5× the cycle reads "older than your usual cycle", 2× "stagnant". These ratios are defaults from vendor sources, so label them as such. When the CRM median differs from the brain value by more than 25%, say so in one line and propose the new value to the approver for `ideal-customer-profile` to write; never write it. Unanswered: 30 and 14 days, labelled "defaults, cycle unknown". Missing and relevant: ask once, combined. Unanswered: mark the dependent boxes "not assessed" and say so.
