# Feed-Forward and Learning

Read at Steps 3, 10, 11 and 12. Propose-only: log, count, propose. Nothing writes the brain or another skill. The skill gets smarter in two ways: it learns from its own graded plans, and it reads what sibling skills have already learned.

## 1. Outcome log (no typing required)

Every plan saves a record with `outcome: open`. Closure comes from, in order of strength:

1. **CRM join** (read-only, after the owner approves outcomes): the opportunity for the account slug: created, stage, won or lost.
2. **Transcript read** (`sweep`, after approval): the call graded from the transcript.
3. **Seller reply** to the plain closing question, or `log:`: seller-reported.

A grade is `seller-reported`, `transcript-read`, `crm` or `calendar`. A `calendar` grade is weak and never alone sets "priority confirmed": a follow-up with the same account domain booked within 14 days reads "advanced"; none within 30 days reads "stalled". A seller-reported grade is labelled so; where sources disagree, show both and prefer the transcript.

| Field | Values |
|---|---|
| `priority` | `confirmed` (the lead hypothesis held, in the buyer's words), `changed` (a different priority, recorded in a few words), `not a fit`, `not asked` |
| `pov_hit` | `yes` (confirmed), `partial` (changed but related to the same pain), `no` |
| `dq` | `yes` with reason, or `no`. A fast, correct disqualify counts as a good outcome |
| `gap` | Open-deal short form only: `closed`, `partly`, `open`. Counted per gap type and handed to `deal-review` `_gaps.md` as a read, never written there |
| `next_step` | `booked` with date, or `none` |
| `questions` | per id: `asked`, and `unlocked` (the buyer gave a number, an owner, a consequence or a requirement the plan lacked), or `flat` |
| `opp` | `created`, `stage`, `won`, `lost` with reason (from the CRM) |

## 2. What it records

1. Each run appends `_patterns.md`: date, slug, segment, role family, lead signal type, call type. No names, amounts or quotes.
2. Each graded plan appends `_questions.md` rows and `_outcomes.md`.
3. Hit rates show only at 10 or more plans; below that, counts. A rate is shown per signal type, per question id and per stage, never per seller.
4. Rows older than `retain_days` roll into a one-line summary in the weekly `meta-synthesis` sweep. A question that has not been planned in 180 days is flagged stale in `library`, not deleted.

## 3. Learned from siblings (read-only; each named on the "Learned from" line with skill and date)

| Skill | Reads | Changes |
|---|---|---|
| `prospect-research` | The account's record and `_signals.md` hit and miss counts by signal type; `_outcomes.md` | Which signal types to trust when ranking the lead hypothesis; the account's timing |
| `deal-review` | `_gaps.md` and `_patterns.md` for the segment: which gap most often caused a stall or a loss | The question added to stage 4, 6 or 7 for that gap; the open-deal short form's gap |
| `objection-handling` | `_ledger.md`: top objections by segment, role and stage | The "likeliest objection" line and a stage-7 question that surfaces it early; the approved card is named, never improvised |
| `customer-context` | `_patterns.md` and won-deal baselines for the segment | Hypothesis candidates from what similar won customers prioritised (counted at 3 or more) |
| `competitive-battlecard`, `competitive-profile`, alternatives (Section 3) | Sourced edges, the rival's current profile, `_outcomes.md` | "Where we are different, in their words" |
| `product-marketing-context` | Sections 1, 2, 3, 4, 6, 8 | Language (`customer_phrases`), pains, disqualifiers, approved proof, who owns discovery knowledge |
| `meta-synthesis` | The promotion queue, quiet-skill list | Whether this skill is unused: it is registered in `/context/learning-sources.md` |

A learned item shapes ranking and wording. It never becomes proof, never overrides a confirmed brain value, and a conflict is shown as a question with both values.

## 4. Proposals (counted as distinct plans inside 180 days; exact text plus the receiving skill)

| Observed | n | Proposed to |
|---|---|---|
| A signal type that led to a confirmed priority, or to none | 5 | `prospect-research` `_signals.md` |
| A question that unlocked evidence the plan lacked | 3 | `product-messaging-playbook` (discovery questions) |
| A priority stated in the buyer's words | 1 | `product-marketing-context` (`customer_phrases`) |
| A role's dreaded email confirmed or corrected, by role | 3 | `buyer-personas` |
| A disqualify reason that repeats | 5 | `ideal-customer-profile` (audit) |
| A required capability buyers set that matches a sourced edge | 3 | `competitive-battlecard` (field note) |
| An alternative or DIY build the buyer named that is not in Section 3 | 2 | `alternatives-map` |
| A competitor the buyer named, with stage and role | 2 | `competitive-profile` (`intake`) |
| A stage where calls stall | 3 | `product-messaging-playbook`, `positioning-messaging` |
| A buyer-dated event before an opportunity | 3 | `product-marketing-context` (`triggers`), `market-context` |
| A discovery to won-or-lost pattern by segment | 10 per segment | `win-loss-analysis`, `beachhead-segment` |
| A hypothesis worth testing on about ten plans | 1 | `experiment-doc` |
| An objection raised in discovery | 2 | `objection-handling` (ledger hand-off) |
| A call length that converts differently | 10 | `library` (owner) |
| Ledger rows | n/a | `meta-synthesis` via `/context/learning-sources.md` |

Rules: a proposal that conflicts with a confirmed brain value is a question, not a replacement. Unattended runs log and propose nothing. Never in a seller's thread: proposals go to the owner. The approver says yes, then runs the receiving skill. The discovery-question row is produced here; `deal-review` hands that row off.

## 5. Owner

Section 8 `context_owners` names who owns discovery knowledge. Missing or older than 90 days: ask once, after the first plan, "Which team owns discovery knowledge here, and who is the backup role?" Roles only. The owner approves proposals, clears a seller's own question into the library and decides data access. Offer a weekly reminder only if an owner is confirmed, and create it only after a yes.

## 6. Digest and sweep

`sales-research-digest` reads `_outcomes.md` and `_questions.md` for a "Discovery" section: plans made, priority-confirmed rate, fast-disqualify rate, calls that became an opportunity, the three questions that unlock most, the stage where calls stall. Rates only at 10 or more; otherwise counts and "not enough data". No seller-level view. With no CRM, the digest shows "Outcomes blind" and pushes to connect one.
