# product-marketing-context connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~knowledge base` | Product Context, Market Context | Notion, Atlassian |
| `~~CRM` | ICP Definition (win/loss, deal data) | HubSpot |
| `~~call recordings` | ICP, Alternatives, Proof Points (buyer language, objections) | Fireflies, Gong |
| `~~market data` | Alternatives and Market Context | SimilarWeb |
| `~~support` | ICP pain points, Voice and Tone | Intercom |
| `~~cloud storage` | Product Context and Proof Points (decks, pricing, case studies) | Google Drive |
| `~~team chat` | Voice and Tone, Proof Points (field feedback, win threads) | Slack |

Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, fireflies, gong, similarweb, intercom, google-drive, slack.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
