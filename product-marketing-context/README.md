# product-marketing-context

The PMM brain. Builds and maintains `/foundation/brain.md` — the shared
GTM context file every other plugin in this marketplace reads before
producing output. Install this first.

## Start here

- **You get:** one file, `/foundation/brain.md`, that the other plugins read instead of asking you the same questions again.
- **First command:** `/product-marketing-context:build-brain`
- **Try:** "Build my PMM brain for [product]. We sell to [buyer]."
- **Want to see it first?** Open the [example brain](../examples/example-brain.md), a finished brain for a fictional company.

## Skills (1)

- **product-marketing-context** — Guided setup wizard for building your
  brain from scratch (6 sections: Product Context, ICP Definition,
  Alternatives & Positioning, Voice & Tone, Market Context, Proof Points
  Registry), plus a health-audit mode that scores an existing brain
  file and recommends specific fixes.

## Commands (1)

- `/product-marketing-context:build-brain` — Build or audit your PMM brain.

## Why This Comes First

Every other plugin in this marketplace — `pmm-positioning`,
`pmm-toolkit`, `pmm-execution`, `pmm-go-to-market`, `pmm-meta` — reads
`/foundation/brain.md` for company context before producing output.
Building it once here means you never re-explain your product, ICP, or
positioning to another skill again.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

| Category | What it adds | Tools |
|---|---|---|
| `~~knowledge base` | Product Context, Market Context | Notion, Atlassian |
| `~~CRM` | ICP Definition (win/loss, deal data) | HubSpot |
| `~~call recordings` | ICP, Alternatives, Proof Points (buyer language, objections) | Fireflies, Gong |
| `~~market data` | Alternatives and Market Context | SimilarWeb |
| `~~support` | ICP pain points, Voice and Tone | Intercom |
| `~~cloud storage` | Product Context and Proof Points: decks, pricing, case studies, working docs and sheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~team chat` | Voice and Tone, Proof Points (field feedback, win threads) | Slack |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
