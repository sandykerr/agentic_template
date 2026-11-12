# Ticket 23 implementation report

Fixed original baseline: `851a855889b1ec99ae78ce415da1d66a3cf06687`.
Fresh GPT-6.1 Sol Medium assignment, no override, advisory <=250000 active-context tokens; backend delivery/enforcement and measured active-context telemetry unavailable. Applying implement-with-checkboxes, OOP, codebase-design, test-strategy and the approved behavioral seam. Root owns separate reviews, completion bookkeeping and handoff; no subagents launched by this worker.

## Eligibility and preparation

Approved oop-v2/review-process-1; M1 10–24 is earliest required unaccepted milestone. Ticket23 ready-for-agent, unclaimed, prerequisites15/21/22 completed (5/7/7 checked criteria). Their completion evidence retains required checks and separate reviews. Root independently verified all six declared retained implementation/bookkeeping ancestors; historical21 report IDs retain history-repair provenance. No next milestone, runtime harness orchestration, development QA acceptance, promotion or push authorized. Unrelated dirty tracker/guidance/archive changes remain preserved.

## Coverage map recorded before executable changes

Existing public CLI/scripted-process/isolated Git seam suffices; no new test or private-class assertion planned. Ownership is assessed by source inspection.

| Criteria | Existing coverage |
| --- | --- |
| 1 initialization/continuation interface | run/continue CLI cases in test_cli and test_continuation; source ownership trace |
| 2 branch/base/protection/baseline/diagnostics | test_cli successful full cycle/status and failed baseline; test_preflight invalid inputs/environment; test_transaction integrity/branch movement |
| 3 ticket coordination/fail-fast/milestone gates | test_dependencies scheduling/fixed bases/blocked dependents; test_milestones first-group and later-work exclusion; test_qa_promotion exact acceptance |
| 4 non-replay/repeated continuation/rejections | test_continuation new-process/repeated stops, active owner, checkpoint mutation matrix; genuine baseline-produced live fixture continued under final source |
| 5 saved verification/canonical restoration | test_continuation continued_run_records_invalidation_of_earlier_verified_source plus repeated stops; test_qa_promotion source invalidation; source tracing canonical gate aliases |
| 6 schemas/names/integrity/atomic persistence | all existing CLI/transaction/QA/continuation coverage and genuine old checkpoint |
| 7 review/history/checkpoints | this report and canonical packet; independent root-owned axes and immutable reports remain pending |

Focused development selection: test_cli, test_preflight, test_dependencies, test_milestones, test_continuation and test_qa_promotion. Required final gate: full pytest, strict mypy, Ruff lint/format, both whitespace checks. Packaging unchanged, no installed CLI replay warranted.

## Architecture triggers at start

All four **No**: lifecycle already exists in runner._run and QA; this slice localizes existing start/continue responsibility. Existing qa._persist/restore path, version1 and fields stay unchanged. Existing record/config/gate aliases remain; no new shared mutable registry. Existing run and QA writers move behind run-owned operations without adding a writer. Reassess final source, particularly restored gate canonicalization and QA's export consumer. No positive trigger currently requires broader per-ticket assessment; actual M1 all-package cumulative assessment and human QA remain separate and unperformed.

## Genuine pre-refactor checkpoint

`23-checkpoint/produce.py` used unchanged public fixtures and actual CLI before executable edits. `producer.json` records baseline HEAD, all runtime/test hashes, stopped record, CLI and foreground exits. Both explicit cleanup and TemporaryDirectory finalization were disabled. `stopped-live.tar.gz` retains the genuine Git repository/worktrees at original absolute paths; `stopped-run.json` and `stopped-checkpoint.json` preserve original bytes. Synthetic approvals in this isolated fixture confer no development QA acceptance.

## Ownership and changed/unchanged collaborators

