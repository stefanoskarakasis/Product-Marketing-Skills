---
name: meta-learn
version: 2.0.0
description: >
  Compound learning engine with auto-trigger, smart routing, and hypothesis tracking.
  Runs after any PMM skill session to extract patterns, detect cross-skill signals,
  confirm/contradict open hypotheses, and route learnings to the correct knowledge files.
  Auto-detects skill completion, routes to domain-specific or global knowledge base,
  tracks confidence, and compounds learnings across all skills. Trigger on: "capture
  what we learned", "log this session", "save the learnings", "run learn", "what did
  we learn", or any request to encode insights from a completed skill session.

metadata:
  author: Stefanos Karakasis
  version_history: "1.0.0 → 2.0.0 (added auto-trigger, smart routing, hypothesis tracking)"
  context: context-agnostic
  quality_gate: true
  phase: "1B"
last_updated: 2026-07-21
---

# Meta-Learn v2.0.0

The compound intelligence layer. Every skill session teaches the system something.
This skill ensures learnings compound across skills, hypotheses get confirmed/contradicted,
patterns get routed to the right place, and your tenth session is measurably smarter
than your first.

**New in v2.0.0:**
- Auto-trigger detection (recognizes when skill session ends)
- Smart routing (cross-skill pattern detection, domain classification)
- Hypothesis tracking (open questions from prior sessions confirmed or contradicted)
- Confidence scoring (patterns ranked by evidence strength)
- Self-improvement trigger detection (patterns that should become guardrails)
- Approval gates (when to ask user vs. auto-write to knowledge base)

---

## Trigger

**Auto-Trigger Mode (Primary):**
- After any PMM skill session with output, meta-learn runs automatically
- Detects: skill name, session start/end time, outputs produced
- Does NOT trigger: mid-session reviews, skill file quality checks (use meta-review),
  output quality checks (use meta-verify)

**Manual Trigger (Secondary):**
- User says: "run learn", "/learn", "capture learnings", "log this session"
- User provides: session summary + skill name + outputs

**No Trigger:**
- Sessions with no output ("we just talked through it")
- Skill startup/pre-flight (not a closed session yet)
- Skill iterations (only after final output)

---

## Inputs

**Auto-Trigger Detection:**
- Skill name (extracted from execution context)
- Session start/end timestamps
- Session outputs (documents, briefs, decisions)
- User feedback on outputs (if provided)

**Manual Trigger Inputs:**
- Session content (description or paste)
- Skill name (if not obvious)
- User's three extraction answers (below)

**Context Files (Pre-Flight Load):**
- `/config/routing.yml` — domain map, cross-skill signal rules
- `/config/hypothesis-tracking.yml` — open hypotheses, confirmation criteria
- `/config/approval-gates.yml` — when user approval needed
- `/knowledge/INDEX.md` — existing domains and file locations
- `/knowledge/global/rules.md` — confirmed cross-skill rules
- `/knowledge/global/hypotheses.md` — open questions
- `/sessions/log.md` — append session summary (automatic write)

**NOT loaded:** `/foundation/brain.md` (context-agnostic design)

---

## Pre-Flight (Step 0)

1. **Load config files** (routing.yml, hypothesis-tracking.yml, approval-gates.yml)
2. **Load knowledge index** (INDEX.md — where does this pattern go?)
3. **Load global rules** (what cross-skill patterns already exist?)
4. **Load open hypotheses** (what questions from prior sessions could this confirm?)
5. **Detect skill name** (from execution context or user input)
6. **Confirm session closed** (outputs produced and session end detected)
7. **Gate pass:** If no session content, ask user for it before proceeding

---

## Steps

### Step 1: Auto-Detect Skill Completion (30 sec)

**What:** Determine if a skill session has actually ended.

**How:**
- Check execution context for skill name, start time, end time
- Verify outputs exist (document, brief, decisions, etc.)
- If outputs missing: ask user "Did the skill session complete?"
- If outputs present: proceed

**Output:** Confirmed skill name + session duration + list of outputs produced

