# Efficient ticket development

Apply this procedure before requesting development review or another repair round.
It reduces premature assignments and repeated setup while preserving the target's
required checks, fresh role assignments, whole-ticket review and human QA authority.
The [testing policy](testing.md), [ownership contract](ownership-review.md) and
[review records](review-records.md) remain authoritative. These are development
instructions; runtime enforcement remains separate work.

## Prepare before requesting review

1. **Plan the necessary work.** Map acceptance requirements to existing coverage
   and distinct missing observations. Identify required roles/checkpoints and any
   agreed time, context or repair bounds in the existing ticket notes. Ordinary
   tickets use their implementation worker and required independent reviewers;
   additional assignments need a concrete task or required checkpoint. Local
   test failures, formatting, links and capture setup stay with the current worker.
2. **Check the promises locally.** Before review, the worker traces the affected
   operations, callers, writers and failure behavior against the actual contract.
   Reuse relevant tests and probe representative risks left uncovered. A copying
   promise calls for checking retained aliases; a parser change calls for checking
   the relevant accepted/rejected inputs. Choose risks from the change rather than
   expanding every possible input combination. Reviewer evaluation alone uses
   [evaluate-reviewers](../../.agents/skills/custom/evaluate-reviewers/SKILL.md) to
   establish concern/control ground truth before freezing its corpus.
3. **Finish checks and evidence first.** Arrange commands, output paths and lossless
   raw capture before execution. Use normal local tools for mechanical validation.
   Keep the current worker iterating until the required final-source checks pass
   and the promised observations are retained, then commit the implementation.
   A missing log calls for collecting the missing observation; it does not justify
   replaying an entire passing matrix or launching another source reviewer.
4. **Supply one usable evidence index.** Give both reviewers the same original
   baseline/current committed source, contracts, affected scope, coverage/check
   results and relevant full finding keys/history. Link canonical artifacts by
   path and revision instead of rebuilding duplicate packets. Send role-specific
   instructions, with raw details available for inspection. Completed prerequisite
   campaigns keep their original evidence; repeat them only for a concrete
   compatibility uncertainty or a required gate. Reviewers still inspect actual
   source and relevant collaborators; a summary or passing check is not a review.

Request the required fresh Spec and Standards assessments independently on that
same checkpoint, in parallel where available. Keep their current outputs separate
until all originals are saved. Preparation is complete when the contract/coverage
map, required passing checks, retained evidence and committed source are ready;
an incomplete packet stays with the current worker.

## Repair a complete diagnosis

Collect both original reports before changing their assessed source or dispatching
the repair. Consolidate their blocking findings by full key, preserving different
judgments and optional suggestions. A fresh repair assignment receives the complete
rejection and original baseline under the existing role/repair contract.

The repair worker checks the demonstrated failure and closely related paths within
approved scope before resubmitting. For an alias failure, trace input, saved/restored
and returned references where present; for a decoding failure, inspect the relevant
representation conversions. This is a bounded cause investigation, not permission
for a neighboring refactor or an exhaustive new test matrix. Finish all authorized
related fixes and affected checks locally, renew required final-source checks,
commit, then obtain the required fresh whole-ticket axes from the original baseline.
Optional suggestions alone do not create repair assignments.

If another round exposes the same failure pattern, pause new dispatches and use the
current worker/orchestrator to diagnose what preparation missed. Record rounds and
assignments so far, the remaining blocker, the next assignment's purpose and any
applicable bounds in the existing evidence. Resolve unstable examples/contracts,
capture failures or an incomplete repair before paying for another full round.
Continue authorized work; seek a human decision only where existing scope/authority
or exhausted agreed bounds require it. Cost limits never turn missing checks or an
unresolved blocker into a pass.

## Reuse evidence with its actual scope

Reuse unchanged mechanical evidence only when its source, inputs and scope still
match, and the governing check policy permits it. Source changes renew applicable
checks and reviews. Bookkeeping/handoff changes receive their own consistency and
link checks rather than replaying production tests. Preserve all failed trials,
original reports and append-only dispositions. Report actual checks and remaining
limits; fewer assignments alone is not evidence of correctness.

The [ticket 19 record](../../.scratch/ticket-harness/evidence/19-completion.md)
motivates these changes: invalid nominal controls and incomplete preparation
repeatedly reached expensive reviewers. Its completed reports and finite G2/C5
claim retain their original source/instructions. This later preparation procedure
does not retroactively validate itself through that evaluation or reopen ticket 19.
