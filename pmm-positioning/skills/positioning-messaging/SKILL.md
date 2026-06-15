---
name: hs-positioning-messaging
version: 2.1.0
description: >
  Use for positioning statement, messaging hierarchy, homepage copy, persona cards,
  messaging audit, value prop, or elevator pitch. Trigger when user says "we sound
  like everyone else," "messaging is not landing," or mentions April Dunford, Emily
  Kramer, or Obviously Awesome. Also trigger when user pastes copy for review.
  Runs full Dunford sequence across BUILD / AUDIT / FLETCH / SALES-ENABLEMENT /
  HOMEPAGE modes. Refuses to generate without named primary persona and 3+
  alternatives including status quo. Blocks output until 7-point verification
  gate passes.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-15
---

# hs-positioning-messaging

Built on April Dunford's Obviously Awesome method. Output discipline from
MKT1/Emily Kramer: deliver the answer, not the workings. Self-improving memory
via Pawel Huryn's compounding loop.

---

## Onboarding

> Run this block once at the start of every new session. No output until
> complete. One question at a time. This is the Settings screen — not discovery.

**Step 1 — Check brain:**
```
Does /foundation/brain.md exist?
  YES → Load silently. Note ICP, alternatives, energy state. Proceed.
  NO  → Surface once: "No brain found. You can still run this skill, but output
         will be less precise. Run hs-product-marketing-context first for
         sharper results. Continuing."
```

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
- **Not for:** Product specification → use hs-product-requirement-doc. Buyer
  persona building → use hs-buyer-personas. Alternatives mapping in isolation →
  use hs-alternatives-map first.
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
    3 (alternatives), 5 (voice) if available
  - `knowledge/rules.md` — load at session start; apply confirmed patterns
  - `knowledge/hypotheses.md` — load at Phase 5; check for active tests
  - `references/positioning-worksheet.md` — load at Phase 3
  - `references/example-messaging-doc.md` — load at Phase 6 as quality bar
  - `references/validation-playbook.md` — load at Phase 6 or on request

---

## Pre-flight

- Load `/foundation/brain.md` if it exists. Extract ICP, positioning hypothesis,
  competitive alternatives silently.
- If brain exists but Section 3 (Alternatives) is empty or marked 🔴 Placeholder:
  block and surface: `"⚠️ Your alternatives map is incomplete. Run hs-alternatives-map
  first, then return here. I need named alternatives before positioning."`
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

**Ideal additions:** T1 customer quotes · current messaging/screenshots ·
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

Load `references/positioning-worksheet.md`. Follow it exactly.

Dunford sequence:
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

Load `knowledge/rules.md` and `knowledge/hypotheses.md`. Apply confirmed rules
first, then check hypotheses for active tests.

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

Load `references/example-messaging-doc.md`. That is the quality bar.

**Self-Verification Gate** — binary pass/fail. Re-enter named phase on any failure.
Do not deliver with a caveat instead of a fix.

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
Version + review date · Next steps from `references/validation-playbook.md`

---

## Outputs

- **Files written:** n.v.t. — outputs delivered in chat only
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

- **hs-product-marketing-context** — when the task is buyer profiling or market
  definition → use that skill first
- **hs-value-prop-statements** — when you only need segment-specific value props
  without a full messaging hierarchy
- **hs-competitive-battlecard** — when building sales competitive response cards;
  use that skill after positioning is locked
- **hs-icp** — when the primary need is ICP definition, not positioning output
- **hs-alternatives-map** — when the primary need is mapping competitive
  alternatives in depth; use that skill first, then return here
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

## Learning Mode Close

At session end:
> "Run Learning Mode close? I'll log what worked and update the skill's memory."

If yes, in order:
1. Check `knowledge/rules.md` — demote any rule contradicted this session
2. Check `knowledge/hypotheses.md` — promote any confirmed 3+ times; log new
   observations
3. Check `decisions/INDEX.md` — log any structural decision made this session
4. Append to `sessions/log.md` using the session format
5. Update `knowledge/INDEX.md` status counts if rules/hypotheses changed

**No file is written without explicit user approval. No updates mid-session.**

---

## Reference Files

| File | Load when |
|---|---|
| `knowledge/INDEX.md` | Session start. Always first. |
| `knowledge/rules.md` | Session start + Phase 5 |
| `knowledge/hypotheses.md` | Phase 5 + Learning Mode close |
| `knowledge/false-beliefs/catalog.md` | AUDIT mode + diagnosing weak positioning |
| `decisions/INDEX.md` | Before any structural decision (category, segment, evidence tier) |
| `references/positioning-worksheet.md` | Phase 3 |
| `references/example-messaging-doc.md` | Phase 6 |
| `references/validation-playbook.md` | Phase 6 + on request |
| `sessions/log.md` | Learning Mode close only |

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

---

## Self-Improvement Loop

### Before every session:
1. Load `knowledge/INDEX.md` — load `knowledge/rules.md` and
   `knowledge/hypotheses.md`
2. Check `decisions/INDEX.md` for any prior structural decisions relevant to
   this product/domain
3. Parse all attached images before reading the user's text
4. Run Onboarding block

### After every session where output was produced:
1. Extract any positioning pattern → `knowledge/positioning/patterns.md`
2. If the same stress-test failure appears 3+ times → propose rule addition
   to `knowledge/rules.md`
3. If a competitor alternative was underestimated 3+ times → propose update
   to `knowledge/competitive-blind-spots.md`
4. Append session summary to `sessions/log.md`

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed this session]
Proposed update: [exact wording of what would be added or changed]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.1.0 — 2026-06-15
Added Onboarding block (Ramp-style setup wizard) as a standalone section before
Trigger. Added `/settings` command to re-run Onboarding mid-session. Updated
Operating Rules to 10 rules (was 8) — added onboarding enforcement and settings
reset rule. Added Quality Gate row for Onboarding completion check. Fixed
Self-Improvement Trigger format to match SKILL-SPEC v2.0.0 surface-before-encoding
requirement. Description expanded with additional trigger phrases for passive
discovery cases. Evals file added at `evals/evals.json`.

Architecture decisions:
- Onboarding runs before Phase 1, not inside it — separates configuration from
  discovery
- `/settings` command preserves session work while resetting configuration — parity
  with how Ramp handles settings without losing context
- Trigger format block is now a standalone declared section at end of Self-Improvement
  Loop per spec requirement
- Onboarding block checks brain, sets mode, confirms persona, confirms alternatives,
  and parses images — 5 explicit steps that previously were implicit in Pre-flight
  and Phase 1

### v2.0.0 — 2026-06-11
Full rebuild to SKILL-SPEC v2.0.0. Added all 7 required sections. 6-phase discovery
flow formalized. Stress-test 4-question rubric. 5 output modes. Evidence tier
classification. Operating rules + Quality Gate + Self-Improvement Loop.

### v1.0.0 — [date]
Initial build. Phase-based positioning framework.
