# pmm-intelligence connectors

Optional. `signal-monitor` works without them: paste what you have and the
output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | competitor traffic and audience shifts | SimilarWeb |
| `~~SEO` | keyword demand and competitor organic movement | Ahrefs |

Servers in this plugin's `.mcp.json`: similarweb, ahrefs.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, and treat pulled facts as drafts until confirmed.
