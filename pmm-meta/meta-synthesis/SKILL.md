---
name: meta-synthesis
version: 3.2.0
description: >
    Reads /context/skill-sessions.md (the session log every execution skill writes to) to detect patterns that repeat across 2+ sessions, proposes new guardrails for /context/meta-patterns.md, and proposes brain updates for confirmed learnings. Run on-demand or roughly weekly — not a scheduled background job. Trigger on: "run meta-synthesis", "what patterns are emerging", "detect cross-skill signals", "update guardrails", "compound our learnings", "what should we remember".
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-24
---

# meta-synthesis — Skill

## How This Works

Reads the session log every execution skill already writes to, finds patterns that repeat across 2 or more sessions, and turns confirmed patterns into either a guardrail (for `/context/meta-patterns.md`) or a brain update (for `/foundation/brain.md`). This is what makes the rest of the stack compound instead of starting fresh every session.

The skill runs in 5 steps:

**Step 0** — Load `/context/skill-sessions.md` and `/context/meta-patterns.md`. Block if the session log doesn't exist or has zero rows.

**Step 1** — Scan sessions for repeated patterns, both within one skill and across skills.

**Step 2** — Rank patterns by confidence (occurrence count) and propose next action for each.

**Step 3** — Surface proposed guardrails and brain updates, gated on user approval.

**Step 4** — Write approved guardrails to `/context/meta-patterns.md` and approved brain updates to `/foundation/brain.md`. Log the session.

---

## Trigger

- **When:** Detecting patterns across 2+ prior sessions logged by other skills, and turning confirmed patterns into guardrails or brain updates.
- **Not for:** Real-time feedback during a session — execution skills already check `/context/meta-patterns.md` at their own Step 0. Auditing a single skill's output quality → use `meta-review`. One-off pattern lookups — this skill's value is in running it repeatedly.
- **Example prompts:**
  - "run meta-synthesis"
  - "what patterns are emerging"
  - "detect cross-skill signals"
  - "update guardrails"
  - "compound our learnings"
  - "what should we remember"

---

## Inputs

- **Args:** Timeframe to analyze — all sessions, or a specific window (e.g. last 30 days). Asked in Step 0 if not specified.
- **Defaults:** All sessions in `/context/skill-sessions.md` if no timeframe is given.
- **Context keys:**
  - `/context/skill-sessions.md` — required. The session log every execution skill writes to.
  - `/context/meta-patterns.md` — optional; loaded if it exists, treated as empty otherwise.
  - `/foundation/brain.md` — optional; Sections 1-6 loaded silently as baseline context for proposed updates.
  - **Brain contract:** Reads Sections 1-6. Writes: Section named in an approved brain-update proposal only, after explicit user approval (Step 3).

---

## Pre-flight

- Load `/context/skill-sessions.md` — see Step 0.
- **Hard block:** if `/context/skill-sessions.md` is missing or has zero rows, stop and tell the user there's nothing to synthesize yet.
- Load `/context/meta-patterns.md` and `/foundation/brain.md` if they exist — see Step 0.

---

## Steps

### Step 0 — Pre-Flight

Load:
- `/context/skill-sessions.md` — required. If missing or has zero rows, stop and tell the user there's nothing to synthesize yet.
- `/context/meta-patterns.md` — load if it exists; if missing, treat as empty (this run may create it).
- `/foundation/brain.md` — load Sections 1-6 silently, as baseline context for any proposed updates.

Ask, if not specified: "Look at all sessions, or a specific timeframe (e.g. last 30 days)?" Default: all sessions in the log.

---

### Step 1 — Scan for Repeated Patterns

Read every row in `/context/skill-sessions.md` for the chosen timeframe. Group by two lenses:

**Within one skill** — the same issue showing up 2+ times in sessions from the same skill (e.g. `retro` logging "champion alignment gap" in two different launches).

**Across skills** — the same underlying issue showing up in sessions from 2+ different skills (e.g. `pre-mortem` flags a risk that `retro` later confirms happened). Cross-skill patterns are the ones most worth turning into a guardrail, since they're not visible from inside any single skill.

For each candidate pattern, capture: what it is in one sentence, which sessions it appeared in (skill + date), and how many times.

---

### Step 2 — Rank and Recommend

Classify each pattern by occurrence count:

| Occurrences | Confidence | Recommended action |
|---|---|---|
| 3+ | High | Propose as a guardrail — ready to surface to execution skills at their own Step 0 |
| 2 | Medium | Propose as a guardrail, flagged "watch" rather than "confirmed" |
| 1 | Low | Note only — not enough evidence yet, don't propose anything |

