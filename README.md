# Product Marketing Skills Marketplace: The AI Operating System for Better Go-To-Market Decisions

Build your Product Marketing context once. Every skill gets smarter from it forever.

Built for Claude Code, Cowork, and any agent that supports the [Agent Skills spec](https://agentskills.io). From building your product marketing context (brain) to product messaging, launches, experimentation, and competitive intelligence.

Skills compatible with other AI assistants. Built by [Stefanos Karakasis](https://heystefanos.gumroad.com/).

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

Each skill encodes a proven PMM framework — April Dunford positioning, Fletch PMM canvas, JTBD theory, GACCS briefs, and Gary Klein's pre-mortems — and walks you through it step by step. You get the rigour of established methodologies built into your daily workflow, not sitting on a bookshelf.

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

1. **Download the brain:** [product-marketing-context.zip]
2. **Upload to Claude.ai:** Settings → Skills → Upload
3. **Run setup:** Say "Set up my PMM brain" (takes 15-20 min)
4. **Check health:** Say "Check my brain health"
5. **[Coming Soon] Use execution skills:** "Generate positioning", "Build battlecard"

That's it. You're done.

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
[Download product-marketing-context.zip](https://github.com/yourusername/pmm-skills/releases/download/v2.1.0/product-marketing-context.zip)
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

<details>
<summary><strong>1. product-marketing-context</strong> — The Brain (1 skill, 5 commands)</summary>

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
<summary><strong>2. pmm-positioning</strong> — Positioning & Messaging (1 skill, 5 commands)</summary>

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
<summary><strong>3. pmm-toolkit</strong> — PMM Utilities (4 skills, 4 commands)</summary>

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
