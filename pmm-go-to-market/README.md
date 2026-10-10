# pmm-go-to-market

Go-to-market strategy, tier assignment, and workflow orchestration for product launches, positioning refresh, competitive programs, and quarterly PMM cycles.

## Start here

- **You get:** a launch tier, a GTM brief and a motion stack, scored against your own ICP.
- **First command:** `/pmm-go-to-market:beachhead-segment` (builds a three-question brain if you have none)
- **Try:** "Which segment should we win first? Candidates: [list]"
- **The brain:** `go-to-market-strategy` and `gtm-motions` need one. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (4)

- **beachhead-segment** — Score candidate segments on four dimensions and identify the first wedge of customers to dominate before scaling GTM investment.
- **go-to-market-strategy** — Assign launch tier (T1–T4) and generate a complete GTM strategy brief with positioning angles, channels, success metrics, and competitive context.
- **workflow-orchestrator** — Orchestrate multi-skill PMM programs end-to-end with Program Charters, checkpoints, coherence checks, and master documents.
- **gtm-motions** — Score GTM motions against ICP deal economics and select a primary/secondary stack.

## Commands (4)

- `/pmm-go-to-market:beachhead-segment` — Score candidate segments and identify the first wedge to dominate.
- `/pmm-go-to-market:go-to-market-strategy` — Assign a launch tier and generate a full GTM strategy brief.
- `/pmm-go-to-market:workflow-orchestrator` — Orchestrate a multi-skill PMM program end-to-end.
- `/pmm-go-to-market:gtm-motions` — Score and select a GTM motion stack

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | segment performance and pipeline context | HubSpot |
| `~~market data` | segment sizing and competitor signals | SimilarWeb |
| `~~call recordings` | buyer language for beachhead and motion choices | Fireflies, Gong |
| `~~team chat` | launch coordination context | Slack |
| `~~email marketing` | lifecycle and campaign performance | Klaviyo |
| `~~marketing analytics` | cross-channel performance | Supermetrics |
| `~~design` | launch assets | Canva |
| `~~email` | stakeholder and customer email threads | Gmail |
| `~~calendar` | launch dates and milestones | Google Calendar |
| `~~cloud storage` | launch docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
