---
name: hs-positioning-messaging
version: 2.0.0
description: >
  Use for any positioning or messaging task — positioning statement, messaging
  hierarchy, homepage copy, sales persona cards, competitive deck, messaging audit,
  value proposition, tagline, elevator pitch, or when the user says "we sound like
  everyone else," "our messaging isn't landing," "sales can't explain what we do,"
  or mentions April Dunford, Emily Kramer, or Obviously Awesome; runs the full
  Dunford sequence across five output modes (BUILD / AUDIT / FLETCH /
  SALES-ENABLEMENT / HOMEPAGE) with Pawel Huryn's self-improving memory loop.
  Parses attached screenshots and images before asking any questions, refuses
  briefs without a named primary persona and at least three alternatives including
  status quo, and blocks output until a 7-point self-verification gate passes.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-11
---

# hs-positioning-messaging

Built on April Dunford's Obviously Awesome method. Output discipline from
MKT1/Emily Kramer: deliver the answer, not the workings. Self-improving memory
via Pawel Huryn's compounding loop.

**Session start — silently, in order:**
1. Read `knowledge/INDEX.md` — load `knowledge/rules.md` and `knowledge/hypotheses.md`
2. Check `decisions/INDEX.md` for any prior structural decisions relevant to this product/domain
3. Parse all attached images before reading the user's text
4. Proceed to mode selection

---

## Trigger

- **When:** Positioning, messaging, value prop, sales copy, competitive messaging, homepage copy, or messaging audit work
- **Not for:** Product specification → use hs-product-requirement-doc. Internal positioning audit without output → consult hs-alternatives-map first. Buyer persona building → use hs-buyer-personas.
- **Example prompts:**
  - "Build positioning for [product]"
  - "Our messaging sounds like everyone else"
  - "Help me position against [competitor]"
  - "Write our homepage headline and pillars"
  - "Audit this messaging for coherence"
  - "We can't explain what we do to sales"

---

## Inputs

- **Args:** Product/market context, target persona (required), alternatives (3+ minimum, must include status quo + do-nothing), customer evidence or win/loss signals
- **Defaults:** If no persona named, run Phase 1 discovery first. If fewer than 3 alternatives provided, ask for status quo before proceeding.
- **Context keys:**
  - `/foundation/brain.md` — optional. Sections 1, 2, 4 (ICP, positioning pillars, alternatives map) if available
  - `knowledge/rules.md` — optional. Apply confirmed market energy state patterns
  - `knowledge/hypotheses.md` — optional. Note active tests relevant to this positioning decision

---

## Pre-flight

- Load `/foundation/brain.md` if it exists. Extract ICP, positioning hypothesis, competitive alternatives silently.
- If brain exists but Section 3 (Positioning) is marked 🔴 Placeholder: flag before intake: "⚠️ Your positioning hypothesis is marked Placeholder. This output will be sharper after validation. Continuing."
- If fewer than 3 alternatives provided: block intake and ask for status quo + do-nothing before proceeding.
- If no brain found: surface once, non-blocking: "No brain found. Run hs-product-marketing-context first for sharper output. Continuing."

---

## Steps

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
- Images → Vision Layer already parsed; use findings as T1/T2 where applicable
- Win/loss quotes → T1; extract exact buyer language
- Usage/conversion data → T2; note metric and source
- Homepage/deck text → T3 until validated; audit for undifferentiated terms
- Product description only → T3; flag all capability claims `[T3 — NEEDS VALIDATION]`

**Exit:** Summarise all four hard-floor items back to user. Await confirmation.

---

### Phase 2A: Market Energy Check

Identify primary segment energy state before mapping competitors.

| State | Buyer situation | Messaging job |
|-------|----------------|---------------|
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

**Exit:** Complete before proceeding:
> "For buyers who need [outcome], alternatives fail because [gap], and we address
> this with [specific capability today]."

Cannot complete it? The product has a positioning problem messaging cannot fix. Stop.

---

### Phase 2C: Options-First

Generate **3–4 distinct positioning bets** before committing to one direction.
Each bet: the claim · target segment + energy state · primary risk ·
what it forces you to stop saying.

Present to user. Await selection. Do not proceed to Phase 3 without a chosen direction.

---

### Phase 3: Positioning Development

**Load `references/positioning-worksheet.md`.** Follow it exactly.

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

**Load `knowledge/rules.md` and `knowledge/hypotheses.md`.** Apply confirmed rules first, then check hypotheses for active tests.

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

