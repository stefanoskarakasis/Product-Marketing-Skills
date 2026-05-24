---
name: hs-pre-mortem
version: 2.0.1
description: >
  A self-improving pre-mortem risk engine for PMMs running cross-functional risk analysis
  on any strategic project. Covers: PRD, product launch, pricing change, new marketing
  channel, GTM pivot, new market entry. Run by a PMM facilitating cross-functional teams.
  Trigger on: "pre-mortem", "risk analysis", "what could go wrong", "stress-test this plan",
  "launch readiness", "pressure-test", "failure modes", "risks before we launch",
  "pre-launch review", "what are we missing", "GTM risk", "pricing risk", "market entry risk",
  or any request to identify, categorise, or mitigate strategic risk before a major move.
---

# hs-pre-mortem — Strategic Risk Engine for PMMs

A PMM-led, cross-functional pre-mortem tool.
Not a checklist. A structured thinking system that forces teams to imagine failure
before it happens — and convert that into action.

Built on Gary Klein's pre-mortem methodology. Sharpened for B2B GTM contexts.
Patched from two live mock sessions. Version 2.0.0.

---

## ⓪ PMM CONTEXT — LOAD FIRST

Before intake, check `.agents/product-marketing-context.md`.

**If it exists — load silently. Extract:**

- `## ICP Prioritisation` → who failure would hurt most, and how
- `## Positioning` → is the strategic narrative coherent with this initiative?
- `## Objections & Anti-Personas` → pre-load as signal for demand-side risks
- `## Revenue Levers` → which lever does this target? Risk lens shifts by lever.
- `## GTM Motion & Growth Loops` → which motion is this dependent on? What breaks if it fails?
- `## Beachhead Segment` → if new market entry, flag tension against current beachhead
- `## Marketing Advantages` → are you relying on an advantage that's unproven or weak?
- `## Product Strategy Canvas` → trade-offs accepted hide risks. Read them.

**Confidence awareness:**

If any loaded section is 🔴 Placeholder, flag before intake:
> "⚠️ The [section] in your PMM context is marked Placeholder.
> That's the exact area where pre-mortems surface the worst surprises.
> Flag that assumption now — don't discover it during risk analysis."

**If context file is missing:**

Surface once, non-blocking:
> "No PMM context found. Run `hs-product-marketing-context BUILD` to make this significantly
> sharper. Continuing — but expect more assumption-based risks than evidence-based ones."

---

## RELATED SKILLS

Cross-reference these when building or following up on a pre-mortem:

- **hs-product-marketing-context** → source of ICP, positioning, GTM motion, advantages
- **hs-gaccs-brief** → messaging or campaign risk surfaced → route here
- **hs-competitive-battlecard** → competitive displacement is a Tiger → route here
- **hs-brainstorm-okrs** → success metric ambiguity or KR design gap → route here
- **experiment-doc-builder** → Elephant needs validation before launch → route here
- **hs-gtm-launch-planner** → launch sequencing or tier readiness is a Tiger → route here
- **hs-ci-stakeholder-briefing** → competitive response risk at leadership level → route here

---

## ① INTAKE — ESTABLISH SCOPE BEFORE ANALYSIS

> ⚠️ Most users start with the wrong frame. Always run this first.
> Never generate risks before completing intake and reflecting back.

Ask in one conversational message:

> "Before I build the risk map, a few things I need to be sharp on:
>
> 1. **What type of initiative is this?**
>    (Product launch / Pricing change / New channel / GTM pivot / New market entry / Other)
>
> 2. **What does success look like in 90 days?**
>    Be specific — a number, a behaviour, a deal closed.
>
> 3. **What are the decision gates — not just the launch date?**
>    There's often more than one point of no return. Name the announcement date,
>    but also: when does resource get committed? When does the first public signal go out?
>    When does reversal become expensive?
>
> 4. **Who's in the room for this pre-mortem?**
>    (PMM only / PMM + Product / full GTM / PMM + Finance / other)
>    Note: missing Sales or CS will be flagged as a structural blind spot.
>
> 5. **Do you have a plan document?**
>    Drop it. If not, give me 3–4 sentences on what you're doing and why."

