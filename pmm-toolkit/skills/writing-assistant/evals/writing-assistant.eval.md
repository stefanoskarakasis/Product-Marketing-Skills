---
skill: writing-assistant
test_count: 15
---

# Writing-Assistant Evals

Tests 1 to 3 cover the original rewrite behavior and are the regression set: they must
pass unchanged. Tests 4 to 15 cover routing, marketing content, and audit.

## Test Case 1: With brain (voice match)

**Input:**
Brain exists with voice "authoritative, data-driven, concise". User: "Rewrite this: We
help companies grow faster with our amazing platform"

**Expected output includes:**
- Rewritten copy that matches "authoritative, data-driven, concise"
- Jargon removed and a data-driven framing, with placeholders instead of invented numbers

**Expected output excludes:**
- Any marketing-content intake questions

**Pass condition:**
Voice attributes from the brain are visibly applied and the copy is tighter than the original.

---

## Test Case 2: Without brain (manual voice)

**Input:**
No brain and no legacy file. User: "Rewrite this email to be more concise: [wordy email]"

**Expected output includes:**
- A rewrite roughly 30% shorter, with clear improvements
- At most one non-blocking note that no PMM context was found

**Expected output excludes:**
- A blocking question about voice

**Pass condition:**
The email is rewritten shorter with a neutral voice, and the user is not interrogated.

---

## Test Case 3: Explain changes

**Input:**
"Review this copy: [long wordy text]"

**Expected output includes:**
- A sendable rewrite
- Only the changes that matter explained (removed, reordered, clarified)

**Expected output excludes:**
- A line-by-line changelog of every edit

**Pass condition:**
Rewrite plus a short explanation of the changes that mattered.

---

## Test Case 4: Slack rewrite stays zero-friction (regression)

**Input:**
"Tighten this Slack update: [three rambling paragraphs about a launch delay]"

**Expected output includes:**
- A shorter update with the point first
- A sendable result in one response

**Expected output excludes:**
- Questions about audience, goal, proof, keywords, or format
- Marketing structure such as headline options or an SEO block

**Pass condition:**
The internal message is rewritten without any marketing-content intake.

---

## Test Case 5: Email vs newsletter routing (edge case)

**Input:**
"Write an email about the Q4 launch."

**Expected output includes:**
- One question: "One person, or a list?" (or a draft on the email path with that
  assumption stated)

**Expected output excludes:**
- Newsletter structure (subject options, preview text, footer reminder) without
  confirming it is a list

**Pass condition:**
The ambiguous request is resolved by one short question or a stated assumption, and never
by silently choosing the marketing path.

---

## Test Case 6: Blog post with full inputs and brain

**Input:**
Brain with Sections 2, 3, 4 and 6 filled. User: "Write a blog post on reducing churn in
onboarding. Keyword: onboarding churn. Goal: book a demo. Use our approved stats."

**Expected output includes:**
- Three headline options including the keyword, a short intro with the keyword, three to
  five H2 sections, a closing CTA to book a demo
- An SEO block with meta description (about 160 characters or fewer) and URL slug
- Statistics taken only from brain Section 6
- A Notes list naming the voice applied

**Expected output excludes:**
- A question that the brain already answers (audience, tone)
- Invented search volume or difficulty figures
- A recap ending

**Pass condition:**
A complete, structured post with an SEO block, using only registry numbers, with no
unnecessary questions.

---

## Test Case 7: Blog post with minimal input (one batched intake)

**Input:**
No brain. User: "Write a blog post about our new reporting feature."

**Expected output includes:**
- ONE message listing only the missing items (audience, key messages, goal, proof,
  keyword), numbered and short

**Expected output excludes:**
- Questions about tone or length
- A draft produced before the questions are answered
- Several separate rounds of questions

**Pass condition:**
Exactly one batched intake that asks for what is missing and nothing else.

---

## Test Case 8: "Just draft it" shows assumptions

**Input:**
No brain. User: "Write a landing page for our scheduling tool. Just draft it."

**Expected output includes:**
- An Assumptions list at the top (audience, goal, alternative, objections)
- Three headline options and the landing-page structure
- Placeholders such as `[PLACEHOLDER: customer stat]` where proof is needed

