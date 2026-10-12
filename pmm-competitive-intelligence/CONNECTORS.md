# pmm-competitive-intelligence connectors

Optional. `competitive-battlecard` works without them: paste what you have
and the card has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot (Salesforce: connect your own org's server) |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Fireflies, Gong |
| `~~team chat` | field intel and pricing claims reps reported | Slack |
| `~~market data` | competitor traffic and audience shifts | SimilarWeb |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive |
| `~~competitive intelligence` | the competitor cards, win/loss stories and profiles your CI team already keeps, so the card does not contradict them | none wired: connect your vendor's server (Klue, Crayon) or paste |
| `~~win/loss` | buyer interviews on why deals were won or lost | none wired: paste exports |
| `~~company data` | funding, headcount and hiring moves for the competitor | none wired: paste |
| `~~reviews` | public review themes about the competitor (paste only today) | none wired |

Servers in this plugin's `.mcp.json`: hubspot, fireflies, gong, slack, similarweb, notion, atlassian, google-drive.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, and treat pulled facts as drafts until confirmed.
This plugin never writes to a CRM or any other external tool.
