# Product Marketing Skills for AI Agents: The AI Operating System for Better Go-To-Market Decisions in Competitive Markets

Build your Product Marketing Brain in 2 hours. Then every GTM decision gets 10x faster because Claude remembers your context, positioning, and past launches.

From building your product marketing context (brain) to product messaging, planning product launches, devising growth experiments, and gathering actionable competitive intelligence.

<img width="1440" height="712" alt="marketplace" src="https://github.com/user-attachments/assets/03980d16-0227-4e5d-96db-dd2129aa8e9a" />

Designed for Claude Code and Cowork. Skills compatible with other AI assistants. 

## Start Here

New to product marketing context? → `/setup-context`
Pressure-testing positioning? → `/position`
Planning a launch? → `/launch`
Building a battlecard? → `/compete`
Drafting a campaign brief? → `/brief`

If this project helps you, ⭐ the repo.

## Why Product Marketing Skills?

**The problem:** Every time you ask Claude for positioning, battlecards, or briefs, you re-explain your company. By session #5, you're copy-pasting from previous chats.

**The solution:** Build your brain once (`product-marketing-context`). Every other skill reads it. Zero repetition.

The result: better positioning, sharper launches, and stronger competitive intelligence — anchored to your specific company context, not generic templates.

**Results**
- ✅ 10x faster (no re-explaining context)
- ✅ Consistent messaging (all skills read the same source)
- ✅ Compound intelligence (skills reference each other's outputs)

## How It Works (Skills, Commands, Plugins)

**Skills** are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PMM task. Some skills also work as reusable foundations that multiple commands share. Installing the marketplace gives you all PMM domains at once.

Skills are loaded automatically when relevant to the conversation — no explicit invocation needed. If needed (e.g., prioritizing skills over general knowledge), you can **force loading skills** with `/plugin-name:skill-name` or `/skill-name` (Claude will add the prefix).

**Commands** are user-triggered workflows invoked with `/command-name`. They chain one or more skills into an end-to-end process. For example, `/launch` chains product-marketing-context → positioning-messaging → gtm-launch-planner together.

**Plugins** group related skills and commands into installable packages. Each plugin covers a GTM domain — building your context, product marketing strategy, execution, and so on.

## How Skills Work Together

Skills reference each other and build on shared context. The `product-marketing-context` skill is the foundation — every other skill checks it first to understand your product, ICP, personas, positioning, and competitive landscape before doing anything.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        COMPOUND INTELLIGENCE                                  │
│  Brain stores context once → All skills read it → Outputs save to Section 7  │
│                     Zero repetition, consistent messaging                     │
└──────────────────────────────────────────────────────────────────────────────┘
                                      ↓
┌───────────────────────┬──────────────────────────┬─────────────────────────┐
│  Phase 1:             │  Phase 2:                │  Phase 3:               │
│  FOUNDATION           │  EXECUTE                 │  SUPPORT                │
├───────────────────────┼──────────────────────────┼─────────────────────────┤
│                       │                          │                         │
│ ┌───────────────────┐ │ ┌──────────────────────┐ │ ┌─────────────────────┐│
│ │ Product Marketing │ │ │  PMM-Execution       │ │ │  PMM-Toolkit        ││
│ │ Context           │→│ │                      │ │ │                     ││
│ │                   │ │ │  Day-to-day PMM work │ │ │  Utilities & Tools  ││
│ │ • Brain Setup     │ │ │                      │ │ │                     ││
│ │   (31 questions)  │ │ │  • PRDs              │ │ │  • Writing Asst     ││
│ │ • Brain Audit     │ │ │  • OKRs              │ │ │  • Resume Review    ││
│ │   (0-100 score)   │ │ │  • Stakeholder Maps  │ │ │  • Privacy Policy   ││
│ │ • Creates brain   │ │ │  • Pre-mortems       │ │ │  • GACCS Brief      ││
│ │   file            │ │ │  • Retros            │ │ │                     ││
│ │                   │ │ │  • Experiment Docs   │ │ │  Read brain         ││
│ │ Saves to:         │ │ │  • Prioritization    │ │ │  (optional)         ││
│ │ /foundation/      │ │ │  • Meeting Notes     │ │ │                     ││
│ │ brain.md          │ │ │                      │ │ │                     ││
│ │                   │ │ │  All read brain +    │ │ │                     ││
│ │                   │ │ │  save to Section 7   │ │ │                     ││
│ └───────────────────┘ │ └──────────────────────┘ │ └─────────────────────┘│
│                       │                          │                         │
│ Skill (1):            │ Skills (8):              │ Skills (4):             │
│ ✅ product-marketing- │ ✅ product-requirement-  │ ✅ writing-assistant    │
│    context            │    doc                   │ ✅ pmm-resume           │
│                       │ ✅ stakeholder-maps      │ ✅ privacy-policy       │
│                       │ ✅ pre-mortem            │ ✅ gaccs-brief          │
│                       │ ✅ retro                 │                         │
│                       │ ✅ brainstorm-okrs       │                         │
│                       │ ✅ experiment-doc-       │                         │
│                       │    builder               │                         │
│                       │ ✅ prioritization-       │                         │
│                       │    frameworks            │                         │
│                       │ ✅ meeting-summaries     │                         │
│                       │    (if separate)         │                         │
└───────────────────────┴──────────────────────────┴─────────────────────────┘
                                      ↑
              All outputs stored in /foundation/brain.md Section 7
                  Skills reference each other's work automatically

```

Commands use skills. Some skills serve multiple commands. Some skills (like `prioritization-frameworks` or `proof-points-claims`) are standalone references that Claude draws on whenever relevant — no command needed.

Commands are designed to flow into each other, matching the PMM workflow. After any command completes, it suggests relevant next commands — just follow the prompts.

## Quick Start

**Best option:** Claude Cowork
1. Click **Customize** (bottom-left)
2. Go to **Browse plugins** → **Personal** → **+**
3. Select **Add marketplace from GitHub**
4. Enter: `stefanoskarakasis/Product-Marketing-Skills`
5. Click **Install**

Done. All skills + commands ready.

---

## Installation Quick Reference

| Platform | Method | Status |
|----------|--------|--------|
| **Claude Cowork** | Settings → Browse plugins → Add from GitHub | ✅ Full support |
| **Claude Code (CLI)** | `claude plugin marketplace add ...` | ✅ Full support |
| **Claude.ai (Web)** | Manual skill upload only | ⚠️ Brain only |
| **Cursor / Windsurf** | Copy skill folders | ✅ Skills only |

---

## Installation

### Option 1: Claude Cowork (Recommended)

Install all skills and commands in one click.

```bash
# In Claude Cowork:
# Customize → Browse plugins → Personal → Add marketplace from GitHub
# Enter: stefanoskarakasis/Product-Marketing-Skills
```

All 15+ skills, commands, and brain integration install automatically.

---

### Option 2: Claude Code (CLI)

```bash
claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
```

---

### Option 3: Claude.ai (Web — Brain Only)

⚠️ Web interface only supports manual skill uploads. Use Cowork or Code for full functionality.

1. Download: [product-marketing-context.zip](#)
2. Go to Settings → Skills → Upload
3. Select the .zip file

---

### Option 4: Clone & Copy (Advanced)

```bash
git clone https://github.com/stefanoskarakasis/Product-Marketing-Skills.git
cp -r Product-Marketing-Skills/pmm-*/* ~/.cursor/skills/  # For Cursor
```

---

## What You Get

| | Cowork | Code | Web | Copy |
|---|--------|------|-----|------|
| Skills | ✅ | ✅ | ⚠️ | ✅ |
| Commands | ✅ | ✅ | ❌ | ❌ |
| Brain | ✅ | ✅ | ⚠️ | ✅ |
| Auto-update | ✅ | ✅ | ❌ | Manual |

---

## Usage

Once installed, just ask your agent to help with PMM tasks:

```
"Help me plan a product launch for SSO integration"
→ Uses go-to-market-strategy skill

"Generate positioning for our platform"
→ Uses hs-positioning-messaging skill

"Build a competitive battlecard for Okta"
→ Uses hs-competitive-battlecard skill

"Run Q3 quarterly PMM cycle"
→ Uses workflow-orchestrator skill

"Create a GACCS campaign brief"
→ Uses hs-gaccs-brief skill
```

You can also invoke skills directly with commands:
```
"Run full launch workflow for [product]"
/workflow-orchestrator

"What tier is this feature?"
/go-to-market-strategy

"Build positioning for B2B SaaS"
/hs-positioning-messaging 

"Run retrospective for last launch"
/hs-retro 

"Generate Q4 OKRs"
/hs-brainstorm-okrs 
```
Skills read your brain automatically — zero context re-explaining.

---

## Skill Categories

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

</details>

<details>
<summary><strong>5. pmm-go-to-market</strong> — GTM strategy, workflow orchestration: full launch workflows, positioning refresh, competitive programs, quarterly cycles (2 skills, 2 commands)</summary>

**NEW:** Complete GTM workflows that chain multiple skills together. One prompt runs positioning → competitive → strategy → execution. Brain updates automatically after each workflow.

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

### What Makes This Different:

**Self-learning:** Reads brain Section 7 (launch history) and adjusts recommendations based on YOUR past performance, not generic best practices.

**Brain-integrated:** Pulls positioning (Section 3), ICP (Section 2), competitive intel (Section 4), proof points (Section 5) — or flags gaps.

**Multi-skill orchestration:** One prompt chains positioning → competitive → strategy → campaign → stakeholder → execution. No manual routing.

**Writes back to brain:** Updates Sections 3, 4, 5, 7 automatically after each workflow. Fifth launch is smarter than first.

**Master program documents:** Produces complete program docs with artifacts, coherence reports, open questions, and next steps.

</details>

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
