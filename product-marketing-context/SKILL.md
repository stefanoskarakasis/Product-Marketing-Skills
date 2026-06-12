---
name: product-marketing-context
version: 2.3.0
description: >
  The PMM brain — builds and maintains the GTM foundation every other skill reads.
  ICP, positioning, alternatives, voice, market context, proof points — captured
  once, used everywhere. After setup, surfaces the right skills for your role and
  focus. Trigger on: "build my brain", "set up my GTM foundation", "audit my brain",
  "check brain health", "update my ICP", "configure context", "brain wizard",
  "initialize foundation", or any request to create or refresh the shared context
  that powers the full PMM skill ecosystem.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-12
---

# Product Marketing Context

The brain every other PMM skill reads before doing anything. Build it once. Every
subsequent skill — positioning, competitive, GTM strategy, stakeholder maps — pulls
from it automatically. Zero re-entry.

Not a form. A 15-minute conversation that makes every future PMM output sharper.

---

## Trigger

- **When:**
  - Building GTM context from scratch (new company, new product, new role)
  - Auditing whether your current brain still matches what you're telling customers
  - Refreshing buyer intelligence after a market shift or repositioning event
  - Any PMM skill is about to run and there's no brain file yet
  - Checking brain health and getting improvement recommendations
- **Not for:** One-time positioning work → `hs-positioning-messaging`. Competitive
  analysis → `hs-competitive-battlecard`. Individual audience research →
  `hs-buyer-personas`. OKR planning → `hs-brainstorm-okrs`. Each of those skills
  reads your brain — this skill builds it.
- **Example prompts:**
  - "Build my brain"
  - "Set up my GTM foundation"
  - "Audit my brain"
  - "Check my brain health"
  - "Update my ICP"
  - "What's my current brain?"
  - "Configure my PMM context"

---

## Inputs

- **Args:** None required. Skill auto-detects whether a brain exists or needs building.
  Optional: `--edit-section [1-6]` to update one section without re-running the full wizard.
- **Defaults:**
  - No brain found → first-run onboarding (see Pre-flight) → fresh wizard
  - Brain exists → offer: [View current] [Edit sections] [Rebuild from scratch]
  - v1.x legacy files found in `.agents/` or `.claude/` → offer migration with
    field-by-field confirmation before writing
- **Context keys:**
  - `/foundation/brain.md` — read if exists
  - `.agents/product-marketing-context.md` — check for legacy v1.x
  - `.agents/icp.md` — check for legacy v1.x
  - `.agents/alternatives-map.md` — check for legacy v1.x
  - `.agents/voice-tone.md` — check for legacy v1.x
  - `.agents/market-context.md` — check for legacy v1.x
  - `.agents/proof-points.md` — check for legacy v1.x

---

## Pre-flight

### First-run detection (Ramp Glass pattern)

Before anything else: check for `/foundation/brain.md`.

**If brain is missing AND this is first contact with the skill**, run the first-run hook.
Do not go straight to wizard questions. Show value before asking for effort:

