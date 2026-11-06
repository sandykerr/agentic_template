# Ticket 09 completion evidence

Implemented only [09: Execute verified dependencies in a stable order](../issues/09-execute-dependencies-sequentially.md).
Verified implementation: `7f4eac025cfccd0912f25e3bdd602c1e2b3e516f`.

## Starting state, prerequisite and scope

- Fixed original review baseline: `be2244f10bd9231e7408e9939e11ca8b9723e5a2`, captured before edits. The initial worktree was clean. Historical skill relocation `3d78722` was already committed; no unrelated edits were staged or changed.
- Verified prerequisite 02 from implementation `b11fd20`, bookkeeping `1f7a199`, all five checked criteria, completion comment/index, [completion evidence](02-completion.md) and [actual observations](02-fixture-observations.json). Its legacy readiness header does not negate verified completion. Existing 03–08 contracts were read and preserved; the final full suite includes their regression coverage.
- No active harness run using these approved feature inputs was found. The target repository worktree list contained only this main checkout before implementation/bookkeeping; fixtures use isolated temporary target repositories and their own requirements. Approved inputs were never modified during a run.
- The implementation checkpoint was committed **after checks and before independent reviews**. Both reviewers used the original baseline for the complete four-file diff: `ticket_harness/inputs.py`, `ticket_harness/runner.py`, `tests/test_dependencies.py`, and [public contracts](../../../docs/ticket-harness.md). No fixes or implementation changes followed review.
- The sandbox exposed `.git` read-only. Required local staging/commit operations used approved filesystem escalation; automatic review accepted the operations. No push occurred.

## Contract and criterion evidence

`selected_tickets` is an additive explicit array of paths, defaulting to `[ticket]`, including the primary `ticket` and forming a subset of the context bundle `tickets`. Every selection must be agent-ready. A selected prerequisite executes in this run; an unselected prerequisite requires validated current-source, integrated external Done evidence. Multi-ticket completion records and legacy single-ticket records are supported. Context alone never selects work.

[Saved final-suite CLI/Git observations](09-fixture-observations.json) retain **21 dependency scenarios** and the installed CLI graph. They include actual commands/exits, source hashes, exact run records, role launches, observed worker HEAD/base/integration revisions and ticket states, Git history, output text, report/gate identities, and run/status equality. Disposable repositories are removed by fixture cleanup; committed observations preserve the assertions' observed data and original diagnostic paths. The retained check root is `/tmp/ticket09-checks/`.

| Acceptance criterion (unchanged wording) | Current-revision evidence |
| --- | --- |
| Select ready agent-eligible tickets with a documented stable ordering and at most one active implementation ticket. | `test_dependency_chain_and_independent_work_use_verified_integration_in_stable_order` submits paths in order 04,02,03,01 with primary 02, then observes worker order **01,03,04,02**. The scheduler selects the lowest numeric ready ID, independently of input order. Actual role start/end events alternate, every role is a fresh process, and an exclusive process lock detects overlap. The graph includes both human-ready and agent-ready unselected context; neither launches. Eight selection cases plus whole-bundle cycle/unavailable-unused-check cases reject before gates/worktrees/ref movement; existing preflight coverage remains intact. |
| Run the broader starting baseline once for the run, while retaining per-ticket lightweight checks and per-candidate broader checks. | The principal graph records exactly **one baseline at attempt 0** and four sets of implementation, referenced lightweight check, Spec, Standards, and exact-candidate suite gates. Ticket 03 uses a different named check subset. The repair case repeats each affected ticket's gates with fresh submissions and both reviewers while retaining the single run baseline. Baseline failure launches no agent and consumes no repair attempt. |
| Base each new implementation worktree on the current verified integration revision. | Actual worker-launch Git HEAD, integration tip and assignment base all equal the prior verified candidate, including the independent 03 work before 04. Each candidate's parents are the expected current tip and its reviewed submission; its tree equals that submission, and cumulative delivered source files remain in later trees. The final branch equals the last tested candidate. Repairs preserve each ticket's fixed base while starting from its rejected source and carrying current work into a fresh worktree. |
| Unlock a dependent only when all prerequisites are Done in this run's integration state. | The graph contains chain **01 → 04 → 02** and independent 03; 02 depends on **both 03 and 04**. Launch snapshots show 02/04 initially Pending, 04 Ready only after 01 Done, and 02 still Pending before 04 completes. Promotion precedes Done/unlocking. Decision/integrity stops retain 02 Pending and preserve earlier 01 Done. Multi-ticket external completion unlocks only an explicitly selected follow-up; legacy completion with normalized non-padded ID remains valid. Missing external evidence and malformed snapshots reject before new execution. |
| Report the observed state and integrated revision of every selected ticket and return success only when all selected work is Done. | `tickets` maps all four selected IDs to Done and their exact submitted/candidate/Done revisions; `selected_tickets` is canonical numeric order. `integration_revision` is the last verified promoted tip. Global attempts/gates/operations carry ticket identities and exact gate ranges; shared baseline uses null. `ticket` mirrors the active/latest entry for compatibility. All selected Done yields exit 0/completed. Partial-success decision, integrity and external-ref scenarios yield exit 1/incomplete with preserved Done/Blocked/Ready/Pending observations. Every captured CLI output matches durable record bytes; explicit status comparisons match final run output. |
| Demonstrate a dependency chain and independent ready tickets using scripted agents and real Git repositories. | All 21 scenarios use the public CLI, scripted external processes and isolated real repositories through shared `TicketFixture`. Workers make meaningful cumulative ticket-specific files. Saved launch/revision/history/output observations and asserted source trees/parents demonstrate delivery and integration. The installed wheel repeats the principal four-ticket graph from `/tmp` using only the installed package path and executable. |

