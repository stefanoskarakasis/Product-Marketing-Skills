---
name: brand-voice
version: 1.0.0
description: >
  Builds a persona-adaptive Voice & Tone guide — brand attributes, tone
  shifts by buyer type and channel, forbidden language — then deepens
  brain Section 4 in place. Trigger with "how should we sound", "voice
  guide", "our copy feels off", "we sound like everyone else", "adapt
  tone for", or any request to define, apply, or audit how the brand
  communicates.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-31
---

# Brand Voice

## How This Works

Voice is who you are — it doesn't change. Tone is how you show up in a
specific moment — it shifts by buyer and channel, intentionally, not
randomly. This skill builds a voice guide that survives contact with a
blank page: every trait gets an example, every persona gets a tone
profile, every channel gets a table row. It deepens your brain's existing
Section 4 in place rather than creating a second voice file — one source
of truth stays intact for every downstream writing skill.

**Step 0** — Load brain Section 4 (current voice guide, however thin),
Section 2 (ICP/personas, for tone-by-persona grounding), and any
guardrails from `/context/meta-patterns.md`.

**Step 1** — Establish brand personality and its edges: 3-4 words that
couldn't apply to a competitor, plus what the brand explicitly rejects.

**Step 2** — Map tone by persona: for each buyer in the committee, what
they care about, how they prefer information, what makes them distrust a
vendor immediately, what makes them lean in. Never pre-filled — every
committee is different.

**Step 3** — Build the channel tone table and forbidden-language list,
then run the one-sentence voice test against both.

**Step 4** — Deepen brain Section 4 with the guide (on user confirmation).

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Defining or sharpening how the brand sounds — voice
  attributes, tone shifts by persona or channel, forbidden language,
  or auditing copy that's drifted off-brand.

- **Not for:** Positioning statement or messaging hierarchy itself → use
  `positioning-messaging`. Writing the actual copy → no dedicated
  drafting skill exists yet in this repo; produce copy within
  `positioning-messaging`'s own output modes, using this skill's voice
  guide as input. Buying-committee mapping → `buyer-personas`, run first
  if tone-by-persona needs real committee data instead of guessed roles.

- **Example prompts:**
  - "How should we sound on LinkedIn vs. a sales deck?"
  - "Our copy feels off — voice audit"
  - "We sound like everyone else"
  - "Write this in our voice for the Champion persona"
  - "Build our voice guide"

---

## Inputs

- **Args:** None required — the skill asks one question at a time if
  nothing is on file. 3-5 samples of existing copy speed up the AUDIT
  path but aren't required for BUILD.
- **Defaults:** No brain, or Section 4 still empty → run full BUILD.
  Section 4 populated → load silently, offer [View current] [Update]
  [Audit for drift] [Apply to a specific piece].
- **Context keys:**
  - `/foundation/brain.md` — read Sections 2 and 4 if present; written to
    (Section 4 only) after explicit user confirmation of the exact
    before/after.
  - `/context/meta-patterns.md` — guardrails, read at Step 0.

---

## Pre-flight

- Check `/foundation/brain.md` Section 4 — if populated, this is an
  UPDATE, AUDIT, or APPLY, not a fresh BUILD.
- If `/foundation/brain.md` doesn't exist at all, surface once: "No brain
  found. You can still run this skill, but output will be less precise.
  Run product-marketing-context first for sharper results. Continuing."
  No hard block.

---

## Steps

**Step 1 — Brand personality and its edges.**
Ask for 3-4 words describing the brand as if it were a person at a
professional dinner — reject defaults like "authentic" or "innovative."
Challenge: could a competitor claim the same words? If yes, push for a
reference brand that gets it right and one that gets it wrong. Then ask
what the brand explicitly rejects — name brands or archetypes that feel
wrong, and why. "Not too salesy" isn't specific; ask what salesy looks
like in this market.

**Step 2 — Tone by persona.**
If a recent `buyer-personas` session exists, load its committee roles
instead of re-asking. Otherwise ask directly: who's on the committee, what
they care about professionally, how they prefer to receive information,
what makes them distrust a vendor immediately, what makes them lean in.
Rate the brand on four dimensions (Formality, Warmth, Boldness, Energy) —
push past "casual but professional," which is everyone's answer; ask for
a reference point (casual like Slack, or casual like a boutique
consultancy?).