**Example:**
```
Detected: meta-review session (15 min)
Outputs: 3 quality scores, 1 fix recommendation
Session: complete ✓
```

---

### Step 2: Ask the Three Extraction Questions

**What:** Capture what the user learned that the skill didn't explicitly surface.

**How:** Ask all three in one message. Wait for complete answers before proceeding.

> "Before we close, three quick questions:
>
> 1. **What surprised you?** Something unexpected — a risk, a pattern, an insight the skill surfaced that you hadn't considered before.
>
> 2. **What was wrong or off?** Any recommendation you pushed back on, disagreed with, or felt was missing the mark. Be specific: what and why?
>
> 3. **What was missing?** A gap — context the skill didn't have, a question it didn't ask, an output it didn't produce that would have been valuable."

**Gate:** If all three answered as "nothing", proceed to Step 6 (clean close). If any have content, proceed to Step 3.

---

### Step 3: Extract Patterns & Classify (2 min)

**What:** Turn answers into specific, falsifiable patterns.

**How:**

For each answer that isn't "nothing":
1. **Restate specifically** — "You said [exact quote]. Let me sharpen this..."
2. **Make falsifiable** — If vague ("better communication"), reframe as testable:
   - ❌ Vague: "We should communicate better about milestones"
   - ✅ Falsifiable: "When timeline changes >10 days, notify stakeholders within 24h OR deals slip"
3. **Classify as:**
   - **New Pattern** — First time observed
   - **Confirmed Hypothesis** — Matches open hypothesis (see Step 4)
   - **Contradicts Hypothesis** — Disproves open hypothesis
   - **Skill Gap** — Patterns about what the skill missed (route to meta/gaps)
   - **Cross-Skill Signal** — Appears in 2+ skill domains (route to global/rules)

**Output format:**
```
Pattern 1: [Falsifiable statement]
  Surprise/Wrong/Missing: [Which question it came from]
  Classification: New Pattern / Hypothesis Confirmation / Cross-Skill Signal / Skill Gap
  Confidence: High / Medium / Low (based on evidence)
  Source: [Skill name + domain]
```

**Example:**
```
Pattern 1: "When champion sentiment is declining (2+ signals in Gong), deal velocity slows 40%"
  From: Wrong (skill didn't flag declining champion as deal risk)
  Classification: Cross-Skill Signal (seen in GTM-strategy + pre-mortem + gaccs-brief)
  Confidence: High (4 occurrences, spans 3 domains)
  Recommendation: Add "champion sentiment" monitor to /knowledge/global/deal-signals
```

---

### Step 4: Check Open Hypotheses (1 min)

**What:** Does this session confirm or contradict any open hypothesis?

**How:**
1. Load `/knowledge/global/hypotheses.md`
2. For each pattern from Step 3, scan for matches
3. If match found: note confirmation status
   - ✅ **Confirms** — Additional evidence for hypothesis
   - ❌ **Contradicts** — Evidence against hypothesis
   - ⚠️ **Partially confirms** — Evidence for one aspect, not others
4. If no match: note as new hypothesis candidate

**Output:**
```
Hypothesis Check:
  Open H1: "Beachhead ICP wins faster with champion alignment"
    Status: CONFIRMED (pre-mortem session observed 3 deals lost due to weak champion)
    Evidence strength: ↑↑ (now 6 total confirmations)
    Confidence: HIGH (was MEDIUM)
    Action: Move to /knowledge/global/rules.md (threshold: 5+ confirmations ✓)

  Open H2: "Pricing elasticity varies by segment"
    Status: NO DATA THIS SESSION (pre-mortem doesn't touch pricing)
    Confidence: Still MEDIUM
    Action: Continue tracking, need more evidence
```

---

### Step 5: Route Pattern to Correct Knowledge File (1 min)

**What:** Decide where this pattern belongs.

**How:**
1. Load `/config/routing.yml` — domain map
2. For each pattern, determine primary domain:
   - **Single-domain** (Pre-mortem-specific) → `/knowledge/pre-mortem/[pattern-name].md`
   - **Cross-domain** (appears in 2+ skills) → `/knowledge/global/[pattern-name].md`
   - **Skill gap** (something the skill missed) → `/knowledge/meta/skill-gaps/[skill-name].md`

