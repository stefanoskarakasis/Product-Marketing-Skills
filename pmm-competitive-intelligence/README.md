# pmm-competitive-intelligence

Competitive intelligence skills for B2B SaaS PMMs: dated competitor profiles, live-deal battlecards and decision-ready deep-dives, with competitor answers your team can get in Slack.

## Start here

- **You get:** dated profiles of your five key competitors and a one-page battlecard for a live deal, tied to your alternatives map. In Slack, anyone can tag Claude with a competitor question and get a short answer with sources, and tag it again to log new intel for your PMM to approve.
- **First command:** `/pmm-competitive-intelligence:competitive-profile`
- **Try:** "Set up my competitive profiles. We sell [product] to [buyer]."
- **In Slack:** tag Claude and ask "What do we say against [competitor] on pricing?" Setup for your Slack admin: [`docs/slack-setup.md`](../docs/slack-setup.md).
- **The brain:** sharper with a brain (Sections 1 to 3) and an alternatives map; without them the skills ask for what they need. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (3)

- **competitive-profile** — Keep a roster of your five key competitors with a dated, sourced profile each, refresh only what has gone stale, answer your team's competitor questions in Slack from all your CI records, and fold in new intel once a named approver says yes.
- **competitive-battlecard** — Build a one-page competitor battlecard for a live deal, tailored to role, GTM motion, buyer persona and deal stage, with every competitor claim sourced and dated, a roster tier and a re-check date. List your saved cards in one index and log how deals ended so the next card shows field results.
- **competitor-deep-dive** — Build a long-form, sourced deep-dive on one competitor for a named decision, with deal evidence, reviews, a head-to-head per offering and where they genuinely win.

## Commands (6)

- `/pmm-competitive-intelligence:competitive-profile` — Set up your market and roster of up to five competitors, review their profiles, or ask a question about one.
- `/pmm-competitive-intelligence:competitor-refresh` — Refresh only the stale lines of one profile or the whole roster.
- `/pmm-competitive-intelligence:competitor-roster` — Check who really shows up in your deals and propose a swap.
- `/pmm-competitive-intelligence:profile-status` — Show the freshness board for your profiles.
- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a one-page competitor battlecard for a live deal.
- `/pmm-competitive-intelligence:competitor-deep-dive` — Build or refresh a long-form, sourced deep-dive on one competitor for a named decision.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | closed-won and closed-lost deals naming the competitor, loss reasons, account type, contract end date | HubSpot |
| `~~call recordings` | objections as buyers said them, and what moved the deal after | Gong, Wispr Flow |
| `~~team chat` | where questions arrive and answers are posted; field intel and pricing claims reps reported | Slack |
| `~~market data` | competitor traffic and audience shifts | Semrush |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards and win/loss logs | Google Drive |
| `~~competitive intelligence` | the competitor cards and win/loss stories your CI team already keeps (paste only today, or connect your vendor's server) | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews on why deals were won or lost | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount and hiring moves for the competitor (paste only today) | Crunchbase |
| `~~reviews` | public review themes about the competitor (paste only today) | none wired: paste, or connect your own server |
| `~~web research` | public pages about a named competitor when a line is stale or missing | Exa |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
