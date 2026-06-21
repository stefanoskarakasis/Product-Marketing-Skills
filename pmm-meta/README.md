# pmm-meta

Meta skills that operate on the skill system itself. Install alongside any PMM plugin to improve skill quality and compound learnings across sessions.

## Skills (4)

- **meta-synthesis** (v1.0.0) — The beating heart of your GTM system. Reads all execution skill session logs, detects recurring patterns across skill domains, proposes guardrails, and gates brain updates. Makes every execution smarter than the last. Runs monthly or on-demand after 3+ skill sessions.

- **meta-learn** — Captures post-session patterns, routes them to the correct knowledge files, and compounds intelligence across all skills over time.

- **meta-review** — Audits any SKILL.md against SKILL-SPEC v2.0.0 — 19-point checklist with prioritised fixes.

- **meta-verify** — Second-pass quality check on T1 skill output before delivery.

## Core Commands (8)

The essential commands to get the most out of the meta skill set:

### Compounding & Learning
- `/pmm-meta:synthesis` — Run meta-synthesis monthly. Reads `/context/skill-sessions.md`, detects cross-skill patterns (2+ domains = HIGH priority), proposes guardrails and brain updates, gates approval before write. Output: `/context/meta-patterns.md` (master guardrails file read by all execution skills at pre-flight).

- `/pmm-meta:synthesis-status` — Show current meta-synthesis state: patterns detected this cycle, guardrails active/stale, brain updates proposed/approved, next run date.

- `/pmm-meta:learn` — Capture post-session learnings from any execution skill. Routes patterns to knowledge base. Run after every skill session to compound intelligence.

### Quality & Governance
- `/pmm-meta:review [skill-name]` — Audit any skill against SKILL-SPEC v2.0.0 (19-point checklist). Returns prioritised fix list.

- `/pmm-meta:review-all` — Batch review all skills in pmm-meta folder. Generates scorecard with gaps ranked by impact.

- `/pmm-meta:verify [skill-output]` — Independent quality check on T1 skill output before you ship it. Pressure-tests assumptions, flags weak reasoning.

### Knowledge Management
- `/pmm-meta:learn-history` — Show what patterns have been captured in knowledge base. Searchable by skill type, date, confidence level.

- `/pmm-meta:learn-promote [pattern-name]` — Promote a detected pattern to a confirmed rule. Moves from "watch" status to "active guardrail."

## How It Works

### The Compounding Loop
1. **Run execution skills** (experiment-doc, interview-summary, retro, pmm-okrs, etc.)
2. **Each skill logs session data** to `/context/skill-sessions.md` (Step 7 of every skill)
3. **Run `/pmm-meta:learn`** after each session to capture learnings
4. **End of month: Run `/pmm-meta:synthesis`**
   - Reads all logs from all skills
   - Detects patterns (2+ occurrences = flagged)
   - Proposes guardrails (injected into `/context/meta-patterns.md`)
   - Proposes brain updates (Sections 2, 5, 7) with approval gates
5. **Approve/reject guardrail & brain proposals**
6. **Next month: Execution skills load updated guardrails at Step 0 pre-flight**
7. **System gets smarter. Learnings compound.**

**By month 3:** System knows more about your GTM than you do.

### What Gets Stored & Reused

**`/context/skill-sessions.md`** — Master log of all skill executions
- One row per skill session
- Includes: quality scores, guardrails triggered, patterns detected, confidence deltas, brain update proposals
- Read by meta-synthesis to detect trends

**`/context/meta-patterns.md`** — Master guardrails file (written by meta-synthesis)
- HIGH-confidence patterns (3+ occurrences)
- MEDIUM-confidence patterns (2 occurrences)
- Cross-skill signals (2+ domains)
- Active/stale/new guardrail status
- Read by all execution skills at Step 0 pre-flight

**`/foundation/brain.md` Sections 2, 5, 7** — Updated by meta-synthesis (with approval gates)
- Section 2 (Anti-ICP): Anti-signals discovered in interviews
- Section 5 (Revenue): Adjusted if confidence calibration signals lever weight shift
- Section 7 (Meta-Learnings): Recurring patterns + system learnings

## Quick Start

1. **After your first execution skill run:**
   ```
   /pmm-meta:learn
   ```

2. **After 3+ skill sessions (or monthly):**
   ```
   /pmm-meta:synthesis
   ```

3. **Review guardrails proposed:**
   ```
   /pmm-meta:synthesis-status
   ```

4. **Before shipping any skill output:**
   ```
   /pmm-meta:verify [output]
   ```

5. **Audit a skill for spec compliance:**
   ```
   /pmm-meta:review [skill-name]
   ```

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
