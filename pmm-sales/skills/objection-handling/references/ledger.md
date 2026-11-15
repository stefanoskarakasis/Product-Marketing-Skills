# Ledger, schemas and feed-forward

## Files in `/context/objections/`

| File | What | Written by |
|---|---|---|
| `_library.md` | Tailored cards | `setup`, owner edits |
| `_ledger.md` | One row per objection raised, plus exposure rows | every run |
| `_config.md` | Per-user context, owner pending proposal | `setup` |

## Ledger row

`date | deal slug | segment | stage | role | account_type (new/renewal) | card ID | buyer phrase (verbatim) | play used | capture (transcript, notes, slack, email, backfill) | outcome | decisive | source`

- Roles and slugs only; no names, no contact details.
- **Exposure rows:** a call reviewed where no objection came up is logged as `none raised`. They feed the denominator.
- `outcome` comes read-only from the CRM when connected and `data_access.crm_outcomes` is `approved` (won, lost, open, renewed, churned); otherwise it stays `unknown`. `decisive` is set only when the CRM loss reason or a transcript names this objection.
- Typing is never required. Getting help is the log. A one-line receipt follows every log: "Logged: price (premature), Marlow, call 2. Undo?" `log:` is only an optional correction.

## Feed-forward (propose-only)

A pattern is proposed only at the n below, counted as distinct deals inside 180 days. Below n it stays a note. A proposal is exact text plus the receiving skill. Unattended runs log and propose nothing. Proposals go to the owner, never the seller's thread.

| Observed | n | Proposed to |
|---|---|---|
| A buyer phrase for a problem or cost, verbatim, role and date | 1 | `product-marketing-context` (`customer_phrases`) |
| An objection by role and stage | 2 | `product-marketing-context` (`objections`) |
| A DIY build or status quo not in Section 3 | 2 | `alternatives-map` |
| A named rival raised in objections | 2 | `competitive-profile`, `competitive-battlecard` (offer only) |
| The same objection costing deals | 3 | `product-messaging-playbook`, `positioning-messaging` |
| A product gap behind repeated product-fit objections | 3 | The owner, for Product |
| A card that never resolves | 3 | The owner, to retire or rewrite it |

Counts start at zero. Never inherit counts from another source.

## Privacy

Roles only. `retain_days` in `_config.md` (default 365) prunes old rows. Call recordings: consent rules and works-council involvement vary by country; reading them needs the owner's approval (`connectors.md`) and `rules.md` applies.
