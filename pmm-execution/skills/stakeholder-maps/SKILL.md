---
name: stakeholder-maps
version: 3.0.0
description: >
  PMM stakeholder intelligence engine. Builds a political map — not a grid — that tells
  you who can kill your launch, who can champion it, and exactly what to say to each.
  Trigger on: "stakeholder map", "who do I need to align", "stakeholder plan", "who can
  block this", "executive alignment", "cross-functional buy-in", "who owns what",
  "communication plan", "launch alignment", "who do I brief", "who needs to know",
  "internal enablement", "build my stakeholder map", or any request to map, engage,
  or align stakeholders around a GTM initiative, launch, or campaign.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# stakeholder-maps — PMM Stakeholder Intelligence Engine

Stakeholder maps built in a vacuum are a waste of time. This skill builds a map anchored
to political reality: who has power over your launch, who's a hidden champion, who's a
silent blocker, and what the map tells you to do before you're in the room — not after.

---

## Trigger

- **When:** Any launch, campaign, pricing change, new channel, GTM pivot, or internal
  programme where internal alignment determines whether the initiative succeeds or stalls.
- **Not for:** Positioning or messaging work → use `positioning-messaging`. Post-launch
  diagnosis → use `retro`. Risk analysis of the initiative itself → use `pre-mortem`.
  Campaign brief building → use `gaccs-brief`.
- **Example prompts:**
  - "Build a stakeholder map for our enterprise pricing launch"
  - "Who do I need to align before we announce the rebrand?"
  - "Who can block our Q3 GTM pivot?"
  - "/map analytics dashboard launch"
  - "Generate Sprint Cards for the SSO integration rollout"

---

## Inputs

- **Args:** Initiative name or one-line description. Free format.
- **Defaults:** If no initiative named, run intake before proceeding. Never generate
  a map without a named initiative and confirmed decision gate.
- **Context keys:**
  - `/foundation/brain.md` — optional but recommended. Load ICP Prioritisation,
    Positioning, GTM Motion, Revenue Levers, Beachhead Segment silently if present.
  - `knowledge/INDEX.md` — load confirmed rules and active hypotheses before intake.
  - `sessions/` — check for existing map on this initiative before building a new one.
  - `decisions/` — load prior structural decisions before making new ones.

---

## Pre-flight

- Load `/foundation/brain.md` silently if present. Extract: ICP Prioritisation,
  Positioning, GTM Motion, Revenue Levers, Beachhead Segment.
- If brain missing: proceed, surface once:
  > "No brain found. Run `product-marketing-context` first for sharper stakeholder
  > framing. Continuing — map will be initiative-specific only."
- Load `knowledge/INDEX.md` — apply confirmed rules silently before intake.
- Check `sessions/` — if a map for this initiative already exists, offer to update
  it rather than rebuild from scratch.

---

## Steps

### Step 1: Run Intake

Ask in one message. Never build without context.

> "Before I build the map:
> 1. **What's the initiative?** One sentence.
> 2. **What does success look like in 60–90 days?** A number, a behaviour, a deal.
> 3. **Who has explicitly said yes?** Name them by role.
> 4. **Who has said nothing or might push back?** Silence is not alignment.
> 5. **What's the highest-stakes decision needed?** And who makes it or can veto it?
> 6. **When does the first irreversible action happen?** Announcement, budget commit, customer comms."

Reflect back the initiative in 3 sentences before proceeding.

---

### Step 2: Run Inversion Check

After reflecting back, ask:
> "If this launch failed because of an internal stakeholder — who would it most likely
> be, and why? Not execution gaps. The person whose resistance or inaction is the root cause."

If they can't answer: flag that the political map is assumed, not validated.

---

### Step 3: Build the Map

Classify each stakeholder on Power × Interest:

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | 🔴 Manage Closely | 🟡 Keep Satisfied |
| **Low Power** | 🟢 Keep Informed | ⚪ Monitor |

Then assign political role:

| Role | Signal |
|---|---|
| 🏆 Champion | Proactively advocates. Extends credibility. |
| 🛑 Blocker | Actively opposes or competes for resources. |
| 🧊 Frozen | Silent. Neither opposing nor supporting. |
| 🔍 Gatekeeper | Controls access to decision-maker or budget. |
| 🎭 Performer | Says yes in rooms, acts differently outside. |
| 🌊 Floating Voter | Undecided. Moveable with evidence or early wins. |

> ⚠️ Never assume malice. Most blockers are Frozen Voters with incomplete context.

---

### Step 4: Generate Document A — The Map

Render an HTML widget first (Power × Interest grid with stakeholder chips, Communication
Plan table, Conflict Map cards, PMM Confidence Assessment), then the markdown diagnostic.

Map diagnostic includes per Manage Closely / Keep Satisfied stakeholder:
- Why they matter (their specific power over this initiative)
- What they care about (their actual priority, not their title)
- Risk if neglected (second-order consequence)
- Key message (exact framing they need, not generic positioning)

---

### Step 5: Generate Document B — Sprint Card

Immediately after the Map. Covers Manage Closely and Keep Satisfied only.
Five fields per card. No exceptions. No paragraphs.

Fields: Next touchpoint / Send before touchpoint / What you need from them /
The one sentence that has to land / Watch For signal + immediate action.

---

### Step 6: Run Quality Gate and Learning Close

Run the quality gate (14 checks). Deliver only on pass.

Learning close — ask three questions before ending:
1. Which stakeholder landed in a different place than expected?
2. Which card are you most confident will hold?
3. Which card do you most doubt — and what will slip first?

Log Q3 answer to `knowledge/` as a Watch For pattern candidate.

---

## Outputs

