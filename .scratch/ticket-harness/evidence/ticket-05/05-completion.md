# Ticket 05 completion evidence

Implemented only [05: Repair rejected submissions within a bounded allowance](../issues/05-repair-rejected-submissions-within-budget.md).
Verified implementation: `34a49b7090a77d689a67c4230cc8b5f12c9c9f35`.

## Revisions and scope

- Fixed review baseline, captured before edits: `d6abfd62f86165c5a3e63c61b3c0ff86d2af452f`.
- Implementation checkpoint: `34a49b7`, committed before separate fresh Spec and Standards reviews. Both reviewed the complete committed diff against the original baseline. No blocking findings, optional suggestions, fix commits, or runtime changes after review.
- Files: `ticket_harness/{runner,agents,git,inputs,records}.py`, `tests/test_repairs.py`, the prerequisite fixture's explicit zero-repair configuration in `tests/test_cli.py`, and [public contract documentation](../../../docs/ticket-harness.md).
- Prerequisite 03 verified from implementation `07094fa`, bookkeeping `9604651`, checked criteria, checks, separate reviews and [completion evidence](03-completion.md). Prerequisite 04 verified from checkpoint `dc27eb2`, final implementation `8d345bd`, bookkeeping `237d6ff`, checked criteria, separate reviews and [completion evidence](04-completion.md) / [observations](04-fixture-observations.json). Both headers are completed. Tickets 01/02's legacy readiness headers do not supersede their verified completion evidence.
- No active harness run using these feature requirements was found. All executed harness runs use separate disposable target requirements. The pre-existing skill relocation remains unstaged and outside all ticket commits. No push was performed.

## Acceptance evidence

[20 saved actual CLI/Git observations](05-fixture-observations.json) identify the exact implementation, complete attempt records, stage/revision/exit/report identities, operations and diagnostics, repair assignment context, final integration, status equality, and raw run/artifact locations. Every scenario's assertions and status equality passed. Temporary diagnostic worktrees and artifacts remain at the recorded paths; committed observations persist after eventual temporary-directory cleanup.

| Criterion | Current implementation and observable evidence |
| --- | --- |
| Configurable allowance, default two repairs; worker iterations do not count separately | `max_repairs` is a nonnegative integer, default 2, rejecting booleans/floats/strings/null and other types before any process. CLI tests exhaust allowances 0/1/2 and perform several internal edits plus a worker-run check within one assignment. Saved `final-default-repair` succeeds on attempt 3, while all five exhaustion scenarios stop at attempt 3. |
| Fresh repair context with current changes, rejected identities and concrete failure evidence | Each assignment invokes a fresh external process in a new detached worktree; assignments retain approved inputs and checks with exact integer attempt identity. Current working contents, including uncommitted changes after an invalid report, are copied without changing rejected work. `repair_context` carries previous failure and all captured rejected submission/candidate identities; `check_results` carries findings and readable command artifacts. Saved `check-repaired`, `invalid-worker-repaired`, and `final-default-repair` inspect current edits, process IDs, prompts, diagnostics and accumulated history. |
| Repair lightweight checks, either review axis and candidate-integration failures | Saved `check-repaired`, `spec-repaired`, `standards-repaired`, `candidate-repaired`, and `merge-repaired` each demonstrate a concrete rejection followed by successful repair. Matching exhaustion observations preserve three failed attempts for every gate type. Failed Git operations retain per-attempt diagnostics. |
| New repaired revision, renewed lightweight checks, both fresh reviews and candidate suite | Each repair is captured as a new commit against its starting revision, with changed paths derived from the original base. Even unchanged repair contents require a fresh captured revision and complete verification. Tests bind each check/review to the repaired submission and candidate suite/parents/tree/integration/Done to the exact candidate. Saved success scenarios and `approval-invalidated-and-repaired` demonstrate renewed verification after source changes; stale reports cannot approve repairs. Independent Spec review also reproduced unchanged-content repair publicly. |
| Exhaustion preserves changes/history, Blocked and incomplete | Five saved exhausted scenarios retain all three submitted revisions, per-attempt worktrees, candidate identities when available, prompts/reports/stdout/stderr, gate ranges and failure messages. CLI exits 1 with Blocked/incomplete and no Done revision; integration remains at base. Caller HEAD, distinct staged/unstaged contents, and untracked work are verified intact; status equals durable records. |
| Successful repair and exhaustion; no unlimited secondary path | 58 repair-focused cases cover successful repairs, final-allowance success, exhaustion, invalid configuration, missing/malformed/stale/mistyped/overflow reports and nonzero processes across all roles under the same allowance. Saved stale-Spec/nonzero-worker exhaustion cases stop after three attempts. Valid worker human-decision reports stop immediately, including nonzero exits; baseline/preflight start no attempts. External integration movement and input/evidence integrity violations stop without authorizing more repair. |

