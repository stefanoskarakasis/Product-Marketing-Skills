# Product Marketing Skills for AI Agents

**Positioning, competitive intelligence, GTM strategy and launch planning for B2B SaaS product marketers.** Build your company brain once; every skill reads it, so you stop re-explaining your product in every chat.

Built for PMMs, product marketing leaders and GTM operators. Runs in Claude Code and Claude; the skills are plain `SKILL.md` files, so the same install works in other agents that support them.

Built by [Stefanos Karakasis](https://stefanoskarakasis.substack.com/). Contributions: spot a way to improve a skill, or have a new one to add? [Open a PR](https://github.com/stefanoskarakasis/Product-Marketing-Skills#contributing). Questions or problems: [open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues).
## Install in 60 seconds

```bash
# Any supported agent (recommended): pick skills interactively
npx skills add stefanoskarakasis/Product-Marketing-Skills

# Claude Code only, no prompts
npx skills add stefanoskarakasis/Product-Marketing-Skills -a claude-code
```

Then run **`product-marketing-context`** first. It interviews you for about 15 minutes and writes `/foundation/brain.md`. Everything else builds on it. No time? Open [`examples/`](examples/) to see a finished brain and five prompts to try.

Prefer the plugin marketplace? See [Installation](#installation) below.

## Why a brain?

**The problem:** every time you ask an AI agent for positioning, battlecards or a brief, you re-explain your company. By the fifth conversation you're copy-pasting from old chats.

**The fix:** `product-marketing-context` builds one document, `/foundation/brain.md`: product, ICP, alternatives, positioning, voice, market context and proof points. Every other skill reads it before producing anything. One brain covers one product; for several product lines, keep one folder and one brain per product.

## Start here: pick by job

Nine plugins, grouped by the work you do. Install `product-marketing-context` first; add the rest as you need them.

| I need to… | Start with | Plugin |
|---|---|---|
| Build my brain | `product-marketing-context` | `product-marketing-context` |
| Define who we sell to and why we win | `ideal-customer-profile`, `alternatives-map` | `pmm-positioning` |
| Write positioning and messaging | `positioning-messaging`, `message-house` | `pmm-positioning` |
| Hand Sales a messaging playbook | `product-messaging-playbook` | `pmm-positioning` |
| Pick a first segment and plan a launch | `beachhead-segment`, `go-to-market-strategy` | `pmm-go-to-market` |
| Beat a competitor in a live deal | `competitive-battlecard` | `pmm-competitive-intelligence` |
| Profile a competitor | `competitive-profile`, `competitor-deep-dive` | `pmm-competitive-intelligence` |
| Know what changed around my product this week | `signal-monitor` | `pmm-intelligence` |
| Run the PMM job: OKRs, retros, pre-mortems | `pmm-okrs`, `retro`, `pre-mortem` | `pmm-execution` |
| Generate and measure growth ideas | `experiment-ideas`, `pmm-metrics` | `pmm-growth` |
| Write customer stories | `customer-stories` | `pmm-growth` |
| Draft content, briefs, resumes | `writing-assistant`, `gaccs-brief` | `pmm-toolkit` |
| Keep my skills sharp | `meta-review`, `meta-learn` | `pmm-meta` |

**Skills** are single guided workflows; **plugins** bundle related skills into one install. The full catalogue is under [Available Skills](#available-skills-39-total).

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

Ask in plain language, or call a skill directly.

| Say this | Skill that runs |
|---|---|
| "Build my ICP from these customer interviews" | `ideal-customer-profile` |
| "Map the alternatives my buyers consider" | `alternatives-map` |
| "Write positioning for our new product" | `positioning-messaging` |
| "Plan the launch for this feature as a Tier 2" | `go-to-market-strategy` |
| "Build me a battlecard against Acme" | `competitive-battlecard` |
| "Run a retro on last quarter's launch" | `retro` |

Direct call example: `/pmm-positioning:ideal-customer-profile`.

## Available Skills (39 Total)

| Skill | Plugin | Description |
|-------|--------|-------------|
| [product-marketing-context](product-marketing-context/) | product-marketing-context | Build or audit your GTM brain |
| [ideal-customer-profile](pmm-positioning/skills/ideal-customer-profile/) | pmm-positioning | ICP from research: demographics, behaviors, JTBD, needs |
| [alternatives-map](pmm-positioning/skills/alternatives-map/) | pmm-positioning | Named alternatives map — direct competitors, adjacent tools, DIY, status quo |
| [buyer-personas](pmm-positioning/skills/buyer-personas/) | pmm-positioning | Buying committee map + alternatives-anchored persona cards |
| [market-context](pmm-positioning/skills/market-context/) | pmm-positioning | "Why now" narrative: market maturity, macro forces, category moment |
| [brand-voice](pmm-positioning/skills/brand-voice/) | pmm-positioning | Persona-adaptive voice guide: tone by buyer and channel |
| [positioning-messaging](pmm-positioning/skills/positioning-messaging/) | pmm-positioning | Positioning statements, messaging hierarchy, homepage copy |
| [proof-points](pmm-positioning/skills/proof-points/) | pmm-positioning | Sourced, gated claims registry — approved metrics, quotes, forbidden claims |
| [message-house](pmm-positioning/skills/message-house/) | pmm-positioning | Formats existing positioning into a Roof + Value Pillars table |
| [product-messaging-playbook](pmm-positioning/skills/product-messaging-playbook/) | pmm-positioning | Sales/CS-ready messaging playbook: problem, story, one named competitive comparison, discovery/objection script |
| [signal-monitor](pmm-intelligence/skills/signal-monitor/) | pmm-intelligence | Weekly read: at most five opportunities from signals you name |
| [competitive-profile](pmm-competitive-intelligence/skills/competitive-profile/) | pmm-competitive-intelligence | Roster of five key competitors with dated, sourced profiles, refreshed only where stale |
| [competitive-battlecard](pmm-competitive-intelligence/skills/competitive-battlecard/) | pmm-competitive-intelligence | One-page competitor battlecard for a live deal, tailored to role, motion, persona and stage |
| [competitor-deep-dive](pmm-competitive-intelligence/skills/competitor-deep-dive/) | pmm-competitive-intelligence | Long-form, sourced deep-dive on one competitor for a named decision |
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
/plugin install pmm-meta
```

Connectors load per plugin. `product-marketing-context` (the brain) wires the whole catalog, so installing it alone gives you every connector, and each other plugin wires only what its skills read. If you instead load the repo root as one plugin, the root `.mcp.json` carries the same catalog. Pick one path: using both declares the same servers twice. Install `product-marketing-context` first — every other plugin reads the brain it
builds. `pmm-meta` can be installed alongside any combination of the
others; it doesn't depend on which ones you have.

**Want to see output before you build a brain?** Open [`examples/`](examples/): a finished brain for a fictional company and five prompts to try.

### Option 2: Clone and Copy

```bash
git clone https://github.com/stefanoskarakasis/Product-Marketing-Skills.git
cp -r Product-Marketing-Skills/pmm-execution/skills/* .agents/skills/
```

Adjust the source path per plugin depending on which skills you want.

### Option 3: Fork and Customize

1. Fork this repository
2. Customize skills for your specific PMM needs
3. Clone your fork into your projects

## Connectors (Optional)

Skills work without connectors. Connect tools and they pull candidate facts for you to confirm instead of asking you to type them.

<!-- generated:plugin-table begin -->
| Plugin | Connectors wired |
|---|---|
| product-marketing-context | Notion, Atlassian, HubSpot, Gong, Intercom, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Linear, Figma, Canva, Gmail, Google Calendar, Klaviyo, Supermetrics, Amplitude (US and EU), Mixpanel (US and EU), Asana, Wispr Flow, Semrush, Crunchbase, Exa |
| pmm-positioning | Notion, Atlassian, HubSpot, Gong, Intercom, Slack, Google Drive, Google Docs, Google Slides, Gmail, Google Calendar, Mixpanel (US and EU), Wispr Flow, Semrush |
| pmm-execution | Notion, Atlassian, Gong, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Linear, Figma, Canva, Gmail, Google Calendar, Asana, Wispr Flow |
| pmm-go-to-market | HubSpot, Gong, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Canva, Gmail, Google Calendar, Klaviyo, Supermetrics, Wispr Flow, Semrush |
| pmm-growth | HubSpot, Gong, Slack, Google Drive, Google Sheets, Gmail, Google Calendar, Klaviyo, Supermetrics, Amplitude (US and EU), Mixpanel (US and EU), Wispr Flow, Semrush |
| pmm-intelligence | Slack, Gmail, Google Calendar, Semrush, Crunchbase, Exa |
| pmm-competitive-intelligence | Notion, Atlassian, HubSpot, Gong, Slack, Google Drive, Gmail, Google Calendar, Wispr Flow, Semrush, Crunchbase |
| pmm-toolkit | Notion, Atlassian, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Canva, Gmail, Google Calendar |
| pmm-meta | None |
<!-- generated:plugin-table end -->

Some connectors need extra access: Semrush needs an API plan,
Gong usually needs an admin to enable it, Crunchbase needs a workspace seat, and Wispr Flow needs
Notetaker and MCP access on your account. Salesforce, GitHub, Zendesk,
Snowflake, Zoom, Salesloft, Clay and other tools with no public endpoint are
connect-your-own or paste-only. The brain plugin (`product-marketing-context`) wires every connector in the catalog. Every other plugin wires only the tools its skills read. Install each plugin on its own to load its connectors (see Installation). To add or change a connector, edit `connectors.json` ([how](docs/add-a-connector.md)). Sign-in steps: [docs/connect-your-tools.md](docs/connect-your-tools.md). Category registry: [CONNECTORS.md](CONNECTORS.md).

## Workflow Intelligence

`workflow-orchestrator` (in `pmm-go-to-market`) chains multiple skills
into one coherent, end-to-end program — a Program Charter, sequenced
skill runs, coherence checks between their outputs, and one master
document at the end.

## Making Them Yours

The skills use `~~category` placeholders (like `~~CRM`) instead of vendor names, so you can swap in your own stack. Use the defaults, add a different tool in the same category, or fork the repo and edit the skills to fit your company. Full guide: [docs/make-it-yours.md](docs/make-it-yours.md).

## Contributing

Contributions are welcome: new skills, better frameworks, fixes, and connector ideas.

- Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SKILL-SPEC.md](SKILL-SPEC.md) first.
- Connector rules (placeholders only, never commit credentials) are in [CLAUDE.md](CLAUDE.md).
- A structure check runs on every change. Locally: `python3 .github/scripts/check_structure.py`.
- Found a bug or have an idea? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues).

## About

This marketplace evolves with practice and AI capabilities.

Selected skills based on the work of:

- Marty Cagan — [*INSPIRED*](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/) and [*TRANSFORMED*](https://www.amazon.com/dp/1119697336/)
- Ash Maurya — [*Running Lean*](https://www.amazon.com/dp/B004J4XGN6/)
- Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
- Alistair Croll & Benjamin Yoskovitz — [*Lean Analytics*](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675/)
- April Dunford — [*Obviously Awesome*](https://www.aprildunford.com/)

Curated by [Stefanos Karakasis](https://stefanoskarakasis.substack.com/). Follow along at [Stefanos's Stack](https://stefanoskarakasis.substack.com/).

## License

[MIT](LICENSE)