`__main__.main -> runner.run/continue_run -> _Run.execute` is now the complete caller flow. Public run retains fresh output creation and exclusive ownership. Public continue retains ownership, validated `qa.restore`, rejection capture and ValueError behavior. Neither caller sets configuration, protection paths, milestone position or lifecycle fields. `_Run.execute` owns setup, prepared-input consumption/conversion, branch/base validation, baseline establishment, milestone scheduling, continuation restoration, final outcomes and stage-based failure classification. Its constructor owns the existing output subdirectories and initial/restored record. There is one lifecycle operation, with a configuration path for fresh execution or the already validated checkpoint supplied to construction. The local checkpoint is consumed after resumed QA so later groups execute normally.

Initialization still calls `inputs.load` once, projecting its complete prepared result rather than enriching raw settings. Config/record aliases retain previous sharing; no copy/immutability contract was added. `tickets.initialize/unlock/next_ready` remain readiness functions. `_TicketExecution.execute` retains fixed-base/repair/integration policy; `_Attempt` alone edits attempt lifecycle transitions and observations. `_Run` passes only concrete ticket data and `_TicketVerification`'s scoped operations, then records successful integration/unlocks dependents. Existing fail-fast exceptions stop the run; independent-after-block policy29 remains out of scope. Run failure finalization's current ticket Blocked observation remains as before and does not create an extra attempt transition.

Run save uses unchanged atomic `records.write_json`. `check` remains the writer of canonical gates and registry entries; `validate_sources` marks those canonical gates invalidated. `reject_checks` retires rejected ticket references without erasing gate history. `_Run.export_checks` owns conversion from the internal tuple registry to existing checkpoint lists with source strings. QA receives those finished values and persists them unchanged. Export retains gate aliases during the synchronous atomic persistence operation, exactly like the previous inline conversion; it promises checkpoint shape, not independently mutable snapshots. Restore resolves each decoded gate against `record['gates']` and reconstructs source Paths, so later invalidation changes the durable canonical gate, including subsequent checkpoint exports/restorations.

QA remains callable and retains candidate/request/evidence/decision/checkpoint rules, stage observations and expected-old promotion. That ownership migration is ticket24, explicitly excluded here. QA owns checkpoint envelope persistence and validates external durable identities; its inspection of checkpoint-shaped verified entries during restore is the public saved shape, not the runner's private registry layout. `agents.report` returns validated observations without record mutation; Git/process/filesystem/protection/atomic primitives remain functions. CLI status still only reads run.json.

Inspected changed runner.py and qa.py; unchanged __main__.py, input preparation/plan validation, ticket/attempt transitions, agent report/process records, Git primitives, and relevant CLI assertions. Cross-module review must follow all these collaborators; omitted work is new milestone ownership24, independent scheduling29, runtime33/34, orchestration, packaging, development QA/promotion and unrelated dirty edits. A plausible new run initialization/continuation invariant now changes `_Run.execute` rather than public callers. A new check category changes run-owned checking plus actual category consumers; checkpoint export stays localized in `_Run`, with QA envelope unchanged unless the saved contract deliberately changes.

## Architecture triggers after implementation

| Trigger | Start | Final | Evidence |
| --- | --- | --- | --- |
| New lifecycle | No | No | Existing `_run` sequence moved into run operation; same one start or deliberate continuation and QA lifecycle |
| Persistence/restoration path | No | No | Existing save/qa._persist/qa.restore path and version1 fields retained; inline registry conversion relocated to owner |
| Shared mutable state | No | No | Existing run/config/gate references retained, private checkpoint holds the already existing input only; no independent state store |
| Additional writer | No | No | Removes orchestration writer; same run/ticket/attempt/QA writers and failure observations retained |

No triggered third per-ticket assessment required. Separate whole-ticket axes remain pending with root. Real M1 cumulative assessment needs feature-start provenance, every package file and fresh High Standards before eventual QA readiness; it has not happened here.

## Resumed worker and retained interrupted evidence

