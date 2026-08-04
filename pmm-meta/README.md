# pmm-meta

Self-improving GTM system for product marketers. Meta skills that read execution logs, detect patterns, propose guardrails, score collaboration, predict success, and compound learnings across sessions.

## Skills (4)

- **meta-synthesis** — Reads all skill session logs, detects cross-skill patterns, mines integrations, synthesizes dynamic user profiles, proposes guardrails, gates brain updates. Runs 24h automation cycle.
- **meta-learn** — Captures post-session learnings, classifies patterns, routes to knowledge base, tracks hypothesis confirmation/contradiction, gates approvals. Runs auto-trigger on skill completion.
- **meta-review** — Scores output quality, generates fix recommendations, trends quality, validates tier match, gates deployments, logs team learnings.
- **meta-verify** — Predicts success confidence, scores collaboration readiness (ownership/shareability/learnings), suggests scope expansion (T2→T1), calibrates predictions over time.

## Commands (4)

- `/pmm-meta:synthesis` — Run 24h automation. Detects patterns, proposes guardrails, updates brain. Show status: `/pmm-meta:synthesis-status`
- `/pmm-meta:learn` — Capture post-session learnings. Routes patterns to knowledge base. Run after every skill session.
- `/pmm-meta:review [output]` — Score quality. Get auto-fix recommendations + confidence prediction.
- `/pmm-meta:verify [output]` — Predict success confidence. Suggest scope expansion if quality justifies T1 tier.

## How It Works

Your system compounds learnings every 24 hours:

1. **Run execution skills** (go-to-market-strategy, beachhead-segment, retro, positioning, etc.)
2. **Run `/pmm-meta:learn`** after each session — captures patterns, routes to knowledge base
3. **Run `/pmm-meta:review`** on outputs — scores quality, logs team insights
4. **Meta-synthesis runs 24h** — detects cross-skill patterns (2+ domains), proposes guardrails
5. **Guardrails injected** → next skill loads updated guardrails at Step 0 pre-flight
6. **System gets smarter** — by month 3, your system knows more about your GTM than you do

## What Gets Stored & Reused

- `/context/skill-sessions.md` — Execution log (quality scores, guardrails triggered, confidence)
- `/context/meta-patterns.md` — Active guardrails (proposed by meta-synthesis, approved by user)
- `/sessions/quality-learnings.md` — Persistent team insights (what works, what doesn't, what to watch)
- `/sessions/confidence-log.md` — Confidence predictions + actual outcomes (calibration)
- `/sessions/collaboration-log.md` — Adoption tracking (predicted vs. actual reach)
- `/foundation/brain.md` Sections 2, 5, 7 — Updated with meta-learnings (gated approval)

## Quick Start

1. Run any execution skill
2. `/pmm-meta:learn` — Capture learnings
3. `/pmm-meta:review` — Score output
4. `/pmm-meta:verify` — Predict confidence + collaboration readiness
5. (After 3+ skills) `/pmm-meta:synthesis` — Detect patterns, propose guardrails
6. Approve guardrails
7. Next skill loads updated guardrails → output quality improves

## License

MIT
