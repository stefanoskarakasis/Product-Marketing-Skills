# Marketing content

Moved verbatim from `SKILL.md`.

## Marketing content workflow (moved verbatim)

### Marketing content

Formats: blog post, social post, newsletter, landing page, press release, case study.

**Step 1: Gather inputs.** Take what the user gave you and what the brain holds, then
check each item:

| Input | Comes from | Ask the user? |
|---|---|---|
| Format | the request | only if the Route table can't settle it |
| Topic | the request | yes, if missing |
| Audience (role, industry, seniority, pain) | brain Section 2, else the request | only if neither has it |
| Key messages (2 to 4) | brain Section 3, else the request | only if neither has it |
| One goal (the single action the reader should take) | the request | yes, if missing |
| Proof (real stats, quotes, customer names, results) | brain Section 6, else the request | yes for case studies and press releases, and for any copy with a numeric claim |
| Tone | brain Section 4, else mirror a pasted sample, else plain and direct | no |
| Length | the format's default in its reference file | no; state the default you used |

Each format also has extras (platform for social, keyword and search intent for blog,
news hook for press release, customer approval for case study, main alternative and
objections for landing page). They are listed in that format's reference file.

For a case study, check `/context/customer-stories.md` (read only). If it holds a packet
for this customer, draft from it and keep its `[NEEDS APPROVAL]` flags. If not, offer
`customer-stories` once for the interview and the stat and quote checks, then continue
here if the user declines.

**Step 2: Ask once, or assume.** If nothing needs asking, go on. If something does, send
ONE message that lists only the missing items, numbered and short. Never ask about tone
or length. If the user says "just draft it", skip the questions and open the draft with
an **Assumptions** list so every guess is visible. This intake rule applies to the six
marketing formats only. Everything else keeps the Guardrails rule: ask one question
only if the work is blocked.

**Step 3: State the brief.** Three lines: reader, goal, angle. Then draft.

**Step 4: Draft.** Open `references/<format>.md` (`blog-post`, `social-post`,
`newsletter`, `landing-page`, `press-release`, `case-study`) and follow its structure.
Blog posts and landing pages also use `references/seo-checklist.md`.

**Step 5: Honesty rules.** These beat every other instruction in this skill.
- Never invent a statistic, quote, customer name, date, result, search volume, or
  attribution. Use `[PLACEHOLDER: what is needed]`. Quotes use `[QUOTE: speaker, the point
  they should make]`, and a quote is written out only when the user supplied the exact words.
- Anything on the brain's forbidden-claims list never appears.
- Words like "first", "only", "#1" and "best" need support from the user or the brain.
  Without it, cut them or use a placeholder.
- Promise only what the product does, per the brief and the brain.

**Step 6: Self-check, silently.** Run the usual check against **Words to Cut**,
**Patterns to Cut** and the **Voice and Non-Robotic Guarantee**, plus these:
- Every claim is supplied by the user or the brain, or it is a placeholder.
- No em dashes in landing pages, social posts, or subject lines; two at most in longer pieces.
- Each headline and section opener fails the portability test (a competitor could not
  paste it unchanged).
- One primary CTA.
- The ending is a concrete last point or the CTA, not a recap or a kicker.
- Length is inside the target.
Fix what fails and check again. Do not show a draft that has not passed.

**Step 7: Output.**
1. The draft, in the format's structure.
2. Notes: the voice applied (brain Section 4, a pasted sample, or the default), the
   assumptions, and the placeholders to fill, as a list.
3. One question: revise a section, change the tone, or adapt it to another format?
   For landing pages and case studies, also offer a Behavioral Messaging Review.
