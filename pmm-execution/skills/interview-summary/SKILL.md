---
name: interview-summary
version: 2.2.0
description: >
  Self-improving customer interview synthesis engine for PMMs, Product Managers, and UX Researchers.
  Transforms raw transcripts into structured discovery outputs anchored in JTBD theory,
  with signal-level pattern detection, confidence scoring, and compounding learning loop
  that writes to /context. Includes post-session logging for meta-synthesis pattern detection.
  Trigger on: "summarize interview", "process transcript", "interview summary", "what did customers say", 
  "synthesize discovery", "interview debrief", "JTBD analysis", "customer insight", "research synthesis", 
  or any request to process, structure, or extract meaning from a customer or prospect interview.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
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
  - `/context/meta-patterns.md` — optional; recurring patterns from all skills (guardrail prompts)
  - `/context/interviews/patterns.md` — optional, if exists: apply confirmed patterns
  - `/context/interviews/hypotheses.md` — optional, if exists: check active hypotheses
  - `/context/interviews/rules.md` — optional, if exists: apply confirmed rules before synthesis
  - `/context/interviews/decisions/` — optional, if exists: check prior strategic decisions
  - `BRAIN.md` (specifically: ICP, Positioning, Beachhead Segment sections) — optional, if exists: load for validation
  - All writes target `/context/interviews/` — non-blocking if directory missing
**Brain contract:** Reads: Section 2 (ICP), Section 3 (Positioning), Section 4 (Competitors). Writes: `/context/interviews/`, `/context/skill-sessions.md`, `/foundation/brain.md` Section 2 (if anti-ICP discovered).
---
## Pre-flight
- **Load guardrails first:** Check `/context/meta-patterns.md` for recurring patterns from prior interviews. If pattern matches (e.g., "procurement mentioned 7/12 interviews"), surface guardrail prompt before Step 1.
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
**Step 0: Surface Guardrails (NEW)**
**Before intake, check for patterns:**

If `/context/meta-patterns.md` exists and contains interview patterns:
```
🔁 PATTERN DETECTED FROM PRIOR INTERVIEWS

I've detected [specific pattern] in [N] prior interviews.
Example: "Procurement mentioned 7x as deal-killer", "Long onboarding cycles (60+ days) blocking adoption"

Quick question: Are you seeing [specific signal] in this interview?
- If YES → note it, we'll flag it as confirmed
- If NO → proceed, but watch for this signal

This helps the system learn.
```

**Common guardrail patterns to surface:**
- "Procurement mentioned 7+ times as delay factor" → "Watch for procurement blockers in this interview?"
- "Champion sentiment declining (3 recent interviews)" → "Is your champion feeling less engaged?"
- "Long sales cycles (avg 90+ days) blocking enterprise deals" → "How long is their sales cycle?"
- "Vendor lock-in fears appearing in 5+ interviews" → "Are they concerned about lock-in?"

If patterns apply, ask guardrail question. User can skip, but they've been warned.

**Step 1: Orientation & Context Load**
- If no context provided, ask: "Who is this? (role, company, segment) | What was the purpose? | What are you trying to learn?"
- Load `/context/BRAIN.md` and extract ICP, Positioning, Beachhead Segment for validation.
- Load `/context/interviews/rules.md` and note which patterns apply.
- Load `/context/meta-patterns.md` and flag any cross-skill patterns that might be relevant (e.g., "post-sales prep underestimation").
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
- Check against `/context/meta-patterns.md`: Do any cross-skill patterns apply? (e.g., "post-sales prep" appeared in 2 retros + 3 PDRs, now appearing in interview).
- Flag any new signal: Is this a new hypothesis worth tracking? New Job type?
**Step 4: Validation Against Context**
- ICP match: Does this interviewee match the ICP? Flag if not.
- Anti-ICP discovery: Does this interview surface new anti-ICP signals? (e.g., "Long procurement cycles are a blocker").
- Positioning signal: Does what they said validate or contradict current positioning?
- Beachhead alignment: Does this person represent the beachhead or an adjacent segment?
- Objection discovery: Any new objection or anti-persona signal?
**Step 5: Pattern Detection & Hypothesis Promotion**
- Check if today's signal matches any active hypothesis in `/context/interviews/hypotheses.md`.
- If a hypothesis now has 3+ confirmations: propose promotion to rule.
- Log this session's signals to `/context/interviews/patterns.md` for future pattern detection.
- Cross-reference `/context/meta-patterns.md`: Does today's signal appear in other skill domains? Flag for compounding.
**Step 6: Generate Structured Summary**
- Produce markdown summary with template structure.
- All Metadata fields on separate lines; all Job fields on separate lines; separate Key Insights (analysis only) from Signal Quotes (verbatim only).
- Include Action Items table with named owners and dates.
- Include Flags section (contradictions with positioning or ICP) or explicitly mark "None detected".
**Step 7: Decision Journal & Context Writes**
- If summary produces a strategic decision (ICP change, positioning shift, Jobs model update): log to `/context/interviews/decisions/YYYY-MM-DD-{topic}.md`.
- Write pattern findings to `/context/interviews/patterns.md`.
- Write new hypotheses to `/context/interviews/hypotheses.md` (with confirmation count = 1).
- If anti-ICP discovered: propose update to `/foundation/brain.md` Section 2.
- If promotion triggered: surface explicit approval gate before writing to rules.md.
**Step 8: Post-Session Logging (NEW)**
After every session, log structured data to `/context/skill-sessions.md`:

