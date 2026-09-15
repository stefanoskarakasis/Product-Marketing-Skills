# message-house Eval Suite

Setup populates `/foundation/brain.md` with a baseline PMM context (Sections 1–6) unless a test explicitly varies it, and checks `/context/skill-sessions.md` for the Learning Close row after each run.

## Eval 1 — Full source, complete Roof + Pillars

**Setup:** `/foundation/brain.md` fully populated — Section 1 (product name, tagline, use case, descriptions), Section 2 (ICP with target audience/user/buyer persona), Section 3 (positioning statement + 3 named differentiators), Section 5 (customer pain per differentiator), Section 6 (proof points and one real customer example per differentiator).

**Prompt:** "Build our message house."

**Expect:** Single deliverable with a complete Roof table (all 11 fields populated, none blank) and a 3-column Pillars table (Key value, Promise, Customer pain, Product promise, Product proof points, Customer examples — all populated from Sections 3/5/6). No `[MISSING]` tags. "Still needed" list absent or empty.

## Eval 2 — No brain, no pasted positioning output → block

**Setup:** No `/foundation/brain.md` file. No positioning-messaging output pasted in conversation.

**Prompt:** "Give me a message house for our product."

**Expect:** Skill blocks before building any table. Response redirects to `product-marketing-context` or `positioning-messaging` (BUILD mode), matching the Pre-flight gate language. No table is produced.

## Eval 3 — Partial brain: gaps flagged, never fabricated

**Setup:** `/foundation/brain.md` present with Section 3 positioning statement and one differentiator, but Section 2 (ICP/personas) empty, Section 6 proof points containing a literal placeholder ("xx% increase", "[customer]").

**Prompt:** "Build our message house."

**Expect:** Target audience, User persona, and Buyer persona rows marked `[MISSING — ...]`, not invented. The placeholder proof point is flagged `[MISSING — replace placeholder]`, not carried through as if it were a real stat. A "Still needed" list at the end enumerates every flagged field — count in the list matches count of `[MISSING]` cells in the tables.

## Eval 4 — More than 3 pillar candidates → forces ranking, never silently picks

**Setup:** `/foundation/brain.md` Section 3 contains 5 named differentiators, all with supporting Section 5/6 content.

**Prompt:** "Build our message house."

**Expect:** Skill does not silently choose 3 of the 5. It asks the user to rank or merge down to 3 before building the Pillars table. No table with more than 3 pillar columns is ever produced, and none is produced before the ranking question is resolved.

## Eval 5 — Pasted positioning-messaging output overrides stale brain

**Setup:** `/foundation/brain.md` Section 3 has an old positioning statement. User pastes a fresh `positioning-messaging` BUILD-mode output in the same message with a different positioning statement and updated pillars.

**Prompt:** "Here's our latest positioning: [pasted BUILD output]. Now build the message house."

**Expect:** Roof's Positioning statement row and the Pillars table reflect the pasted output, not the stale brain content. The one-line conflict note is surfaced to the user (e.g. "used your pasted positioning over the brain's older Section 3 statement").

## Eval 6 — Learning Close logs the real shape, no permission asked

**Setup:** Any successful run (e.g. Eval 1's setup).

**Expect:** After delivering the message house, the skill appends one row to `/context/skill-sessions.md` with exactly these fields — `skill`, `session_date`, `source`, `pillars_built`, `missing_fields`, `missing_field_names`, `pattern` — matching Step 6 of `SKILL.md` verbatim. No additional fields. Logged directly, without asking the user to confirm the log entry (only brain writes require confirmation, and this skill makes none).

## Eval 7 — End-to-end, single deliverable

**Setup:** Eval 1's fully-populated brain.

**Prompt:** "Build our message house."

**Expect:** Output arrives as one document containing both tables together, not split across multiple messages or a table-then-a-follow-up-message pattern. The skill does not attempt to also audit or rewrite the underlying positioning (that's `positioning-messaging`'s job) — it only reformats what it read.

## Eval 8 — /gaps returns the punch list only, no table

**Setup:** Eval 3's partial brain (some fields missing, one placeholder proof point).

**Prompt:** "/gaps"

**Expect:** Steps 0–1 run, but no Roof or Pillars table is produced. Response is just the "Still needed" list — same field names and count that Eval 3's full run would have produced under "Still needed." No Learning Close row is required to test here, but if one is logged it must still match the Step 6 shape.

## Eval 9 — /roof and /pillars build only their half

**Setup:** Eval 1's fully-populated brain.

**Prompt A:** "/roof"
**Expect A:** Only the Roof table is returned (Steps 0, 1, 2). No Pillars table, no pillar-selection question, even though Section 3 has 3 valid differentiators available.

**Prompt B:** "/pillars"
**Expect B:** Only the Pillars table is returned (Steps 0, 1, 3, 4). No Roof table. If more than 3 differentiators are present, the same ranking gate from Eval 4 still applies before the table is built.

## Eval 10 — /house matches default full-run behavior

**Setup:** Eval 1's fully-populated brain.

**Prompt:** "/house"

**Expect:** Identical output shape to Eval 1's plain-language prompt — full Roof + Pillars table, "Still needed" section (empty here), and a Learning Close row logged. Confirms the shortcut is not a different code path with different guarantees, just a faster entry point into the same Steps 0–6.
