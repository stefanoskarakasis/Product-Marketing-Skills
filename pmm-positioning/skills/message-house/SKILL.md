---
name: message-house
version: 1.3.0
description: >
  Turns your existing positioning into one clean table: your core story
  at the top, your 3 supporting reasons to believe it below. Use when
  someone asks to "build a message house," "put our messaging in a
  message house," or wants positioning laid out as one scannable page.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-15
---

## Trigger

Use when the user asks to "build a message house," "put our messaging in a message house," "give me the roof and pillars," references messagehouse.org, or wants their positioning and value pillars laid out as a single scannable table for sales, leadership, or a new hire.

Not for: building positioning or a messaging hierarchy from scratch (route to positioning-messaging), or building personas from scratch (route to buyer-personas). This skill formats what already exists — it does not derive strategy.

Example prompts:
- "Build our message house"
- "Turn our positioning into a message house table"
- "I need the roof and pillars for a new hire deck"

## Inputs

- **Product/company name** (if not resolvable from brain Section 1)
- Optional: a pasted `positioning-messaging` BUILD or AUDIT output from this session — takes precedence over stale brain content for the same field
- Optional: number of pillars to build (default: however many the source material supports, capped at 3)

**Brain Read/Write Contract**
- Reads: Section 1 (Product context), Section 2 (ICP — for Target audience/User persona), Section 3 (Positioning), Section 4 (Voice and tone), Section 5 (Market context — for Customer pain), Section 6 (Proof points)
- Writes: none. This is a read-only, output-only formatter. It never edits `/foundation/brain.md`.
- Never writes to: any brain section.

## Pre-flight

Load `/foundation/brain.md` if present. If absent, check whether the user has pasted a `positioning-messaging` output this session.

**Gate check — block if both are missing:**
> "No brain and no positioning output found. A message house formats existing positioning — it doesn't create it. Run `product-marketing-context` to build the brain, or `positioning-messaging` (BUILD mode) first, then come back."

**Gate check — block if positioning is present but too thin:** if Section 3 has no positioning statement and no named differentiators/pillars, do not proceed to Step 2. Surface the same redirect.

## Steps

### Step 0 — Load Source Material
Pull Sections 1–6 from the brain. If a `positioning-messaging` output was pasted this session, prefer its fields over brain content wherever both exist, and note the conflict to the user in one line.

### Step 1 — Gap Check (never invent)
Walk every Roof and Pillar field. For each one with no traceable source (brain section or explicit user/pasted statement), mark it `[MISSING — <what's needed>]`. Never fill a gap with plausible-sounding copy. Flag any placeholder-style content in the source (e.g. literal "xx%", "[insert link]", "[customer]") as `[MISSING — replace placeholder]` rather than copying it through as if it were real.

### Step 2 — Build the Roof
One table, one row per field, in this exact order:
Product name · Tagline · Use case · Short description (≤25 words) · Long description (≤150 words) · Positioning statement · Key features (used) · Benefits (max 5) · Target audience · User persona · Buyer persona.
Apply the cell-formatting rules below — a multi-item field is never one run-on line.

**Description length is a hard requirement, not a suggestion.** Count the words in Short description and Long description before finalizing the table. If Short description exceeds 25 words, cut it down before it ships — don't ship an over-length draft with a caveat. If Long description exceeds 150 words, cut it down the same way. If the sourced brain content is already over-length, trim it for the deliverable (never fabricate a shorter version's content — cut redundant clauses, don't rewrite the substance) and do not mark it `[MISSING]` solely for being long; only mark it `[MISSING]` if there's no source content at all.

### Step 3 — Select Value Pillars (max 3)
Pull candidate pillars from brain Section 3 (named differentiators/messaging hierarchy tiers) or the pasted positioning output. Cap at 3 — more than 3 pillars means nothing is actually a pillar. If more than 3 credible candidates exist, ask the user to rank or merge before building the table; do not silently pick.