**Load `references/example-messaging-doc.md`.** That is the quality bar.

### Self-Verification Gate

Binary pass/fail. If any check fails: re-enter the named phase, fix, re-run
gate from top. Do not deliver with a caveat instead of a fix.

| Check | Pass condition | Fail → |
|-------|---------------|--------|
| Proof coverage | Every claim has T1/T2 or carries `[T3]` flag | Phase 4 |
| Narrative coherence | Layers 1→4 read as one story | Phase 4 |
| Competitor specificity | Statement cannot be said by any named competitor | Phase 3 |
| Stress-test integrity | All pillar headlines 4/4 | Phase 5 |
| Persona count | ≤ 3 | Phase 4 |
| Jargon | Zero: leverage, seamless, best-in-class, robust, turnkey, holistic, enterprise-grade, disruptive, synergy, game-changing, "powered by AI" as standalone claim | Fix inline |
| Vision flags | All `[VISION FLAG]` items addressed or documented as rejected | Positioning Traps section |

Before delivering, state: `"Self-verification passed. [N]/7 checks clear."`

### Mode outputs

**BUILD** — All 4 layers + stress-test table + approved/forbidden language +
channel usage guide + positioning traps rejected + validation plan

**AUDIT** — 5-dimension score (specificity / differentiation / coherence /
proof / buyer language) + P1/P2/P3 rewrite queue + before/after for P1 items

**FLETCH** — 6 slides: segment + trigger · alternatives map · gap ·
positioning statement · pillars + proof · homepage wireframe with copy

**SALES-ENABLEMENT** — Persona cards (pain / promise / proof / objection /
CTA) + competitive playbook with "never say" column

**HOMEPAGE** — Hero headline <8 words · subhead <20 words · 3 pillar headlines
+ 1-sentence descriptions · primary + secondary CTA · 2 proof strip options.
No placeholders.

### All modes include
Approved language · Forbidden language + reason · Version + review date ·
Next steps from `references/validation-playbook.md`

---

### Vision Layer (Opus 4.7)

Parse every attached image immediately. Do not ask the user to describe it.
Surface findings in Phase 1 as **"What your current materials are saying"**
before any discovery questions.

**Extract from any image:**
- Every explicit claim (exact text)
- Implied market category and target buyer
- Proof elements present (logos, metrics, quotes)
- All undifferentiated terms → flag each:
  `[VISION FLAG] "exact text" — reason this is weak`

The same extraction applies regardless of image type (homepage, deck slide,
ad, competitor page, one-pager). Flag, don't describe.

---

### Evidence Standard

Classify all inputs before Phase 2. Tier governs output weight.

| Tier | Qualifies as | Output rule |
|------|-------------|-------------|
| **T1** | Verbatim customer quotes, win/loss transcripts, NPS verbatims, G2 reviews in buyer's words | Can anchor a pillar headline |
| **T2** | Usage data, churn rates, win rates, A/B results, conversion data | Supports a pillar claim |
| **T3** | Product descriptions, PMM assertions, founder hypotheses | Must carry `[T3 — NEEDS VALIDATION]` flag; cannot headline a pillar |

**Refusal triggers:**
- Product in market 6+ months with zero T1/T2 → ask for it; don't proceed without
- Primary persona missing or unranked → ask: who has this problem worst, right now?
- Fewer than 3 alternatives (must include status quo + do-nothing) → no positioning without them
- Differentiator is a roadmap item → mark `[ROADMAP — NOT YET VALID]`; exclude

---

## Outputs

- **Files written:** n.v.t. — hs-positioning-messaging produces no persistent files; outputs delivered in chat
- **Chat output format:** Mode-specific (BUILD / AUDIT / FLETCH / SALES-ENABLEMENT / HOMEPAGE), all include approved/forbidden language, version, review date, next steps
- **External side effects:** n.v.t.

---

## Verification

- Positioning statement cannot be said by any named competitor
- All pillar headlines scored 4/4 on stress-test (true, relevant, unique, sustainable)
- Self-verification gate passed all 7 checks before delivery
- Mode-specific output matches expected format (BUILD / AUDIT / FLETCH / SALES-ENABLEMENT / HOMEPAGE)
- Evidence tier respected: T1/T2 claims anchor content; T3 claims flagged

---

## Do Not Use For

