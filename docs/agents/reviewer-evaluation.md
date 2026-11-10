# Evaluated development-review guidance

For ownership refactors 20–24, use the existing
[ownership and scope contract](ownership-review.md), [review records](review-records.md)
and [architecture checkpoints](architecture-checkpoints.md), with the approved
role-specific design/testing guidance. Carry the evaluation references below into
planning, worker/repair context and both implementation and M1 checkpoint handoffs.
This evidence supplements the approved spec; it does not replace new source review.

## Evaluated version and finite evidence

**G1** is the substantive guidance frozen from baseline
`f2929e79cfd5a68f670862775053ae85ba9582b5`, with
[exact guidance/source digests](../../.scratch/ticket-harness/evidence/19-evaluation/source-manifest.json)
and [retained reviewer snapshot](../../.scratch/ticket-harness/evidence/19-evaluation/snapshot/REVIEW.md).
The [pre-assignment corpus declaration](../../.scratch/ticket-harness/evidence/19-evaluation/declaration.md)
identifies eight short synthetic cases: four required concerns and four acceptable
controls. [Evaluation record](../../.scratch/ticket-harness/evidence/19-evaluation/README.md)
links original inputs, settings, raw reports, history and capture limitations.

One fresh GPT-6.1 Sol High Spec assignment and one separately configured fresh
High Standards assignment each assessed the complete corpus. The
[per-case expected/observed comparison](../../.scratch/ticket-harness/evidence/19-evaluation/results.md)
records all four concerns detected on their declared relevant axes and no unsupported
blocker on the controls. No optional suggestions were raised. There was one trial,
no judgment miss, no substantive guidance correction and no retrial. Reviewer report
preservation followups are evidence capture, not more trial observations.

These are bounded observations under explicit contracts, not guaranteed detection
or a general reliability rate. They do not assess actual package architecture,
large-file attention, future refactors or production runtime behavior. In particular,
h8's copied observations were accepted under ordinary scalar identity/revision
values. Its unspecified nested mutable input types remain a disclosed limitation;
no deep-copy guarantee was demonstrated. Future reviews must establish actual value
types and contracts rather than carrying that assumption to unrelated source.

## Use in subsequent work

Supply both fresh reviewers with the current approved contracts, original ticket
baseline, exact committed source, affected callers/owners/writers/consumers,
persistence/restoration/invalidation paths, test coverage/check evidence and prior
full finding keys/dispositions. Apply G1's substantive reasoning and reporting
contract. The corpus's outcomes are evaluator material; they are not requirements
to reproduce particular findings in new source. Record actual inspected scope,
clean reasoning, omissions and assumptions. Evidence-specific optional suggestions
remain optional, and authorized in-scope repairs proceed under existing bounds.

If substantive guidance changes, identify that new version and retain G1 as
historical evidence. No evaluation is silently transferred to changed instructions
or source. Changed authoring routes are checked separately from reviewer judgment.
Required detection misses/unsupported blockers stay visible with original reports;
a correction needs fresh complete declared-corpus evaluation before claiming the
corrected version met this evaluation. Actual later refactor reviews and decisions
belong to tickets 20–24 and the real M1 cumulative assessment, not this corpus.

Carry any unresolved evaluation limits, actual finding keys, missing/stale review
work and consequential human decisions into the next handoff. The corpus's seeded
findings remain open only in their frozen fixtures; they are not actual harness
blockers. Human design/risk/scope decisions and exact-candidate milestone QA remain
human-owned. Clean reviews and ordinary authorized repairs provide no acceptance.

This is development evidence. Requested/observed assignment settings, readable
reviewer-preserved inputs and opaque session captures do not establish runtime
backend availability, effective instruction delivery, filesystem isolation or hard
context enforcement. Tickets 33/34 must verify runtime enforcement/delivery and
actual behavior separately. No harness run or production private-module tests are
part of this evaluation. M1 cumulative review and human QA remain unperformed.
