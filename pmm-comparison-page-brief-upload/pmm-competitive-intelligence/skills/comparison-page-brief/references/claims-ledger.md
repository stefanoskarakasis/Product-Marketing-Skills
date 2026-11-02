# Claims Ledger and Lint

## Ledger row

`claim_id`, `text`, `source_url`, `retrieved` (YYYY-MM-DD), `tier` (S1 vendor page, S2 reputable third party, S3 review/community, S4 unsourced), `audience` (public or sales-only), `expires` (30 days pricing, 90 days features), `page_section`.

Public render: S1/S2, inside expiry. Sales-sent render may add S3 labelled as such. S4 never appears. Expired rows are listed in the checklist for refresh.

## Table rules

- Values only: Yes, Partial, Beta, Plan-gated, Not publicly available, No. A "No" needs an S1 source stating absence or a feature list that omits it; otherwise `Not publicly available`.
- Prices carry a unit column (per seat per month, billed annually) and compare annual with annual.
- 8 to 12 rows per table; split into category tables.
- Ratings show source and date; one source per number.

## Lint

1. A statistic supports its claim (a "40% faster" row names what was measured and by whom).
2. Every asterisk resolves to a footnote.
3. No unsourced Yes or No cell.
4. A testimonial's heading matches its attribution.
5. Byline or owner, and update date, appear on the page.
6. One headline count (customers, integrations) comes from one source across all pages.
7. No rating or review schema unless the rating is real and on the page.
8. Sales-only claims are absent from the public render.
