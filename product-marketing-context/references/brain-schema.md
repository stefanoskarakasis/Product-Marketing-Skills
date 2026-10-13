# Brain Schema (canonical)

Single source for section numbers, field keys, freshness limits and write rights.
Skills keep their own one-line "Brain contract" (plugins install standalone).
`tests/test_consistency.py` fails if a skill cites a section that is not listed here.

| Sec | Name | Field keys | Fresh for | May be written by |
|---|---|---|---|---|
| 1 | Product Context | name, description, stage, target_market, value_prop, offerings, glossary, permitted_claims | 180 days | product-marketing-context |
| 2 | ICP Definition | company_size, industry, geography, persona, economic_buyer, champion, pains, triggers | 180 days | product-marketing-context, ideal-customer-profile, beachhead-segment, gtm-motions (stub only) |
| 3 | Alternatives & Positioning | alternatives, status_quo, why_leaving, unique_capabilities, category, market_type | 180 days | product-marketing-context, alternatives-map, positioning-ideas (stub only), competitive-battlecard (field notes and stub only, user-confirmed), competitive-profile (roster and profile notes only, user-confirmed, never from an unattended run) |
| 4 | Voice & Tone | attributes, tone_shifts, language_prefs, forbidden_phrases, tone_example | 365 days | product-marketing-context, brand-voice |
| 5 | Market Context | maturity, macro_forces, why_now, narrative | 90 days | product-marketing-context, market-context |
| 6 | Proof Points Registry | approved_metrics, quotes, forbidden_claims | 12 months per claim | proof-points |
| 7 | Strategy | priorities, launches, quarter_goals, active_bets, not_doing | 90 days | product-marketing-context, pmm-okrs (proposal, user-confirmed) |
| 8 | Execution | stakeholders, approvals, prohibited, channels, cadence | 180 days | product-marketing-context, stakeholder-maps (proposal, user-confirmed) |

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
