# pmm-competitive-intelligence

Competitive plays a seller can use in a live deal, built from your brain and your alternatives map. `competitive-profile` keeps a roster of your five key competitors current, with a dated, sourced profile for each. `competitive-battlecard` takes one competitor and returns one page: what to say first, what to ask, what to say when the buyer pushes back, and when to walk away. It is tailored to who is selling to whom, at what stage, and what the competitor's role in the deal is.

## Start here

- **You get:** a one-page card (a paste-ready Google Doc in chat, or an HTML page) for one competitor in one deal, with every competitor claim tagged and dated.
- **First command:** `/pmm-competitive-intelligence:competitive-profile` to set up your five, then `/pmm-competitive-intelligence:competitive-battlecard` for a live deal (both work with pasted notes; no connector needed)
- **Try:** "Battlecard for [competitor]. I am an AE talking to their CFO in the evaluation stage."
- **The brain:** Sharper with a brain (Sections 3 and 6 especially). With no brain it asks five quick questions and holds the answers for the session only. The brain-building skill is a separate plugin, `product-marketing-context`. The map of who you compete with is built by `alternatives-map` in `pmm-positioning`.

## Skills (3)

- **competitive-profile** — Keep a roster of your five key competitors with a dated, sourced profile each, refresh only what has gone stale, and get a weekly scheduled refresh proposed.
- **competitive-battlecard** — Build a one-page competitor battlecard for a live deal, tailored to role, GTM motion, buyer persona and deal stage, with every competitor claim sourced and dated.
- **competitor-deep-dive** — Build a long-form, sourced deep-dive on one competitor for a named decision, with deal evidence, reviews, a head-to-head per offering and where they genuinely win.

## Commands (6)

- `/pmm-competitive-intelligence:competitive-profile` — Set up your market and roster of up to five competitors, or review their profiles.
- `/pmm-competitive-intelligence:competitor-refresh` — Refresh only the stale lines of one profile or the whole roster.
- `/pmm-competitive-intelligence:competitor-roster` — Check who really shows up in your deals and propose a swap.
- `/pmm-competitive-intelligence:profile-status` — Show the freshness board for your profiles.
- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a one-page competitor battlecard for a live deal.
- `/pmm-competitive-intelligence:competitor-deep-dive` — Build or refresh a long-form, sourced deep-dive on one competitor for a named decision.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Gong, Wispr Flow |
| `~~team chat` | field intel and pricing claims reps reported | Slack |
| `~~market data` | competitor traffic and audience shifts | Semrush |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive |
| `~~competitive intelligence` | the competitor cards and win/loss stories your CI team already keeps (paste only today, or connect your vendor's server) | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews on why deals were won or lost | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount and hiring moves for the competitor (paste only today) | Crunchbase |
| `~~reviews` | public review themes about the competitor (paste only today) | none wired: paste, or connect your own server |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [GitHub](https://github.com/stefanoskarakasis)

## License

MIT
