# PMM Skills Marketplace: Product Marketing Skills for AI Agents

A collection of AI agent skills focused on product marketing tasks. Built
for Product Marketing Managers, founders, and marketing leaders who want AI
agents to help with positioning, competitive intelligence, launch planning,
OKRs, experiments, and GTM strategy.

Designed for Claude Code and Cowork. Skills compatible with other AI assistants.

Built by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

Contributions welcome! Found a way to improve a skill or have a new one to
add? [Open a PR](CONTRIBUTING.md).

Run into a problem or have a question? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) — happy to help.

## What This Is

This is a Claude agent marketplace designed to streamline product
marketing tasks. The system operates on a foundational principle:
"Build your brain once (`product-marketing-context`). Every other skill
reads it. Zero repetition."

**The Brain System:**

Users establish a single context document — `/foundation/brain.md` —
that stores product context, ICP, positioning, voice and tone, market
context, and proof points across 6 sections. Every skill in this
marketplace reads this file before producing output, eliminating the
need to re-explain context across sessions.

## Why Product Marketing Skills?

**The problem:** every time you ask an AI agent for positioning,
battlecards, or briefs, you re-explain your company. By the fifth
conversation, you're copy-pasting from old chats.

**The solution:** build your brain once with `product-marketing-context`. Every other skill in this stack reads from `/foundation/brain.md` instead
of asking again.

## How It Works: Skills and Plugins

**Skills** are the building blocks. Each skill gives Claude domain
knowledge, a framework, or a guided workflow for a specific PMM task.

**Plugins** group related skills into installable packages, one per GTM
domain. This repo has seven plugins:

| Plugin | What it covers |
|---|---|
| `product-marketing-context` | The brain |
| `pmm-positioning` | Positioning and messaging |
| `pmm-go-to-market` | GTM strategy, launch tiering, workflow orchestration |
| `pmm-execution` | Day-to-day PMM work: PRDs, OKRs, retros, pre-mortems |
| `pmm-growth` | Growth ideation and measurement: a North Star Metric and capped scorecard, pre-commitment positioning angles, brain-grounded campaign ideas, and value-prop variants |
| `pmm-toolkit` | Utilities: writing assistant, resume review, privacy policy, GACCS briefs |
| `pmm-meta` | Skills that operate on the skill system itself |

## The Foundation: `product-marketing-context`

Every other skill in this repo checks `/foundation/brain.md` first to
understand your product, ICP, positioning, and competitive landscape before
doing anything. Build it once with the `product-marketing-context` skill;
every other skill reads from it.

## Available Skills (34 Total)

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
| [gaccs-brief](pmm-toolkit/skills/gaccs-brief/) | pmm-toolkit | Campaign briefs (Goals, Audience, Creative, Channels, Stakeholders) |
| [writing-assistant](pmm-toolkit/skills/writing-assistant/) | pmm-toolkit | Sharpen any written communication |
| [pmm-resume](pmm-toolkit/skills/pmm-resume/) | pmm-toolkit | Resume tailoring for PMM roles |
| [privacy-policy](pmm-toolkit/skills/privacy-policy/) | pmm-toolkit | GDPR/CCPA-aware privacy policies |
| [experiment-doc](pmm-execution/skills/experiment-doc/) | pmm-execution | Growth experiments, A/B tests, hypotheses |
| [positioning-ideas](pmm-growth/skills/positioning-ideas/) | pmm-growth | Divergent, ungated positioning angles before committing to positioning-messaging |
| [experiment-ideas](pmm-growth/skills/experiment-ideas/) | pmm-growth | Brain-grounded growth ideas: channel, message, cost-efficiency, ranked |
| [value-prop-statements](pmm-growth/skills/value-prop-statements/) | pmm-growth | Segment-specific value-prop variants of an already-set positioning |
| [pmm-metrics](pmm-growth/skills/pmm-metrics/) | pmm-growth | North Star Metric (7-criteria validated) + capped scorecard across 4 categories |
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
| [meta-synthesis](pmm-meta/meta-synthesis/) | pmm-meta | Pattern detection across skill sessions |
| [meta-learn](pmm-meta/meta-learn/) | pmm-meta | Captures post-session learnings |
| [meta-review](pmm-meta/meta-review/) | pmm-meta | Audits skills against `SKILL-SPEC.md` |
| [meta-verify](pmm-meta/meta-verify/) | pmm-meta | Quality gate on skill output |

## Installation

### Option 1: Claude Code / Cowork Plugin Marketplace

```bash
/plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
/plugin install product-marketing-context
/plugin install pmm-positioning
/plugin install pmm-toolkit
/plugin install pmm-execution
/plugin install pmm-go-to-market
/plugin install pmm-growth
/plugin install pmm-meta
```

Connectors load per plugin, so install the plugins individually as above. Install `product-marketing-context` first — every other plugin reads the brain it
builds. `pmm-meta` can be installed alongside any combination of the
others; it doesn't depend on which ones you have.

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

| Plugin | Connectors wired |
|---|---|
| product-marketing-context | Notion, Atlassian, HubSpot, Fireflies, Gong, SimilarWeb, Intercom, Slack, Google Drive, Google Docs, Google Sheets, Google Slides |
| pmm-positioning | Fireflies, Gong, HubSpot, SimilarWeb, Intercom, Notion, Atlassian, Ahrefs, Slack, Google Drive, Google Docs, Google Slides |
| pmm-execution | Fireflies, Gong, Notion, Atlassian, Linear, Figma, Canva, Slack, Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides |
| pmm-go-to-market | HubSpot, SimilarWeb, Fireflies, Gong, Slack, Klaviyo, Supermetrics, Canva, Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides |
| pmm-growth | Amplitude (US and EU), Pendo, SimilarWeb, Ahrefs, HubSpot, Klaviyo, Supermetrics, Google Drive, Google Sheets |
| pmm-toolkit | Notion, Atlassian, Slack, Canva, Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides |
| pmm-meta | None |

Some connectors need extra access: SimilarWeb and Ahrefs need an API plan,
Gong usually needs an admin to enable it, and G2 and other review sites are
paste-only. Install each plugin on its own to load its connectors (see Installation). Sign-in steps: [docs/connect-your-tools.md](docs/connect-your-tools.md). Category registry: [CONNECTORS.md](CONNECTORS.md).

## Workflow Intelligence

`workflow-orchestrator` (in `pmm-go-to-market`) chains multiple skills
into one coherent, end-to-end program — a Program Charter, sequenced
skill runs, coherence checks between their outputs, and one master
document at the end.

## Usage

Once installed, ask your agent to help with PMM tasks:

- "Build my ICP from these customer interviews"
- "Map the alternatives my buyers consider and how we compare"
- "Plan the launch for our new feature as a Tier 2 launch"
- "Run a retro on last quarter's launch"

Or call a skill directly, for example `/pmm-positioning:ideal-customer-profile`.

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

- **April Dunford**, *Obviously Awesome*: positioning
- **Jobs to Be Done** theory: customer needs and switching behavior
- **Intercom**: RICE prioritization
- **Noriaki Kano**: the Kano model
- **ICE scoring**: lightweight experiment prioritization
- **Paweł Huryn**: the self-improving memory loop, and the plugin structure of [pm-skills](https://github.com/phuryn/pm-skills)
- **Anthropic**: [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins), the model for plugin and connector layout

Curated by [Stefanos Karakasis](https://stefanoskarakasis.substack.com/). Subscribe to the newsletter for new skills, templates, and PMM playbooks.

## License

[MIT](LICENSE)