### Step 4 — Build the Pillars Table
One column per pillar (max 3), one row per field, in this exact order:
Key value (label) · Promise · Customer pain · Product promise · Product proof points · Customer examples.
Every proof point and customer example must trace to brain Section 6 or an explicit user statement this session — cite the source inline in parentheses if it's not obviously the company's own name. Apply the cell-formatting rules below.

**Cell formatting (Steps 2 and 4, every table cell):**
- A field with 2+ items (Key features, Benefits, Product proof points) renders as one bulleted line per item inside the cell, using the `•` bullet character — never a hyphen/dash — separated by `<br>` so each renders as a real line break (`<br>• ` between items in the raw markdown), never packed onto one visual line.
- **Key features specifically: bold the feature name.** Each bullet is `• **Feature name** — one-sentence explanation.` The name is the short label (2–4 words), bolded; everything after the em dash is plain text. Benefits and Product proof points stay plain bullets — no bolding — since they're outcomes, not named things.
- A field with one idea but multiple clauses (Long description, Customer pain, Product promise) breaks at sentence boundaries onto separate lines when it's more than one sentence — no bullet character on these, just a line break; don't force a single-sentence field onto its own line.
- A quote (Customer examples) stays on its own line, attribution on the line directly below it, not inline after an em dash mid-paragraph. No bullet on the quote or attribution line.
- No dashes anywhere in the deliverable as a bullet marker — `•` is the only bullet character this skill uses, matching this repo's existing convention (`beachhead-segment` and others use `•`, not `-`, for list content).
- No emoji inside table cells or bullets — content stays plain. Reserve emoji for section-level scannability only (see Step 5).

### Step 5 — Assemble & Deliver
Combine the Roof table and Pillars table into a single markdown deliverable. List every `[MISSING]` field together at the end under "Still needed" so the user has one punch list, not scattered flags.

**Section headers get one functional emoji each, matching this repo's existing convention (status/gate markers, never decoration):** 🏠 Roof, 🏛️ Value Pillars, 📋 Still needed (omit this marker entirely when the list is empty — an empty "Still needed" needs no icon). Do not add emoji anywhere else — not per-bullet, not per-row, not in the Roof/Pillars table content itself. One marker per section heading is the ceiling, not a starting point to build on.

### Step 6 — Learning Close
Log to `/context/skill-sessions.md`:

```yaml
skill: message-house
session_date: [YYYY-MM-DD]
source: [brain / positioning-messaging output / both]
pillars_built: [count, max 3]
missing_fields: [count]
missing_field_names: [list, or "none"]
pattern: [falsifiable statement about what happened this session, or "none"]
```

Written directly, no permission required — observational log, not content approval.

## Commands

### /house
Run the full skill immediately — Steps 0 through 6 — using default sourcing (brain, falling back to any pasted positioning output). Skips the trigger-phrase matching; use when you already know you want a message house.
```
/house
```

### /gaps
Run Steps 0–1 only. Return just the "Still needed" list of `[MISSING]` fields — no table. Useful for a pre-flight check before asking someone else to fill brain gaps, without generating the full deliverable yet.
```
/gaps
```

### /roof
Build only the Roof table (Steps 0, 1, 2). Skip pillar selection entirely. Useful when only the roof-level facts (tagline, description, positioning statement) changed and the pillars are still current.
```
/roof
```

### /pillars
Build only the Pillars table (Steps 0, 1, 3, 4). Useful after a `positioning-messaging` AUDIT changes the differentiators but the roof-level facts haven't moved.
```
/pillars
```

## Outputs

A single markdown document containing the Roof table and the Pillars table (side by side, up to 3 pillar columns), plus a "Still needed" list of any `[MISSING]` fields with what's required to fill each. Section headers carry one functional emoji each (🏠 / 🏛️ / 📋, per Step 5) — nothing decorative inside the tables themselves. Multi-item cells are line-broken per Step 2/4's cell-formatting rules, not packed onto one line. No files are written to the brain or filesystem by this skill — the deliverable is returned in chat/as a document for the user to save or paste into Notion, Slides, or Confluence themselves.

## Verification

