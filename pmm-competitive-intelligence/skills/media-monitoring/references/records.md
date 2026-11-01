# Records

Reference for `media-monitoring`. Read it in Step 3 and Step 9.

## Contents

1. Folder and rules
2. Files
3. Finding and action rows
4. Memory
5. The State Block
6. Drift

---

## 1. Folder and rules

All records live in `/context/monitoring/`, not in the skill folder.

- Every file opens with `schema: 1`. A different schema stops the run with a migration note.
- Files are append-only, except `watchlist.md`. A correction is a new row.
- Other skills cite `M-` ids in their own records. No skill writes another skill's files.
- Each scheduled run is a fresh session; everything the next run needs is here or in the State Block.

## 2. Files

| File | Holds |
|---|---|
| `watchlist.md` | Roster with `roster_position` and `competes_with`, category themes, channels per competitor, triggers, reader views, delivery, executor and backup |
| `_state.md` | Per channel and competitor: state (`read`, `listing`, `partial`, `blocked`, `not-run`), the rungs tried, last read date |
| `signal-log.md` | Every finding |
| `actions.md` | Every action card and its status |
| `memory.md` | Marks (`acted`, `useful`, `noise`, `mute`) and their counts |
| `misses.md` | Items the user said were missed |
| `YYYY-MM-DD.md` | The run record: cost line, brief, gate result |
| `snapshots/<slug>/<channel>-YYYY-MM-DD.md` | Page snapshots for diffing |

## 3. Finding and action rows

- **Finding:** `M-nnn` | competitor | claim | tier | published date | retrieved date | triage | touches | content hash.
- The id is minted from the content hash: the same hash keeps the same id. Without file access, ids are provisional and carry the session, for example `Q-20261105a-001`.
- **Action:** `A-nnn` | finding id | touches | status | drafted date | approved by | approved on | run id.

## 4. Memory

- Marks: `acted`, `useful`, `noise`, `mute`.
- Action rates are kept per trigger type. No reordering before 5 marks on a type.
- A mute lasts 90 days.
- `reset memory` clears it.
- Each brief states what memory changed.
- Memory is operational. It is never promoted to `/context/meta-patterns.md` automatically.

## 5. The State Block

At most 40 lines, posted at the end of the Doc and shown in chat when files cannot be saved.

```
schema: 1
run: [date, baseline or sweep]
executor / backup: [names]
roster: [competitors with positions]
next_id: M-nnn
open actions: [ids with ages]
watch: [ids with expiry]
blocked / partial: [channels]
memory: [counts]
```

## 6. Drift

- The log wins over the Doc except in the Watchlist section. Slack never wins.
- Store drift: if the Doc's State Block and the files disagree, show both and ask which is right.
- Snapshot drift: a snapshot older than 14 days is re-read.
- Config drift: a roster competitor not in brain Section 3 is flagged once.
- Contract drift: consumers cite `M-` ids; an id that does not resolve is reported.
