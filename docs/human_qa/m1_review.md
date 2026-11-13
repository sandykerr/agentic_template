# Milestone 1 human code review

## Helper functions
These functions need helper functions:

1. tickets._TicketExecution.execute()
2. runner._Run.check()
3. records.protect(): I'm on the fence on this one
4. records.execute(): a lot of nested code, I'd prefer to extract helpers to keep it more readable.
5. qa.MilestoneReview._prepare()
6. qa.MilestoneReview.restore_checkpoint(): a helper could be useful but I'm having trouble seeing where it could be inserted
7. plans.validate()
8. inputs.load()
9. inputs.completed_tickets()
10. inputs.normalize_ticket()

## Other abstractions I think fit

### Enumerations:
1. agents.assignment() - creates a lot of dicts, we could define these in a separate file, create a factor or something; it looks ugly to me to create the large dict in that function.
2.

## Documentation

Most functions need more extensive docstrings, especially object methods. Implement this with medium gpt6.1-sol workers, with you as a reviewer.

## Response and implementation — 2026-11-12

Implemented the readability and docstring changes with three fresh GPT-6.1 Sol
workers at Medium reasoning, with root reviewing their code. Each worker owned a
different set of files; they also inspected another worker's changes without
editing them. Your review remains above, with the responses below.

### Helper functions

| Review point | Result and rationale |
| --- | --- |
| `tickets._TicketExecution.execute()` | Extracted `_implement()` for worktree preparation, assignment and submission, and `_prepare_repair()` for invalidation, branch/HEAD checks and repair context. The attempt loop retains visible stage assignments, repair eligibility and integration order. |
| `runner._Run.check()` | Extracted `_evaluate_report()` for report validation, findings and human-decision handling. `check()` retains gate append/save, environment/timeout precedence, verification registration and source invalidation. The helper preserves nonrepairable errors even when it fails before returning its classification. |
| `records.protect()` | Kept the capture/restore loop together. Its `finally` block must retain rejected bytes before restoring protected paths and updating evidence. Splitting that loop would scatter this ordering; its docstring now explains restoration policy and failures. |
| `records.execute()` | Extracted `_communicate()` for deadlines, group termination and bounded output draining, and `_finish_process()` for cleanup in `finally`. The main function shows artifact setup, process creation, output recording and guaranteed cleanup. |
| `qa.MilestoneReview._prepare()` | Extracted `_verify_candidate()`, `_publish_request()` and `_restore_request()`. The entry method now shows the fresh-versus-restored branch; the review remains the owner of both paths. |
| `qa.MilestoneReview.restore_checkpoint()` | Extracted `_require_checkpoint_identity()` for schema, directory, embedded-record and archive checks. The remaining method shows the ordered approved-input, frozen-evidence, verified-source and request checks. Canonical check restoration stays with the run. |
| `plans.validate()` | Extracted milestone membership/QA validation, dependency-order checking and worker-setting normalization into `_milestone_membership()`, `_validate_dependency_order()` and `_worker_settings()`. Existing validation and mutation order remain intact. |
| `inputs.load()` | Extracted `_input_paths()`, `_capture_inputs()`, `_ticket_requirements()` and `_require_executable()`. `load()` still performs the complete checked preparation and constructs `PreparedInputs` only after every required phase passes. |
| `inputs.completed_tickets()` | Extracted `_collect_completed()` for each saved record's Done state, approved ticket hash, revision ancestry and duplicate checks. Record loading and source-attributed error wrapping remain visible in the caller. |
| `inputs.normalize_ticket()` | Extracted `_ticket_dependencies()` and `_ticket_acceptance()` for the two substantial parsing phases. Heading, metadata, readiness and check validation remain in their original order. |

### Assignment dictionaries and enumerations

The large nested literal in `agents.assignment()` describes a report schema,
rather than an enumeration of runtime states. Extracted `_report_contract()` in
the same module to name that responsibility and keep assignment construction
readable. It returns fresh nested dictionaries/lists for each assignment. A
separate factory module or enum would add navigation and conversion without
improving this contract, so neither was introduced. Wire field names, role-specific
content and existing supplied gate/check/repair references are preserved.

