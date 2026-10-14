# Brain Schema (canonical)

Single source for section numbers, field keys, freshness limits and write rights.
Skills keep their own one-line "Brain contract" (plugins install standalone).
`tests/test_consistency.py` fails if a skill cites a section that is not listed here.

| Sec | Name | Field keys | Fresh for | May be written by |
|---|---|---|---|---|
| 1 | Product Context | name, description, stage, target_market, value_prop, offerings, glossary, permitted_claims, business_model | 180 days | product-marketing-context |
| 2 | ICP Definition | company_size, industry, geography, persona, economic_buyer, champion, pains, triggers, jobs_to_be_done, cost_of_problem, anti_persona, committee_roles | 180 days | product-marketing-context, ideal-customer-profile (including `jobs_to_be_done`, `cost_of_problem`, `anti_persona`, `committee_roles`), beachhead-segment, gtm-motions (stub only) |
| 3 | Alternatives & Positioning | alternatives, status_quo, why_leaving, unique_capabilities, category, market_type, alt_shortfalls, switching_forces, objections | 180 days | product-marketing-context, alternatives-map (including `alt_shortfalls`, `switching_forces`), positioning-ideas (stub only), competitive-battlecard (field notes and stub only, user-confirmed), competitive-profile (roster and profile notes only, user-confirmed, never from an unattended run) |
| 4 | Voice & Tone | attributes, tone_shifts, language_prefs, forbidden_phrases, tone_example, customer_phrases | 365 days | product-marketing-context, brand-voice |
| 5 | Market Context | maturity, macro_forces, why_now, narrative | 90 days | product-marketing-context, market-context |
| 6 | Proof Points Registry | approved_metrics, quotes, forbidden_claims | 12 months per claim | proof-points |
| 7 | Strategy | priorities, launches, quarter_goals, active_bets, not_doing, conversion_action | 90 days | product-marketing-context, pmm-okrs (proposal, user-confirmed) |
| 8 | Execution | stakeholders, approvals, prohibited, channels, cadence | 180 days | product-marketing-context, stakeholder-maps (proposal, user-confirmed) |

## Deal-reality fields (added in 3.4.0)

Ten fields hold what happens in deals and what customers actually say. They sit inside Sections 1 to 4 and 7. No section number changed.

| Field | Section | What it holds | Notes |
|---|---|---|---|
| `business_model` | 1 | How you charge and how buyers buy: pricing model, what the price scales with, self-serve or sales-led | A model, not a price list |
| `jobs_to_be_done` | 2 | The 2 to 3 jobs customers hire the product for, as "When __, I want to __, so I can __" | |
| `cost_of_problem` | 2 | What the problem costs the buyer: time, money or risk, with a number and where it came from | An estimate is labelled as one |
| `anti_persona` | 2 | Who is NOT a fit, and why you turn them down | |
| `committee_roles` | 2 | The standing buying-committee roles (champion, economic buyer, technical blocker, end user): what each cares about and what makes each block | Defaults only. A committee for one deal stays in `buyer-personas`, which still writes nothing |
| `alt_shortfalls` | 3 | Per named alternative: where it falls short for this ICP | One line per alternative |
| `switching_forces` | 3 | Push (what drives them away), pull (what draws them to you), habit (what keeps them), anxiety (what worries them about switching) | All four, or the missing ones become gaps |
| `objections` | 3 | The 3 to 5 objections heard most in deals: who raises it, and the approved response | An objection with no approved response is stored with the response left open and a gap is added |
| `customer_phrases` | 4 | Exact words customers use for the problem and for you, each with who said it and where | Verbatim only. See the rule below |
| `conversion_action` | 7 | The one action the funnel is built to make people take, for example "book a demo" | |

Rules for these ten fields:
- They use the same provenance tag, freshness limit and confirmation as every other field. A field inherits its section's freshness limit.
- `customer_phrases` entries are exact quotes. Each carries a source: an evidence id, or who said it and when. An entry with no source is not stored; it becomes a gap. Never paraphrase, merge or tidy a quote.
- `customer_phrases` and `objections` are written only by `product-marketing-context`. Other skills read them and hand suggestions back.
- An existing brain without these fields stays complete. The audit reports how many of the ten are captured and never scores their absence as a gap.
- Customer words guide copy. They are not proof. A number a customer mentioned goes to Section 6 through `proof-points`.

Scope: one brain covers one product or platform. Modules and plans live in the Offerings block of Section 1. A company with several product lines keeps one folder and one brain per product. The key `product` is reserved for a future multi-product design and is not used today.

Rules:
- A value the user confirmed is never overwritten by newer evidence. If newer material disagrees, show both and ask.
- Sections 1 to 8 keep their numbers forever. Add sections; never renumber.
- A "write" always means: shown as an exact before/after and confirmed by the user.

## Files

| File | What it holds | Written by |
|---|---|---|
| `/foundation/brain.md` | The distilled brain (Sections 1 to 8) | `product-marketing-context`, after you confirm |
| `/foundation/evidence.md` | Raw facts extracted from your material (format: `evidence-format.md`) | `product-marketing-context`, Step 8 |
| `/foundation/me.md` | How you like to work: format, length, detail, review habits (format: `me-format.md`). About you, not the company. Skills read it for format and detail only, never for company facts | `product-marketing-context`, Step 9, after you confirm |
| `/foundation/gaps.md` | Open questions (format: `gaps-format.md`) | Any brain-dependent skill adds; `product-marketing-context` answers |

## Provenance tags

Every field value may carry one tag, appended on the same line:

    [src: <where> | <YYYY-MM-DD> | <stated|pulled|inferred> | <draft|confirmed|stale>]

- stated = the user said it. pulled = a connector or document supplied it. inferred = derived from several facts.
- A field with no tag is read as: stated by the user, confirmed on the file's last-updated date.
- Evidence ids may follow the source, for example `[src: pricing page E-004, call 0912 E-011 | 2026-10-11 | pulled | confirmed]`.
- Pulled proof points and quotes always enter Section 6 as `draft`, never `confirmed`.
