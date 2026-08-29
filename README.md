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
| `product-marketing-context` | The brain |
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

## Available Skills (24 Total)

| Skill | Plugin | Description |
|-------|--------|-------------|
| [product-marketing-context](product-marketing-context/) | product-marketing-context | Build or audit your GTM brain |
| [ideal-customer-profile](pmm-positioning/skills/ideal-customer-profile/) | pmm-positioning | ICP from research: demographics, behaviors, JTBD, needs |
| [buyer-personas](pmm-positioning/skills/buyer-personas/) | pmm-positioning | Buying committee map + alternatives-anchored persona cards |
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
/plugin install pmm-meta
```

Install `product-marketing-context` first — every other plugin reads the brain it
builds. `pmm-meta` can be installed alongside any combination of the
others; it doesn't depend on which ones you have.

## Workflow Intelligence

`workflow-orchestrator` (in `pmm-go-to-market`) chains multiple skills
into one coherent, end-to-end program — a Program Charter, sequenced
skill runs, coherence checks between their outputs, and one master
document at the end.

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