> "Before we start: what you're about to build is the file every PMM skill in this
> ecosystem reads automatically. ICP, positioning, alternatives, voice, proof points —
> captured once here, never re-entered. Skills like `hs-positioning-messaging`,
> `hs-competitive-battlecard`, and `go-to-market-strategy` will pull from it without
> you typing a word.
>
> It takes 15 minutes. You do it once. Ready to start?"
> [Yes, let's build it] [Not now — remind me later] [I have old files to migrate]

**If brain exists**: skip first-run hook. Load silently, offer [View / Edit / Rebuild].

**If legacy v1.x files found** (in `.agents/` or `.claude/`): offer migration:
> "Found older foundation files from v1.x. Want to migrate them automatically?
> I'll show you each extracted value before writing anything."
> [Yes, migrate] [No, start fresh]

### Standard checks
- `/foundation/` directory — create if missing
- Any section marked 🔴 Placeholder → flag before running dependent skills:
  > "Section [X] is incomplete. Skills that depend on it will produce weaker output."

---

## Steps

### Step 1: Detect Brain State

Check what exists and branch accordingly:

- `/foundation/brain.md` present → offer [View / Edit section / Rebuild]
- Legacy v1.x files in `.agents/` → offer migration
- Neither → first-run hook (Pre-flight) → fresh wizard

If editing: ask which section (1–6) or "all". Jump directly to that section's
questions without re-running the others.

---

### Step 2: Product Context (5 Questions)

**Why this section:** Every skill needs to know what you're selling and to whom.
Without it, positioning output is generic. This anchors everything.

**Q1:** What's your product called?
**Q2:** In 2–3 sentences, what does it do? Focus on the problem it solves, not features.
**Q3:** What stage is it at? (Pre-launch / Launch / Growth / Scale)
**Q4:** Who's your primary target market? Be specific — company size, industry, role.
**Q5:** Complete: "[Product] helps [target market] to _____ so they can _____"

Store as: `product_name`, `product_description`, `product_stage`, `target_market`,
`value_proposition`

**Confirm Section 1:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 3: ICP Definition (8 Questions)

**Why this section:** Vague ICP = vague messaging. Every persona, battlecard, and
launch brief traces back to this. Specificity here multiplies across every output.

**Q1:** What company size (employees or ARR) is your ideal customer?
**Q2:** Any specific industries or verticals? Or horizontal across all industries?
**Q3:** Primary geographic market(s)?
**Q4:** Who's the primary buyer? (Title + role description)
**Q5:** Who actually signs the contract? (Economic buyer, if different)
**Q6:** Who becomes your internal champion? What do they care about?
**Q7:** What are the top 3 pain points your ICP has that your product solves?
**Q8:** What event triggers them to start looking for a solution like yours?

Store as: `icp_company_size`, `icp_industry`, `icp_geography`, `icp_primary_persona`,
`icp_economic_buyer`, `icp_champion`, `icp_pain_points[]`, `icp_buying_triggers`

**Confirm Section 2:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 4: Alternatives & Positioning (6 Questions)

**Why this section:** April Dunford's framework. You're not positioning against
"competitors" — you're positioning against what buyers are actually comparing you to,
including doing nothing. This is the hardest section to get right and the one that
makes the biggest difference.

**Q1:** What are the top 3 products buyers compare you to? (Not "our competitors" —
what do BUYERS actually consider before choosing?)
**Q2:** What do buyers do TODAY if they don't buy any tool, including yours?
**Q3:** Why do buyers leave those alternatives and consider you instead?
**Q4:** What can you do that NO alternative can do? (Features, approach, delivery model)
**Q5:** What category do you compete in? (If creating a new category, name it)
**Q6:** Are you in an existing market, new market, or resegmenting an existing market?

Store as: `alternatives_primary[]`, `alternatives_status_quo`, `alternatives_why_leaving`,
`unique_capabilities`, `category`, `market_type`

**Confirm Section 3:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 5: Voice & Tone (5 Questions)

**Why this section:** Consistency across channels. Every writing skill reads this
before producing copy. Without it, outputs sound like AI. With it, they sound like you.

**Q1:** Pick 3–5 words that describe your brand voice.
**Q2:** Does your tone shift when talking to different personas? Describe the shifts.
**Q3:** Any language preferences? ("We say X, not Y")
**Q4:** Any words or phrases you NEVER use? (Jargon, clichés, competitor language)
**Q5:** Paste a paragraph of copy that perfectly captures your voice.

Store as: `voice_attributes[]`, `tone_shifts`, `language_preferences`,
`forbidden_phrases`, `tone_example`

**Confirm Section 4:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 6: Market Context (4 Questions)

**Why this section:** The "why now" that makes launches feel inevitable rather than
arbitrary. Without this, GTM briefs lack urgency and messaging lacks a market narrative.

**Q1:** How mature is your market? (Nascent / Emerging / Growing / Mature)
**Q2:** What macro trends or forces make your solution relevant NOW?
**Q3:** Complete: "Buyers need [your product] NOW because _____"
**Q4:** What's the bigger story about where the market is going? (2–3 sentences)

Store as: `market_maturity`, `macro_forces`, `why_now`, `market_narrative`

**Confirm Section 5:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 7: Proof Points Registry (3 Questions)

**Why this section:** Claims without evidence get cut by legal and ignored by buyers.
This is the approved claims registry every battlecard and launch brief pulls from.

**Q1:** What metrics can your team confidently cite? (With sources if possible)
**Q2:** Any customer quotes, testimonials, or case study results you can reference?
**Q3:** Any claims your team is NOT allowed to make? (Unverified, exaggerated, legally risky)

Store as: `approved_metrics[]`, `proof_points_quotes`, `forbidden_claims`

**Confirm Section 6:** Show answers. "Look good? (yes / edit / skip for now)"

---

### Step 8: Generate and Save Brain File

Once all 6 sections are confirmed:
- Populate all 31 variables from wizard answers
- Write to `/foundation/brain.md`
- Delete `/foundation/.brain-draft.md` if it exists
- Confirm to user:

```markdown
✅ Your brain is live at /foundation/brain.md

Every PMM skill in this ecosystem will now read from it automatically.
ICP, positioning, alternatives, voice, proof points — captured once, used everywhere.

Want to see your brain file? (yes / no)
```

---

### Step 9: Post-Setup Routing (Role × Focus)

After brain is confirmed live, ask ONE question:

> "What's your primary focus right now? I'll point you to the right skills."
>
> 1. Launching a product or feature
> 2. Fixing or refreshing our positioning
> 3. Building competitive intelligence
> 4. Understanding our buyers better
> 5. Enabling the sales team
> 6. Planning the quarter (OKRs, priorities)

Then surface 2–3 skills matched to their answer:

**Path 1 — Launch:**
- `go-to-market-strategy` — tier the launch, build the strategy brief
- `hs-pre-mortem` — stress-test before committing resources
- `hs-gaccs-brief` — campaign brief with channels and messaging

**Path 2 — Positioning:**
- `hs-positioning-messaging` — full positioning BUILD or AUDIT
- `hs-alternatives-map` — map what buyers actually compare you to
- `hs-value-prop-statements` — persona-specific value props

**Path 3 — Competitive:**
- `hs-competitive-battlecard` — build or refresh a battlecard
- `hs-ci-stakeholder-briefing` — exec-level competitive newsletter
- `hs-alternatives-map` — named alternatives framework

**Path 4 — Buyers:**
- `hs-buyer-personas` — buying committee map and messaging personas
- `hs-icp` — build or pressure-test your ICP
- `hs-interview-summary` — synthesize customer discovery

**Path 5 — Sales enablement:**
- `hs-value-prop-statements` — persona-specific statements for decks and talk tracks
- `hs-competitive-battlecard` — objection handling and attack angles
- `hs-stakeholder-maps` — map champions, blockers, and internal power

**Path 6 — Quarterly planning:**
- `hs-brainstorm-okrs` — build or pressure-test PMM OKRs
- `workflow-orchestrator` — chain multiple skills into a full program
- `hs-prioritization-frameworks` — score and tier your initiative backlog

For senior operators and VP-level users, also surface:
- `workflow-orchestrator` — for any multi-skill program
- `hs-ci-stakeholder-briefing` — for exec-level competitive updates

---

## Outputs

- **Files written:** `/foundation/brain.md` — 6 sections, all 31 variables populated.
  All PMM skills read this. `/foundation/.brain-draft.md` — partial state written if
  wizard is interrupted, deleted once full brain is written.
- **Chat output format:** Section-by-section confirmation → final brain summary →
  success message → post-setup routing (Step 9). Each section shows answers and asks
  for confirmation before proceeding.
- **External side effects:** If legacy v1.x files in `.agents/`, migration is offered
  with field-by-field confirmation. Old files are not deleted — user keeps them.

---

## Verification

| Check | Standard | Pass = |
|---|---|---|
| All 6 sections populated | No section is blank or Placeholder | Yes |
| Answers are specific | No vague values — ICP has company size, industry, role | Yes |
| Alternatives named | At least 2 named alternatives + status quo defined | Yes |
| Proof points quantified | At least 1 metric with a number and source | Yes |
| Brain file written | `/foundation/brain.md` exists and is parseable | Yes |
| Post-setup routing ran | User received skill recommendations matched to focus | Yes |

---

## Do Not Use For

- **One-time positioning work** → `hs-positioning-messaging` (reads brain + generates output)
- **Competitive analysis** → `hs-competitive-battlecard`
- **Buyer research** → `hs-buyer-personas`
- **OKR planning** → `hs-brainstorm-okrs`
- **Multi-skill programs** → `workflow-orchestrator` (runs skills in sequence using brain)
- **Direct file edits without Q&A** — always edit brain through this skill's wizard.
  Direct edits bypass validation and can introduce inconsistencies.

---

## Operating Rules

- **Show value before asking for setup.** First-run users see the first-run hook (Step
  Pre-flight) before wizard questions. They know what they're building and why before
  they start. This is the Ramp Glass principle: earn the setup, don't demand it.
- **Never run wizard without brain state check.** Always check `/foundation/brain.md`
  first. If it exists, offer View/Edit/Rebuild — never auto-launch the wizard.
- **Validate specificity at every answer.** Reject vague answers inline: "We sell to
  businesses" → push back: "Be more specific — what company size, industry, or role?"
  The brain is only as sharp as the answers that build it.
- **Save partial state on any interrupt.** If user quits mid-wizard, write
  `/foundation/.brain-draft.md` with all completed sections and current question
  number. On next run, detect draft and offer to resume from exactly where they left.
- **Parse legacy files with confirmation, never silently.** Show each extracted field
  before writing. User must confirm. Silent migration introduces errors that corrupt
  the brain without anyone noticing.
- **Post-setup routing is mandatory.** After every completed brain setup or edit,
  run Step 9. A brain without a next action is a brain that doesn't get used.
- **Role-surface the right skills.** VP and senior operators get `workflow-orchestrator`
  and `hs-ci-stakeholder-briefing` surfaced alongside path skills. IC operators get
  individual execution skills. Ask about focus, not title — focus reveals role.
- **Brain writes require section confirmation.** Each section must be confirmed before
  writing. Never write the brain file from unconfirmed answers.
- **Never recommend direct file edits.** If user wants to edit brain manually, redirect
  to `--edit-section [1-6]` wizard flow. Manual edits bypass validation.

---

## Quality Gate

Runs after brain file is written, before Step 9 routing.

| Check | Standard | Pass = |
|---|---|---|
| First-run hook ran (new users) | Value shown before wizard started | Yes |
| All 6 sections confirmed | User confirmed each section before proceeding | Yes |
| No placeholder values written | Brain file has no blank or "TBD" fields | Yes |
| Specificity checks passed | ICP has numbers, alternatives are named products | Yes |
| Brain file written to correct path | `/foundation/brain.md` exists | Yes |
| Post-setup routing completed | Step 9 ran and skills surfaced for user's focus | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Check if `/foundation/brain.md` exists — load it silently.
2. Check `knowledge/brain/rules.md` if it exists — apply confirmed quality patterns.
3. Note current brain section scores if last audit was run — flag degraded sections.

### After every completed brain setup or edit:
1. Note which sections users most commonly skip or ask to revisit.
   Log to `knowledge/brain/hypotheses.md`.
2. Note which answers most commonly fail the specificity check.
   If same field fails 3+ times across sessions → propose a more specific example
   prompt for that question. Log proposed change to `knowledge/brain/hypotheses.md`.
3. Note which post-setup routing path was chosen most. If one path dominates,
   consider surfacing it as the default suggestion.
4. Log session: setup or edit, sections completed, routing path chosen.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed this session]
Proposed update: [exact wording — what would be added or changed]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.3.0 — 2026-06-12
Spec compliance fixes (11/19 → 18/19) + Glass onboarding + role routing.