**If they share a document:**

Read it fully. Extract core assumptions, timelines, and success metrics.
Do not start risk analysis until you understand the plan.

**If they describe verbally:**

Reflect back in 3 sentences before proceeding.
Ask them to correct anything wrong.
This is not polish — it's assumption-surfacing.

---

### THESIS INTERROGATION — ALWAYS RUN AFTER REFLECT-BACK

After reflecting back the initiative, ask one additional question:

> "One more: **what would have to be true for this initiative to be the wrong move entirely?**
> Not what could go wrong in execution — what would have to be true about the market,
> the customer, or the business for this to be a mistake regardless of how well you execute?"

**If the team cannot answer clearly:**

> "⚠️ If the team can't articulate what would make this initiative wrong,
> the thesis is assumed — not validated. That's where the deepest risks live.
> We'll surface them in the failure frame."

This question surfaces the gap between the stated rationale and the actual thesis.
Most initiatives have a thinner thesis than they present.
The real reason for the initiative is often executive momentum, opportunistic signal,
or competitive anxiety — not validated market demand.

---

### FAILURE SCENARIO CALIBRATION — ALWAYS RUN BEFORE WRITING THE SCENARIO

Before writing the failure scenario, ask:

> "What would failure unambiguously look like to your CEO or CRO?
> Not a bad quarter — the specific outcome that would make them say
> 'we shouldn't have done this.'"

Use their answer to anchor the failure scenario.
Do not invent a failure scenario without this calibration.
A scenario that doesn't match their definition of failure
will not shift the team out of defensive optimism.

---

## ② SCENARIO FRAME — SET THE FAILURE MINDSET

Before generating risks, run this framing exercise:

> "Imagine it's [primary decision gate + 60 days]. The initiative has failed.
>
> Not dramatically — no one got fired, no press coverage.
> Just: [insert calibrated failure scenario from intake].
>
> The team is in a retrospective. One question is on the table:
> **'What did we know — or should have known — that we ignored?'**
>
> That's what we're surfacing right now, while there's still time to act."

> ⚠️ This reframe is not optional. It shifts teams from defensive optimism to honest
> diagnosis. Do not skip it. Do not rush through it.

**Watch for the tell:**

When a PMM or product lead says "honestly" before answering the failure frame,
the next sentence is almost always a Tiger that was being avoided — not an Elephant.

File it as a Tiger immediately.
Avoidance of a known risk is not uncertainty — it's a decision not to act.

---

## ③ RISK GENERATION — FIVE LENSES

Generate risks across five lenses.
Each lens maps to a cross-functional domain.
Tag every risk with its lens — untagged risks don't get owned.

Apply initiative type modifiers from Section ⑩ before generating.

For **New Market Entry**: run the local knowledge audit in Section ⑩
before generating Lens 1 and Lens 2 risks.

---

### 🔍 LENS 1: Market & Customer
*Does the market actually want this? Will the right customers find it and adopt it?*

- Demand assumptions — who wants this and why — validated or assumed?
- Validation signal quality — is the evidence robust, or is it a single data point being over-read?
- ICP misfit — is this built for who you think it's built for?
- ICP translation — if new market, are buyer triggers, personas, and cycles the same?
- Timing risk — too early, too late, or competing with a market event?
- Customer awareness gap — do they know they have this problem?
- Willingness to pay — is the price anchored to value or competitive parity?
- Regulatory or compliance constraints on the buyer side

---

### 🔍 LENS 2: Competitive & Strategic
*Does this make you stronger relative to alternatives — or does it expose you?*

- Competitive response — what does the primary competitor do when this launches?
- Local competitive landscape — for new markets, who is already there and how strong?
- Positioning drift — does this confuse the existing narrative?
- Cannibalization — does this hurt an existing revenue line?
- Me-too risk — matching a competitor with no differentiated wedge?
- Opportunity cost — what are you NOT doing to do this?
- Thesis validity — is this the right strategic move, or rationalised momentum?

---

### 🔍 LENS 3: GTM & Execution
*Can the go-to-market motion actually deliver this?*

