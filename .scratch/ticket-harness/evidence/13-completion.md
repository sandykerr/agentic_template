# Ticket 13 completion evidence

Implemented only [13: Present a tested feature-to-dev candidate](../issues/13-prepare-a-tested-feature-to-dev-candidate.md).
Verified implementation: `19ea4f1b0bbdc601653468212aaaa0a7211d5c6f`.
Original fixed review baseline: `fd292a988cde79532bb84714b5800e4baa5de127`.

## Scope, prerequisites and source identity

A fresh GPT-6.1 Sol Medium worker implemented milestone candidate preparation,
an independent exact-candidate regression gate, an identity-bound QA request,
public CLI/Git coverage and documentation. The five-file implementation checkpoint
preceded both independent High reviews. No implementation changes followed the
final checks or reviews.

[Prerequisite audit](13-prerequisite-audit.json) verifies ticket 12's implementation
`14cafef40726eba80d8648d98d9c263fde3a5d0b` and bookkeeping `969f043` are ancestors
of the starting baseline; all 20 recorded source hashes matched that baseline.
Its five completed criteria, actual checks, separate review reports and retained
observations establish the prerequisite. There was no runtime/test/public-guide
delta since that implementation. Historical 499-test results are not reused as
ticket 13 verification. Ticket 12's earlier prerequisite provenance remains in
[its completion evidence](12-completion.md).

[Final source identity](13-final-source-identity.json), [actual check results](13-check-results.json),
[consolidated observations](13-fixture-observations.json) and the [root audit](13-root-audit.json)
verify the current source. Root and both reviewers independently matched all 20
file hashes to committed `19ea4f1` and current bytes. Every one of the five final
check captures identifies that same source. All 88 distinct final-suite scenarios
match their retained raw JSON after excluding only the added `retained_file`
locator. Temporary fixture repositories were cleaned after capture; their actual
CLI output, records, assignments, gate output, Git identities and applicable QA
request/candidate observations remain consolidated. Raw originals are available
at the manifest's recorded paths under `/tmp/ticket13-checks/archived-observations/renewed-final-suite/`.

No active harness run using these development-plan inputs was identified: the
checkout has only its main worktree and no run records outside historical
evidence. Runtime scenarios used isolated synthetic plans. Approved spec,
proposal and milestone definitions are unchanged. The unrelated unstaged tracker
edit remains byte-identical, SHA256
`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`,
and is excluded from all commits.

## Criterion-specific evidence

The [coverage map](13-coverage-map.md) reuses existing ticket gates, repairs,
dependency, protection and status coverage. Ten new milestone cases exercise
distinct risks; existing two-group and final-group scenarios were extended.
The required final run retains all 40 milestone, 21 dependency and 27 timeout
scenarios. The [implementation report](13-implementation-report.md) maps the
behavior to the implementation.

| Criterion | Verified evidence |
| --- | --- |
| Combined candidate, unchanged dev, later work held | `test_two_group_plan_presents_tested_qa_without_starting_later_work` checks candidate parents/content, caller staged/unstaged/untracked preservation and later Pending/zero-attempt tickets. `test_changed_development_base_is_combined_with_feature_using_a_clean_same_file_merge` observes dev movement during ticket work, then combines its current tip with feature edits, including nonoverlapping edits in one file. The already-contained-feature case still runs regression and waits. |
| Separate exact-candidate regression before request | Every ticket retains its own lightweight checks, Spec/Standards reviews and candidate suite. A separate `milestone-regression` runs configured `suite` against the exact milestone candidate using the candidate timeout. Failed regression leaves Done tickets intact and issues no request. A public status tracer verifies `preparing_milestone` while regression runs. |
| Exact identities, human checks and actual evidence | The passing request records unique run/request identities, plan version/approval/snapshot hash, milestone, feature/development branches and revisions, candidate/worktree, planned setup/actions/pass conditions and the passing regression command/revision/exit/timeout/output evidence. Root audited the equality of request, gate, record and Git identities. |
| Failed/changed candidate cannot become ready or overwrite refs | Failed regression, external feature/development movement, candidate mutation and earlier verified-source mutation preserve evidence and reject readiness. Invalidated gates become failed; external branch tips remain untouched by the harness. No request or promotion occurs, completed tickets stay Done and later groups stay unstarted. |
| Source-changing conflict resolution cannot reuse approvals | Real unresolved conflicts, custom merge-driver resolutions and post-merge hook edits stop before QA, preserving source and diagnostics and explicitly requiring renewed checks/reviews. An independent plain merge isolates target configuration/attributes; changed resolution source cannot inherit ticket approvals. Ordinary clean same-file merges pass. This ticket stops for renewal; it does not claim to launch conflict-repair or renewed-review assignments. |

