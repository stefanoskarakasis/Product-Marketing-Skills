# Feed-Forward and Learning

Read at Steps 1, 11 and 13. Propose-only: log, count, propose. Nothing writes the brain or another skill. It gets smarter two ways: from its own reviews, and from what sibling skills already learned. No seller types anything: a review is the log.

## 1. What it records

1. The seller's own `mine/` file: marks, pattern, replay moments typed, next-call moves. Read back by this skill (`trend`) and, for the seller only, by `discovery-call-prep`, which then adds a "From your last review" line to the next plan.
2. `_reviews.md`, one row per review: `date`, `slug`, `role_family`, `call_type`, `pattern`, a mark for each of the seven stages, `objection_raised` (card id or `none`), `unlocked` (question ids). No names, no quotes, no seller field.
3. Rates show at 10 or more reviews, per stage and pattern, never per seller. Rows older than `retain_days` roll into a one-line summary in the weekly `meta-synthesis` sweep.

## 2. Learned from siblings (read-only; each named on the Sources line with skill and date)

| Skill | Reads | Changes |
|---|---|---|
| `discovery-call-prep` | The plan record, `_questions.md`, `_outcomes.md` | Plan versus call; which planned questions unlocked evidence; whether the lead hypothesis was tested |
| `objection-handling` | The ledger and library | Whether an objection raised on the call is one the library covers, and the card to read |
| `deal-review` | `_gaps.md` for the segment | Which stage-gap most often precedes a stall, so the moves weight it |
| `prospect-research` | The account's record | Whether the view the seller brought matched the signals found |
| `product-marketing-context` | Sections 2, 3, 4, 6, 8 | Buyer language, approved proof for a suggested story, who owns discovery knowledge |
| `meta-synthesis` | The quiet-skill list | Registered in `/context/learning-sources.md` |

A learned item shapes weighting and wording. It never becomes proof and never overrides a confirmed brain value; a conflict is shown as a question with both values.

## 3. Who reads this skill's files (read-only; each reader names this skill and the date)

| Reader | Reads | Uses it for |
|---|---|---|
| `discovery-call-prep` | the seller's own `mine/` file only | A "From your last review" line on that seller's next plan: the habit to fix and one question to use. Never in a shared thread |
| `sales-research-digest` | `_reviews.md` | A counts-only "Discovery reviews" section: how many reviews, the stage most often Needs Work, the pattern most often named. Below 10 reviews, counts only |
| `objection-handling` | `_reviews.md` (`objection_raised`) | Which library cards come up on calls, by segment, to rank what to tailor first |
| `meta-synthesis` | `_reviews.md` | Weekly roll-up and the quiet-skill list; registered in `/context/learning-sources.md` |

## 4. Proposals (distinct reviews inside 180 days; exact text plus the receiving skill)

| Observed | n | Proposed to |
|---|---|---|
| A stage most often Needs Work across reviews | 10 | `product-messaging-playbook` and the PMM (an enablement topic, counts only) |
| A consequence stated in the buyer's words | 1 | `product-marketing-context` (`customer_phrases`) |
| A question that unlocked evidence on 3 calls | 3 | `discovery-call-prep` question library, via the PMM |
| An objection raised and not handled the same way twice | 3 | `objection-handling` |
| An alternative or DIY build the buyer named that is not in Section 3 | 2 | `alternatives-map` |
| A competitor named, with stage and role | 2 | `competitive-profile` (`intake`) |
| A disqualify reason that repeats | 5 | `ideal-customer-profile` (audit) |

Never in a seller's thread. Never about a person.
