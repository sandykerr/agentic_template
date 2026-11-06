# Ticket 01 completion evidence

Implemented only [01: Complete one scripted ticket through every gate](../issues/01-complete-one-scripted-ticket-cycle.md).
This is the scripted tracer bullet, not completion of the first usable release.

## Commits and scope

- Review baseline captured before editing: `1a623bad0b08241367948948b731b9e1f5114671`; initial worktree clean.
- Implementation checkpoint: `b09e324` (`Implement ticket 01 scripted single-ticket CLI cycle`). Created before invoking code-review, so the committed diff contained the implementation.
- Final implementation: `1666920` (`Remove duplicate ignore entries from ticket 01 setup`), including the checkpoint. No runtime code changed after independent review.
- Review command: `git diff 1a623bad0b08241367948948b731b9e1f5114671...HEAD`.
- Implementation files: `ticket_harness/`, `tests/test_cli.py`, `examples/scripted/`, `pyproject.toml`, `.gitignore`, and [CLI/contract documentation](../../../docs/ticket-harness.md).
- Concurrent Python setup edits to `AGENTS.md`, `README.md`, `environment.yml`, and `docs/agents/python-environment.md` were left outside implementation/tracking commits. The supplied shared micromamba environment was used for tests; check tools were isolated in `/tmp/ticket-harness-env`.

## Acceptance evidence

The [saved fixture observations](01-fixture-observations.json) contain actual CLI exit codes, Git revisions, all gate outputs, and run-record locations from two persistent disposable repositories. Raw assignments, input snapshots, logs, worktrees, and records remain under `/tmp/ticket-harness-01-evidence-tgpa0gkw/` on this machine. The JSON observations are committed evidence; raw `/tmp` artifacts are diagnostic and may eventually be removed.

| Acceptance criterion | Actual evidence |
| --- | --- |
| Reproducible Python/check setup, run/status operations, documented minimal fixture | `pyproject.toml` declares Python 3.12+, no runtime dependencies, pinned build backend/dev checks, and CLI entry point. Documentation includes micromamba/check commands and an executable fixture walkthrough. Wheel built and installed successfully in `/tmp/ticket-harness-01-installed`; installed `ticket-harness --help` exited 0. |
| Approved inputs/base separate from editable source; fresh scripted external assignments | Passing CLI test compares snapshot bytes to approved files and checks recorded identities/base. Separate artifact/input/worktree directories are observable. Actual implementation/Spec/Standards reports carry distinct process IDs and the correct ticket/attempt/base/revision. Full assignments record role instructions, project standards, approved requirements, required checks, report contract, and check results. |
| Independently execute baseline, lightweight checks, both reviews, candidate suite | Passing observation records `baseline`, `implementation`, `check-ticket`, `spec`, `standards`, and `candidate`; all exit 0 and pass. Check stdout independently reports the actual Git HEAD. Both review reports identify the submitted revision. |
| Capture submission in Git; advance only to passing candidate; Done records that revision | Passing base `6148f5f8e0d8d0353e305bf0939c19b4a7cbc5c8`; candidate/integration/Done `0ef4b6f61c35bf1c0d6ba356f10bc4c1dce2a3ab`. CLI test verifies merge parents, Git-derived changed files, integrated content, and candidate gate identity. |
| A failed required gate cannot integrate or complete | Saved candidate-rejected run exits 1 with outcome `incomplete`, state `Blocked`, candidate gate exit 1, and integration unchanged at `6148f5f8e0d8d0353e305bf0939c19b4a7cbc5c8`. No Done revision. Tests additionally reject baseline, implementation-process, lightweight-check, Spec-review, and Standards-review failures, preserving available submission/candidate evidence. |
| Status reads recorded outcomes/artifact locations without agents or caller changes | Passing test removes the agent executable before status; JSON equals the recorded run, record bytes and caller Git status stay identical. Both saved scenarios independently verify read-only status and preservation of staged/untracked caller changes. |

## Checks

All commands ran from the repository root. The suite uses real temporary Git repositories, public CLI subprocesses, and scripted external assignments; no network or model calls are part of the suite.

| Command | Result |
| --- | --- |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_cli.py -q` | Exit 0, 8 passed. Repeated during the vertical slices. |
| `.micromamba/envs/dev/bin/python -m pytest` | Exit 0, complete suite: 8 passed in 3.93s, Python 3.12.16 / pytest 9.2.0. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0, no issues in 7 source files; strict mode. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0, all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0, 10 files formatted. |
| `git diff --check` | Exit 0; also rerun for the ignore-only review fix and final tracking edits. |
| `.micromamba/envs/dev/bin/python -m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-01-installed .` | Exit 0; wheel built and installation succeeded without network. Packaging smoke check used the environment's installed setuptools; the declared isolated-build pin remains in project metadata. |
| `PYTHONPATH=/tmp/ticket-harness-01-installed /tmp/ticket-harness-01-installed/bin/ticket-harness --help` | Exit 0; run/status entry point available. |

TDD evidence: the first CLI test failed because `ticket_harness.__main__` did not exist, then passed after implementation. The blocking-review scenario failed before the external fixture implemented its rejection switch, then passed with a genuine blocking report. Assignment-contract assertions failed with missing `required_checks`, then passed after required checks and the report contract were supplied. Additional rejection scenarios exercise the already-established failure invariant through the same CLI seam.

## Standards

Independent fresh agent `/root/review_standards`, reviewing committed checkpoint `b09e324` against the captured baseline:

> Documented standards violations: none found. The implementation keeps lifecycle ownership in runner.py, Git operations in git.py, contracts in agents.py/inputs.py, and process artifacts in records.py, consistent with the scoped cohesive-module guidance. No blocking design finding.
>
> Optional baseline smell: .gitignore:8–16 — Duplicated Code: .pytest_cache/, *.egg-info/, build/, and dist/ each occur twice. Remove the repeated block so future ignore-list edits have one clear location. This has no behavioral consequence and should not delay integration.

Follow-up review of committed fix `1666920`:

> Confirmed resolved in 1666920: the repeated ignore entries were removed, including the redundant .micromamba/ entry. No residual standards findings.

Standards sources supplied explicitly: `AGENTS.md`, domain instructions/glossary/ADR, applicable design sections in `docs/harness-design.md`, Python-environment guidance, project check configuration, and the full code-review smell baseline. No `CODING_STANDARDS.md` or `CONTRIBUTING.md` was found. Tool-enforced findings were excluded from design review.

## Spec

Separate independent fresh agent `/root/review_spec`, reviewing committed checkpoint `b09e324` against the captured baseline:

> No findings within ticket 01's scope.
>
> The implementation provides the documented run/status CLI, approved-input snapshots, fresh external assignments, independent gates, harness-owned submission capture, exact tested-candidate promotion, and preserved rejection evidence.
>
> No missing or partial ticket-01 requirements, unasked scope, or incorrect implementations identified. Broader input/report validation, tampering protection, repairs, scheduling, and enforced access boundaries remain appropriately assigned to later tickets.

The reviewer received ticket 01 explicitly plus Public interface and approval, Ticket lifecycle, and Independent checks and exact revisions from the approved spec. Supporting initial contract requirements and later-ticket boundaries were explicit. These reviewers assessed the implementation independently; fixture-script reports were not used as a substitute.

Standards: 1 optional finding, fixed and rechecked, 0 outstanding. Spec: 0 findings. No blocking findings on either axis; no unresolved ticket-01 decisions. All agents stayed below the 250K active-context target using fresh, focused review contexts.
