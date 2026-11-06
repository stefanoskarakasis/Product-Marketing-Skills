# Format: the report in plain words

Read at Step 7, every run. The shape never changes. The reader is a busy PMM who has not read the logs and does not know the skill's inner words. A ten-year-old should understand every line.

## Plain-language rules

1. **Short sentences.** Twenty words or fewer. One idea each.
2. **Every number says what it counts and what it is compared to.** "31 times by 14 salespeople, up from 22 by 9", never "31, +41%".
3. **Say it with these words, not the repo's.**

| Never write | Write instead |
|---|---|
| brief | research report on one company |
| verdict | advice, or the green, yellow or red light |
| signal | a sign, a clue |
| hypothesis | our best guess |
| ICP | the kind of company you usually sell to |
| Section 2 / 3 / 6 | "who you usually sell to" / "your list of rivals and tools" / "your approved proof" |
| thin brain | missing company notes |
| ledger, n, cohort, attribution, funnel | say what you mean in plain words |
| fit | whether the company is the kind you sell to |

4. **Every part ends with a "What this means" line** in one sentence a manager could repeat out loud.
5. **Every action starts with a verb,** names the thing, gives the reason, says how long and who does it.
6. **Say what you could not see.** A blank is not a zero.
7. **Names stay in the file.** The Slack summary shows teams only.
8. **No rate under 10 cases.** Show the count and say it is too few to judge.

## Full report (the file, and the Doc copy)

```
# How the sales team used the research helper: week of [date]

**Overall:** [🟢 | 🟡 | 🔴] [one sentence: the single most important thing]

## 1. Did people use it?
- The helper was used [n] times by [n] salespeople. Last period: [n] by [n].
- Teams that did not use it: [team (n uses)].
- [n] of [n] salespeople tried it once and never came back.
**What this means:** [one sentence]

## 2. Was the advice any good?
- The helper gave [n] green, [n] yellow and [n] red lights.
- [n] of the [n] red companies were contacted anyway. [We do not know yet whether the helper or the salesperson was right. | CRM not connected, so I cannot tell.]
- In [CRM name], [n] of [n] companies have a deal started within 60 days. [Too few to judge. | Count only.]
**What this means:** [one sentence]

## 3. What did the companies have in common?
- [n] companies use a tool that is not on your list of rivals: [tool].
- [n] reports said the same thing: [their words, with source and date].
- [n] companies were [bigger | smaller] than the kind you usually sell to.
- [Missing company notes: what the helper could not do because of it.]
**What this means:** [one sentence]

## 4. What to do this week
1. **[Verb] [thing].** Why: [reason]. Time: [minutes]. Who: [PMM | a named role]. Evidence: [where].
(at most three)

## Waiting for your yes
[Exact text of each proposed change, the file or skill that would receive it, and its evidence. "None" if none.]

## What I could not see
[Not connected, not queried, weak matches, data too thin.]

## How I counted
[Period, files read, how companies were matched, one line each.]

## Names (this file only)
| Salesperson or team | Runs | Last run | Red lights contacted anyway |
```

When no CRM answered, the line under part 2 is replaced by: "⚠️ **Outcomes blind.** No CRM is connected, so I can count the reports but not what happened next. Connect HubSpot or Salesforce (an admin step, see the connector file) and the next report will check for deals." Print it every run until a CRM answers.

## Slack summary (teams only, 150 words or fewer)

```
📊 *Sales research digest*, week of [date]

[🟢|🟡|🔴] *[Overall sentence]*

📈 *Use*
• [n] reports by [n] people, up from [n] by [n]
• Quiet: [team (n)]

🎯 *Advice*
• [n] green, [n] yellow, [n] red
• [n] of [n] red companies were contacted anyway
• [CRM result sentence]

🧩 *Common threads*
• [one line each, at most three]

▶️ *Do next* ([n] waiting for your yes)
1. [Verb thing, time]
2. ...

🔌 *Connected:* [list] · *Not queried:* [list]
📄 *Full report:* [file or Doc link]
```

Bold in Slack uses single asterisks. No names, no table, no header marks.
