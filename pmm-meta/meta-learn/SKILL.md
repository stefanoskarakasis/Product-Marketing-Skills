---
name: meta-learn
version: 1.0.0
description: >
  Centralised post-session learning engine. Runs after any PMM skill session to
  extract patterns, route them to the correct knowledge files, and maintain a shared
  intelligence layer that compounds across all skills. Trigger on: "capture what we
  learned", "log this session", "save the learnings", "run learn", "what did we learn
  from this session", or any request to record, encode, or compound insights from a
  completed skill session.

metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-06-06
---

# meta-learn

The compound interest mechanism for the skill repo. Runs after any skill session,
extracts what was observed, routes patterns to the right knowledge files, and
ensures every future session of any skill is sharper than the last.

Without this: patterns decay in skill-specific silos and never compound across the
system. With this: your tenth pre-mortem is measurably smarter than your first —
and so is your tenth retro, GTM brief, and beachhead assessment.

---

## Trigger

- **When:** At the end of any skill session where output was produced — especially
  after `pre-mortem`, `go-to-market-strategy`, `retro`, `beachhead-segment`,
  `gaccs-brief`, `stakeholder-maps`, `positioning-messaging`, `pmm-okrs`.
- **Not for:** Running mid-session — patterns extracted before a session closes are
  incomplete. Starting a skill session → that's the skill's job. Reviewing skill
  file quality → use `meta-review`. Checking skill output quality → use `meta-verify`
  (when built).
- **Example prompts:**
  - "Run learn on this session"
  - "Capture what we learned from this retro"
  - "Log the patterns from this GTM strategy session"
  - "/learn"
  - "Save the learnings before we close"

---

## Inputs

- **Args:** Skill name (optional) + session summary or full session output.
  If no session content provided, ask the three extraction questions directly.
- **Defaults:** If skill name not stated, infer from session content. If session
  content not provided, prompt for it before extracting.
- **Context keys:**
  - `knowledge/global/rules.md` — load before routing. Cross-skill confirmed rules
    applied by default to all future sessions.
  - `knowledge/global/hypotheses.md` — load before routing. Check if today's session
    confirms or contradicts any open hypothesis.
  - `knowledge/INDEX.md` — load to identify which domain folders exist and route
    new patterns correctly.
  - `sessions/log.md` — append session summary after every run.
  - n.v.t. — no brain file. This skill is context-agnostic by design. It operates
    on session content, not company context.

---

## Pre-flight

- Load `knowledge/INDEX.md` — identify existing domain folders before routing.
  If INDEX.md doesn't exist: create it silently. System builds from session one.
- Load `knowledge/global/rules.md` — check if any global rule is testable today.
- Load `knowledge/global/hypotheses.md` — note any open hypothesis this session
  could confirm or contradict.
- If no session content provided: ask for it before proceeding. Never extract
  patterns from an empty or incomplete session.
- This skill is **context-agnostic**. Do not load `/foundation/brain.md`.
  Patterns must be observable from session content alone — not inferred from
  company context.

---

## Steps

### Step 1: Ask the Three Extraction Questions

Always ask all three in one message. Do not skip any.

> "Before we close, three questions:
>
> 1. **What surprised you?** Something the skill surfaced that you hadn't considered
>    before this session — a risk, a pattern, a reframe.
>
> 2. **What was wrong or off?** Any recommendation you pushed back on, overrode, or
>    felt was missing the mark. Be specific.
>
> 3. **What was missing?** A gap the skill couldn't fill that you had to work around
>    — context it didn't have, a question it didn't ask, an output it didn't produce."

Wait for answers. Do not proceed to extraction until all three are answered.
If the user says "nothing" to all three: confirm once, then close without writing.
A session with no learnings is valid — do not force patterns.

---

### Step 2: Extract Patterns

From the three answers, extract 1–3 observations. For each observation:

- State it as a specific, falsifiable pattern — not a vague direction.
  - ❌ "The skill could be clearer on tier assignment"
  - ✅ "When the user has no launch history in brain Section 7, tier assignment
    defaults to conservative (T3) even when initiative signals point to T2"

- Classify the observation:
  - **New hypothesis** — observed once, needs confirmation
  - **Hypothesis confirmation** — matches an existing open hypothesis
  - **Hypothesis contradiction** — conflicts with an existing hypothesis or rule
  - **Skill gap** — structural missing piece in the skill itself
  - **User pattern** — recurring behaviour or mistake from the user, not the skill

- Identify the correct domain for routing (see Step 3).

---

### Step 3: Route to Correct Knowledge Files

Route each pattern to the domain that matches the skill it came from:

| Source skill | Domain folder |
|---|---|
| `go-to-market-strategy` | `knowledge/gtm/` |
| `retro` | `knowledge/gtm/` |
| `beachhead-segment` | `knowledge/segments/` |
| `pre-mortem` | `knowledge/risk/` |
| `positioning-messaging` | `knowledge/positioning/` |
| `stakeholder-maps` | `knowledge/stakeholders/` |
| `gaccs-brief` | `knowledge/briefs/` |
| `pmm-okrs` | `knowledge/okrs/` |
| `experiment-doc` | `knowledge/experiments/` |
| `workflow-orchestrator` | `knowledge/workflows/` |
| Cross-skill (affects 2+ skills) | `knowledge/global/` |
| Skill structure / behaviour | `knowledge/meta/` |

Within each domain, route to the correct file:
- `hypotheses.md` — new or updated hypotheses
- `rules.md` — confirmed rules (promotion requires explicit approval)
- `knowledge.md` — factual patterns and observations

---

### Step 4: Apply Promotion and Demotion Logic

**Hypothesis → Rule:** When an hypothesis has been confirmed in 3+ independent
sessions (different users or different initiatives), propose promotion to `rules.md`.
Never auto-promote. Surface as a Self-Improvement Trigger and wait for approval.

**Rule → Hypothesis:** When new session data directly contradicts a confirmed rule,
propose demotion to `hypotheses.md` with a note on what contradicted it.

**Stale hypothesis:** If a hypothesis has not been tested in 90+ days, flag it for
review rather than carrying it forward silently.

Surface all proposed changes before writing:

```
🔁 SELF-IMPROVEMENT TRIGGER
Observation: [specific pattern from this session]
Classification: [New hypothesis / Confirmation / Contradiction / Skill gap / User pattern]
Proposed write: [exact text to add or change]
Location: [file path]
Action: [Add to hypotheses.md / Promote to rules.md / Demote to hypotheses.md / Update knowledge.md]
Awaiting approval before encoding.
```

Never encode without explicit user approval.

---

### Step 5: Log the Session

After all approved writes are complete, append to `sessions/log.md`:

```markdown
## Session: [Skill name] — [YYYY-MM-DD]
**Trigger:** [What the user was trying to do]
**Output:** [What the skill produced — one line]
**Patterns extracted:** [N]
**Writes approved:** [list of files written]
**Writes declined:** [list of declined triggers]
**Open hypotheses updated:** [Y/N — which ones]
**Global rules applied:** [Y/N — which ones]
**Next check:** [Any hypothesis with a validation deadline]
```

---

## Outputs

- **Files written:** `knowledge/[domain]/hypotheses.md` — new and updated hypotheses
  on approval. `knowledge/[domain]/rules.md` — promoted rules on approval.
  `knowledge/[domain]/knowledge.md` — factual observations on approval.
  `knowledge/global/` — cross-skill patterns on approval.
  `sessions/log.md` — session summary appended automatically (no approval needed).
  `knowledge/INDEX.md` — updated if new domain folders created.
- **Chat output format:** Three extraction questions → pattern proposals in
  Self-Improvement Trigger format → session log entry. All writes shown before
  executing — never silent.
- **External side effects:** n.v.t.

---

## Verification

- All three extraction questions asked and answered before extraction begins.
- Every pattern stated as a specific, falsifiable observation — not a direction.
- Every pattern routed to the correct domain folder.
- Promotion and demotion proposals surfaced as Self-Improvement Triggers.
- No write executed without explicit user approval (except `sessions/log.md`).
- Session log appended after every run.
- Stale hypotheses (90+ days untested) flagged before closing.

---

## Do Not Use For

- **meta-review** — for auditing SKILL.md files against SKILL-SPEC. `meta-learn`
  captures session patterns; `meta-review` checks file structure.
- **meta-verify** — for checking skill output quality on a specific run. `meta-learn`
  captures what was learned; `meta-verify` checks whether the output was correct.
- **Individual skill self-improvement loops** — those run within a skill session.
  `meta-learn` runs after the skill session closes, captures the broader pattern,
  and routes it to the shared knowledge layer.
- **Starting a session** — this skill closes sessions, it doesn't open them.

---

## Commands

### /learn
Run the full learning session for the most recent skill output. Asks the three
extraction questions, proposes patterns, routes on approval.

```
/learn
/learn retro
/learn go-to-market-strategy
```

---

### /learn-history
Show what's been captured in the knowledge base. Filter by domain or skill.

```
/learn-history
/learn-history gtm
/learn-history global
```

Output:
```
## Knowledge Base Summary
Last updated: [date]

knowledge/gtm/
  rules.md      — [N] confirmed rules
  hypotheses.md — [N] open hypotheses ([N] stale)
  knowledge.md  — [N] observations

knowledge/global/
  rules.md      — [N] confirmed cross-skill rules
  hypotheses.md — [N] open cross-skill hypotheses

Sessions logged: [N total] | Last: [date] | Skill: [name]
```

