# Connectors

Skills in this repo refer to tools by **category**, written with two tildes before the category name,
never by vendor. Each plugin ships its own `.mcp.json` that wires the
vendors it supports, and its own `CONNECTORS.md` that lists which categories
it uses. This file is the master list of categories. Every category used in a
plugin must exist here.

Connectors are optional. Every skill works without them: paste what you
have and the output has the same shape.

## Rules

1. Read-only by default. Ask before writing to any external tool.
2. Every pulled fact is tagged with category, tool and date.
3. Pulled facts are drafts until you confirm them.
4. Pulled proof points and quotes enter the registry unverified.
5. No connectors? Paste the material and continue.

## Categories

| Placeholder | What it provides | Wired today |
|---|---|---|
| `~~knowledge base` | Company overview, product docs, pricing, positioning docs | Notion, Atlassian (Confluence) |
| `~~CRM` | Win/loss reasons, deal data, segment performance | HubSpot |
| `~~call recordings` | Sales and customer call transcripts, objections, buyer language | Fireflies, Gong |
| `~~market data` | Competitor traffic, audience and market-size signals | SimilarWeb |
| `~~support` | Support conversations, recurring pain points, churn language | Intercom |
| `~~reviews` | Public reviews and win/loss themes (G2 etc.) | Docs-only today: paste exports |
| `~~SEO` | Keyword demand, competitor organic positioning | Ahrefs |
| `~~product analytics` | Usage, activation and adoption metrics | Amplitude, Pendo |
| `~~team chat` | Team threads, launch coordination, field feedback | Slack |
| `~~project tracker` | Launch tasks, roadmap items, ticket context | Linear, Asana |
| `~~design` | Design files and prototypes referenced in specs | Figma |

Gmail, Google Calendar and Google Drive are first-party Claude connectors.
They are enabled in Claude settings, not in `.mcp.json`, and no skill uses
them yet.

See `docs/connect-your-tools.md` for sign-in steps per tool.