**Step 3 — Channel table and forbidden language.**
List the channels in active use (homepage, sales deck, outbound email,
LinkedIn, thought leadership, talk tracks, customer comms). Persona takes
precedence over channel when both apply — channel adapts the voice, it
doesn't replace persona tone. Every Do/Don't needs a concrete example
before it's encoded — "be direct" is useless without "e.g., write X not
Y." Draft the one-sentence voice test: "[Brand] sounds like [descriptor]
— always [consistent quality], even when [the tone shifts]." Exit check —
every persona profile and channel entry must pass this sentence before
the guide ships.

**Step 4 — Deepen brain Section 4 on confirmation.**
Show the user the exact before/after for Section 4 before writing
anything. On confirmation, write:

```markdown
## Section 4: Voice & Tone

**Brand Voice Attributes:**
{{3-4 words, plus the one-sentence voice test}}

**Tone Shifts by Persona:**
{{per-persona block: cares about / prefers / distrust trigger / lean-in
  trigger / tone dimension ratings}}

**Language Preferences:**
{{channel table — channel, primary audience, tone goal}}

**Forbidden Phrases:**
{{explicit list, with the "why" for each}}

**Tone Example (Copy that captures our voice):**
> {{a real example line that passes the voice test}}
```

Never write silently — this is a shared source of truth every downstream
writing skill reads.

**Step 5 — Learning Close.**
Append a row to `/context/skill-sessions.md`:

```yaml
skill: brand-voice
session_date: {{date}}
pattern: "{{what surprised you, a tone-drift pattern AUDIT caught, or
  'none' if nothing notable happened — never skip the row}}"
source: {{surprised/wrong/missing/n.v.t.}}
```

---

## Outputs

- Brain Section 4 deepened in place (on confirmation only)
- A stated voice test sentence, persona tone profiles, channel table, and
  forbidden-language list — not buried in prose
- Session logged to `/context/skill-sessions.md`
- **External side effects:** n.v.t.
- **Next skill:** check `next-skill-map.md` for "After brand-voice" and
  surface that prompt.

---

## Verification

- Brand voice stated as one paragraph — the anchor everything attaches to
- Every persona tone profile is complete with at least one concrete Do
  and Don't example — no abstract-only instructions survive
- Channel table populated only for channels actually in use, persona
  takes precedence over channel
- Forbidden language list is explicit and named, not implied
- One-sentence voice test passes across every profile before delivery
- Brain Section 4 write shown to the user before it happens, written only
  on confirmation
- Session logged with all four fields, `pattern: none` written explicitly
  if nothing notable happened — the row is never skipped

---

## Do Not Use For

- **positioning-messaging** — when the task is producing the positioning
  statement or messaging hierarchy itself, not the voice it should be
  written in. Run this skill first if Section 4 is thin, then that one.

- **product-marketing-context** — when the task is the full brain build
  from zero, or any section other than 4

- **buyer-personas** — when the task is mapping who's in the room, not
  how to sound when writing to them

- **market-context** — when the task is why now, not how to sound saying it

---

## Operating Rules

1. **Load brain Section 4 first.** Don't re-ask what's already answered.
2. **Never write to Section 4 without showing the exact before/after
   first.** No silent writes, ever.
3. **Never pre-fill the buying committee.** Every committee is different;
   pre-assumed personas produce generic tone guidance. If a recent
   `buyer-personas` session exists, load it — don't guess.
4. **Every Do/Don't needs an example.** Abstract instructions don't
   survive contact with a blank page.
5. **Persona beats channel when both apply.** Channel adapts voice, never
   replaces persona tone.
6. **Reject generic personality traits.** If a competitor could claim the
   same 3-4 words, push for specificity before encoding.
7. **Run the one-sentence voice test on every profile before delivery.**
   Same company, different room — or it doesn't ship.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Brand personality specific | Not competitor-claimable; has a reference brand | Yes |
| Persona profiles complete | Every profile has Do/Don't with examples | Yes |
| Channel table populated | Only for channels in active use | Yes |
| Forbidden language explicit | Named list, not implied | Yes |
| Voice test passes | Every profile passes the one-sentence test | Yes |
| Confirmation before write | Exact before/after shown, user confirmed | Yes |
| Learning Close complete | Four-field row appended, never skipped | Yes |

---

## Commands

### /build
Run full BUILD: personality, edges, persona tone mapping, channel table,
forbidden language, voice test.

### /update
Refresh Section 4 after a new persona, new channel, or brand evolution —
asks only for what's new.

### /audit
Score 5-10 recent copy samples across 3+ channels against the four tone
dimensions per persona. Identify drift patterns and recommend targeted
updates — not a full rebuild unless drift is systemic.

### /apply [persona] [channel]
Generate on-brand copy for one persona and one channel using the current
guide. Runs the voice test on the output before returning it.
