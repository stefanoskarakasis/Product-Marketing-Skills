# Eval: product-messaging-playbook

## Eval 1 — No brain, no pasted output → Quick-Brain
**Input:** "Build a messaging playbook for our new automations feature." No brain exists, nothing pasted this session.
**Expected:** The skill does not block. It asks the five Quick-Brain questions, waits for all five, then builds the playbook from the answers. The playbook is labelled "Built from Quick-Brain answers, not a full brain"; unanswered fields ship as `[MISSING — ...]`; the single proof point is `[NEEDS PROOF]` unless the source was given. Nothing is written to the brain. The Feature-Specific Intake (Step 2) still runs separately.

## Eval 2 — Full run with message-house + proof-points populated, no competitor named
**Input:** Brain exists, Section 6 has 3 clean approved entries, user pastes a `message-house` output, doesn't name a competitor.
**Expected:** Messaging Foundation (with Step 2 intake questions asked fresh), Story (pulled from pasted message-house output, Customer Proof pulled from the 3 clean Section 6 entries), Comparative Positioning section **skipped entirely** (not built with a placeholder competitor), Sales Enablement Kit, "Still needed" list, Learning Close entry appended.

## Eval 3 — Competitor named, present in Section 3
**Input:** User names "Breezy HR" as the competitor; Section 3 has a Breezy HR entry with stated differentiation.
**Expected:** Comparative Positioning section built — high-level pitch, differentiation pulled from Section 3 (not invented), 4-Forces classification with one force named as strongest, Customer Proof for this comparison flagged as "No customers referencing a switch from Breezy HR yet" since none exist in Section 6.

## Eval 4 — Competitor named but not in Section 3
**Input:** User names a competitor absent from brain Section 3.
**Expected:** Soft-block warning surfaced (not a hard block) recommending `alternatives-map`; skill offers to build Section 3 content from what the user states now, or continue without it. Does not silently invent Section 3 alternatives-map-quality research.

## Eval 5 — Success target requested, correctly separated from proof points
**Input:** Step 2 intake: user states "we expect 25% adoption and 30% stickiness in the first quarter."
**Expected:** Both numbers appear in Messaging Foundation labeled exactly `[TARGET — not yet measured]`. Neither number appears anywhere in the Story section's Customer Proof subsection or the Sales Enablement Kit's objection handling as if it were Section 6 evidence. Quality Gate "Targets labeled correctly" check passes.

## Eval 6 — Section 6 entries present but all flagged
**Input:** Section 6 has entries, but every one is `[NEEDS PROOF]` or `[NEEDS APPROVAL]`.
**Expected:** Customer Proof subsection ships as `[MISSING — no approved proof points yet; run proof-points]`, not silently empty, not populated with the flagged entries.

## Eval 7 — No SALES-ENABLEMENT output pasted, Section 6 has no Forbidden Claims
**Input:** No `positioning-messaging` SALES-ENABLEMENT output pasted; Section 6 exists but has no Forbidden Claims list.
**Expected:** Objection handling subsection ships as `[MISSING — run positioning-messaging SALES-ENABLEMENT mode or proof-points Audit mode for sourced objection handling]` — no freehand objection scripts invented to fill the gap.

## Eval 8 — Fields the user can't answer in Step 2
**Input:** User can't supply Keywords or Products Needed during intake.
**Expected:** Both ship as `[MISSING — <what's needed>]` in Messaging Foundation, both appear in the final "Still needed / not yet measurable" list — not silently dropped, not guessed from Section 1 product description.

## Eval 9 — Learning Close always runs
**Input:** Any completed session, including a Quick-Brain session (Eval 1).
**Expected:** Every session that proceeds past Pre-flight, including a Quick-Brain session, including one that skips Comparative Positioning (Eval 2) or ships several `[MISSING]` fields, appends exactly one `type: execution` entry to `/context/skill-sessions.md` with the canonical 5-field shape.

## Eval 10 — Connector present: pulled facts are tagged drafts

**Setup:** The `call recordings` connector is available and returns relevant material.

**Prompt:** "Build the messaging playbook and pull objections from our calls."

**Expect:** Facts are pulled and each is shown tagged with category, tool and date. Nothing is written to the brain or any external tool until the user confirms. Pulled quotes and proof points are marked unverified.

## Eval 11 — No connectors: paste fallback, same output shape

**Setup:** No connectors are available.

**Prompt:** "Build the messaging playbook."

**Expect:** The skill asks the user to paste the material, then produces the same output format as with a connector. It does not claim to have pulled anything.
