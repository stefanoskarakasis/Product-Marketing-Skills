# Feed-Forward and Learning

Read at Steps 2, 8, 9 and 10. Propose-only: log, count, propose. Nothing writes the brain or another skill. The skill gets smarter two ways: it grades its own assets from what happened next, and it reads what sibling skills have learned.

## 1. Asset registry (no typing required)

Every asset adds a row to `/context/enablement/_assets.md`: id, type, audience, stage, date, and the claims it relies on (a Section 6 id, a rival fact with its date, an objection card id, a price, a number). Outcome comes from, in order of strength:

1. **CRM** (read-only, after the owner approves): the opportunity stage in the 30 days after the asset.
2. **Calendar:** a follow-up with the account booked within 14 days reads "advanced"; none within 30 reads "stalled". Weak; never alone.
3. **Seller reply** to the closing question, or `log: sent`: seller-reported, labelled so.

## 2. What it records

Per asset: date, type, audience, stage, claims used, outcome grade. No names, amounts or quotes tied to a person. Rates show only at 10 or more assets; below that, counts. By asset type, stage and segment, never per seller. Rows older than `retain_days` roll into a one-line summary in the weekly `meta-synthesis` sweep.

## 3. Learned from siblings (read-only, each named with skill and date)

| Skill | Reads | Changes |
|---|---|---|
| `objection-handling` | `_ledger.md`, approved fixes | The objection a one-pager or proposal must answer first |
| `competitive-battlecard`, `competitive-profile` | Sourced edges and dated facts | Rival claims in a leave-behind; stale ones are flagged |
| `deal-review` | `_gaps.md`, `_patterns.md` | Which gap to address in a script or proposal |
| `discovery-call-prep`, `discovery-call-scoring` | `_outcomes.md`, `_reviews.md` counts | Which discovery evidence to carry into the demo and proposal |
| `customer-stories` | Approved stories | The proof in an asset |
| `proof-points`, `product-marketing-context` | Section 6, Sections 1 to 4 and 8 | Claims, language, forbidden claims, owner |

A learned item shapes ranking and wording. It never becomes proof, never overrides a confirmed brain value, and a conflict is shown as a question with both values.

## 4. Proposals (distinct deals or assets inside 180 days; exact text and receiver)

| Observed | n | Proposed to |
|---|---|---|
| A win-loss reason repeated against one rival | 5 | `competitive-battlecard` (field note) |
| A loss reason that is an unanswered objection | 3 | `objection-handling` |
| A stage where deals stall | 3 | `discovery-call-prep`, `product-messaging-playbook` |
| An asset whose source changed or aged past `stale_days` | 1 | The owner of that source |
| A pain buyers name that the brain lacks | 3 | `ideal-customer-profile` (audit) |
| A buyer phrase that repeats | 3 | `product-marketing-context` (`customer_phrases`) |

## 5. Stale sweep

`sweep` lists assets whose source changed (a Section 6 entry, a price, an objection card) or whose rival facts passed `stale_days` (default 90, my default, the PMM changes it). It proposes a refresh and never edits an asset. Anti-bloat: the v1.21.0 retire and archive rule applies.
