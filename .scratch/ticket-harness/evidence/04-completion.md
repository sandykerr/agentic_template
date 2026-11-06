# Ticket 04 completion evidence

Implemented only [04: Promote only the exact verified candidate](../issues/04-promote-only-the-verified-candidate.md).
The verified implementation is `8d345bddabd3d7fdc9cfb049e3cc7ce70f66e54a`.

## Revisions and scope

- Fixed review baseline captured before editing: `6c8df5cd23f35d7d164fea5e9e5d224f8bed4cf0`.
- Implementation checkpoint: `dc27eb2`, committed before separate independent reviews.
- Review fixes and final implementation: `8d345bd`. Both reviewers reassessed the complete committed diff against the original baseline. No implementation changes followed final review.
- Files: `ticket_harness/{git,inputs,records,runner}.py`, `tests/test_transaction.py`, and [public contract documentation](../../../docs/ticket-harness.md).
- Ticket 01 prerequisites were verified from its checked criteria, implementation commits `b09e324`/`1666920`, bookkeeping `3c6bff3`, separate independent reviews, and [completion evidence](01-completion.md), rather than its legacy readiness header. Ticket 02/03 contracts and evidence were read; their tests remain passing.
- The pre-existing skill relocation from `.agents/skills/implement-with-checkboxes/` to `.agents/skills/custom/` remains outside these commits. No active harness run using these feature requirements was found; tests and observations use disposable target requirements. Bookkeeping occurs outside harness execution.

## Acceptance evidence

[Saved actual CLI/Git observations](04-fixture-observations.json) cover 16 scenarios at `8d345bd`. Each records CLI exit/outcome, exact Git identities, gate validity, integrity diagnostics, preserved caller work, status equality, and the raw run-record location. Individual diagnostic repositories, snapshots, logs, assignments, and rejected work remain at the `/tmp/ticket-harness-test-*` locations named in that file. Committed observations survive eventual removal of those temporary artifacts.

| Acceptance criterion | Current implementation and observed evidence |
| --- | --- |
| Record approved identities; detect requirement/state tampering | Recorded SHA-256 identities are checked before execution and promotion. Shared integrity protection brackets agents, checks, checkout hooks, submission capture, and candidate merge. Tests alter snapshots, originals, assignments, `run.json`, prior outputs, and source requirements across implementation/Spec/Standards roles; hook tests cover the same ownership boundary. Rejected bytes are saved, harness-owned originals restored, and source edits retained. Deletion and directory replacement also retain diagnostics and restore snapshots. Saved snapshot/record/hook/checkout/deletion/directory scenarios all reject without Done. |
| Bind checks/reviews to submission and suite to candidate | The original passing CLI test verifies every stage/revision and both review report identities. All 256 earlier CLI/preflight/report cases remain passing. New tests invalidate evidence when its worktree changes, including dirty contents, commits, HEAD changes, index visibility flags, and cross-worktree edits. Saved passing observations record the exact submission on lightweight and review gates and candidate on the broader suite. |
| Promote only exact tested candidate with expected previous tip | Git validates candidate parents and its tree against the reviewed submission, checks source freshness, and performs compare-and-swap using the original integration tip. Final ref update disables hooks so user code cannot execute after validation. Saved passing and final-ref-hook runs finish with candidate = suite revision = integration = Done revision; hook-written resolutions cannot integrate. |
| Preserve external branch updates and failed merge/candidate evidence | Public tests move integration during Spec, Standards, and candidate stages; CAS fails while the external tip survives. A failed merge preserves submission and merge diagnostics; failed candidate suites preserve candidate/logs. Saved external-movement, failed-merge, merge-resolution, and failed-candidate runs exit 1 without Done and leave integration unchanged by the harness. |
| Source changes invalidate approval | Every verified source is rechecked after processes and before promotion. Affected gates become `passed: false`, `verification_status: invalidated`, with diagnostics, while structurally valid reports retain their separate valid status. Persistent hidden edits using assume-unchanged/skip-worktree are rejected. Cross-review and candidate-stage edits invalidate earlier evidence. This attempt stops; renewed verification is necessary, and automatic repair remains ticket 05. |
| Preserve caller/rejected work; no unverified Done | Tests compare staged index contents, distinct unstaged contents, untracked bytes, caller HEAD/status, retained submitted/candidate contents, logs, and status records. All 16 saved scenarios preserve dirty caller work; all 14 rejecting scenarios have no Done revision. Worktrees/rejected directories and Git commits remain inspectable. |