- **Files written:** `sessions/map-[initiative]-[date].md` — Map document.
  `sessions/sprint-[initiative]-[date].md` — Sprint Card document.
  `knowledge/` — Watch For patterns after session close.
  `sessions/log.md` — QG pass/fail logged.
- **Chat output format:** HTML widget → markdown diagnostic → Sprint Cards.
  Both documents in markdown, copy-paste ready for Notion or Google Docs.
- **External side effects:** n.v.t.

---

## Verification

- Initiative named and decision gate confirmed before map generated.
- Inversion check run — who could sink this from inside is named.
- Every stakeholder has quadrant placement AND political role.
- HTML widget rendered before markdown diagnostic.
- Sprint Card generated immediately after Map — never standalone.
- Five fields only per Sprint Card. No exceptions.
- Quality gate scored before either document delivered.
- Watch For patterns logged at session close.

---

## Do Not Use For

- **pre-mortem** — for risk analysis of the initiative itself, not the internal political
  landscape. Use `pre-mortem` to stress-test the plan; use this skill to align the humans.
- **gaccs-brief** — once the map is complete, use `gaccs-brief` to build the comms brief.
  Don't brief campaigns inside a stakeholder mapping session.
- **retro** — for post-launch diagnosis. This skill maps stakeholders before and during;
  `retro` analyses what happened after.
- **pmm-okrs** — if accountability gaps surface during mapping, route to `pmm-okrs` for
  OKR alignment. Don't rebuild OKRs inside a stakeholder session.

---

## Commands

### /map [initiative]
Build the full stakeholder map. Runs intake → inversion → quadrant placement → conflict
map → silent blocker scan → confidence assessment → HTML widget + markdown diagnostic.

### /sprint [initiative]
Generate weekly Sprint Cards from an existing map. Must run `/map` first.

### /deep-dive [name] — [initiative]
Full diagnostic for a single stakeholder: power, priorities, risk if neglected,
key message, Watch For signal, this week's action.

### /update [initiative] — [what changed]
Update map after an alignment conversation. Saves a new versioned map.

### /check [initiative]
Weekly health check. Flags stakeholders silent 7+ days, unresolved conflicts
approaching decision gate, Sprint Cards not updated in 10+ days.

---

## Operating Rules

- **Silence is not alignment.** Any stakeholder who hasn't explicitly engaged is Frozen.
- **The map is not the territory.** Update after every major alignment conversation.
  A 4-week-old map is a historical document, not a working tool.
- **Name the Performers.** Verbal yes with no follow-through is the most common failure.
  Written commitment or it didn't happen.
- **Gatekeepers are not blockers.** Bypassing a Gatekeeper converts them into one.
- **Inversion before confidence.** Before declaring the landscape safe: who could sink this?
- **Conflict without resolution is just documentation.** Assign owner and date.
- **Five fields. No exceptions.** A Sprint Card with six fields is an analysis document.
- **Watch For signals are hypotheses.** Three confirmations makes a rule.
- **Second-order before action.** Ask "and then what?" before every comms decision.
- **Never build without intake.** A stakeholder map without initiative context is an org chart.

---

## Quality Gate

Runs after both documents generated. Surface failures before delivering either.

| Check | Standard | Pass = |
|---|---|---|
| Inversion check run | Named who could sink this | Yes or gap flagged |
| Political role assigned | Every stakeholder has role beyond quadrant | Yes |
| HTML widget rendered | Before markdown diagnostic | Yes |
| Grid populated | Every stakeholder placed with chip + role | Yes |
| Comms plan table | Every MC + KS has key message + next action | Yes |
| Conflict map | Every conflict has risk block + resolution block | Yes |
| Confidence cards | All six dimensions scored | Yes |
| Sprint: five fields | No card has more than five fields | Yes |
| Sprint: execution notes | Every touchpoint has what cannot slip | Yes |
| Sprint: explicit asks | Every card names ask, deadline, fallback | Yes |
| Sprint: Watch For | Every MC card has signal + immediate action | Yes |
| Sprint: next session block | Stakeholder-specific, not generic | Yes |
| Both documents generated | Map and Sprint Card exist as separate files | Yes |
| Brain integration | Map cross-referenced with ICP and GTM motion | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load `knowledge/INDEX.md` — apply confirmed rules silently.
2. Check `knowledge/` for Watch For patterns relevant to this initiative type.
3. Check `sessions/` for an existing map on this initiative.

### After every session:
1. Extract Watch For patterns from Q3 of learning close.
2. Log to `knowledge/[initiative-type]/` with tag.
3. If confirmed 3+ times → propose promotion to `knowledge/INDEX.md` rules.

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed this session]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v3.0.0 — 2026-06-06
Spec compliance pass against SKILL-SPEC v2.0.0. Score: 9/19 → 19/19.
- Fixed: `name` changed from `hs-stakeholder-maps` to `stakeholder-maps`.
- Added: `## Trigger`, `## Inputs`, `## Outputs`, `## Verification`, `## Do Not Use For`.
- Renamed: `## ⓪ PMM CONTEXT — LOAD FIRST` → `## Pre-flight`.
- Restructured: circled sections converted to named `## Steps`.
- Condensed: HTML widget spec, Sprint Card format, Initiative Type Modifiers,
  Section Metadata moved to references. Core logic preserved. Trimmed to <500 lines.
- Self-Improvement Loop restructured to before/after session format.

### v2.2.0 — 2026-04-17
Commands block added: /map, /sprint, /deep-dive, /update, /check.

### v2.1.0 — 2026-04-17
Visual-first output: HTML widget before markdown diagnostic.

### v2.0.0 — 2026-04-17
Map and Sprint Card split into two separate session documents.

### v1.0.0 — 2026-04-17
Initial build.
