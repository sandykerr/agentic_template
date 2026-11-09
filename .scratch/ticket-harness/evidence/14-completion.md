# Ticket 14 completion evidence

Implemented only [14: Consume approval, promote, and continue](../issues/14-promote-only-the-human-approved-milestone.md).
Verified implementation: `29fb5569cf53c75bd351d6bd176bb29889c42a65`.
Original fixed review baseline: `d67c12d91495af00557b279d0bf0e1da518e6fcc`.

## Scope and provenance

A fresh GPT-6.1 Sol Medium worker implemented the foreground QA decision,
promotion and next-group cycle. Only seven source/test/public-guide paths are in
the implementation checkpoint. The approved CLI/external-script/isolated-real-Git
seam is preserved. No runtime source, test or public-guide changes followed final
verification or independent review.

[Prerequisite audit](14-prerequisite-audit.json) verifies ticket 13's implementation
`19ea4f1` and bookkeeping `fb3874a` are ancestors of the starting baseline, all 20
historical source hashes match the implementation and starting baseline, five final gate captures agree,
and all 88 retained historical observations match their raw originals. Its
[completion evidence](13-completion.md) retains earlier prerequisite provenance.
Those historical 509-test results are not ticket 14 verification.

[Final source identity](14-final-source-identity.json), [actual checks](14-check-results.json),
[consolidated observations](14-fixture-observations.json) and the independent
[root audit](14-root-audit.json) establish the reviewed implementation's identity.
All 21 captured source hashes match committed `29fb556` and current bytes; every
final check has that same map. All 103 consolidated scenarios exactly match their
retained raw JSON after excluding the added `retained_file` locator. Raw records
are retained in [14-observations/final-suite/](14-observations/final-suite/).
Temporary fixture repositories were cleaned after their observations were saved.