- **hs-product-marketing-context** — when the task is buyer profiling or market definition → use that skill first
- **hs-value-prop-statements** — when you only need segment-specific value props (not full messaging hierarchy)
- **hs-competitive-battlecard** — when building sales competitive response; use that skill instead
- **hs-icp** — when the primary need is ICP definition, not positioning
- **experiment-doc-builder** — when testing messaging assumptions; this skill builds messaging, not validates it

---

## Commands

### /build [product name or context]
Run full BUILD mode: all 6 phases → 4-layer messaging document.

### /audit [existing copy or landing page]
Run AUDIT mode: score existing messaging + rewrite queue.

### /fletch [product name]
Run FLETCH mode: 6-slide internal deck + homepage wireframe.

### /sales [product name]
Run SALES-ENABLEMENT mode: persona cards + competitive playbook.

### /homepage [product name]
Run HOMEPAGE mode: production-ready hero + subhead + pillars + CTA.

---

## Learning Mode Close

At session end:
> "Run Learning Mode close? I'll log what worked and update the skill's memory."

If yes, in order:
1. Check `knowledge/rules.md` — demote any rule contradicted this session
2. Check `knowledge/hypotheses.md` — promote any confirmed 3+ times; log new observations
3. Check `decisions/INDEX.md` — log any structural decision made this session
4. Append to `sessions/log.md` using the session format
5. Update `knowledge/INDEX.md` status counts if rules/hypotheses changed

**No file is written without explicit user approval. No updates mid-session.**

---

## Reference Files

| File | Load when |
|------|-----------|
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

- **Load brain first.** Context changes which energy state (M1/M2/M3) applies.
- **Parse attached images before asking discovery questions.** Every explicit claim and visual signal tells you something.
- **No positioning without 3+ alternatives — status quo mandatory.** If you can't name it, you don't understand the choice.
- **Never skip phases.** All 6 phases run for every mode. Shortcuts produce weak output.
- **Primary persona must be ranked.** Ask: who has this problem worst, right now?
- **Stress-test all pillars before delivery.** 4/4 or remove. No exceptions.
- **Layer 3 claims must trace to Layer 1.** Cannot trace = doesn't belong.
- **Evidence tier is binding.** T3 claims must be flagged. Don't hide assumptions.

---

## Quality Gate

Runs after output generation, before delivery. Surface failures — do not deliver
incomplete output.

| Check | Standard | Pass = |
|---|---|---|
| Proof coverage | Every claim has T1/T2 or carries `[T3]` flag | Yes |
| Narrative coherence | Layers 1→4 read as one story | Yes |
| Competitor specificity | Statement cannot be said by any named competitor | Yes |
| Stress-test integrity | All pillar headlines 4/4 | Yes |
| Persona count | ≤ 3 | Yes |
| Jargon free | Zero forbidden terms | Yes |
| Vision flags resolved | All `[VISION FLAG]` items addressed or documented as rejected | Yes |
| Mode format correct | Output matches expected format for selected mode | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load `knowledge/INDEX.md` — load `knowledge/rules.md` and `knowledge/hypotheses.md`
2. Check `decisions/INDEX.md` for any prior structural decisions relevant to this product/domain
3. Parse all attached images before reading the user's text
4. Proceed to mode selection

### After every session where output was produced:
1. Extract any positioning pattern → `knowledge/positioning/patterns.md`
2. If the same stress-test failure appears 3+ times → propose rule addition to `knowledge/positioning/rules.md`
3. If a competitor alternative was underestimated 3+ times → propose update to `knowledge/competitive-blind-spots.md`
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

### v2.0.0 — 2026-06-11
Full rebuild to SKILL-SPEC v2.0.0. Replaced legacy document with production-grade skill.

Changes from v1.0.0:
- Added all 7 required sections: Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For
- Frontmatter now includes version, author, context, quality_gate, last_updated
- 6-phase discovery flow formalized (Discovery → Market Energy Check → Competitive Mapping → Options-First → Development → Output)
- Stress-test 4-question rubric (True / Relevant / Unique / Sustainable)
- 5 output modes documented (BUILD / AUDIT / FLETCH / SALES-ENABLEMENT / HOMEPAGE)
- Evidence tier classification (T1/T2/T3) with output rules
- Operating rules (8) + Quality Gate (8 checks) + Self-Improvement Loop
- Learning Mode close formalized
- Reference file loading documented
- Changelog added

### v1.0.0 — [date]
Initial build. Phase-based positioning framework.
