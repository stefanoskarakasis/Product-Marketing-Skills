# Product Marketing Skills for AI Agents

19 PMM skills across 3 plugins. Built for Claude Code, Cowork, and any agent that supports the [Agent Skills spec](https://agentskills.io). From product marketing context to messaging, launches, and execution.

Designed for Claude Code and Cowork. Skills compatible with other AI assistants. Built by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

## Start Here

New to product marketing context? → `/setup-context`
Pressure-testing positioning? → `/position`
Planning a launch? → `/launch`
Building a battlecard? → `/compete`
Drafting a campaign brief? → `/brief`

If this project helps you, ⭐ the repo.

## Why Product Marketing Skills?

Generic AI gives you text. Product Marketing Skills gives you structure.

Each skill encodes a proven PMM framework — April Dunford positioning, Fletch PMM canvas, JTBD theory, GACCS briefs, Gary Klein pre-mortems — and walks you through it step by step. You get the rigor of established methodologies built into your daily workflow, not sitting on a bookshelf.

The result: better positioning, sharper launches, and stronger competitive intelligence — anchored to your specific company context, not generic templates.

## How It Works (Skills, Commands)

**Skills** are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PMM task. Some skills also work as reusable foundations that multiple commands share. Installing the marketplace gives you all PMM domains at once.

Skills are loaded automatically when relevant to the conversation — no explicit invocation needed. If needed (e.g., prioritizing skills over general knowledge), you can **force loading skills** with `/plugin-name:skill-name` or `/skill-name` (Claude will add the prefix).

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process. For example, `/launch` chains product-marketing-context → positioning-messaging → gtm-launch-planner together.

## How Skills Work Together

Skills reference each other and build on shared context. The `product-marketing-context` skill is the foundation — every other skill checks it first to understand your product, ICP, personas, positioning, and competitive landscape before doing anything.

```
                            ┌─────────────────────────────────────┐
                            │     product-marketing-context       │
                            │   (read by all other skills first)  │
                            └─────────────────┬───────────────────┘
                                              │
        ┌─────────────────┬───────────────────┼──────────────────┐
        ▼                 ▼                   ▼                  ▼
   ┌──────────┐      ┌──────────┐       ┌──────────┐       ┌──────────┐
   │Knowledge │      │Knowledge │       │ Toolkit  │       │Execution │
   │Foundation│      │Foundation│       │          │       │          │
   │ (apex)   │      │ (depth)  │       │          │       │          │
   ├──────────┤      ├──────────┤       ├──────────┤       ├──────────┤
   │ context  │      │ icp      │       │ writing- │       │ prd      │
   │ strategy │      │ personas │       │  asst    │       │ okrs     │
   │          │      │ position │       │ resume   │       │ retro    │
   │          │      │ proof    │       │ privacy  │       │ pre-mort │
   │          │      │ alts-map │       │ gaccs    │       │ stake-   │
   │          │      │ market   │       │          │       │  maps    │
   │          │      │ voice    │       │          │       │ priorit  │
   │          │      │          │       │          │       │ summary  │
   └──────────┘      └──────────┘       └──────────┘       └──────────┘
```

Commands use skills. Some skills serve multiple commands. Some skills (like `prioritization-frameworks` or `proof-points-claims`) are standalone references that Claude draws on whenever relevant — no command needed.

Commands are designed to flow into each other, matching the PMM workflow. After any command completes, it suggests relevant next commands — just follow the prompts.

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **Browse plugins** → **Personal** → **+**
3. Select **Add marketplace from GitHub**
4. Enter: `stefanoskarakasis/Product-Marketing-Skills`

All 3 plugins install automatically. You get both commands (`/launch`, `/compete`, etc.) and skills.

### Claude Code (CLI)

```bash
# Step 1: Add the marketplace
claude plugin marketplace add stefanoskarakasis/product-marketing-skills

# Step 2: Install plugins
claude plugin install pmm-knowledge-foundation@product-marketing-skills
claude plugin install pmm-toolkit@product-marketing-skills
claude plugin install pmm-execution@product-marketing-skills
```

### Other AI assistants (skills only)

The `skills/*/SKILL.md` files follow the universal skill format and work with any tool that reads it. Commands (`/slash-commands`) are Claude-specific.

| Tool | How to use | What works |
| --- | --- | --- |
| **Cursor** | Copy skill folders to `.cursor/skills/` | Skills only |
| **Codex CLI** | Copy skill folders to `.codex/skills/` | Skills only |
| **Gemini CLI** | Copy skill folders to `.gemini/skills/` | Skills only |
| **Windsurf** | Copy skill folders to `.windsurf/skills/` | Skills only |

```bash
# Example: copy all skills for Cursor
for plugin in pmm-*/; do
  cp -r "$plugin/skills/"* ~/.cursor/skills/ 2>/dev/null
done
```

---

## Skill Categories

### 1. pmm-knowledge-foundation — The Brain

> 8 skills, 1 command. The shared context layer every other PMM skill reads first.

The foundation of the marketplace. These skills build, maintain, and govern your `product-marketing-context.md` — the living source of truth for product, ICP, personas, positioning, competitive landscape, narrative pillars, and GTM priorities.

**Skills (8):**

* `product-marketing-context` — When the user wants to create or update their product marketing context document. The apex skill — every other skill in this repo reads this first.
* `product-marketing-strategy` — When the user wants to run the 7-exercise strategic thinking process that populates the context file (product context, personas + ICP, competitive landscape, positioning, narrative pillars, PMM advantages, GTM priorities).
* `ideal-customer-profile` — When the user wants to build, enrich, or pressure-test their ICP. Synthesizes PMF survey data, win/loss signals, and customer interviews into a living ICP that grounds all downstream PMM work.
* `buyer-personas` — When the user wants to build, map, or refine B2B SaaS buyer personas including the buying committee, JTBD profiles, and decision criteria.
* `positioning-messaging` — When the user wants to build a message house, write a positioning document, develop value props by segment, or pressure-test existing messaging against strategy.
* `proof-points-claims` — When the user wants to build, validate, or audit their claims registry — the canonical source of approved metrics, quotes, case studies, and forbidden claims.
* `alternatives-map` — When the user wants to map competitive alternatives or build April Dunford's named alternatives framework.
* `market-context` — When the user wants to capture market category, macro forces, buying triggers, and the narrative arc that makes the solution feel inevitable.
* `voice-tone` — When the user wants to build a brand voice and tone guide that adapts by buyer type and channel.

**Commands (1):**

* `/setup-context` — Bootstrap or update the product marketing context file. Stage-gated for pre-PMF, post-PMF, and mature companies.

**Examples:**

Skills:
* `Help me build the buyer committee map for our enterprise deals`
* `Pressure-test our ICP — we're losing more deals in healthcare than we expected`
* `Build a message house for our Champion persona, anchored to our positioning`

Commands:
* `/setup-context — Post-PMF B2B SaaS, FinTech vertical, mid-market focus`

---

### 2. pmm-toolkit — Beyond Core PMM Work

> 4 skills, 2 commands. The PMM utilities that don't fit into strategy or execution but ship work every week.

Resume tailoring for PMM job searches, jurisdiction-aware privacy policies, B2B writing review, and structured marketing briefs. The skills you reach for when you're not planning a launch or building a battlecard, but you still need PMM-grade output.

**Skills (4):**

* `writing-assistant` — When the user wants to rewrite, sharpen, or pressure-test any written communication for B2B tech. Slack messages, async updates, decision memos, PRDs, one-pagers, homepage copy, ads, or email campaigns.
* `pmm-resume` — When a Product Marketing Manager wants to review, tailor, or rebuild their resume for a specific PMM role (IC to VP, including AI PMM). Takes a JD and baseline resume, ranks bullets by impact fit, rebuilds in one pass.
* `privacy-policy` — When the user wants to draft a jurisdiction-aware privacy policy for any digital product. Covers GDPR, CCPA, UK GDPR obligations, cookie policy, and DPA requirements.
* `gaccs-brief` — When the user wants to build a GACCS marketing brief (Goals, Audience, Creative, Channels, Stakeholders) for any campaign, launch, content piece, or enablement asset.

**Commands (2):**

* `/tailor-resume` — Tailor a PMM resume to a specific job description.
* `/brief` — Build a GACCS brief for any marketing project.

**Examples:**

Skills:
* `Review my PMM resume against the Director of PMM role at [Company] [attach JD]`
* `Sharpen this Slack update to my CMO about Q2 launch readiness`
* `Draft a privacy policy for our SaaS product launching in the EU and California`

Commands:
* `/tailor-resume [attach resume + paste JD]`
* `/brief — Q2 product launch campaign for our enterprise tier`

---

### 3. pmm-execution — Day-to-Day PMM

> 7 skills, 4 commands. The skills that fire every week — PRDs, OKRs, launches, retros, and the operational work that compounds.

Day-to-day product marketing: PRDs with embedded Solution Stories, quarterly OKRs, structured GTM retros, pre-mortems, stakeholder maps, prioritization frameworks, and meeting summaries.

**Skills (7):**

* `product-requirement-doc` — When the user wants to build a complete PRD with an embedded Solution Story for cross-functional PM/PMM collaboration.
* `brainstorm-okrs` — When the user wants to set quarterly PMM OKRs, review existing OKRs, or stress-test KR quality.
* `retro` — When the user wants to run a structured GTM retrospective for a cross-functional squad. Anchored to OKRs and launch outcomes with a self-improving learning loop.
* `pre-mortem` — When the user wants to pressure-test a strategic plan before launching. PRD, product launch, pricing change, GTM pivot, or new market entry. Gary Klein methodology with five initiative types.
* `stakeholder-maps` — When the user wants to build a stakeholder political map for a launch or campaign. Identifies who can kill it, who can champion it, and what to say to each.
* `prioritization-frameworks` — When the user needs to prioritize PMM projects, score launches, or decide what gets GTM investment. Reference for nine frameworks with launch tier output logic.
* `interview-summary` — When the user wants to synthesize customer interview transcripts into structured discovery outputs. Anchored in JTBD theory with signal-level pattern detection and confidence scoring.

**Commands (4):**

* `/write-prd` — Create a PRD from a feature idea or problem statement.
* `/plan-okrs` — Brainstorm quarterly PMM OKRs.
* `/pre-mortem` — Pre-mortem risk analysis on a PRD or launch plan.
* `/sprint` — Sprint lifecycle (`plan|retro`).

**Examples:**

Skills:
* `Which prioritization framework should I use for a 50-item GTM backlog?`
* `Map our stakeholders for the Q2 platform launch — VP Sales is the wildcard`
* `Synthesize these 8 customer interview transcripts into JTBD signals`

Commands:
* `/write-prd Smart notification system that reduces alert fatigue for FinOps teams`
* `/plan-okrs Q2 PMM OKRs aligned to company-level revenue targets`
* `/pre-mortem Launch plan for our enterprise pricing tier [attach plan]`

---

## Roadmap

These plugins are in active development and will ship in future drops. The structure of the marketplace is built to scale — each new plugin will install alongside the existing ones without disrupting current setups.

* **pmm-go-to-market** — GTM strategy, beachhead segments, growth loops, GTM motions, objection handling, launch planning. (v1.1, Q3 2026)
* **pmm-competitive-intelligence** — Battlecards, signal monitoring, judgment logs, market command matrix, win/loss extraction. (v1.2, Q3 2026)
* **pmm-research** — Customer research, market research, segment analysis. (v2.0, Q4 2026)
* **pmm-marketing-growth** — Product naming, marketing ideas, North Star metrics. (v2.0, Q4 2026)

Want to influence what ships next? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) with your use case.

---

## About

This marketplace will evolve in tandem with PMM practices and LMM capabilities.

Selected skills based on the work of:

* April Dunford — [*Obviously Awesome*](https://www.aprildunford.com/obviously-awesome) and [*Sales Pitch*](https://www.aprildunford.com/sales-pitch-book)
* Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
* Emily Kramer — [*MKT1 Newsletter*](https://newsletter.mkt1.co/) (GACCS framework)
* Maja Voje — [*Go-To-Market Strategist*](https://gtmstrategist.com/)
* Paweł Huryn — [*The Product Compass Newsletter*](https://www.productcompass.pm/) (compounding skill architecture)
* Corey Haines — [*Marketing Skills*](https://github.com/coreyhaines31/marketingskills) (structural inspiration)
* Fletch PMM — [Anchor + Value Model canvas](https://www.fletchpmm.com/)
* Gary Klein — Pre-mortem methodology
* Roger L. Martin — [*Playing to Win*](https://www.amazon.com/Playing-Win-Expanded-Bonus-Articles/dp/B0F25SDYWV/)

Curated by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

## Contributing

Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding or improving skills.

## License

[MIT](./LICENSE) — Use these however you want.
