# PMM Skills Marketplace: Product Marketing Skills for AI Agents

A collection of AI agent skills focused on product marketing tasks. Built
for Product Marketing Managers, founders, and marketing leaders who want AI
agents to help with positioning, competitive intelligence, launch planning,
OKRs, experiments, and GTM strategy.

Works with Claude Code, Claude Cowork, Cursor, Windsurf, and any agent that
supports the [Agent Skills spec](https://agentskills.io/).

Built by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

Contributions welcome! Found a way to improve a skill or have a new one to
add? [Open a PR](CONTRIBUTING.md).

Run into a problem or have a question? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) — happy to help.

## What This Is

Build your product marketing brain once, in `product-marketing-context`.
Every other skill in this repo reads it before producing output. No
re-explaining your company, your buyer, or your competitors every time.

**Status note:** cross-skill "compounding" (skills automatically logging
session data and getting smarter from prior runs) is a design goal for this
repo, not a shipped feature yet. Today, each skill reads
`/foundation/brain.md` directly for shared context. Automatic session
logging and pattern detection across skills is on the roadmap — see
`product-marketing-context/ROADMAP.md`.

## Why Product Marketing Skills?

**The problem:** every time you ask an AI agent for positioning,
battlecards, or briefs, you re-explain your company. By the fifth
conversation, you're copy-pasting from old chats.

**The solution:** build your brain once with `product-marketing-context`.
Every other skill in this stack reads from `/foundation/brain.md` instead
of asking again.

## How It Works: Skills and Plugins

**Skills** are the building blocks. Each skill gives Claude domain
knowledge, a framework, or a guided workflow for a specific PMM task.

**Plugins** group related skills into installable packages, one per GTM
domain. This repo has six plugins:

| Plugin | What it covers |
|---|---|
| `pmm-foundation` | The brain — `product-marketing-context` |
| `pmm-positioning` | Positioning and messaging |
| `pmm-go-to-market` | GTM strategy, launch tiering, workflow orchestration |
| `pmm-execution` | Day-to-day PMM work: PRDs, OKRs, retros, pre-mortems |
| `pmm-toolkit` | Utilities: writing assistant, resume review, privacy policy, GACCS briefs |
| `pmm-meta` | Skills that operate on the skill system itself |

## The Foundation: `product-marketing-context`

Every other skill in this repo checks `/foundation/brain.md` first to
understand your product, ICP, positioning, and competitive landscape before
doing anything. Build it once with the `product-marketing-context` skill;
every other skill reads from it.

## Available Skills (21 Total)