## Checks and TDD

All Python used the documented reusable `.micromamba/envs/dev/bin/python`. Mypy and Ruff were verified available in `/tmp/ticket-harness-env/bin/`. No dependencies or network/model calls were added.

| Actual check | Result |
| --- | --- |
| `python -m pytest tests/test_repairs.py -q` | 57 passed before the final shared-baseline regression; that additional regression separately passed. |
| `python -m pytest tests/test_repairs.py -q -k invalidated_shared` | Exit 0: 1 passed, stopping before any repair worktree starts. |
| `python -m pytest -q` | 355 passed in 329.83s at the earlier collection; final checkpoint-wide run: **362 passed in 408.88s** at `34a49b7` (exit 0). |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0: strict mode, no issues in 7 source files, including final checkpoint. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 14 files already formatted. |
| `git diff --check` | Exit 0 for implementation and bookkeeping. |
| Reusable Python `-m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-05-reviewed-installed .` | Exit 0: checkpoint wheel built and installed without network. |
| `PYTHONPATH=/tmp/ticket-harness-05-reviewed-installed /tmp/ticket-harness-05-reviewed-installed/bin/ticket-harness --help` | Exit 0: installed run/status entry point. |
| Reusable Python `/tmp/observe-ticket-05.py` | Exit 0: 20 saved public CLI/Git observations at `34a49b7`, all assertions/status comparisons passed. |

Red/green slices at the agreed public CLI/Git/report seam exposed the original stop-after-check behavior, loss of uncommitted changes after invalid reports, absent Git-operation diagnostics, nonzero human-decision repair churn, artifact collisions with valid numbered check names, and attempts consumed after baseline invalidation. Each failing behavioral regression preceded its implementation and focused passing checks/typechecking. Additional public scenarios cover all required rejection types, renewed identities/gates and bounded report/process failures. No parser-internal mocks or fixture reviews substitute for implementation review.

## Standards

Fresh independent `/root/review_standards_05` reviewed `git diff d6abfd6...34a49b7`:

> No Standards findings for `d6abfd6...34a49b7`.
>
> The changes preserve cohesive ownership: configuration validates the allowance, Git owns worktree copying and submission capture, records own artifact naming, and the runner owns bounded lifecycle decisions. This follows `docs/harness-design.md:49` and the spec's “Cohesive module responsibilities” guidance.
>
> Reviewed all changed hunks against documented standards and the full supplied smell baseline. No mandatory blockers or sufficiently supported optional design suggestions found. Behavioral coverage crosses the documented CLI seam using scripted processes and real Git repositories, consistent with the accepted testing approach.

Standards sources: AGENTS.md, domain/environment/tracker guidance, glossary/ADR-0001, `docs/harness-design.md`, scoped cohesive-module and combined design-policy spec sections, `pyproject.toml`, and the complete code-review smell baseline. Matt's deep-module vocabulary and Microsoft's OOP principles were supplied as the combined design lens. No CODING_STANDARDS.md or CONTRIBUTING.md exists. Tool-enforced concerns were kept separate.

## Spec

Separate fresh `/root/review_spec_05` reviewed the same complete committed diff with ticket 05 and the scoped Bounded failures and timeouts, Independent checks and exact revisions, and Ticket lifecycle requirements supplied explicitly:

> No Spec findings.
>
> The implementation meets ticket 05's bounded repair requirements and preserves the preceding report-validation, input/evidence protection, revision-bound verification, candidate identity, and CAS contracts. No missing requirements, scope creep, or incorrect behavior identified.
>
> Independent public-CLI reproduction passed: a transient lightweight-check failure followed by unchanged repair contents produced a fresh submission revision, renewed checks, both reviews, and candidate verification before completing on attempt 2.

Standards: 0 blockers, 0 optional suggestions. Spec: 0 findings. Both reviews used fresh contexts under the feature's 250K target. All six criteria are verified at the final checkpoint; no unchecked criteria or unresolved ticket-05 decisions remain. Broader human-decision handling, optional-suggestion reporting, timeouts, scheduling, live Codex/role skills, OS role enforcement, concurrency, and recovery remain with later tickets. Existing protection remains a process-boundary integrity check, not an OS sandbox.