3. If domain folder doesn't exist: create it (system builds incrementally)

**Logic from config/routing.yml:**
```yaml
domains:
  beachhead:
    skills: [beachhead-segment, positioning-messaging]
    patterns_file: /knowledge/beachhead/
    cross_skill_threshold: 2  # If seen in 2+ domains, escalate to global
  gtm:
    skills: [go-to-market-strategy, gaccs-brief]
    patterns_file: /knowledge/gtm/
    cross_skill_threshold: 2
  sales:
    skills: [competitive-battlecard, retro]
    patterns_file: /knowledge/sales/
    cross_skill_threshold: 2
  global:
    patterns_file: /knowledge/global/  # Cross-skill, high-impact
    rules_file: /knowledge/global/rules.md
    hypotheses_file: /knowledge/global/hypotheses.md
```

**Output:**
```
Routing Decision:
  Pattern 1 (champion sentiment → deal velocity): 
    Domains touched: GTM + Sales + Pre-mortem = 3 skills
    Decision: ROUTE TO GLOBAL (cross_skill_threshold=2, met)
    File: /knowledge/global/deal-signals.md
    
  Pattern 2 (beachhead ICP pain ≠ beachhead pain):
    Domains touched: Beachhead-segment only = 1 skill
    Decision: ROUTE TO DOMAIN (beachhead)
    File: /knowledge/beachhead/ica-pain-alignment.md
```

---

### Step 6: Detect Self-Improvement Triggers (1 min)

**What:** Identify patterns that should become guardrails or skill improvements.

**How:**
1. Check if pattern appears in `/context/meta-patterns.md` (guardrails)
2. If pattern has 2+ occurrences across sessions → FLAG FOR GUARDRAIL PROMOTION
3. If pattern identifies a skill gap → FLAG FOR SKILL UPDATE
4. If pattern contradicts existing rule → FLAG FOR RULE REWRITE

**Output:**
```
Self-Improvement Flags:

GUARDRAIL PROMOTION:
  Pattern: "Champion misalignment kills deals"
  Current status: Guardrail exists (added 3 weeks ago, triggered 4x)
  Recommendation: PROMOTE from MEDIUM to HIGH confidence
  Action: Update /context/meta-patterns.md confidence level

SKILL GAP FOUND:
  Pattern: "Pre-mortem doesn't ask about champion alignment pre-execution"
  Affected skill: meta-review
  Recommendation: Add question to pre-mortem Step 8
  Action: Route to meta-review improvement queue

HYPOTHESIS → RULE:
  Pattern: "Beachhead pain must match buyer pain" confirmed 6x
  Recommendation: Graduate from hypothesis to confirmed rule
  Action: Move to /knowledge/global/rules.md
```

---

### Step 7: Proposal + Approval Gate (2 min)

**What:** Show user exactly what will be written, request approval (if needed).

**How:**
1. Load `/config/approval-gates.yml` — approval rules
2. Determine: Auto-write or ask approval?
   - **Auto-write:** Routine pattern to existing file (no threshold crossed)
   - **Ask approval:** New file, contradicts existing rule, or guardrail promotion
3. If approval needed: show exact text that will be written
4. Wait for explicit approval before writing

**Example approval request:**
```
APPROVAL NEEDED:

I'm about to write this pattern to /knowledge/global/deal-signals.md:

---
# Champion Sentiment as Deal Velocity Predictor
**Pattern:** When champion sentiment is declining (2+ signals in Gong), 
deal velocity slows 40% on average.
**Evidence:** 4 confirmations (GTM-brief + pre-mortem + gaccs-brief + retro)
**Confidence:** HIGH
**Recommendation:** Add "champion sentiment" monitor to all deal forecasts
**Action threshold:** If declining, escalate to champion management conversation within 48h
---

OK to write? (yes / no / edit)
```