For the passing two-group observation, exact feature/development/candidate values
are also retained together in [the root request audit](13-root-audit.json).
They are fixture identities, not this repository's M1 QA candidate or acceptance.

## Actual checks and development provenance

All Python used the documented reusable environment. [Tool verification](13-tooling.json)
records Python 3.12.16, pytest 9.2.0, mypy 1.19.1, Ruff 0.14.10 and Git 2.53.0.
Command-local `PYTHONPATH=/tmp/ticket12-tools` reused verified pinned check tools;
the shared environment was unchanged. [Actual commands/output](13-checks.log)
and [command exits/timings](13-check-results.json) retain the final results.

| Actual command | Result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **509 passed in 795.92s**; wrapper elapsed 796.788s. |
| Reusable Python `-m mypy` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples` | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples` | Exit 0: 20 files formatted. |
| `git diff --check`; committed original-baseline diff whitespace | Exit 0. |

Packaging and entry points did not change; installed packaging checks were not
required under the testing policy. Existing packaging is not claimed as newly tested.

[Development provenance](13-development-notes.md) separates red/green and focused
checks from final verification. The first full-suite wrapper was interrupted
after a self-audit found transient `completed` status during preparation; observed
wrapper exit was 130, and the child pytest exit/count was not observed. The CLI
tracer reproduced the bug, then passed after `preparing_milestone` was implemented.
The entire required full/static set was renewed afterward. Only
`13-renewed-final-*` captures establish the final implementation. Earlier
`13-final-*`, interrupted and development checks remain historical. Exact
originals of three whitespace-normalized historical display logs are retained in
[13-log-originals.json](13-log-originals.json).

## Separate independent reviews

[Spec](13-review-spec.md): fresh `/root/review_spec13`, GPT-6.1 Sol High,
original baseline and `19ea4f1`. **0 blockers; 0 optional suggestions.**
Independently checked all five final captures against 20 committed/current hashes,
all 88 raw/consolidated observations and representative requests/failures.
Reproduced changed-base and failed-regression public CLI scenarios:
**2 passed, 38 deselected in 12.89s**.

[Standards](13-review-standards.md): separate fresh `/root/review_standards13`,
same independently configured High setting and review range. **0 blockers;
0 documented violations; 1 optional suggestion.** Independently verified the
same hashes, final check provenance and all 88 observations. The optional possible
Duplicated Code suggestion concerns repeated read-only status assertions at
`tests/test_milestones.py:140` and `:177`; it is recorded without mandatory rework.

Neither reviewer read the other's report or changed implementation. They
inspected the full-suite evidence without claiming an independent full repeat.
No blocking repair was required. Scripted fixture reviewers are distinct from
these independent implementation reviews.

## Completion and next handoff

All five criteria and required gates are verified at `19ea4f1`. The ticket header,
checked criteria, completion comment and feature index agree; prior readiness is
`ready-for-agent`, and declared dependencies remain history. No unchecked
criterion or unresolved blocker remains. The optional Standards cleanup is not a
completion gate. Ticket/index/evidence receive a separate bookkeeping commit;
its identity is available from this file's Git history. The generated handoff
receives a third separate commit. No push occurred.

Ticket 14 is next in the approved M1 order, followed by prerequisite-ready 15.
The handoff does not launch either. M1 and final feature QA remain unaccepted;
M2 stays gated by human acceptance of M1. E1 ticket 25 retains its independent
priority immediately after verified 24 and does not gate release acceptance.
Approval consumption/promotion, planned continuation, QA correction workflows,
background operation, live Codex and role skill capture remain later slices.
Source-changing conflict resolutions must obtain renewed checks/reviews before
any future QA request. Plain-merge validation requires Git `--attr-source`
support and fails closed when unavailable. Status is observational after a run
stops; future approval consumption must revalidate exact current identities.
