# Records

Reference for `weekly-competitive-updates`. Read it in Step 1, Step 2, Step 8 and Step 11.

## Contents

1. Folder and rules
2. Files
3. Row formats
4. How each file is used
5. The Carry-forward Block
6. Drift

---

## 1. Folder and rules

All records live in `/context/weekly-updates/`, not in the skill folder.

- Every file opens with `schema: 1`. A different schema stops the run with a one-line migration note.
- Files are append-only. A correction is a new row, never an edit.
- Each scheduled run is a fresh session; everything the next run needs is in these files or the Carry-forward Block.
- No skill writes another skill's files. This skill reads `/context/competitor-profiles/`, `/context/monitoring/` and `/context/signals/` and writes none of them.

## 2. Files

| File | Holds |
|---|---|
| `setup.md` | Company, competitor set (with parent and sub-brands), markets, requester and the date it was confirmed, delivery, the schedule flag |
| `editions/YYYY-MM-DD.md` | One saved edition: the update, the Items table, the Method (sources read, sources blocked) |
| `_threat-ledger.md` | One row per competitor per edition that had a change |
| `_watchlist.md` | One row per watchlist item and one row per status change |

## 3. Row formats

- **Setup row:** `date` | `company` | `competitors` (name; sub-brands; parent) | `markets` | `requester` (name; role title; role; department; market) | `confirmed_on` | `scheduled` (yes or no) | `delivery`.
- **Items table (inside each edition):** `competitor` | `DD Mon` | `fact in one line` | `url` | `⚠️ or blank`. The next run uses it to avoid reporting the same item twice.
- **Threat row:** `edition_date` | `competitor` | `level` (High, Medium-High, Medium, Low-Medium) | `trend` (rising, weakening, stable) | `change_note`.
- **Watchlist row:** `W-nnn` | `status_date` | `item` | `type` (scheduled or weak-signal) | `expected_date` | `url` | `status` (open, happened, lapsed, dropped).
- Watchlist ids count up and are never reused. A status change is a new row with the same id.

## 4. How each file is used

- **`setup.md`:** read in Step 2. The newest row wins. The requester block is shown for confirmation in an interactive run; a scheduled run uses it only when `scheduled: yes` and `confirmed_on` is under 90 days old.
- **Newest edition:** read in Step 1 and Step 5 for its Items table.
- **`_threat-ledger.md`:** read in Step 6 for continuity; appended in Step 11.
- **`_watchlist.md`:** read in Step 8, where each open id is resolved, kept or lapsed; appended in Step 11.
- **Learning:** the Learning Close row goes to `/context/skill-sessions.md`, where `meta-synthesis` reads it. A watchlist item that lapses three weeks running is a pattern worth writing there.

## 5. The Carry-forward Block

Shown at the end of the chat answer when the files cannot be written (for example, no file access). At most 30 lines. The user pastes it into the next run's request, or the run reads it from the Doc.

```
schema: 1
edition: [date]
company / markets: [list]
requester: [name; role; department; market], confirmed [date]
threat levels: [competitor: level, trend; ...]
open watchlist: [W-id: item, expected date; ...]
items reported: [competitor, DD Mon, short fact; ...]
```

Without the file or the block, the next run is a first edition and the Threat Board says continuity is limited.

## 6. Drift

- **Store drift:** if the Doc's Carry-forward Block and the files disagree, show both and ask which is right. In a scheduled run, use the files and say so in the Coverage line.
- **Setup drift:** a competitor in `setup.md` that is not on the brain roster is flagged once, never added or removed automatically.
- **Window drift:** the window starts the day after the newest edition's run date, up to a maximum of 14 days. A longer gap is reported as a coverage gap, not swept in full.
