# pmm-positioning connectors

Every connector is optional. All 9 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `alternatives-map` | CRM, call recordings, reviews, market data |
| `brand-voice` | call recordings, knowledge base, support |
| `buyer-personas` | CRM, call recordings, support |
| `ideal-customer-profile` | CRM, call recordings, support |
| `market-context` | knowledge base, SEO, market data |
| `message-house` | No connector named in the skill |
| `positioning-messaging` | CRM, call recordings, cloud storage, knowledge base, market data |
| `product-messaging-playbook` | CRM, call recordings, support |
| `proof-points` | CRM, call recordings, team chat, cloud storage, product analytics |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | win/loss reasons and segment data | HubSpot |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | win threads and field feedback | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~call recordings` | buyer language, objections, alternatives named on calls | Gong, Wispr Flow, Granola, Dovetail |
| `~~video meetings` | meeting recordings and summaries from calls with buyers | Zoom |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | existing decks, case studies and docs | Google Drive, Google Docs, Google Slides |
| `~~knowledge base` | internal positioning and market notes | Notion, Atlassian |

## Customer health

Signals from customers you already have.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~support` | pain points and churn language | Intercom |
| `~~product analytics` | usage evidence for proof points | Mixpanel (US and EU) |
| `~~reviews` | public review themes (paste only today) | none wired: paste, or connect your own server |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | competitor and market signals | Semrush, Ahrefs |
| `~~SEO` | keyword demand and competitor organic positioning | Semrush, Ahrefs |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, google-slides, gmail, google-calendar, mixpanel, mixpanel-eu, wispr-flow, semrush, ahrefs, granola, dovetail, zoom.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
