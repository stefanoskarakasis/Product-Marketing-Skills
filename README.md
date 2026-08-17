# Product Marketing Skills for AI Agents

A collection of AI agent skills focused on product marketing tasks. Built for Product Marketing Managers, founders, and marketing leaders who want AI agents to help with positioning, competitive intelligence, launch planning, OKRs, experiments, and GTM strategy.

Works with Claude Code, Claude Cowork, Cursor, Windsurf, and any agent that supports the [Agent Skills spec](https://agentskills.io/).

Built by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

New to skills and agents? Start with the **Quick Start** section above or jump to **Installation**.

Contributions welcome! Found a way to improve a skill or have a new one to add? [Open a PR](#contributing).

Run into a problem or have a question? [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) — we're happy to help.

## What This Is

Build your product marketing brain once. Every other skill reads it. No re-explaining. No copy-pasting from old chats. Sharper positioning, consistent messaging, smarter launches.

**NEW:** The system learns over time. By month 3, meta-synthesis detects patterns across all your work and updates guardrails automatically.

## See It in Action (90 Seconds)

Don't want to commit 15 minutes to setup before seeing value?

→ **[Read the 90-Second Quick Start](./QUICK-START.md)**

Run one skill, get one output, see how the system works. Then decide if you want the full brain setup.

Already convinced? Jump to [Installation](#installation) below.

## Start Here

Setting up your Product Marketing Context? → `/setup-context`\
Pressure-testing positioning? → `/position`\
Planning a launch? → `/plan-launch`\
Building a battlecard? → `/compete`\
Drafting a campaign brief? → `/brief`\
Detecting patterns in your work? → `/pmm-meta:synthesis`\

If this project helps you, ⭐ the repo.

## Why Product Marketing Skills?

**The problem:** Every time you ask Claude for positioning, battlecards, or briefs, you re-explain your company. By session #5, you're copy-pasting from previous chats.

**The solution:** Build your brain once (`product-marketing-context`). Every other skill reads it. Zero repetition.

The result: better positioning, sharper launches, and stronger competitive intelligence — anchored to your specific company context, not generic templates.

**Results**
- ✅ 10x faster (no re-explaining context)
- ✅ Consistent messaging (all skills read the same source)
- ✅ Compound intelligence (skills reference each other's outputs)
- ✅ **System learns over time** — meta-synthesis detects patterns across all your work and updates guardrails monthly

## How It Works: Skills, Commands, and the Compounding Loop

### Skills & Commands

**Skills** are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PMM task.

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process.

**Plugins** group related skills and commands into installable packages covering specific GTM domains.

### The Compounding Loop (NEW)

This system isn't just a collection of tools—it's a **self-improving operating system**. Every execution teaches the system. By month 3, it knows more about your GTM than you do.

```
Month 1: Baseline
└─ Run execution skills (experiments, retros, OKRs, interviews)
   └─ Each skill logs session data to /context/skill-sessions.md
      └─ System collects patterns
         └─ Monthly meta-synthesis runs
            └─ Detects patterns (2+ occurrences = guardrail)
               └─ Proposes guardrails + brain updates
                  └─ You approve/reject via gates

Month 2: Compound
└─ Run execution skills again
   └─ Each skill loads guardrails from meta-synthesis at pre-flight (Step 0)
      └─ Inputs are smarter (guided by prior learnings)
         └─ Outputs are higher quality
            └─ Meta-synthesis detects new patterns
               └─ Guardrails + brain update again
                  └─ System gets smarter

Month 3+: Exponential
└─ Every execution is informed by every prior execution
   └─ System knows your GTM blindspots
      └─ System knows what risks to watch
         └─ System knows your confidence calibration
            └─ System makes better decisions than you could manually
```

**What gets stored and reused:**

- `/context/skill-sessions.md` — Master log of all skill executions (logs from experiment-doc, interview-summary, retro, pmm-okrs, pre-mortem, prd, prioritization, stakeholder-maps)
- `/context/meta-patterns.md` — Master guardrails file (written by meta-synthesis, read by all execution skills at pre-flight)
- `/foundation/brain.md` Sections 2, 5, 7 — Updated by meta-synthesis with learnings (anti-ICP signals, revenue lever adjustments, system patterns)

**Core monthly workflow:**

1. Run execution skills throughout the month (30+ days of data)
2. End of month: run `/pmm-meta:synthesis`
3. Meta-synthesis detects patterns, proposes guardrails + brain updates
4. You approve/reject via approval gates
5. Next month: execution skills load updated guardrails → outputs are smarter
6. Repeat. System compounds.

---

## How Skills Work Together

Your skills cascade. Each reads your brain (the shared context layer), produces output, and stores learnings. The next skill is smarter because it inherited context from the last one.

<img width="2534" height="795" alt="image" src="https://github.com/user-attachments/assets/1ea0d18b-a7ca-4ef8-b661-87be076fa359" />

Skills reference each other and build on shared context. The `product-marketing-context` skill is the foundation — every other skill checks it first to understand your product, ICP, personas, positioning, and competitive landscape before doing anything.

```
┌──────────────────────────────────┐
│  product-marketing-context       │
│ (read by all other skills first) │
└───────────────┬──────────────────┘
                │
┌──────────────┬──────────┬──┼──┬──────────────┬──────────────┬──────────────┐
▼              ▼          ▼  ▼  ▼              ▼              ▼              ▼
┌──────────────┐ ┌────────┐ ┌──────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Foundation   │ │Execution│ │Go-to-│ │ Positioning  │ │   Toolkit    │ │  Meta Layer  │
│              │ │         │ │Market│ │              │ │              │ │(Self-Improve)│
├──────────────┤ ├─────────┤ ├──────┤ ├──────────────┤ ├──────────────┤ ├──────────────┤
│product-      │ │prd      │ │gtm-  │ │positioning-  │ │writing-      │ │meta-         │
│marketing-    │ │okrs     │ │strat-│ │messaging     │ │assistant     │ │synthesis     │
│context       │ │pre-     │ │egy   │ │              │ │pmm-resume    │ │meta-learn    │
│              │ │mortem   │ │work- │ │              │ │privacy-      │ │meta-review   │
│              │ │retro    │ │flow- │ │              │ │policy        │ │meta-verify   │
│              │ │experi-  │ │orch  │ │              │ │gaccs-brief   │ │              │
│              │ │ment-doc │ │      │ │              │ │              │ │Logs all      │
│              │ │inter-   │ │      │ │              │ │              │ │execution     │
│              │ │view-sum │ │      │ │              │ │              │ │detects       │
│              │ │stake-   │ │      │ │              │ │              │ │patterns      │
│              │ │holder   │ │      │ │              │ │              │ │proposes      │
│              │ │priorit- │ │      │ │              │ │              │ │guardrails    │
│              │ │ization  │ │      │ │              │ │              │ │updates brain │
│              │ │          │ │      │ │              │ │              │ │              │
│ Skill: 1     │ │Skills: 8 │ │Skills:2 │ Skills: 1   │ │ Skills: 4    │ │ Skills: 4    │
└──────────────┘ └─────────┘ └──────┘ └──────────────┘ └──────────────┘ └──────────────┘
        │             │          │         │              │              │
        └─────────────┴──────────┴─────────┴──────────────┴──────────────┘
                                  ↓
                All outputs → logged → meta-synthesis reads → learns → updates brain
                            (feedback loop, monthly cadence)
```

Commands use skills. Some skills serve multiple commands. Some skills (like `prioritization-frameworks` or `proof-points-claims`) are standalone references that Claude draws on whenever relevant — no command needed.

Commands are designed to flow into each other, matching the PMM workflow. After any command completes, it suggests relevant next commands — just follow the prompts.

---

## Available Skills (22 Total)

| Skill | Description | Reads From | Writes To |
|-------|-------------|-----------|----------|
| [product-marketing-context](product-marketing-context/) | Build or audit your brain | N/A | `/foundation/brain.md` |
| [positioning-messaging](pmm-positioning/skills/positioning-messaging/) | Positioning statements, message house, homepage copy (5 output modes) | ICP, Competitors | `brain Section 3` |
| [gaccs-brief](pmm-toolkit/skills/gaccs-brief/) | Campaign briefs (Goals, Audience, Creative, Channels, Stakeholders) | Positioning, Brain | `/campaigns/` |
| [writing-assistant](pmm-toolkit/skills/writing-assistant/) | Sharpen any written communication | Voice guide, Positioning | (in-place edits) |
| [experiment-doc](pmm-execution/skills/experiment-doc/) | Growth experiments, A/B tests, hypotheses | Brain, `/context/experiments/` | `/context/skill-sessions.md` (NEW) |
| [interview-summary](pmm-execution/skills/interview-summary/) | Customer discovery using JTBD | Transcripts, Brain | `/context/skill-sessions.md` (NEW) |
| [prd](pmm-execution/skills/prd/) | Product requirements, Solution Stories | Brain, Positioning | `/docs/prd/` |
| [pre-mortem](pmm-execution/skills/pre-mortem/) | Risk analysis, cross-functional alignment | Brain, `/context/meta-patterns.md` (NEW) | `/context/skill-sessions.md` (NEW) |
| [retro](pmm-execution/skills/retro/) | Post-launch retrospectives, learnings | Brain, Launch data | `/context/skill-sessions.md` (NEW) |
| [pmm-okrs](pmm-execution/skills/pmm-okrs/) | Quarterly OKR building | Brain, Prior OKRs | `brain Section 7` + `/context/skill-sessions.md` (NEW) |
| [stakeholder-maps](pmm-execution/skills/stakeholder-maps/) | Political maps (champions, blockers) | Brain, Prior maps | `/context/skill-sessions.md` (NEW) |
| [prioritization-frameworks](pmm-execution/skills/prioritization-frameworks/) | Score initiatives (RICE, ICE, Kano, etc.) | Brain, Initiatives | `/analysis/` |
| [go-to-market-strategy](pmm-go-to-market/skills/go-to-market-strategy/) | GTM strategy, launch tier assignment | Brain, Positioning, Competitive | `brain Section 7` |
| [beachhead-segment](pmm-go-to-market/skills/beachhead-segment/) | First customer wedge scoring | ICP, Brain | `brain Section 2` |
| [workflow-orchestrator](pmm-go-to-market/skills/workflow-orchestrator/) | Full launch workflows (10 types) | Brain, All above | `brain + /artifacts/` |
| [meta-synthesis](pmm-meta/skills/meta-synthesis/) | **NEW** Pattern detection across all skills, guardrail proposals, brain updates | `/context/skill-sessions.md`, brain | `/context/meta-patterns.md`, brain Sections 2, 5, 7 |
| [meta-learn](pmm-meta/skills/meta-learn/) | Capture post-session learnings | Skill outputs | Knowledge base |
| [meta-review](pmm-meta/skills/meta-review/) | Audit skills against SKILL-SPEC | All SKILL.md files | Gap list + fixes |
| [meta-verify](pmm-meta/skills/meta-verify/) | Quality gate on T1 skill output | Skill outputs | Verification report |
| [pmm-resume](pmm-toolkit/skills/pmm-resume/) | Resume tailoring for PMM roles | Your resume, JD | Tailored resume |
| [privacy-policy](pmm-toolkit/skills/privacy-policy/) | GDPR/CCPA-compliant privacy policies | Product data | `policy.md` |
| [competitive-battlecard](pmm-execution/skills/competitive-battlecard/) | Competitive positioning vs named rival | Brain, Positioning, Competitors | `/battlecards/` |

> Each skill reads from the "Reads From" column to produce output in "Writes To". This data flow is how the system compounds — outputs from one skill become inputs to the next. **NEW execution skills (experiment-doc, interview-summary, pre-mortem, retro, pmm-okrs, stakeholder-maps) now log to `/context/skill-sessions.md` so meta-synthesis can read and detect patterns across all your work.**

## Installation

Pick any method below. All work with Claude Code CLI, Cursor, Cowork, and Windsurf.

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install skills directly:

```bash
# Install all skills
npx skills add stefanoskarakasis/Product-Marketing-Skills

# Install specific skills
npx skills add stefanoskarakasis/Product-Marketing-Skills --skill positioning-messaging experiment-doc

# List available skills
npx skills add stefanoskarakasis/Product-Marketing-Skills --list
```

This automatically installs to your `.agents/skills/` directory (and symlinks into `.claude/skills/` for Claude Code compatibility).

### Option 2: Claude Cowork Plugin

Install via Claude Cowork's built-in plugin system:

```bash
# Add the marketplace
/plugin marketplace add stefanoskarakasis/Product-Marketing-Skills

# Install all PMM skills
/plugin install pmm-skills
```

### Option 3: Clone and Copy

Clone the entire repo and copy the skills folder:

```bash
git clone https://github.com/stefanoskarakasis/Product-Marketing-Skills.git
cp -r Product-Marketing-Skills/skills/* .agents/skills/
```

### Option 4: Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/stefanoskarakasis/Product-Marketing-Skills.git .agents/pmm-skills
```

Then reference skills from `.agents/pmm-skills/skills/`.

### Option 5: Fork and Customize

1. Fork this repository
2. Customize skills for your specific PMM needs
3. Clone your fork into your projects

### Option 6: SkillKit (Multi-Agent)

Use [SkillKit](https://github.com/rohitg00/skillkit) to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):

```bash
# Install all skills
npx skillkit install stefanoskarakasis/Product-Marketing-Skills

# Install specific skills
npx skillkit install stefanoskarakasis/Product-Marketing-Skills --skill positioning-messaging experiment-doc

# List available skills
npx skillkit install stefanoskarakasis/Product-Marketing-Skills --list
```

## Usage

Once installed, just ask your agent to help with PMM tasks:

```
"Help me plan a product launch for SSO integration"
→ Uses go-to-market-strategy skill

"Generate positioning for our platform"
→ Uses positioning-messaging skill

"Build a competitive battlecard for Okta"
→ Uses competitive-battlecard skill

"Run Q3 quarterly PMM cycle"
→ Uses workflow-orchestrator skill

"Create a GACCS campaign brief"
→ Uses gaccs-brief skill

"Run meta-synthesis to detect patterns"
→ Reads all execution logs, proposes guardrails + brain updates
```

You can also invoke skills directly with commands:

```
"Run full launch workflow for [product]"
/workflow-orchestrator

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

Skills read your brain automatically — zero context re-explaining.

---

## Skill Categories: How They Chain Together

These skills are organized by domain, but they're designed to flow into each other. After any skill completes, it suggests the next logical step.

<details>
<summary><strong>1. product-marketing-context</strong> — The Brain: setup wizard, health audit, compound intelligence (1 skill, 5 commands)</summary>

The foundation of the marketplace. Setup wizard + health audit. Creates `/foundation/brain.md` — the shared context layer every other PMM skill reads first.

### Skills (1):

- **product-marketing-context** — When the user wants to create or update their product marketing context document. The apex skill — every other skill in this repo reads this first.

### Commands (5):

- `/product-marketing-context:setup-brain` — Bootstrap or update the product marketing context file. Stage-gated for pre-PMF, post-PMF, and mature companies.
- `/product-marketing-context:brain-audit` — Run brain health diagnostics (0-100 score) with recommendations
- `/product-marketing-context:brain-view` — Display brain contents
- `/product-marketing-context:brain-export` — Export brain as markdown
- `/product-marketing-context:brain-reset` — Delete brain and start fresh

### Examples:

**Skills:**
- `Set up my PMM brain`
- `Check my brain health`
- `What's in my brain?`

**Commands:**
- `/product-marketing-context:setup-brain` — Post-PMF B2B SaaS, mid-market focus
- `/product-marketing-context:brain-audit` — We're losing more deals in healthcare than we expected

</details>

<details>
<summary><strong>2. pmm-positioning</strong> — Positioning & messaging: Dunford framework, message house, homepage copy, sales decks, audit mode (1 skill, 5 commands)</summary>

Strategic positioning using April Dunford's Obviously Awesome framework. Generates positioning statements, messaging hierarchies, homepage copy across 5 output modes.

### Skills (1):

- **positioning-messaging** — When the user wants to build a message house, write a positioning document, develop value props by segment, or pressure-test existing messaging against strategy.

### Commands (5):

- `/pmm-positioning:build` — Positioning statement + full 4-layer messaging document
- `/pmm-positioning:audit` — Scored audit + prioritized rewrite queue with before/after
- `/pmm-positioning:fletch` — 6-slide internal positioning deck + homepage wireframe
- `/pmm-positioning:sales-enablement` — Persona cards + competitive response guide
- `/pmm-positioning:homepage` — Production-ready headline, subhead, pillars, CTA — no placeholders

### Examples:

**Skills:**
- `Generate positioning for our platform`
- `Audit our current messaging — we sound like everyone else`
- `Create homepage copy in HOMEPAGE mode`

**Commands:**
- `/pmm-positioning:build` — Mid-market B2B SaaS targeting marketing ops teams
- `/pmm-positioning:audit` — Our messaging doc from Q2 (attach file)
- `/pmm-positioning:homepage` — Use positioning from brain Section 7

</details>

<details>
<summary><strong>3. pmm-toolkit</strong> — Writing assistant, resume tailoring, privacy policy generator, GACCS campaign briefs (4 skills, 4 commands)</summary>

PMM utilities: writing assistant, resume review, privacy policy, GACCS briefs.

### Skills (4):

- **writing-assistant** — Rewrites copy to match brand voice and checks against positioning
- **pmm-resume** — Reviews and tailors PMM resumes for specific roles
- **privacy-policy** — Generates jurisdiction-aware privacy policies
- **gaccs-brief** — Creates campaign briefs (Goals, Audience, Creative, Channels, Stakeholders)

### Commands (4):

- `/pmm-toolkit:rewrite` — Rewrite copy to match brand voice
- `/pmm-toolkit:tailor-resume` — Tailor resume for specific PMM role
- `/pmm-toolkit:privacy-policy` — Generate privacy policy for product
- `/pmm-toolkit:gaccs-brief` — Create campaign brief

### Examples:

**Skills:**
- `Rewrite this homepage hero to match our voice`
- `Review my PMM resume for a Director role at Stripe`
- `Create privacy policy for our B2B SaaS product (US + EU)`
- `Build GACCS brief for Q4 product launch`

**Commands:**
- `/pmm-toolkit:rewrite` — Make this email more concise and authoritative
- `/pmm-toolkit:tailor-resume` — [paste resume] + [paste JD]
- `/pmm-toolkit:gaccs-brief` — Campaign: Series B announcement

</details>

<details>
<summary><strong>4. pmm-execution</strong> — PRDs, OKRs, experiments, pre-mortems, retros, stakeholder maps, prioritization, interview synthesis (8 skills, 8 commands)</summary>

Day-to-day product marketing: PRDs, growth experiments, OKRs, pre-mortems, retrospectives, stakeholder management, meeting summaries, and prioritization frameworks.

**All execution skills now load guardrails from meta-synthesis at pre-flight (Step 0) and log session data for meta-synthesis to read and learn from.**

### Skills (8):

- **stakeholder-maps** — Build political stakeholder maps for launches and GTM initiatives
- **retro** — Facilitate structured GTM retrospectives with cross-functional teams
- **prioritization-frameworks** — Apply 9 GTM-native prioritization frameworks (RICE, ICE, etc.)
- **pre-mortem** — Run pre-mortem risk analysis on strategic projects
- **pmm-okrs** — Build quarterly OKR sets for PMM teams
- **prd** — Create HubSpot-style PRDs with embedded Solution Stories
- **experiment-doc** — Build, audit, and score growth experiment documents
- **interview-summary** — Summarize customer interviews with JTBD analysis

### Commands (8):

- `/pmm-execution:stakeholder-map` — Build stakeholder map for launch or initiative
- `/pmm-execution:retro` — Facilitate post-launch or sprint retrospective
- `/pmm-execution:prioritize` — Score and rank initiatives using prioritization frameworks
- `/pmm-execution:pre-mortem` — Run pre-mortem risk analysis
- `/pmm-execution:okrs` — Build quarterly PMM OKR set
- `/pmm-execution:prd` — Create product requirements document
- `/pmm-execution:experiment` — Build growth experiment document
- `/pmm-execution:interview-summary` — Summarize interview transcript

### Examples:

**Skills:**
- `Build stakeholder map for Q4 product launch`
- `Run a retro on our last launch`
- `Help me prioritize these 5 feature ideas using RICE`
- `Create a PRD for our new dashboard feature`
- `Build Q3 OKRs for my 3-person PMM team`
- `Pre-mortem: we're raising prices 40% next quarter`
- `Score this experiment: changing homepage headline to outcomes-focused`
- `Summarize this customer interview transcript`

**Commands:**
- `/pmm-execution:stakeholder-map` — Q4 enterprise launch
- `/pmm-execution:retro` — Last sprint (Apr 15-30)
- `/pmm-execution:experiment` — Pricing page A/B test
- `/pmm-execution:okrs` — Solo PMM at Series B, low seller adoption
- `/pmm-execution:prd` — Analytics dashboard for marketing ops teams

### How Logging Works (NEW):

Every execution skill logs session data automatically:

```yaml
skill: retro
session_date: 2026-06-21
quality_score: 78
guardrails_triggered: 2
risks_materialized: 2
pre_mortem_accuracy: 67%
brain_updates_proposed: 1
```

This data feeds into meta-synthesis, which detects patterns:
- "Pre-mortem accuracy is 67% → let's refine the process"
- "Champion alignment gap appeared 4 times → add to guardrails"
- "Post-sales prep underestimated twice → give users more time"

Each pattern becomes a guardrail that next month's skills load at pre-flight (Step 0).

</details>

<details>
<summary><strong>5. pmm-meta</strong> — **NEW** Self-improving system: meta-synthesis, meta-learn, meta-review, meta-verify (4 skills, 8 commands)</summary>

**The meta layer that makes your entire system self-improving.** Reads execution logs, detects patterns, proposes guardrails and brain updates, gates approval before write.

### Skills (4):

- **meta-synthesis** (v1.0.0) — Monthly pattern detection across all execution skills. Reads `/context/skill-sessions.md`, detects cross-skill patterns (2+ domains = HIGH), proposes guardrails and brain updates, outputs to `/context/meta-patterns.md`. The beating heart of the system.
- **meta-learn** — Captures post-session learnings and routes them to knowledge base.
- **meta-review** — Audits any skill against SKILL-SPEC v2.0.0 (19-point checklist).
- **meta-verify** — Quality gate on T1 skill output before delivery.

### Commands (8):

- `/pmm-meta:synthesis` — Run meta-synthesis monthly. Detects patterns, proposes guardrails + brain updates, gates approval.
- `/pmm-meta:synthesis-status` — Show current meta-synthesis state (patterns, guardrails active/stale, updates proposed/approved).
- `/pmm-meta:learn` — Capture learnings from last execution skill session.
- `/pmm-meta:learn-history` — Show patterns captured in knowledge base (searchable).
- `/pmm-meta:learn-promote [pattern]` — Promote pattern from "watch" to "active guardrail."
- `/pmm-meta:review [skill]` — Audit skill against SKILL-SPEC (19-point checklist).
- `/pmm-meta:review-all` — Batch review all skills in pmm-meta folder.
- `/pmm-meta:verify [output]` — Quality check on T1 output before ship.

### Examples:

**Skills:**
- `Run meta-synthesis for June` → Detects patterns, proposes guardrails
- `Show synthesis status` → What patterns? Which guardrails active? Which proposals pending?
- `Capture learnings from today's retro`
- `Review experiment-doc skill against spec`
- `Quality check: is this positioning brief ready to ship?`

**Commands:**
- `/pmm-meta:synthesis` — End of June
- `/pmm-meta:synthesis-status` — Check state before approving guardrail proposals
- `/pmm-meta:verify [positioning brief]` — Before sharing with CEO

### How It Works:

**Monthly loop:**
1. Run execution skills throughout the month (30+ days of data)
2. End of month: `/pmm-meta:synthesis`
3. Meta-synthesis reads `/context/skill-sessions.md`, detects patterns
4. Proposes guardrails + brain updates with approval gates
5. You approve/reject
6. Next month: execution skills load updated guardrails at Step 0
7. System is smarter. Repeat.

**By month 3:** System compounds automatically. Every execution is informed by every prior execution.

### Files

See [pmm-meta/](pmm-meta/) for:
- `meta-synthesis/SKILL.md` — Full skill documentation (10 steps, 19/19 SKILL-SPEC)
- `meta-synthesis/meta-synthesis.eval.md` — 8 comprehensive test scenarios
- `README.md` — Complete meta layer documentation

</details>

<details>
<summary><strong>6. pmm-go-to-market</strong> — GTM strategy, workflow orchestration: full launch workflows, positioning refresh, competitive programs, quarterly cycles (2 skills, 2 commands)</summary>

Complete GTM workflows that chain multiple skills together. One prompt runs positioning → competitive → strategy → execution. Brain updates automatically after each workflow.

### Skills (2):

- **go-to-market-strategy** — Assigns launch tier (T1-T4), generates strategic briefs with messaging and channels, self-learns from past launches
- **workflow-orchestrator** — Chains 20+ hs- skills for complete GTM programs. Covers 10 workflows: full launch, positioning refresh, competitive program, quarterly PMM cycle, market entry, post-launch retro, competitive response, ICP foundation, voice foundation, and new hire onboarding

### Commands (2):

- `/pmm-go-to-market:launch-strategy` — Assign tier and generate GTM strategy for product/feature launch
- `/pmm-go-to-market:run-workflow` — Run complete multi-skill GTM workflow (launch, quarterly, competitive, etc.)

### Examples:

**Skills:**
- `We're launching SSO integration. What tier is this?`
- `Run full launch workflow for analytics dashboard`
- `Run Q3 PMM cycle — refresh all assets`
- `Competitive program for top 3 competitors`
- `We're entering the healthcare vertical — run market entry workflow`
- `Run retro for our last launch and update brain`

**Commands:**
- `/pmm-go-to-market:launch-strategy` — SSO integration launch
- `/pmm-go-to-market:run-workflow` — Full launch workflow for [product], DRI: me
- `/pmm-go-to-market:run-workflow` — Quarterly PMM cycle, goal: refresh all core assets

### Supported Workflows (10):

1. **Full Product Launch** — positioning → competitive → strategy → campaign → stakeholder → retro (6-12 weeks)
2. **Positioning Refresh** — positioning → value props → update battlecards (1-2 weeks)
3. **Competitive Intelligence Program** — alternatives → battlecards → CI briefing (2-4 weeks)
4. **Quarterly PMM Cycle** — retro → positioning audit → competitive refresh → OKRs (3-4 weeks)
5. **New Market Entry** — ICP → personas → positioning → competitive → strategy (8-12 weeks)
6. **Post-Launch Retro** — retro → update brain with actuals (1 week)
7. **Competitive Response** — fast battlecard → value props → sales assets (1-2 weeks)
8. **ICP + Personas Foundation** — ICP → personas → interviews (2-3 weeks)
9. **Voice & Tone Foundation** — voice guide → test with writing-assistant (1 week)
10. **Full PMM Onboarding** — audit brain → gap report (1-2 weeks, read-only)

## How Skills Compound Over Time

Each skill learns from all prior skills. Here's the flow:

### Week 1: First Skill Runs
- Skill reads `/foundation/brain.md` (shared context)
- Skill executes
- Meta-learn detects pattern, logs to `/sessions/quality-learnings.md`

### Week 2: Second Skill Runs
- Skill reads `/foundation/brain.md`
- Skill reads `/sessions/quality-learnings.md` (Week 1 learnings)
- Pre-flight displays: "Based on Week 1: [Pattern from first skill]"
- Skill's quality improves 2-3% automatically from loading prior learnings
- Skill executes, meta-learn detects new pattern

### Week 3+: Each New Skill
- Loads all prior learnings automatically
- Quality improves baseline from loaded patterns
- Adds new learnings
- System compounds exponentially

## Shared Files (Read-Only for Skills)

- `/foundation/brain.md` — ICP, positioning, alternatives, market context (from product-marketing-context)
- `/context/meta-patterns.yml` — Active guardrails (populated by meta-synthesis)
- `/sessions/quality-learnings.md` — Learnings log (populated by meta-learn)
- `/sessions/stack-learnings.md` — Pattern aggregation (populated by meta-synthesis)

## Adding New Skills

1. Create new skill folder
2. Add Step 0 to SKILL.md:
   - Read `/foundation/brain.md`
   - Load `/context/meta-patterns.yml` at pre-flight
   - Read `/sessions/quality-learnings.md` and display learnings to user
3. Skill automatically compounds with prior learnings
4. No other setup needed

---

## About

This marketplace will evolve in tandem with PMM practices and LLM capabilities.

Selected skills based on the work of:

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

Want to add a skill to the marketplace?
1. Fork this repo
2. Create your skill in `/skills/your-skill-name/`
3. Follow the [Skill Creation Guide](SKILL_GUIDE.md)
4. Submit a PR

**Skill requirements:**
- Must read from `/foundation/brain.md` if brain-powered
- Must include SKILL.md with YAML frontmatter
- Must include description and triggers
- Must pass quality evals

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

[MIT](./LICENSE) — Use these however you want.
