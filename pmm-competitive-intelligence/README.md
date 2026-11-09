# pmm-competitive-intelligence

Competitive intelligence for B2B SaaS PMMs: a scheduled sweep of your core competitors with the fixes drafted, a weekly C-suite update from public sources, comparison pages for competitive search, plus profiles, battlecards, deep-dives, a leadership brief and a weekly newsletter. Competitor answers in Slack.

## Start here

- **First command:** `/pmm-competitive-intelligence:competitive-profile`
- **To watch your competitors weekly:** `/pmm-competitive-intelligence:media-monitoring`
- **To publish a vs or alternatives page:** `/pmm-competitive-intelligence:comparison-page-brief`
- **Try:** "Set up my competitive profiles. We sell [product] to [buyer]."
- **For leadership:** `/pmm-competitive-intelligence:competitive-briefing`
- **For the C-suite, from public sources:** `/pmm-competitive-intelligence:weekly-competitive-updates`
- **For GTM leaders:** `/pmm-competitive-intelligence:industry-newsletter`
- **In Slack:** tag Claude with "What do we say against [competitor] on pricing?" Admin setup: [`docs/slack-setup.md`](../docs/slack-setup.md)
- **Safety (Claude Code):** a built-in guard asks you before anything is sent or posted to Slack or email. Details: [`docs/agents-map.md`](../docs/agents-map.md)
- **The brain:** better with Sections 1 to 3 and an alternatives map (`product-marketing-context` plugin); without them, skills ask.

## Which skill do I use?

| You say | Skill |
|---|---|
| "Brief the CEO on competitors" | `competitive-briefing` |
| "Run the weekly competitive updates" | `weekly-competitive-updates` |
| "Write this week's industry newsletter" | `industry-newsletter` |
| "Battlecard for [competitor]" | `competitive-battlecard` |
| "What do we say against [competitor] on pricing" | `competitive-profile` |
| "Deep-dive on [competitor]" | `competitor-deep-dive` |
| "Run the weekly competitor sweep" | `media-monitoring` |
| "Build our vs page against [competitor]" | `comparison-page-brief` |
| "What changed this week" (in `pmm-intelligence`) | `signal-monitor` |

A bare "competitive update" gets one question. Routing checks: [`docs/routing-checks.md`](../docs/routing-checks.md).

## How it fits with the other plugins

- **This plugin (competitors: collect and produce):** `media-monitoring` collects what changed on your named competitors' public pages; `weekly-competitive-updates` turns a week of public news into the C-suite update; the other skills turn it into profiles, cards, briefs and newsletters.
- **`pmm-intelligence` (signals: rank what changed):** `signal-monitor` ranks signals of any kind against your priorities. Run it after a sweep when more than one thing moved.
- **`pmm-meta` (learn):** every skill here logs one row per session to `/context/skill-sessions.md`; `meta-synthesis` finds patterns and proposes guardrails you approve.
- **`product-marketing-context` (the brain):** read by all of them; none of these skills writes it.

## Skills (8)

- **competitive-profile** — Dated, sourced profiles for your five key competitors, refreshed only where stale. Answers team questions in Slack.
- **competitive-battlecard** — One-page battlecard for a live deal, sourced and dated, with field results from past deals.
- **competitor-deep-dive** — Long-form sourced deep-dive on one competitor for a named decision.
- **competitive-briefing** — Weekly leadership brief: verdict with the euro at risk, one decision, last call graded.
- **media-monitoring** — Scheduled sweep of your core competitors' public pages: one screen of what needs you, the fix drafted, blind spots named.
- **weekly-competitive-updates** — Weekly C-suite update from public sources: last 7 days, every item dated and linked, decisions, a threat board that remembers last week.
- **comparison-page-brief** — A vs, alternatives or switch page for a named rival, built from your brain and records, with a sourced claims ledger behind every row.
- **industry-newsletter** — Weekly newsletter on competitors and your industry for Google Doc, email or Slack. Every claim linked.

## Commands (11)

- `/pmm-competitive-intelligence:competitive-profile` — Set up your roster and profiles, or ask about one competitor.
- `/pmm-competitive-intelligence:competitor-refresh` — Refresh the stale lines of one profile or the roster.
- `/pmm-competitive-intelligence:competitor-roster` — Check who shows up in your deals and propose a swap.
- `/pmm-competitive-intelligence:profile-status` — Show profile freshness.
- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a battlecard.
- `/pmm-competitive-intelligence:competitor-deep-dive` — Build or refresh a deep-dive.
- `/pmm-competitive-intelligence:competitive-briefing` — Build the weekly leadership brief.
- `/pmm-competitive-intelligence:media-monitoring` — Set up or run the competitor sweep, and act on its items.
- `/pmm-competitive-intelligence:weekly-competitive-updates` — Build the weekly C-suite competitor update.
- `/pmm-competitive-intelligence:comparison-page-brief` — Build or refresh a vs, alternatives or switch page.
- `/pmm-competitive-intelligence:industry-newsletter` — Build the weekly industry newsletter.

## Connectors (Optional)

Optional. Sign-in: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). All categories: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | closed deals naming the competitor, loss reasons | HubSpot |
| `~~call recordings` | objections as buyers said them | Gong, Wispr Flow, Granola, Dovetail |
| `~~team chat` | questions and answers; field intel from reps | Slack |
| `~~market data` | competitor traffic shifts | Semrush, Ahrefs |
| `~~knowledge base` | internal positioning and product notes | Notion, Atlassian |
| `~~cloud storage` | existing decks, battlecards, win/loss logs | Google Drive, Google Docs |
| `~~competitive intelligence` | cards your CI team keeps (paste only today) | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews on wins and losses | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount, hiring moves | Crunchbase |
| `~~reviews` | public review themes | none wired: paste, or connect your own server |
| `~~web research` | public pages for stale or missing lines | Exa |
| `~~email` | stakeholder email context | Gmail |
| `~~calendar` | meeting cadence and launch dates | Google Calendar |
| `~~SEO` | keyword demand, organic positioning | Semrush, Ahrefs |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
