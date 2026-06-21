---
name: interview-summary
version: 2.1.0
description: >
  Self-improving customer interview synthesis engine for PMMs, Product Managers, and UX Researchers.
  Transforms raw transcripts into structured discovery outputs anchored in JTBD theory,
  with signal-level pattern detection, confidence scoring, and compounding learning loop
  that writes to /context. Trigger on: "summarize interview", "process transcript",
  "interview summary", "what did customers say", "synthesize discovery", "interview debrief",
  "JTBD analysis", "customer insight", "research synthesis", or any request to process,
  structure, or extract meaning from a customer or prospect interview.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-21
---

# interview-summary — Customer Discovery Synthesis Engine

Transforms raw interview transcripts into structured intelligence that compounds.
Not a transcription service. A synthesis engine that extracts Jobs, surfaces patterns,
flags contradictions, and writes learnings to `/context` where every other skill can read them.

Built on JTBD theory. Anchored to the four-layer GTM system (System of Context, System of Skills, System of Orchestration, System of Integrations).
Sharpened for B2B product and GTM contexts.

---

## Trigger

- **When:** Any customer or prospect interview needs synthesis into structured discovery output.
  This includes: discovery calls, win/loss debriefs, churn interviews, competitive research interviews,
  onboarding feedback, feature validation calls, or any call where you need to extract Jobs, map solutions,
  and flag contradictions with your positioning or ICP.

- **Not for:**
  - **interview-summary** is not a transcription tool — use Otter.ai or Fireflies for that.
  - **interview-summary** is not for analyzing *your own* positioning or messaging in isolation.
    If you need to check whether your messaging lands with buyers, route to `hs-positioning-messaging` or `hs-gaccs-brief`.
  - **interview-summary** is not for building buyer personas from scratch without interviews.
    Use `hs-buyer-personas` for that; this skill synthesizes existing transcript data.

- **Example prompts:**
  - "Summarize this customer discovery call and flag which Jobs matter most"
  - "I have a win/loss interview — help me extract what we lost and why"
  - "Process this transcript. Flag any positioning signal that contradicts our current narrative"
  - "Run synthesis and update the pattern library with new findings"
  - "Churn interview debrief — what Job did we fail to deliver on?"

---

## Inputs

- **Args:** Path to a transcript file (`.txt`, `.md`, `.pdf`), pasted plain text,
  structured note dump, or Otter/Fireflies/Rev transcription output.
  Optional: interview context (interviewee role, company, interview purpose).
  Free format — transcript alone is sufficient; context makes synthesis sharper.

- **Defaults:** If no context provided, skill asks three orientation questions.
  If interviewee segment unknown, default to "Unclassified" in ICP match.
  If no interview type specified, default to "Discovery".

- **Context keys:** Requires `/context/interviews/` directory structure.
  - `/context/interviews/patterns.md` — optional, if exists: apply confirmed patterns
  - `/context/interviews/hypotheses.md` — optional, if exists: check active hypotheses
  - `/context/interviews/rules.md` — optional, if exists: apply confirmed rules before synthesis
  - `/context/interviews/decisions/` — optional, if exists: check prior strategic decisions
  - `BRAIN.md` (specifically: ICP, Positioning, Beachhead Segment sections) — optional, if exists: load for validation
  - All writes target `/context/interviews/` — non-blocking if directory missing

---

## Pre-flight

- Load `/context/BRAIN.md` if it exists. Extract: ICP Prioritisation, Positioning, Beachhead Segment, Revenue Levers.
  If missing, surface non-blocking notice: "No brain context. Synthesis will be transcript-isolated."

- Load `/context/interviews/rules.md` if it exists. These are confirmed patterns (3+ instances) to apply by default.

- Load `/context/interviews/hypotheses.md` if it exists. Note which hypotheses can be tested against today's transcript.

- Accept transcript in any format: pasted text, uploaded file (`.txt`, `.md`, `.pdf`),
  or structured notes. Read the full file before producing output.

- Identify interview type (Discovery / Validation / Win-loss / Churn / Competitive / Other)
  from context or ask in intake step.

---

## Steps

**Step 1: Orientation & Context Load**
- If no context provided, ask: "Who is this? (role, company, segment) | What was the purpose? | What are you trying to learn?"
- Load `/context/BRAIN.md` and extract ICP, Positioning, Beachhead Segment for validation.
- Load `/context/interviews/rules.md` and note which patterns apply.
- Declare interview type and confidence upfront.

**Step 2: Intake & Pre-Synthesis Audit**
- Read transcript in full.
- Run silent pre-synthesis audit: Does it have ≥1 identifiable Job? Current solution? Satisfaction signals? Verbatim quotes?
- If too sparse, surface: "Coverage too thin. What I can extract: [list]. Proceed with caveats or follow up?"
- If adequate: proceed to synthesis.