```yaml
skill: interview-summary
session_date: 2026-06-21
interview_count: 1
interview_type: "Discovery"
interviewee_role: "procurement-manager"
interviewee_company: "mid-market-saas"
buyer_personas_mentioned:
  - "procurement manager": 1
  - "finance ops": 0
  - "technical buyer": 0
  - "exec sponsor": 0
primary_pain_points_extracted:
  - "procurement delays (60+ days, high severity)"
  - "vendor lock-in concerns"
anti_signals_detected:
  - "Long procurement cycles"
  - "Requires legal review"
recurring_themes:
  - "Integration with existing tools"
jtbd_summary:
  - "Help us avoid vendor lock-in while accelerating procurement"
icp_match: "Partial"
positioning_validation: "Contradicts"
new_hypothesis_triggered: true
confidence_score: 8
output_path: "/context/interviews/sessions/20260621-procurement-manager.md"
guardrails_triggered:
  - "Procurement mentioned as deal-killer (3+ prior interviews). This confirms pattern. Recommend: update anti-ICP to flag 'long procurement cycles'."
  - "Vendor lock-in concerns (now 4 interviews total). Recommendation: address in messaging."
```

This feeds into `meta-synthesis` skill (monthly) which detects patterns across all skills and updates brain + `/context/meta-patterns.md`.

**Step 9: Learning Close & Skill Improvement Offer**
- Ask: "What surprised you most? Wish I'd flagged anything else?"
- Ask: "Does this change your view of the most important Job?"
- Ask: "Does this change how you want to describe the problem?"
- Offer to update skill based on feedback.
---
## Outputs
- **Files written:**
  - `/context/skill-sessions.md` — row appended with session metadata and guardrails (NEW)
  - `/context/interviews/patterns.md` — appended with recurring Jobs, pain patterns, vocabulary
  - `/context/interviews/hypotheses.md` — created or appended with new signals (confirmation count = 1)
  - `/context/interviews/rules.md` — created or updated if hypothesis promotion approved (confirmation count ≥3)
  - `/context/interviews/decisions/YYYY-MM-DD-{topic}.md` — created if strategic decision logged
  - `/context/interviews/sessions/{timestamp}-{interviewee-role}.md` — saved summary with full metadata
  - `/foundation/brain.md` Section 2 — optional, if anti-ICP discovered (updated with user approval)
  
- **Chat output format:** Structured markdown summary with Metadata, Background, Current Solution, What they like, Problems (JTBD blocks),
  Key Insights, Action Items table, Flags, Signal Quotes, Pattern Signal.
  All output in markdown, copy-paste ready for Notion, GitHub, or email.
- **External side effects:** Queries brain to load context (non-blocking).
  Checks `/context/meta-patterns.md` for cross-skill patterns. May trigger routing to downstream skills 
  (e.g., flag competitors for `hs-competitive-battlecard` LEARN mode).
  Writes are always explicit and surface approval gates where applicable.
---
## Verification
- [ ] Guardrails checked before intake (Step 0) — patterns from prior interviews surfaced
- [ ] Every summary includes Metadata with Date, Participants, Interview Type, Confidence, ICP Match.
- [ ] Every Job block has: Job name, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
- [ ] Key Insights contain only analysis — no verbatim quotes (those go in Signal Quotes section).
- [ ] Signal Quotes are verbatim, not paraphrased. Include speaker name and context.
- [ ] Action Items table has named owners (not placeholders) and real dates (YYYY-MM-DD format).
- [ ] Flags section is populated with contradictions, or explicitly states "None detected".
- [ ] ICP match is assessed (not defaulted to "Yes") — reasoning included if "Partial" or "No".
- [ ] Anti-ICP signals are flagged (e.g., "Long procurement cycles") and proposed for brain update.
- [ ] Positioning signals are noted in Key Insights or Flags, not omitted.
- [ ] Cross-skill pattern matching to `/context/meta-patterns.md` is explicit.
- [ ] Pattern matching to `/context/interviews/rules.md` is explicit (e.g., "Matches Rule: [rule name]").
- [ ] Context writes surface approval gates where applicable (hypothesis promotion, decision logging, brain updates).
- [ ] If sparse transcript: confidence is 🔴 Low and warning prepended.
- [ ] If new hypothesis detected: entry created in `/context/interviews/hypotheses.md` with confirmation count = 1.
- [ ] If promotion triggered (3+ confirmations): explicit approval gate surfaces before rules.md write.
- [ ] Session logged to `/context/skill-sessions.md` with all metadata.
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
1. **Guardrails first.** Load `/context/meta-patterns.md` at pre-flight. Surface guardrail prompt if pattern matches this interview type.
2. **Context-first synthesis** — Load `/context/BRAIN.md` and `/context/interviews/` before synthesis.
   If missing, surface non-blocking notice. Synthesis is transcript-isolated if context missing.
