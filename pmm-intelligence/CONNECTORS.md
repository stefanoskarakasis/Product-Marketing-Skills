# pmm-intelligence connectors

Optional. `signal-monitor` works without them: paste what you have and the
output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | competitor traffic and audience shifts | Semrush |
| `~~SEO` | keyword demand and competitor organic movement | Semrush |
| `~~team chat` | team threads, launch coordination, field feedback | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: slack, gmail, google-calendar, semrush, crunchbase, exa.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, and treat pulled facts as drafts until confirmed.
