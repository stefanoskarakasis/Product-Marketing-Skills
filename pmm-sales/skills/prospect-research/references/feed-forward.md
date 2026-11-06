# Feed-Forward: What Other Skills Learn From Prospects

Read at Step 11. Prospect-research sees where buyers are in motion and what actually gets a reply, so it is the cheapest honest source of trigger evidence. It never writes the brain. It logs, counts and proposes. The same columns are used by `customer-context`, so a later win/loss skill can read both.

## Mechanism

1. Each run appends rows to `/context/prospects/_patterns.md` with the shared columns: `date | slug | type | segment | role | observation | count`. `type` is the pattern type (for example `signal:hiring-spike`, `tool:incumbent`, `status-quo`, `angle`). No contact names, no quotes tied to a person, no deal amounts.
2. A `log:` line appends to `_outcomes.md` (`signals.md` section 5). Outcomes are counted per signal type, per segment and per angle.
3. A pattern is proposed only when it reaches the n below inside 180 days. One account stays a note. The n values are defaults; change them in `_config.md`.
4. A proposal is shown as exact text with the receiving skill named. The user confirms, then runs the receiving skill with that text. Unattended runs log and propose nothing.
5. The Learning Close row lets `meta-synthesis` see which proposals were accepted.
6. v1 records outcomes but does not compute hit rates. Proposals that depend on outcomes appear only once the log holds enough rows, which takes weeks of real use.

## Targets

| What the run observed | n needed | Proposed to | Receiving skill does |
|---|---|---|---|
| A signal type that preceded a booked meeting, stated as something a seller can see | 3 outcomes | `product-marketing-context` | Adds to Section 2 `triggers` after the user's yes |
| A prospect's own public words for the problem, verbatim, with source and date | 1 | `positioning-messaging` (as input, not a brain write) | Reads it beside customer language |
| A tool, DIY process or status quo seen at prospects and not in Section 3 | 2 accounts | `alternatives-map` | Adds it with evidence |
| A competitor installed or named at a prospect, with the role | 2 accounts | `competitive-profile` (`intake`) | Drafts one change for the approver; a tool seen at 3 accounts is raised as a roster candidate |
| An incumbent present at a prospect | 1 | `competitive-battlecard` | Hand-off only; the seller decides |
| Strong-fit accounts that never reply, or anti-persona accounts that do | 5 outcomes | `ideal-customer-profile` (audit) | Pressure-tests the ICP with outcome evidence |
| A segment with a reply or meeting rate | 10 outcomes per segment | `beachhead-segment` | Evidence for Winnability |
| Titles that appear as buyers, and committee size seen | 3 accounts | `buyer-personas`, `stakeholder-maps` | Updates `committee_roles` defaults |
| A hypothesis worth testing on about ten accounts | 1 | `experiment-doc` | Turns it into an experiment |
| An angle that got replies | 3 outcomes | `positioning-messaging` | Message-test input |

## Rules

- Prospect language is an exact quote from a public source, or it is not stored.
- A metric from a prospect's public statement is never used as proof of ours. Proof comes only from `proof-points` as approved.
- A proposal that conflicts with a confirmed brain value is shown as a question with both values.
- Nothing here changes a signal window or a threshold; the user edits them in `_signals.md` and `_config.md`, or `meta-synthesis` proposes it.
- Nothing is sent to the prospect, and no prospect is added to a CRM or a sequence by this skill.