**Step 3: JTBD Synthesis & Pattern Matching**
- Extract Jobs (functional, emotional, social).
- For each Job: Desired outcome, Importance, Satisfaction level, Verbatim signal.
- Check against `/context/interviews/rules.md`: Does this Job match a confirmed pattern? Flag alignment.
- Flag any new signal: Is this a new hypothesis worth tracking? New Job type?

**Step 4: Validation Against Context**
- ICP match: Does this interviewee match the ICP? Flag if not.
- Positioning signal: Does what they said validate or contradict current positioning?
- Beachhead alignment: Does this person represent the beachhead or an adjacent segment?
- Objection discovery: Any new objection or anti-persona signal?

**Step 5: Pattern Detection & Hypothesis Promotion**
- Check if today's signal matches any active hypothesis in `/context/interviews/hypotheses.md`.
- If a hypothesis now has 3+ confirmations: propose promotion to rule.
- Log this session's signals to `/context/interviews/patterns.md` for future pattern detection.

**Step 6: Generate Structured Summary**
- Produce markdown summary with template structure.
- All Metadata fields on separate lines; all Job fields on separate lines; separate Key Insights (analysis only) from Signal Quotes (verbatim only).
- Include Action Items table with named owners and dates.
- Include Flags section (contradictions with positioning or ICP) or explicitly mark "None detected".

**Step 7: Decision Journal & Context Writes**
- If summary produces a strategic decision (ICP change, positioning shift, Jobs model update): log to `/context/interviews/decisions/YYYY-MM-DD-{topic}.md`.
- Write pattern findings to `/context/interviews/patterns.md`.
- Write new hypotheses to `/context/interviews/hypotheses.md` (with confirmation count = 1).
- If promotion triggered: surface explicit approval gate before writing to rules.md.

**Step 8: Learning Close & Skill Improvement Offer**
- Ask: "What surprised you most? Wish I'd flagged anything else?"
- Ask: "Does this change your view of the most important Job?"
- Ask: "Does this change how you want to describe the problem?"
- Offer to update skill based on feedback.

---

## Outputs

- **Files written:**
  - `/context/interviews/patterns.md` — appended with recurring Jobs, pain patterns, vocabulary
  - `/context/interviews/hypotheses.md` — created or appended with new signals (confirmation count = 1)
  - `/context/interviews/rules.md` — created or updated if hypothesis promotion approved (confirmation count ≥3)
  - `/context/interviews/decisions/YYYY-MM-DD-{topic}.md` — created if strategic decision logged
  - `/context/interviews/sessions/{timestamp}-{interviewee-role}.md` — saved summary with full metadata
  
- **Chat output format:** Structured markdown summary with Metadata, Background, Current Solution, What they like, Problems (JTBD blocks),
  Key Insights, Action Items table, Flags, Signal Quotes, Pattern Signal.
  All output in markdown, copy-paste ready for Notion, GitHub, or email.

- **External side effects:** Queries brain to load context (non-blocking).
  May trigger routing to downstream skills (e.g., flag competitors for `hs-competitive-battlecard` LEARN mode).
  Writes are always explicit and surface approval gates where applicable.

---

## Verification

- [ ] Every summary includes Metadata with Date, Participants, Interview Type, Confidence, ICP Match.
- [ ] Every Job block has: Job name, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
- [ ] Key Insights contain only analysis — no verbatim quotes (those go in Signal Quotes section).
- [ ] Signal Quotes are verbatim, not paraphrased. Include speaker name and context.
- [ ] Action Items table has named owners (not placeholders) and real dates (YYYY-MM-DD format).
- [ ] Flags section is populated with contradictions, or explicitly states "None detected".
- [ ] ICP match is assessed (not defaulted to "Yes") — reasoning included if "Partial" or "No".
- [ ] Positioning signals are noted in Key Insights or Flags, not omitted.
- [ ] Pattern matching to `/context/interviews/rules.md` is explicit (e.g., "Matches Rule: [rule name]").
- [ ] Context writes surface approval gates where applicable (hypothesis promotion, decision logging).
- [ ] If sparse transcript: confidence is 🔴 Low and warning prepended.
- [ ] If new hypothesis detected: entry created in `/context/interviews/hypotheses.md` with confirmation count = 1.
- [ ] If promotion triggered (3+ confirmations): explicit approval gate surfaces before rules.md write.

---

## Do Not Use For

- **Transcription** — use Otter.ai, Fireflies, or Rev. This skill synthesizes, not transcribes.
  Route: Transcription tool of choice.

- **Building personas from scratch** — use `hs-buyer-personas`. This skill processes existing interviews.
  Route: `hs-buyer-personas` for de novo persona work.

