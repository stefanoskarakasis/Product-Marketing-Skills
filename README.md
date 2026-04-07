# Product Marketing Skills Marketplace
PMM Skills Marketplace: 10+ agentic skills, commands, and plugins — from context setup to strategy, execution, go-to-market, launch, and growth. A collection of AI agent skills focused on product marketing tasks. Built for go-to-market operators and Product Marketers founders who want AI assistance to help with go-to-market strategy, PRD's, growth experiments, competitive intelligence, and customer research. 

[insert visual]

Designed for Claude Code and Cowork. Skills compatible with other AI assistants. Built by Stefanos Karakasis.

**Contributions welcome!** Found a way to improve a skill or have a new one to add? Open a PR.

<h2>What are Skills?</h2>
Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.

These skills live in .claude/skills as packaged .skill files and share a common context file at .agents/product-marketing-context.md**.

<h2>Start Here</h2>

New idea? → <code>/discover</code><br>
Need strategic clarity? → <code>/strategy</code><br>
Writing a PRD? → <code>/write-prd</code><br>
Planning a launch? → <code>/plan-launch</code><br>
Defining metrics? → <code>/north-star</code><br>
<br>
If this project helps you, ⭐ the repo.

<h2>Why PM Skills Marketplace?</h2>
Generic AI gives you text. Product Marketing Skills Marketplace gives you structure.

Each skill encodes a proven Marketing framework — ICP, positioning, messaging, prioritization, strategy — and walks you through it step by step. You get the rigor of Fletch, April Dunford, and Reforge built into your daily workflow, not sitting on a bookshelf.

The result: better insights, not just faster documents.

<h2>How It Works (Skills, Commands, Plugins)</h2>
*Skills* are the building blocks of the marketplace. Each skill gives Claude domain knowledge, analytical frameworks, or a guided workflow for a specific PM task. Some skills also work as reusable foundations that multiple commands share.

Skills are loaded automatically when relevant to the conversation — no explicit invocation needed. If needed (e.g., prioritizing skills over general knowledge), **you can force loading skills** with ``/plugin-name:skill-name`` or ``/skill-name`` (Claude will add the prefix).

**Commands** are user-triggered workflows invoked with ``/command-name``. They chain one or more skills into an end-to-end process. For example, '/discover' chains four skills together: brainstorm-ideas → identify-assumptions → prioritize-assumptions → brainstorm-experiments.

<h2>How Skills Work Together</h2>
Skills reference each other and build on shared context. The <code>/product-marketing-context</code><br> skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

<h2>Installation</h2>

<h3>Claude Cowork (recommended for non-developers)</h3>
1. Open *Customize* (bottom-left)<br>
2. Go to *Browse plugins → Personal → +*<br>
3. Select *Add marketplace from GitHub*<br>
4. Enter: <code>/stefanoskarakasis/product-marketing-skills</code><br>

<br>All x plugins install automatically.<br>

[insert visual]<br>

***

<h2>Skill Categories</h2><br>

<details>
  <summary><strong>1. pmm-execution</strong> — PRDs, OKRs, roadmaps, sprints, retros, release notes, stakeholder management (xx skills, xx commands)</summary><br>

Day-to-day product marketing: PRDs, OKRs, roadmaps, sprints, retrospectives, release notes, pre-mortems, stakeholder management, user stories, and prioritization frameworks.

**Skills (xx):**
* <code>create-prd</code> — Comprehensive 8-section PRD template<br>
* <code>brainstorm-okrs</code> — Team-level OKRs aligned with company objectives<br>
* <code>outcome-roadmap</code> — Transform a feature list into an outcome-focused roadmap<br>

**Commands (xx):**
* <code>/write-prd</code> — Create a PRD from a feature idea or problem statement
* <code>/plan-okrs</code> — Brainstorm team-level OKRs
* <code>/transform-roadmap</code>  — Convert a feature-based roadmap into outcome-focused

**Examples:**

Skills:

* <code>Which prioritization framework should I use for a 50-item backlog?</code> 
* <code>Map our stakeholders for the platform migration project</code> 
* <code>What's the difference between Opportunity Score, ICE, and RICE?</code> 

Commands:

* <code>/write-prd Smart notification system that reduces alert fatigue</code> 
* <code>/sprint retro — Here are the notes from our last sprint</code> 
* <code>/write-stories job — Break down the "team dashboard" feature into job stories</code><br>

</details>

<h2>About</h2>
This marketplace evolves with practice and AI capabilities.

Selected skills based on the work of:

* Anthony W. Ulwick — Jobs to Be Done
* Maja Voje — [Go-To-Market Strategist](https://gtmstrategist.com)
* Paweł Huryn — The Product Compass Newsletter
* Corey Haines — [Marketing Skills](https://www.corey.co)

Curated by Stefanos Karakasis.

<h2>Contributing</h2>
Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!<br>

<br>See CONTRIBUTING.md for guidelines on adding or improving skills.

