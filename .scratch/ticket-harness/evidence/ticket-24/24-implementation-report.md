# Ticket 24 implementation evidence

Original whole-ticket baseline: `ed017ae0c2b96769f31c710cfb4ff4708989b446`.
Assignment: fresh GPT-6.1 Sol Medium implementation worker; <=250000 active-context target, backend enforcement and measured telemetry unavailable. Root owns independent fresh High Spec/Standards reviews, reconciliation and handoff. No runtime/development QA acceptance or publishing is authorized.

## Starting ownership and coverage map

`__main__.main -> runner.run/continue_run -> _Run.execute -> qa.review` currently coordinates milestone review. Run owns prepared inputs, baseline, milestone scheduling, check execution/report authority, canonical gates and invalidation. QA's procedural review owns candidate preparation, exact request, frozen evidence, decision observations, stop checkpoint and promotion. Public continue holds exclusive output ownership, calls QA checkpoint validation, then restores run-owned canonical verification references before resumed work. Git/process/protection/atomic primitives remain functions. Only QA writes review fields; run writes run lifecycle/scheduling fields. Run persistence serializes their existing shared durable record; no new state store or writer is intended.

| Contract/failure | Existing approved public CLI/scripted-process/isolated-Git coverage |
| --- | --- |
| Candidate, exact approval, both refs, later milestone bounds | `test_qa_promotion.test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision`; `test_milestones.test_two_group_plan_presents_tested_qa_without_starting_later_work` |
| Missing/unreadable/malformed/mismatched/stale/replayed decisions; waits, no repair | `test_qa_promotion.test_invalid_decisions_keep_waiting_without_repairs_or_authority_from_incidental_text`; `test_continuation.test_clean_qa_stop_continues_in_new_process_without_replaying_done_work` |
| Frozen evidence/source/ref rejection | QA acceptance mutation matrix; continuation protected identity matrix; transaction source mutation cases |
| Canonical post-restore invalidation | `test_continuation.test_continued_run_records_invalidation_of_earlier_verified_source` |
| Repeated stop lineage, prior decisions and Done assignments | `test_continuation.test_repeated_stops_retain_previous_decisions_and_checkpoint_lineage` |
| Preparation/regression/promotion errors, exact candidate, naming | `test_milestones` merge/conflict/regression/ref/source cases; QA mutation cases; full CLI/transaction suite |
| Genuine old producer compatibility | This ticket's `24-checkpoint/producer.json`, baseline hashes and stopped live archive; final-source continuation passed; source/archive audit retained |
| Review ownership | Substantive source review of operations/writers, not private-class tests |

Existing coverage exercises the unchanged behavior; no distinct missing failure identified at start. No implementation-prescriptive test will be added merely to require a class. TDD applies if a meaningful uncovered failure emerges. Focused four-file QA/continuation/milestone/transaction checks during development, then required final full suite, strict mypy, Ruff lint/format and both whitespace checks. Packaging is unchanged.

## Architecture trigger assessment

| Trigger | Start | Evidence/anticipated ownership |
| --- | --- | --- |
| New lifecycle | No | Existing preparation/wait/stop/restore/promotion lifecycle retained |
| New persistence/restoration path | No | Existing version1 envelope, validation, canonical gate restore retained |
| New shared mutable state | No | Existing record/config/gate references retained; review state consolidates existing locals |
| Additional writer | No | Existing QA review writes move to its owner; run retains verification/lifecycle writes |

Post-implementation assessment below records all four No. Any actual positive trigger requires broader fresh High assessment before integration. M1 cumulative assessment and human QA remain unperformed and root-owned.

## Genuine pre-refactor checkpoint

Before any runtime edits, `24-checkpoint/produce.py` invoked unchanged fixtures and real public CLI at the fixed baseline, observed `stop` exit 0 and foreground exit 2, and saved stopped record/checkpoint bytes. Both explicit cleanup and temporary-directory finalization were disabled, preserving `/tmp/ticket-harness-test-h3xlit3z` across the producer process. `producer.json` records CLI/foreground observations and all runtime/test source hashes; every hash independently matches `git show` at the baseline. `stopped-live.tar.gz` retains the complete live fixture before edits. These isolated scripted approvals do not confer development QA acceptance.

## Worker checkpoint

Implementation, genuine old-checkpoint continuation, ownership/coverage map, canonical packet and all required final-source checks are prepared/passing. Independent fresh Spec/Standards review, review history, criterion reconciliation and bookkeeping/handoff remain root-owned and pending. This worker submits implementation evidence; it does not declare ticket completion or M1 acceptance.

## Implemented ownership and local source trace

`_Run.execute` constructs one `MilestoneReview` with concrete existing durable record/config/output, milestone index and run-computed candidate/request artifact paths. `execute(checkpoint)` owns preparation/restored review and indefinite decision assessment, returning `ReviewOutcome.STOPPED` or `PROMOTED`. The run alone translates stopped to exit 2, schedules further milestones after promotion, and completes the feature. `continue_run` retains exclusive ownership and separate rejection capture; review-owned `restore_checkpoint` validates the existing envelope without modifying it. `_Run.execute` still restores canonical gates and invalidates the stopped marker before resumed work.

Review's private state keeps the tested candidate/source, expected feature/development inputs, exact request/digest, frozen evidence and last raw decision observation together. `_prepare`, `_await_decision`, `_stop_if_requested`, `_read_decision`, `_consider_decision`, `_require_current` and `_persist` own all existing review transitions and observations. Both freshly prepared and restored requests enter that same wait/approval/stop/promotion flow. Restoration retains the prior archived checkpoint among frozen identities. Stop refreshes evidence after validating prior frozen content, including later observations, then saves exactly the version1 envelope and lineage. Only exact APPROVED, equal request content and an unconsumed request enter promotion; runner validation and frozen evidence precede the expected-old atomic two-ref update. Rejected decisions stay observations and never consume ticket repairs. No saved schema key/value, output filename or naming rule was introduced.

