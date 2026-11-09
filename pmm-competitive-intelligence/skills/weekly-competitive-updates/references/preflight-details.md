# Preflight details

Reference for `weekly-competitive-updates`. Read it in Pre-flight. The route check, the constraints and the cost line stay in `SKILL.md`.

## Brain absent: the setup answers are the Quick-Brain

A plugin can be installed alone, so this skill never ends a session with a redirect. Say once: "No PMM brain found, so I'll build from your setup answers for this session. Run `product-marketing-context` later (a separate plugin) to keep them."

Ask in the Step 2 message, five questions at most: (1) the company, (2) the competitors and their sub-brands, (3) the markets, (4) one line on what you sell and to whom, (5) the requester. Use (4) as the stand-in for Sections 1 and 2 for this session only; mark anything you cannot source `[Rep-stated]`. The Coverage line says "Built from setup answers; no brain loaded". Save the answers to `setup.md`.

## Freshness

A loaded brain section past its limit (Sections 2, 3 and 8: 180 days; Sections 5 and 7: 90 days; Section 6: 12 months per claim) goes into Data Confidence & Gaps as a one-line flag. A saved competitor set older than 90 days is re-confirmed in the Step 2 line.

## Gap capture

If a brain field this update needs is empty or stale and the answer would change it, ask one question: the question, one line on why it matters, and "answer or skip". Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run, and none in a scheduled run.

## Personal context

If `/foundation/me.md` exists, read it for output length, level of detail and how blunt to be. Never take a company fact or the requester's identity from it. A missing `me.md` is normal.

## Meta-patterns

Load `/context/meta-patterns.md` if present. Surface a guardrail that fired two or more times in earlier sessions of this skill.