### Docstrings

Added or expanded docstrings across the package's nontrivial functions and object
methods, including the Git operations and CLI entry point. They describe relevant
preconditions, results, state changes, alias identity, ordering and failure
behavior. Simple observation methods retain short descriptions; the more involved
preparation, verification, process and checkpoint methods explain their contracts
in more detail.

### Review and verification

Root reviewed the changed flows against the pre-edit source. The supplemental
worker reviews found no regression in stage attribution, repair state, report
precedence, process cleanup, validation order, mutable assignment contracts or
canonical restored evidence. All four ownership triggers remain **No** before
and after: no new lifecycle, persistence/restoration path, shared mutable state
or additional writer was introduced.

Focused checks passed: execution/report handling **21 cases**; input/plan handling
**104 cases**; process/QA handling **38 cases**. These are separate selections and
are not presented as a count of distinct tests. Strict mypy, Ruff lint, Ruff
format and whitespace checks passed on the combined source.

The first full-suite campaign was stopped after three Git-observer scenarios
failed; [the interrupted result](../../.scratch/ticket-harness/evidence/m1-human-review-01/interrupted-suite-result.json)
is retained. A comparison with the pre-edit package also reproduced the observer
problem. The existing tests now arm the observer before the candidate check is released
and use optional real Git Trace2 events to identify an unreaped Git child after
its command line disappears. Trace history alone cannot select a child. Existing
authority/ref/lock assertions and time limits remain intact; no cases were removed
or production hooks introduced. Three final same-source trials each passed all
three affected cases. The failed/control trials and exact source hashes are
retained in the [worker evidence archive](../../.scratch/ticket-harness/evidence/m1-human-review-01/worker-evidence.tar.gz).
These are finite Linux/installed-Git observations, not a universal scheduling
guarantee. **The renewed full suite passed all 559 cases**. Strict mypy, Ruff lint, Ruff
format and whitespace checks also passed on that same source. The [full result](../../.scratch/ticket-harness/evidence/m1-human-review-01/renewed-suite-result.json),
[static results](../../.scratch/ticket-harness/evidence/m1-human-review-01/renewed-static-results.json)
and [root review](../../.scratch/ticket-harness/evidence/m1-human-review-01/root-01.md)
retain exact commands, outputs and scope. Source/test hashes remained unchanged
through the full run; total wrapper time was 969.47 seconds. [Final source identities](../../.scratch/ticket-harness/evidence/m1-human-review-01/renewed-source.json) and [starting context](../../.scratch/ticket-harness/evidence/m1-human-review-01/start.json)
identify the starting commit and actual working-tree changes; no uncommitted
implementation is represented as verified unchanged HEAD.

### M1 status

This response implements the requested readability corrections. The separate
Git-index routing blocker `review-M1-architecture-01/standards-01/F1` remains open;
these changes do not fix it. The original cumulative report and earlier QA
candidate retain their historical source identities. Current-source cumulative
review, candidate preparation and explicit human acceptance remain required
before M1 readiness/acceptance or M2 progression.

## Human review completion — 2026-11-13

The human reported: “I've done my part of the human code and documentation review.”
The human code/documentation review is therefore recorded as complete. The human
also proposed marking M1 complete; this statement does not identify a tested
candidate or explicitly disposition the separate caller-index blocker.

The [M1 assessment](../../.scratch/ticket-harness/reviews/M1-architecture-01.md)
still records `review-M1-architecture-01/standards-01/F1` as open. Under
[ADR-0002](../adr/0002-human-qa-gates-feature-promotion.md) and the
[M1 pass conditions](../../.scratch/ticket-harness/milestones.md#m1-a-complete-qa-controlled-git-cycle),
closing the milestone still requires resolving that finding, renewed applicable
checks/cumulative review, and explicit acceptance of the exact tested candidate.
This entry records completed human review without inventing those technical
results, a risk waiver, a candidate-specific QA decision or M2 eligibility.