`ReviewVerification` is a structural interface to existing run operations: stage observation, save, protected Git operation, check, source validation and JSON-safe verification export. It exposes neither `_Run`, scheduling, ticket operations nor the registry. It creates no new checker or forwarding callback collection. Review receives concrete data instead of recovering its configuration, record, index, trees or artifacts from an unrestricted run. Private shared durable dictionaries are retained under the spec's explicit allowance for existing record persistence; QA owns review field mutations, run owns lifecycle/check mutations. No public setters or record getters were added.

Unchanged collaborators inspected: CLI run/stop/continue/status dispatch and exit handling; input/plan preparation and immutable snapshots; ticket/attempt transitions and agent report authority; runner canonical gate writers, export/restore alias reconstruction and invalidation; protected Git operations; candidate preparation/validation and expected-old promotion; process/file protection and atomic writes. A plausible approval/request rule change stays within `MilestoneReview`, while a verification category or invalidation change stays within run-owned operations; the caller only interprets the explicit outcome. Exact public behavior remains covered by the existing four-file map and required full suite; tests were not added or changed.

## Final architecture trigger assessment

| Trigger | Final | Source reasoning |
| --- | --- | --- |
| New lifecycle | No | Class operations replace the existing procedural preparation/wait/stop/restore/promotion flow; no extra phase, scheduler or continuation kind |
| New persistence/restoration path | No | Existing version1 record/checkpoint/archive validation and writes moved to review operations; canonical gate reconstruction remains `_Run.restore_checks` |
| New shared mutable state | No | Existing run/config/milestone/gate references remain; request/evidence/decision locals became private review state without another exposed alias or store |
| Additional writer | No | Existing QA writes are localized in the review; run remains canonical verification/lifecycle writer and Git remains the expected-old primitive |

All four start/final observations are No, so no unconditional third ticket reviewer is required. The separate M1 cumulative checkpoint still requires actual feature-start provenance, all-package fresh High assessment and explicit human QA before readiness/acceptance; none is claimed here.

No actual inherited unresolved finding, missing prerequisite report, pending relevant repair revalidation or human-owned contract decision was identified. Root independently verified prerequisites 15/23 evidence and commit ancestry, and preserves prior full finding history. This worker neither disposes new review findings nor substitutes mechanical checks for independent assessment.

## Final verification and provenance

- Frozen source: [26 runtime/test/example/config identities](24-final-source.json), independently asserted before and after each check. [Tool identities](24-tool-identities.json) and [environment](24-environment.json) identify the capture/check utilities and reused pinned tool installation. No dependencies, packaging or entry points changed.
- Focused four-file run: **123 passed in 486.10s**, exit 0. [Exact command/environment/exit/wrapper timing](24-focused-check-results.json), [log](24-focused-check-0.log). Raw focused observations remain at `/tmp/ticket24-focused-raw`; the final retained archive includes these same scenarios on the same frozen source, avoiding a second committed copy of their artifacts.
- Required full suite: **544 passed in 515.90s**, exit 0 (wrapper 516.26s). [Six final command/exit records](24-final-check-results.json), [suite log](24-final-check-0.log), [strict mypy log](24-final-check-1.log), [Ruff lint](24-final-check-2.log), [Ruff format](24-final-check-3.log), [worktree whitespace](24-final-check-4.log), [fixed-baseline runtime/test/example whitespace](24-final-check-5.log). Every command exited0. Mypy reports 10 source files; Ruff reports 24 formatted files.
- Genuine baseline checkpoint: [producer](24-checkpoint/producer.json) 22 runtime/test hashes independently match `ed017ae`; [consumer](24-checkpoint/continuation-final.json) 22 hashes independently match the final 26 manifest. Actual new-process continuation completes with exit 0, one baseline, four unreplayed original-once assignments, two consumed matching decisions, exact feature/development refs and status equality. [Archive/source audit](24-checkpoint/audit.json) streamed 335 stopped/593 continued regular files and checked retained record/checkpoint bytes. Both complete live archives remain alongside their scripts, stdout/stderr and observations.
- Final suite capture contains **544 scenario observations and 10,446 regular files**, archived losslessly in `24-final-raw.tar.gz` (3,968,518 bytes, SHA256 `86a9ef39c941921ce71c12fbb065f436f5e027975b7b9d7ecccdfe1810c9516d`); [scenario index](24-observation-index.json), [every-file size/SHA256 manifest](24-raw-manifest.json) and [stream readback audit](24-capture-audit.json) retain actual CLI/status/Git/ref/history, inputs, artifacts, checkpoints and rejection observations before cleanup. Suite capture preserves observations/artifacts rather than complete live worktrees; the separate old-checkpoint archives preserve live fixture state. Synthetic fixture decisions confer no development QA acceptance.
- Local preparation found one Ruff import-order diagnostic, corrected before the final source freeze; initial strict mypy passed. Those exploratory tool outputs are not standalone retained logs or completion gates. No test failed or was added/changed. No runtime/test/example/config source bytes changed after freeze. Final prose/evidence reconciliation receives link/identity/whitespace checks without redundant runtime-suite replay.

[Canonical packet](24-review-packet.md) supplies shared contracts, full-ticket baseline, ownership/coverage, exact evidence, scope/limits and inherited finding context for root's separate fresh High axes. The commit containing this report is the implementation checkpoint; root will name its exact commit in original assessment envelopes. No independent ticket24 review exists yet and no new finding disposition is invented. Actual M1 cumulative assessment and human QA remain unperformed.
