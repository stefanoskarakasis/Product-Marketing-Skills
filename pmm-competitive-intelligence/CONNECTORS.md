# pmm-competitive-intelligence connectors

Every connector is optional. All 8 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.
- **No connector needed** for public pages about a named competitor: they are read with web search.

## Which skill reads what

| Skill | Reads |
|---|---|
| `comparison-page-brief` | CRM, call recordings, cloud storage, SEO |
| `competitive-battlecard` | CRM, win/loss, call recordings, team chat, cloud storage, knowledge base, reviews, company data, competitive intelligence, market data |
| `competitive-briefing` | CRM, win/loss, call recordings, team chat, cloud storage, company data, competitive intelligence, web research |
| `competitive-profile` | CRM, win/loss, call recordings, team chat, cloud storage, knowledge base, reviews, company data, competitive intelligence, market data, web research |
| `competitor-deep-dive` | CRM, win/loss, call recordings, team chat, cloud storage, knowledge base, reviews, company data, competitive intelligence, market data |
| `industry-newsletter` | win/loss, call recordings, email, team chat, cloud storage, company data, competitive intelligence, market data, web research |
| `media-monitoring` | team chat, cloud storage, reviews, company data, market data, web research |
| `weekly-competitive-updates` | team chat, cloud storage, reviews, company data, market data, web research |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot |
| `~~win/loss` | buyer interviews on why deals were won or lost | none wired: paste, or connect your own server |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | where questions arrive and answers are posted; field intel and pricing claims reps reported | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Gong, Wispr Flow, Granola, Dovetail |
| `~~video meetings` | meeting recordings and summaries from calls with buyers | Zoom |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive, Google Docs |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |

## Customer health

Signals from customers you already have.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~reviews` | public review themes about the competitor (paste only today) | none wired: paste, or connect your own server |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | competitor traffic and audience shifts | Semrush, Ahrefs |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush, Ahrefs |
| `~~competitive intelligence` | the competitor cards, win/loss stories and profiles your CI team already keeps, so the card does not contradict them | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount and hiring moves for the competitor | Crunchbase |
| `~~web research` | public pages about a named competitor when a line is stale or missing | Exa |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, slack, google-drive, google-docs, gmail, google-calendar, wispr-flow, semrush, crunchbase, exa, ahrefs, granola, dovetail, zoom.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **This plugin never writes to a CRM** or any other external tool.
