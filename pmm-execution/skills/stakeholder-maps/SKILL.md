---
name: stakeholder-maps
version: 2.3.0
description: >
  Builds political maps (not org charts) showing who can kill your launch, who champions it, and what to say to each stakeholder. Reads brain context (ICP, positioning, GTM motion) and guardrails from prior stakeholder mapping sessions; produces Power × Interest grid with political role assignment, conflict map, and weekly Sprint Cards for execution. Logs session data to /context/skill-sessions.md for meta-synthesis pattern detection and compounds learnings over time.
---

# Stakeholder-Maps — Skill

## How This Works

Stakeholder maps built in a vacuum are a waste of time. This skill builds a map anchored to political reality: who has power, who's a hidden champion, who's a silent blocker, and what to do before you're in the room.

The skill runs in 7 steps:

**Step 0** — Load brain context (ICP, positioning, GTM motion) and guardrails from `/context/meta-patterns.md` (e.g., "product launches without Sales Manage Closely engagement fail 80% of the time").

**Step 1** — Intake: Initiative description, success definition, timeline, and current champions/blockers.

**Step 2** — Inversion: Who could sink this from inside? (If you can't name them, the map is assumed, not validated.)

**Step 3** — Classification: Place each stakeholder on Power × Interest grid; assign political role (Champion, Blocker, Frozen, Gatekeeper, Performer, Floating Voter).

**Step 4** — Conflict mapping: Identify stakeholder conflicts; define second-order risks and resolution owners.

**Step 5** — Silent blocker scan: Which functions/roles aren't in the room but should be?

**Step 6** — Output: HTML widget (grid + comms plan + conflict map + confidence assessment) + markdown diagnostic + Sprint Cards.

**Step 7** — Log session to `/context/skill-sessions.md` with quality score, stakeholder counts, Watch For patterns, confidence assessment, guardrails triggered, and brain updates proposed.

---

## Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 5): ICP, positioning, GTM motion — these shape which stakeholders matter and what power they hold
- **Guardrails** from `/context/meta-patterns.md`: If a pattern fired 2+ times in prior stakeholder mapping sessions (e.g., "Sales performers without written commitment silently resist," "Finance gatekeepers kill launches when not Manage Closely"), surface it now

**Surface guardrails like this:**

```
🔁 PATTERN FROM PRIOR STAKEHOLDER MAPS

I've seen [pattern description] in 2 prior sessions.
Examples: [specific initiatives or stakeholder failure modes]

Quick check: Does this apply to your initiative?
- If YES → We'll build it into the Watch For signals
- If NO → Let's flag it if it emerges during mapping
```

You can skip a guardrail if you disagree, but you'll see it first.

---

## Step 1 — Intake (Conversational, One Round)

Ask 6 questions in one conversational block:

1. **What's the initiative?** — One sentence. Launch, campaign, pricing change, new channel, GTM pivot, or internal programme.
2. **What does success look like in 60–90 days?** — Specific. A number, behaviour, deal closed, or capability shipped.
3. **Who has explicitly said yes to this?** — Name champions by role. Who's already committed?
4. **Who has said nothing, or who might push back?** — Name people or functions you're unsure about.
5. **What's the highest-stakes decision that needs to get made?** — Who makes it or can veto it?
6. **What's your timeline?** — When does the first irreversible action happen? (Announcement, budget commit, sales enablement kickoff, etc.)

If they share a brief or plan, read it fully. Extract stakeholder names, decision gates, power signals. Reflect back in 3 sentences before proceeding. Assumption-surfacing, not polish.

---

## Step 2 — Inversion: Who Could Sink This?

After intake, ask:

> "One more: **if this failed because of an internal stakeholder — who would it most likely be, and why?**
> Not execution gaps. The person or team whose resistance, inaction, or misalignment would be the root cause."

If they can't answer clearly, flag it: "If you can't name who could sink this, the political map is assumed — not validated. We'll surface this risk in the mapping step."

---

## Step 3 — Classification: Power × Interest Grid + Political Roles

Place each stakeholder on a 2×2 grid:

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | 🔴 **Manage Closely** — Make-or-kill power. Meet early, involve in decisions. | 🟡 **Keep Satisfied** — Can block silently. Periodic high-signal updates only. |
| **Low Power** | 🟢 **Keep Informed** — Amplify or dampen momentum. Regular updates, invite to demos. | ⚪ **Monitor** — Light-touch. Available on request. |

For each stakeholder, assign a **political role** (beyond quadrant placement):

- 🏆 **Champion** — Proactively advocates. Arm with proof points; give early wins to share.
- 🛑 **Blocker** — Actively opposes or competes for resources. Diagnose: values conflict, territorial, or information gap?
- 🧊 **Frozen** — Neither supporting nor opposing; silent. Silence is not alignment. Investigate and re-engage.
- 🔍 **Gatekeeper** — Controls access to decision-maker or budget, but isn't the decision-maker. Never bypass.
- 🎭 **Performer** — Says yes in rooms, acts differently outside. Validate with written artefacts, not verbal agreement.
- 🌊 **Floating Voter** — Undecided. Moveable by evidence, relationships, or early momentum. Bring them a win from a Champion.

---

## Step 4 — Conflict Mapping

Identify stakeholder conflicts. For each conflict:

1. **Stakeholder A vs Stakeholder B** — Name both
2. **Conflict description** — 2 sentences
3. **Second-order risk** — What happens if unresolved by the decision gate? (Not just what they do, but what breaks downstream)
4. **Resolution owner + deadline** — Specific structural move the PMM owns

Unresolved conflicts compound. Assign resolution explicitly.

---

## Step 5 — Silent Blocker Scan

Ask: Which functions/roles aren't in the room but could kill this?

- Finance (if pricing or budget implications)
- Legal (if compliance or contract implications)
- Security/InfoSec (if data or access implications)
- CS/Support (if customer-facing or operational implications)
- Sales (if revenue-dependent)
- Product (if feature-dependent)
- Engineering (if technical or timeline-dependent)

For each silent function: what do they control? When to brief them? Who owns outreach?

---

## Step 6 — Output Structure

Deliver three artifacts:

**Artifact 1: HTML Widget** (render before markdown)
- Power × Interest grid with stakeholder chips (colour-coded by political role)
- Communication Plan table (Manage Closely + Keep Satisfied only)
- Conflict Map cards (each with second-order risk block + resolution block)
- PMM Confidence Assessment (six metric cards: Champion coverage, Blocker diagnosis, Frozen visibility, Silent function coverage, Comms plan completeness, Overall)

**Artifact 2: Markdown Diagnostic**
```
Initiative: [name]
PMM Owner: [name]
Date: [YYYY-MM-DD]
Primary Decision Gate: [first irreversible action + date]
Confidence Score: 🟢 / 🟡 / 🔴

For each Manage Closely + Keep Satisfied stakeholder:

[Name / Role] · [Political Role emoji + label]
Why they matter: [their power over this initiative — 1–2 sentences]
What they care about: [their actual priority, not job title]
Risk if neglected: [second-order consequence]
Key message: [exact framing they need — not generic positioning]

Silent blockers — functions not in the room:
[Function] — [what they control] — [when to brief] — [owner]
```

**Artifact 3: Sprint Cards** (one file, one card per Manage Closely + Keep Satisfied stakeholder)
```
Week of: [Monday date]
PMM: [name]
Decision gate: [date + what]
Cards this week: [n]
Last updated: [YYYY-MM-DD]

[Political Role emoji] [Name] — [Role]
📅 Next touchpoint: [date · format]
  _(Execution note: what cannot be allowed to slip)_
📝 Send before touchpoint: [Specific artefact — not "an update"]
  _[Prep time. Send by deadline.]_
🎯 What you need from them, by when: [Explicit ask. Deadline. What to do if no response.]
🗣️ The one sentence that has to land: "[Exact line in their frame]"
  _(If they push back: "[Response that holds frame]")_
🚨 Watch for: [Specific behavioural signal that means they've shifted]
  → [Immediate action if signal fires]
```

---

## Step 7 — Post-Session Logging

Log to `/context/skill-sessions.md` with YAML metadata:

```yaml
skill: stakeholder-maps
session_date: [YYYY-MM-DD]
initiative_name: [Name]
initiative_type: [product launch / pricing change / new channel / GTM pivot / new market entry / campaign / internal programme]
quality_score: [0-100]
stakeholder_count: [total]
manage_closely_count: [count]
champion_count: [count]
blocker_count: [count]
frozen_count: [count]
conflicts_identified: [count]
silent_functions_flagged: [count]
guardrails_triggered: [list if any]
brain_context_loaded: true
brain_sections_referenced: [list]
brain_updates_proposed: [list if any]
watch_for_patterns_extracted: [count]
confidence_score: [🟢 / 🟡 / 🔴]
inversion_check_run: [true/false]
decision_gate: [date + description]
output_path: "[Where files were saved]"
```

---

## Operating Rules (Condensed)

- **Silence is not alignment.** Frozen until proven otherwise.
- **Name the Performers.** Verbal yes without written commitment = it didn't happen.
- **Second-order before action.** Ask "and then what?" once before every comms decision.
- **The map is a working tool.** Update after every major alignment conversation.
- **Gatekeepers aren't blockers.** Bypassing them converts them.
- **Sprint Cards are weekly.** If not updated in 10 days, it's wrong.
- **Watch For signals are hypotheses.** Confirm, log, and promote to rules at 3 confirmations.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Inversion check run | Named who could sink this |
| Political roles assigned | Every stakeholder has a role beyond quadrant |
| HTML widget rendered | Grid + comms table + conflict map + confidence cards |
| Comms plan table | Every Manage Closely + Keep Satisfied has key message + next action |
| Conflict map | Every conflict has second-order risk + resolution block |
| Markdown diagnostic | Rendered with role analysis for Manage Closely stakeholders |
| Sprint Cards | Five fields per stakeholder, no exceptions |
| Watch For signals | Every Manage Closely card has behavioral signal + immediate action |
| Brain context | Map cross-referenced with ICP, GTM motion, positioning |

---

## Self-Improvement Loop

Each session logs stakeholder counts, Watch For patterns, conflicts, and confidence to `/context/skill-sessions.md`.

Monthly, meta-synthesis detects patterns:
- "Product launches without Sales Manage Closely engagement fail 80%" → Guardrail surfaces next time
- "Frozen Finance become Blockers within 2 weeks of budget pressure" → Add to Watch For rules
- "Champion coverage >80% = 90% launch success" → Recommend higher champion threshold

Patterns feed back into guardrails (Step 0) and brain updates (Section 3, 5, 7).

---

## Initiative Type Modifiers

| Initiative Type | Dominant Quadrant Risk | Watch especially for |
|---|---|---|
| **Product Launch** | Manage Closely → Sales, Product | Sales Performers (verbal yes, no enablement) |
| **Pricing Change** | Keep Satisfied → Finance, Legal, CS | Finance silent blocker; CS frozen with blast radius |
| **New Channel** | Keep Informed → Demand Gen, RevOps | Channel conflicts; RevOps as gatekeeper |
| **GTM Pivot** | Manage Closely → CEO, Sales VP, RevOps | VP Performers; ICs frozen on old motion |
| **New Market Entry** | Manage Closely → Regional leads, Legal | Local Gatekeepers; home market frozen voters |
| **Campaign Launch** | Keep Informed → Content, Design, Sales | Legal/Brand silent blockers; Sales Floating Voters |
| **Internal Programme** | Manage Closely → HR, Finance, Ops | Function heads seeing overhead (Blockers) |

---

## Do Not Use For

- **Buyer personas** → use hs-buyer-personas
- **Competitive intelligence** → use hs-ci-stakeholder-briefing
- **Campaign messaging** → use hs-gaccs-brief (after stakeholder map)
- **Risk analysis** → use hs-pre-mortem (before stakeholder map)
- **GTM channel design** → use go-to-market-strategy
