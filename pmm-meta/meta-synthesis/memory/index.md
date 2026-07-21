# Memory Index
**Last updated:** [Will be auto-updated by meta-synthesis]

## Active Files
- `/memory/user-profile.md` — Current 24h profile (overwritten each cycle)
- `/memory/meta-synthesis-log.md` — Historical log (cumulative, never deleted)

## Archives
- `/memory/archived/initiatives/` — Old projects (14+ days inactive)
- `/memory/archived/blockers/` — Resolved issues (60+ days old)
- `/memory/archived/skill-sessions/` — Compressed old logs (90+ days)
- `/memory/archived/guardrails/` — Stale guardrails (90+ days no trigger)
- `/memory/archived/index.md` — Archive registry

---

## How Memory Works

1. Meta-synthesis runs every 24 hours
2. Mines: /context/skill-sessions.md + integrations (Slack, Drive, etc.)
3. Synthesizes: who, what, blockers, timeline, patterns
4. Writes to: `/memory/user-profile.md` (overwrite)
5. Appends to: `/memory/meta-synthesis-log.md` (history)
6. Archives: old entries to `/memory/archived/`
7. Next skill reads: `/memory/user-profile.md` at Step 0 → gets context

---

See MEMORY-README.md for full architecture.