If a pattern points at something durable about the business rather than a process gap — a buying trigger, a market shift, a proof point that keeps landing — propose it as a brain update instead of a guardrail, naming the exact section (2 ICP, 5 Market Context, 6 Proof Points) it belongs in.

---

### Step 3 — Propose and Gate

Surface every High and Medium confidence pattern together, in one message, for approval:

```
🔁 PATTERNS FROM /context/skill-sessions.md

1. [Pattern name] — HIGH confidence (4 occurrences: 2 retros, 2
   pre-mortems, dates [list])
   Proposed: add guardrail to /context/meta-patterns.md:
   "[exact guardrail text]"

2. [Pattern name] — MEDIUM confidence (2 occurrences: [dates])
   Proposed: add guardrail (watch status):
   "[exact guardrail text]"

3. [Pattern name] — durable signal, not a process gap
   Proposed: brain update, Section [N]:
   "[exact text]"

Approve all / approve some (name which) / reject all?
```

Never write anything without this gate. If the user rejects a pattern, log it as rejected with the reason and move on — don't re-propose it next run unless new occurrences push it to a higher confidence tier.

---

### Step 4 — Write and Log

For each approved item:
- Guardrail → append to `/context/meta-patterns.md` with the pattern text, occurrence count, and date added.
- Brain update → write to the named section of `/foundation/brain.md`, showing the exact before/after, same confirmation standard as every other skill that writes to the brain.

Log this session to `/context/skill-sessions.md`:

```yaml
skill: meta-synthesis
session_date: [YYYY-MM-DD]
sessions_analyzed: [count]
timeframe: [all / last N days]
patterns_found:
  high_confidence: [count]
  medium_confidence: [count]
guardrails_proposed: [count]
guardrails_approved: [count]
brain_updates_proposed: [count]
brain_updates_approved: [count]
```

Close by telling the user plainly what changed: how many guardrails are now live, what the brain updates were, and what's worth watching next time (the Low-confidence, single-occurrence notes from Step 1).

---

## Outputs

- **Files written:** `/context/meta-patterns.md` — approved guardrails
  appended (Step 4). `/foundation/brain.md` — approved updates written to
  the named section (Step 4). `/context/skill-sessions.md` — one appended
  row per session (Step 4).
- **Chat output format:** Numbered list of proposed patterns with
  confidence tier and exact guardrail/brain-update text (Step 3), followed
  by a plain-language close summarizing what changed (Step 4).
- **External side effects:** None beyond the three files above, and only
  after explicit user approval.

---

## Verification

- `/context/skill-sessions.md` has at least one row before proceeding past Step 0.
- Every candidate pattern classified by occurrence count (Step 2).
- No guardrail or brain update written without explicit approval shown as exact text first (Step 3).
- Rejected patterns logged with reason, not silently dropped (Step 3).
- Session logged to `/context/skill-sessions.md` (Step 4).

---

## Operating Rules

- **Session log is the only input.** No integrations, no scheduler, no separate memory store — everything this skill needs, every other skill already writes to `/context/skill-sessions.md`.
- **2+ occurrences minimum to propose anything.** A single session is an anecdote, not a pattern.
- **Cross-skill patterns take priority.** They're invisible from inside any one skill, which is the entire reason this skill exists.
- **Every write is gated.** No guardrail or brain update happens without explicit approval, shown as exact text before it's written.
- **Rejected patterns aren't silently dropped.** Log the rejection so the same pattern isn't re-proposed next run without new evidence.
- **Durable signals go to the brain, not a guardrail.** A pattern about the business itself (buying trigger, market shift, proof point) is a brain update, not a process guardrail.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Session log loaded | `/context/skill-sessions.md` parsed, ≥1 row |
| Patterns ranked | Every candidate classified High/Medium/Low by occurrence count |
| Cross-skill patterns flagged | Patterns spanning 2+ skills marked as priority |
| Proposals gated | All guardrails and brain updates shown for approval before writing |
| Session logged | Metadata appended to `/context/skill-sessions.md` |

---

## Do Not Use For

- **Real-time feedback during a session** — execution skills already check `/context/meta-patterns.md` at their own Step 0
- **Auditing a single skill's output quality** — use `meta-review`
- **One-off pattern lookups** — this skill's value is in running it repeatedly, not as a single query tool
