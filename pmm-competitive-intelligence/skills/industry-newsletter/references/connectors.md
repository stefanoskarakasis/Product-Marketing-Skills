# Connectors

Moved verbatim from `SKILL.md`.

## Connectors

Every skill in this repo works without connectors. This skill checks which are connected before it builds and asks once (Step 2).

| Connector | What it adds | Feeds |
|---|---|---|
| `~~web research` | Public pages: newsrooms, pricing pages, changelogs, filings, trade press | Every claim |
| `~~market data`, `~~company data` | Traffic shifts; funding, headcount and hiring moves | Industry Changes, early signals (🟡) |
| `~~call recordings` (Gong) | Objection themes and competitor mentions from calls, as counts and paraphrase | Leads to check, the Enablement note's objection |
| `~~team chat` (Slack) | The CI channel and replies to the last issue that name a section; posts the Slack version | Leads, feedback, delivery |
| `~~competitive intelligence` (Klue) | The cards and win/loss stories your CI team already keeps (paste, or connect your vendor's server) | Leads to check, Enablement context |
| `~~cloud storage` (Google Drive) | Earlier issues, decks and battlecards; creates the Google Doc after you say yes | Continuity, delivery |
| `~~win/loss` | Buyer interview themes | Leads to check |
| `~~email` | Reads replies you ask it to read | Feedback |

Internal inputs are leads, never the claim: a public page must confirm anything before it is published. The rules are in `references/inputs.md`.

> **No connectors?** Paste the sources, the Slack thread, the Gong themes, the Klue cards and any feedback, and I'll work from that. The output has the same shape.
> Pulled facts are drafts: each is tagged with category, tool and date. Connectors are read-only.
