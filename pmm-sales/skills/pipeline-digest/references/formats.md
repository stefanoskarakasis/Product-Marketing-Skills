# Formats

Read at Step 6. Lead with what the reader does, then why. Plain words, short sentences (about 15 words at most), one fact per line. No abbreviations, no idioms, no jargon: a junior Account Manager in any market must follow it. Bold, never italics: `*x*` in Slack, `**x**` elsewhere.

## Words and dates

- Say "close date passed", "quiet", "slow in stage", "only one person", "Next Step empty", "deals to consider closing". Do not say "stuck", "overdue", "single-threaded", "dead weight", "ARR", "AE" or "SDR".
- Dates as weekday, day and month name: "Wed 25 Nov". Never `11/25`, `25/11` or ISO.
- Roles as full words: "Account Executive, Mid-Market".
- Reply in the language the asker writes in. Translate headings, flags and questions; leave CRM field and stage names exactly as the CRM labels them.
- Every number says what it counts and out of how many ("4 of 31 deals").

## Icons

Emoji only for a section, a flag, an action or a status. None in running text.

- **Sections:** 📊 digest and health · ⚡ do this · 🔄 what changed · 🔧 fix in the CRM · ❓ I need this from you · 📨 DM drafts · 🗑️ deals to consider closing · 🔁 last week's actions · 🧠 approver only · 🔍 what I read
- **Flags:** 📅 close date passed · 🕰️ quiet · 🐌 slow in stage · 👤 only one person · 📝 Next Step empty
- **Status:** ✅ done or won · 🟡 still open · ❌ lost · ➖ not checked · ⚠️ a check found something

Header sizes: `#` digest title, `##` sections, `###` each deal or DM. Slack has no headers: a bold label on its own line.

## Slack card (hard cap 100 words)

```
📊 *Pipeline: [N] open deals, [n] need you this week*
[CRM] · [scope] · [date]

⚡ *Do first*
• [Deal] [flags]: [why, one line]. [Action] · by [date]

⚡ *Then* (max 2)
• [Deal] [flags]: [why]. [Action] · by [date]

❓ *Need from you:* [deals] have no [field]. [One question]

*Next:* draft a DM to each deal owner, or open the digest?
```

- Over 100 words: drop the second "Then", then shorten reasons. Never drop the ❓ line when a field is missing.
- No amounts, no seller names, no call quotes. Owner shows as a role only when asked.
- Nothing needs attention: "📊 *Pipeline: [N] open deals, nothing needs you this week*", the counts, and the next line.
- The last line is one plain question that offers the next step. Any natural yes works. A yes to "draft a DM to each owner" shows each draft in full; nothing sends until a yes names it.
- Stop in a channel with outsiders: post nothing from the CRM, say the digest is held because an outsider is present, and ask the seller to ask again in a private thread. Never promise delivery elsewhere.

If more deals need you than fit in 100 words, the headline still gives the true count and the card ends with "+N more in the digest". Sections 2 and 7 appear only on a repeat run, so the numbers can skip.

## Full digest

```
# 📊 Pipeline digest: week of [date]
**Start with section 1.** Each deal there has one thing to do and a date.
**Icons:** [flag legend]
- **Who this covers:** [scope, N open deals by segment]. It lists deals, never people.
- **Where the data comes from:** [CRM, read only, date and time]
- **Compared with:** [last digest date]
- **How sure I am:** [level, what it rests on]
- **Rules I used:** [quiet, slow, cycle; labelled defaults if any]

## ⚡ 1. Deals to act on         (max 5; each a ### with Where it is, Why it is here, Owner, Do this, By, Watch out)
## 🔄 2. What changed since [date]  (bullets, only on a repeat run)
## 📊 3. Pipeline health          (table: icon, check, what it means, deals, out of; one ⚠️ line)
## 🔧 4. Fix in [CRM]: [n] issues on [m] deals   (table: field, what is wrong, deals)
## ❓ 5. I need this from you     (questions per deal; ➖ not checked; then ### 📨 DM drafts)
## 🗑️ 6. Deals to consider closing (only if any; "I changed nothing")
## 🔁 7. Last week's actions      (✅ done, 🟡 still open; "my reading from activity")
## 🧠 8. For the approver only    (only when the reader is the approver; never in a seller's thread)
## 🔍 9. What I read and what I did not
```

Rules:
- Empty sections never print. A first run has no sections 2 and 7.
- Section 3 prints "out of" per check; a check that skipped deals says how many and why.
- Section 8 holds proposals at the n in `feed-forward.md`: exact text, the receiving skill, and any conflict with a brain value shown as a question with both values.
- End with "A read of the evidence, not a forecast."

## DM draft (per deal owner)

```
**DM [n]: to the owner of [deal and deal]**
> Hi! [One, two] quick question[s] for [CRM].
> [Deal]: [the one missing field as a question].
> One line each is enough. Thank you!
```

- One DM per owner, about the deals that owner holds. Only the missing field. No deadline, no other deal, no mention of the digest or of other sellers.
- The recipient is the CRM owner, found through `~~team chat`. Not found: paste-ready text only.
- Solo run: the question goes to the asker in the digest. No DM.

## Forecast sheet

One block per deal in commit or best case: **Deal** · category · stage; **Evidence** (dated, `CRM` or `activity`); **Where the category is stronger than the evidence**; **The question you will be asked**. Ends "A read of the evidence, not a forecast." No probabilities, no amounts, no sums.

## Hygiene list

Table: field, what is wrong, deals. Then each deal on its own line with the exact field to fix, grouped by field. End with the one field that clears the most issues.

## Paste-ready blocks

1. **CRM note per deal** the reader owns: flags, the next step and its date, two lines.
2. **The five actions for Slack or email** as a short list.
3. **DM drafts** as above.

They are also the fallback when a write is refused or no connector exists.
