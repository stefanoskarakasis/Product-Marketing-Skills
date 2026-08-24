---
name: positioning-messaging
version: 2.3.0
description: >
  Use for positioning statement, messaging hierarchy, homepage copy, persona cards,
  messaging audit, value prop, or elevator pitch. Trigger when user says "we sound
  like everyone else," "messaging is not landing," or mentions April Dunford or
  Obviously Awesome. Also trigger when user pastes copy for review.
  Runs full Dunford sequence across BUILD / AUDIT / FLETCH / SALES-ENABLEMENT /
  HOMEPAGE modes. Refuses to generate without named primary persona and 3+
  alternatives including status quo. Blocks output until 7-point verification
  gate passes.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-22
---

## Step 0: Pre-Flight

### Load Context & Guardrails

1. **Load Brain** (REQUIRED)
   - Read `/foundation/brain.md`
   - Require: Section 1 (Product Context), Section 2 (ICP), Section 3 (Alternatives & Positioning)
   - If missing → Offer to run product-marketing-context

2. **Load Active Guardrails**
   - If `/context/meta-patterns.md` exists in the user's workspace: if a pattern
     has actually fired 2+ times in prior positioning runs logged there, surface
     it now
   - If it doesn't exist, skip this step silently

---

# positioning-messaging

Built on Dunford's Obviously Awesome framework. Delivers sharp, defensible
positioning through a 6-phase discovery and stress-test process.

---

## Onboarding

> Run this block once at the start of every new session. No output until
> complete. One question at a time. This is the Settings screen — not discovery.

**Step 1 — Check brain:**

````
Does /foundation/brain.md exist?
  YES → Load silently. Note ICP, alternatives, energy state. Proceed.
  NO  → Surface once: "No brain found. You can still run this skill, but output will be less precise. Run product-marketing-context first for sharper results. Continuing."
````

**Step 2 — Select mode:**

Ask: `"What are you trying to accomplish today?"`

Present options (let user pick one — no typing required):

- `[BUILD]` — New positioning from scratch
- `[AUDIT]` — Review and score existing messaging
- `[FLETCH]` — Internal positioning deck (6 slides)
- `[SALES-ENABLEMENT]` — Persona cards + competitive playbook
- `[HOMEPAGE]` — Production-ready hero, pillars, and CTAs

**Step 3 — Confirm persona focus:**

Ask: `"Which persona are we positioning for today?"`

- If brain has ICP: surface it — `"Based on your brain: [ICP]. Is this correct?"`
- If no brain: ask for title, company type, and triggering situation

**Step 4 — Confirm alternatives:**

Ask: `"What are buyers comparing you against?"`

- Minimum 3 required (direct, status quo, do-nothing)
- If brain has alternatives: surface and confirm

**Step 5 — Surface any attached images:**

Parse all attached images before reading user text. Extract claims, flags, and
implied category. Report as: `"Your current materials say: [findings]"`

> After Steps 1–5: state the session setup back to the user in one paragraph.
> Await confirmation. Then proceed to Phase 1.

---

## Trigger

- **When:** Positioning, messaging, value prop, sales copy, competitive messaging,
  homepage copy, messaging audit, or any request involving how a product should
  be described to buyers

- **Not for:** Product specification → use `prd`. Buyer persona building or
  alternatives mapping in isolation → no dedicated skill exists for these yet;
  handle within this skill's own intake instead.

- **Example prompts:**
  - "Build positioning for [product]"
  - "Our messaging sounds like everyone else"
  - "Help me position against [competitor]"
  - "Write our homepage headline and pillars"
  - "Audit this messaging for coherence"
  - "We can't explain what we do to sales"
  - "Is this positioning working?"

---

## Inputs

- **Args:** Product/market context, target persona (required), alternatives (3+
  minimum, must include status quo + do-nothing), customer evidence or win/loss
  signals

- **Defaults:** If no persona named, surface from brain or ask. If fewer than 3
  alternatives, block and ask before proceeding.

- **Context keys:**
  - `/foundation/brain.md` — preferred. Sections 1 (product), 2 (ICP),
    3 (alternatives), 4 (voice) if available

---

## Pre-flight

- Load `/foundation/brain.md` if it exists. Extract ICP, positioning hypothesis,
  competitive alternatives silently.

