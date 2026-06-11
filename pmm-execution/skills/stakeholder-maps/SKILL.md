---
name: hs-stakeholder-maps
version: 2.2.0
description: >
  PMM stakeholder intelligence engine. Builds a political map — not a grid — that tells
  you who can kill your launch, who can champion it, and exactly what to say to each.
  Trigger on: "stakeholder map", "who do I need to align", "stakeholder plan", "who can
  block this", "executive alignment", "cross-functional buy-in", "who owns what",
  "communication plan", "stakeholder communication", "launch alignment", "who do I brief",
  "who needs to know", "internal enablement", "build my stakeholder map", or any request
  to map, engage, or align stakeholders around a GTM initiative, launch, or campaign.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-11
---

# hs-stakeholder-maps — PMM Stakeholder Intelligence Engine

Stakeholder maps built in a vacuum are a waste of time.
This skill builds a stakeholder map anchored to political reality: who has power over your
launch, who's a hidden champion, who's a silent blocker, and what the map tells you to do
before you're in the room — not after.

Built on the Power × Interest grid. Sharpened with second-order thinking, inversion, and
map-vs-territory mental models. Structured using a five-layer institutional knowledge
architecture. Compounding via a self-improving learning loop.

---

## Trigger

- **When:** Stakeholder mapping, internal alignment, launch/campaign readiness, cross-functional planning, execution risk management
- **Not for:** Buyer persona building → use hs-buyer-personas. External competitive intelligence → use hs-ci-stakeholder-briefing. Pricing alignment strategy → use go-to-market-strategy
- **Example prompts:**
  - "Build my stakeholder map for this launch"
  - "Who do I need to align?"
  - "Who can block this?"
  - "Map my stakeholder communication plan"
  - "Internal alignment for a GTM pivot"

---

## Inputs

