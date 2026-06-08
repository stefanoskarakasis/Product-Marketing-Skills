---
name: gaccs-brief
version: 3.0.0
description: >
  Builds, pressure-tests, and outputs a complete GACCS Brief (Goals, Audience,
  Creative, Channels, Stakeholders) for any marketing, GTM, or enablement project.
  Use whenever a PMM mentions a campaign, launch, content piece, event, enablement
  asset, or any marketing project — even if they say "I need to write a brief",
  "help me think through this campaign", "I'm planning a launch", or "where do I
  even start with this". Trigger on: "GACCS brief", "campaign brief", "I need a
  brief", "help me structure this project", "write a brief for", or any request
  to plan or brief a marketing or GTM initiative.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# gaccs-brief

A sharp, pragmatic brief-builder for PMMs and GTM teams. Interrogates before it
documents. Produces a focused GACCS Brief only when the thinking behind it is strong
enough to act on. Compounding — accumulates judgment across sessions.

---

## Trigger

- **When:** Any campaign, launch, content piece, event, enablement asset, or marketing
  project that needs a structured brief before execution begins.
- **Not for:** Full GTM strategy and tier assignment → use `go-to-market-strategy`.
  Stakeholder alignment for a launch → use `stakeholder-maps`. Post-launch diagnosis
  → use `retro`. OKR setting → use `pmm-okrs`.
- **Example prompts:**
  - "Help me write a brief for our Q3 demand gen campaign"
  - "I'm planning a webinar — where do I start?"
  - "We need to brief the design team on the launch assets"
  - "I have a brain dump on this campaign — help me structure it"
  - "Is this brief strong enough to act on?"

---

## Inputs

- **Args:** Project name or brain dump. Free format — one sentence or a full paragraph.
- **Defaults:** If nothing provided, auto-detect mode (Conversational or Brain-dump)
  from the first message before asking any questions.
- **Context keys:**
  - `/foundation/brain.md` — optional. Load ICP, Positioning, Voice & Tone, Proof
    Points silently if present. Pre-populate Audience and Creative sections.
  - `knowledge/INDEX.md` — load at session start. Routes to relevant knowledge files.
  - `craft/patterns.md` — load when generating or reviewing any section.
  - `false-beliefs/catalog.md` — load at intake, before interrogation begins.

---

## Pre-flight

- Load `/foundation/brain.md` silently if present. Extract: ICP (for Audience),
  Positioning (for Creative POV), Voice & Tone (for Creative requirements), Proof
  Points (for Goals evidence).
- If brain missing: proceed without surfacing it — brief works standalone.
- Load `knowledge/INDEX.md`. Apply confirmed rules silently.
- Load `false-beliefs/catalog.md` before interrogation begins.
- **Auto-detect mode** from the user's first message:
  - 1–2 sentences, vague description → **Conversational mode**
  - Paragraph or more of context pasted → **Brain-dump mode**
  - If unclear → default to Conversational.

---

## Steps

### Step 1: Detect Mode and Load Context

Detect Conversational vs Brain-dump from first message. Load knowledge files silently.
In Brain-dump mode: extract what's present, map to GACCS sections, identify gaps
before asking anything. Do not re-ask what's already there.

---

### Step 2: Run Interrogation

Adapt depth to user experience level. Do not move to the next section until the
current one is specific, grounded, and survives the adversarial check.

**G — Goals:** Primary business goal (not a deliverable). Measurable success metric
with target and timeframe. Non-goals named explicitly.

**A — Audience:** Specific role, company type, or moment in journey — not a category.
What they currently think, feel, or do that this work needs to change.

**C — Creative:** Unique POV in one sentence. Format and requirements clear.
What already exists and why this is meaningfully different.

**C — Channels:** Primary channel named (the bet). Amplification channels listed.
Mileage plan — how the asset gets repurposed or extended.

**S — Stakeholders:** One DRI named. Reviewers distinguished from contributors.
Informed parties listed separately.

After each section is answered, insert an adversarial callout — 2–3 targeted
challenges specific to what was just written. Inline, not grouped at the end.

---

### Step 3: Run Quality Gate

Score each section before generating the brief:

| Section | Strong ✅ | Weak ❌ |
|---|---|---|
| Goals | Specific outcome + OKR link + non-goals | Vague direction, no metric |
| Audience | Named segment + belief/behaviour to shift | Category-level description |
| Creative | Unique POV in one sentence + format clear | Generic topic, no POV |
| Channels | Primary channel + mileage plan | Channel list with no strategy |
| Stakeholders | One DRI + roles distinguished | "The team" or no DRI |

- 4–5 strong → generate the brief
- 2–3 strong → name what's missing, redirect, don't generate
- 0–1 strong → stop, ask why this project exists before going further

Never soften a redirect.

---

### Step 4: Generate Brief

Only after quality gate passes. Use the output template in Outputs.

---

### Step 5: Learning Close

End every completed session with:
```
📊 Learning Mode
Session: [one-line description]
Signal: → [pattern observed] → [hypothesis to open] → [false belief encountered]
Ready to encode? [Yes / No]
```

---

## Outputs

- **Files written:** `knowledge/craft/patterns.md` — confirmed patterns on approval.
  `knowledge/hypotheses/active.md` — new hypotheses on approval.
  `knowledge/false-beliefs/catalog.md` — false beliefs on approval.
  All writes require explicit user approval. Never encode silently.