**Approval gates from config:**
```yaml
approval_gates:
  auto_write:
    - adding to existing file (same pattern type)
    - routine session log entry
    - updating hypothesis confidence (same status)
  
  require_approval:
    - new file creation
    - contradicts existing rule
    - guardrail promotion (MEDIUM → HIGH)
    - hypothesis → rule graduation
    - cross-skill signal (first time in global)
```

---

### Step 8: Write to Knowledge Base (1 min)

**What:** Persist patterns to knowledge files.

**How:**
1. If user approved (or auto-write gate passed): write
2. If user said "no": don't write, offer to refine
3. Append mode for logs, overwrite for specific patterns
4. Format: Markdown, include evidence, date, source skill, confidence

**Files written:**
- `/knowledge/[domain]/[pattern].md` — Pattern documentation
- `/knowledge/global/rules.md` — Append confirmed cross-skill rules
- `/knowledge/global/hypotheses.md` — Update hypothesis status + confidence
- `/context/meta-patterns.md` — Update guardrail confidence if triggered
- `/sessions/log.md` — Append session summary (automatic, no approval needed)

**Format example:**
```markdown
# Pattern: Champion Sentiment → Deal Velocity
**Date:** 2026-07-21  
**Skill Source:** meta-review, go-to-market-strategy, gaccs-brief  
**Confidence:** HIGH (4 confirmations)  
**Evidence:** 4 sessions across 3 skill domains flagged this  

## Pattern Statement
When champion sentiment is declining (2+ signals from Gong), deal velocity slows 40%.

## Why This Matters
Deal risk isn't just about price or product fit. Champion engagement is a leading indicator
of deal health. Declining sentiment predicts slower close by 4-6 weeks.

## Actionable Recommendation
When Gong flags declining champion sentiment:
1. Schedule champion alignment call within 48h
2. Review deal assumptions with champion
3. Escalate to sales leadership if sentiment doesn't recover in 1 week

## Sources
- Session 1 (2026-07-15, go-to-market-strategy): Sales team noted champion disengagement
- Session 2 (2026-07-18, pre-mortem): Pre-mortem identified champion as kill-risk
- Session 3 (2026-07-20, gaccs-brief): Messaging assumption: champion is champion ✓

**Next update:** TBD (hypothesis tracking will update if more confirmations)
```

---

### Step 9: Update Global Hypothesis File (1 min)

**What:** Record which hypotheses were confirmed/contradicted this session.

**How:**
1. Update `/knowledge/global/hypotheses.md` with:
   - Hypothesis name
   - Confirmation status (CONFIRMED / CONTRADICTED / PARTIAL)
   - New evidence count
   - Confidence level change
   - Recommendation (keep tracking / promote to rule / close)

**Example entry:**
```markdown
## H3: Champion Alignment Predicts Deal Velocity
**Status:** CONFIRMED (added 1 more confirmation)  
**Evidence count:** 6 total  
**Confidence:** HIGH (was MEDIUM)  
**Last updated:** 2026-07-21  
**Recommendation:** GRADUATE TO RULE (threshold met: 5+ confirmations ✓)  
**Action:** Move to /knowledge/global/rules.md on next synthesis cycle
```

---

### Step 10: Log Session (1 min)

**What:** Record this session in the historical log.

**How:**
1. Append to `/sessions/log.md`
2. Include: date, skill, duration, patterns extracted, hypothesis updates, writes approved
3. Format: CSV or markdown table for easy trending

**Example:**
```markdown
| Date | Skill | Duration | Patterns | Hypotheses Updated | Writes | Quality Score |
|------|-------|----------|----------|-------------------|--------|---------------|
| 2026-07-21 | go-to-market-strategy | 18 min | 3 new | H3 confirmed | ✓ global/deal-signals | 87/100 |
| 2026-07-20 | pre-mortem | 25 min | 1 new, 2 confirm | H1, H3 confirmed | ✓ beachhead/ica-pain | 91/100 |
```

**Auto-logged (no approval):** Every session generates a log entry regardless of patterns.

---

### Step 11: Detect Compounding (30 sec)

**What:** Identify if this session's learnings compound with prior sessions.

