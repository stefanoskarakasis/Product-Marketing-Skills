# meta-learn — Eval Suite
**Skill version:** 1.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: Clean extraction — one clear pattern

**Input:**
```
/learn retro

Session: Q2 product launch retro. Surfaced that tier was assigned T2 but
the launch performed at T1 signal — $280K pipeline vs $90K target.
Sales used it in 80% of enterprise deals within 6 weeks.

1. Surprised: The pipeline number was 3x target. We under-invested in enablement.
2. Wrong: The skill suggested the tier mismatch was a process failure. It was actually
   a signal reading failure — we had the data but weighted it incorrectly.
3. Missing: No prompt to check win/loss data before tier assignment. We had it.
```

**Expected output includes:**
- All three extraction questions confirmed as answered before extraction begins
- Pattern extracted: specific and falsifiable — "When win/loss data shows >60% win rate
  in a segment, tier assignment should weight that above revenue target alone"
- Classified as: New hypothesis
- Routed to: `knowledge/gtm/hypotheses.md` (not `knowledge/retro/`)
- Self-Improvement Trigger surfaced with exact proposed text before any write
- Skill gap noted: missing win/loss data check prompt → routed to `knowledge/meta/`
- Session log entry proposed for `sessions/log.md`

**Expected output excludes:**
- Any write before user approval
- Pattern routed to `knowledge/retro/` instead of `knowledge/gtm/`
- Vague pattern: "tier assignment could be better"

**Pass condition:**
Pattern is specific and falsifiable, routed to correct domain, no write before approval.

---

## Test Case 2: No learnings — session closes cleanly

**Input:**
```
/learn gaccs-brief

1. Surprised: Nothing — the brief went as expected.
2. Wrong: Nothing I'd change.
3. Missing: Nothing obvious.
```

**Expected output includes:**
- Skill acknowledges all three answers were "nothing"
- Confirms once: "No patterns to capture this session — that's valid."
- Session log entry still appended (automatic write — no approval needed):
  `Patterns extracted: 0 | Writes approved: none`
- Clean close — no forced patterns

**Expected output excludes:**
- Pressing the user for patterns when they've said there are none
- Writing anything to hypotheses.md or rules.md
- Treating "nothing" as incomplete answers that need follow-up

**Pass condition:**
Session closes cleanly with a log entry and zero knowledge base writes.

---

## Test Case 3: Cross-skill pattern routes to global

**Input:**
```
/learn pre-mortem

1. Surprised: The skill caught a competitive risk I hadn't considered — incumbent
   response timing. Same thing happened in last week's GTM strategy session.
2. Wrong: Nothing.
3. Missing: Nothing.
```

**Expected output includes:**
- Pattern identified as cross-skill (observed in both `pre-mortem` and `go-to-market-strategy`)
- Routed to `knowledge/global/hypotheses.md` — not `knowledge/risk/`
- Self-Improvement Trigger explicitly states: "Cross-skill pattern — routes to global"
- Note that this is the first observation (1/3 needed for rule promotion)
- Session log captures the cross-skill nature of the pattern

**Expected output excludes:**
- Routing to `knowledge/risk/` (source skill's domain) instead of `knowledge/global/`
- Auto-promoting to a rule after one observation
- Missing the cross-skill signal

**Pass condition:**
Cross-skill pattern correctly identified and routed to `knowledge/global/`.

---

## Test Case 4: Hypothesis confirmation — promotion proposed at threshold

**Input:**
```
/learn go-to-market-strategy

1. Surprised: Same pattern again — when positioning in brain Section 3 is over
   6 months old, the channel recommendations default to broad rather than targeted.
   This is the third time I've seen this.
2. Wrong: Nothing.
3. Missing: Nothing.
```

**Context:** `knowledge/gtm/hypotheses.md` already contains:
- H-012: "When brain Section 3 (Positioning) is >6 months old, channel recommendations
  default to broad rather than ICP-specific" — confirmed 2 times previously.

**Expected output includes:**
- Hypothesis H-012 identified as matching
- Confirmation count updated: now 3/3
- Promotion to `knowledge/gtm/rules.md` proposed — not auto-executed
- Self-Improvement Trigger format used with exact proposed rule text
- Explicit "Awaiting approval before encoding" statement
- If approved: H-012 moved from hypotheses to rules with confirmation dates

**Expected output excludes:**
- Auto-promotion without user approval
- Promotion proposed at 2 confirmations
- Pattern treated as new hypothesis instead of matching existing H-012

**Pass condition:**
Promotion correctly proposed at 3 confirmations, not executed without approval.

---

## Test Case 5: /learn-history — correct domain summary

**Input:**
```
/learn-history gtm
```

**Context:** `knowledge/gtm/` contains rules.md with 2 rules, hypotheses.md with
4 hypotheses (one stale — last tested 95 days ago), knowledge.md with 6 observations.

**Expected output includes:**
- Summary table for `knowledge/gtm/` only — not all domains
- Correct counts: 2 rules, 4 hypotheses, 6 observations
- Stale hypothesis flagged: "1 hypothesis untested for 95 days"
- Last session date and skill name from `sessions/log.md`
- Offer to run `/learn-review gtm` to address the stale hypothesis

**Expected output excludes:**
- All domains shown when only `gtm` was requested
- Stale hypothesis not flagged
- Incorrect counts

**Pass condition:**
Correct domain filtered, counts accurate, stale hypothesis surfaced.

---

## Test Case 6: Skill gap extraction — routes to meta

**Input:**
```
/learn stakeholder-maps

1. Surprised: Nothing from the skill.
2. Wrong: The skill asked who has said yes but never asked about who controls budget
   approval. That was the actual blocker and it never surfaced until week 3.
3. Missing: A specific question about budget authority — separate from power/interest.
```

**Expected output includes:**
- Skill gap identified: missing budget authority question in intake
- Classified as: Skill gap (not a user pattern or GTM pattern)
- Routed to: `knowledge/meta/hypotheses.md` — not `knowledge/stakeholders/`
- Self-Improvement Trigger proposes specific addition to `stakeholder-maps` intake
- Note that skill gap proposals should also be considered for the skill's own
  self-improvement loop in the next `/meta-review` pass

**Expected output excludes:**
- Routing to `knowledge/stakeholders/`
- Treating as a user error rather than a skill gap
- No specific proposed addition to the stakeholder-maps intake step

**Pass condition:**
Skill gap correctly classified, routed to `knowledge/meta/`, specific fix proposed.

---

## Test Case 7: /learn-review — stale hypothesis audit

**Input:**
```
/learn-review hypotheses
```

**Context:** knowledge base contains:
- H-003 in `knowledge/gtm/`: last tested 94 days ago
- H-007 in `knowledge/segments/`: last tested 45 days ago
- H-012 in `knowledge/risk/`: last tested 12 days ago
- H-015 in `knowledge/global/`: last tested 102 days ago

**Expected output includes:**
- Two stale hypotheses flagged (94 days and 102 days — both over 90-day threshold)
- H-007 (45 days) and H-012 (12 days) listed as healthy — not flagged
- For each stale: specific suggestion on how to test it in the next relevant session
  (e.g. "H-003 can be tested in the next `go-to-market-strategy` or `retro` session")
- Option to archive stale hypotheses that are no longer relevant

**Expected output excludes:**
- H-007 (45 days) flagged as stale
- No actionable suggestion for testing stale hypotheses
- Stale hypotheses auto-archived without user decision

**Pass condition:**
Exactly two stale hypotheses flagged, healthy ones correctly excluded,
testing suggestions specific to the relevant skill.
