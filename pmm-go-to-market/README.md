# pmm-go-to-market

Go-to-market skills for PMMs: beachhead segments, launch tiering and GTM strategy briefs, GTM motions and multi-skill workflow orchestration.

## Start here

- **You get:** a launch tier, a GTM brief and a motion stack, scored against your own ICP.
- **First command:** `/pmm-go-to-market:beachhead-segment` (builds a three-question brain if you have none)
- **Try:** "Which segment should we win first? Candidates: [list]"
- **The brain:** `go-to-market-strategy` sends you to `beachhead-segment` if you have none; `gtm-motions` asks two quick questions instead. The full brain is built by a separate plugin, `product-marketing-context`.

## Skills (4)

- **beachhead-segment** — Score candidate segments on four dimensions and pick the first wedge of customers to win before scaling.
- **go-to-market-strategy** — Assign a launch tier (T1–T4) and generate a GTM brief with positioning angles, channels, metrics and competitive context.
- **workflow-orchestrator** — Chain several PMM skills into one program with a charter, checkpoints and a master document.
- **gtm-motions** — Score GTM motions against ICP deal economics and pick one primary and at most one secondary.

## Commands (4)

- `/pmm-go-to-market:beachhead-segment` — Score candidate segments and identify the first wedge to dominate.
- `/pmm-go-to-market:go-to-market-strategy` — Assign a launch tier and generate a full GTM strategy brief.
- `/pmm-go-to-market:workflow-orchestrator` — Orchestrate a multi-skill PMM program end to end.
- `/pmm-go-to-market:gtm-motions` — Score and select a GTM motion stack.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | segment performance and pipeline context | HubSpot |
| `~~market data` | segment sizing and competitor signals | Semrush |
| `~~call recordings` | buyer language for beachhead and motion choices | Gong, Wispr Flow |
| `~~team chat` | launch coordination context | Slack |
| `~~email marketing` | lifecycle and campaign performance | Klaviyo |
| `~~marketing analytics` | cross-channel performance | Supermetrics |
| `~~design` | launch assets | Canva |
| `~~email` | stakeholder and customer email threads | Gmail |
| `~~calendar` | launch dates and milestones | Google Calendar |
| `~~cloud storage` | launch docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |

## Author

Stefanos Karakasis — [GitHub](https://github.com/stefanoskarakasis)

## License

MIT
