# pmm-intelligence connectors

Every connector is optional. The skill works without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | team threads, launch coordination, field feedback | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | competitor traffic and audience shifts | Semrush, Ahrefs |
| `~~SEO` | keyword demand and competitor organic movement | Semrush, Ahrefs |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: slack, gmail, google-calendar, semrush, crunchbase, exa, ahrefs.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
