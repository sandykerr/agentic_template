# Bounded caller-index repair worker

Actor: `/root/m1_repair`, implementation/repair role. Configured GPT-6.1 Sol
Medium; advisory active context target 250K. Actual backend delivery, hard
enforcement and active-context telemetry are unavailable. Parent owns checkpoint
commit, independent Spec/Standards and cumulative review, tracker and QA records.
No further delegation, commits, tracker changes or acceptance by this worker.

Repair full key: `review-M1-architecture-01/standards-01/F1`. Starting HEAD is
`e2b0a260fa192a7b51edc5f4cc5692c6340444c2`. Fixed cumulative baseline remains
`1a623bad0b08241367948948b731b9e1f5114671`. Original reports, finding history,
reproduction/control and retained readability evidence remain unchanged. This
worker's implementation claim does not establish an independently fixed finding.

## Instructions and environment

Read AGENTS, GLOSSARY, ADR-0001/0002, current environment/testing/review-records
policies, the task handoff, approved spec/approval/M1 requirements, architecture
assessment/history/original Standards report, readability assessment and renewed
source/suite identities, and evidence cleanup/retention decisions. Applied
diagnosing-bugs, TDD (including examples/mocking guidance), and test-strategy.
The public CLI/scripted processes/real disposable Git seam is already approved;
no new module or private seam was requested or used.

The initial environment instructions referred to an absent micromamba prefix.
Parent prepared a temporary container fallback. Its proposed regression command
was interrupted before execution: no red log or residual test process existed.
The human then changed AGENTS and linked policies to checkout-local uv. Reread
these instructions before resuming and used `.venv/bin/python` for all executed
Python/test checks. Parent reports Python 3.12.15 and Git 2.43.7; current command
identities are in the worker manifest. Preserve the human's unrelated environment,
README, requirements and ignore-file changes; they are not this repair's output.
Parent also authored a bounded environment-isolation paragraph in
`docs/ticket-harness/agents.md` after executable-source freeze; that documentation
is separately attributed and does not change these worker source/test bytes.
Parent's original `starting.json` and `starting.patch` are retained, along with
its resumed instruction/source capture. The original starting Python field is
the fallback capture environment, not the interpreter used for executed tests.

## Red loop, ranked hypotheses and probes

First command:

```sh
.venv/bin/python -m pytest tests/test_transaction.py::test_inherited_caller_index_is_preserved_during_ticket_execution -q
```

`red-caller-index.log`: exit 1, one failed in 0.42s. The real CLI inherited the
absolute caller `.git/index`; the test observed different index bytes immediately
after CLI exit, before any observer Git could refresh its index. The caller had
distinct staged/unstaged/untracked content. No production bytes had changed from
e2b0a26. The exact initial test is retained by `starting.patch` applied to that
commit, and its full file SHA-256 is
`8329d8681309d1dc7db330e540182bffd1001f223defafc0c3c0d3de154d39aa`
in `starting.json`. This is the actual initial red identity, not the later
parameterized test. No deliberately broken fixture was used to force the red.
The historical retained clean/control pair supplies the unminimized predecessor;
the fresh `routing-observations/caller-index` and control rerun that clean pattern.

Ranked falsifiable hypotheses were shown before testing them:

1. Ordinary harness Git inherits the route despite `-C`; removing it at that
   process boundary should preserve the caller's index.
2. Agent/check processes inherit independently; isolating harness Git alone
   should still allow their Git commands to mutate the caller's index.
3. Worktree setup/source validation may refresh the inherited index before
   submission; changing only the staging operation would leave earlier mutation.

