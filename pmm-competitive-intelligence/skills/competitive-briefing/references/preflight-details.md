# Preflight details

Moved verbatim from `SKILL.md`.

## Pre-flight (moved verbatim; route check and constraints stay in SKILL.md)

- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times in earlier briefing sessions.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): if `/foundation/me.md` exists, read it for format, detail and currency only. Never take a company fact from it.
- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll build from three quick answers for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask in the Step 2 message: (1) who we sell to, one line; (2) our two real strengths against competitors, with a source; (3) the quarter's one priority. Use them as stand-ins for Sections 2, 6 and 7 for this session only, and mark unsourced items `[Rep-stated]`. Our side of every option carries only what the user sourced.
- **Freshness:** a loaded brain section past its limit (Section 3, 2, 8: 180 days; Section 5, 7: 90 days; Section 6: 12 months per claim) goes into the Held list. For competitor facts use the `competitive-profile` windows: price 60 days; product, positioning and moves 90 days; buyer-side facts 180 days.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If naming a competitor to this audience is prohibited, stop and show the entry; do not build around it.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a brain field this brief needs is empty or stale and the answer would change it, ask one question (the question, one line on why, "answer or skip"). Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run.
