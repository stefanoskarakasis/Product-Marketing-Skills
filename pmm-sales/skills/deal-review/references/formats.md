# Formats

Read at Step 9. Lead with what the seller does, then why. Bold, never italics: `*x*` in Slack, `**x**` elsewhere. One fact per line; bullets for anything with two or more parts. Empty sections never print. Every line carries its source in words and a date.

Emoji only for a section (⚡ do now, ⚠️ contradictions, ❓ questions, 📋 paste-ready), an action (⚡) or a status (✅ validated · 🟡 stated · ❌ not found · ➖ not assessed · 🕰️ stale). None in running text. Trend in words: up, flat, down, new.

Header sizes: `#` deal title, `##` sections, `###` each action or block. Body stays plain text. Slack has no headers: a bold label on its own line.

## Slack reply (hard cap 100 words)

```
*[Deal]: [one verdict label], [N] days to [buyer's dated event]*

⚡ *Do first, today*
[What the buyer is waiting on from us, one line.] Send:
> [exact line to paste]

⚡ *Then* (max 2)
• [Move] · by [date]
• [Move] · by [date]

*Risk:* [what kills it, one line]
*Fix in your CRM:* [field]: [what the calls show] (max 2 items)

*Next:* want me to draft the message, or post the full review?
```

- No buyer-dated event: headline is the verdict alone; never invent a date.
- Over 100 words means cut: drop Risk first, then the second "Then" bullet, then the CRM line. No walk-away test, worksheet or contradiction table in Slack.
- Print one confidence line only when confidence is low ("Confidence: low, rests on seller notes"); when it is medium or high print nothing. Missing context adds one line: ❓ *To sharpen this:* [one combined question].
- The last line is always one plain question that offers the next step; any natural yes works, and nothing runs unasked. Drafting hands off to `writing-assistant`. Asked why, show the contradiction table.
- The first action is the top of the order in `plays.md`; only it carries the exact line.
- Stop in channels with outsiders: post nothing from CRM, calls, email or chat, say only that the review is held because an outsider is present, and ask the seller to ask again in a private thread or DM. Never promise to deliver it elsewhere. No format question in Slack. Check the thread first; the deal named earlier is the deal.

## Full review

```
# [Deal]: review, [date]
- **Verdict:** [exactly one of: qualified and progressing · qualified but stuck (wrong person) · not qualified · at risk; nothing added]
- **Momentum:** [word, for how long]
- **Confidence:** [level, what it rests on]
- **Asked of you:** [missing context, including sales cycle, asked once here and nowhere else; or "none"]

## ⚡ Do now           (max 3; each a ### with bullets: **Who** · **By** · **In practice** (the move, with the exact line to say) · **Could fail if**)
## Your other requests  (only if the seller asked for something declined or redirected: a quote, a deadline line, a rival claim, odds; one line each)
## What kills it       (bullets: **Dies if**, **Changes my mind**)
## Changed since [last date]   (bullets, only on a repeat run)
## Gaps                (the three that matter most: bold gap, what it costs, what happens if ignored)
## Worksheet           (table: box, status icon, trend word, evidence)
## ⚠️ Contradictions   (only where two sources disagree, max 5; one source never prints it)
## Buyer decisions     (five one-line bullets, status icon first, no repeat of the gaps)
## ❓ Questions        (bullets: must answer, send now, at most two categories; never repeats "Asked of you")
## 📋 Paste-ready      (### per block)
## Sources and not queried   (bullets, ending "A read of the evidence, not a forecast.")
```

Rules:
- Notes only, no transcript or buyer email: print the top block, Do now, What kills it, Questions (must answer and send now) and Paste-ready. Skip worksheet, gaps, decisions and contradictions.
- Icon and word must agree: ✅ made, 🟡 shaky, ❌ not made.
- Dates as "Mon 9 Nov", never ISO.
- Names in a deal record come only from the seller's own materials.

## Paste-ready blocks (every run, last)

1. **CRM note:** stage, verdict, top gap, next step and date, three lines.
2. **Next steps for Slack or email:** the steps as a short list.
3. **Send-now questions:** one email, subject line included, no pitch.

They are also the fallback when a write is refused or no connector exists.

## Queue

```
## Deals to look at this week
### 1. [Deal]
- **Stage:** [stage]
- **Gap:** [gap]
- **Owner:** [role]
- ⚡ **Do:** [one action] · by [date]
```
Close with a count and the line "Deals only; no sellers listed." In Slack: bold deal name, then one line each.

## Prep

```
## Prep: [Deal], [call]
- **Objective:** …
- **Gap to close:** …
### Ask in this order
1. …
2. …
3. …
- **Likely objection:** … · **Say:** "…"
```