3. **Full transcript read** — Never summarize from a partial read. Read the complete file before output.
4. **Confidence calibration** — Score (🟢 High / 🟡 Medium / 🔴 Low) based on transcript quality and completeness.
   For 🔴 summaries, prepend explicit warning. Confidence must match input quality, not optimism.
5. **Every Job gets all five fields** — Job, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
   No blank fields. No block text. Each on its own line.
6. **Verbatim quotes are sacred** — Signal Quotes are exact verbatim. Key Insights are pure analysis, no quotes.
   Never paraphrase a quote as verbatim. Never bury a quote in an insight.
7. **ICP match is assessed, not defaulted** — If interviewee matches ICP: state "Yes". If partial match: state "Partial" with reason.
   If doesn't match: state "No" with reason. Never default to "Yes" for convenience.
8. **Anti-ICP discovery is actionable** — If interview surfaces anti-ICP signal (e.g., "long procurement cycles"), flag it explicitly.
   Propose brain update with user approval. Don't suppress it.
9. **Positioning signals are explicit** — If interview validates positioning, state it. If contradicts, flag it.
   If neutral, mark as such. Don't suppress contradictions.
10. **Approval gates are mandatory** — Pattern promotion (3+ confirmations) requires explicit user approval before rules.md write.
    Decision logging requires approval gate. Brain updates require approval. Learnings surface before encoding — never silent.
11. **Pattern matching is proactive** — Every synthesis checks rules.md and meta-patterns.md and applies confirmed patterns by default.
    Hypothesis confirmation count increments explicitly. Promotion to rule requires 3+ confirmations + user approval.
12. **Context writes only if `/context/` exists** — Non-blocking. If `/context/interviews/` missing, write to session metadata only.
    Writes are graceful; if permission denied, flag and continue.
13. **Interview type shapes the synthesis** — Win/loss emphasizes what we lost and why.
    Churn emphasizes Job delivery failure. Discovery emphasizes new Jobs. Validation emphasizes confirmation or contradiction.
    Weighting differs by type; synthesis logic adapts.