**Expected output excludes:**
- Intake questions before the draft
- Invented statistics, customer names, or testimonials
- More than one primary CTA
- Em dashes

**Pass condition:**
A full draft appears immediately, with every guess visible and every unsupported claim a
placeholder.

---

## Test Case 9: Landing page uses the brain's alternative and proof

**Input:**
Brain with Section 3 naming "spreadsheets" as the main alternative and Section 6 with one
approved metric and one forbidden claim ("#1 in the market"). User: "Draft landing page
copy for the free trial."

**Expected output includes:**
- Copy that positions against spreadsheets
- The approved metric, used as written
- A headline that passes the competitor test

**Expected output excludes:**
- The forbidden claim or any "#1" or "best" wording
- A second competing CTA

**Pass condition:**
The page uses the brain's alternative and proof, and the forbidden claim never appears.

---

## Test Case 10: Press release with no news hook

**Input:**
"Write a press release about how we think about customer onboarding."

**Expected output includes:**
- One sentence saying there is no news hook
- An offer to write a blog post or announcement post instead

**Expected output excludes:**
- A full press release with a manufactured announcement

**Pass condition:**
The news gate fires, and no newsworthiness is invented.

---

## Test Case 11: Press release never invents a quote

**Input:**
"Press release: we launched Atlas 2.0 today, announced by our CEO Dana Rivera. Boston.
No quotes provided."

**Expected output includes:**
- Release line, headline, Boston dateline, a lead covering who, what, when, where, why
- A quote written as `[QUOTE: Dana Rivera, CEO, the point to make]`
- Boilerplate and media contact as placeholders when not supplied
- A closing `###`

**Expected output excludes:**
- Any sentence in quotation marks attributed to Dana Rivera
- Invented figures or customer names

**Pass condition:**
No words are put in a named person's mouth, and every gap is a placeholder.

---

## Test Case 12: Case study without proof (gate)

**Input:**
"Write a case study about Acme using our product." No results, no permission details.

**Expected output includes:**
- A skeleton with placeholders for results and the quote
- A label at the top: "Not publishable until the items below are filled."
- A list of what is needed (metrics with baseline and timeframe, permission, quote)

**Expected output excludes:**
- Any invented percentage, dollar figure, or customer quote

**Pass condition:**
The draft is clearly marked unpublishable and contains no fabricated results.

---

## Test Case 13: Social post needs a platform (edge case)

**Input:**
"Write a post announcing our new feature." No platform given, no blog signals.

**Expected output includes:**
- A single question asking which platform (or whether it is a blog post)

**Expected output excludes:**
- A guessed-platform draft with hashtags

**Pass condition:**
The missing platform is asked once, and with "LinkedIn" supplied the next reply is a
LinkedIn-shaped post with a strong first line, one CTA, and no em dashes.

---

## Test Case 14: Audit names patterns and does not rewrite

**Input:**
"Does this read as AI? We leverage a seamless platform to unlock transformative growth.
It's not just a tool. It's a movement."

**Expected output includes:**
- Each pattern named with the quoted line: the banned words "leverage", "seamless",
  "unlock", "transformative" and the "not just X, it's Y" pattern
- A short fix for each
- The closing offer "Want me to edit it?"

**Expected output excludes:**
- A rewritten version of the text
- A score, or a guess about whether an AI wrote it

**Pass condition:**
Patterns are listed with quotes and fixes, with no rewrite and no verdict on authorship.

---

## Test Case 15: Self-check keeps banned words out and falls back to the legacy file

**Input:**
No brain, but `.agents/product-marketing-context.md` exists with a Brand Voice section
("plain, direct, no hype"). User: "Write a newsletter issue about our September
release. Main point: the new import tool saves setup time. Goal: try the import tool.
List: customers on a monthly plan. Just draft it."

**Expected output includes:**
- The voice drawn from the legacy file's Brand Voice, named in the Notes
- Three subject line options, preview text, one primary CTA, a footer reminder
- A placeholder for any time-saved figure that was not supplied

**Expected output excludes:**
- The words "leverage", "seamless", "unlock", "robust", "game changer"
- An invented time-saved number
- A "no PMM context found" notice, since the legacy file was found

**Pass condition:**
The legacy fallback is used, the draft passes the banned-word check, and no figure is invented.