- Every Roof row is either populated with sourced content or explicitly `[MISSING — ...]` — no blank cells, no invented copy.
- No more than 3 pillar columns.
- Every proof point and customer example in the Pillars table traces to brain Section 6 or an explicit statement made this session — none copied through from a placeholder.
- The "Still needed" list accounts for every `[MISSING]` cell in the tables — no silent gaps.
- Output is a single deliverable (one document, two tables), not fragmented across multiple messages.
- No cell contains 2+ items run together on one visual line — each item or sentence is on its own line per the cell-formatting rules.
- Every bulleted item uses `•`, never `-` or `*`.
- Emoji appear only on the three section headers, never inside a table cell or bullet.
- Short description is ≤25 words and Long description is ≤150 words — actually counted, not eyeballed. Neither ships over-length.
- Every Key features bullet has a bolded feature name before the em dash; Benefits and Product proof points bullets are plain, unbolded.

## Do Not Use For

- **positioning-messaging** — to build or audit the underlying positioning statement, messaging hierarchy, or homepage copy from scratch. Run this first if brain Section 3 is empty or thin.
- **product-marketing-context** — to build or audit the brain itself.
- **buyer-personas** — to build user/buyer personas from scratch, not just restate existing ones in the Roof.
- **product-marketing-context** — to add or update proof points and metrics; they live in brain Section 6, not a separate skill. Run first if Section 6 is thin, then message-house pulls from it.

## Operating Rules

- **Never fabricate.** A field with no traceable source is `[MISSING]`, never a plausible guess. This includes not "rounding up" a placeholder stat into a real-looking number.
- **This skill does not derive strategy.** If positioning is absent or thin, redirect to `positioning-messaging` rather than inventing a positioning statement to fill the Roof.
- **Max 3 pillars, always.** More than 3 means the user hasn't actually prioritized — force the ranking conversation rather than listing 4+.
- **Every proof point must be traceable.** Brain Section 6 or an explicit statement this session — never an invented percentage, quote, or unnamed "[customer]" treated as real.
- **Read-only.** This skill never writes to `/foundation/brain.md`. It only reads and reformats.
- **Persona rows restate, not redefine.** Target audience/User persona/Buyer persona rows must reference existing brain Section 2 / persona-skill output — if none exists, mark `[MISSING]` and redirect, don't sketch a new persona on the spot.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Source loaded | Brain and/or pasted positioning output checked before building | Step 0 completed, source noted |
| No fabricated fields | Every Roof/Pillar cell sourced or flagged | Zero invented copy |
| Pillar cap respected | ≤3 pillar columns | Count ≤ 3 |
| Proof points traceable | Every proof point/example cites brain Section 6 or explicit user input | No placeholder text carried through as real |
| Missing-field list complete | "Still needed" accounts for every `[MISSING]` cell | Counts match |
| Single deliverable | One document, two tables | Not fragmented |
| Cell formatting applied | No multi-item cell packed onto one line | Each item/sentence on its own line |
| Bullet character correct | `•` used for every bulleted list item, never `-` or `*` | Zero dash/asterisk bullets anywhere in the deliverable |
| Emoji restrained | Only the 3 section headers carry a marker | None inside tables or bullets |
| Description length enforced | Short ≤25 words, Long ≤150 words, actually counted | Both under cap, neither shipped over-length |
| Feature names bolded | Every Key features bullet has a bolded name before the em dash | Benefits/proof points stay plain |
| Learning Close logged | Step 6 YAML appended | Row present in `/context/skill-sessions.md` |

## Self-Improvement Loop

Each session logs to `/context/skill-sessions.md`: source used, pillar count, missing-field count and names, and one falsifiable pattern statement.

Monthly, `meta-synthesis` reads these logs for patterns such as: "Target audience is missing more often than any other Roof field → brain Section 2 is chronically thin" or "Users consistently request 4+ pillars → reconsider whether the 3-pillar cap needs an explicit override path." Patterns feed back into brain-quality guardrails surfaced by `product-marketing-context`, not into this skill's own logic — message-house stays a formatter.
