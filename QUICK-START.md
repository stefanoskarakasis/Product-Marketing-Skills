# Quick Start: 90 Seconds to First Value

Want to see what's possible *before* committing 15 minutes to brain setup? Do this first.

---

## 0:00 → 0:30 — Clone

```bash
# Option 1: Use this template
gh repo create my-pmm-skills --template stefanoskarakasis/Product-Marketing-Skills --private
cd my-pmm-skills

# Option 2: Clone directly
git clone https://github.com/stefanoskarakasis/Product-Marketing-Skills.git
cd Product-Marketing-Skills
```

---

## 0:30 → 2:00 — Run Your First Skill (No Setup Required)

Open Claude Code, Claude Cowork, Cursor, or Windsurf in this repo and run:

```
/positioning-messaging audit
```

Claude will ask you three quick questions (takes 60 seconds to answer):

1. **Who is your primary buyer?**  
   Example: "Marketing ops manager at mid-market B2B SaaS"

2. **How are you different?**  
   Example: "We integrate with your entire martech stack without rip-and-replace"

3. **Who's your toughest competitor?**  
   Example: "HubSpot"

That's it. No brain file. No 30-question setup. Just three specifics.

---

## 2:00 → 5:00 — Read the Output

Claude produces:

- **Positioning audit** — scores your messaging against April Dunford's framework
- **Before/after copy** — shows what sharper positioning looks like
- **Competitive context** — explains how you position differently
- **Messaging hierarchy** — 3-tier structure for sales, marketing, product
- **Next steps** — what to lock next (value props, battlecards, homepage)

You now have a working artifact. Bookmark it. Share it with your team.

---

## 5:00 → 90:00 — Ready to Unlock the Full System?

You've seen what one skill produces. Now unlock 17 others by populating your brain once.

### Option A: Fast Setup (15 minutes)

Your `/foundation/brain.md` is the shared context layer. Every other skill reads it first. Setup now:

```
/product-marketing-context setup
```

Claude walks you through:
- Product description (who you are, what you solve)
- ICP + anti-ICP (who wins with you, who doesn't)
- Competitive landscape (how you're different)
- Positioning (your anchor + differentiators)
- Revenue model + GTM motion (how you sell)
- Success metrics (how you measure wins)

Takes ~15 minutes. After this, every skill is context-aware.

### Option B: Populate Gradually

Don't want to commit 15 minutes upfront? No problem.

Each time you run a skill, it prompts:
> "Your brain isn't fully populated. These sections would make me sharper: [Section name]. Want to populate them now or skip?"

You can build incrementally. Recommend: populate ICP + Positioning first (those are the highest-leverage for all other skills).

---

## What You Can Do Now (All Skills Live)

Once brain is populated, you unlock 18 skills across 5 domains:

### 🧠 Foundation
- **product-marketing-context** — Build or audit your brain once, use it everywhere

### 🎯 Positioning & Messaging  
- **positioning-messaging** — Build positioning statements, messaging hierarchies, homepage copy (5 output modes)
- **gaccs-brief** — Campaign briefs (Goals, Audience, Creative, Channels, Stakeholders)
- **writing-assistant** — Rewrite copy to match your brand voice

### 📊 Execution (Day-to-Day)
- **experiment-doc** — Build, audit, score growth experiments with guardrail metrics
- **interview-summary** — Analyze customer interviews using JTBD theory
- **prd** — HubSpot-style PRDs with embedded Solution Stories
- **pre-mortem** — Cross-functional risk analysis before launches
- **retro** — Post-launch retrospectives with compounding learnings
- **pmm-okrs** — Quarterly OKR building for PMM teams
- **stakeholder-maps** — Political maps for launches (champions, blockers, deal-killers)
- **prioritization-frameworks** — Score initiatives using RICE, ICE, Kano, or 8 other frameworks

### 🚀 Go-to-Market
- **go-to-market-strategy** — Assign launch tier (T1–T4), generate GTM strategy briefs
- **beachhead-segment** — Score and select your first customer wedge before scaling
- **workflow-orchestrator** — Chain 10+ skills for full launch workflows (positioning → competitive → strategy → campaign → execution)

### 🛠️ Toolkit
- **competitive-battlecard** — Build sales battlecards (positioning, objection handling, pricing intel)
- **pmm-resume** — Tailor your PMM resume for specific roles
- **privacy-policy** — Generate GDPR/CCPA-compliant privacy policies

---

## Suggested Order (First 2 Weeks)

If this is your first time using the system:

**Week 1:**
1. Run `/positioning-messaging audit` on your current positioning (right now, no setup)
2. Populate brain (`/product-marketing-context setup`) — 15 minutes
3. Run `/experiment-doc` on a current idea or hypothesis you want to test
4. Run `/pre-mortem` on your next big launch or initiative

**Week 2:**
1. Run `/interview-summary` on a customer call transcript (if you have one)
2. Run `/go-to-market-strategy` on your next launch
3. Run `/workflow-orchestrator` for a full multi-skill GTM cycle (positioning → competitive → strategy → execution)
4. Populate `/foundation/brain.md` Section 7 (Meta-Learnings) — notes on what you learned this week

By end of week 2, you'll understand how skills chain together and how your brain compounds.

---

## Troubleshooting

**"I ran a skill and it asked for my brain context, but I skipped setup."**  
You can answer "I'll do this later" and the skill will work with assumptions. Or populate that section now (`/product-marketing-context setup`).

**"I want to run a specific skill but I'm not sure which one."**  
See the "What You Can Do Now" section above. Each skill has a one-liner. Or search by task:
- "I want to test an idea" → `/experiment-doc`
- "I want sharper positioning" → `/positioning-messaging`
- "I want to identify launch risks" → `/pre-mortem`
- "I want to pick my first customer segment" → `/beachhead-segment`
- "I want to run a full launch end-to-end" → `/workflow-orchestrator`

**"I populated my brain but a skill still feels generic."**  
Run `/product-marketing-context audit` to check your brain health. Some sections might be Placeholder or missing depth. Update those sections and re-run the skill.

**"Can I use this with Claude Code CLI, Cursor, Claude Cowork, etc.?"**  
Yes. These skills work with any IDE/agent that supports the Agent Skills spec. Install via `npx skills add`, GitHub template, or git submodule — they work everywhere.

---

## What Happens Next

Once you've run 3-4 skills, you'll feel the compounding:

- Skill #1 (positioning audit) is generic — shows you *possibilities*
- Skill #2 (GTM strategy) reads your positioning → more specific
- Skill #3 (experiment design) reads positioning + GTM strategy → much sharper
- Skill #4 (pre-mortem) reads all above + brain learnings → specific to your launch

That's the system working. Each skill is smarter because it inherited context from prior runs.

---

## Ready to Go Deeper?

- See all 18 skills + how they chain together → [Main README](./README.md)
- Contribute a new skill → [Contributing Guide](./CONTRIBUTING.md)
- Report a bug or request a feature → [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues)

**Questions?** [Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) or reach out to [Stefanos](https://heystefanos.gumroad.com/).

---

## One More Thing

If this system helps you ship sharper positioning, land better customers, or run tighter launches, star the repo. It means a lot and tells us people are finding value in this.

⭐ [Star on GitHub](https://github.com/stefanoskarakasis/Product-Marketing-Skills)