- **F1/F5:** Moved `version:` and `last_updated:` to root level (were nested in metadata).
- **F3:** Description expanded to 412 chars with "Trigger on:" phrase verbatim.
- **S6:** Verification converted from checkbox list to binary table (6 checks).
- **T2:** Added Quality Gate section (6 binary checks in table format).
- **T3:** Added Self-Improvement Loop (before/after + trigger format).
- **Q2:** Step 8 success message wrapped in ```markdown fence.
- **Pre-flight:** First-run hook added (Ramp Glass pattern) — shows value before
  asking for setup effort. Zero-state detection hardened.
- **Step 9:** New post-setup routing step — one question maps user's focus to 2–3
  specific skills. Senior/VP operators surface `workflow-orchestrator` and
  `hs-ci-stakeholder-briefing` alongside path skills.
- **Operating Rules:** Two new rules — first-run hook (Rule 1) and role-surface
  routing (Rule 7). Total: 9 rules.

### v2.2.0 — 2026-06-11
Restructured to SKILL-SPEC v2.0.0 (partial). Removed brain-audit logic (now uses
`meta-verify`). Added legacy v1.x migration. Added partial-state save on interrupt.

### v2.1.0 — 2026-05-20
Initial brain wizard + audit combined. Six-section setup.

### v2.0.0 — 2026-05-01
Renamed from "pmm-foundation". Introduced `/foundation/` directory convention.