Initial shared environment repair made the first case green (exit 0, one passed
in 0.76s; `green-caller-index.log`). To distinguish hypothesis 2, deliberately
restored only `records.execute`'s previous ambient environment line, extended the
test with real agent and candidate-check `git add --all` writers, and ran again.
`red-external-processes.log`: exit 1, three failed/three passed in 4.09s, with
the agent/check failure assertions again on exact caller-index byte inequality.
At that intermediate source, all Git adapters already used the helper, while
`execute` still used `{**os.environ, "TICKET_HARNESS_STAGE": stage}`. The test
then had the Cartesian writer x rejection decorators shown in that log. This
intermediate execution is not claimed to be the original pre-repair source.
`intermediate-source-identities.json` provides explicitly derived reconstruction
hashes from those exact edits; it is not mislabeled as an original capture.
Removed two redundant combinations, including candidate-check staging after an
earlier Standards rejection that cannot reach the candidate, and restored the
process environment fix. Final four-case command: exit 0, four passed in 2.74s
(`green-external-processes.log`). No neighboring readability refactor or debug
instrumentation was added.

## Coverage map and scope

| Requirement/failure | Existing or additional coverage |
| --- | --- |
| Caller staged/worktree/HEAD preservation without ambient routing | `TicketCycleTests.test_one_ticket_passes_every_gate_and_status_reads_its_exact_revision`, `test_rejected_candidate_preserves_caller_index_and_file_bytes`, repair exhaustion/human-decision cases |
| Exact caller index bytes with inherited absolute route | New parametrized transaction test, harness success and Standards rejection; checks bytes before observer Git, then staged/unstaged/untracked/HEAD and integration outcome |
| Agent's Git inherits caller index independently | New agent writer case; scripted external implementation stages via Git before returning its report |
| Configured check's Git inherits caller index independently | New candidate-check writer case; scripted external check stages in candidate source |
| Foreign repository/worktree/common/object/config routing | Fresh public-CLI `observe-routing.py` observations; two independent real temporary repositories per case, exact caller/foreign index hashes plus HEAD/worktree and integration assertions |
| Intentional isolated clean merge configuration/object routing | Existing clean same-file development merge and conflicting-development cases, included in focused checks |
| Expected-old/alias ref transaction invariants and diagnostic trace | Existing CLI/transaction tests and selected development/QA concurrent alias tests using real Git tracing, included in focused checks |
| Repair/current source invalidation and canonical restored gates | Existing repair file and restored-source invalidation case, included in focused checks |

Eight routing observations passed: ordinary control, original clean caller-index
pattern, foreign GIT_DIR, GIT_WORK_TREE, GIT_COMMON_DIR, GIT_OBJECT_DIRECTORY,
GIT_CONFIG_COUNT with core.worktree, and GIT_NAMESPACE. `GIT_NAMESPACE` did not
redirect this current primitive workflow; it remains inherited. This is a bounded
observation, not universal namespace/platform coverage. Other local keys use the
same explicit policy; no exhaustive environment matrix is claimed. The active
numbered config entries become inactive when their count is removed.

## Ownership and process trace

The selected source/worktree owns each Git index. The caller's index remains
caller-owned; no saved/restored copy or rollback after mutation is introduced.
The fix prevents ambient routing before writes rather than restoring caller
state after an integrity rejection. `worktree_environment` is a pure operation
in the existing process module, already imported by Git. It creates a new mapping
per launch without mutating the parent's environment. Its set matches this Git's
`rev-parse --local-env-vars` repository-local list. Global configuration, identity,
PATH and diagnostic settings, including GIT_TRACE2_EVENT, remain inherited.

Every package process launch and relevant writers were traced:

| Boundary and callers | Writers/invariants and repair |
| --- | --- |
| `git.git`, reached by input validation, run setup/checks, ticket worktrees/capture/candidates, QA fresh/restore/promotion | Copied filtered environment selects target via `-C`. Worktree creation/hooks, submission add/commit, ticket merge, milestone merge initialization/hash-object, and source checks use this adapter. Git source validation can no longer refresh an inherited caller index. Hook descendants receive the selected Git environment. |
| `git._update_direct_branches` direct Popen, called by ticket and milestone promotion | Same filtered mapping before the interactive prepared/commit/abort transaction. Existing locks, direct-ref validation, expected-old checks, hook disabling and cleanup remain owned here and unchanged. |
| `records.execute` direct Popen, called only by run checking | Same filtered mapping plus TICKET_HARNESS_STAGE, so baseline/lightweight/candidate/milestone suite processes and implementation/repair/Spec/Standards assignments and descendants run against their selected cwd. Existing payload persistence, deadlines, cleanup, protected-file capture and gate result ownership are unchanged. |
| `git.require_clean_milestone_candidate` direct subprocess | Existing intentionally isolated bare merge comparison removes all inherited GIT_* keys, then supplies object directory/global/system/attribute overrides. Left unchanged: this is deliberate per-operation routing, independent of the ordinary copied-environment rule. Initialization and tree/object lookups surrounding it use the fixed normal adapter. |

No other package subprocess launch exists. Inputs/plans/agents/tickets/QA and
runner continue using these owners, not new process routes. State persistence
and restoration retain existing config, run/checkpoint/gate/request schemas.
`continue_run` restores its canonical checks and every later process observes
the same runtime environment rule; no environment mapping is persisted, no new
checkpoint key is introduced, and no completed work is replayed by the repair.
`_Run.validate_sources` retains canonical gate invalidation after external work;
prevention now keeps that later rejection from being the first caller protection.
GateFailure/OS/process diagnostics and run/ticket outcome recording are unchanged.

Four architecture trigger decisions at start and after implementation:

| Trigger | Start | Final | Reason |
| --- | --- | --- | --- |
| New lifecycle | No | No | Existing Git/process/attempt/run/review operations and sequencing retained. |
| New persistence/restoration path | No | No | New mapping exists only for a process launch; saved schemas and canonical restoration unchanged. |
| New shared mutable state | No | No | Helper returns a fresh dictionary; environment is never mutated. |
| Additional state writer | No | No | Existing Git/process writers are constrained to the selected source rather than adding writers. |

Existing owners remain correct under the approved preservation contract. Mandatory
M1 cumulative assessment still applies independently of these No decisions. A
future additional gate using `records.execute` receives the same routing rule;
a future direct subprocess writer must explicitly choose this rule or an owned
isolated override rather than inherit caller-local Git state. Saved gate identity,
source invalidation and report policy continue with their established owners.

## Checks and next authority

Worker focused/static command results are recorded in `worker-checks.json` and
their named logs. Final source hashes/changed-file patch and instruction hashes
are in `worker-source.json` and `worker-source.patch`. Parent's canonical full
suite/static results must identify the actual final source; earlier 559 passes
or these focused passes cannot satisfy that gate. No packaging or entry-point
change, installed behavior uncertainty or dependency change was introduced by
this worker, so no extra wheel/install campaign is selected for this repair.

The first focused run used the default `/tmp`: 15 failed/110 passed in 100.86s.
All failures were hook scenarios. A direct executable probe raised EACCES under
`/tmp`; `findmnt` confirmed `noexec`. The same chmod755 probe in the checkout's
owned `test-tmp` directory executed and exited its intentional 42. See
`hook-execution-diagnostic.json`. The source was not changed in response. The
required meaningful hook checks are repeated with explicit absolute TMPDIR on
the executable checkout filesystem, captured separately as
`focused-exec-tmp-pytest.log`/XML; the original failed run is not relabeled.
That repeat finished exit 0: **125 passed in 563.12s**, with no failures,
errors or skips. Worker mypy, Ruff lint, Ruff format and whitespace commands
all exited 0. Every source/test hash still matches `worker-source.json` and
the routing observations at completion; no source edits followed those checks.

Parent owns the scoped committed review input and fresh separate original Spec,
Standards and High cumulative Standards assessments. Finding remains open until
exact-source independent verification and the required disposition. M1 candidate
preparation/acceptance and M2 eligibility remain outside this worker's authority.