**How:**
1. Check: Does this pattern appear in prior session logs (last 30 days)?
2. If yes: Note as "pattern strengthened" (confidence increases)
3. Count: How many times has this specific pattern been confirmed?
4. Threshold check: If confirmed 3+ times → flag for guardrail promotion

**Output:**
```
Compounding Check:
  Pattern: "Champion alignment → deal velocity"
  Prior observations: 2 (in last 30 days)
  Today: 1 new confirmation
  Total now: 3 confirmations
  Threshold: 2 (for cross-skill awareness), 5 (for guardrail promotion)
  Status: CROSS-SKILL RULE READY (next synthesis cycle, promote confidence)
```

---

### Step 12: Close & Surface Next Action (1 min)

**What:** Confirm all writes, show what changed, suggest next step.

**How:**
1. Summarize: Patterns extracted, files written, hypotheses updated
2. Show impact: How many files changed? Which guardrails promoted?
3. Suggest next: "This pattern might affect [next skill session]"
4. Link to meta-synthesis: "Your 24h synthesis cycle will compound this learning"

**Example:**
```
✓ Session complete.

Captured:
  - 3 new patterns extracted
  - 1 hypothesis confirmed (H3 champion-alignment)
  - 2 files written (global/deal-signals.md, beachhead/ica-pain-alignment.md)
  - 1 guardrail promoted (champion-alignment: MEDIUM → HIGH)

Impact:
  - Your next GTM strategy session will load this champion-alignment guardrail
  - Your next beachhead session will avoid the ICP-pain mismatch
  - Next 24h meta-synthesis will see 6 total confirmations of H3 → graduates to rule

Suggested next action:
  "Before your next deal review, check: is your champion aligned on positioning?"
```

---

## Operating Rules

1. **Extract first, decide second.** Always ask the three questions before classifying patterns. Don't assume.

2. **Route by evidence, not intuition.** Use `/config/routing.yml` domain map. If pattern touches 2+ skill domains, it's global (not domain-specific).

3. **Hypothesis confirmation is stricter than pattern extraction.** Need explicit match to existing hypothesis, not inference.

4. **Approval gates prevent bad writes.** Never write a pattern that contradicts an existing rule without user approval.

5. **Compounding is the goal.** If pattern appears 2+ times, flag it. If 5+ times, it becomes a guardrail. This is how the system gets smarter.

6. **Skill gaps route to meta/improvements.** If the skill missed something, don't add it to domain knowledge — flag it for skill review instead.

7. **Context-agnostic extraction.** Patterns come from session content alone. Do NOT load /foundation/brain.md and infer context.

8. **Never force patterns.** If user says "nothing surprised me", accept that. Log the session and close cleanly.

9. **Logging is automatic.** Every session gets logged to /sessions/log.md regardless of patterns. This is the historical record.

10. **Confidence compounds.** Track how many times each pattern has been confirmed. Confidence increases with repetition (MEDIUM → HIGH after 3 confirmations, becomes guardrail after 5).

---

## Quality Gate

Before finalizing any write, verify:

- [ ] All three extraction questions answered
- [ ] Patterns are specific and falsifiable (not vague)
- [ ] Routing decision matches domain map (config/routing.yml)
- [ ] Hypothesis check completed (confirmed/contradicted/no-match)
- [ ] Approval gate assessed (auto-write or user approval?)
- [ ] No contradictions to existing rules without flagging for review
- [ ] Cross-skill signal correctly identified (if 2+ domains)
- [ ] Session log entry created (automatic)
- [ ] Compounding detected (if pattern appeared before)
- [ ] User explicitly approved (if approval gate required)

---

## Related Files

- `/config/routing.yml` — Domain map, cross-skill signal rules
- `/config/hypothesis-tracking.yml` — Open hypotheses, confirmation criteria
- `/config/approval-gates.yml` — When to ask user vs. auto-write
- `/knowledge/INDEX.md` — Domain folder locations
- `/knowledge/global/rules.md` — Confirmed cross-skill rules
- `/knowledge/global/hypotheses.md` — Open questions
- `/context/meta-patterns.md` — Current guardrails
- `/sessions/log.md` — Historical session log