- **Args:** Initiative name/description (required), success definition (required), timeline (required)
- **Defaults:** If no timeline provided, ask for decision gates. If success undefined, run intake first.
- **Context keys:**
  - `/foundation/brain.md` — optional. Sections 2 (ICP), 3 (Positioning), 5 (GTM Motion) if available
  - `knowledge/INDEX.md` — optional. Load prior stakeholder patterns by initiative type
  - `sessions/` — optional. Prior maps for this initiative (update, don't rebuild from scratch)

---

## Pre-flight

**Block ⓪: PMM CONTEXT — LOAD FIRST**

Before intake, check `.agents/product-marketing-context.md`.

**If it exists — load silently. Extract:**

- `## ICP Prioritisation` → who the launch serves and at what tier; shapes which internal stakeholders matter most
- `## Positioning` → does the stakeholder map reflect the positioning hierarchy? Misalignment here creates mixed internal messaging
- `## GTM Motion & Growth Loops` → which motion is this dependent on? Sales-led vs PLG vs CS-led maps look entirely different
- `## Revenue Levers` → which lever does this initiative target? Finance, Sales, or CS stakeholders gain/lose power accordingly
- `## Beachhead Segment` → if new market entry, which internal teams need to shift and who currently owns the old segment?
- `## Objections & Anti-Personas` → internal objections are often mirrored by anti-persona patterns. Pre-load for blocker diagnosis.

**If context file is missing:**

> "No PMM context found. Run `hs-product-marketing-context BUILD` first to make this significantly sharper.
> Continuing — but stakeholder framing will be initiative-specific only, not grounded in your positioning strategy."

---

## Steps

### ① INTAKE — DO NOT BUILD WITHOUT CONTEXT

> ⚠️ A stakeholder map without initiative context is just an org chart.
> Always run intake before generating any output.

Ask in one message:

> "Before I build the map, I need to understand the landscape:
>
> 1. **What's the initiative?** One sentence. Launch, campaign, pricing change, new channel, or internal programme.
>
> 2. **What does success look like — in 60 or 90 days?**
>    Specific. A number, a behaviour, a deal closed, a capability shipped.
>
> 3. **Who has explicitly said yes to this initiative?**
>    Name them by role. Who's a confirmed champion inside the organisation?
>
> 4. **Who has said nothing — or who do you suspect might push back?**
>    Silence is not alignment. Name the people or functions you're unsure about.
>
> 5. **What's the highest-stakes decision this initiative needs to get made?**
>    And who ultimately makes it — or can veto it?
>
> 6. **What's your timeline?** Specifically: when does the first irreversible action happen?
>    (Announcement, budget commit, agency brief, customer comms, sales enablement kickoff)"

**If they share a brief or plan:**

Read it fully. Extract stakeholder names, decision gates, and power signals. Do not begin mapping until you've reflected back the initiative accurately.

**If they describe verbally:**

Reflect back in 3 sentences. Ask them to correct anything wrong. Assumption-surfacing — not polish.

---

### INVERSION CHECK — ALWAYS RUN AFTER REFLECT-BACK

After reflecting back the initiative, ask:

> "One more: **if this launch failed because of an internal stakeholder — who would it most likely be, and why?**
> Not execution gaps. The person or team whose resistance, inaction, or misalignment would be the root cause."

**If they can't answer clearly:**

> "⚠️ If you can't name who could sink this from the inside, the political map is assumed — not validated.
> That's where stakeholder plans fail. We'll surface it in the mapping step."

---

### ② THE STAKEHOLDER MAP

#### Power × Interest Grid

Classify each stakeholder on two axes:

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | 🔴 **Manage Closely** — They can make or kill this. Meet early, meet often, involve in decisions, give them credit. | 🟡 **Keep Satisfied** — They can block without warning. Periodic high-signal updates only. Never surprise them. |
| **Low Power** | 🟢 **Keep Informed** — They amplify or dampen momentum. Regular updates. Invite to demos. Make them feel included. | ⚪ **Monitor** — Light-touch. Available on request. Don't over-invest. |

---

#### The hs- Stakeholder Taxonomy

Beyond quadrant placement, classify each stakeholder by **political role** — because power and interest alone don't tell you *how* to act:

| Role | Signal | What to do |
|---|---|---|
| 🏆 **Champion** | Proactively advocates for the initiative. Extends credibility to others. | Arm with your strongest proof points. Give them early wins to share. |
| 🛑 **Blocker** | Actively opposes, delays, or competes for resources/attention. | Diagnose root cause. Is this values conflict, territorial, or information gap? Each needs a different response. |
| 🧊 **Frozen** | Neither opposing nor supporting. Silent. Treating silence as alignment is the #1 stakeholder mistake. | Investigate. Surface their real concern. Re-engage with something concrete. |
| 🔍 **Gatekeeper** | Controls access to a decision-maker, budget, or process. Not the decision-maker themselves. | Never bypass them. Earn their trust first. |
| 🎭 **Performer** | Says yes in rooms. Acts differently outside of them. | Validate commitment with written artefacts or specific asks — not verbal agreement. |
| 🌊 **Floating Voter** | Undecided. Could be moved by evidence, relationships, or early momentum. | Bring them a win from a Champion early. Proof beats argument. |

> ⚠️ **Hanlon's Razor applied:** Before labelling someone a Blocker,
> never assume malice when misalignment or information gap explains the resistance.
> Most internal blockers are Frozen Voters with incomplete context, not saboteurs.

---

### ③ OUTPUT — TWO DOCUMENTS, TWO JOBS

Every session produces two files. They are not interchangeable.

```
sessions/
  map-[initiative]-[date].md     → The Map. Political reality. Persistent record.
  sprint-[initiative]-[date].md  → The Sprint Card. Weekly execution. Updated every Monday.
```

**The Map** answers: what is the political reality?
**The Sprint Card** answers: what do I do this week, to whom, and what has to land?

Generate the Map first. Generate the Sprint Card immediately after.
Never generate the Sprint Card without the Map. The Map is the source of truth the Sprint Card distils from.

---

#### DOCUMENT A — THE MAP

The Map renders in two layers: a **visual HTML widget** (the grid, communication plan, conflict map, and confidence assessment), followed by the **deep diagnostic** in markdown (political role analysis, risks, key messages).

Never produce the markdown diagnostic without the HTML widget. The widget is the entry point. The diagnostic is the depth behind it.

---

##### MAP WIDGET — RENDER THIS FIRST

Generate an HTML widget with four sections stacked vertically:

**① Power × Interest Grid**
A 2×2 CSS grid. Each quadrant has: a colour-coded dot, a quadrant name, a one-line recommendation in italic, and stakeholder chips stacked inside.

Quadrant colours (light / dark adaptive):
- 🔴 Manage Closely (High Power × High Interest) — red tint background
- 🟡 Keep Satisfied (High Power × Low Interest) — amber tint background
- 🟢 Keep Informed (Low Power × High Interest) — green tint background
- ⚪ Monitor (Low Power × Low Interest) — gray tint background

Each stakeholder chip contains: political role emoji + name (bold) + role title + political role label.
Chip colour maps to political role:
- 🏆 Champion → green chip
- 🛑 Blocker → red chip
- 🧊 Frozen → blue chip
- 🔍 Gatekeeper → purple chip
- 🎭 Performer → coral chip
- 🌊 Floating Voter → gray chip

Each chip is clickable via `sendPrompt('Tell me more about [Name] stakeholder strategy')`.

Include a legend below the grid mapping emoji to political role name and chip colour.

**② Communication Plan Table**
Columns: Stakeholder (name + role subtitle) / Quadrant pill / Frequency / Channel / Key message (italic) / Next action.
Cover Manage Closely and Keep Satisfied stakeholders in full rows.
Keep Informed stakeholders in lighter rows.
Monitor stakeholders omitted from the table.

Quadrant pills: colour-coded to match the grid (red / amber / green).
Key message is the one sentence that has to land — not generic positioning.
Next action is dated and specific.

**③ Conflict Map**
One card per conflict pair. Each card contains:
- Stakeholder A vs Stakeholder B (bold)
- Conflict description (2 sentences)
- Second-order risk block (amber tint): what happens if unresolved by the decision gate
- Resolution block (green tint): the specific structural move the PMM owns

**④ PMM Confidence Assessment**
Six metric cards in a 3-column grid:
Champion coverage / Blocker diagnosis / Frozen voter visibility / Silent function coverage / Comms plan completeness / Overall.
Each card: label (uppercase 10px) + emoji score (🟢 🟡 🔴) + one-line note explaining the score.

---

##### MAP DIAGNOSTIC — RENDER AFTER THE WIDGET

After the HTML widget, output the deep diagnostic in markdown. This is the political analysis the widget summarises.

**Header block:**
```
Initiative: [name]
PMM Owner: [name]
Date: [YYYY-MM-DD]
Primary Decision Gate: [first irreversible action + date]
Confidence Score: 🟢 / 🟡 / 🔴
```

**For each Manage Closely and Keep Satisfied stakeholder:**

**[Name / Role]** · [Political Role emoji + label]
Why they matter: [their specific power over this initiative — 1–2 sentences]
What they care about: [their actual priority — not their job title]
Risk if neglected: [second-order consequence — what breaks downstream, not just what they do]
Key message: [the exact framing they need to hear — not the generic positioning]

**For each Keep Informed stakeholder (condensed):**

**[Name / Role]** · [Political Role emoji + label]
Why they matter: [one sentence]
Amplification potential: [can they move message to higher-power stakeholders?]

**Silent blockers — who isn't in the room:**
For each: **[Function]** — [what they control] — [when to brief] — [who owns outreach]

> ⚠️ The map is not the territory. Update it after every major alignment conversation.
> A 4-week-old stakeholder map is a historical document, not a working tool.

---

#### DOCUMENT B — THE SPRINT CARD

Generated immediately after the Map. Covers Manage Closely and Keep Satisfied only.
Keep Informed stakeholders appear in the Week Summary table only.
Five fields per card. No exceptions. No paragraphs.

---

#### ⚡ COMMS SPRINT CARDS — [Initiative Name]

**Week of:** [Monday date]
**PMM:** [name]
**Decision gate:** [date + what it is]
**Cards this week:** [n] ([x] × Manage Closely, [y] × Keep Satisfied)
**Last updated:** [YYYY-MM-DD]

---

##### 🔴 MANAGE CLOSELY

---

**[Political Role emoji] [Name] — [Role]**

📅 **Next touchpoint:** [date · format]
_(Execution note: the specific thing that cannot be allowed to slip — channel, format, or timing)_

📝 **Send before the touchpoint:**
[Specific artefact — name, format, what it must contain. Not "an update." Not "a summary."]
_[Prep time estimate. Send by deadline.]_

🎯 **What you need from them, by when:**
[Explicit ask. Named deadline. What constitutes an acceptable response vs. silence.]
_[What to do if they don't respond by the deadline.]_

🗣️ **The one sentence that has to land:**
"[The actual line — not the positioning. The thing they need to hear in their frame, not yours.]"
_(If they push back: "[The one response that holds the frame without escalating.])_

🚨 **Watch for:**
[The specific behavioural signal that means they've shifted quadrant or political role.]
→ [What to do immediately if that signal fires.]

---

##### 🟡 KEEP SATISFIED

[Same five-field format]

---

##### 📋 WEEK SUMMARY

| Stakeholder | Send by | Need back by | Status |
|---|---|---|---|
| [Name] | [date — artefact name] | [date — what you need] | ⬜ Not started |

Keep Informed stakeholders: [Name / Role / this week's action / channel] in a single line each.

---

##### 🔁 NEXT SESSION CHECK-IN

Answer these before updating next week's cards:

1. [Per Manage Closely stakeholder: did the Watch For signal fire? Yes/No. If yes — what happened?]
2. [Any stakeholder whose quadrant or political role has shifted? Update the Map document.]
3. [Any new silent blocker surfaced this week? Add to the Map. Build a card for next week.]
4. [Which card held? What does that tell you about this stakeholder?]
5. [Which card broke down? Why? What changes in the card format next week?]

> Confirmed Watch For patterns → log to `knowledge/` with initiative type tag.
> Three confirmations of the same pattern → promote to rule in `knowledge/INDEX.md`.

---

## Outputs

- **Files written:** Two files to `sessions/`: map-[initiative]-[date].md + sprint-[initiative]-[date].md
- **Chat output format:** HTML widget (Power × Interest grid + Communication Plan + Conflict Map + Confidence Assessment), followed by markdown diagnostic
- **External side effects:** n.v.t.

---

## Verification

- Inversion check run: named who could sink this from inside (or gap explicitly flagged)
- Political role assigned: every stakeholder has a role beyond quadrant placement
- Map widget rendered: HTML grid + communication table + conflict map + confidence cards before markdown
- Grid populated: every stakeholder placed in a quadrant with chip + political role
- Comms plan table: every Manage Closely + Keep Satisfied has key message + next action
- Conflict map: every conflict has second-order risk block + resolution block
- Confidence cards: all six dimensions scored with one-line note
- Sprint Card generated: both documents exist as separate files

---

## Do Not Use For

- **hs-product-marketing-context** — when the task is defining ICP or positioning (not stakeholder alignment)
- **hs-gaccs-brief** — when building the communications brief; use this skill first, then GACCS for messaging content
- **hs-pre-mortem** — when stress-testing a plan; pre-mortem runs before stakeholder mapping, not after
- **go-to-market-strategy** — when designing GTM channels; stakeholder map informs GTM strategy, not vice versa

---

## Commands

### /map [initiative name or one-line description]
Build the full stakeholder map for an initiative. Runs intake → inversion check → quadrant placement → conflict map → silent blocker scan → confidence assessment → output. Produces the HTML widget + markdown diagnostic, saved to `sessions/map-[initiative]-[date].md`.

```
/map [initiative name]
```

### /sprint [initiative name]
Generate weekly Sprint Cards for an active initiative. Reads the existing map from `sessions/`. Produces one five-field card per Manage Closely and Keep Satisfied stakeholder, a Week Summary table, and the Next Session Check-In block. Must be run after `/map`.

```
/sprint [initiative name]
```

### /deep-dive [name] — [initiative]
Full diagnostic for a single stakeholder: why they matter, what they care about, risk if neglected, the one sentence that has to land, channel rules, Watch For signals, and this week's action.

```
/deep-dive [name] — [initiative]
```

### /update [initiative] — [what changed]
Update the map after an alignment conversation. Takes a brief on what changed. Updates quadrant placement, political role, or conflict status. Saves a new versioned map.

```
/update [initiative] — [what changed]
```

### /check [initiative]
Weekly map health check. Flags stakeholders silent for 7+ days, Watch For signals that may have fired, conflicts approaching the decision gate unresolved, and Sprint Cards not updated in 10+ days.

```
/check [initiative]
```

---

## Operating Rules (Iron Rules)

- **Silence is not alignment.** Any stakeholder who has not explicitly engaged is Frozen until proven otherwise.
- **The map is not the territory.** Update the Map after every major alignment conversation. A 4-week-old map is a historical document.
- **Name the Performers.** Verbal yes with no follow-through is the most common stakeholder failure mode. Written commitment or it didn't happen.
- **Second-order before action.** Before every communication decision: ask "and then what?" once.
- **Inversion before confidence.** Before declaring the landscape safe: who could sink this, and how?
- **Conflict without resolution is just documentation.** Assign a resolution owner and a date. Unresolved conflicts compound.
- **Gatekeepers are not blockers.** Bypassing a Gatekeeper converts them into one.
- **The Sprint Card is a weekly tool.** If it hasn't been updated in 10 days, it's wrong.
- **Watch For signals are hypotheses.** Confirm them. Log them. Three confirmations makes a rule.
- **Five fields. No exceptions.** A Sprint Card with six fields is an analysis document pretending to be an action tool.

---

## Quality Gate

Runs after both documents are generated. Flags before delivering either.

| Check | Standard | Pass = |
|---|---|---|
| Inversion check run | Named who could sink this from inside | Yes — or gap explicitly flagged |
| Political role assigned | Every stakeholder has a role beyond quadrant placement | Yes |
| Map: Widget rendered | HTML widget generated before markdown diagnostic | Yes |
| Map: Grid populated | Every stakeholder placed in a quadrant with chip + political role | Yes |
| Map: Comms plan table | Every Manage Closely + Keep Satisfied has key message + next action | Yes |
| Map: Conflict map | Every conflict has second-order risk block + resolution block | Yes |
| Map: Confidence cards | All six dimensions scored with one-line note | Yes |
| Sprint: Five fields only | No card has more than five fields. No paragraphs. | Yes |
| Sprint: Execution notes | Every touchpoint field has a parenthetical that names what cannot slip | Yes |
| Sprint: Explicit asks | Every card names what's needed, by when, and what to do if no response | Yes |
| Sprint: Watch For | Every Manage Closely card has a specific behavioural signal + immediate action | Yes |
| Sprint: Next Session block | Answers are stakeholder-specific — not generic reflection questions | Yes |
| Both documents generated | Map and Sprint Card exist as separate files | Yes |
| PMM context integration | Map cross-referenced with ICP, GTM motion, positioning if context loaded | Yes |

**On flag:** Surface the failure. Do not deliver incomplete output.
**On pass:** Deliver both documents. Log `QG: Pass` in `sessions/log.md`.

---

## Self-Improvement Loop

### Before every session:
1. Read `knowledge/INDEX.md` — load confirmed rules by initiative type
2. Check prior stakeholder maps in `sessions/` — are there patterns?
3. Check `knowledge/stakeholder/patterns.md` if it exists
4. Load PMM context (Block ⓪)

### After every session:

1. Extract Watch For patterns → `knowledge/stakeholder/[initiative-type].md`
2. If same pattern confirmed 3+ times across sessions → promote to rule
3. Log session → `sessions/log.md`

---

### Learning Close — Run at End of Every Session

At the end of every session, before closing:

> "Three questions before we close:
> 1. Which stakeholder landed in a different place than you expected — and why?
> 2. Which card are you most confident will hold through the week? What made it easy?
> 3. Which card do you most doubt — and what's the specific thing you'll let slip first?"

Extract the answer to Q3. It is almost always a Watch For pattern in disguise.
Log it to `knowledge/` with initiative type tag.
If confirmed in a future session: promote to rule.

---

## INITIATIVE TYPE MODIFIERS

Apply before mapping.

| Initiative Type | Dominant Quadrant Risk | Watch especially for |
|---|---|---|
| **Product Launch** | Manage Closely → Sales leadership, Product | Sales Performers — verbal yes, no enablement follow-through |
| **Pricing Change** | Keep Satisfied → Finance, Legal, CS leadership | Finance as silent blocker; CS as frozen voter with high blast radius |
| **New Channel** | Keep Informed → Demand Gen, RevOps | Attribution conflict between channel owners; RevOps as gatekeeper |
| **GTM Pivot** | Manage Closely → CEO, Sales VP, RevOps | Performers at VP level; frozen ICs who depend on old motion |
| **New Market Entry** | Manage Closely → Regional leads, Legal | Gatekeepers who control local access; frozen voters who own home market |
| **Campaign Launch** | Keep Informed → Content, Design, Sales | Silent blockers in Legal/Brand; Floating Voters in Sales field |
| **Internal Programme** | Manage Closely → HR, Finance, Ops | Frozen function heads who see this as additional overhead |

---

## SECTION METADATA

Every Map file saved to `sessions/` carries:

```
_Initiative: [name]_
_Type: [initiative type]_
_Session date: YYYY-MM-DD_
_PMM owner: [name]_
_Primary decision gate: [date]_
_Stakeholder count: [n]_
_Manage Closely: [n]_
_Blockers identified: [n]_
_Frozen voters: [n]_
_Silent functions flagged: [n]_
_Confidence score: 🟢 / 🟡 / 🔴_
_QG: Pass / Fail_
_Version: [n]_
```

Every Sprint Card file saved to `sessions/` carries:

```
_Initiative: [name]_
_Sprint week: YYYY-MM-DD_
_Cards: [n]_
_Manage Closely cards: [n]_
_Keep Satisfied cards: [n]_
_Watch For signals fired last week: [n]_
_Stakeholder role changes since last sprint: [n]_
_Version: [n]_
```

---

## CHANGELOG

### v2.2.0 — 2026-06-11
Spec compliance update: added Trigger, Inputs, Pre-flight, Outputs, Verification, Do Not Use For sections to meet SKILL-SPEC v2.0.0.

Structural changes:
- Trigger section added with explicit When / Not for / Examples
- Inputs section added with Args / Defaults / Context keys
- Pre-flight section structure formalized
- Outputs section clarified (two documents, file write targets)
- Verification section specified (checklist format)
- Do Not Use For section added (routing to related skills)
- Commands block formalized (/map, /sprint, /deep-dive, /update, /check)

No changes to core stakeholder mapping methodology or output architecture (v2.1.0 visual-first approach retained).

### v2.1.0 — 2026-04-17
Visual-first output architecture introduced.
- Document A now renders an HTML widget before the markdown diagnostic
- Widget contains: Power × Interest grid with stakeholder chips, Communication Plan table, Conflict Map cards, PMM Confidence Assessment
- Stakeholder chips colour-coded by political role; clickable via sendPrompt
- Conflict Map cards structured with second-order risk block (amber) and resolution block (green)
- Confidence Assessment rendered as six metric cards in a 3-column grid
- Markdown diagnostic retained as the depth layer behind the widget

### v2.0.0 — 2026-04-17
Two-phase output architecture introduced.
- Map and Sprint Card split into two separate session documents
- Sprint Card format: five fields per stakeholder, five fields only
- Watch For observations wired into knowledge/ as primary pattern data source
- Quality Gate expanded to cover both documents

### v1.0.0 — 2026-04-17
Initial build.