- **Analyzing your own positioning in isolation** — use `hs-positioning-messaging` or `hs-gaccs-brief`.
  This skill extracts buyer signals; those skills validate positioning.
  Route: `hs-positioning-messaging` for positioning audit, `hs-gaccs-brief` for campaign messaging.

- **Automated decision-making** — approval gates are explicit. Learnings surface before encoding.
  Never silent. Route: User approves pattern promotion or decision logging.

---

## Operating Rules

1. **Context-first synthesis** — Load `/context/BRAIN.md` and `/context/interviews/` before synthesis.
   If missing, surface non-blocking notice. Synthesis is transcript-isolated if context missing.

2. **Full transcript read** — Never summarize from a partial read. Read the complete file before output.

3. **Confidence calibration** — Score (🟢 High / 🟡 Medium / 🔴 Low) based on transcript quality and completeness.
   For 🔴 summaries, prepend explicit warning. Confidence must match input quality, not optimism.

4. **Every Job gets all five fields** — Job, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
   No blank fields. No block text. Each on its own line.

5. **Verbatim quotes are sacred** — Signal Quotes are exact verbatim. Key Insights are pure analysis, no quotes.
   Never paraphrase a quote as verbatim. Never bury a quote in an insight.

6. **ICP match is assessed, not defaulted** — If interviewee matches ICP: state "Yes". If partial match: state "Partial" with reason.
   If doesn't match: state "No" with reason. Never default to "Yes" for convenience.

7. **Positioning signals are explicit** — If interview validates positioning, state it. If contradicts, flag it.
   If neutral, mark as such. Don't suppress contradictions.

8. **Approval gates are mandatory** — Pattern promotion (3+ confirmations) requires explicit user approval before rules.md write.
   Decision logging requires approval gate. Learnings surface before encoding — never silent.

9. **Pattern matching is proactive** — Every synthesis checks rules.md and applies confirmed patterns by default.
   Hypothesis confirmation count increments explicitly. Promotion to rule requires 3+ confirmations + user approval.

10. **Context writes only if `/context/` exists** — Non-blocking. If `/context/interviews/` missing, write to session metadata only.
    Writes are graceful; if permission denied, flag and continue.

11. **Interview type shapes the synthesis** — Win/loss emphasizes what we lost and why.
    Churn emphasizes Job delivery failure. Discovery emphasizes new Jobs. Validation emphasizes confirmation or contradiction.
    Weighting differs by type; synthesis logic adapts.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Frontmatter complete | 7 fields present | Yes |
| Description 300–600 chars | Count chars, ≥6 triggers | Yes |
| All 7 required sections | Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For | Yes |
| Steps named and imperative | ≥5 steps, imperative form | Yes |
| Outputs specify all 3 sub-fields | Files written, chat format, side effects | Yes |
| Verification is concrete | ≥10 checkable checks | Yes |
| Operating Rules ≥6 | At least 6 rules in imperative form | Yes |
| Quality Gate ≥5 checks | Table with ≥5 binary checks | Yes |
| Self-Improvement Loop | Before/After session structure | Yes |
| Changelog ≥1 entry | At least 1 dated version entry | Yes |
| Line count ≤500 | SKILL.md ≤500 lines | Yes |
| Output templates in code fences | ```markdown``` fences for all templates | Yes |
| Evals file with ≥3 test cases | `/evals/interview-summary.eval.md`, ≥3 cases | Yes |

---

## Self-Improvement Loop

**Before every session:**
1. Load `/context/interviews/rules.md` if exists. Note which patterns apply.
2. Load `/context/interviews/hypotheses.md` if exists. Check if today's transcript tests hypothesis.
3. Load `/context/BRAIN.md` if exists. Extract ICP, Positioning, Beachhead for validation.
4. If SKILL-SPEC.md version changed, surface delta.

**After every session:**
1. Log this session's row to `/context/interviews/sessions/{timestamp}-summary.md`.
2. Extract patterns and append to `/context/interviews/patterns.md`.
3. If new hypothesis: create entry in `/context/interviews/hypotheses.md` (confirmation count = 1).
4. If hypothesis has 3+ confirmations: surface promotion gate.
5. If strategic decision logged: note in `/context/interviews/decisions/`.
6. Note most common signal across sessions. If 3+ instances: propose rule encoding.

