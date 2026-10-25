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
  brain from scratch, plus refresh and gap modes that keep it current (6 core sections plus optional strategy and execution sections, and ten deal-reality fields for objections, switching forces, customer language and anti-persona: Product Context, ICP Definition,
  Alternatives & Positioning, Voice & Tone, Market Context, Proof Points
  Registry), plus a health-audit mode that scores an existing brain
  file and recommends specific fixes.

## Commands (4)

- `/product-marketing-context:build-brain` — Build or audit your PMM brain.
- `/product-marketing-context:refresh-brain` — Find the fields that have gone stale and re-confirm only those.
- `/product-marketing-context:brain-gaps` — Answer the open questions other skills left in your gaps queue.
- `/product-marketing-context:my-context` — Tell the brain how you like to work (length, detail, tone of feedback). Saved to `/foundation/me.md`, kept apart from company facts.

## How a brain gets built

The skill starts from what you already have. It asks for your website and pricing page, drafts from them, and takes decks, call notes and win/loss docs if you have them. It then shows the facts it found, with sources, as a proposed brain you approve section by section. It asks questions only about what your material could not answer. Facts live in `/foundation/evidence.md`; if your folder is under version control, do not commit that file, because it can hold customer details. A demo you can run is in [`examples/ingest-demo`](../examples/ingest-demo/).

## One brain, one product

A brain covers one product or platform (modules and plans go in its Offerings block). If your company has several product lines, keep a separate folder, each with its own `/foundation/brain.md`, and run the skills once per product.

## Why This Comes First

Every other plugin in this marketplace — `pmm-positioning`,
`pmm-toolkit`, `pmm-execution`, `pmm-go-to-market`, `pmm-meta` — reads
`/foundation/brain.md` for company context before producing output.
Building it once here means you never re-explain your product, ICP, or
positioning to another skill again.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~knowledge base` | Product Context, Market Context | Notion, Atlassian |
| `~~CRM` | ICP Definition (win/loss, deal data) | HubSpot |
| `~~call recordings` | ICP, Alternatives, Proof Points (buyer language, objections) | Gong, Wispr Flow |
| `~~market data` | Alternatives and Market Context | Semrush |
| `~~support` | ICP pain points, Voice and Tone | Intercom |
| `~~cloud storage` | Product Context and Proof Points: decks, pricing, case studies, working docs and sheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~team chat` | Voice and Tone, Proof Points (field feedback, win threads) | Slack |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~email` | customer and stakeholder email threads | Gmail |
| `~~design` | design files and assets referenced in PRDs | Figma, Canva |
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |
| `~~SEO` | keyword and content demand signals | Semrush |
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Mixpanel (US and EU) |
| `~~project tracker` | launch tasks and ticket context | Linear, Asana |
| `~~win/loss` | buyer interviews and research on why deals were won or lost | none wired: paste, or connect your own server |
| `~~reviews` | public review themes (G2 and similar) | none wired: paste, or connect your own server |
| `~~competitive intelligence` | competitor cards and win/loss stories your CI team already keeps | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~email marketing` | lifecycle email performance | Klaviyo |
| `~~revenue intelligence` | pipeline health, forecast and sales-engagement activity | none wired: paste, or connect your own server |
| `~~data warehouse` | your own product, pipeline and revenue tables | none wired: paste, or connect your own server |
| `~~video meetings` | meeting recordings, transcripts and summaries from your video tool | none wired: paste, or connect your own server |
| `~~enrichment` | company and contact enrichment for named accounts | none wired: paste, or connect your own server |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
