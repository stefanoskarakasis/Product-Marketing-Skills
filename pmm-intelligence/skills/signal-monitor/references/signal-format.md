# Signal list: canonical format

`/context/signals/YYYY-MM-DD.md` holds one run of `signal-monitor`. One file per run date. If a file for today exists, add `-2`, `-3` and so on. Never overwrite an earlier run.

## File format

    # Signals — [YYYY-MM-DD]
    Brain read: [which sections were present; "Quick-Brain, session only" if none]
    Sources named this run: [list]
    Dropped (no brain field touched): [count]

    ## O-1 [short title]
    - Signal: [what changed, one sentence]
    - Evidence: [source, date, quote or figure] [pulled|stated|inferred]
    - Brain field: [Section N, field key]
    - Priority served: [Section 7 priority, or "none stated"]
    - Confidence: [high | medium | low] — [why, one line]
    - Suggested next move: [one move, one owner role]
    - Brain change to consider: [field and proposed value, or "none"]

## Rules

- Max 5 opportunities. Ranked: priority served first, then confidence, then recency.
- Every opportunity has evidence with a source and a date. No evidence, no opportunity.
- `Confidence: high` needs two independent sources. One source is at most `medium`. A rumor or an unnamed source is `low`.
- A signal about the company's own claims (a website figure, a press line) is evidence of what was said, never proof it is true.
- "Brain change to consider" is a suggestion. This skill never writes the brain.
- No personal data about named individuals. Roles and company names only.
