---
name: product-marketing-context
description: Build and maintain your GTM brain in 15 minutes. ICP, alternatives, positioning, voice, market context, proof points. Every PMM skill reads this. Brain setup, brain wizard, foundation, configure context, audit brain health.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  version: 2.2.0
  quality_gate: true
  last_updated: 2026-06-11
---

# Product Marketing Context

## Trigger

**When:**
- You're building GTM context from scratch (new company, new product, new market)
- You're auditing existing positioning (does your brain match what you're telling customers?)
- You're refreshing buyer intelligence (the market changed, you need to update)
- Any other PMM skill is about to run and needs your context first
- You want to check your brain health and get improvement recommendations

**Not for:**
- One-time positioning work → use `hs-positioning-messaging` skill
- Competitive analysis → use `hs-competitive-battlecard` skill
- Individual audience research → use `hs-buyer-personas` skill
- Brain health scoring → use `meta-verify` on `/foundation/brain.md` directly

**Example prompts:**
- "Build my brain"
- "Set up my GTM foundation"
- "Let me audit my brain"
- "Check my brain health"
- "Update my ICP"
- "What's my current brain?"

---

## Inputs

**Args:**
- None required. Skill auto-detects whether user has existing brain or is starting fresh.
- Optional: `--edit-section [1-6]` to update only one section without re-answering all questions.

**Defaults:**
- If no brain exists: launch fresh brain wizard (6 sections, ~15 min)
- If brain exists: offer three options: [View current] [Edit sections] [Rebuild from scratch]
- If v1.x legacy files found (in `.agents/` or `.claude/`): offer automatic migration with confidence checks