- Sales readiness — do sellers understand and believe the pitch?
- Sales belief — would sellers bring this up unprompted in a prospect call?
- Channel fit — is the launch channel right for this ICP?
- Channel-team fit — is the team structurally equipped for this channel? (language, network, knowledge)
- Enablement gap — does CS / Sales / Partner have what they need?
- Message-market fit — sharp enough to convert, not just resonate?
- Activation path — for adoption goals: what is the specific behaviour change sequence?
- Launch timeline — is the sequence logical? What breaks if one thing slips?
- Pipeline pre-seeding — for event/conference launches: is there pipeline to accelerate, or is announcement expected to create it?
- Pricing & packaging clarity — easy to sell and buy?

---

### 🔍 LENS 4: Organisational & Stakeholder
*Is the internal machine aligned enough to execute this?*

- Executive alignment — actually committed, or just not vetoing?
- Resource commitment — budget and headcount explicitly approved, or assumed?
- Resource contention — what else is competing for the same people and budget?
- Cross-functional handoff gaps — who is assuming someone else owns what?
- Change management — how are customers, partners, and internal teams being prepared?
- Decision authority — who can kill this? Have they been consulted and committed?
- Decision trigger — defined go/no-go condition with a date, or drifting?
- Political dynamics — is this initiative driven by validated strategy, or executive momentum?

---

### 🔍 LENS 5: Data & Measurement
*Can you tell if it worked — and fast enough to course-correct?*

- Success metric ambiguity — KPI defined, owned, and instrumented before launch?
- Leading indicator gap — what signal tells you in week 2–3 whether it's working?
- Lagging metric trap — if the only metric is a 90-day number, there's no course-correction window
- Attribution risk — can you isolate the impact of this initiative?
- Failure mode framework — can you distinguish fit failure from motion failure from timing failure?
- Feedback loop speed — how long before real signal arrives? Is that too long to act?

---

## ④ RISK CLASSIFICATION — TIGERS / PAPER TIGERS / ELEPHANTS

Classify each generated risk into one of three categories.

---

### 🐯 Tigers — Real risks. Act on them.

- Based on evidence, logic, or direct experience
- Left unaddressed, they derail the initiative
- Every Tiger gets a mitigation action and a named owner

---

### 📄 Paper Tigers — Acknowledged, but not acted on.

- Surfaced because someone in the room will raise them
- Low probability or low impact on actual outcomes
- Document to clear the air — not to drive action
- Explain *why* they don't warrant resource investment

> ⚠️ **Paper Tiger integrity rule:**
> A PMM's confidence in their existing customer relationship, brand strength,
> or internal alignment is never sufficient evidence to classify a commercial,
> competitive, or perception risk as a Paper Tiger.
> Familiarity is not validation. Confidence is not data.
> If a risk is being downgraded because it *feels* unlikely — push back.

---

### 🐘 Elephants — Unspoken. Needs investigation.

- The thing nobody is talking about
- Not confirmed as a real problem — but not dismissed either
- Requires an experiment, a conversation, or a data pull before launch

> 🔴 **Elephant upgrade rule:**
> If the team has access to the evidence needed to investigate an Elephant
> and has chosen not to gather it — that is avoidance, not uncertainty.
> Upgrade it to a Tiger immediately.
> Avoidance of a known unknown is a known risk.

> 🔴 **Investigator rule:**
> Every Elephant must have a named investigator and a due date
> at the moment of classification — not at the end of the session.
> An Elephant with no investigator automatically becomes a Tiger.

**Elephant classification format (enforce at point of classification):**

```
🐘 [Risk name]
What needs to be found out: [specific question]
Investigator:              [name / function]
Due date:                  [specific date]
If unresolved by due date: becomes 🚨 Tiger
```

**PMM facilitation prompt:**

> "What's the thing you're personally most worried about
> that nobody else has said out loud yet?"

That question surfaces Elephants faster than any framework.

---

## ⑤ TIGER TRIAGE — URGENCY CLASSIFICATION

For every Tiger, assign an urgency level:

| Level | Meaning | Action required |
|---|---|---|
| 🚨 **Launch-Blocking** | Must be resolved before launch. Unresolved = recommend delay. | Full mitigation plan |
| ⚡ **Fast-Follow** | Must be resolved within 30 days post-launch | Owner + due date now |
| 📊 **Track** | Monitor post-launch. Act if it materialises. | Threshold metric |

