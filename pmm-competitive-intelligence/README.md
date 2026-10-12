# pmm-competitive-intelligence

Competitive plays a seller can use in a live deal, built from your brain and your alternatives map. `competitive-battlecard` takes one competitor and returns one page: what to say first, what to ask, what to say when the buyer pushes back, and when to walk away. It is tailored to who is selling to whom, at what stage, and what the competitor's role in the deal is.

## Start here

- **You get:** a one-page card (a paste-ready Google Doc in chat, or an HTML page) for one competitor in one deal, with every competitor claim tagged and dated.
- **First command:** `/pmm-competitive-intelligence:competitive-battlecard` (works with pasted notes; no connector needed)
- **Try:** "Battlecard for [competitor]. I am an AE talking to their CFO in the evaluation stage."
- **The brain:** Sharper with a brain (Sections 3 and 6 especially). With no brain it asks five quick questions and holds the answers for the session only. The brain-building skill is a separate plugin, `product-marketing-context`. The map of who you compete with is built by `alternatives-map` in `pmm-positioning`.

## Skills (1)

- **competitive-battlecard** — Build a one-page competitor battlecard tailored to role, GTM motion, buyer persona, deal stage and the competitor's status in the deal. Reads brain Sections 1 to 8, checks your forbidden claims and prohibited items first, saves the card to `/context/battlecards/`, and proposes field notes back to Section 3 for you to confirm. Use when a competitor is in a live deal and a seller needs one page to read before the call and quote from during it.

## Commands (1)

- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a one-page competitor card for a live deal.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot (Salesforce: connect your own) |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Fireflies, Gong |
| `~~team chat` | field intel and pricing claims reps reported | Slack |
| `~~market data` | competitor traffic and audience shifts | SimilarWeb |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive |
| `~~competitive intelligence` | the competitor cards and win/loss stories your CI team already keeps (paste only today, or connect your vendor's server) | none wired (Klue, Crayon work if you connect them) |
| `~~win/loss` | buyer interviews on why deals were won or lost (paste only today) | none wired |
| `~~company data` | funding, headcount and hiring moves for the competitor (paste only today) | none wired |
| `~~reviews` | public review themes about the competitor (paste only today) | none wired |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [GitHub](https://github.com/stefanoskarakasis)

## License

MIT