No active harness run using these development-plan inputs was identified: only
the main checkout worktree exists and no run record was found outside retained
historical evidence. Synthetic fixture plans are separate from this development
plan. Approved spec, proposal and milestone definitions remain unchanged. The
unrelated unstaged tracker edit is excluded from all commits and retains SHA-256
`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.

## Criterion-specific evidence

The [coverage map](14-coverage-map.md) reuses existing milestone, dependency,
transaction, report, repair and integrity coverage. Fifteen new public CLI cases
cover distinct approval/authority/invalidation/eligibility failures. The final
run retains 21 dependency, 40 milestone, 15 QA and 27 timeout scenarios.
The [implementation report](14-implementation-report.md) describes the bounded behavior.

| Criterion | Verified evidence |
| --- | --- |
| Separate exact approval; reject invalid/stale/replayed authority | `test_invalid_decisions_keep_waiting_without_repairs_or_authority_from_incidental_text` exercises incidental text, malformed JSON, missing/extra/duplicate fields, nonexact decision values, request/run/milestone/version mismatches and Boolean-for-numeric evidence substitution. The two-group test rejects a stale candidate and replay of M1 acceptance at M2. Only `{"decision":"APPROVED","request":<complete current request>}` with matching JSON types/values authorizes promotion. |
| Observable indefinite waits; no repair consumption or worker self-approval | The invalid-decision scenario waits beyond every configured process timeout with unchanged attempts, observes missing/unreadable/rejected states, and replaces directory/FIFO artifacts without blocking the watcher. Initial and repair variants of `test_implementation_and_repair_cannot_write_qa_authority` reject worker writes through protected-path integrity. Preparation fixtures retain successful status reads separately from intentional foreground termination. |
| Expected-old promotion to exact candidate; align before later work | `test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision` verifies dev advances to the first tested candidate and the next worker's HEAD/base/integration all identify that commit. A single `update-ref` transaction compares and advances dev and feature together. All later ticket checks/reviews/candidate gates still execute; only one shared baseline runs. |
| Preserve external movement; reject stale state; retain consumed decision | Nine `test_acceptance_revalidates_the_exact_candidate_evidence_and_both_refs` variants cover both externally moved refs, candidate/prior source, approved input, request, regression evidence, and checked-out dev/feature. They preserve observed refs, consume no decision and leave later attempts zero. Consumed decisions retain actual bytes/hash/request identity; prior acceptance cannot authorize a new request. |
| Feature complete only after final promotion | The two-group scenario observes all required tickets Done while M2 remains `awaiting_human_qa` with `feature_complete: false`. Only the second accepted promotion makes dev/feature equal the final tested candidate, records `completed`/true and exits 0. Single-final-group and legacy coverage remain passing. |
| Two foreground milestones with stale rejection and acceptance-controlled progress | The complete two-group CLI fixture demonstrates both waits, stale rejection, first acceptance unlocking M2, replay rejection and final completion. Root independently verified both consumed hashes, next-worker alignment and final refs in the [scenario audit](14-root-observation-audit.json). The separate Spec reviewer reproduced this public scenario successfully. |

Full-plan readiness and outside-plan prerequisites are now validated before any
worker starts, including later groups. Two focused cases prevent executing a later
human-ready ticket or a ticket missing external prerequisite evidence.

## Actual checks and development evidence

All Python used the documented reusable environment. [Tool verification](14-tooling.json)
records actual versions; command-local `PYTHONPATH=/tmp/ticket12-tools` reused
the pinned mypy/Ruff tools without modifying the shared environment.
[Actual commands/output](14-checks.log) and [results/timings](14-check-results.json)
record the final gates:

| Command | Actual result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **524 passed in 684.03s**; wrapper elapsed 684.962s. |
| Reusable Python `-m mypy` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples` | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples` | Exit 0: 21 files formatted. |
| `git diff --check` | Exit 0; staged implementation and committed original-baseline whitespace checks also exit 0. |

Packaging and entrypoint files did not change; installed packaging checks are not
required under the testing policy and are not claimed as newly tested.
[Development provenance](14-development-notes.md) separates three actual red/green
slices and focused checks from the final captures. Only `14-final-*` establish the
final implementation's required checks. Exact historical red-log bytes/hashes are
preserved in [14-log-originals.json](14-log-originals.json); only trailing whitespace
was removed from their display logs. Final logs are unchanged.

The initial authorized staging request's automatic approval review timed out;
its explicitly permitted retry succeeded. The implementation checkpoint and its
renewed staged/committed whitespace checks completed. This is resolved, not a
remaining permission blocker.

## Separate independent reviews

[Spec](14-review-spec.md): fresh `/root/review_spec14`, GPT-6.1 Sol High,
fixed baseline through `29fb556`. **0 blockers; 0 optional suggestions.**
Independently audited final source/check identities, retained outcomes and historical
log provenance. Reproduced the public two-milestone scenario: **1 passed in 9.37s**,
exit 0; independently checked committed-diff whitespace.

[Standards](14-review-standards.md): separate fresh `/root/review_standards14`,
independently configured GPT-6.1 Sol High, same review range. **0 blockers;
0 documented violations; 1 optional suggestion.** Verified final identities,
representative artifacts and nine rejection outcomes. The optional possible
Duplicated Code suggestion concerns polling mechanics shared by `wait_for` and
`run_until_wait` in `tests/test_milestones.py:78–108`; it remains optional maintenance.

Neither reviewer read the other axis's report or changed implementation. Scripted
fixture reviewers do not replace these implementation reviews. No blocking repair
or further executable change was required, so the final suite remains current.

## Completion and handoff

All six acceptance criteria and required gates are verified at `29fb556`. The
ticket header, checked criteria, completion comment and feature index agree.
Previous readiness is `ready-for-agent`; declared dependency history is preserved.
No unchecked criterion or unresolved blocker remains. Ticket/index/evidence are
committed separately from implementation; that bookkeeping revision is available
from this file's Git history. The generated handoff is a third separate commit.

Ticket 15 is prerequisite-ready next in M1. This completion does not execute it,
accept M1 or complete the development feature. M1 and final human QA remain
unaccepted; M2 stays gated. E1 ticket 25 retains its separate priority immediately
after verified 24 and never gates release acceptance. Planned restart/ownership,
QA sessions/corrections, background operation, live backend and OS role enforcement
remain later slices. No real human decision was synthesized, and no push occurred.
