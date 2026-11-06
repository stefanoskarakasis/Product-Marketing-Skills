# Brief Format

Read at Step 8. This file is the format standard. Copy the templates; do not invent sections, reorder them or add emoji of your own, so every reader meets the same shape on every run.

## Emoji key

Use only these, one per label, never inside a body sentence.

| Emoji | Where |
|---|---|
| 📋 | Brief title |
| 🎯 | Hypothesis |
| ❓ | First question |
| 📡 | Signals |
| ⚖️ | Fit and timing |
| 🆕 | Changed since, and new lines in a delta |
| 🗂️ | CRM |
| 👤 | Committee (deep only) |
| 🧠 | Brain check |
| 🛡️ | EMEA mode (only when on) |
| 🔁 | Proposed for other skills |
| ✅ | Gate, a yes in a table |
| ❌ | A no in a table |
| ⚠️ | Ageing, stale, not queried, unmapped or conflicting. Never decoration |
| ➡️ | Angle and next move (Slack) |
| 📎 | Sources (Slack) |
| 📄 | Full brief link (Slack) |
| 🟢 🟡 🔴 | Verdict status, Slack first line only: reach out now, worth a touch or wait, not yet or poor fit |
| 🔌 | Connected and not queried (Slack) |
| ✉️ | Draft note to the account owner (full brief only) |
| ▶️ | Do next, one to three bullets (Slack) |
| 🚫 | Why not now, on 🟡 and 🔴 verdicts only (Slack) |
| 🧩 | Learned from the brain and other skills (Slack) |

## Full brief (chat, Cowork, Claude Code or a Google Doc)

Order never changes. The default (quick) brief holds Hypothesis, Signals, Fit and timing, Changed since, CRM, Gate and the sections that have content (Learned from, Note to the owner, EMEA mode). Committee, Brain check and Proposed for other skills appear in `deep`, or when they hold a conflict or a proposal. Use real headers: one `#` title, `##` for each section. A section with no data is named and left short ("Committee: quick depth, not built"), never padded.

```
# 📋 Prospect research: [Company]

**Date:** [date] · **Mode:** [first brief | delta since date] · **Depth:** [quick | deep] · **Valid until:** [date]
**CRM:** [net new | owned by name | earlier record date]
**Sources used:** [list]
**Not queried:** [list]
🛡️ **EMEA mode:** [on, reason | off by your setting] (omit the line if not in scope)

## 🎯 Hypothesis
**Hypothesis (inference, [confidence]):** [one sentence]
**Behind it:** [one to three signals, source in words, date]
**➡️ Angle for [role]:** [one or two sentences]
**❓ First question:** "[question]"
**Fallback:** [one sentence]
**Warmer:** [approved proof | none approved]
**What they probably believe:** [one sentence]

## 📡 Signals ([n] of max 5, freshest first)
1. **[Signal]:** [what, source in words, date]. Expires [date]. Maps to: [brain pain]. `found | stated`
⚠️ **Ageing:** [signal past its window] (only when it helps)
⚠️ **Unmapped, ignored:** [signal types]

## ⚖️ Fit and timing
**Fit: [strong | moderate | poor]** · [one sentence]
[Table: dimension, evidence, result ✅ ❌ or "not verified"]
**Timing: [now | ageing | none]** · [one sentence]

## 🆕 Changed since [date]
[New or expired lines only; "unchanged" for the rest | first brief, nothing to compare]

## 🗂️ CRM
*[tool, date]*
[Owner, type, open opportunities, last touch, opt-out status | "net new, no CRM record" | "not queried"]

## 👤 Committee
[Deep only: roles from Section 2, a person only where the company names them, source and date; unknown stays unknown]

## 🧠 Brain check
[ICP fit and anti-persona, alternatives or tools seen, claims we may use; conflicts as questions]

## 🛡️ EMEA mode
[What was applied: legal form, person reads off or on request, enrichment fields withheld, channel note, retain until] (only when on)

## 🧩 Learned from
[Skill, date, what it contributed | "No earlier skill output found"]

## ✉️ Note to the account owner (draft, not sent)
[Three lines, only when a colleague owns the account: who is asking, why now, what you propose to do]

## 🔁 Proposed for other skills
[Exact text and receiver | none proposed, and the pattern count]

## ✅ Gate
**[n] of 12** · Not queried: [list]
```

In a Google Doc, tables stack in one column.

## Slack thread reply (the default in Slack)

Slack does not render markdown headers or tables. Build the look from bold section labels that start with an emoji, one blank line between sections, and short bullets. Bold uses Slack's single asterisks. About 120 words or fewer; the first line is the verdict with its status emoji. Every section label is on its own line and the content sits under it.

```
[🟢|🟡|🔴] *[Company]*: [verdict in one sentence: reach out now | worth a touch, signals ageing | not yet | poor fit, and the reason in a few words]

🎯 *Hypothesis* ([confidence]: [reason], inference)
[one sentence]

📡 *Signals* (freshest first)
• [signal], [source], [date]
• [signal], [source], [date]
⚠️ [ageing or unmapped signal, only when it matters]

⚖️ *Fit and timing*
• *Fit:* [strong | moderate | poor], [reason]
• *Timing:* [now | ageing | none], [reason]

➡️ *Angle for [role]*
[one sentence]

❓ *First question*
"[question]"

🚫 *Why not now* (🟡 and 🔴 only)
[one sentence: the single biggest reason]

▶️ *Do next*
• [owner-aware: when a colleague owns the account, "Message [owner] first" is bullet one]
• [one concrete action]

🗂️ *CRM:* [net new | owned by name, stage | earlier record date]
🧩 *Learned from:* [skill, date] · [skill, date] (only when used)
🔌 *Connected:* [tools that answered] · *Not queried:* [list]
📎 *Sources:* [source, date] · [source, date]
🛡️ *EMEA mode on:* [reason, one line] (only when on)
📄 *Full brief:* [Google Doc link]
```

Rules: on a 🔴 verdict "Do next" is one bullet; on 🟡 and 🔴 the "Why not now" block is required and on 🟢 it is left out; signals are listed freshest first; no more than three bullets in a section, no table, no header marks, no sentence over 25 words. The "Do next" bullets are mandatory and must be actions the reader can take today, never a restatement of the angle.

**Delta reply** (a record exists): the first line says what changed. Then `🆕 *Changed:* [line, source, date]`, `⚠️ *Expired:* [signal]`, and `🎯 *Hypothesis unchanged | revised:* [one sentence]`. The rest is as above.

If "Full brief" cannot be a link, post the sections as up to three follow-up messages in the thread. Who may be in the room and what to leave out: `surfaces.md` section 2.

## Plain text note (to paste into a CRM or email)

Same order and labels, no markdown and no emoji.
