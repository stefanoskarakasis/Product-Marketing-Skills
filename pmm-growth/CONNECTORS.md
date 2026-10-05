# pmm-growth connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Pendo |
| `~~market data` | traffic and market benchmarks | SimilarWeb |
| `~~SEO` | keyword and content demand signals | Ahrefs |
| `~~CRM` | funnel and conversion data | HubSpot |
| `~~email marketing` | lifecycle email performance | Klaviyo |
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |

Servers in this plugin's `.mcp.json`: amplitude, amplitude-eu, pendo, similarweb, ahrefs, hubspot, klaviyo, supermetrics.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
