# Pre-flight details

Moved verbatim from `SKILL.md` Pre-flight.

- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times in earlier battlecard sessions.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): if `/foundation/me.md` exists, read it for format and detail only (length, shape, how blunt). It may shorten the card, never lengthen it past one page. Never take a company fact or the seller's role from it.
- **Freshness** (limits in `product-marketing-context/references/brain-schema.md`): a loaded section past its limit (Section 3, 2, 8: 180 days; Section 5, 7: 90 days; Section 6: 12 months per claim) goes into Check before use. A section marked 🔴 Placeholder is flagged before proceeding.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a brain field this card needs is empty, stale or untagged and the answer would change it (most often Section 3 `why_leaving` or Section 6 `approved_metrics`), ask one question (the question, one line on why, "answer or skip"). Answer: use it and offer it as a brain update. Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (`product-marketing-context/references/gaps-format.md`). At most one per run.
