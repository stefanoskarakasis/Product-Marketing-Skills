# Memory Architecture: Write-Once-Read-Many
**Version:** 2.0.0  
**Last Updated:** 2026-06-22

---

## Overview

Memory is the persistent context layer between meta-synthesis cycles. Every 24 hours, meta-synthesis synthesizes what's actually happening (who you work with, what you're building, top blockers) and writes it to memory files. Execution skills read these files at startup (Step 0 pre-flight) to get immediate context.

**Core Principle:** Write-Once-Read-Many
- **Write:** Only meta-synthesis writes to /memory/
- **Read:** All execution skills read /memory/user-profile.md at Step 0
- **Modification:** Agent never modifies memory during conversation
- **Immutability:** Memory files are immutable between synthesis cycles

---

## Directory Structure
/memory/
├── README.md (this file)
├── index.md (registry of what's in memory)
├── user-profile.md (24h snapshot: who, what, blockers, timeline)
├── meta-synthesis-log.md (historical record of all synthesis cycles)
└── archived/
├── README.md (archive registry)
├── initiatives/ (old projects, not mentioned 14+ days)
├── blockers/ (resolved issues, >60 days old)
└── skill-sessions/ (compressed old logs, >90 days)

---

## File Descriptions

### /memory/user-profile.md
**Updated:** Every 24 hours by meta-synthesis  
**Read:** Every execution skill at Step 0 (pre-flight)  
**Content:** Dynamic profile snapshot of user's current work

Sections: Who You Work With | What You're Working On | Top Blockers | Timeline Pressure | Patterns & Signals | Metadata

**Lifetime:** 24 hours (overwritten next cycle)

### /memory/meta-synthesis-log.md
**Updated:** Appended every 24 hours by meta-synthesis  
**Read:** Optional (historical reference, trend analysis)  
**Content:** Historical record of all synthesis cycles

**Lifetime:** Permanent (365-day retention)

### /memory/archived/
**Updated:** Every 24 hours by meta-synthesis cleanup  
**Content:** Old entries automatically archived

---

## Write Flow (meta-synthesis)

Every 24 hours:
1. meta-synthesis runs
2. Mines all signals (skill logs + integrations)
3. Synthesizes profile
4. Writes /memory/user-profile.md (overwrite)
5. Appends to /memory/meta-synthesis-log.md (cumulative)
6. Archives stale entries to /memory/archived/
7. CYCLE COMPLETE

---

## Read Flow (Execution Skills)

User starts any execution skill
→ Step 0 (Pre-flight): Load /memory/user-profile.md
→ Skill now has immediate context
→ Skill executes with full context → SMARTER DECISIONS

---

## Privacy & Data Isolation

**Stored in /memory/ (Summaries Only):**
- "Blocked on CFO approval" (summary of email thread)
- "Champion sentiment declining" (summary from Gong)
- "Top blocker: procurement delays" (summary from interviews)

**NOT Stored (Raw Data):**
- Raw Slack messages
- Raw email thread content
- Raw Gong transcripts
- Full calendar events

---

## Lifecycle: Stale Entry Cleanup

Memory self-cleans automatically:

| Entry Type | Active Duration | Stale Threshold | Archive Action |
|---|---|---|---|
| Initiative | Current | 14 days no mention | Move to archived/initiatives/ |
| Blocker | Current | 60 days since resolution | Move to archived/blockers/ |
| Guardrail | Current | 90 days no trigger | Mark STALE in meta-patterns |
| Skill Session | Detailed log | 90 days old | Compress to summary, move to archived/ |

---

## Related Files

- `/context/skill-sessions.md` — Execution logs (source for profile synthesis)
- `/foundation/brain.md` — Company context (baseline for profile)
- `/context/meta-patterns.md` — Current guardrails
- `/config/scheduler.yml` — When to run synthesis
- `/config/integration-queries.yml` — Which MCPs to query
