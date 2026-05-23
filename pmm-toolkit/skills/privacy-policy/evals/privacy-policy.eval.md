---
skill: privacy-policy
test_count: 3
version: 1.0.0
---

# Privacy-Policy Evals

## Test 1: Jurisdiction Detection

**Input:** "Create privacy policy for B2B SaaS product selling to US + EU customers"
**Expected:** 
- Generates policy covering GDPR (EU) + CCPA (California)
- Flags high-risk clauses with [⚠️ LEGAL REVIEW REQUIRED]
**Pass:** Both jurisdictions covered; legal review flags present

---

## Test 2: Data Types

**Input:** "Privacy policy for mobile app collecting location + payment data"
**Expected:** 
- Includes sections for sensitive data (location, financial)
- Proper consent language
- Data retention policies
**Pass:** All data types addressed; consent mechanisms specified

---

## Test 3: Legal Review Markers

**Input:** Any privacy policy generation
**Expected:** High-risk clauses marked with [⚠️ LEGAL REVIEW REQUIRED]
**Pass:** Legal review flags present; output states "requires legal review"
