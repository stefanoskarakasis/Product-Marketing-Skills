# Product Marketing Skills for AI Agents

**Product marketing that compounds.**

Free skills that start from your company brain, not a blank chat. Positioning, battlecards, call prep and launch plans that already know your product, your buyer and your voice.

**Your best work shouldn't live in one person's chat.**

**Build the brain once. Every skill reads it. Nothing changes without your yes.**

Built for PMMs, product marketing leaders and GTM operators in B2B SaaS. Free, MIT licensed.

**Works with:** Claude Code and Codex (tested), Claude on the web and desktop (upload as zips), and any agent that reads standard `SKILL.md` folders, such as Cursor. More in the [Quick start](QUICK-START.md).

**Want your skills to read your CRM, calls, email and Slack?** Skills work without connectors. Connect your tools and they pull facts for you to confirm. Start with the [connectors guide](docs/connect-your-tools.md).

Built by [Stefanos Karakasis](https://stefanoskarakasis.substack.com/).

> [!TIP]
> **Contributions welcome!** Found a way to improve a skill or have a new one to add? [Open a PR](#contributing). Run into a problem or have a question? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues).

**Jump to:** [Try it](#see-it-in-2-minutes) · [Install](#install-in-60-seconds) · [Why a brain?](#why-a-brain) · [Find by job](#find-your-skill-by-job) · [Usage](#usage) · [All skills](#available-skills) · [Installation options](#installation) · [Connectors](#connectors-optional) · [About](#about)

## See it in 2 minutes

No brain yet? Use the example one. It is a finished brain for **Ledgerlane**, a fictional accounts payable company, so you see real output before you build your own.

1. Copy `examples/example-brain.md` into your working folder as `/foundation/brain.md`. In Claude.ai, paste it into the chat and say "Use this as my brain."
2. Say: **"Build our message house."**
3. You get a Roof and Pillars table filled from the brain, with anything missing listed under "Still needed".

Four more prompts to try, and how to switch to your own brain: [examples/](examples/).

## Install in 60 seconds

```bash
# Any supported agent (recommended): pick skills interactively
npx skills add stefanoskarakasis/Product-Marketing-Skills

# Claude Code only, no prompts
npx skills add stefanoskarakasis/Product-Marketing-Skills -a claude-code
```

> [!IMPORTANT]
> Run **`product-marketing-context`** first. About 15 minutes, starting from your website, pricing page or deck. It writes `/foundation/brain.md`. Everything else builds on it.

> [!NOTE]
> **Draft only.** Skills ask before writing to any tool, and nothing in your brain changes without your yes. [How connectors stay safe](docs/connect-your-tools.md#start-read-only)

- **Prefer the plugin marketplace?** See [Installation](#installation) below.

## Why a brain?

Every new chat starts from zero. You paste the ICP. You re-explain the competitors. You fix the tone. Again.

`product-marketing-context` ends that. It builds one document, `/foundation/brain.md`, in about 15 minutes, and every other skill reads it before it writes a word.

| Without a brain | With the brain |
|---|---|
| Every chat starts from zero | Every skill starts from your company |
| You re-paste the ICP and the competitors | The skill reads them from the brain |
| Your best prompt lives in one person's chat | Your best work lives in one file the whole stack reads |
| Output sounds like any B2B SaaS company | Output sounds like yours |

| The brain holds | |
|---|---|
| **Your company** | Product, ICP, alternatives |
| **How you sound** | Positioning, voice |
| **What you can claim** | Market context, proof points |

> [!TIP]
> **The brain keeps learning, on your terms.** Skills flag what's stale and ask what's missing. You approve every change. Nothing is rewritten behind your back.

> [!NOTE]
> One brain covers one product. For several product lines, keep one folder and one brain per product. What loads and when, and how to turn the Slack and email prompts off: [docs/agents-map.md](docs/agents-map.md).

## Find your skill by job

> [!TIP]
> Install `product-marketing-context` first, then add plugins as you need them. The full job-to-skill table is in [docs/pick-by-job.md](docs/pick-by-job.md).

| I need to… | Plugin |
|---|---|
| Stop re-explaining your company | `product-marketing-context` |
| Define who we sell to, write positioning and messaging | `pmm-positioning` |
| Pick a first segment and plan a launch | `pmm-go-to-market` |
| Profile competitors, build battlecards, brief the C-suite weekly | `pmm-competitive-intelligence` |
| Prep or score a discovery call, review a deal, handle an objection, catch up on a customer, build a one-pager or a win-loss read | `pmm-sales` |
| Rank what changed around my product against my priorities | `pmm-intelligence` |
| Run OKRs, retros and pre-mortems | `pmm-execution` |
| Generate and measure growth ideas, write customer stories | `pmm-growth` |
| Draft content, briefs and resumes | `pmm-toolkit` |
| Build or audit skills yourself | `pmm-meta` |

## How it fits together

```
                  product-marketing-context
                  /foundation/brain.md  (built once)
                            |
        every skill below reads it before it writes
                            |
  +--------------+--------------+--------------+--------------+
  | positioning  | go-to-market | competitive  | execution    |
  | ICP, message | beachhead,   | profiles,    | OKRs, PRDs,  |
  | house, voice | launch tier  | battlecards  | retros       |
  +--------------+--------------+--------------+--------------+
        growth | intelligence | toolkit | meta  (same pattern)
```

## Usage

Ask in plain language. The right skill picks itself. Or call one directly, for example `/pmm-positioning:ideal-customer-profile`.

| Say this | Skill that runs |
|---|---|
| "Build my brain from our website and pricing page" | `product-marketing-context` |
| "Build my ICP from these customer interviews" | `ideal-customer-profile` |
| "Write positioning for our new product" | `positioning-messaging` |
| "Build me a battlecard against Acme" | `competitive-battlecard` |
| "Prep my discovery call with the VP Finance at Tidewell Foods" | `discovery-call-prep` |
| "Score this discovery call and tell me what I missed" | `discovery-call-scoring` |
| "A buyer says we are too expensive. What do I say?" | `objection-handling` |
| "What launch tier is this feature, and what is the plan?" | `go-to-market-strategy` |
| "Give me positioning angles to choose between" | `positioning-ideas` |
| "Run a pre-mortem on our Q1 launch" | `pre-mortem` |
| "What changed around us this week?" | `signal-monitor` |
| "Tighten this Slack message to our VP" | `writing-assistant` |
| "Review this skill against the spec" | `meta-review` |

## Available Skills

| Skill | Plugin | Description |
|-------|--------|-------------|
| [product-marketing-context](product-marketing-context/) | product-marketing-context | Build or audit your GTM brain |
| [ideal-customer-profile](pmm-positioning/skills/ideal-customer-profile/) | pmm-positioning | ICP from research: demographics, behaviors, JTBD, needs |
| [alternatives-map](pmm-positioning/skills/alternatives-map/) | pmm-positioning | Named alternatives map: direct competitors, adjacent tools, DIY, status quo |
| [buyer-personas](pmm-positioning/skills/buyer-personas/) | pmm-positioning | Buying committee map + alternatives-anchored persona cards |
| [market-context](pmm-positioning/skills/market-context/) | pmm-positioning | "Why now" narrative: market maturity, macro forces, category moment |
| [brand-voice](pmm-positioning/skills/brand-voice/) | pmm-positioning | Persona-adaptive voice guide: tone by buyer and channel |
| [positioning-messaging](pmm-positioning/skills/positioning-messaging/) | pmm-positioning | Positioning statements, messaging hierarchy, homepage copy |
| [proof-points](pmm-positioning/skills/proof-points/) | pmm-positioning | Sourced, gated claims registry: approved metrics, quotes, forbidden claims |
| [message-house](pmm-positioning/skills/message-house/) | pmm-positioning | Formats existing positioning into a Roof + Value Pillars table |
| [product-messaging-playbook](pmm-positioning/skills/product-messaging-playbook/) | pmm-positioning | Sales/CS-ready messaging playbook: problem, story, one named competitive comparison, discovery/objection script |
| [signal-monitor](pmm-intelligence/skills/signal-monitor/) | pmm-intelligence | Weekly read: at most five opportunities from signals you name |
| [competitive-profile](pmm-competitive-intelligence/skills/competitive-profile/) | pmm-competitive-intelligence | Roster of five key competitors with dated, sourced profiles, refreshed only where stale; answers team questions in Slack |
| [competitive-battlecard](pmm-competitive-intelligence/skills/competitive-battlecard/) | pmm-competitive-intelligence | One-page competitor battlecard for a live deal, tailored to role, motion, persona and stage |
| [competitor-deep-dive](pmm-competitive-intelligence/skills/competitor-deep-dive/) | pmm-competitive-intelligence | Long-form, sourced deep-dive on one competitor for a named decision |
| [competitive-briefing](pmm-competitive-intelligence/skills/competitive-briefing/) | pmm-competitive-intelligence | Weekly leadership brief: verdict with the risk in euro, one recommended decision, what moved, the last call graded and the decisions still open |
| [media-monitoring](pmm-competitive-intelligence/skills/media-monitoring/) | pmm-competitive-intelligence | Scheduled sweep of your core competitors' public pages: a one-screen brief, the fix for each item drafted, and a line on what it could not see |
| [weekly-competitive-updates](pmm-competitive-intelligence/skills/weekly-competitive-updates/) | pmm-competitive-intelligence | Weekly C-suite competitor update from public sources: the last 7 days, every item dated and linked, decisions, fact versus interpretation, a threat board that remembers last week and a 30-day watchlist |
| [comparison-page-brief](pmm-competitive-intelligence/skills/comparison-page-brief/) | pmm-competitive-intelligence | A vs, alternatives or switch page for a named rival, built from your brain and competitor records, with a sourced claims ledger behind every row |
| [customer-context](pmm-sales/skills/customer-context/) | pmm-sales | Dated brief on one customer from your CRM, email, calls and chat, checked against your brain; Slack first |
| [prospect-research](pmm-sales/skills/prospect-research/) | pmm-sales | Pain hypothesis, angle and first question for one prospect from web search, CRM and enrichment, checked against your brain; EMEA-aware; Slack first |
| [deal-review](pmm-sales/skills/deal-review/) | pmm-sales | Weekly-ready deal review: what changed, the buyer's own words, what could kill the deal and one next step, with paste-ready CRM and email blocks; private pattern mirror; Slack first |
| [discovery-call-prep](pmm-sales/skills/discovery-call-prep/) | pmm-sales | Point of view and a 7-stage discovery call plan from the prospect company and the buyer's title, with a lead hypothesis, questions per stage and a fast no; learns from call outcomes; Slack first |
| [discovery-call-scoring](pmm-sales/skills/discovery-call-scoring/) | pmm-sales | Paste a discovery call you ran: a seven-stage score, your pattern, the moments that cost you and the moves for the next call; private to the seller; Slack first |
| [objection-handling](pmm-sales/skills/objection-handling/) | pmm-sales | The next line for a buyer objection, a call digest or a paste-ready email reply, with a library that learns from every deal; draft only, from Slack, a pasted line, a transcript or an email |
| [sales-collateral](pmm-sales/skills/sales-collateral/) | pmm-sales | The sales assets a rep sends or uses: one-pager, leave-behind, demo script, proposal, ROI calculator, deck outline and win-loss analysis, every claim sourced from your brain; sends every other ask to the skill that owns it |
| [pipeline-digest](pmm-sales/skills/pipeline-digest/) | pmm-sales | Digest of the open pipeline of a seller or a team from Salesforce, another CRM or a CSV: what changed, quiet, slow and past-due deals, the CRM fields to fix and five deals to act on; asks for what is missing and drafts a DM per owner; deals only; Slack first |
| [sales-research-digest](pmm-sales/skills/sales-research-digest/) | pmm-sales | Weekly plain-language report for the PMM on how the sales research skills are used, whether the advice held up and what to do next; outcomes from your CRM |
| [industry-newsletter](pmm-competitive-intelligence/skills/industry-newsletter/) | pmm-competitive-intelligence | Weekly industry newsletter for GTM leaders in one locked layout: numbered competitor tables, industry changes, pricing watch and role-owned actions; formatted for Google Doc, email or Slack |
| [gaccs-brief](pmm-toolkit/skills/gaccs-brief/) | pmm-toolkit | Campaign briefs (Goals, Audience, Creative, Channels, Stakeholders) |
| [writing-assistant](pmm-toolkit/skills/writing-assistant/) | pmm-toolkit | Sharpen any written communication; draft blog posts, landing pages, press releases, case studies, newsletters, social posts |
| [pmm-resume](pmm-toolkit/skills/pmm-resume/) | pmm-toolkit | Resume tailoring for PMM roles |
| [privacy-policy](pmm-toolkit/skills/privacy-policy/) | pmm-toolkit | GDPR/CCPA-aware privacy policies |
| [experiment-doc](pmm-execution/skills/experiment-doc/) | pmm-execution | Growth experiments, A/B tests, hypotheses |
| [positioning-ideas](pmm-growth/skills/positioning-ideas/) | pmm-growth | Divergent, ungated positioning angles before committing to positioning-messaging |
| [experiment-ideas](pmm-growth/skills/experiment-ideas/) | pmm-growth | Brain-grounded growth ideas: channel, message, cost-efficiency, ranked |
| [value-prop-statements](pmm-growth/skills/value-prop-statements/) | pmm-growth | Segment-specific value-prop variants of an already-set positioning |
| [pmm-metrics](pmm-growth/skills/pmm-metrics/) | pmm-growth | North Star Metric (7-criteria validated) + capped scorecard across 4 categories |
| [customer-stories](pmm-growth/skills/customer-stories/) | pmm-growth | Kickoff to customer approval for customer stories in one fixed structure; every stat and quote checked |
| [interview-summary](pmm-execution/skills/interview-summary/) | pmm-execution | Customer discovery synthesis using JTBD |
| [prd](pmm-execution/skills/prd/) | pmm-execution | Product requirements docs with embedded Solution Stories |
| [pre-mortem](pmm-execution/skills/pre-mortem/) | pmm-execution | Cross-functional risk analysis |
| [retro](pmm-execution/skills/retro/) | pmm-execution | Post-launch retrospectives |
| [pmm-okrs](pmm-execution/skills/pmm-okrs/) | pmm-execution | Quarterly OKR building |
| [stakeholder-maps](pmm-execution/skills/stakeholder-maps/) | pmm-execution | Political maps: champions, blockers |
| [prioritization-frameworks](pmm-execution/skills/prioritization-frameworks/) | pmm-execution | Score initiatives (RICE, ICE, Kano, and more) |
| [go-to-market-strategy](pmm-go-to-market/skills/go-to-market-strategy/) | pmm-go-to-market | Launch tier assignment, GTM strategy briefs |
| [gtm-motions](pmm-go-to-market/skills/gtm-motions/) | pmm-go-to-market | GTM motion stack selection scored against ICP deal economics |
| [beachhead-segment](pmm-go-to-market/skills/beachhead-segment/) | pmm-go-to-market | First customer wedge scoring |
| [workflow-orchestrator](pmm-go-to-market/skills/workflow-orchestrator/) | pmm-go-to-market | Chains multiple skills into full GTM programs |
| [meta-synthesis](pmm-meta/skills/meta-synthesis/) | pmm-meta | Pattern detection across skill sessions |
| [meta-learn](pmm-meta/skills/meta-learn/) | pmm-meta | Captures post-session learnings |
| [meta-review](pmm-meta/skills/meta-review/) | pmm-meta | Audits skills against `SKILL-SPEC.md` |
| [meta-verify](pmm-meta/skills/meta-verify/) | pmm-meta | Quality gate on skill output |

## Installation

The one-line `npx skills add` install is at the top of this page. These are the alternatives.

### Option 1: Plugin marketplace (Claude Code / Claude)

```bash
/plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
/plugin install product-marketing-context   # install first: everything reads its brain
/plugin install pmm-positioning
/plugin install pmm-toolkit
/plugin install pmm-execution
/plugin install pmm-go-to-market
/plugin install pmm-growth
/plugin install pmm-intelligence
/plugin install pmm-competitive-intelligence
/plugin install pmm-sales
/plugin install pmm-meta
```

> [!IMPORTANT]
> Install `product-marketing-context` first: every other plugin reads the brain it builds. `pmm-meta` can be installed alongside any combination of the others; it doesn't depend on which ones you have.

**Connectors load per plugin.**

- `product-marketing-context` (the brain) wires the whole catalog, so installing it alone gives you every connector.
- Each other plugin wires only what its skills read.
- If you instead load the repo root as one plugin, the root `.mcp.json` carries the same catalog. Pick one path: using both declares the same servers twice.

> [!TIP]
> **Want to see output before you build a brain?** Open [`examples/`](examples/): a finished brain for a fictional company and five prompts to try.

### Option 2: Clone and Copy

Each agent reads skills from its own folder. Copy the skill folders there.

| Agent | Project folder | Personal folder |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |

```bash
git clone https://github.com/stefanoskarakasis/Product-Marketing-Skills.git
mkdir -p .claude/skills                                   # Codex: .agents/skills
cp -r Product-Marketing-Skills/product-marketing-context .claude/skills/
cp -r Product-Marketing-Skills/pmm-positioning/skills/* .claude/skills/
```

Repeat the last line for each plugin you want (`pmm-execution`, `pmm-competitive-intelligence`, and so on). The brain is copied whole because its helper scripts live inside it. Folders are as documented by [Claude Code](https://code.claude.com/docs/en/skills) and Codex at the time of writing; `npx skills add` at the top of this page picks the right folder for you.

> [!NOTE]
> **Cursor:** the skills are plain `SKILL.md` folders, so the copy method above works there too (Cursor documents `.cursor/skills/` and `.agents/skills/`, and also reads `.claude/skills/`). The repo also ships Cursor plugin manifests (`.cursor-plugin/`); they pass the JSON schemas in Cursor's public `cursor/plugins` repo, but they have not been tested inside Cursor itself. Connectors: Cursor reads `mcp.json`, not the `.mcp.json` files shipped here, so add your connector in Cursor's own MCP settings. Tell us what you see.

### Option 3: Fork and Customize

1. Fork this repository
2. Customize skills for your specific PMM needs
3. Clone your fork into your projects

## Connectors (optional)

Skills work without connectors. Connect tools and they pull candidate facts for you to confirm instead of asking you to type them.

| I want to… | Read |
|---|---|
| See which plugin wires which tool, and how to sign in | [docs/connect-your-tools.md](docs/connect-your-tools.md) |
| Add or change a connector | [docs/add-a-connector.md](docs/add-a-connector.md) |
| Answer competitor questions in a Slack thread | [docs/slack-setup.md](docs/slack-setup.md) |

## Make them yours

The skills use `~~category` placeholders (like `~~CRM`) instead of vendor names, so you can swap in your own stack.

- **Guide:** [docs/make-it-yours.md](docs/make-it-yours.md)
- **Chain several skills into one program:** use `workflow-orchestrator` in `pmm-go-to-market`

## Contributing

Contributions are welcome: new skills, better frameworks, fixes and connector ideas.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SKILL-SPEC.md](SKILL-SPEC.md) first.
2. Connector rules are in [AGENTS.md](AGENTS.md).
3. A structure check runs on every change. Locally: `python3 .github/scripts/check_structure.py`.

Found a bug or have an idea? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues).

## About

This marketplace evolves with practice and AI capabilities.

Selected skills based on the work of:

- Marty Cagan: [INSPIRED](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/) and [TRANSFORMED](https://www.amazon.com/dp/1119697336/)
- Ash Maurya: [Running Lean](https://www.amazon.com/dp/B004J4XGN6/)
- Anthony W. Ulwick: [Jobs to Be Done](https://jobs-to-be-done-book.com/)
- Alistair Croll & Benjamin Yoskovitz: [Lean Analytics](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675/)
- April Dunford: [Obviously Awesome](https://www.aprildunford.com/)
- Rick Mans: [Already Ready](https://alreadyready.me/)
- Corey Haines: [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
- Kyle Asay: [Sales Introverts](https://salesintroverts.com/)
- Pawel Huryn: [Product Compass](https://www.productcompass.pm/)
- Shane Parrish: [Farnam Street](https://fs.blog/)

Curated by Stefanos Karakasis from [Stefanos's Stack](https://stefanoskarakasis.substack.com/).

## License

[MIT](LICENSE)