**On Launch-Blocking Tigers with 🔴 mitigation confidence:**

State it without softening:
> "⚠️ This Tiger has no credible mitigation assigned.
> Launching without resolving it is a strategic bet, not a plan.
> This is a hard launch blocker until a credible, owned mitigation exists."

**QG escalation rule:**

If any Launch-Blocking Tiger carries 🔴 mitigation confidence,
the PMM Recommendation cannot be 🟢 Go.
It must be 🟡 Conditional Go or 🔴 No-Go.
A 🔴 mitigation score on a launch blocker is not a detail — it is the recommendation.

---

## ⑥ ACTION PLANS — LAUNCH-BLOCKING TIGERS ONLY

For each Launch-Blocking Tiger, produce this format with explicit line breaks:

```
### 🚨 Tiger: [Risk name]

**What breaks:**
[One clear consequence per line. Not bundled prose.]
[If multiple consequences, list each on a new line.]

**Why it's real:**
[Evidence or direct reasoning — not assertion.]
[Quote the PMM if they named it directly.]

**Mitigation:**
[A deliverable, a decision, or a conversation with a named output.]
[Not "look into this." Concrete and completable.]

**Owner:**
[Function + specific person if known]

**Due date:**
[Specific date — or "before [named milestone]"]

**Confidence in mitigation:**
🟢 Credible — specific, owned, no external dependencies
🟡 Partial — plan exists but has a dependency or timing risk
🔴 Weak — vague, unowned, or not achievable before launch
```

If confidence is 🔴:
> "⚠️ The mitigation for [Tiger name] is weak.
> This is an unresolved launch blocker.
> The PMM Recommendation will reflect this."

---

## ⑦ OUTPUT STRUCTURE

Deliver as formatted markdown.
Emoji callouts are navigational — not decorative.
Every section break represents a topic shift.
Do not bundle multiple topics into a single paragraph.
Line breaks between every named field in action plans.

```markdown
## 🔬 Pre-Mortem: [Initiative Name]

**Type:** [Initiative type]

**Announcement date:** [Date]

**Key decision gates:**
- [Gate 1: description + date]
- [Gate 2: description + date]

**PMM facilitator:** [Name]

**Session date:** [Date]

---

### 💀 The Failure Scenario

[2–3 sentences. Specific metric. Named consequence. Named audience.
Anchored to the CEO/CRO definition of failure from intake.
Not "things went badly" — a concrete picture of what bad looks like.]

---

### 🐯 Tigers (Real Risks)

| # | Risk | Lens | Urgency | One-line summary |
|---|---|---|---|---|
| R-01 | [Name] | [Lens] | 🚨 / ⚡ / 📊 | [One sentence] |

---

### 📄 Paper Tigers (Acknowledged — Not Acted On)

| # | Risk | Why it's not a blocking risk |
|---|---|---|
| PT-01 | [Name] | [Specific reason] |

---

### 🐘 Elephants (Unspoken — Needs Investigation)

| # | Risk | What to find out | Investigator | Due date | If unresolved |
|---|---|---|---|---|---|
| E-01 | [Name] | [Question] | [Owner] | [Date] | 🚨 Tiger |

---

### 🚨 Action Plans — Launch-Blocking Tigers

[Full action plan blocks — one per Tiger, Section ⑥ format]

---

### ⚡ Fast-Follow Watch List

| Tiger | Owner | Due date | Threshold metric |
|---|---|---|---|
| [Name] | [Owner] | [Date] | [What triggers action] |

---

### 📋 PMM Recommendation

[🟢 Go / 🟡 Conditional Go / 🔴 No-Go]

[Explicit rationale.]

[If Conditional Go: the one condition, and the date it expires.]

[If No-Go: what specifically changes the recommendation.]

[If politically complex: reframe as a validation sprint — see Section ⑧.]

---

### 📊 Pre-Mortem Confidence Score

Overall readiness: 🟢 High / 🟡 Medium / 🔴 Low

**What would move the score up:**
[One specific action — not a general direction]
```

