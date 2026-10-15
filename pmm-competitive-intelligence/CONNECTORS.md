# pmm-competitive-intelligence connectors

Optional. `competitive-profile` and `competitive-battlecard` work without them:
paste what you have and the output has the same shape. Public pages about a
named competitor are read with web search, so no connector is needed for those. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Gong, Wispr Flow |
| `~~team chat` | field intel and pricing claims reps reported | Slack |
| `~~market data` | competitor traffic and audience shifts | Semrush |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive |
| `~~competitive intelligence` | the competitor cards, win/loss stories and profiles your CI team already keeps, so the card does not contradict them | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews on why deals were won or lost | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount and hiring moves for the competitor | Crunchbase |
| `~~reviews` | public review themes about the competitor (paste only today) | none wired: paste, or connect your own server |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, slack, google-drive, gmail, google-calendar, wispr-flow, semrush, crunchbase.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, and treat pulled facts as drafts until confirmed.
This plugin never writes to a CRM or any other external tool.
