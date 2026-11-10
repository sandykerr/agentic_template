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
