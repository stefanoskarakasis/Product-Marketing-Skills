# pmm-competitive-intelligence

Competitive intelligence for B2B SaaS PMMs: profiles, battlecards, deep-dives, a leadership brief and a weekly newsletter. Competitor answers in Slack.

## Start here

- **First command:** `/pmm-competitive-intelligence:competitive-profile`
- **Try:** "Set up my competitive profiles. We sell [product] to [buyer]."
- **For leadership:** `/pmm-competitive-intelligence:competitive-briefing`
- **For GTM leaders:** `/pmm-competitive-intelligence:industry-newsletter`
- **In Slack:** tag Claude with "What do we say against [competitor] on pricing?" Admin setup: [`docs/slack-setup.md`](../docs/slack-setup.md)
- **The brain:** better with Sections 1 to 3 and an alternatives map (`product-marketing-context` plugin); without them, skills ask.

## Which skill do I use?

| You say | Skill |
|---|---|
| "Brief the CEO on competitors" | `competitive-briefing` |
| "Write this week's industry newsletter" | `industry-newsletter` |
| "Battlecard for [competitor]" | `competitive-battlecard` |
| "What do we say against [competitor] on pricing" | `competitive-profile` |
| "Deep-dive on [competitor]" | `competitor-deep-dive` |
| "What changed this week" (in `pmm-intelligence`) | `signal-monitor` |

A bare "competitive update" gets one question. Routing checks: [`docs/routing-checks.md`](../docs/routing-checks.md).

## Skills (5)

- **competitive-profile** — Dated, sourced profiles for your five key competitors, refreshed only where stale. Answers team questions in Slack.
- **competitive-battlecard** — One-page battlecard for a live deal, sourced and dated, with field results from past deals.
- **competitor-deep-dive** — Long-form sourced deep-dive on one competitor for a named decision.
- **competitive-briefing** — Weekly leadership brief: verdict with the euro at risk, one decision, last call graded.
- **industry-newsletter** — Weekly newsletter on competitors and your industry for Google Doc, email or Slack. Every claim linked.

## Commands (8)

- `/pmm-competitive-intelligence:competitive-profile` — Set up your roster and profiles, or ask about one competitor.
- `/pmm-competitive-intelligence:competitor-refresh` — Refresh the stale lines of one profile or the roster.
- `/pmm-competitive-intelligence:competitor-roster` — Check who shows up in your deals and propose a swap.
- `/pmm-competitive-intelligence:profile-status` — Show profile freshness.
- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a battlecard.
- `/pmm-competitive-intelligence:competitor-deep-dive` — Build or refresh a deep-dive.
- `/pmm-competitive-intelligence:competitive-briefing` — Build the weekly leadership brief.
- `/pmm-competitive-intelligence:industry-newsletter` — Build the weekly industry newsletter.

## Connectors (Optional)

Optional. Sign-in: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). All categories: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | closed deals naming the competitor, loss reasons | HubSpot |
| `~~call recordings` | objections as buyers said them | Gong, Wispr Flow |
| `~~team chat` | questions and answers; field intel from reps | Slack |
| `~~market data` | competitor traffic shifts | Semrush |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards, win/loss logs | Google Drive |
| `~~competitive intelligence` | cards your CI team keeps (paste only today) | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews on wins and losses | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount, hiring moves | Crunchbase |
| `~~reviews` | public review themes | none wired: paste, or connect your own server |
| `~~web research` | public pages for stale or missing lines | Exa |
| `~~email` | stakeholder email context | Gmail |
| `~~calendar` | meeting cadence and launch dates | Google Calendar |
| `~~SEO` | keyword demand, organic positioning | Semrush |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