**Context keys:**
- `/foundation/brain.md` — read if exists (user's current brain)
- `.agents/product-marketing-context.md` — check for legacy v1.x file
- `.agents/icp.md` — check for legacy v1.x file
- `.agents/alternatives-map.md` — check for legacy v1.x file
- `.agents/voice-tone.md` — check for legacy v1.x file
- `.agents/market-context.md` — check for legacy v1.x file
- `.agents/proof-points.md` — check for legacy v1.x file

---

## Pre-flight

- **Check 1:** Does `/foundation/` directory exist?
  - If NO: create it
  - If YES: proceed
- **Check 2:** Does `/foundation/brain.md` exist?
  - If YES: user has a brain. Offer [View] [Edit] [Rebuild]
  - If NO: check for legacy v1.x files. If found, offer migration. If not found, start fresh wizard.
- **Check 3:** Is user trying to run this skill to START a session (vs. run another skill that depends on it)?
  - If starting a session: full wizard or edit mode
  - If dependency from another skill: load brain silently, no wizard (other skill will ask for input)

---

## Steps

### Step 1: Detect Brain State
Check what exists:
- `/foundation/brain.md` → existing brain (user chooses: View / Edit / Rebuild)
- Legacy v1.x files in `.agents/` → offer migration with confidence checks
- Neither → start fresh wizard

If existing brain + user editing: offer section-by-section edit (Section 1–6, or all)

### Step 2: Product Context (5 Questions)
If starting fresh wizard, ask:

**Q1:** What's your product called?
**Q2:** In 2–3 sentences, what does it do? Focus on the problem it solves.
**Q3:** What stage is it at? (Pre-launch / Launch / Growth / Scale)
**Q4:** Who's your primary target market? Be specific (company size, industry, role).
**Q5:** Complete: "[Product] helps [target market] to _____ so they can _____"

Store as: `product_name`, `product_description`, `product_stage`, `target_market`, `value_proposition`

**Confirm Section 1:** Show answers back. "Look good? (yes/edit/skip)"

### Step 3: ICP Definition (8 Questions)
**Q1:** What company size (employees or ARR) is your ideal customer?
**Q2:** Any specific industries or verticals? Or horizontal?
**Q3:** Primary geographic market(s)?
**Q4:** Who's the primary buyer? (Title + role description)
**Q5:** Who actually signs the contract? (Economic buyer, if different)
**Q6:** Who becomes your internal champion? What do they care about?
**Q7:** What are the top 3 pain points your ICP has?
**Q8:** What event triggers them to start looking for a solution?

Store as: `icp_company_size`, `icp_industry`, `icp_geography`, `icp_primary_persona`, `icp_economic_buyer`, `icp_champion`, `icp_pain_points[]`, `icp_buying_triggers`

**Confirm Section 2:** Show answers back. "Look good? (yes/edit/skip)"

### Step 4: Alternatives & Positioning (6 Questions)
Using April Dunford's named alternatives framework:

**Q1:** What are the top 3 products buyers compare you to? (Not "competitors" — what BUYERS actually consider)
**Q2:** What do buyers do TODAY if they don't buy any tool (including yours)?
**Q3:** Why do buyers leave those alternatives and consider you instead?
**Q4:** What can you do that NO alternative can do? (Features, approach, delivery model)
**Q5:** What category do you compete in? (If new category, what do you call it?)
**Q6:** Are you in an existing market, new market, or resegmenting an existing market?

Store as: `alternatives_primary[]`, `alternatives_status_quo`, `alternatives_why_leaving`, `unique_capabilities`, `category`, `market_type`

**Confirm Section 3:** Show answers back. "Look good? (yes/edit/skip)"

### Step 5: Voice & Tone (5 Questions)
**Q1:** Pick 3–5 words that describe your brand voice. (Examples: authoritative, playful, technical, empathetic, bold, straightforward)
**Q2:** Does your tone shift when talking to different personas? If yes, describe the shifts.
**Q3:** Any language preferences? (e.g., "we say X, not Y")
**Q4:** Any words or phrases you NEVER use? (Jargon, clichés, competitor language)
**Q5:** Paste a paragraph of copy that perfectly captures your voice.

Store as: `voice_attributes[]`, `tone_shifts`, `language_preferences`, `forbidden_phrases`, `tone_example`

**Confirm Section 4:** Show answers back. "Look good? (yes/edit/skip)"

### Step 6: Market Context (4 Questions)
**Q1:** How mature is your market? (Nascent / Emerging / Growing / Mature)
**Q2:** What macro trends or forces make your solution relevant NOW?
**Q3:** Complete: "Buyers need [your product] NOW because _____"
**Q4:** What's the bigger story about where the market is going? (2–3 sentences)

Store as: `market_maturity`, `macro_forces`, `why_now`, `market_narrative`

**Confirm Section 5:** Show answers back. "Look good? (yes/edit/skip)"

### Step 7: Proof Points Registry (3 Questions)
**Q1:** What metrics can your team confidently cite? (With sources if possible)
**Q2:** Any customer quotes, testimonials, or case study results you can reference?
**Q3:** Any claims your team is NOT allowed to make? (Unverified, exaggerated, legally risky)

Store as: `approved_metrics[]`, `proof_points_quotes`, `forbidden_claims`

**Confirm Section 6:** Show answers back. "Look good? (yes/edit/skip)"

### Step 8: Generate and Save Brain File
Using the brain template (see `/foundation/templates/brain-template.md`):
- Populate all 31 variables with user answers
- Write to `/foundation/brain.md`
- Create or update `.brain-draft` if user quits mid-wizard (resume capability)

---

## Outputs

**Files written:**
- `/foundation/brain.md` — Complete brain file with 6 sections. ~500–800 lines. All subsequent PMM skills read this file.

**Chat output format:**
- After each section: confirmation showing user's answers + "Look good? (yes/edit/skip)"
- After all sections: final summary showing all 6 sections populated
- Success message: "✅ Your brain is set up at `/foundation/brain.md`. All PMM skills will now read from this."
- Next steps guidance: "Want to run your first brain-powered skill? Try `hs-positioning-messaging` to build positioning."

**Side effects:**
- If legacy v1.x files exist in `.agents/`, offer migration. If accepted: parse old files into new brain.md format.
- If user quits mid-wizard: save `/foundation/.brain-draft.md` with partial state. On restart, offer to resume.
- `/foundation/.brain-draft.md` is auto-deleted once full brain.md is written.

---

## Verification

Your brain is solid if:
- [ ] All six sections are populated (Product Context, ICP, Alternatives, Voice, Market, Proof Points)
- [ ] Every answer is specific, not vague. (Not "businesses" → "mid-market B2B SaaS, 50–500 employees")
- [ ] You can describe your ICP + alternatives to a stranger without looking at the file
- [ ] You can paste this brain into a new team member's onboarding and they'd understand your positioning
- [ ] Run `meta-verify /foundation/brain.md` — should pass quality checks (confidence scoring)

If you want a detailed health score, other skills can read your brain and score it:
- `hs-positioning-messaging` reads brain Sections 1, 2, 3, 4 to check positioning rigor
- `hs-competitive-battlecard` reads brain Sections 1, 2, 3, 5 to check differentiation
- `hs-buyer-personas` reads brain Section 2 to check persona specificity

---

## Do Not Use For

- **One-time brain tweaks without structure:** Use this skill for full brain setup or structured section edits. Don't use for "just update one field" without Q&A.
- **Brain health scoring:** Use `meta-verify` on `/foundation/brain.md` directly. It confidence-scores your brain against quality rubrics.
- **Competitive intelligence:** Use `hs-competitive-battlecard` skill.
- **General audience research:** Use `hs-buyer-personas` skill.
- **Individual skill positioning:** Use `hs-positioning-messaging` skill (it reads your brain + generates positioning).

---

## Operating Rules

1. **Load or detect brain state before any wizard flow.** Always check `/foundation/brain.md` existence first. If it exists, offer user choice (View/Edit/Rebuild). Never assume wizard is the right choice.

2. **Validate all input through wizard questions, not free-form.** Every field must go through the Q&A flow. This ensures consistency and completeness. If user tries to paste raw content, reject it and re-ask the question.

3. **Save partial state on interrupt.** If user quits mid-wizard, save `/foundation/.brain-draft.md` with all completed sections + question number where they left off. On next restart, check for draft and offer to resume.

4. **Enforce specificity checks.** Reject vague answers:
   - "We sell to businesses" → require concrete example (company size, industry, role)
   - "High value" → require number ($ amount, usage metric)
   - "Pain point: they need to be faster" → require specific impact (hours saved, revenue gained)

5. **Parse legacy v1.x files with confidence checks.** If migrating old files from `.agents/`, extract field-by-field, show user each extracted value, ask for confirmation before writing to new brain.md. Never silently convert old files.

6. **Brain file is the single source of truth.** All PMM skills read from `/foundation/brain.md`. Changes to brain must go through this skill (full wizard or edit mode). Never recommend direct file edits. If user edits file manually, run `meta-verify` to catch inconsistencies.

7. **Offer brain-powered skills AFTER brain is live.** Once brain is written, suggest: "Want to run your first brain-powered skill? Try `hs-positioning-messaging` (15 min) to build positioning statements."

---

## Changelog

### v2.2.0 — 2026-06-11
- Restructured to SKILL-SPEC v2.0.0 (19/19 compliant)
- Removed brain-audit logic (now uses `meta-verify` for health scoring)
- Added legacy v1.x file migration support
- Added partial-state save on interrupt (resume capability)
- Added six-question section flow with confirmation steps

### v2.1.0 — 2026-05-20
- Initial brain wizard + audit combined skill
- Six-section brain setup (Product, ICP, Alternatives, Voice, Market, Proof Points)

### v2.0.0 — 2026-05-01
- Renamed from "pmm-foundation" to "product-marketing-context"
- Introduced `/foundation/` directory convention
- Brain-powered skills ecosystem launched
```