## Checks and TDD

All Python used the documented reusable `.micromamba/envs/dev/bin/python`. Mypy/Ruff were verified available in `/tmp/ticket-harness-env/bin/`; no dependencies or network/model calls were added.

| Actual check | Result |
| --- | --- |
| `python -m pytest tests/test_transaction.py -q` | Exit 0: 48 passed after final fixes. |
| `python -m pytest -q` | Exit 0: **304 passed in 154.15s** at final implementation `8d345bd`. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0: strict mode, no issues in 7 source files. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 13 files formatted. |
| `git diff --check` | Exit 0 for implementation; also checked for bookkeeping/handoff. |
| Reusable Python `-m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-04-reviewed-installed .` | Exit 0: final implementation wheel built/installed without network. |
| `PYTHONPATH=/tmp/ticket-harness-04-reviewed-installed /tmp/ticket-harness-04-reviewed-installed/bin/ticket-harness --help` | Exit 0: installed run/status entry point. |
| Reusable Python `/tmp/observe-ticket-04.py` | Exit 0: 16 public CLI/Git scenarios at `8d345bd`; saved observations and retained diagnostic runs. |

Red/green slices exposed requirement rewriting in a worker source tree, later edits to earlier review source, merge-hook source resolutions, and submission-hook requirement edits. The independent Spec review then produced two further failing public reproductions: hidden tracked edits and hook overwrites of review evidence. Regression tests first reproduced both failures, then passed with index-visibility validation and shared protection of hook-capable operations. Follow-up failing tests covered checkout-hook overwrites, post-verification reference hooks, and directory replacement of snapshots; each received a focused fix. Tests use external processes and real repositories through the agreed CLI/Git/artifact seam, without parser-internal mocks.

## Standards

Fresh independent `/root/review_standards_04` found no blocking concern at `dc27eb2`. Two optional judgment calls concerned the restoration-policy boolean name and duplicate repository-relative path selection. Both were addressed while sharing integrity protection.

Final independent re-review of the entire original-baseline-to-`8d345bd` diff:

> No blocking findings or documented-standard violations. No remaining actionable optional suggestions.
>
> The two earlier optional concerns are resolved: `restore_on_violation_by_path` and its docstring explain the restoration policy, and `approved_source` centralizes repository-relative input-path selection. The shared protection context has two demonstrated callers and localizes integrity ownership without speculative abstraction. Git validation and hook suppression remain within Git ownership.

Standards sources: `AGENTS.md`, domain guidance/glossary/ADR-0001, applicable ownership/design rules in `docs/harness-design.md` and the spec, environment guidance, `pyproject.toml`, and the complete code-review smell baseline. No `CODING_STANDARDS.md` or `CONTRIBUTING.md` exists. Tool-enforced checks were kept separate.

## Spec

Separate fresh `/root/review_spec_04` found two blockers at `dc27eb2`: `git status` could miss edits hidden by index flags, and merge hooks could overwrite accepted evidence outside the integrity bracket. Both were fixed in `8d345bd` with real failing/passing regressions.

Final independent re-review:

> Blocking findings: none. Both previously reported failures are fixed. Original public CLI reproductions against `8d345bd` now return exit 1 and Blocked, preserve hidden source edits, restore the original review artifact, and retain rejected evidence. No remaining concrete requirement mismatch or unasked scope expansion was found within the documented trusted-process and process-boundary limits. Optional suggestions: none.

Spec review explicitly received ticket 04 and its scoped requirements: Independent checks and exact revisions; Requirements, configuration, and run records; Agent contracts and access. Both independent reviewers stayed below the feature's 250K active-context target. Scripted fixture reports did not substitute for implementation review.

Standards: 0 blockers, 2 optional suggestions resolved, 0 outstanding. Spec: 2 blockers fixed and independently reproduced/re-reviewed, 0 outstanding. All six criteria are verified; no unresolved ticket-04 decisions remain. Integrity checks observe process boundaries and are not an OS access/security boundary. Repairs, recovery/resume, concurrency, scheduling, timeouts, live Codex, new role-skill delivery, and OS role enforcement remain with later tickets.
