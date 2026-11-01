---
name: product-marketing-context
version: 3.6.0
description: >
  Builds and maintains the shared GTM brain (product context, ICP, positioning, voice,
  market context, proof points, plus optional strategy and execution sections and the
  deal-reality fields) that every other skill reads before producing output. Works
  standalone from your own answers, and gets stronger when you connect docs or a CRM.
  Trigger with "build my brain", "set up my GTM foundation", "audit my brain", "update my
  ICP", "add my objections", "capture what customers say", "refresh my brain", "what's
  stale in my brain", "my brain gaps", "build my brain from my website and docs", or "my
  context".
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-11-01
---

# Product Marketing Context (The Brain)

Stop re-explaining your company, your buyer, and your competitors to every tool you use. Answer these questions once and every other skill in this stack reads the answers automatically instead of asking again.

---

## Trigger

- **When:** Building the GTM brain for the first time, editing a section, refreshing fields that have gone stale, answering the open questions other skills left behind, or running a health audit on the existing brain.
- **Not for:** Any skill that reads the brain rather than builds it — every brain-dependent skill in this stack routes here first if the brain is missing, then uses its own Trigger. This skill has no downstream overlap since it is upstream of everything else.
- **Example prompts:**
  - "Build my brain"
  - "Set up my GTM foundation"
  - "Audit my brain"
  - "Update my ICP"
  - "Add my objections" or "capture what customers say"
  - "Update my strategy" or "update my execution"
  - "Check brain health"
  - "Refresh my brain"
  - "What's stale in my brain?"
  - "Answer my brain gaps"
  - "Build my brain from my website and these docs"
  - "Set up my context" (how you like to work)

---

## Inputs

- **Args:** None required. The skill first asks for your website and pricing page and builds a draft from them and any material you add (Step 8). The wizard (Step 2) then asks one question at a time, only about what is missing. A pitch deck, pricing page, call notes or win/loss doc speeds this up but isn't required.
- **Defaults:** No brain found → start the wizard from Section 1. Brain exists → load silently and offer [View current] [Edit a section] [Refresh stale fields] [Answer open gaps] [Add material] [My context] [Run health audit].
- **Context keys:** `/foundation/brain.md` (read if present; written section by section only after confirmation), `evidence.md` (append only, Step 8), `me.md` (Step 9 only; describes you, not the company), `gaps.md` (append only), legacy `.agents/*.md` and `.claude/*.md` (offered for migration), and `AGENTS.md` / `CLAUDE.md` (Step 10 only, inside one marked block each). Formats: `references/inputs-detail.md`.
  - **Brain contract:** Reads all sections (1 to 8) if present, and `me.md` for format and detail only. Writes any section, only after explicit confirmation of the exact before/after (Operating Rule 1).

---

## Pre-flight

- Check `/foundation/brain.md` — see Step 1 (Detect Brain State).
- Check for legacy files (`.agents/*.md`, `.claude/*.md`) and offer migration if found.
- No hard block: this skill is the entry point for users with no brain at all.

---

## Connectors (Optional)

The `~~` connectors this skill can pull from, and which sections each feeds, are in `references/connectors.md`. With a connector, candidate answers are pulled first, tagged with category, tool and date, and confirmed, edited or rejected before anything is written to `/foundation/brain.md`. No connectors? Paste a deck excerpt, a pricing page or a win/loss doc.

---

## Output Format

```markdown
# Brain Update: [Section Name]

## What Changed
[Old value → New value, or "New — first time this section is filled"]

## Section Status
[Confirmed / Needs another pass — specific gap noted]

## Health Score (if audit was run)
| Section | Score | Status |
|---------|-------|--------|
| Product Context | X/100 | ... |
| ICP | X/100 | ... |
| Alternatives & Positioning | X/100 | ... |
| Voice & Tone | X/100 | ... |
| Market Context | X/100 | ... |
| Proof Points | X/100 | ... |

Deal-reality fields captured: X of 10

## Next Step
[One sentence — what to run or fix next]

---
_Brain update proposed: [Yes — exact section and field / No — audit or view only]_
```

---

## Steps

### Step 1: Detect Brain State

Check for `/foundation/brain.md`.

- **Missing:** Explain in one line what the brain does, then offer Step 8 first (build from your website and material). If the user has none, start the wizard from Section 1.
- **Exists:** Load all sections silently. Offer: [View current] [Edit a section] [Refresh stale fields] [Answer open gaps] [Add material] [My context] [Run health audit]. If `/foundation/gaps.md` has open gaps, say how many in one line. If fewer than 10 of the deal-reality fields are captured, say how many in one line ("4 of 10 deal-reality fields captured") and that [Edit a section] picks up the rest. Do not treat this as a gap or ask for them unprompted.
- **Exists with a `🟡 Cold start` line:** another skill started the brain with one section. Say so in one line and list which of Sections 1 to 6 are filled and which are missing. Offer: [Build the missing sections] [Expand a filled section] [Run health audit]. Start at the first missing section unless the user picks one. For a section that is present but partial, ask only for its missing fields, show the merged result, and replace the section only after the user confirms it. Never rewrite a filled section the user did not choose.
- **Legacy files found** (`.agents/*.md`, `.claude/*.md`): offer to migrate, showing each extracted value before writing anything.

### Step 2: Run the Wizard

Open with: "Do you have a website, a pricing page, a deck, call notes or a win/loss doc? If yes, we build from that first (Step 8)." With nothing to share, or after Step 8, ask about the sections still empty or thin.

Ask one question at a time. After each section show the answers and ask "Look good? (yes / edit / skip)." Push back on vague answers before storing them.

Sections 1 to 6 are required, 7 (Strategy) and 8 (Execution) recommended. Ask the questions for each section in `references/wizard-questions.md` (read it now): 1 Product Context, 2 ICP Definition, 3 Alternatives & Positioning, 4 Voice & Tone (customer language is verbatim, no source means a gap: Operating Rule 10), 5 Market Context, 6 Proof Points Registry, 7 Strategy, 8 Execution (roles first; a name only if the user wants it). "Subscription" is not a business model, "everyone" is not an ICP, "competitors" is not a list of named alternatives.

### Step 3: Write the Brain File

Once a section is confirmed, write it to `/foundation/brain.md` using the template at `templates/brain-template.md`. Write section by section, not in one batch — a mid-wizard exit should still leave a partial, usable brain plus a `.brain-draft.md` marker noting which section to resume from. Tag every confirmed value with a provenance tag as defined in `references/brain-schema.md` (user answers are `stated`, today's date, `confirmed`); never retag a legacy untagged field unless the user edits it. Keep a `🟡 Cold start` line in the header until Sections 1 to 6 are confirmed (Sections 7 and 8 are recommended, not required), then remove it in the same write.

### Step 4: Health Audit (Run Standalone or After Edits)

Score each of Sections 1 to 6 0-100 on: does the field exist, and is it specific rather than generic (named alternatives not "competitors," numbers not "high," a real persona not "businesses"). A section absent from a cold-start brain scores 0; a section present with fields missing scores 50 or lower. Report strengths (80+), needs improvement (50-79), and critical gaps (<50), with one concrete fix per gap. Also report: open gaps (count of `open` gap blocks), the oldest field in each section, provenance coverage (share of fields with a source tag; legacy untagged fields count as untagged), stale fields (older than the section's limit in `references/brain-schema.md`), Sections 7 and 8 status ("not built" is reported as such, never as a gap or a zero), and the deal-reality fields: how many of the ten are captured, with the one that would help most named (for example "no `objections`: every battlecard will re-ask"). A missing deal-reality field never lowers a section score. Offer to jump straight into editing the weakest section.

### Step 5: Route to What's Next

After any completed setup, edit, or audit, first run Step 10 when Sections 1 to 6 are confirmed (it changes nothing when nothing is new). Then tell the user plainly that the brain is ready and other skills in the stack will read from it automatically. Offer next steps only from the "After product-marketing-context" entry in `.claude-plugin/next-skill-map.md`. The repo's tests check every skill name in that file against the skills that exist, so a name taken from it is verified. Never name a skill from memory.

### Step 6: Refresh Stale Fields

Run when the user picks [Refresh stale fields] or says "refresh my brain" or "what's stale?". It ends with Step 5.

Load the brain and `references/brain-schema.md`, age each field from its source tag date against the section's limit (Section 6 per claim), and stop if nothing is stale. Otherwise list stale fields (sections 2, 3, 6 first) and ask one at a time "Still true? [yes / changed / drop]": `changed` re-asks that field with an exact before/after and a new tag (`stated`, today, `confirmed`); `drop` shows what will be removed and confirms; `yes` answers get one batch confirmation, then a date bump. Never refresh a field the user did not choose; "stop" keeps what is confirmed. Full procedure: `references/refresh-and-gaps.md`.

### Step 7: Answer Open Gaps

Run when the user picks [Answer open gaps] or says "my brain gaps". It ends with Step 5.

Read `/foundation/gaps.md` (newest block per `gap_id`; `open`, or `skipped` over 30 days ago); stop if none. Take gaps oldest first: the question, why it matters, "answer or skip". Answer: show the before/after, confirm, write with a `stated` tag, append `answered`. Skip: append `skipped`, not asked again for 30 days. Procedure: `references/refresh-and-gaps.md`.

### Step 8: Ingest Material (build from what you have, then ask)

Run when the user picks [Add material], says "build my brain from my website and docs", or when Step 1 or Step 2 offers it. It ends with Step 5. Evidence writes need no per-fact confirmation, because evidence is not the brain. Every brain write keeps its gate (Operating Rule 1).

Procedure in `references/ingest.md` (read it now): (1) start with the website and pricing page, treated as rank 4 `website` evidence; public copy is never proof, so a metric enters Section 6 only as `draft` with `[NEEDS PROOF]`; (2) ask what else they have, from sources named in this run, about 10 documents or 5 calls per run; (3) extract atomic facts with source and date to `/foundation/evidence.md`, no emails, phones or private details; (4) cluster: two or more independent sources propose `pulled`, one source `inferred`, `4.customer_phrases` never merged, disagreements shown with rank and date, a confirmed value never replaced; (5) Brain Diff, approved section by section, written with evidence ids in the source tag; (6) fields with no evidence become `open` gaps, asked one at a time (Step 7).

### Step 9: My Context (how you like to work)

Run when the user picks [My context], says "set up my context", or runs `/product-marketing-context:my-context`. It does not need a brain and does not touch one. It ends with Step 5 when a brain exists.

1. Read `/foundation/me.md` if it exists, and `references/me-format.md`. If it exists, show it and ask what to change. Otherwise start fresh.
2. Ask at most six short questions, one at a time, only for empty keys: role and level; output length; headline first or full reasoning; bullets, tables or prose; how blunt; phrases you dislike. Offer a default for each.
3. Never ask for company facts here (product, customers, numbers). Those belong in the brain. If the user volunteers one, say so and offer to add it to the brain instead.
4. Show the exact before/after for `/foundation/me.md`, confirm, then write it. Max 12 lines, no private details.
5. If files cannot be written, show the file and say it was not saved.

### Step 10: Write the Agent Map (automatic)

Runs on its own at the start of Step 5 once Sections 1 to 6 are confirmed (no `🟡 Cold start` line), and when the user runs `/product-marketing-context:agents-map`. It asks no question: it only adds one marked block and never changes the brain.

1. Run `python3 scripts/write_agents_map.py --project <the user's project root>` (the script sits next to this skill). It writes one map block into the project's `AGENTS.md`, adds a marked `@AGENTS.md` line to `CLAUDE.md` so Claude Code reads it, and copies `brain_section.py` and `lint_draft.py` into `foundation/tools/`.
2. It never touches text outside its markers. A second run with nothing new changes nothing. `--dry-run` shows the changes without writing.
3. Tell the user in two lines what was written and where, and why: the map is what makes the agent read the brain in chats where no skill is called.
4. If scripts cannot run here, fill `templates/agents-map-template.md` by hand from the brain's section list and the folders that exist, show the block, and ask the user to paste it into `AGENTS.md`. Say it was not saved.
5. Offer `python3 foundation/tools/lint_draft.py <draft>` whenever the user drafts copy that will leave the building. It lists forbidden phrases, unapproved numbers and leftover placeholders; a human reads each hit.

---

## Outputs

- **Files written:** `/foundation/evidence.md` — appended to only: facts extracted from the user's material (Step 8). `/foundation/gaps.md` — appended to only: blocks marking a gap answered or skipped (Step 7). `/foundation/brain.md` — written section by section,
  only after user confirmation (Step 3). `/foundation/me.md` — written by Step 9 only, after confirmation. `.brain-draft.md` — a resume
  marker left behind if the wizard exits mid-session. `AGENTS.md`, `CLAUDE.md` and `foundation/tools/` — written by Step 10 only, one marked block per file and two copied scripts; nothing outside the markers is changed.
- **Chat output format:** The Output Format template above — Brain Update
  header, What Changed, Section Status, Health Score if an audit ran, Next
  Step.
- **External side effects:** None beyond the files above. Step 10 runs a local script; it sends nothing anywhere.

---

## Quality Gate

| Check                                          | Pass =                          |
|-------------------------------------------------|----------------------------------|
| Brain state checked before any question asked  | Yes                              |
| No section written without user confirmation   | Yes                              |
| Vague answers challenged, not silently stored  | Yes                              |
| Alternatives are named products, not categories| Yes                              |
| Proof points are quantified with a source      | Yes                              |
| Output format fully populated                  | No `[Needs input]` left blank    |
| Next-skill names come only from the next-skill-map | Yes, or none named          |
| Refresh asked only about stale fields          | Yes                              |
| Gap blocks appended, never edited              | Yes                              |
| Disagreeing sources shown, never auto-resolved | Yes                              |
| Website claims not stored as confirmed proof   | Yes                              |
| me.md holds no company facts                   | Yes                              |
| Customer phrases verbatim, each with a source  | Yes                              |
| Deal-reality fields never lower a section score| Yes                              |
| Agent map written only inside its markers      | Yes                              |
| Cold-start brain recognised; line removed only once Sections 1 to 6 are confirmed | Yes |
| Audit scores Sections 1 to 6, names a fix for every gap under 50, reports provenance coverage, stale fields and deal-reality count | Yes |

---

## Operating Rules

1. **Never write to brain.md without user confirmation.** Every write is an exact before/after and a yes.
2. **Never re-ask what the brain already knows.** Load silently; skip answered questions.
3. **Push back on vague answers inline,** before they are accepted.
4. **Name a next skill only from the next-skill-map.** The repo's tests validate it; a name from anywhere else is a broken promise.
5. **Pulled facts are drafts.** Tag category, tool and date, confirm first; pulled proof points and quotes enter Section 6 as unverified.
6. **A confirmed value is never overwritten by newer evidence.** Show both and ask; a disagreement is a question, never an update.
7. **Store the minimum from sources.** No emails, phone numbers or private details in evidence; ingest only sources named in this run.
8. **Website copy is not proof.** Metrics and superlatives enter Section 6 as `draft` with `[NEEDS PROOF]`.
9. **me.md is about the user, never the company.** A company fact found there is ignored and moved to the brain only after confirmation.
10. **Customer words stay verbatim.** `customer_phrases` are exact quotes, each with a source (evidence id, or who said it and when); never paraphrase, merge, tidy or invent one. No source, no entry: it becomes a gap. Customer words guide copy but are not proof; a number goes to Section 6 through `proof-points`.
11. **The agent map touches only its own markers.** Step 10 adds or refreshes one marked block in `AGENTS.md` and one marked import line in `CLAUDE.md`, never edits the user's text, and never copies company facts there.

---

This skill is upstream of everything else in this stack — it doesn't need a
Related Skills section pointing out to its dependents. Every other skill that
reads or writes `/foundation/brain.md` should name this skill and its exact
section numbers in its own file instead.
