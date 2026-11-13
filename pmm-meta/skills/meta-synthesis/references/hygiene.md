# Guardrail and log hygiene

Read at the end of every run. Nothing here changes a file without a yes shown as exact text.

1. **Status on every guardrail.** Each line in `/context/meta-patterns.md` carries `status: confirmed | watch | retired`.
2. **Retire, never delete.** A guardrail leaves by a status change to `retired`, with `retired: YYYY-MM-DD` and a one-line reason. Its text stays.
3. **When to propose a retirement.** No session cited it for 90 days, a later pattern contradicts it, or the user rejected its advice twice.
4. **Cap of 20 live guardrails** (confirmed plus watch). Past 20, propose retiring the oldest uncited ones before adding a new one.
5. **Archive.** When retired lines pass 20, or once a year, propose moving them word for word to `/context/meta-patterns-archive.md`. Move, do not rewrite.
6. **Session log.** Rows older than 180 days that a synthesis has already read may move word for word to `/context/skill-sessions-archive.md`. Archived rows do not count toward a pattern unless the user asks.
7. **Say it in one line** at the close: live, watch, retired, and how many are due for review.
