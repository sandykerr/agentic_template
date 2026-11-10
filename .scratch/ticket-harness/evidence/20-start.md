# Ticket 20 implementation entry

Fixed starting HEAD: `0d79d016907a03ce39d33c749523a8700e4233a4`.
Working tree was clean. Authorized scope: ticket 20 only, oop-v2 / review-process-1.
Prerequisite 05/06/19 completion and 19 assessment read; root independently checked
all implementation/bookkeeping ancestors. No unresolved actual finding remains.
No active harness process using these requirements was observed; only disposable
fixture runs are authorized here. Historical/frozen evidence is preserved.

Using implement-with-checkboxes, OOP, codebase-design, test-strategy and TDD guidance.
Existing approved seam is public CLI, scripted processes, isolated real Git and
record/ref observations. No new test seam is proposed.

## Start ownership and triggers

`ticket_harness/tickets.py:execute` owns the bounded loop and directly initializes,
submits, rejects and completes attempt dictionaries. `runner.py:_Run.check` writes
handoffs into `record['attempts'][-1]` and current ticket; `agents.py:report` writes
canonical report status/content/diagnostics. These are the migrated writers.
The attempt operation will receive only its history/current-ticket record and
gate list, never unrestricted runner access. Ticket execution retains repair policy,
original base, worktree carry and history construction (ticket 21 is excluded).
Run keeps execution, verification and outer Blocked/failure classification (23
excluded). Parsing remains a pure transformation. QA/checkpoint ownership (24)
and input preparation (22) remain unchanged.

| Trigger | Start assessment/source reasoning |
| --- | --- |
| New lifecycle | No: existing Running/Verifying/Rejected/Done attempt lifecycle only; `tickets.execute`, documented records. |
| New persistence/restoration path | No: `execution.save` atomic writes and `qa.restore` version-1 checkpoint remain; existing JSON only. |
| New shared mutable state | No: existing history/ticket/gate dictionaries remain canonical, wrapped by their new approved owner; no new state shared across assignments. |
| Additional writer | No: existing lifecycle and handoff writers migrate to one owner; parsing loses canonical write authority, runner remains sole gate writer. |

No trigger requires a third assessment at entry. Independent ticket Spec/Standards
remain mandatory and actual M1 cumulative assessment remains unperformed.

## Coverage selection before changes

| Criteria | Existing public behavioral coverage |
| --- | --- |
| 1 lifecycle/revisions/files/ranges | `test_repairs`: failed check renewal, invalid worker pre-submission carry, exhaustion ranges, final default repair; `test_dependencies`: multi-ticket ordered history. |
| 2 runner ownership/failure precedence | `test_reports`: invalid/ambiguous/deep reports, complete failed-exit reports, diagnostics; `test_transaction`: protected inputs and source invalidation; `test_timeouts`. Ownership requires actual-source review. |
| 3 validated handoff | `test_human_decisions`: three roles × initial/repair × exits 0/7, exact handoff in both locations and immediate stop; `test_repairs`: decision before capture. |
| 4 bounded distinct failures | `test_human_decisions`: malformed/optional decisions; `test_optional_suggestions`; `test_repairs`: report/process allowance; `test_timeouts`. |
| 5 compatibility/persistence | Existing CLI/status, caller preservation and integrity tests, dependency history, `test_continuation` and genuine baseline checkpoint described below. |
| 6 encapsulation | Actual-source cross-module independent reviews; no private shape tests. |
| 7 review history | Root owns fresh independent reviews, records and bookkeeping after implementation commit. |

No missing behavior identified before refactoring; reuse existing coverage without
manufacturing a red test or adding implementation-coupled assertions.

## Genuine checkpoint

[Producer](20-checkpoint/produce.py) ran before any runtime edits with the baseline
Python files. [Identity and CLI observations](20-checkpoint/producer.json),
[log](20-checkpoint/produce.log), [stopped run](20-checkpoint/stopped-run.json),
[checkpoint](20-checkpoint/stopped-checkpoint.json) retain producer source hashes,
actual foreground exit 2, stop acknowledgement and stopped_at_qa outcome.
The live disposable repository/worktrees remain at the producer's recorded /tmp
home for final-source continuation; source/artifact archives will preserve both
observations. No real feature QA request or acceptance is created.

Worker assignment requested GPT-6.1 Sol Medium, advisory <=250000 active-context
tokens. Backend setting enforcement, delivered model identity and measured active
context telemetry are unavailable to this worker; request configuration is not proof.
