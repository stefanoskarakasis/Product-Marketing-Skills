# pmm-positioning connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~call recordings` | buyer language, objections, alternatives named on calls | Fireflies, Gong |
| `~~CRM` | win/loss reasons and segment data | HubSpot |
| `~~market data` | competitor and market signals | SimilarWeb |
| `~~support` | pain points and churn language | Intercom |
| `~~knowledge base` | internal market notes | Notion, Atlassian |
| `~~reviews` | public review themes (paste only today) | none wired |
| `~~SEO` | keyword demand and competitor organic positioning | paste only today |
| `~~product analytics` | usage evidence for proof points | paste only today |

Servers in this plugin's `.mcp.json`: fireflies, gong, hubspot, similarweb, intercom.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
