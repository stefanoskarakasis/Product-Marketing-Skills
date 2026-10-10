# pmm-growth

Growth ideation and fast iteration — grounded in real brain context, not
generic tactic lists or copy that drifts from your actual positioning.
`positioning-ideas` generates divergent, ungated positioning angles to
choose a direction from; `experiment-ideas` generates the raw campaign
list and hands off to `pmm-execution`'s `experiment-doc` for
pressure-testing; `value-prop-statements` fans an already-set positioning
out into segment- and channel-specific copy without re-running the full
positioning process each time; `pmm-metrics` defines what to measure in
the first place — a North Star Metric and a capped scorecard — so the others have a real target to aim at instead of guessing.
`customer-stories` turns customer calls into stories whose stats and quotes
are checked before they ship.

## Start here

- **You get:** campaign ideas, value-prop variants, a metrics scorecard and customer stories that stay tied to your real positioning.
- **First command:** `/pmm-growth:customer-stories` (needs no brain)
- **Try:** "I have a call with [customer] on Thursday. What do I ask?"
- **The brain:** The idea skills are sharper with a brain; `positioning-ideas` and `value-prop-statements` ask for what they need if you have none. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (5)

- **positioning-ideas** — Generate 3-5 divergent positioning angle
  options, each tied to a specific named alternative's unclaimed
  territory, for choosing a direction before committing. Asks
  for 3+ named alternatives including status quo if the brain has none, and offers to keep them as the start of your brain. Ungated by design
  — every option still needs `positioning-messaging` BUILD mode's
  7-point gate before it ships as real copy.
- **experiment-ideas** — Generate several concrete, cost-efficient growth
  ideas (channel, core message, why it works, cost efficiency), each
  checked against named alternatives so they don't collapse into what a
  status-quo competitor already says, ranked by effort vs. impact.
- **value-prop-statements** — Fan an existing positioning statement out
  into segment- or channel-specific value-prop copy for marketing, sales,
  and onboarding. Asks you to paste your positioning if none exists, never invents one, and
  trace-checks every variant against drift.
- **pmm-metrics** — Classify the business game, define a North Star
  Metric validated against 7 criteria, name 3-5 Input Metrics with a
  stated causal link and owner, then build a capped (8-16 metric)
  scorecard across Financial, Customer, Product & GTM, and Process &
  Growth. Rejects revenue-shaped metrics as North Star candidates and
  flags vanity metrics nobody can move.
- **customer-stories** — Run a B2B customer story from kickoff to
  customer approval in one fixed seven-block structure. You pick the
  depth and the angle; every stat needs a baseline, period, denominator
  and source, every quote a named speaker and a job, and nothing is
  invented. Roles are asked for, never assumed.

## Commands (5)

- `/pmm-growth:positioning-ideas` — Brainstorm divergent positioning
  angles grounded in your named alternatives, before committing to one.
- `/pmm-growth:experiment-ideas` — Brainstorm growth ideas grounded in
  your brain, ranked, and handed off to experiment-doc.
- `/pmm-growth:value-prop-statements` — Generate segment-specific
  value-prop variants from your set positioning.
- `/pmm-growth:pmm-metrics` — Build a North Star Metric and a capped
  measurement scorecard from scratch, or audit an existing metrics list
  for sprawl and vanity metrics.
- `/pmm-growth:customer-stories` — Kickoff and internal brief, interview
  questions, a draft from your notes, the customer review pack, or an
  audit of a finished story.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

| Category | What it adds | Tools |
|---|---|---|
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Pendo |
| `~~market data` | traffic and market benchmarks | SimilarWeb |
| `~~SEO` | keyword and content demand signals | Ahrefs |
| `~~CRM` | funnel and conversion data | HubSpot |
| `~~call recordings` | customer calls and quotes to build stories from | Fireflies, Gong |
| `~~email marketing` | lifecycle email performance | Klaviyo |
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |
| `~~cloud storage` | metric sheets, past reports and experiment logs | Google Drive, Google Sheets |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
