---
description: Draft a blog post, landing page, press release, case study, newsletter, or social post
argument-hint: "<format> <topic>   (or: audit <paste a draft>)"
---

# /pmm-toolkit:marketing-content -- Marketing Content

Draft marketing content in one of six formats: blog post, social post (name the
platform), newsletter, landing page, press release, or case study. The skill reads your
brain for audience, key messages, voice, and proof, so you are only asked for what is
missing. It never invents statistics, quotes, customer names, or results: every gap
becomes a visible placeholder you fill in.

## Invocation

```
/pmm-toolkit:marketing-content blog post about our new reporting feature
/pmm-toolkit:marketing-content landing page for the Q4 webinar
/pmm-toolkit:marketing-content press release: we closed our Series A
/pmm-toolkit:marketing-content case study for Acme, 30% faster onboarding
/pmm-toolkit:marketing-content newsletter issue on this week's launch
/pmm-toolkit:marketing-content LinkedIn post about the launch
/pmm-toolkit:marketing-content audit [paste a draft to scan for AI patterns]
```

## Workflow

Uses the `writing-assistant` skill in its Marketing content mode, or its Audit mode when
the first word is `audit`. It picks the format, takes inputs from your request and the
brain, asks once for anything still missing (or lists its assumptions if you say "just
draft it"), then drafts to that format's structure and checks the draft before showing it.
The output is the draft, a notes list (voice used, assumptions, placeholders to fill), and
one follow-up question.

For Slack messages, emails, memos, and rewrites, use `/pmm-toolkit:write` instead.