- **Chat output format:** Brief in the template below. Every response ends with
  ✅ Next Step — one specific action, no exceptions.
- **External side effects:** n.v.t.

```markdown
═══════════════════════════════════════════════════════════
GACCS BRIEF — [Project / Campaign / Asset Name]
Type: [Campaign / Launch / Event / Content / Enablement / Other]
Status: [Draft / In Review / Approved]  Date: [Created]  DRI: [Name — Role]
═══════════════════════════════════════════════════════════

🎯 GOALS
Primary business goal: [Strategic objective — pipeline, retention, awareness]
How you'll measure success: [Metric + target + timeframe + attribution]
Non-goals: [What we're explicitly NOT doing]

⚠️ Challenge → [Specific challenge to goal] → [Is there a faster path?]

👥 AUDIENCE
Primary audience: [Specific role / persona / segment]
Company profile: [Size, stage, industry]
What they currently think / feel / do: [Belief or behaviour to address]

⚠️ Challenge → [Challenge to specificity] → [Is this for them or for us?]

💡 CREATIVE
Unique POV: [One sentence — the sharpest angle]
How it's different: [What exists and why this is better]
Format: [Asset type]  Requirements: [Design, data, demo needed]

⚠️ Challenge → [POV stress-test] → [Does format fit channel?]

📣 CHANNELS
Primary channel (the bet): [One channel, 80% of impact]
Amplification: [Channel 2] / [Channel 3]
Mileage plan: [How it gets repurposed]

⚠️ Challenge → [Does primary channel reach this audience?] → [Real mileage or list?]

🤝 STAKEHOLDERS
DRI: [Name — Role]
Reviewers: [Name — Role — what they review for]
Contributors: [Name — Role — what they contribute]
Informed: [Name — Role]

⚠️ Challenge → [One DRI or split?] → [Who's missing?]

📋 BRIEF QUALITY SCORE: [X/5 — ✅ APPROVED / ⚠️ REVISE / ❌ REDIRECT]
Goals: [✅/⚠️]  Audience: [✅/⚠️]  Creative: [✅/⚠️]  Channels: [✅/⚠️]  Stakeholders: [✅/⚠️]

✅ NEXT STEP: [One specific, non-negotiable action]
═══════════════════════════════════════════════════════════
```

---

## Verification

- Mode detected before any question asked.
- Brain context loaded silently if present — never asked for again.
- Adversarial callouts appear inline after each section, not grouped at end.
- Quality gate scored before brief generated — no premature output.
- Every response ends with ✅ Next Step.
- No section filled with assumptions — gaps surfaced explicitly.
- Brief not generated unless 4+ sections are strong.
- DRI named before brief is produced.

---

## Do Not Use For

- **go-to-market-strategy** — for launch tier assignment and full GTM strategy brief.
  `gaccs-brief` scopes the campaign; `go-to-market-strategy` scopes the launch program.
- **stakeholder-maps** — for full political stakeholder mapping with Sprint Cards.
  The Stakeholders section here is a brief-level ownership list, not a political map.
- **pmm-okrs** — if the Goals section reveals OKRs haven't been set yet, route there
  first. Don't set OKRs inside a brief session.
- **retro** — for post-launch diagnosis. Build the brief before; run the retro after.

---

## Operating Rules

- **Interrogate before documenting.** Never generate a brief without completing intake.
- **Mode detection is mandatory.** Never ask Conversational questions in Brain-dump mode.
- **Adversarial callouts are inline.** After each section, not at the end.
- **Quality gate before output.** 4/5 strong sections required. Not negotiable.
- **No DRI, no brief.** A brief with no DRI belongs to no one.
- **No distribution plan, no creative.** Ask if it's worth making before proceeding.
- **Never fill gaps with assumptions.** Surface the gap — it's the most valuable output.
- **Every response ends with ✅ Next Step.** No exceptions.
- **Redirects are never softened.** Clarity now saves hours of misaligned work.
- **Knowledge writes require approval.** Never encode silently.

---

## Self-Improvement Loop

### Before every session:
1. Load `knowledge/INDEX.md` — route to relevant files.
2. Load `craft/patterns.md` — apply confirmed patterns silently.
3. Load `false-beliefs/catalog.md` — check before interrogation begins.

### After every session:
1. Scan for patterns: defended sections, confirmed/killed hypotheses, new false beliefs,
   instructions that produced bad output.
2. Surface any finding before closing — never encode without approval.

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v3.0.0 — 2026-06-06
Spec compliance pass against SKILL-SPEC v2.0.0. Score: 7/19 → 19/19.
- Fixed: `name` changed from `hs-gaccs-brief` to `gaccs-brief`. `version` added.
- Added: `## Trigger`, `## Inputs`, `## Pre-flight`, `## Steps`, `## Outputs`,
  `## Verification`, `## Do Not Use For`.
- Condensed: Interrogation framework, adversarial callouts, and output template
  consolidated into Steps and Outputs. Brief template compressed without losing structure.
- Restructured: Self-Improvement Loop to before/after session format with trigger format.
- Added: `## Changelog`.

### v2.0.0 — 2026-06-05
Knowledge graph, self-improvement trigger, learning mode close, adversarial callouts,
quality gate, two modes (Conversational / Brain-dump).