14. **Always log.** Even sparse interviews are logged to `/context/skill-sessions.md`. Meta-synthesis learns from both rich and thin data.
---
## Quality Gate
| Check | Standard | Pass = |
|---|---|---|
| Guardrails surfaced | `/context/meta-patterns.md` checked at pre-flight | Yes |
| Frontmatter complete | 8 fields present (added: logging_enabled) | Yes |
| Description 300–600 chars | Count chars, ≥6 triggers | Yes |
| All 9 required sections | Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For, Operating Rules, Quality Gate | Yes |
| Steps named and imperative | ≥9 steps, imperative form | Yes |
| Outputs specify all 3 sub-fields | Files written, chat format, side effects | Yes |
| Verification is concrete | ≥15 checkable checks | Yes |
| Operating Rules ≥14 | At least 14 rules in imperative form | Yes |
| Quality Gate ≥8 checks | Table with ≥8 binary checks | Yes |
| Self-Improvement Loop | Before/After session structure | Yes |
| Changelog ≥2 entries | At least 2 dated version entries | Yes |
| Session logged | Data written to `/context/skill-sessions.md` | Yes |
---
## Self-Improvement Loop
**Before every session:**
1. **Load guardrails:** Check `/context/meta-patterns.md` for patterns matching this interview type. Surface if found.
2. Load `/context/interviews/rules.md` if exists. Note which patterns apply.
3. Load `/context/interviews/hypotheses.md` if exists. Check if today's transcript tests hypothesis.
4. Load `/context/BRAIN.md` if exists. Extract ICP, Positioning, Beachhead for validation.
5. If SKILL-SPEC.md version changed, surface delta.
**After every session:**
1. **Log to `/context/skill-sessions.md`:** Complete session metadata (see Step 8 schema).
2. Log this session's row to `/context/interviews/sessions/{timestamp}-summary.md`.
3. Extract patterns and append to `/context/interviews/patterns.md`.
4. If new hypothesis: create entry in `/context/interviews/hypotheses.md` (confirmation count = 1).
5. If hypothesis has 3+ confirmations: surface promotion gate.
6. If strategic decision logged: note in `/context/interviews/decisions/`.
7. If anti-ICP discovered: propose update to brain Section 2 with approval gate.
8. Note most common signal across sessions. If 3+ instances: propose rule encoding.
**Self-Improvement Trigger format:**
```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [What was observed across reviewed interviews]
Occurrences: [N interviews showing this pattern]
Proposed update: [Exact wording to add to /context/interviews/rules.md or /foundation/brain.md]
Location: [rules.md or brain.md Section X]
Awaiting approval before encoding.
```
Trigger surfaces explicitly before any write. Never silent.
---
## Changelog
### v2.2.0 — 2026-06-21
Added post-session logging + guardrail intake. Guardrails loaded from `/context/meta-patterns.md` at pre-flight. Step 0 surfaces patterns (e.g., "procurement mentioned 7+ times, watch for this signal"). Step 8 logs session metadata to `/context/skill-sessions.md` for meta-synthesis to read. Operating Rules reprioritized (guardrails first). Anti-ICP discovery now actionable (propose brain updates). Quality gate updated to verify guardrail checks + session logging.
Changes from v2.1.0:
- Added Step 0: Surface guardrails before intake (reads `/context/meta-patterns.md`)
- Updated Pre-flight: Load guardrails first + check meta-patterns for cross-skill signals
- Updated Step 1: Load `/context/meta-patterns.md` for cross-skill pattern reference
- Updated Step 3: Check meta-patterns for cross-skill pattern matches
- Updated Step 4: Anti-ICP discovery now explicit + actionable (propose brain updates)
- Updated Step 7: Propose brain Section 2 updates if anti-ICP discovered
- Added Step 8: Post-session logging to `/context/skill-sessions.md`
- Updated Outputs: Now writes to `/context/skill-sessions.md` (NEW) + optional `/foundation/brain.md` Section 2
- Updated Inputs: Now reads `/context/meta-patterns.md` (NEW)
- Updated Operating Rules: "Guardrails first" + "Anti-ICP discovery is actionable" + "Always log"
- Updated Quality Gate: Added checks for guardrails + session logging
- Updated Self-Improvement Loop: Load guardrails first, log to `/context/skill-sessions.md` after
- Updated Verification: Added checks for guardrails + anti-ICP signals + session logging
- Updated metadata: Added `logging_enabled: true`
- Version bump 2.1.0 → 2.2.0
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
interview-summary v2.2.0
---
## 📋 Metadata
**Date:** [Date and time]
**Participants:** [Interviewer name + role] | [Interviewee name + role + company]
**Interview type:** [Discovery / Validation / Win-loss / Churn / Competitive / Other]
**Confidence:** [🟢 High / 🟡 Medium / 🔴 Low]
**ICP match:** [Yes / Partial / No — one-line reason if not Yes]
**Anti-ICP signals:** [List if any, else "None detected"]
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
**Cross-skill pattern match:** [Yes / No — which meta-pattern]
**New signal for tracking:** [Yes / No]
**Hypothesis triggered:** [State it, or "None"]
**Confirmation count (if hypothesis):** [N / 3 threshold for promotion]
**Anti-ICP signal detected:** [Yes / No — specific signal]
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
- **meta-synthesis** → After 3+ interviews logged → meta-synthesis detects patterns + updates brain.
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
| `/anti-icp` | Show all detected anti-ICP signals and proposed brain updates |
| `/decisions` | Show all logged strategic decisions from `/context/interviews/decisions/` |
| `/meta-patterns` | Show cross-skill patterns from `/context/meta-patterns.md` relevant to interviews |
| `/close` | Run the Learning Close for the current session |
| `/save` | Save the current summary to `/context/interviews/sessions/` with full metadata |
| `/help` | Show available commands and current knowledge base status |
---
## Integration with Four-Layer GTM System
This skill operates as the **System of Context layer** (Layer 1: System of Context):
1. **Input:** Unstructured interview transcript
2. **Process:** JTBD synthesis, pattern matching, context validation, guardrail checking
3. **Output:** Structured markdown summary + pattern writes to `/context/interviews/` + session logs to `/context/skill-sessions.md`
4. **Compounds:** Every session improves pattern library, hypothesis tracking, rule confidence, and meta-synthesis visibility
5. **Feeds:** Every other skill (hs-positioning-messaging, hs-gaccs-brief, hs-competitive-battlecard, meta-synthesis) reads from this context layer
The skill builds the "System of Context" that powers the entire GTM orchestration engine.
