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

## E06 — Branch-control repair submitted

Actor `/root/repair19_branch` submitted authorized repair
`8e2c82679a2314e31ebff69accab3743f55f996d` for blocking
`review-ticket-19/spec-02/F1`. [Repair report](19-repair-c5-report.md),
[checks](19-repair-c5-checks.log) and [C5 source/results](19-evaluation-g5/results.md)
retain full-ref branch semantics and supported transport/routing/read-only fixes.
All C1–C4 sources, reports, old adjudications and prior events remain unchanged.
The worker claim and passing C5 trial alone did not establish independent fixed
status. User-requested reusable authoring skill/probe is distinct from frozen G2
reviewer guidance. No human waiver/deferral or approved-contract change occurred.

## E07 — Exact final source independently verified by Spec

Actor `/root/spec19_round3` independently verifies **both** original blocking keys
`review-ticket-19/spec-01/F1` and `review-ticket-19/spec-02/F1` repaired at exact
`8e2c82679a2314e31ebff69accab3743f55f996d`. [Original spec-03](19-review-spec-03.md),
[identities](19-review-round3-spec-identities.json) and
[disposable observations](19-review-round3-spec-observations.json) reproduce the
old h8/C4 failures and verify final alias/transition and branch/tag/path/routing/
read-only behavior. **Disposition:** fixed for spec-02/F1 and exact-source
revalidated fixed for spec-01/F1, preserving each original classification/history.
Whole-ticket baseline remains f2929e7. Spec reports 0 new blockers/0 optional.
No sibling current output supplied; no authority or M1 acceptance inferred.

## E08 — Independent Standards confirms both fixes

Actor `/root/standards19_round3` separately verifies **both** original blocking keys
`review-ticket-19/spec-01/F1` and `review-ticket-19/spec-02/F1` fixed/revalidated at
exact `8e2c82679a2314e31ebff69accab3743f55f996d`. [Original standards-03](19-review-standards-03.md),
[identities](19-review-round3-standards-identities.json) and its preserved audits
confirm owning operations/current controls and the evidence chain. This
corroborates E07, does not overwrite earlier clean/differing judgments and issues
0 new blockers/0 optional. Original captures/keys and E01–E07 remain unchanged.

**Current actual findings:** none unresolved; both keys are fixed on the final
exact source with independent verification. No pending relevant revalidation,
missing required ticket report, human decision, amendment or blocker deferral.
Further source changes require applicable renewal. The intentionally defective
historical/seeded fixtures keep their own original keys/scope. Real M1 cumulative
source provenance/all-file assessment and exact-candidate human QA remain
unperformed; review completion and ticket completion do not accept a milestone.
