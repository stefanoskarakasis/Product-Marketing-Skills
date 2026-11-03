# Brief Format

Read at Step 10. This file is the format standard. Copy the templates; do not invent sections, reorder them or add emoji of your own, so every reader meets the same shape on every run.

## Emoji key

Use only these, one per label, never inside a body sentence.

| Emoji | Where |
|---|---|
| 📋 | Brief title |
| 📅 | Current state |
| 🚩 | A flag |
| 🆕 | Changed since, and new lines in a delta |
| 🗂️ | CRM |
| 👤 | Contacts |
| ✉️ | Correspondence |
| 📞 | Calls and docs |
| 💬 | Chat, support, usage |
| 🧠 | Brain check |
| 🔁 | Proposed for other skills |
| ✅ | Gate, a cleared flag, a yes in the contacts table |
| ❌ | A no in the contacts table |
| ⚠️ | Stale, not queried, conflicting or not fired. Never decoration |
| ➡️ | Next move (Slack) |
| 📎 | Sources (Slack) |
| 📄 | Full brief link (Slack) |

## Full brief (chat, Cowork, Claude Code or a Google Doc)

Order never changes. Use real headers: one `#` title, `##` for each section. A section with no data is named and left short ("Support: not queried"), never padded.

```
# 📋 Customer context: [Customer]

**Date:** [date] · **Mode:** [first brief | delta since date] · **Owner:** [name] · **Last touch:** [date, who]
**Sources used:** [list]
**Not queried:** [list]

## 📅 Current state
[Two or three sentences: what is happening, what is at stake, the next date that matters.]

## 🚩 Flags ([n] of max 5)
1. **[Flag]:** [what, source in words, date]. `found | stated | validated`
⚠️ **Not fired:** [flag, and why] (only when it helps)

## 🆕 Changed since [date]
[New or re-read lines only; "unchanged" for the rest | first brief, nothing to compare]

## 🗂️ CRM
*[tool, date]*
[Owner, profile, renewal opp (stage, amount, close date, next step), last closed, last activity]

## 👤 Contacts
[Table: role, last touch, two-way thread ✅ or ❌]

## ✉️ Correspondence
*[5 most recent, one line each, date first]*

## 📞 Calls and docs
[Latest call and key point; account plan, success plan, contract: last modified, desired outcome written or not]

## 💬 Chat, support, usage
[Themes and counts; "not queried" where it applies]

## 🧠 Brain check
[ICP, competitors, objections, claims we may use]

## 🔁 Proposed for other skills
[Exact text and receiver | none proposed, and the pattern count]

## ✅ Gate
**[n] of 12** · Not queried: [list]
```

In a Google Doc, tables stack in one column and the customer's renewal context sits in its own block above the sections.

## Slack thread reply (the default in Slack)

Slack does not render markdown headers or tables, so no `#` headers and no tables. Bold labels use Slack's single asterisks. About 150 words or fewer; the first line is the answer.

```
*[Customer]* [answer in one or two sentences: renewal, date, the one fact that matters].

🚩 *[Flag]:* [what, source, date]
🚩 *[Flag]:* [what, source, date]
(at most three)

➡️ *Next move:* [one sentence]

📎 *Sources:* [source, date] · [source, date]
⚠️ *Note:* [only when stale, not queried or conflicting]
📄 *Full brief:* [Google Doc link]
```

**Delta reply** (a brief exists): the first line says what changed. Then `🆕 *Changed:* [line, source, date]`, `✅ *Cleared:* [flag]` where a flag no longer fires, and `🚩 *Unchanged:* [flag, source, date]`. The rest is as above.

If "Full brief" cannot be a link, post the sections as up to three follow-up messages in the thread. Who may be in the room and what to leave out: `surfaces.md` section 2.

## Owner DM (offered when the user is not the owner)

Two sentences in a conversational tone: the opp, one detail from the brief, one question ("Anything you need from me on it?"). Show the draft. Post it only if asked.

## Plain text note (to paste into a CRM or email)

Same order and labels, no markdown and no emoji.