The original worker turn was interrupted by the user before either pytest invocation completed. A fresh GPT-6.1 Sol Medium worker resumed the same assignment/source without executable edits; the fixed original baseline remains unchanged. On resume neither pytest process remained. The prior corrected full-suite log and focused six-file log lack summaries/exit results, so neither supplies a passing gate. Both logs and the interrupted raw capture tree are preserved losslessly under `23-interrupted/`, with `interruption.json` declaring that limit. The full required suite was restarted once against the frozen final hashes with the corrected capture-plugin import path. The interrupted focused run was not replayed separately because the required full suite includes its scenarios. Initial capture import exit 3 and earlier package-install failure remain preserved rather than overwritten.

## Continuation configuration-path compatibility trace

Local preparation traced the removed wrapper expression `Path(checkpoint['record']['inputs']['configuration']['source'])`. The old continuation `_run` did not consume that path. `inputs.load` always produces the `configuration` snapshot with a resolved string source, artifact and digest; `qa._persist` saves that complete record. `qa.restore` first checks the run marker/checkpoint digest, exact embedded-record equality and archived checkpoint digest, then calls `inputs.require_approved`, which constructs `Path(snapshot['source'])` and verifies both original and artifact bytes for every snapshot. It then verifies frozen evidence, verified trees and branch identities. Thus the removed expression duplicates source-path conversion for any present configuration entry and adds nothing for genuine persisted deliberate checkpoints. The genuine pre-edit continuation and protected-identity mutation matrix are the governing compatibility observations.

Limit: `require_approved` iterates existing entries; it is not a complete mandatory-key/schema validator. A wholly re-authored self-consistent envelope that removes `configuration` and recomputes run/checkpoint/archive identities could differ at the old dead lookup. No claim of exhaustive hand-authored-envelope validation or checkpoint authenticity is made. This refactor does not introduce such a validator; the approved scope preserves genuinely persisted checkpoints and existing protected-identity rejections. This records source reasoning and an evidence boundary, not a human risk waiver or an assumption excluding any valid configuration generated by the existing producer.

## Final verification and retained observations

- Full final-source suite: **544 passed in 706.22s**, exit 0 (`23-final-suite-result.json`; wrapper 706.58s). The runner asserted all 26 frozen identities before and after execution. Command: absolute reusable Python `-m pytest -q --durations=20 -p capture23`, with `PYTHONPATH=tests:/tmp/ticket23-tools:.scratch/ticket-harness/evidence/23-tools` and raw destination `/tmp/ticket23-final-raw`.
- Strict configured mypy: success, 10 source files; Ruff lint: all checks passed; Ruff format: 24 files already formatted; worktree whitespace and fixed-baseline runtime/test/example whitespace: exit 0. Exact commands/exits/timings are in `23-final-check-results.json`. Initial index0 capture-import exit 3 remains a failed pre-collection attempt; corrected full-suite result alone supplies the suite completion gate. Pinned mypy 1.19.1 / Ruff 0.14.10 were installed only in `/tmp/ticket23-tools`; original failed and successful install logs retained.
- Final raw capture: 544 scenario observations, 10,446 regular files, 3,977,366-byte compressed lossless archive. Every regular archive member was streamed and matched to recorded byte size/SHA256 (`23-capture-audit.json`); archive SHA256 `ef32b28a2544c0401cdedadec5c927d0581bf121a32697f97d1201ac36503dba`. The scenario index links each case to CLI/status/Git/ref/history and artifact observations. These suite captures preserve artifacts/observations, not complete live worktrees. Genuine producer/consumer archives separately retain live Git/worktree state; their audit checked 335 / 593 files respectively and source provenance.
- No runtime, test, configuration, packaging or dependency bytes changed after final-source freeze. No tests were added/changed. Prose/evidence finalization receives document/link/identity checks; no redundant suite replay. Root-owned independent reviews, criterion reconciliation and ticket bookkeeping remain pending at this worker checkpoint.