Earlier evidence remains protected across tickets and repairs. Representative tests delete an earlier review output, replace it with a directory, delete it from a submission hook, and mutate an earlier review source. Harness-owned output is restored with rejected content retained; earlier source approval is invalidated; the run stops without launching more work or erasing the earlier Done revision. Repair tests prove separate attempt counters, unique artifact/worktree/operation names, current rejected work preservation, exact per-ticket gate ranges and no transfer of another ticket's findings or rejected revisions. An external branch update during a later candidate suite is preserved by failed compare-and-swap promotion.

This slice stops at the first blocked ticket. Continuing unrelated ready work is ticket 10. Role/design-skill delivery, live Codex profiles, OS access enforcement, concurrency and interrupted-run recovery remain deferred. No public-contract decision remains unresolved for ticket 09.

## Coverage selection and TDD

Approved seam: CLI/scripted external agents/real Git/report outcomes, as established in the testing policy. Existing `test_preflight.py` covers full-bundle normalization/eligibility/graph/configuration/external evidence; `test_cli.py` covers the exact cycle/status/caller work; transaction, repairs, reports, decisions, optional-suggestion and timeout files cover their respective independent invariants. The new graph scenario combines six-criterion evidence; further cases target distinct selection, multi-ticket repair, earlier-evidence integrity, external-completion, baseline and CAS failure risks without replaying the old role/report/timeout matrices. Repositories remain isolated while fixture construction is reused.

TDD tracer slices demonstrated actual red results before their implementation: unsupported `selected_tickets` prevented the graph; single-entry completion parsing failed the multi-ticket follow-up; a canonical-key check rejected a previously valid non-padded legacy ID; malformed external `inputs` caused a preflight crash rather than durable invalid-input output. Each was implemented and verified before proceeding. The malformed-input test is retained. Already working repair/protection behavior received compatibility coverage without manufacturing artificial failures.

The first full-suite run was interrupted (exit 130) after the final malformed-input regression was discovered. Its log/observations are under `/tmp/ticket09-checks/superseded/` and are **not** completion evidence. The full suite and required checks below were renewed for the final source.

## Actual checks and source identity

All Python used `/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python` after reading environment guidance. Existing `/tmp/ticket-harness-env/bin/mypy` and `ruff` were verified available. No dependency/environment changes were made. [Retained check output](09-checks.log) and saved observations preserve the commands, results and final source hashes. The four committed file hashes were independently compared with the check manifests by the parent and both reviewers; they match `7f4eac0` exactly.

