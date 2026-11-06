# Signals, Windows and Files

Read at Steps 1, 3 and 4.

## 1. Evidence states

| State | Meaning |
|---|---|
| `found` | A connected tool or a fetched public page shows it, with a date |
| `stated` | The user, or a seller in a thread, said it; no source shows it |
| `inferred` | Claude's reading of one or more found facts; always labelled and never promoted |
| `not queried` | The source was not read; the claim is not made |

A hypothesis is always `inferred`. A signal may rest on `stated` only if the brief says so.

## 2. What counts as a signal

A data point is not a signal until you can say why it matters to your business and what to do about it. A signal earns a place only if it passes all three:

1. **Dated and sourced.** A public page, filing, record or tool result with a date.
2. **Mapped.** It points at a pain in brain Section 2 (`pains`, `triggers`). If it does not, it is listed once as "unmapped, ignored".
3. **Actionable.** It changes the angle or the first question. If it does not, drop it.

Show at most five. Fewer, better signals beat many. No composite score in v1: the count of hits and misses per signal type is recorded (Step 11) and nothing is weighted until outcomes exist.

## 3. Seed signal map

Seeded the first time the skill runs; only rows that map to a pain in the user's brain are switched on. Windows are defaults, not research findings. Tune them in `_signals.md`.

| Signal type | Where to look | Window | Typical reading (a hypothesis to test, not a fact) |
|---|---|---|---|
| Hiring spike in a function you sell into | Careers page, job boards | 30 days | The function is under strain or being built |
| Leadership change in your buyer's function | Press, company site | 30 days | A new owner reviews tools and vendors early |
| Tool installed or removed | Job-post requirements, partner pages, site tech | 60 days | A switching window may be open |
| Funding or financial event | Press, filings, `~~company data` | 90 days | New budget, or pressure to show efficiency |
| Company priority in their own words | Earnings remarks, interviews, posts | 90 days | Where spend is likely to go |
| Launch, expansion or entry to a market | Newsroom, press | 30 days | New process, new compliance, new volume |
| Reorganisation or layoffs | Press, filings | 30 days | Consolidation or cost pressure |
| Regulatory change affecting their sector | Regulator, press | 90 days | Compliance work with a deadline |

Timing signals decay in days or weeks; structural facts last longer. A signal older than its window is shown as ageing and does not count toward "timing: now".

## 4. Files this skill creates (first run)

`/context/prospects/_config.md`

```
# Prospect research config
brain_source: drive        # drive | notion | github | local
brain_path: [link or path to the brain file]
workspace_path: [defaults to a context folder beside the brain]
usage_identity: handle     # handle | team (see emea.md)
pmm_owner: [handle of the PMM who owns the setup]
emea_mode: auto            # auto | on | off
home_region: [where your team sells from, e.g. EEA, UK, US]
default_depth: quick       # quick | deep
approver: [name of the PMM who approves proposals]
retain_days: 180
n_thresholds: defaults in feed-forward.md   # edit here to change them
feed_targets: all on       # list targets to switch off
```

`/context/prospects/_signals.md`

```
# Signal map
| Signal type | Where to look | Window (days) | Brain pain it maps to | Action | Hits / total |
|---|---|---|---|---|---|
[one row per active signal, seeded from section 3; "Hits / total" starts at 0 / 0]

Unmapped, ignored: [signal types that match no brain pain]
```

## 5. Outcome log

`/context/prospects/_outcomes.md`, one row per `log:` line:

```
date | company slug | hypothesis id | outcome (meeting booked | no reply | lost: reason | won) | signal types behind it
```

The slug, the hypothesis id and signal types only. No names.
