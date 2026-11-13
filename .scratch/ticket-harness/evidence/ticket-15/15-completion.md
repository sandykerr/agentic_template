# Ticket 15 completion evidence

Implemented only [15: Continue after a deliberate QA stop](../issues/15-continue-from-a-planned-qa-checkpoint.md).
Original fixed review baseline: `90255aaf6faf9aedce18f7159093f5dbfde294b7`.
Initial implementation: `36ed3e72c278cf147c84ae9c282cd2899af23ad0`.
Final implementation and review repair: `d11f0bc60a2c11c40683e58581dffa10e36a91be`.

## Scope and provenance

Fresh GPT-6.1 Sol Medium implementation and repair assignments implemented the
planned foreground QA stop/continuation contract. Each targeted 250K active context.
The [public guide](../../../docs/ticket-harness.md) documents `stop RUN_DIRECTORY`
and `continue RUN_DIRECTORY`, exit semantics, directory ownership, checkpoint
validation and unsupported arbitrary interruption recovery. Only seven implementation
paths changed; the repair changes the runner and its behavioral regression.

The [root prerequisite audit](15-root-prerequisite-audit.json) independently verifies
ticket 14 implementation/bookkeeping ancestry, 21 baseline source hashes, five
historical gate maps and 103 raw observations. [Ticket 14 completion](14-completion.md)
links earlier provenance. Historical verification does not establish ticket 15 gates.

The final [source identity](15-repair1-final-source-identity.json),
[check results](15-repair1-check-results.json), [observations](15-repair1-fixture-observations.json)
and [root audit](15-repair1-root-audit.json) establish repaired-source verification.
All 23 final source/test/guide/config hashes match the final commit and current bytes;
all ten final gates share that map and exit zero. All 123 consolidated scenarios
match their retained raw hashes/outcomes; all 1,242 files in the
[raw-file manifest](15-repair1-raw-artifact-hashes.json) independently match.
The [detailed root audit](15-repair1-root-observation-audit.json) verifies actual
checkpoint/input/evidence/request histories, consumed decisions, branch alignment,
state rejections and durable source invalidation.

## Criterion evidence

The [coverage map](15-coverage-map.md) maps existing milestone, promotion, dependency,
transaction, report, timeout and integrity coverage before adding continuation cases.
The final continuation file has 20 scenarios at the approved public CLI, external
scripted process, isolated real-Git and observable record/ref seam. Runtime QA waits
remain indefinite; fixture waits are bounded and owned processes are cleaned up.

| Acceptance criterion | Verified observable evidence |
| --- | --- |
| Persist safe planned QA checkpoint; clean stop/new process | `test_clean_qa_stop_continues_in_new_process_without_replaying_done_work` observes stop acknowledgement, owner exit 2/`stopped_at_qa`, an archived checkpoint and continuation under a new owner through final completion. Exact requests, inputs, evidence, gates and checkpoints are copied in the retained raw run trees. |
| Validate captured inputs, version, branches/candidate and evidence | Fifteen variants of `test_continuation_rejects_changed_checkpoint_without_overwriting_prior_state` reject changed plan/snapshot, record/type/malformed record, checkpoint/archive, request, gate output, fabricated consumption, baseline/candidate source, both refs and caller checkout. They assert prior bytes and refs remain unchanged and unique rejection diagnostics exist. Input hashing binds every plan/version change. Observation rewriting before stop is separately rejected. |
| Preserve Done/history; no assignment or approval replay | The two-group scenario preserves prior attempts, runs one baseline and exactly four implementations in order 03/01/04/02, rejects replay and consumes two distinct request-specific decisions. `test_repeated_stops_retain_previous_decisions_and_checkpoint_lineage` preserves the first archive/acceptance through another clean stop at M2. Root independently verifies raw decision hashes and next-worker alignment to the first promotion. |
| Serialize ownership; prevent duplicate continuation/promotion | A directory-inode POSIX lock covers run/continuation through execution and promotion. Active-owner continuation rejects with retained diagnosis; completed or arbitrarily interrupted runs cannot be continued. Accepted promotion retains the existing atomic expected-old two-ref transaction. No rejected continuation overwrites prior run/checkpoint/evidence or refs. |
| Demonstrate first-QA restart and next-group completion; exclude arbitrary crashes | Both successful renewed CLI scenarios reach exact final refs and `completed`/true only after final acceptance. The unsupported-interruption scenario rejects restart after fixture termination without a deliberate checkpoint. Installed console-script success and invalidation scenarios independently exercise the repaired wheel. Arbitrary mid-stage recovery remains explicitly excluded. |