| Actual command (from repository root unless noted) | Result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **469 passed in 370.27s**, comprising all 448 existing tests and 21 new cases. Required final run captured the dependency observations without replaying a separate full fixture matrix. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0: strict mode, no issues in 7 source files. Also passed during implementation. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 18 files formatted. |
| `git diff --check`; `git diff --cached --check` before checkpoint; committed diff whitespace review | Exit 0. |
| Reusable Python `-m pip wheel --no-deps --no-build-isolation --wheel-dir /tmp/ticket09-checks/wheels .` | Exit 0: wheel SHA-256 `5a646dd2aa812b22daf84c0d0b171f4a47b9aa0282936e17602e9af377975b84`. |
| Reusable Python `-m pip install --no-deps --no-index --target /tmp/ticket09-checks/installed-final /tmp/ticket09-checks/wheels/ticket_harness-0.1.0-py3-none-any.whl` | Exit 0. Changed installed runtime files match final tested source hashes. |
| Reusable Python `/tmp/ticket09-checks/installed_smoke.py` | Exit 0: installed `--help`, four-ticket graph and exact matching status from `/tmp`, with installed-only `PYTHONPATH`. Actual installed CLI commands are saved in the observations. |
| Focused dependency/preflight/repair checks during development | Passed at their stated development sources; the final full suite supersedes those earlier-source results. Final malformed-snapshot focused case passed before the renewed suite. |

## Standards review

Fresh independent `/root/review_standards_09`, GPT-6.1 Sol, reviewed the entire original-baseline diff at `7f4eac0`:

> Standards review passed with no blocking findings or optional suggestions.
>
> Input normalization cohesively owns selection and completion evidence; lifecycle ownership retains scheduling, ticket-local attempts, verification and promotion, consistent with the Python design policy. The existing functional/closure structure does not require a class hierarchy or speculative seams. Tests reuse isolated TicketFixture setup at the approved CLI/scripted-process/real-Git seam; graph assertions and parameterizations cover distinct risks without an unnecessary matrix or material reliability concern. Documentation matches configuration and records.

The reviewer inspected the diff, surrounding implementation, all supplied standards sources, coverage map, test fixture ownership, source-hash evidence and retained passing checks; ran committed-diff whitespace validation and confirmed the clean worktree. Runtime tests were not repeated. Sources included AGENTS, environment/domain/testing/tracker guidance, glossary/ADR-0001, harness design/public contracts, pyproject, both combined design references and the complete Fowler smell baseline. No CODING_STANDARDS.md or CONTRIBUTING.md exists. Tool-enforced checks stayed separate from design findings.

## Spec review

Separate fresh `/root/review_spec_09`, GPT-6.1 Sol, reviewed the same complete original-baseline diff at `7f4eac0`:

> No findings: no missing or partial scoped requirements, scope creep, or incorrectly implemented requirements identified. No blocking findings or optional suggestions.
>
> All six ticket criteria are satisfied, including independent work, dependency chains, current integration bases, one shared baseline, per-ticket checks and reviews, unlocking after promotion and Done, and complete selected-ticket outcomes. Repairs retain local identities/fixed baselines; earlier approvals are excluded from assignments while history remains durable. Stopping at the first blocked ticket matches ticket 09; continuation is ticket 10.

The reviewer inspected the ticket/scoped spec, compatibility instructions, implementation/docs/tests, supporting Git/report contracts, testing policy, coverage map and retained evidence; verified the four source hashes and clean worktree. Independent actual command:

```bash
/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python -m pytest -q -p no:cacheprovider tests/test_dependencies.py -k 'dependency_chain_and_independent_work or repairs_keep_ticket_local or malformed_external_snapshot'
```

Exit 0: **3 passed, 18 deselected in 11.39s**. Output is retained in the review tool transcript; no separate runtime log was created.

Standards: **0 blockers, 0 optional suggestions**. Spec: **0 blockers, 0 optional suggestions**. No implementation changes followed the passing reviews. Earlier optional streaming-output advice from ticket 08 remains outside this slice; it is not a ticket-09 blocker.

## Completion reconciliation

All six original criteria are verified at `7f4eac0`; all required checks and both separate reviews passed before bookkeeping. The ticket's header is completed, all six markers are checked, the completion comment retains prior `ready-for-agent`, the declared dependency is preserved, and the feature index links this evidence. No unchecked criteria or unresolved required work remain for ticket 09. Implementation, bookkeeping and generated next-agent handoff are separate local commits. The next handoff does not execute another ticket.
