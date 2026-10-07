# Connectors

Skills in this repo refer to tools by **category**, written with two tildes
before the category name, never by vendor. Each plugin ships its own
`.mcp.json` that wires the vendors it supports, and its own `CONNECTORS.md`
that lists which categories it uses. This file is the master list of
categories. Every category used in a plugin must exist here.

Connectors are optional. Every skill works without them: paste what you
have and the output has the same shape.

## Rules

1. Read-only by default. Ask before writing to any external tool.
2. Every pulled fact is tagged with category, tool and date.
3. Pulled facts are drafts until you confirm them.
4. Pulled proof points and quotes enter the registry unverified.
5. No connectors? Paste the material and continue.

## Categories

| Placeholder | What it provides | Wired today | Other tools that work |
|---|---|---|---|
| `~~knowledge base` | Company overview, product docs, pricing, positioning docs | Notion, Atlassian (Confluence) | Confluence, Guru, Google Drive |
| `~~CRM` | Win/loss reasons, deal data, segment performance | HubSpot | Salesforce, Pipedrive, Attio |
| `~~call recordings` | Sales and customer call transcripts, objections, buyer language | Fireflies, Gong | Chorus, Grain, Otter, Avoma |
| `~~market data` | Competitor traffic, audience and market-size signals | SimilarWeb | Crunchbase, Semrush Traffic, Sensor Tower |
| `~~support` | Support conversations, recurring pain points, churn language | Intercom | Zendesk, Front, Help Scout |
| `~~reviews` | Public reviews and win/loss themes (G2 etc.) | Docs-only today: paste exports | G2, Capterra, TrustRadius (export and paste) |
| `~~SEO` | Keyword demand, competitor organic positioning | Ahrefs | Semrush, Moz |
| `~~product analytics` | Usage, activation and adoption metrics | Amplitude (US and EU), Pendo | Mixpanel, Heap, Google Analytics |
| `~~marketing analytics` | Cross-channel campaign and spend performance | Supermetrics | Google Analytics, Funnel, Windsor |
| `~~email marketing` | Lifecycle email and campaign performance | Klaviyo | Mailchimp, Marketo, Customer.io |
| `~~team chat` | Team threads, launch coordination, field feedback | Slack | Microsoft Teams |
| `~~project tracker` | Launch tasks, roadmap items, ticket context | Linear | Jira, Asana, ClickUp, monday |
| `~~design` | Design files, prototypes and launch assets | Figma, Canva | Adobe Creative Cloud |
| `~~email` | Customer and stakeholder email context | Gmail | Outlook |
| `~~calendar` | Meeting cadence, launch dates and attendees | Google Calendar | Outlook Calendar |
| `~~cloud storage` | Decks, docs and spreadsheets in Drive | Google Drive, Docs, Sheets, Slides | OneDrive, SharePoint, Dropbox, Box |

Gmail, Google Calendar, Google Drive, Docs, Sheets and Slides can also be enabled as built-in
Claude connectors in Claude settings. If sign-in through a plugin fails,
use the built-in connector instead.

**Your own tool is not listed?** Skills ask for a category, not a vendor. Connect
any server in that category and the skill uses it. See `docs/make-it-yours.md`.

See `docs/connect-your-tools.md` for sign-in steps per tool.