**Self-Improvement Trigger format:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [What was observed across reviewed interviews]
Occurrences: [N interviews showing this pattern]
Proposed update: [Exact wording to add to /context/interviews/rules.md]
Location: /context/interviews/rules.md
Awaiting approval before encoding.
```

Trigger surfaces explicitly before any write. Never silent.

---

## Changelog

### v2.1.0 — 2026-06-21
Major upgrade: Full SKILL-SPEC v2.0.0 compliance + four-layer GTM framework integration.

**Architecture upgrades:**
- Frontmatter complete: author, context (brain-dependent), quality_gate, last_updated
- Context-writing hardened: All writes target `/context/interviews/` (patterns, hypotheses, rules, decisions)
- Self-Improvement Loop added: Before/After session structure with explicit rule promotion gates
- Quality Gate table added: 13 binary checks ensuring 19/19 spec compliance
- Operating Rules expanded to 11: Context-first, full reads, confidence calibration, ICP assessment, positioning signals, approval gates, pattern matching, context-aware writes

### v2.0.1 — 2026-04-20
Formatting and structure patch from review session.

### v2.0.0 — 2026-04-20
Full rebuild from v1.0.0. Breaking changes throughout.

---

## Summary Output Template

````markdown
---
# Interview Summary
interview-summary v2.1.0
---

## 📋 Metadata

**Date:** [Date and time]

**Participants:** [Interviewer name + role] | [Interviewee name + role + company]

**Interview type:** [Discovery / Validation / Win-loss / Churn / Competitive / Other]

**Confidence:** [🟢 High / 🟡 Medium / 🔴 Low]

**ICP match:** [Yes / Partial / No — one-line reason if not Yes]

---

## 🏢 Background

[Role, company, team size, and context about their situation.]

---

## 🛠️ Current solution

[What they use today — tool, process, or workaround.]

---

## ✅ What they like about their current solution

- **[Strength label]:** [What Job it satisfies and how.]

---

## 🔴 Problems with their current solution

**Job:** [The functional task they're trying to get done]

**Desired outcome:** [What success looks like for them]

**Importance:** [Critical / High / Medium / Low] — [one-line evidence]

**Satisfaction:** [Not satisfied / Partially / Satisfied] — [one-line evidence]

**Verbatim signal:** *"[Exact quote if available]"*

[Repeat block per Job. Separate each with a line break.]

---

## 💡 Key insights

- [Unexpected finding or analytical observation — no quotes here, pure interpretation.]

---

## 📋 Action items

| Date | Owner | Action |
|------|-------|--------|
| YYYY-MM-DD | [Name] | [Specific action] |

---

## ⚠️ Flags

- **[Flag label]:** [What it contradicts and why it matters.]

---

## 🗣️ Signal quotes

> *"[Quote]"* — [Speaker, context. What makes this one irreplaceable.]

---

## 📊 Pattern signal

**Matches existing pattern:** [Yes / No / Partial — which rule]

**New signal for tracking:** [Yes / No]

**Hypothesis triggered:** [State it, or "None"]

**Confirmation count (if hypothesis):** [N / 3 threshold for promotion]

**Promotion ready:** [Yes / No]
````

---

## Related Skills

Cross-reference when findings trigger downstream work:

- **hs-product-marketing-context** → Always load first. Use to validate ICP, Positioning, Beachhead.
- **hs-competitive-battlecard** → Competitor named as current solution → flag for LEARN mode.
- **hs-value-prop-statements** → Strong Job discovered → pressure-test value prop against it.
- **hs-gaccs-brief** → Messaging hypothesis surfaced → route here for campaign brief.
- **hs-pre-mortem** → Risk or failure mode surfaced by customer → route here.
- **hs-brainstorm-okrs** → Success metric gap surfaces → route here for KR signal.

---

## Commands

| Command | What it does |
|---------|-------------|
| `/summarize [transcript or file]` | Run the full synthesis flow on a transcript |
| `/summarize-quick [transcript or file]` | Output only: skips intake questions, produces summary immediately |
| `/patterns` | Show all recurring Jobs, pain patterns, vocabulary across all interviews |
| `/hypotheses` | Show active hypotheses and their current confirmation count |
| `/promote [hypothesis name]` | Propose promotion of a hypothesis to a confirmed rule (requires 3+ confirmations) |
| `/flags` | List all flags across sessions — contradictions with positioning or ICP assumptions |
| `/decisions` | Show all logged strategic decisions from `/context/interviews/decisions/` |
| `/close` | Run the Learning Close for the current session |
| `/save` | Save the current summary to `/context/interviews/sessions/` with full metadata |
| `/help` | Show available commands and current knowledge base status |

---

## Integration with Four-Layer GTM System

This skill operates as the **System of Context layer** (Layer 1: System of Context):

1. **Input:** Unstructured interview transcript
2. **Process:** JTBD synthesis, pattern matching, context validation
3. **Output:** Structured markdown summary + pattern writes to `/context/interviews/`
4. **Compounds:** Every session improves pattern library, hypothesis tracking, and rule confidence
5. **Feeds:** Every other skill (hs-positioning-messaging, hs-gaccs-brief, hs-competitive-battlecard) reads from this context layer

The skill builds the "System of Context" that powers the entire GTM orchestration engine.
