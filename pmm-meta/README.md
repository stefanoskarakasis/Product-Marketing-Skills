# pmm-meta

Self-improving GTM system for product marketers. Meta skills that read execution logs, detect patterns, propose guardrails, predict success, and compound learnings across sessions. Integrated with Pawel Huryn's positioning rigor and 2026 GTM adoption lens.

## Skills (4)

- **meta-synthesis** — Reads all skill session logs, detects cross-skill patterns, proposes guardrails, gates brain updates. Runs 24h automation cycle.
- **meta-learn** — Captures post-session learnings, classifies patterns, routes to knowledge base, tracks hypothesis confirmation/contradiction. Runs auto-trigger on skill completion.
- **meta-review** — Scores output quality (Pawel positioning rigor + 2026 adoption lens), generates fix recommendations, trends quality, gates CI/CD deployments. Logs persistent team learnings.
- **meta-verify** — Predicts success confidence, suggests scope expansion (T2→T1), calibrates predictions over time, feeds learnings back to meta-learn.

## Commands (4)

- `/pmm-meta:synthesis` — Run 24h automation. Detects cross-skill patterns, proposes guardrails, updates brain. Show status: `/pmm-meta:synthesis-status`
- `/pmm-meta:learn` — Capture post-session learnings. Routes patterns, tracks hypotheses, gates approvals. Run after every skill session.
- `/pmm-meta:review [output]` — Score quality (Pawel rigor + adoption lens). Get auto-fix recommendations + confidence prediction.
- `/pmm-meta:verify [output]` — Predict success confidence. Suggest scope expansion if T2 quality justifies T1 tier.

## How It Works

Your system compounds learnings every 24 hours:

1. **Run execution skills** (go-to-market-strategy, beachhead-segment, retro, positioning, etc.)
2. **Run `/pmm-meta:learn`** after each session — captures patterns, routes to knowledge base
3. **Run `/pmm-meta:review`** on outputs — scores quality, logs team insights
4. **Meta-synthesis runs 24h** — detects cross-skill patterns (2+ domains), proposes guardrails
5. **Guardrails injected** → next skill loads updated guardrails at Step 0 pre-flight
6. **System gets smarter** — by month 3, your system knows more about your GTM than you do

## What Gets Logged & Reused

- `/context/skill-sessions.md` — Execution log (quality scores, guardrails triggered, confidence)
- `/context/meta-patterns.md` — Active guardrails (proposed by meta-synthesis, approved by user)
- `/sessions/quality-learnings.md` — Persistent team insights (what works, what doesn't, what to watch)
- `/foundation/brain.md` Sections 2, 5, 7 — Updated with meta-learnings (gated approval)

## Quick Start

1. Run any execution skill
2. `/pmm-meta:learn` — Capture learnings
3. (After 3+ skills) `/pmm-meta:synthesis` — Detect patterns, propose guardrails
4. Approve guardrails
5. Next skill loads updated guardrails → output quality improves

## Tech Stack

- **Positioning rigor:** Pawel Huryn (unique value clarity test)
- **Adoption lens:** 2026 GTM best practices (sales ramp, CS handoff, expansion triggers, enablement timing)
- **Pattern detection:** Cross-skill signal identification with confidence compounding
- **Hypothesis tracking:** Open hypothesis confirmation/contradiction/promotion
- **Approval gates:** User gates high-stakes knowledge base writes
- **Persistent memory:** Team learnings compound via quality-learnings.md
- **Confidence prediction:** Historical baseline → success probability
- **Calibration trending:** Prediction accuracy improves over time

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
