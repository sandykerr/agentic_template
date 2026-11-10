# Isolated review tracker example

All reports, reviewer assignments, plan approvals and human decisions here are
**synthetic**. Only disposable Git commits, source snapshots and mechanical check
observations are real. This is saved Markdown illustrating the
[record contract](../../../../docs/agents/review-records.md); it neither accepts
real risk nor completes ticket 16, calibration or a development milestone.

## Originating work

- [Ticket 01](issues/01-preserve-input.md) and [optional follow-up 02](issues/02-polish.md).
- [Milestone MX](milestones.md), with a separate QA decision still absent.
- [Ticket assessment](reviews/ticket-01.md): Spec and Standards reports share one work item.
- [Cross-ticket assessment](reviews/architecture-MX.md): its own review ID, no ticket number.
- [Exact source commits](evidence/commits.md) and [instruction identities](evidence/instructions.md).

## Six navigable histories

| Case | Concern | History and outcome |
| --- | --- | --- |
| Fixed finding | [Spec F1](evidence/spec-01.md#f1) | [Independent exact repair and revalidation](reviews/history.md#e05) |
| Deferred optional finding | [Spec F2](evidence/spec-01.md#f2) | [Linked follow-up](reviews/history.md#e06) |
| Explicit human risk decision | [Spec F3](evidence/spec-01.md#f3) | [Awaiting decision](reviews/history.md#e07) then [synthetic decision](reviews/risk-decision.md) |
| Duplicate local IDs | [Spec F1](evidence/spec-01.md#f1) and [Standards F1](evidence/standards-01.md#f1) | [Distinct full keys](reviews/ticket-01.md#current-findings) |
| Reopened changed source | [Standards F1](evidence/standards-01.md#f1) | [Original fix](reviews/history.md#e04), [new report](evidence/standards-02.md#f1), [reopened event](reviews/history.md#e09) |
| Completed review, outstanding findings | [Ticket assessment](reviews/ticket-01.md) | [Unresolved current concern](reviews/history.md#e09) and [pending milestone assessment](milestones.md) |

The helper records hashes before history/index changes and verifies original
reports/evidence stay unchanged. It records append-only prefix preservation for
history events, resolves these links/anchors, and retains commands/results in
the [check output](../16-check-results.json). Scripted observations test record
mechanics only, not reviewer effectiveness or runtime enforcement.