- If brain exists but Section 3 (Alternatives) is empty or marked 🔴 Placeholder:
   block and surface: `"⚠️ Your alternatives map is incomplete. Complete Section 3
  (Alternatives & Positioning) of your brain via product-marketing-context

- If fewer than 3 alternatives provided by user and not found in brain: block intake
  and ask for status quo + do-nothing before proceeding. Hard stop.

- If no brain found: surface once, non-blocking. Continue.

---

## Steps

> All modes run all 6 phases unless noted. Shortcuts produce weak output.

### Phase 1: Discovery

Run as a conversation. One question at a time. Never generate on the first message.

**Hard floor — all four required before Phase 2:**

- [ ] Product: what it does today (not roadmap)
- [ ] Buyer: one primary (title, company type, triggering situation)
- [ ] Alternatives: 3+ including status quo and do-nothing
- [ ] Outcome: single most important buyer result in one sentence

**Ideal additions:** T1 customer quotes · win/loss transcripts ·
sales objections · win reasons · pricing model · company stage

**Evidence tier on input:**

- Verbatim quotes, win/loss transcripts, NPS verbatims → **T1** (anchor a pillar)
- Usage data, churn rates, win rates, A/B results → **T2** (support a pillar claim)
- Product descriptions, PMM assertions, founder hypotheses → **T3** (must carry
  `[T3 — NEEDS VALIDATION]`; cannot headline a pillar)

**Exit:** Summarise all four hard-floor items back to user. Await confirmation.

---

### Phase 2A: Market Energy Check

Identify primary segment energy state before mapping competitors.

| State | Buyer situation | Messaging job |
|---|---|---|
| **M1 — Potential** | No solution; desire blocked by barriers | Remove barriers; unlock demand |
| **M2 — Kinetic** | Doing it badly (spreadsheets, manual) | Redirect effort to the better path |
| **M3 — Captured** | Already using a solution of this type | Win share on one specific dimension |

Confirm with user. Primary positioning serves one state only. Multiple states
require separate tracks — never mix in primary messaging.

---

### Phase 2B: Competitive Mapping

Map all five alternative types honestly:

1. Direct competitors (same category)
2. Adjacent competitors (overlapping use case)
3. Status quo (spreadsheets, legacy tools, manual process)
4. Build in-house
5. Do nothing

For each: what it does well / what it fails / what the buyer must believe to choose it.

**Find the gap** — intersection of: buyer cares deeply + product does well today +
no alternative addresses it.

**Exit — cannot proceed without completing this sentence:**

> "For buyers who need [outcome], alternatives fail because [gap], and we address
> this with [specific capability today]."

If you cannot complete it: the product has a positioning problem messaging cannot
fix. Stop and surface this to the user.

---

### Phase 2C: Options-First

Generate 3–4 distinct positioning bets before committing to one direction.

Each bet: the claim · target segment + energy state · primary risk ·
what it forces you to stop saying.

Present to user. Await selection. Do not proceed to Phase 3 without a chosen direction.

---

### Phase 3: Positioning Development

Follow the Dunford sequence:

1. Competitive alternatives (from Phase 2B)
2. Unique attributes — specific only ("3-click onboarding" not "better UX")
3. Value translation — "So what?" × 3 levels; Level 3 belongs in messaging
4. Who cares most — narrow to trigger-event segment, not demographic
5. Market category — frame that makes strengths obvious, not odd
6. Positioning statement × 3 versions:
   > "For [segment] who [situation], [product] is the [category] that
   > [differentiator], unlike [alternative] which [limitation]."

Pick sharpest version. **Exit:** Statement cannot be said honestly by any
named competitor. If it can, rewrite.

---

### Phase 4: Messaging Hierarchy

Build top-down. Layer 3 claims must trace to Layer 1. Cannot trace → remove.

**Layer 1 — Strategic Narrative** (150–250 words)

Old world → Shift → New world → Your role. Product appears after the problem
is fully established.

**Layer 2 — Core Positioning**

Tagline 5–8 words · One-liner 15–25 · Elevator pitch 50–75 · Boilerplate 75–100

**Layer 3 — Key Message Pillars** (exactly 3–4, MECE)

Each: headline claim + 2–3 sentence explanation + 2–3 proof points

**Layer 4 — Persona Cards** (1–3 max)

Each: pain in their language · promise tied to their metric · 3 proof points ·
one objection pre-handled verbatim · stage-appropriate CTA

**Exit:** All layers complete. Persona CTAs match actual sales motion.

---

### Phase 5: Differentiation Stress-Test

4-question test per differentiator. YES or NO only:

1. **TRUE?** — Provable with evidence a skeptical buyer accepts
2. **RELEVANT?** — Buyer cares enough to switch or pay more
3. **UNIQUE?** — 2+ competitors cannot honestly claim the same
4. **SUSTAINABLE?** — Still true in 12–18 months

Scoring (no exceptions):

- 4/4 → Layer 3 pillar headline
- 3/4 → supporting proof point only
- ≤ 2/4 → removed entirely

---

### Phase 6: Output Packaging

**Self-Verification Gate** — binary pass/fail, 7 checks. Re-enter named phase on
any failure. Do not deliver with a caveat instead of a fix.

| Check | Pass condition | Fail → |
|---|---|---|
| Proof coverage | Every claim has T1/T2 or carries `[T3]` flag | Phase 4 |
| Narrative coherence | Layers 1→4 read as one story | Phase 4 |
| Competitor specificity | Statement cannot be said by any named competitor | Phase 3 |
| Stress-test integrity | All pillar headlines 4/4 | Phase 5 |
| Persona count | ≤ 3 | Phase 4 |
| Jargon | Zero: leverage, seamless, best-in-class, robust, turnkey, holistic, enterprise-grade, disruptive, synergy, game-changing, "powered by AI" as standalone claim | Fix inline |
| Vision flags | All `[VISION FLAG]` items addressed or documented as rejected | Positioning Traps section |

Before delivering, state: `"Self-verification passed. [N]/7 checks clear."`

**Mode outputs:**

`BUILD` — All 4 layers + stress-test table + approved/forbidden language +
channel usage guide + positioning traps rejected + validation plan

`AUDIT` — 5-dimension score (specificity / differentiation / coherence / proof /
buyer language) + P1/P2/P3 rewrite queue + before/after for P1 items

`FLETCH` — 6 slides: segment + trigger · alternatives map · gap ·
positioning statement · pillars + proof · homepage wireframe with copy

`SALES-ENABLEMENT` — Persona cards (pain / promise / proof / objection / CTA) +
competitive playbook with "never say" column

`HOMEPAGE` — Hero headline <8 words · subhead <20 words · 3 pillar headlines
+ 1-sentence descriptions · primary + secondary CTA · 2 proof strip options.
No placeholders.

**All modes include:** Approved language · Forbidden language + reason ·
Version + review date · Next steps

---

### Phase 7: Learning Close

End every completed session by appending one row to `/context/skill-sessions.md`
(create the file with a header row if it doesn't exist yet):

````yaml
skill: positioning-messaging
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
````

Write this row directly — do not ask the user for permission. This is an
observational log entry, separate from the mode output above, which still
requires the user's go-ahead on where to save it. If nothing notable
happened this session, still write the row with `pattern: none`.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one appended row per
  session, per Phase 7. Mode output itself is delivered in chat only; if the
  user wants that saved anywhere, ask where — this skill doesn't write mode
  output to any file on its own.

- **Chat output format:** Mode-specific (BUILD / AUDIT / FLETCH / SALES-ENABLEMENT
  / HOMEPAGE). All modes include approved/forbidden language list, version, review
  date, and next steps

- **External side effects:** n.v.t.

---

## Verification

- Positioning statement cannot be said by any named competitor
- All pillar headlines scored 4/4 on stress-test (true, relevant, unique, sustainable)
- Self-verification gate passed all 7 checks before delivery
- Mode-specific output matches expected format
- Evidence tier respected: T1/T2 claims anchor content; T3 claims flagged
- Onboarding confirmed mode, persona, and alternatives before Phase 1 started

---

## Do Not Use For

- **product-marketing-context** — when the task is buyer profiling, ICP
  definition (Section 2), or mapping competitive alternatives (Section 3)
  rather than producing positioning output

- **value-proposition** — when you only need segment-specific value props
  without a full messaging hierarchy

- **(no dedicated skill yet)** — sales competitive response cards; handle
  within this skill's SALES-ENABLEMENT mode instead

- **experiment-doc-builder** — when testing messaging assumptions; this skill
  builds messaging, not validates it experimentally

---

## Commands

### /build [product name or context]
Run full BUILD mode: Onboarding → all 6 phases → 4-layer messaging document.

### /audit [existing copy or landing page]
Run AUDIT mode: score existing messaging + rewrite queue.

### /fletch [product name]
Run FLETCH mode: 6-slide internal deck + homepage wireframe.

### /sales [product name]
Run SALES-ENABLEMENT mode: persona cards + competitive playbook.

### /homepage [product name]
Run HOMEPAGE mode: production-ready hero + subhead + pillars + CTA.

### /settings
Re-run the Onboarding block. Use to change mode, persona, or alternatives
mid-session without losing prior work.

---

## Operating Rules

1. **Run Onboarding before everything.** Mode, persona, and alternatives must be
   confirmed before Phase 1 starts. No exceptions.

2. **Load brain first.** Context changes which energy state (M1/M2/M3) applies.

3. **Parse attached images before asking discovery questions.** Every explicit
   claim and visual signal tells you something.

4. **No positioning without 3+ alternatives — status quo mandatory.** If you can't
   name it, you don't understand the choice.

5. **Never skip phases.** All 6 phases run for every mode. Shortcuts produce
   weak output.

6. **Primary persona must be ranked.** Ask: who has this problem worst, right now?

7. **Stress-test all pillars before delivery.** 4/4 or remove. No exceptions.

8. **Layer 3 claims must trace to Layer 1.** Cannot trace = doesn't belong.

9. **Evidence tier is binding.** T3 claims must be flagged. Don't hide assumptions.

10. **`/settings` resets Onboarding only.** Prior session work is preserved.

---

## Quality Gate

Runs after output generation, before delivery. Surface failures — do not deliver
incomplete output.

| Check | Standard | Pass = |
|---|---|---|
| Onboarding complete | Mode, persona, alternatives confirmed | Yes |
| Proof coverage | Every claim has T1/T2 or carries `[T3]` flag | Yes |
| Narrative coherence | Layers 1→4 read as one story | Yes |
| Competitor specificity | Statement cannot be said by any named competitor | Yes |
| Stress-test integrity | All pillar headlines 4/4 | Yes |
| Persona count | ≤ 3 | Yes |
| Jargon free | Zero forbidden terms | Yes |
| Vision flags resolved | All `[VISION FLAG]` items addressed or rejected | Yes |
| Mode format correct | Output matches expected format for selected mode | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |
