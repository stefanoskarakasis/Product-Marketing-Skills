---
name: product-marketing-context
version: 3.4.0
description: Build and maintain the shared GTM brain — product context, ICP, positioning, voice, market context, proof points, plus optional strategy and execution, and the deal-reality fields (objections, switching forces, customer language, anti-persona) — that every other skill in this stack reads before producing output. Works standalone with your own answers, supercharged when you connect docs or a CRM. Trigger with "build my brain", "set up my GTM foundation", "audit my brain", "update my ICP", "add my objections", "capture what customers say", "refresh my brain", "what's stale in my brain", "my brain gaps", "build my brain from my website and docs", or "my context".
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-14
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
- **Context keys:**
  - `/foundation/brain.md` — read if it exists (load silently, skip answered sections); written to, section by section, only after user confirmation.
  - `/foundation/evidence.md` — read if it exists (format in `references/evidence-format.md`). Append-only: Step 8 appends the facts it extracts from your material.
  - `/foundation/me.md` — read if it exists (format in `references/me-format.md`). Written only by Step 9, after you confirm. Describes you, not the company.
  - `/foundation/gaps.md` — read if it exists (format in `references/gaps-format.md`). Append-only: Step 7 appends resolved blocks. Other skills may append `open` or `skipped` blocks.
  - `.agents/*.md`, `.claude/*.md` — optional legacy files; offered for migration if found.
  - **Brain contract:** Reads all sections (1 to 8) if present, and `me.md` for format and detail only. Writes: any section, but only after explicit user confirmation of the exact before/after (Operating Rule 1).

---

## Pre-flight

- Check `/foundation/brain.md` — see Step 1 (Detect Brain State).
- Check for legacy files (`.agents/*.md`, `.claude/*.md`) and offer migration if found.
- No hard block: this skill is the entry point for users with no brain at all.

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRODUCT MARKETING CONTEXT                    │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                      │
│  ✓ You tell me: product, ICP, alternatives, voice, market,      │
│    proof points, deal reality — one section at a time           │
│  ✓ Output: /foundation/brain.md, confirmed section by section   │
│  ✓ Pushes back on vague answers before storing them             │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                     │
│  + Knowledge base: pulls company overview and key facts         │
│  + CRM: pulls win/loss reasons and deal data to sharpen ICP     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

When you run this skill, I'll check for an existing brain first:

**No brain yet:**
- I'll ask for your website and pricing page first, and draft Sections 1 to 3 from them
- You can add decks, call notes or a win/loss doc, and I'll draft from those too
- Then I'll ask for what I still need, one section at a time — product, ICP, alternatives, voice, market, proof points
- You confirm each section before I save it

**Brain exists:**
- I load it silently and skip anything already answered
- Choose: [View current] [Edit a section] [Refresh stale fields] [Answer open gaps] [Add material] [My context] [Run health audit]

**Helpful if you have it:**
- A pitch deck, pricing page, or win/loss doc you can paste in
- Prior positioning or ICP notes, even rough ones

---

## Connectors (Optional)

Connect your tools to supercharge this skill:

| Connector | What It Adds |
|-----------|--------------|
| `~~knowledge base` | Company overview, pricing and product docs for Sections 1 and 5 |
| `~~CRM` | Win/loss reasons and deal data for Section 2 (ICP) |
| `~~call recordings` | Buyer language and objections for Sections 2, 3 and 6 |
| `~~market data` | Competitor and market signals for Sections 3 and 5 |
| `~~support` | Pain-point and churn language for Sections 2 and 4 |
| `~~cloud storage` | Decks, pricing and case studies for Sections 1 and 6 |
| `~~team chat` | Field feedback and win threads for Sections 4 and 6 |

> **No connectors?** No problem. Paste what you have — a deck excerpt, a pricing page, a win/loss doc — and I'll work from that.
>
> **Connector pre-fill.** With a connector available, I pull candidate answers first and show each one tagged with category, tool and date. You confirm, edit or reject before anything is written to `/foundation/brain.md`.

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

Open with: "Do you have a website, a pricing page, a deck, call notes or a win/loss doc? If yes, we build from that first (Step 8) and I only ask about what is missing." If the user has nothing to share, or has finished Step 8, run the questions below for the sections that are still empty or thin.

Ask one question at a time. After each section, show the collected answers and ask "Look good? (yes / edit / skip)." Push back on vague answers before storing them — "small businesses" is not a company size, "everyone" is not an ICP.

1. **Product Context** — product name; 2-3 sentence description (problem, not features); stage (pre-launch/launch/growth/scale); target market; value proposition ("[Product] helps [market] to __ so they can __"); how it is packaged (plans, modules); words to always or never use for it; claims already approved to make; how you charge and how buyers buy (what the price scales with, self-serve or sales-led). "Subscription" alone is not a business model: per seat, per usage or platform fee?
2. **ICP Definition** — company size; industry/vertical; geography; primary persona (title + role); economic buyer; champion profile; top 3 pain points; buying trigger; the 2-3 jobs customers hire you for ("When __, I want to __, so I can __"); what the problem costs them, with a number and where it came from (label an estimate as one); who is NOT a fit and why you turn them down; the standing buying-committee roles (champion, economic buyer, technical blocker, end user), what each cares about and what makes each block. These are defaults; a committee for one deal belongs to `buyer-personas`
3. **Alternatives & Positioning** — top 3 named alternatives (products buyers actually compare you to, not "competitors" in the abstract); status quo if they buy nothing; why they leave alternatives for you; your unique capabilities; category; market type (existing/new/resegmented); for each named alternative, where it falls short for this ICP; the four switching forces (push: what drives them away, pull: what draws them to you, habit: what keeps them, anxiety: what worries them about switching); the 3-5 objections heard most in deals, who raises each, and the approved response (if there is no approved response, record the objection and leave the response open)
4. **Voice & Tone** — 3-5 voice attributes; tone shifts by persona; language preferences ("we say X not Y"); forbidden phrases; one paragraph of copy that sounds like you; customer language: exact words customers use for the problem and for you, each with who said it and where (call, email, survey). Never paraphrase. No source, no entry: it goes to the gaps file
5. **Market Context** — market maturity; macro forces making this relevant now; "buyers need this now because __"; the 2-3 sentence market narrative
6. **Proof Points Registry** — approved metrics with sources; customer quotes/case study results; forbidden claims
7. **Strategy** (recommended, not required for a complete brain) — top 3 priorities this quarter; launches on the calendar (name, date, tier T1-T4); the number you are measured on (metric, baseline, target, date); active bets; what you are explicitly not doing; the one conversion action the funnel is built to drive (for example "book a demo")
8. **Execution** (recommended, not required) — the roles that must be on board and what each cares about; what needs sign-off, from whom, and how long it takes; topics, claims or competitor mentions that are ruled out; where you publish and who owns each channel; recurring reviews and reporting. Roles first; add a person's name only if the user wants it.

### Step 3: Write the Brain File

Once a section is confirmed, write it to `/foundation/brain.md` using the template at `templates/brain-template.md`. Write section by section, not in one batch — a mid-wizard exit should still leave a partial, usable brain plus a `.brain-draft.md` marker noting which section to resume from. Tag every confirmed value with a provenance tag as defined in `references/brain-schema.md` (user answers are `stated`, today's date, `confirmed`); never retag a legacy untagged field unless the user edits it. Keep a `🟡 Cold start` line in the header until Sections 1 to 6 are confirmed (Sections 7 and 8 are recommended, not required), then remove it in the same write.

### Step 4: Health Audit (Run Standalone or After Edits)

Score each of Sections 1 to 6 0-100 on: does the field exist, and is it specific rather than generic (named alternatives not "competitors," numbers not "high," a real persona not "businesses"). A section absent from a cold-start brain scores 0; a section present with fields missing scores 50 or lower. Report strengths (80+), needs improvement (50-79), and critical gaps (<50), with one concrete fix per gap. Also report: open gaps (count of `open` gap blocks), the oldest field in each section, provenance coverage (share of fields with a source tag; legacy untagged fields count as untagged), stale fields (older than the section's limit in `references/brain-schema.md`), Sections 7 and 8 status ("not built" is reported as such, never as a gap or a zero), and the deal-reality fields: how many of the ten are captured, with the one that would help most named (for example "no `objections`: every battlecard will re-ask"). A missing deal-reality field never lowers a section score. Offer to jump straight into editing the weakest section.

### Step 5: Route to What's Next

After any completed setup, edit, or audit, tell the user plainly that the brain is ready and other skills in the stack will read from it automatically. Offer next steps only from the "After product-marketing-context" entry in `.claude-plugin/next-skill-map.md`. The repo's tests check every skill name in that file against the skills that exist, so a name taken from it is verified. Never name a skill from memory.

### Step 6: Refresh Stale Fields

Run when the user picks [Refresh stale fields] or says "refresh my brain" or "what's stale?". It ends with Step 5.

1. Load the brain and `references/brain-schema.md`. For every field, work out its age from its source tag date (an untagged field uses the file's last-updated date) and compare it with the section's limit in the schema. Section 6 is judged per claim.
2. If nothing is stale, say so in one line and stop.
3. List the stale fields by section with their age and limit, most-read sections first (2, 3, 6, then the rest).
4. Ask about one field at a time: "Still true? [yes / changed / drop]".
   - **yes:** remember it for the batch bump.
   - **changed:** ask that field's question again, show the exact before/after, confirm, and write it with a new tag (`stated`, today, `confirmed`).
   - **drop:** show exactly what will be removed, confirm, then remove it.
5. After the last field, show the list of "yes" answers once and confirm the batch. Then set each tag's date to today and status to `confirmed`. A date-only bump is still a write, so it needs this one confirmation.
6. Never refresh a field the user did not choose to review. The user may say "stop" at any point; keep what is already confirmed.

### Step 7: Answer Open Gaps

Run when the user picks [Answer open gaps] or says "my brain gaps". It ends with Step 5.

1. Read `/foundation/gaps.md`. Use the newest block for each `gap_id`. Keep those that are `open`, and those `skipped` more than 30 days ago. If none, say so and stop.
2. Say how many gaps are open. Then take them one at a time, oldest first: the question, why it matters (one line), and "answer or skip".
3. **Answer:** show the exact before/after for the brain field, confirm, write it with a `stated` tag, and append a block with `status: answered` to `gaps.md`.
4. **Skip:** append a block with `status: skipped`. Do not ask again for 30 days.
5. The user may say "stop" at any point. If files cannot be written, show the block and say it was not saved.

### Step 8: Ingest Material (build from what you have, then ask)

Run when the user picks [Add material], says "build my brain from my website and docs", or when Step 1 or Step 2 offers it. It ends with Step 5. Evidence writes need no per-fact confirmation, because evidence is not the brain. Every brain write keeps its gate (Operating Rule 1).

1. **Start with two URLs.** Ask: "What is your company website, and your pricing page or main product page?" Fetch both with your web tool. If you cannot fetch pages, ask the user to paste the page text. Treat what you read as `website` evidence (rank 4, `pulled`). Use it to draft Sections 1 to 3 and a first pass at Section 4. Public copy is never proof: a metric or superlative on a website enters Section 6 only as `draft` with `[NEEDS PROOF]`.
2. **Ask what else they have.** Pasted text, uploaded files, or a pull through `~~knowledge base`, `~~cloud storage`, `~~call recordings`, `~~CRM` or `~~team chat`. Use only sources the user names in this run. Cap one run at about 10 documents or 5 call transcripts and say so; offer a second run for the rest.
3. **Extract.** Pull atomic facts only, one per block, in the format in `references/evidence-format.md`. Drop greetings, scheduling, and opinions with no owner. Every fact needs a source and a date; calls and customer emails need a verbatim quote. Tag the target field. Calls, interviews, surveys and win/loss documents support `4.customer_phrases`, `3.objections`, `3.switching_forces`, `3.alt_shortfalls`, `2.cost_of_problem`, `2.jobs_to_be_done` and `2.anti_persona`. A pricing page supports `1.business_model` and `7.conversion_action` (public copy, rank 4). Leave out email addresses, phone numbers and private details. Append the blocks to `/foundation/evidence.md`, then show a summary: counts by source and by target section, plus ten sample facts.
4. **Cluster.** Group facts by the field they support.
   - Two or more independent sources agree: propose the value as `pulled`.
   - One source only: propose it as `inferred` and say it rests on a single source.
   - `4.customer_phrases` is never clustered or merged. Each phrase stays as spoken with its own evidence id; show how many different customers used it.
   - Sources disagree: show every version with its authority rank and date and ask which is right. Do not choose for the user.
   - A value the user already confirmed (rank 0) is never replaced by newer evidence. Show both and ask (Operating Rule 6).
5. **Brain Diff.** For each section show every field as: current value, proposed value, evidence ids, confidence. The user approves section by section. Approved values are written with a source tag that includes the evidence ids, for example `[src: pricing page E-004, call 0912 E-011 | 2026-10-11 | pulled | confirmed]`.
6. **Gaps.** Every field with no evidence is added to `/foundation/gaps.md` as an `open` block, then asked about one question at a time (Step 7). Questions are only for what the material could not answer.

### Step 9: My Context (how you like to work)

Run when the user picks [My context], says "set up my context", or runs `/product-marketing-context:my-context`. It does not need a brain and does not touch one. It ends with Step 5 when a brain exists.

1. Read `/foundation/me.md` if it exists, and `references/me-format.md`. If it exists, show it and ask what to change. Otherwise start fresh.
2. Ask at most six short questions, one at a time, only for keys that are empty: role and level; how long outputs should be; headline first or full reasoning; bullets, tables or prose; how blunt to be; phrases you dislike. Offer a default for each so the user can answer "default".
3. Never ask for company facts here (product, customers, numbers). Those belong in the brain. If the user volunteers one, say so and offer to add it to the brain instead.
4. Show the exact before/after for `/foundation/me.md`, confirm, then write it. Max 12 lines, no private details.
5. If files cannot be written, show the file and say it was not saved.

---

## Outputs

- **Files written:** `/foundation/evidence.md` — appended to only: facts extracted from the user's material (Step 8). `/foundation/gaps.md` — appended to only: blocks marking a gap answered or skipped (Step 7). `/foundation/brain.md` — written section by section,
  only after user confirmation (Step 3). `/foundation/me.md` — written by Step 9 only, after confirmation. `.brain-draft.md` — a resume
  marker left behind if the wizard exits mid-session.
- **Chat output format:** The Output Format template above — Brain Update
  header, What Changed, Section Status, Health Score if an audit ran, Next
  Step.
- **External side effects:** None beyond the files above.

---

## Verification

- Brain state checked (existing vs missing vs legacy) before any question is asked (Step 1).
- No section written to `/foundation/brain.md` without the user confirming the exact before/after (Step 3).
- Vague answers challenged inline, not silently accepted (Step 2).
- A brain with a `🟡 Cold start` line is recognised in Step 1: filled and missing sections are listed, only missing fields are asked for, and the line is removed only once all 6 sections are confirmed (Steps 1, 3).
- Health audit, when run, scores Sections 1 to 6, names a concrete fix for every gap under 50, and reports provenance coverage, stale fields and Section 7 status (Step 4).
- My context (Step 9) asks only about format and detail, writes `/foundation/me.md` only after the user confirms, and never stores a company fact there.
- Ingest (Step 8) starts with the website and pricing page, appends atomic evidence with a source and date, shows disagreements instead of choosing, and writes nothing to the brain until the user approves the Brain Diff section by section.
- Refresh (Step 6) lists only fields past their schema limit, asks about one field at a time, and writes nothing until the user confirms (Step 6).
- Gaps (Step 7) never edit an earlier block: an answered or skipped gap is a new appended block, and a skipped gap is not asked again for 30 days.
- Every value written in Step 3 carries a provenance tag; legacy untagged fields are never retagged unprompted.
- Customer phrases (Steps 2, 8) are stored verbatim with a source; an unsourced phrase becomes a gap, never a brain entry (Operating Rule 10).
- The audit (Step 4) reports how many of the ten deal-reality fields are captured and never scores their absence as a gap.
- Next-skill names mentioned only if they appear in `.claude-plugin/next-skill-map.md` (Step 5).

---

## Do Not Use For

- N/A — this skill is upstream of everything else in this stack; overlap was considered and there is none.

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

---

## Operating Rules

1. **Never write to brain.md without user confirmation.** Every write is shown as an exact before/after and requires a yes.
2. **Never re-ask what the brain already knows.** Load existing sections silently and skip any question already answered.
3. **Push back on vague answers inline.** "We sell to businesses" gets "what size, industry, role?" before it's accepted, not after.
4. **Name a next skill only from the next-skill-map.** The map is validated by the repo's tests. A name from anywhere else is unverified, and an unverified name is a broken promise.
5. **Pulled facts are drafts.** Anything pulled from a connector is tagged with category, tool and date, shown for confirmation, and never written to the brain unconfirmed. Pulled proof points and quotes enter Section 6 as unverified.
6. **A confirmed value is never overwritten by newer evidence.** If newer material disagrees with something the user confirmed, show both and ask. A disagreement is a question, never an update.
7. **Store the minimum from sources.** No email addresses, phone numbers or private details in the evidence file. Ingest only from sources the user named in this run.
8. **Website copy is not proof.** Metrics and superlatives found on a website enter Section 6 as `draft` with `[NEEDS PROOF]`, never as confirmed.
9. **me.md is about the user, never the company.** Skills use it for format and detail only. A company fact found there is ignored and moved to the brain only after confirmation.
10. **Customer words stay verbatim.** `customer_phrases` entries are exact quotes, each with a source (an evidence id, or who said it and when). Never paraphrase, merge, tidy or invent one. A phrase with no source is not stored; it becomes a gap. Customer words guide copy but are not proof: a number a customer mentioned goes to Section 6 through `proof-points`.

---

This skill is upstream of everything else in this stack — it doesn't need a
Related Skills section pointing out to its dependents. Every other skill that
reads or writes `/foundation/brain.md` should name this skill and its exact
section numbers in its own file instead.