After continuation, `test_continued_run_records_invalidation_of_earlier_verified_source`
also proves source mutation stops with the canonical durable gate marked
`passed: false`/`verification_status: invalidated`, unchanged dev and no consumed approval.

## Actual final checks

All Python used the documented reusable environment. Pinned mypy 1.19.1 and Ruff
0.14.10 were reverified under `/tmp/ticket12-tools`; the shared environment was not
modified. The [repair report](15-repair1-implementation-report.md) and
[actual command/output log](15-repair1-checks.log) retain precise commands, exits,
timings and source identities.

| Gate | Actual result |
| --- | --- |
| `python -m pytest -q --durations=20` | Exit 0: **544 passed in 910.17s**; wrapper 910.693s. |
| Strict `python -m mypy` | Exit 0. |
| `python -m ruff check ticket_harness tests examples` | Exit 0. |
| `python -m ruff format --check ticket_harness tests examples` | Exit 0. |
| Working, actual staged and committed original-baseline whitespace | All exit 0. Empty-index staging captures are explicitly historical and excluded from final gate consolidation. |
| Pinned-backend wheel, isolated target install, installed console script | All exit 0. All nine installed/wheel Python members match repaired source. |

The [installed observations](15-repair1-installed-observations.json),
[installed invalidation](15-repair1-installed-invalidation.json),
[package manifest](15-repair1-package-manifest.json) and retained
[wheel](15-repair1-package/ticket_harness-0.1.0-py3-none-any.whl) establish installed proof.
The installed script runs from `/tmp`, resolves the isolated installation, completes
two groups with stop/restart, rejects ownership/stale/replayed state, and separately
verifies durable post-restoration invalidation. Raw installed artifacts are retained.

Only `15-repair1-final-*` captures establish final gates. Initial 543-test results,
initial reviews and initial root audits remain historical. Red/green/focused runs
retain their actual identities; [original log bytes/hashes](15-log-originals.json)
preserve five whitespace-normalized historical display logs. Final raw artifacts
are unchanged. Initial sandbox DNS/staging failures were resolved through approved
scoped retries; no permission blocker remains.

## Independent reviews and repair

Initial fresh High [Spec](15-review-spec-initial.md) found zero findings.
Initial separate High [Standards](15-review-standards-initial.md) found STD15-01:
restored evidence dictionaries were detached from durable gate records. Unsafe
promotion stopped, but saved gates could incorrectly remain passing after source
invalidation. A fresh Medium repair reproduced that failure red, rebound restored
verification to canonical gates, passed green and renewed the complete suite and
all affected required gates. [Repair evidence](15-repair1-implementation-report.md)
retains that history.

Final fresh GPT-6.1 Sol High [Spec](15-review-spec.md), `/root/review_spec15_final`:
**0 blockers; 0 optional suggestions.** Independently audited the entire original
baseline-to-final diff, source/check/raw/installed evidence and prerequisite compatibility.

Final separately configured fresh GPT-6.1 Sol High
[Standards](15-review-standards.md), `/root/review_standards15_final`:
**0 blockers; 0 optional suggestions; STD15-01 resolved.** Independently audited the
whole diff and canonical gate associations; reproduced the public invalidation
regression, **1 passed in 2.76s**, exit 0. Neither final reviewer read the other axis's
reports or changed implementation. No executable change followed final verification.

## Completion boundary

All five criteria and required gates are verified at `d11f0bc`. Previous readiness
is `ready-for-agent`; dependency history remains unchanged. Ticket/header/criteria/
comment/index are reconciled in a separate bookkeeping commit, available from this
file's Git history. The QA handoff receives its own commit after bookkeeping.
No unchecked criterion or unresolved ticket 15 blocker remains.

Only the main checkout worktree exists; no active development harness run using
these approved inputs was identified outside retained fixture evidence. Approved
spec/proposal/milestone definitions remain unchanged. The unrelated unstaged tracker
edit is excluded and retains SHA-256
`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.

M1 required tickets 10–15 are verified complete; **M1 is not requested or accepted
for human QA**. The next handoff is preparation/waiting for M1 QA, not executable
ticket 16. No development QA request/run/candidate/gate/decision has been created
or inferred from scripted fixtures. M2 remains gated by explicit human acceptance.
QA sessions/corrections, background operation, independent progress, live backend,
runtime role-skill capture, OS role enforcement and final feature acceptance remain
later work. E1 ticket 25 retains its separate priority immediately after verified 24
and does not gate release acceptance. No push occurred.
