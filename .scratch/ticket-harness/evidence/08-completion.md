# Ticket 08 completion evidence

Implemented only [08: Stop stalled assignments and check processes](../issues/08-stop-timed-out-process-trees.md).
Verified implementation: `fbfc088de61f50636ec2f8557fdf2e119976fc58`.

## Revisions and prerequisites

- Fixed starting review baseline: `3d78722ae2e0f53c40eb169234aebec50e2140fb`.
- Implementation checkpoint `fbfc088` was committed after checks and before separate fresh Spec and Standards reviews of the complete baseline-to-checkpoint diff. No fixes or runtime/test changes followed review.
- Files: `ticket_harness/{inputs,records,runner}.py`, `tests/test_timeouts.py`, and [public configuration/process/status documentation](../../../docs/ticket-harness.md#stage-timeouts-and-cleanup).
- Prerequisite 05 was verified from implementation `34a49b7`, bookkeeping `2a454df`, completed header/all six checked criteria, actual checks, separate independent reviews, [completion evidence](05-completion.md) and [saved observations](05-fixture-observations.json). Later 06 (`dc1018e`/`4ed073d`) and 07 (`83d361d`/`846abc4`) completion evidence supplied compatibility context. Their runtime regressions passed again in the final suite. Tickets 01/02's legacy readiness headers do not supersede their verified completion evidence.
- Starting worktree was clean. The skill relocation mentioned by the old handoff is already committed in baseline `3d78722`; there was no unrelated unstaged relocation to preserve. No active harness run using these feature requirements was found. All executed scenarios used copied disposable requirements. No push was performed.

## Acceptance evidence and coverage map

[27 actual timeout-test observations plus installed CLI smoke](08-fixture-observations.json) were captured during the required full-suite execution, without replaying the scenario matrix. They include exact attempt/revision/gate identities, diagnostics, parsed completed reports, partial stdout/stderr, configuration normalization, final Git integration, caller status, source SHA-256 manifest, the complete pytest result and static-check logs. Fixture repositories were removed after assertions; original temporary paths identify the execution and may no longer exist. Relevant durable records and process output are embedded in the committed JSON. The independent Spec reproduction is also embedded there.

| Criterion | Current implementation and observed coverage |
| --- | --- |
| Positive configurable timeouts for implementation, repair, both review roles, lightweight, baseline and candidate checks | `inputs.timeouts` validates all supplied stages before any worktree/process. Defaults: implementation/repair/baseline/candidate 1800s, Spec/Standards 900s, each lightweight check 300s. Overrides are finite positive integer/fractional seconds, at most 604800s to avoid platform pipe-wait overflow; types, shapes, unknown keys, nonfinite/overflow/unsafe ranges reject at attempt 0 with no gates. `invalid_timeout*`, `default_timeouts*`, and `timed_out_assignment*` verify normalization, independent allowances and every actual gate's category/seconds, including repairs. Existing command/role/report identities are unchanged. |
| Stop timed-out command and descendants; retain output and finish the stage | `records.execute` starts a fresh POSIX session/group, bounds input/output communication, sends group SIGKILL on timeout, bounds final drain/reap separately at five seconds each, and saves raw output bytes before integrity/repair handling. Controlled finite parent/child/grandchild processes ignore SIGTERM; Linux `/proc` observations verify they are absent or stopped zombies awaiting the system reaper. `worker_timeout*`, role/check timeout cases and `exited_worker*` preserve partial output and cleanup evidence. An exited leader with open descendant output handles remains subject to the deadline. |
| Reuse remaining repair allowance or block; no secondary loop | Worker, Spec, Standards, lightweight and candidate timeout cases each reject attempt 1 and pass a fresh attempt 2 with renewed checks/reviews and exact-candidate integration. Worker repair inherits uncommitted value/note contents; prior output/worktrees remain intact through subsequent stages. `timeout_exhaustion*` uses the default two repairs, distinct repair deadline and three fresh groups/worktrees/artifact names, then Blocked/incomplete on attempt 3 with integration unchanged. Existing 58 repair cases cover broader transition/allowance/invalid-report interactions. |
| Baseline/shared-environment failures stop without ticket repair churn | `baseline_timeout*` records environment failure, attempt 0, no ticket attempts and only the baseline gate. `unavailable_shared_executable*` removes a preflight-valid executable during worker execution: the affected check records an execution error and stops the run as environment on its first attempt, without another repair. Existing preflight, failed baseline and invalidated shared-baseline regressions also pass. |
| Status exposes stage, allowance, evidence and ticket/run outcome | Gates retain actual stage/attempt/revision, `timeout_category`, `timeout_seconds`, `timed_out`, cleanup group/signal/sent, exit code, assignment and output paths. Attempts retain exact failures/ranges; repair assignments receive this evidence through existing `check_results`/`repair_context`. `assert_observations` compares final run JSON, durable record and read-only status, including unchanged record bytes. Complete reports from timed-out processes remain raw evidence with `report_status: not-evaluated`; neither success nor human-decision claims override timeout, even when the leader exits 0. |
| Controlled worker/reviewer/check/child demonstrations | The 27 new CLI cases exercise all requested role/check differences, baseline and shared environment, positive validation, successful repair, default exhaustion, exited leaders, decisions and protected evidence. Role/check repaired gates bind to fresh submitted revisions, and candidate parents/tree/integration match verified source. Tests preserve caller HEAD, distinct staged/unstaged data, untracked work and approved source/snapshot bytes. `timeout_cannot_hide_evidence_tampering*` verifies restored earlier evidence, retained rejected contents and immediate stopping despite remaining repairs. All 421 prerequisite regressions pass at the current implementation. |

The agreed seam remains the public CLI with scripted external processes, isolated real temporary Git repositories and observable artifacts/Git outcomes. No parser internals or internal production mocks were used. Existing report validation, human decisions, optional suggestions and transaction coverage were reused rather than multiplied across every timeout permutation. New cases detect distinct deadline routing, cleanup, precedence or bounded-failure regressions.

All stall scripts are finite (20s), an external CLI watchdog is 60s, finalizers clean recorded groups, and termination assertions poll with a five-second observation budget rather than asserting tight elapsed times. Zombies count as stopped, never as executing children. The production contract uses inherited POSIX process groups and trusted commands; deliberate detachment into another session/group is not OS containment. Role enforcement, live Codex, scheduling/continuation and recovery remain later tickets.

## TDD and actual checks

All Python used `/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python` after reading environment guidance. `/tmp/ticket-harness-env/bin/mypy` and `ruff` were verified available. No runtime dependency or network/model call was added.

Red/green slices at the agreed seam: invalid timeout configuration initially gave only an unsupported-field diagnostic; worker stalls initially completed without timeout/cleanup evidence; an enormous finite allowance triggered platform wait overflow and left a running record. Input validation, bounded group execution, then safe numeric range validation made those regressions pass. Additional cases extend implemented behavior and verify compatibility without manufacturing failures in working paths.

| Actual command/check | Result |
| --- | --- |
| Reusable Python `-m pytest tests/test_timeouts.py -q` during development | 26 passed in 27.55s before the final integrity case/evidence-capture additions. |
| Reusable Python `-m pytest tests/test_timeouts.py tests/test_repairs.py -q` on final implementation | Exit 0: **85 passed in 143.50s** (27 timeout and 58 repair cases). |
| `TICKET_HARNESS_TEST_OBSERVATIONS=/tmp/ticket-harness-08/observations` with reusable Python `-m pytest -q --durations=20` | Exit 0: **448 passed in 432.71s**, including all 421 prerequisite cases. Tested staged source was committed unchanged as `fbfc088`; manifest hashes were verified against committed blobs. Full log is embedded in observations. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0 during development and final checks: strict mode, no issues in 7 source files. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 17 files already formatted. |
| `git diff --check`, staged whitespace, baseline-to-checkpoint whitespace | Exit 0. |
| Reusable Python `-m pip install --no-index --no-deps --no-build-isolation --target /tmp/ticket-harness-08-installed .` | Exit 0: wheel built and installed without fetching dependencies. |
| Installed CLI help/import path and `/tmp/ticket-harness-08/installed-smoke.py` | Exit 0 from `/tmp` with installed-only `PYTHONPATH`: actual installed package path verified; worker timeout/child cleanup, fresh repair, exact integration and status equality passed. |
| `/tmp/ticket-harness-08/collect-evidence.py fbfc088de61f50636ec2f8557fdf2e119976fc58` through reusable Python | Exit 0: collected the required execution's 27 actual cases and installed smoke; verified source hashes against committed blobs. No repeated scenario suite. |

Verbose temporary logs, patch/hash manifest, coverage plan and original reviewer reports remain under `/tmp/ticket-harness-08/`; committed evidence preserves the essential results after those temporary files expire. Bookkeeping/handoff are prose and evidence only; no runtime check was relabeled as testing a changed implementation.

## Independent reviews

Both reviews used fresh GPT-6.1 Sol contexts below the feature's 250K target, assessed the full committed `3d78722...fbfc088` diff, and received the coverage map, testing policy and test-strategy review guidance. Scripted fixture reviewers were not counted as implementation reviews. Standards also received the complete Fowler smell baseline and combined deep-module/Microsoft OOP design references, with repo standards taking precedence. No CODING_STANDARDS.md or CONTRIBUTING.md was found.

Spec: **0 blockers, 0 optional suggestions.** Independently reproduced ordinary worker completion with a surviving background child whose output was redirected to DEVNULL: cleanup killed the child, CLI completed, and status matched.

Standards: **0 blockers, 1 optional suggestion S1.** Stream captured pipe output into artifacts to reduce memory growth during verbose stages. This is retained as an optional reliability improvement; no output-size contract or demonstrated failure makes it a completion blocker. No fix commit was required. The earlier ticket-07 optional fixture-consolidation suggestion remains historical context, outside this ticket's required work.

Full review reports follow.

### Spec

Spec review — ticket 08

Reviewed the full committed diff from `3d78722ae2e0f53c40eb169234aebec50e2140fb` to `fbfc088de61f50636ec2f8557fdf2e119976fc58`, originating ticket, scoped spec, handoff, current contracts, coverage map and testing policy. No other implementation review was consulted.

(a) Missing or partial requirements: none found within ticket 08's scope. All seven timeout categories are positively validated before execution and recorded on gates. Timeout failures share the existing repair allowance; baseline and unavailable-environment failures stop the run without another repair. Status retains allowance, role/check, attempt/revision, outputs and resulting outcome.

(b) Unrequested behavior or scope creep: no blocking expansion found. Killing inherited background children after ordinary completion supports cleanup and integrity before subsequent gates. POSIX process-group dependence, numeric defaults and the finite upper bound are documented implementation choices. Dependency continuation, live Codex settings/skills and recovery remain explicitly outside this ticket.

(c) Incorrect implementations: no blocking findings. The spec requires, “On timeout, terminate the affected process and its descendants, collect available output, and record the failed stage” (`spec.md:208`). `records.py:115–160` creates a separate session, bounds communicate (including input/output), kills the inherited process group, bounds draining/reaping and retains bytes. Cleanup addresses an exited leader whose descendants retain output handles; a leader exit of zero cannot override `timed_out`. Deliberately detached groups remain outside the documented trusted-process contract. Completed reports retain validation and human-decision precedence; timed-out reports cannot authorize success or a decision. Existing repair, optional-finding, integrity and exact-candidate flows remain intact.

Verification: inspected the supplied final-suite log (448 passed in 432.71s) and public CLI/Git timeout coverage. Independently exercised successful worker completion with a surviving background child whose output was redirected to DEVNULL: the CLI completed, recorded group cleanup, status matched, and the child was absent. Evidence: `/tmp/ticket-harness-08/spec-normal-cleanup.json`; reproduction script alongside it. Repository/index remained unchanged.

Blocking findings: none. Optional suggestions: none.


### Standards

# Independent Standards review — ticket 08

Reviewed the complete committed diff `3d78722ae2e0f53c40eb169234aebec50e2140fb...fbfc088de61f50636ec2f8557fdf2e119976fc58` (five files). Worktree was clean. No repository/index changes were made.

**Blocking findings: none. Documented-standard violations: none identified.**

Validation stays in `inputs.py`, process lifecycle/artifacts in `records.py`, and timeout-category/repair decisions in `runner.py`. This follows the spec's “Cohesive module responsibilities” and combined design policy, plus `docs/harness-design.md`'s functional/object implementation guidance. The small cleanup helper owns actual shared behavior; no class framework or speculative extension seam is warranted. Existing role/report interfaces remain intact. Documentation records numeric defaults, POSIX ownership assumptions, cleanup bounds, and observable evidence.

Tests preserve `docs/agents/testing.md`'s approved CLI/scripted-process/real-Git seam. The role and check combinations exercise distinct stage routing and repair transitions; exited-leader/decision cases cover meaningful precedence differences. Existing fixture builders are reused, writable repositories remain isolated, child scripts are finite, an external watchdog bounds regressions, and finalizers clean recorded process groups. The coverage map explains new cases and reused compatibility coverage. No unnecessary Cartesian matrix or blocking fixture-ownership/reliability issue was identified.

**Optional suggestion S1 — output memory use:** `ticket_harness/records.py:119–142` replaces file streaming with `stdout=subprocess.PIPE`, `stderr=subprocess.PIPE`, and `captured_out, captured_err = process.communicate(...)`. Captured output now occupies harness memory until the stage completes; memory consumption grows with log volume, including broader suites with 1800-second defaults. Consider streaming pipe chunks into artifact files while preserving deadline/EOF semantics. This is a reliability improvement, not a documented-standard violation or integration blocker: no output-size contract or demonstrated failure was supplied.

**Fowler baseline:** no actionable introduced smell supported by these hunks. In particular, lifecycle cleanup is localized, the timeout dictionary represents configuration transport, and the single stage-category branch does not establish Repeated Switches.

Verification: inspected retained `pytest.log` (`448 passed in 432.71s`) and supplied coverage/check provenance. No additional runtime checks were necessary to resolve the Standards review. Required static/install checks were reported by the implementation agent; this review does not claim an independent rerun.


All six criteria are verified at `fbfc088`; none remain unchecked. No required unresolved items remain. Optional S1 remains recorded. Bookkeeping follows verified implementation and separate reviews; the next handoff is generated after its separate commit.
