# Ticket 15 repair 1: STD15-01

Fresh GPT-6.1 Sol Medium repair assignment, 250K active-context target. Original whole-diff baseline remains `90255aaf6faf9aedce18f7159093f5dbfde294b7`; initial implementation is `36ed3e72c278cf147c84ae9c282cd2899af23ad0`. This repair addresses only the initial Standards blocker STD15-01. Initial Spec review found zero findings. Fresh whole-diff High Spec and Standards re-review and ticket bookkeeping remain parent responsibilities. No development human QA, decision, next-ticket work or push is performed.

## Change and regression

Checkpoint JSON deserialization detached the `verified` evidence dictionaries from the durable `record.gates` entries. Restored source validation therefore stopped unsafe work but saved stale passing gates. The runner now looks up each exact saved evidence value in the verified record's gate array and retains the canonical entry. This preserves checkpoint version 1 and all original bytes/identities; later invalidation mutates the durable gate. The record already binds the checkpoint and all exact gate values before continuation. Gate evidence has distinct stage/worktree/artifact identities.

`tests/test_continuation.py::test_continued_run_records_invalidation_of_earlier_verified_source` uses the approved CLI/process/real-Git seam: stop M1, continue in a fresh owner, modify the earlier baseline source, request another stop. It asserts incomplete exit, durable `passed: false`, `verification_status: invalidated`, diagnostic, unchanged dev and no consumed acceptance. Fixture waits and owned-process cleanup are reused. The baseline represents the common restoration/invalidation path used by checks and structurally valid reviews; a duplicate review variant would not exercise a distinct restoration branch. Existing report/source-integrity tests remain intact. See the added Repair 1 section in `15-coverage-map.md`.

The retained red capture failed at `baseline["passed"] is False` (actual true), exit 1, before runtime repair. Green passed after rebinding. `15-repair1-red-{source,result}.json` / `.log` and `15-repair1-green-{source,result}.json` / `.log` retain exact commands, identities and results. Focused continuation then passed 20 cases in 92.57s. Strict mypy, Ruff lint/format and scoped whitespace passed.

## Isolated installed proof

Offline wheel build reused pinned `/tmp/ticket15-build-deps/setuptools-80.9.0-py3-none-any.whl` (SHA-256 `062d34222ad13e0cc312a4c02d73f059e86a4acbfbdea8f8f76b28c99f306922`) and installed into `/tmp/ticket15-repair1-installed`. All nine installed sources match the repaired tree; wheel SHA-256 is `1dc83a2df7a10737d415c6c3638e5dc1edbbd7e109a9753bbbc995c729b54bae`. See `15-repair1-package-manifest.json` and retained wheel under `15-repair1-package/`. Pinned mypy 1.19.1 and Ruff 0.14.10 were reverified in `/tmp/ticket12-tools`. No shared environment package was changed.

`15-repair1-installed-scenario.py` executes the repaired installed console script from `/tmp`, independently resolves its import under the isolated target, completes the original two-milestone stop/continue/approval scenario, then independently reproduces post-restore baseline invalidation. Both passed (18.102s wrapper). It retains complete commands/exits, final success and invalidation records in `15-repair1-installed-observations.json` and `15-repair1-installed-invalidation.json`, with copied raw checkpoint/request/decision/ownership/rejection artifacts in `15-observations/repair1-installed/`.

## Provenance boundaries

All repair captures use `15-repair1-*`; raw observations use `15-observations/repair1-*`. Initial `15-final-*`, consolidated check/source/observation manifests, installed scenario/package, original logs, independent initial reports and `15-root-*` audits remain intact as historical initial-implementation proof. They are not relabeled as repaired-source gates. The unrelated tracker edit retains SHA-256 `3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.

## Final repair gates and commit

Repair implementation commit: `d11f0bc60a2c11c40683e58581dffa10e36a91be` (only `ticket_harness/runner.py` and `tests/test_continuation.py`; 23 insertions, one deletion). Renewed full suite: **544 passed in 910.17s**, exit 0 (wrapper 910.693s). Strict mypy, Ruff lint/format, scoped working-tree whitespace, actual staged whitespace, committed whole-original-baseline whitespace, offline wheel, isolated install and installed CLI scenarios all exited 0.

`15-repair1-check-results.json` and `15-repair1-checks.log` consolidate the exact ten final gate commands/exits and log hashes. `15-repair1-final-source-identity.json` binds all 23 final-suite runtime/test/guide/config hashes to current bytes and the repair commit; every final gate capture matches that map. `15-repair1-fixture-observations.json` indexes all 123 renewed full-suite raw observations with hashes and retained continuation artifact locations. `15-repair1-consolidate.py` retains the actual assertion/consolidation procedure.

The first sandbox staging command failed because `.git/index.lock` was read-only. The automatic approval review allowed the scoped retry, which staged only the two implementation paths. An empty-index `15-repair1-final-staged-whitespace` capture preceded successful staging; it is retained as history and excluded from consolidated gate proof. The actual gate is `15-repair1-final-actual-staged-whitespace`, and `15-repair1-final-committed-whitespace` checks the entire implementation against the original fixed baseline. No permission blocker remains.

The repair is ready for the parent's fresh independent whole-diff High Spec and Standards reviews. Ticket completion bookkeeping, QA handoff and milestone acceptance are not claimed by this repair assignment.
