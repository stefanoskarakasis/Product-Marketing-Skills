# Signals, Windows and Flags

Read at Steps 3, 8 and 9.

## 1. Evidence states

| State | Meaning |
|---|---|
| `found` | A connected tool shows it (a CRM field, a thread, a call, a doc) |
| `stated` | The user, or a seller in a thread, said it; no tool shows it |
| `validated` | The account owner or user confirmed it this session |
| `not queried` | The source was not read; the claim is not made |

A flag may rest on `stated` only if the brief says so. Nothing is `validated` by Claude alone. This mirrors how deal-review tools separate what AI found from what a rep confirmed.

## 2. Freshness windows (delta runs)

| Line | Re-read when older than |
|---|---|
| Owner, type, size, industry | 180 days |
| Renewal date, stage, amount, next step | 14 days |
| Contacts and last touch | 30 days |
| Correspondence, calls, chat, support | Always read the window since the last brief |
| Usage trend | 30 days |
| Account plan or success plan doc | 90 days |

An unchanged line keeps its original date. Re-reading is not refreshing.

## 3. Flags (show at most five, ranked by cost of ignoring)

| Flag | Fires when | Needs |
|---|---|---|
| Single-threaded | Fewer than two contacts with a two-way thread in 90 days, or none above the day-to-day user | `~~CRM`, `~~email` |
| Champion unconfirmed | A champion is named in the CRM but no two-way thread with them in 90 days | `~~CRM`, `~~email` or calls |
| Economic buyer unmapped | No contact tagged budget owner or exec sponsor | `~~CRM` |
| Renewal runway | Renewal or contract end within 120 days and the next step is blank, or no renewal opp exists | `~~CRM` |
| Silent account | No logged customer touch in 60 days, or an open opp with no activity in 30 | `~~CRM`, `~~calendar` |
| No written desired outcome | No success plan or account plan names what the customer set out to achieve | `~~cloud storage` |
| Usage falling | Adoption trend down against the previous 30 days | `~~product analytics` |
| Open escalation | An open support or chat escalation inside 30 days | `~~support`, `~~team chat` |
| Competitor present | A named alternative appears in CRM, a call, a thread or chat inside 90 days | any |
| Expansion whitespace | Teams or personas using the product are fewer than the committee roles in Section 2 `committee_roles` | `~~product analytics`, `~~CRM` |
| Advocate potential | The customer stated a measured outcome, referred someone, or took part in a story | calls, `~~CRM` |

Do not fire a flag you cannot evidence. "Usage falling" with no analytics connected is "not queried", not a flag.

## 4. Brain check

- **ICP fit:** account against Section 2 company size, industry, geography. Output `fit`, `drift` (outside but not excluded) or `anti-persona` (matches `anti_persona`, with the entry shown).
- **Competitors:** match names seen against Section 3 `alternatives`. A name not in Section 3 is a candidate for `alternatives-map`, proposed only.
- **Objections:** match what the customer or the seller said against Section 3 `objections`. Show the approved response if one exists; if none, say so.
- **Claims:** a claim about us is stated only if it is a Section 1 permitted claim or a Section 6 approved metric or quote.

## 5. Where these signals come from

The flag list adapts four sources: deal-review practice built on MEDDPICC (champion, economic buyer, paper process, decision criteria; the MEDDICC site describes deal reviews as forward-looking, with a weekly cadence); Gong's AI Deal Reviewer (four element states, from nothing found to validated by the AE or manager); Lincoln Murphy's customer-success account signals (a defined desired outcome, time to first value, spread across departments, advocacy, upsell triggers); and the inputs Gainsight lists for relationship and health views (usage, goals, relationships, conversations, sentiment, commercial context). The windows and thresholds above are this repo's defaults, not those vendors' published numbers. Change them in your brain Section 7 or tell the skill your cycle length.
