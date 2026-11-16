# Setup: brain first

Read for `setup`, and on the first run in a workspace (no `_config.md`). Setup is a check and a handover, not a form: it reads, shows what is ready, and asks one question at a time. It never blocks a plan.

## 1. Brain check (always first)

Read the brain (`scripts/brain_section.py` when present). If there is none: say so in one line, point to `product-marketing-context` ("build my brain"), and offer a plan built without a brain (low confidence). Show a short table, one row per field this skill reads, in three states: ready, thin, empty.

| Field | Used for | If empty, fill with |
|---|---|---|
| Section 2 `pains`, `triggers` | the bet and the fallback | `ideal-customer-profile` |
| Section 2 `persona`, `committee_roles` | seniority, who else to bring in | `buyer-personas` |
| Section 2 `anti_persona` | the fast no | `ideal-customer-profile` |
| Section 2 `sales_cycle`, `cost_of_problem` | stage sizing, stakes | `ideal-customer-profile` |
| Section 3 `alternatives`, `status_quo`, `objections` | where you differ, sideways moves | `alternatives-map` |
| Section 4 `customer_phrases` | the buyer's words | `product-marketing-context` |
| Section 6 `approved_metrics`, `quotes`, `forbidden_claims` | the one approved story | `proof-points` |
| Section 8 `prohibited`, `context_owners` | stops, owner | `product-marketing-context` |

Rule: three real customer phrases and a real anti-persona are the two that change plans most. Name the thinnest field first and the skill that fills it. Do not fill the brain from here.

## 2. Who and where

Write `/context/discovery/_config.md`: `emea_mode` (auto), `home_region`, `default_minutes` (30), `retain_days` (180). Defaults are labelled. Ask only what you cannot read.

## 3. Owner

Read Section 8 `context_owners` for discovery knowledge. Missing or older than 90 days: ask once, in `setup`, `library` or `sweep`, never in a seller's reply: "Which team owns discovery knowledge here, and who is the backup role?" Roles, not names. Then show an exact proposal for `product-marketing-context` (`area`, `team`, `owner role`, `backup role`, `confirmed`); the user runs it. Until then record "pending brain proposal" in `_config.md`.

## 4. Data access and recorders

Say which of `~~call recordings`, `~~CRM`, `~~calendar`, `~~team chat` answered. The owner decides, per source (approve, decline, decide later), with role and date stored as `data_access` and asked again after 90 days. Show the risks first: recording consent, works councils, personal data, retention, CRM quality, no per-seller reporting. A decline is respected; the skill keeps working from pasted material.

Recorder path (`references/connectors.md`): connector, then the recorder's transcript in a folder named as `recording_folder`, then a drop folder, then a paste. Ask which recorder each team uses, and which path it can take.

## 5. Seed and first plan

Seed `_questions.md` and `_library.md` from `questions.md` only when absent (never overwrite). End setup with one next action: run `prospect-research` on a real account, then `prep`. Offer the seller card (`references/seller-card.md`) for the sales channel.