---

## ⑧ PMM RECOMMENDATION — NEVER SKIP THIS

A pre-mortem without a recommendation is just a worry list.

The PMM has the clearest view across market, message, and motion.
The recommendation must be explicit — and it must be honest.

---

**🟢 Go**

No Launch-Blocking Tigers unresolved.

Fast-follows owned and dated.

---

**🟡 Conditional Go**

One or more Launch-Blocking Tigers with a credible mitigation in progress.

State the condition:
> "Go — conditional on [specific mitigation] confirmed by [date].
> If not confirmed, this reverts to 🔴 No-Go automatically."

---

**🔴 No-Go**

One or more Launch-Blocking Tigers with no credible mitigation.

State it without softening:
> "Not ready. The risk to [revenue / reputation / positioning]
> outweighs the benefit of launching on schedule.
> Recommend delay until [specific condition] is resolved."

---

### Delivering a No-Go to Leadership

A No-Go in a politically complex situation — where the initiative
has executive momentum, a CEO directive, or a conference commitment —
is not easy to deliver.

The pre-mortem is the cover, not the obstacle.

Frame it:
> "We ran a pre-mortem. The recommendation is a [X]-day validation sprint
> before full launch — because that's how we make [initiative name] work,
> not how we slow it down.
>
> Here's what we validate. Here's the go/no-go condition at the end of the sprint.
> Here's what we announce now vs. what we hold."

This reframes delay as diligence.
It gives leadership a defined decision point — which is what they actually need.
And it protects the PMM from being the person who said no to growth.

---

## ⑨ SELF-IMPROVEMENT LOOP

### Before every session:

1. Read `knowledge/INDEX.md` — route to relevant initiative type folder
2. Scan `hypotheses/active.md` — check if any hypothesis can be tested today
3. Check `sessions/log.md` — pull prior context on this company or initiative
4. Load PMM context (Block ⓪)

### After every session:

1. Extract 1–3 risk patterns → `knowledge/[initiative-type]/knowledge.md`
2. First time a risk appears → `hypotheses/active.md`
3. Risk confirmed 3+ sessions → flag for promotion to `knowledge/[type]/rules.md`
4. Tiger dismissed as Paper Tiger that later proved real → `craft/false-dismissals.md`
5. Log session → `sessions/log.md`

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER

Pattern observed:
[What I noticed across this session]

Proposed update:
[Specific change — exact wording of what would be added or changed]

Location:
[File path]