---

### /learn-review
Audit the knowledge base for stale hypotheses, contradicted rules, and patterns
that haven't been tested recently. Produces a prioritised review list.

```
/learn-review
/learn-review hypotheses
/learn-review rules
```

Output:
```
## Knowledge Base Review — [date]

🔴 Stale hypotheses (90+ days untested):
- [H-ID] in knowledge/[domain]/ — last tested [date]

⚠️ Rules worth challenging (3+ sessions since last confirmation):
- [R-ID] in knowledge/[domain]/ — confirmed [N] times, last [date]

✅ Active and healthy:
- [N] hypotheses being actively tested
- [N] rules applied in last 30 days
```

---

### /learn-promote [hypothesis-id]
Manually propose promotion of a specific hypothesis to a rule. Useful when you've
confirmed a pattern outside a `meta-learn` session.

```
/learn-promote H-007
```

---

## Operating Rules

- **Three questions, always.** Never skip an extraction question. Partial extraction
  produces partial patterns.
- **Specific and falsifiable.** Vague patterns are worse than no patterns — they
  accumulate noise and inflate confidence. Every observation must be specific enough
  to be proved wrong.
- **Never encode without approval.** The only automatic write is `sessions/log.md`.
  Everything else requires explicit confirmation.
- **Route to domain, not skill.** Patterns belong to the domain they inform, not
  the skill they came from. A GTM tier calibration pattern from `retro` goes to
  `knowledge/gtm/`, not `knowledge/retro/`.
- **Global patterns are the highest-value output.** When a pattern applies across
  two or more skills, route it to `knowledge/global/`. These compound fastest.
- **Promotion requires 3 confirmations.** One or two observations is a hypothesis.
  Three independent confirmations is a rule candidate. Never lower this threshold.
- **Stale hypotheses decay.** Flag anything untested for 90+ days. Don't carry
  forward hypotheses that have never been tested — they're assumptions, not patterns.
- **A session with no learnings is valid.** Don't force patterns. If nothing
  surprising, wrong, or missing occurred — close cleanly and log it.
- **Context-agnostic by design.** Do not load brain file. Patterns must be
  observable from session content alone. Company-specific context contaminates
  cross-session learning.
- **Index must stay current.** Update `knowledge/INDEX.md` whenever a new domain
  folder is created. A domain that's not indexed won't be loaded by other skills.

---

## Quality Gate

Runs after pattern proposals, before any write.

| Check | Standard | Pass = |
|---|---|---|
| Three questions answered | All three extraction questions completed | Yes |
| Patterns specific | Each observation falsifiable, not directional | Yes |
| Routing correct | Each pattern in the right domain folder | Yes |
| Trigger format used | All proposals use Self-Improvement Trigger format | Yes |
| No silent writes | Every write shown before executing | Yes |
| Session log appended | `sessions/log.md` updated before closing | Yes |
| Stale check run | Hypotheses 90+ days old flagged | Yes |
| Global patterns identified | Cross-skill patterns routed to `knowledge/global/` | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load `knowledge/INDEX.md` — identify all domains and existing files.
2. Load `knowledge/global/rules.md` — note any cross-skill rule testable today.
3. Load `knowledge/global/hypotheses.md` — note any open hypothesis this session
   could confirm or contradict.

### After every session:
1. Check if any global hypothesis was tested today — update confidence count.
2. If any rule was contradicted — propose demotion before closing.
3. If `meta-learn` itself produced a bad output or missed a pattern — log as
   skill gap to `knowledge/meta/hypotheses.md`.

```
🔁 SELF-IMPROVEMENT TRIGGER
Observation: [what was observed about meta-learn itself]
Proposed update: [exact change to SKILL.md]
Location: pmm-meta/skills/meta-learn/SKILL.md
Awaiting approval before encoding.
```

---

## Changelog

### v1.0.0 — 2026-06-06
Initial build. Third skill in `pmm-meta` plugin alongside `meta-review`.

Architecture decisions:
- Context-agnostic: no brain file. Patterns must be observable from session content
  only. Company context contaminates cross-session learning.
- Three fixed extraction questions — standardised across all skills for comparability.
- Domain routing table — patterns routed by subject, not by source skill.
- Global knowledge layer — cross-skill patterns compound fastest and are highest value.
- Promotion threshold: 3 independent confirmations required. Never lower this.
- Only automatic write is `sessions/log.md` — everything else requires approval.
- Commands: /learn, /learn-history, /learn-review, /learn-promote.
