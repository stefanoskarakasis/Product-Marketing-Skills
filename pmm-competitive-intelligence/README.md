# pmm-competitive-intelligence

Competitive intelligence for B2B SaaS PMMs: profiles, battlecards, weekly sweeps, leadership briefs, comparison pages and a newsletter, with competitor answers in Slack.

## Start here

- Setting up your competitor roster? → `/pmm-competitive-intelligence:competitive-profile`
- Watching your competitors every week? → `/pmm-competitive-intelligence:media-monitoring`
- Need a vs or alternatives page? → `/pmm-competitive-intelligence:comparison-page-brief`
- Selling against a rival in a live deal? → `/pmm-competitive-intelligence:competitive-battlecard`
- Briefing leadership on competitors? → `/pmm-competitive-intelligence:competitive-briefing`
- Need the C-suite update from public sources? → `/pmm-competitive-intelligence:weekly-competitive-updates`
- Writing the weekly newsletter for GTM leaders? → `/pmm-competitive-intelligence:industry-newsletter`
- Need a deep-dive on one competitor? → `/pmm-competitive-intelligence:competitor-deep-dive`
- Slack: tag Claude in a thread. Admin setup is in [`docs/slack-setup.md`](../docs/slack-setup.md).
- Safety in Claude Code: a built-in guard asks you before anything is sent or posted to Slack or email. Details: [`docs/agents-map.md`](../docs/agents-map.md).

> [!NOTE]
> 💬 **Try it:** "@Claude what do we say against [competitor] on pricing?"
>
> 🧠 **Brain:** all 8 skills read your brain (`product-marketing-context`); without one they still run.

## Skills (8)

- **competitive-profile** — Set up a roster of five key competitors with dated, sourced profiles, refresh only what is stale, and answer team questions in Slack.
- **competitive-battlecard** — Build a one-page battlecard a seller can skim in 60 seconds before a live deal, tailored to role, buyer and stage, with deal outcomes logged.
- **competitor-deep-dive** — Build a long-form, sourced deep-dive on one competitor for a named decision such as a pricing change, an RFP or a roadmap bet.
- **competitive-briefing** — Build the weekly leadership brief on competitors: a verdict, one recommended decision, what moved ranked by exposure and last week's call graded.
- **weekly-competitive-updates** — Build the weekly C-suite competitor update from public sources only, with every item dated and linked, a threat board and a 30-day watchlist.
- **industry-newsletter** — Build the weekly industry newsletter for GTM leaders: competitor and industry changes, a pricing watch and actions per role.
- **media-monitoring** — Sweep your 3 to 5 core competitors' public pages on a schedule for a one-screen brief with each fix drafted, then act on items, log misses and hand over to a named backup.
- **comparison-page-brief** — Build a you-vs-rival or best-alternatives page from your brain and fresh public sources, with a sourced claims ledger for SEO or sales.

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

## Connectors (Optional)

> [!TIP]
> 🔌 **Every skill works without connectors.**
>
> 📋 **Paste what you have and the output keeps its shape.**
>
> ⚙️ Install this plugin on its own to load its `.mcp.json`.
>
> 🔑 Sign-in steps are in [`docs/connect-your-tools.md`](../docs/connect-your-tools.md).
>
> 📖 Every category, its tools and which skill reads it: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