Awaiting your approval before encoding.
```

> ⚠️ Never encode without explicit user approval.

---

### Learning Close — Run at End of Every Session

**Step 1 — Unstructured prompt first. Always.**

> "Before I ask you three things — is there anything that came up today
> that you want to say out loud before we close?
> Anything the session surfaced that you haven't voiced yet?"

Wait for the answer. Do not rush to the structured questions.
The most strategically important insight of the session usually surfaces here.

**Step 2 — Three structured questions:**

> "1. Was there a risk that surprised you — one you hadn't considered before today?
>
> 2. Was there a Tiger I flagged that you think is actually a Paper Tiger?
>
> 3. Was there an Elephant the team already knew about but hadn't named?"

**Step 3 — Propose encodes. Always explicitly:**

> "Here's what I'm proposing to add to the knowledge base:
> [List proposed Self-Improvement Triggers]
> Confirm before I encode?"

---

## OPERATING RULES

- **Load PMM context first. Always.** What's in that file changes which risks are real.
- **One mode: facilitator mindset.** Cross-functional session tool, not a solo audit.
- **Thesis interrogation before scenario frame.** Ask what would have to be true for this to be wrong.
- **Calibrate the failure scenario before writing it.** Anchor to the CEO/CRO definition of failure — not a constructed one.
- **Failure scenario before risk generation.** Never generate risks before the team has sat in the failure frame.
- **No risk without a lens.** Every risk tagged. Untagged risks don't get owned.
- **No Tiger without a mitigation.** A Tiger with no action plan is anxiety dressed up as analysis.
- **Launch-Blocking means launch-blocking.** Timeline pressure never reclassifies a blocker as Fast-Follow.
- **PMM recommendation is not optional.** Output without a go/no-go is incomplete.
- **Elephants assigned at classification — not at end of session.** Unassigned = Tiger. No exceptions.
- **Avoidance upgrades Elephants to Tigers.** Evidence accessible and team chose not to gather it = Tiger.
- **Confidence scores on mitigations.** A 🔴 on a launch blocker = the recommendation, not a footnote.
- **Paper Tiger integrity.** Familiarity and confidence are not evidence. Push back if a risk is downgraded by feel.
- **Compound, don't repeat.** Check `knowledge/` before generating. Don't resurface resolved risks.
- **No-Go is not resistance.** Frame delay as a validation sprint with a defined decision gate.

---

## QUALITY GATE

Runs after output generation. Flags before delivering — never after.

| Check | Standard | Pass = |
|---|---|---|
| Thesis interrogation | Team answered "what would have to be true for this to be wrong?" | Yes — or gap explicitly flagged |
| Failure scenario calibration | Scenario anchored to CEO/CRO definition of failure | Yes |
| Failure scenario specificity | Named metric, behaviour, or outcome — not "things went badly" | Yes |
| Decision gates | Multiple gates named, not just announcement date | Yes |
| Risk coverage | All five lenses represented | At least one risk per lens |
| Tiger credibility | Each Tiger backed by evidence or reasoning — not worry | Yes, with source stated |
| Paper Tiger integrity | Any Paper Tiger downgraded by feel rather than evidence? | No — pushback if yes |
| Elephant format | Every Elephant has: what to find out / investigator / due date / upgrade condition | Yes — at point of classification |
| Elephant upgrade check | Any Elephant where evidence accessible and team chose not to gather it? | Upgraded to Tiger |
| Launch-Blocking Tigers | Each has full action plan, Section ⑥ format, with line breaks | Yes |
| Mitigation confidence | Any 🔴 confidence flagged and escalated to PMM Recommendation | Yes |
| QG escalation | Any 🔴 mitigation on launch blocker → Recommendation is not 🟢 Go | Enforced |
| PMM Recommendation | Explicit Go / Conditional Go / No-Go with rationale | Yes |
| No-Go framing | If No-Go, reframe as validation sprint for leadership delivery | Yes |
| Confidence score | Score included with one specific uplift action | Yes |
| Output formatting | Line breaks between What breaks / Why it's real / Mitigation / Owner / Date | Yes |
| PMM context integration | Risks cross-referenced with ICP, positioning, GTM motion if context loaded | Yes |

**On flag:** Surface the failure. Do not deliver incomplete output.

**On pass:** Deliver output. Log `QG: Pass` in `sessions/log.md`.

---

## ⑩ INITIATIVE TYPE MODIFIERS

Apply before risk generation.

| Initiative Type | Dominant Lenses | Watch especially for |
|---|---|---|
| **Product Launch** | Market & Customer / GTM & Execution | ICP misfit, message-market fit, sales belief gap, activation path, AI accuracy claims, conference pre-seeding |
| **Pricing Change** | Market & Customer / Organisational | Churn trigger, sales confidence gap, anchor disruption, existing customer framing |
| **New Marketing Channel** | GTM & Execution / Data & Measurement | Attribution gap, CAC assumptions, channel-ICP fit, leading indicator definition |
| **GTM Pivot** | Organisational / Competitive & Strategic | Sales compensation design, internal trust, resource reallocation, positioning drift, revenue disruption in transition. Note: Lens 4 is the primary lens for GTM pivots — most failures are internal, not external. Run it first. |
| **New Market Entry** | Market & Customer / Competitive & Strategic | Regulatory gaps, ICP translation, local competitive landscape, brand zero-base, team structural fit |

---

### New Market Entry — Additional Checks (run before Lens 1 + 2)

**Local knowledge audit:**

> "Do you have anyone in this session with on-the-ground knowledge of [target market]?
> A customer, a partner, a local hire, a validated market study?"

If no:
> "⚠️ All Market & Customer and Competitive & Strategic risks for this market entry
> are assumption-based — not evidence-based.
> Every risk in those two lenses is flagged 🔴 confidence until local validation exists."

**Also check:**

- Does the Beachhead Segment in PMM context conflict with this new market?
- Are ICP assumptions being translated or assumed to carry over unchanged?
- What is the full regulatory and compliance surface area in this market?
- Is there a local competitive dynamic that doesn't exist in the home market?
- Is the GTM team structurally equipped — language, network, local knowledge?
- Is there a defined beachhead — one city/region, one subsegment, one size band — before outbound begins?
- Is there a defined Country Manager decision trigger with a go/no-go date?

---

### GTM Pivot — Additional Checks (run Lens 4 first)

- Has Sales leadership been briefed before the announcement — not at it?
- Is there a compensation model defined for any new motion before go-live?
- Is there a playbook for how Sales uses the new motion in live deals?
- Has the CEO mandate been translated into explicit resource commitment?
- Is there a defined failure condition — metric, threshold, date — for the new motion?
- What is the opportunity cost of this pivot on the existing motion that is working?
- Is the announcement date giving Sales enough time to process and adapt, or is it creating blindsided resistance?

---

### Product Launch — Additional Checks

- Is there a leading indicator defined for adoption — not just a 90-day lagging metric?
- If AI-powered: has the model been validated on customer data, not just internal data?
- Is there an activation path — a specific behaviour change sequence — for adoption goals?
- Would Sales bring this up unprompted in a prospect call? Or only when asked?
- Has a conference or event announcement been pre-seeded with pipeline — or is the announcement expected to create pipeline?

---

## SECTION METADATA

Every pre-mortem output saved to `sessions/` carries:

```
_Initiative: [name]_
_Type: [initiative type]_
_Session date: YYYY-MM-DD_
_PMM facilitator: [name]_
_Announcement date: YYYY-MM-DD_
_Key decision gates: [list]_
_Confidence score: 🟢 / 🟡 / 🔴_
_QG: Pass / Fail_
_Version: N_
```

---

## INTEGRATION MAP

| Skill | When to cross-reference |
|---|---|
| `hs-product-marketing-context` | Always — read before intake |
| `hs-gaccs-brief` | Tiger: messaging or campaign risk surfaced |
| `hs-competitive-battlecard` | Tiger: competitive displacement or response risk |
| `hs-brainstorm-okrs` | Tiger: success metric ambiguity or KR design gap |
| `experiment-doc-builder` | Elephant: assumption needs validation before launch |
| `hs-gtm-launch-planner` | Tiger: launch sequencing or tier readiness risk |
| `hs-ci-stakeholder-briefing` | Tiger: competitive response risk at leadership level |

---

## CHANGELOG

### v2.0.1 — 2026-04-07
Patch from Session 3 (GTM pivot mock):
- GTM Pivot modifier updated: Lens 4 (Organisational) promoted to primary lens
- GTM Pivot additional checks block added to Section ⑩
- Observation encoded: GTM pivot failures are primarily internal — commission model,
  Sales trust, resource allocation — not competitive or market-side

### v2.0.0 — 2026-04-07
Patched from two mock sessions (product launch + new market entry). 13 gaps addressed.

**Structural patches:**
- Gap 1 → Intake Q3 split into announcement date + named decision gates
- Gap 2 → Failure scenario calibration step added (CEO/CRO definition anchors the scenario)
- Gap 6 → Accountability block added to output structure
- Gap 8 → Thesis interrogation step added to intake
- Gap 9 → No-Go leadership reframe block added to Section ⑧
- Gap 11 → New market entry local knowledge audit added to Section ⑩
- Gap 12 → Failure scenario calibration formalised as mandatory intake step

**Classification logic patches:**
- Gap 4 → Paper Tiger integrity rule added
- Gap 7 → QG escalation rule: 🔴 mitigation on launch blocker = recommendation
- Gap 10 → Elephant upgrade rule: avoidance = Tiger, not Elephant
- Gap 13 → Elephant format enforced at classification point, not end of session

**Craft patches:**
- Gap 3 → Lens 4 expanded with resource commitment and decision trigger probes
- Gap 5 → Learning Close restructured: unstructured prompt runs before three structured questions

### v1.0.0 — 2026-04-07
Initial build.
