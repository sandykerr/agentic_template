# Spec report spec-01

**Synthetic report:** scripted snapshot; not an actual reviewer assessment.

**Assessment:** [review-ticket-01](../reviews/ticket-01.md).
**Fixed baseline:** `77e55e3d5ce00a42f5a17d355a46ec78a386b3c3`.
**Instructions:** [retained instruction identities](instructions.md).
**Settings:** intended GPT-6.1 Sol / High / 250K; actual executor is the
retained scripted helper, no real model assignment claimed.
**Evidence/source identities:** [commits and snapshots](commits.md); SHA-256
capture identities are retained in the [external manifest](../manifest.json).

**Report/assignment:** spec-01 / synthetic-spec-assignment-01 / Spec attempt 1.
**Assessed source:** `77e55e3d5ce00a42f5a17d355a46ec78a386b3c3`.
**Inspected:** source.md, captured-input preservation statement.
**Omitted:** runtime, all real code; not part of this synthetic record example.
**Assumptions:** source statements stand in for behavior; no runtime proof.

## F1

Full key: `review-ticket-01/spec-01/F1`. Blocking: captured inputs can change.
Source A says preservation is no. Repair the authorized statement to yes and
verify the exact source independently. [Disposition history](../reviews/history.md#e01).

## F2

Full key: `review-ticket-01/spec-01/F2`. Optional: clearer wording would help.
No correctness consequence or integration blocker. [History](../reviews/history.md#e06).

## F3

Full key: `review-ticket-01/spec-01/F3`. Optional consequential risk: humans may
mistake simulated evidence for runtime proof. Require an explicit decision for
the demo's labelled presentation at C. [History](../reviews/history.md#e07).

## Result

Assessment report completed. F1 requires repair; F2/F3 remain visible. This is
the original observation, independent of later dispositions.
