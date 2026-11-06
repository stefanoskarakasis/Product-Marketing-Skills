# Surfaces: Slack First, Everywhere Else Too

Read at Step 8. The same skill runs in five places. The surface changes the shape of the answer and who may be in the room. It never changes what counts as evidence, the signal windows, the constraints checks, the EMEA rules or the brain contract.

## Contents

1. Which surface this is
2. Slack (the default design target)
3. Claude chat (app, web, mobile)
4. Claude Cowork
5. Claude Code
6. Scheduled runs
7. When files cannot be saved
8. Delivery formats

## 1. Which surface this is

Decide from the session, never by asking.

| Signal | Surface |
|---|---|
| The message arrives from a Slack thread or channel, or the user says "in Slack" | Slack |
| A chat in the Claude app or web with no Slack signal | Claude chat |
| The session is Cowork, or the user's folders are connected | Cowork |
| The session is a terminal with a repo | Claude Code |
| A scheduled task started it, no one is there | Scheduled run |
| Cannot tell | Claude chat |

## 2. Slack

Design target. Assume the reader is a seller, on a phone, between calls.

- **Who may be in the room.** Check the channel before reading anything internal. If it has members from outside your company (a shared channel, a partner), post nothing from the CRM, calls, chat or email. A web-only brief on a public company may be posted, with the CRM line left out. Say once: "CRM details stay out of shared channels." Do not name what the CRM held.
- **Shape.** The thread reply in `brief-format.md`: the verdict first, the hypothesis, up to three signals, fit and timing, the first question, sources in words, one note line. About 120 words. Bold emoji section labels, blank lines between sections, short bullets and a "Do next" block. No tables, no markdown header marks, no HTML.
- **No format question.** Never ask Doc or HTML in Slack. The thread reply is the default; the full brief is a Google Doc link if `~~cloud storage` is connected, otherwise it is posted as up to three short follow-up messages in the same thread.
- **One clarifying message at most,** and only if the answer would change the reply (two companies with one name, an unknown role). Otherwise state the assumption in the Note line and go.
- **Thread context.** Read the earlier messages in the thread before answering. A company named earlier is the company.
- **Who asked.** Compare the asker's identity to the CRM owner when the connector exposes it. If the account is owned by someone else, say so on the first line.
- **Org-level access.** The connectors read with one login, so a seller can see through Claude what they cannot open in the CRM. In Slack give owner, stage and counts for the CRM, never amounts for deals the asker does not own, call quotes or rep names.
- **EMEA mode in a thread.** Role titles only, no person names, no contact details.
- **Speed.** Say "checking" in one line only if the work goes past the first two reads. Cap tool calls per question: CRM, the last record and two web reads first; enrichment only in `deep`. Never rebuild a whole brief inside a thread when the last record is inside its window; read it and update the changed lines.
- **Memory.** Slack sessions may not keep files between threads. Read `/context/prospects/` if it answers; if it does not exist, work without a delta and say "no earlier record found". If `_config.md` cannot be read, use the defaults and say so.
- **Proposals.** Do not post proposals for other skills in the seller's thread. They go in the run summary for the PMM, or wait for the next interactive run.

## 3. Claude chat

Full brief in the order in `brief-format.md`. One question at most before starting, and none about format: offer the Google Doc after the brief. Tables are fine.

## 4. Claude Cowork

Full brief. Save to `/context/prospects/` in the connected folder. A brief the user will return to is delivered as a Google Doc or an artifact, not only in the reply.

## 5. Claude Code

Full brief. Save to `/context/prospects/` in the working directory. Plain markdown.

## 6. Scheduled runs

No questions. Run the named companies, save each record, append `_patterns.md`, post one summary line per company to the one channel the schedule names, and stop. Content-originated actions are listed as proposals and never run. Proposals to other skills are logged, not shown as asks.

## 7. When files cannot be saved

Do not claim a save. Say in one line what was not saved. Then:

1. If `~~cloud storage` is connected, offer to save the brief as a Google Doc and ask nothing else.
2. Otherwise show the Learning Close row and the `_patterns.md` rows as a code block to keep.
3. Run as if there were no earlier record and say so.

## 8. Delivery formats

| Format | When | Notes |
|---|---|---|
| Thread reply | Slack, always | Template in `brief-format.md`: bold emoji section labels, bullets, spacing, about 120 words, no tables |
| Google Doc | Full brief on request, or Cowork | One column, tables stacked |
| Chat reply | Claude chat, Claude Code | Markdown with `#` and `##` headers and the emoji key, exactly as in `brief-format.md` |
| HTML | Only if the user asks | One column |
| Plain text note | Pasting into a CRM or email | No markdown and no emoji; same order and labels |
