# Append-only implementation finding history: review-ticket-19

Corpus seed keys/history retain their own separate fixture scopes. This history
tracks actual ticket 19 implementation findings and subsequent verification.

## E01 — Original contract/source mismatch

| Field | Value |
| --- | --- |
| Full finding | [review-ticket-19/spec-01/F1](19-review-spec.md#f1--blocking-h8-cannot-supply-the-required-fourth-acceptable-control-under-its-frozen-contract) |
| Disposition/classification | Open; original blocking finding |
| Actor/role | `/root/spec19` original reviewer; `/root` records history after preserving both independent reports |
| Affected revision | `e90abb64ab95c5b15cdb0949b03c6a948365339b` |
| Reason/evidence | h8 source accepts dictionary identity/revision by reference despite explicit input-isolation promise. [Original report](19-review-spec.md), [exact-source observation](19-review-spec-h8-observation.json), [source/check identities](19-review-spec-identities.json) |
| Prior/superseded observation | Initial implementation finding. Both corpus reviewers disclosed but accepted scalar assumptions; G1 evaluator classified clean. Originals preserved, not retroactively reclassified or rewritten. Standards implementation review remains its original clean result. |
| Repair | Authorized bounded evaluation repair for [ticket 19](../issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md), fresh Medium `/root/repair19`; no neighboring production refactor |
| Repair commit/verification | Pending repair checkpoint and fresh independent exact-source whole-ticket Spec/Standards re-review |
| Human decision/amendment | Not required for original-contract fixture/evaluation correction; no waiver, deferral, risk acceptance or approved requirement change authorized |
| Milestone assessment | Real M1 unperformed; no candidate or acceptance |
| Next action | Preserve G1, append failed-trial/mismatch evidence, declare a complete versioned corpus with a genuinely acceptable fourth control and any guidance correction, run fresh independent full-corpus trials, renew checks/commit/reviews. |

## E02 — First repair submitted; independent verification required

Original blocking key `review-ticket-19/spec-01/F1`; actor `/root/repair19`
submitted authorized evaluation repair `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`.
[Repair evidence](19-repair-report.md), [actual checks](19-repair-checks.log) and
complete C1–C4 preserved source/reports support its claimed h8 correction. This
worker claim alone did not establish fixed disposition. No human decision or
amendment required; actual M1 assessment/QA unperformed.

## E03 — Original h8 blocker independently fixed

**Finding:** `review-ticket-19/spec-01/F1` (original blocking classification).
**Disposition:** fixed at exact `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`.
Actor `/root/spec19_round2` independently traced and exercised dictionary/list
input, returned snapshot aliases and invalid transitions, verifying the repair
without the sibling current-round output. [Original spec-02](19-review-spec-02.md),
[identities](19-review-round2-spec-identities.json),
[observations](19-review-round2-spec-observations.json) independently verify E02's
claim. The new b7 finding below is distinct, not a supersession of h8. This does not
accept the whole ticket or M1. Source changes require relevant revalidation; no
human risk waiver, deferral or approved-contract change occurs.

## E04 — Independent Standards confirms original fix

Actor `/root/standards19_round2` separately verifies original blocking
`review-ticket-19/spec-01/F1` fixed at exact `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`.
[Original standards-02](19-review-standards-02.md),
[identities](19-review-round2-standards-identities.json) and linked source/tool
observations confirm deep-copy ownership and pre-mutation transition guarantees.
This corroborates E03; original reports remain unchanged. Standards issues no new
finding. No ticket/candidate/milestone acceptance follows.

## E05 — New branch/tag control mismatch

**Finding:** [review-ticket-19/spec-02/F1](19-review-spec-02.md#f1--blocking-final-b7-falsely-rejects-the-requested-branch-when-a-tag-shares-its-name).
**Disposition:** open; original blocking classification at exact
`ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`.
Actor `/root/spec19_round2` reproduced a clean requested branch `main` alongside
same-name tag `main`: Git's short symbolic ref is `heads/main`, so b7 rejects the
actual requested branch. [Exact-source observation](19-review-round2-spec-b7-observation.json)
and [original report](19-review-spec-02.md) establish a valid control breach missed
by both original C4 corpus reviewers/evaluator. C4 originals and their passing
adjudication must remain preserved with a later correction, not rewritten.

Authorized fresh Medium `/root/repair19_branch` prepares bounded ticket-19 source,
evaluation and summary repair; exact commit and fresh independent verification
pending. Use full local-branch symbolic ref semantics, declare complete corrected
corpus before fresh independent evaluation, renew standalone checks and whole-ticket
reviews from the original baseline. No production refactor, contract weakening,
blocker deferral, human risk acceptance or amendment is authorized/required. Original
h8 key remains independently fixed at its recorded source; renewed whole-ticket
review must name the later exact source. M1 cumulative assessment/QA unperformed.
