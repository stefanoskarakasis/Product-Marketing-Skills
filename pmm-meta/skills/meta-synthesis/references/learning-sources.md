# Learning Sources: the ledgers meta-synthesis reads

Read at Step 0 and Step 1. Skills already write their own ledgers. This file maps each one to four common fields, so meta-synthesis can count across plugins without changing any skill. The registry the user owns is `/context/learning-sources.md`; create it from the table below if it is missing, and keep rows only for skills that are installed.

## The four common fields

| Field | Meaning |
|---|---|
| `date` | When the row happened |
| `subject` | The thing it is about: a competitor, a company slug, a signal type. Roles and slugs only, never a person's name |
| `result` | What happened: won, lost, no decision, meeting booked, no reply, graded right, graded wrong, open |
| `kind` | The ledger it came from |

## Known ledgers

| Ledger | Written by | Date | Subject | Result |
|---|---|---|---|---|
| `/context/skill-sessions.md` | every execution skill | `session_date` | `skill` | `pattern` (free text) |
| `/context/battlecards/_outcomes.md` | `competitive-battlecard` | `date` | `competitor` | `result` |
| `/context/prospects/_outcomes.md` | `prospect-research` | `date` | signal types and `segment` | the `log:` outcome |
| `/context/prospects/_patterns.md` | `prospect-research` | `date` | `type` | `observation` and `count` |
| `/context/deals/_outcomes.md` | `deal-review` | `date` | stage and `segment` | the `log:` outcome |
| `/context/deals/_patterns.md` | `deal-review` | `date` | `type` | `observation` and `count` |
| `/context/deals/_gaps.md` | `deal-review` | `date` | gap `type` | gap and `count` |
| `/context/pipeline/_patterns.md` | `pipeline-digest` | `date` | `segment` and stage | flags and `count` (by deal; no seller field) |
| `/context/pipeline/_gaps.md` | `pipeline-digest` | `date` | CRM field | asked and filled (counts only) |
| `/context/pipeline/_outcomes.md` | `pipeline-digest` | `date` | stage and `segment` | the `log:` outcome (seller-reported) |
| `/context/objections/_ledger.md` | `objection-handling` | `date` | `card ID` and `segment` | `outcome` (from the CRM, read-only) |
| `/context/discovery/_outcomes.md` | `discovery-call-prep` | `date` | `slug` and `segment` | `outcome` (graded from calls, CRM and calendar, read-only) |
| `/context/discovery/_questions.md` | `discovery-call-prep` | `date` | `question id` | `asked` and `unlocked` |
| `/context/discovery/_reviews.md` | `discovery-call-scoring` | `date` | `role_family` and `pattern` | stage marks (counts only; no seller field) |
| `/context/enablement/_assets.md` | `sales-collateral` | `date` | `asset type` and `audience` | `outcome` (graded from CRM, calendar and the closing reply, read-only) |
| `/context/enablement/_winloss.md` | `sales-collateral` | `date` | `rival` and `segment` | reason code and `count` (by deal; no seller field) |
| `/context/prospects/_usage.md` | `prospect-research` | `date` | `surface` | `verdict` |
| `/context/customers/_patterns.md` | `customer-context` | `date` | `type` | `observation` and `count` |
| `/context/digests/*-sales.md` | `sales-research-digest` | report date | the week | actions proposed and answered |
| `/context/briefings/_ledger.md` | `competitive-briefing` | call date | the call | graded right or wrong |
| `/context/briefings/_decisions.md` | `competitive-briefing` | `asked` date | the decision | open or closed |

A skill added later can join by writing one row to the registry. Nothing else changes.

## Standard row for a new ledger

`date | subject | result | note`, append-only, one row per event, roles and slugs only, `note` 20 words or fewer. Existing ledgers keep their own columns; the table above is the adapter.

## Counting rules

1. Count distinct accounts, deals or sessions, not rows. Two rows from one account are one.
2. A seller-reported outcome is labelled seller-reported and never presented as a measured rate.
3. A hit rate is shown only at 10 or more outcomes for that subject. Below 10, show counts only.
4. Thresholds: a guardrail may be proposed at 2 sessions or accounts (labelled "watch" until 3). A brain edit needs 3 distinct accounts, deals or outcomes.
5. A row older than 180 days is read but does not count toward a threshold.