| Skill | Plugin | Description |
|-------|--------|-------------|
| [product-marketing-context](product-marketing-context/) | pmm-foundation | Build or audit your GTM brain |
| [positioning-messaging](pmm-positioning/skills/positioning-messaging/) | pmm-positioning | Positioning statements, message house, homepage copy |
| [gaccs-brief](pmm-toolkit/skills/gaccs-brief/) | pmm-toolkit | Campaign briefs (Goals, Audience, Creative, Channels, Stakeholders) |
| [writing-assistant](pmm-toolkit/skills/writing-assistant/) | pmm-toolkit | Sharpen any written communication |
| [pmm-resume](pmm-toolkit/skills/pmm-resume/) | pmm-toolkit | Resume tailoring for PMM roles |
| [privacy-policy](pmm-toolkit/skills/privacy-policy/) | pmm-toolkit | GDPR/CCPA-aware privacy policies |
| [experiment-doc](pmm-execution/skills/experiment-doc/) | pmm-execution | Growth experiments, A/B tests, hypotheses |
| [interview-summary](pmm-execution/skills/interview-summary/) | pmm-execution | Customer discovery synthesis using JTBD |
| [prd](pmm-execution/skills/prd/) | pmm-execution | Product requirements docs with embedded Solution Stories |
| [pre-mortem](pmm-execution/skills/pre-mortem/) | pmm-execution | Cross-functional risk analysis |
| [retro](pmm-execution/skills/retro/) | pmm-execution | Post-launch retrospectives |
| [pmm-okrs](pmm-execution/skills/pmm-okrs/) | pmm-execution | Quarterly OKR building |
| [stakeholder-maps](pmm-execution/skills/stakeholder-maps/) | pmm-execution | Political maps: champions, blockers |
| [prioritization-frameworks](pmm-execution/skills/prioritization-frameworks/) | pmm-execution | Score initiatives (RICE, ICE, Kano, and more) |
| [go-to-market-strategy](pmm-go-to-market/skills/go-to-market-strategy/) | pmm-go-to-market | Launch tier assignment, GTM strategy briefs |
| [beachhead-segment](pmm-go-to-market/skills/beachhead-segment/) | pmm-go-to-market | First customer wedge scoring |
| [workflow-orchestrator](pmm-go-to-market/skills/workflow-orchestrator/) | pmm-go-to-market | Chains multiple skills into full GTM programs |
| [meta-synthesis](pmm-meta/meta-synthesis/) | pmm-meta | Pattern detection across skill sessions (in development) |
| [meta-learn](pmm-meta/meta-learn/) | pmm-meta | Captures post-session learnings |
| [meta-review](pmm-meta/meta-review/) | pmm-meta | Audits skills against `SKILL-SPEC.md` |
| [meta-verify](pmm-meta/meta-verify/) | pmm-meta | Quality gate on skill output |

## Installation

### Option 1: Claude Code / Cowork Plugin Marketplace

```bash
/plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
/plugin install pmm-foundation
/plugin install pmm-positioning
/plugin install pmm-go-to-market
/plugin install pmm-execution
/plugin install pmm-toolkit
/plugin install pmm-meta
```

Install only the plugins you need — `pmm-foundation` is recommended first
since every other plugin reads from the brain it builds.

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

## Usage

Once installed, ask your agent to help with PMM tasks:

```
"Build my brain"
→ Uses go-to-market-strategy skill

"Generate positioning for our platform"
→ Uses positioning-messaging skill

"Build a competitive battlecard for Okta"
→ Uses competitive-battlecard skill

"Build Q3 OKRs for my team"
→ pmm-okrs

"Create a GACCS campaign brief"
→ Uses gaccs-brief skill

"Run meta-synthesis to detect patterns"
→ Reads all execution logs, proposes guardrails + brain updates
```

You can also invoke skills directly with commands:

```
"What tier is this feature?"
/go-to-market-strategy

"Build positioning for B2B SaaS"
/positioning-messaging 

"Run retrospective for last launch"
/retro 

"Generate Q4 OKRs"
/pmm-okrs 

"Run monthly meta-synthesis"
/pmm-meta:synthesis
```


Skills that read the brain do so automatically once it's been built — no
need to re-explain context each time.

## About

This marketplace draws on the work of:

* April Dunford — [*Obviously Awesome*](https://www.aprildunford.com/obviously-awesome) and [*Sales Pitch*](https://www.aprildunford.com/sales-pitch-book)
* Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
* Emily Kramer — [*MKT1 Newsletter*](https://newsletter.mkt1.co/)
* Maja Voje — [*Go-To-Market Strategist*](https://gtmstrategist.com/)
* Paweł Huryn — [*The Product Compass Newsletter*](https://www.productcompass.pm/)
* Corey Haines — [*Marketing Skills*](https://github.com/coreyhaines31/marketingskills)
* Fletch PMM — [*Anchor + Value Model canvas*](https://www.fletchpmm.com/)
* Gary Klein — Pre-mortem methodology
* Roger L. Martin — [*Playing to Win*](https://www.amazon.com/Playing-Win-Expanded-Bonus-Articles/dp/B0F25SDYWV/)

Curated by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SKILL-SPEC.md](SKILL-SPEC.md)
for the skill-authoring standard every skill in this repo should meet.

## License

[MIT](./LICENSE) — use these however you want.
