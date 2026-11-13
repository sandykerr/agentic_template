# Ticket 15 coverage map

Approved seam: public CLI, external scripted processes, isolated real Git repositories and report/ref observations.

- Existing test_qa_promotion: exact typed decision contract, indefinite waits, source/evidence/ref revalidation, expected-old atomic promotion, later-group eligibility and final-only success. Preserve all.
- Existing test_milestones/dependencies/transaction/integrity: immutable inputs, exact verified sources, ordered Done states, bounded gates and caller work.
- Missing: clean stop/new-process continuation through both groups without baseline/assignment replay; extend with test_continuation end-to-end including replay and repeated stops.
- Missing: stale stopped inputs, snapshots, plan, request, evidence, source, refs and record/checkpoint tampering; representative independent mutations at stopped checkpoint must reject without modifying original state/refs/evidence.
- Missing: simultaneous active ownership and unsupported interruption/duplicate continuation; public CLI tests reject while owner active and reject stopped checkpoint reuse/completed or arbitrary interrupted runs.

Required final checks: full pytest suite, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI continuation scenario. Retain commands/exits/source hashes and fixture observations from actual executions.

## Repair 1: STD15-01

The initial continuation coverage rejected mutation before restoration, but did not inspect durable gate invalidation after restoration. `test_continued_run_records_invalidation_of_earlier_verified_source` stops at M1, continues in a new owner, changes the baseline worktree, and requests another stop. It requires an incomplete exit, durable `passed: false` / `verification_status: invalidated` / source diagnostic, unchanged development and no consumed approval. It uses the existing CLI/process/real-Git seam and owned fixture cleanup.

The test failed before repair because the durable baseline gate still passed, then passed after rebinding deserialized evidence to the canonical gate. A review-specific duplicate adds no distinct ownership path: all baseline/check/review/candidate evidence entries traverse the same restoration and invalidation code. Existing review integrity coverage preserves valid report parsing independently of source invalidation.

Repair captures use only `15-repair1-*` and `15-observations/repair1-*`. Initial `15-final-*`, manifests, installed package and root audits remain historical initial-implementation evidence. Required renewed gates include focused continuation coverage, full suite, strict mypy, Ruff lint/format, actual staged/committed whitespace, isolated offline wheel/install and installed continuation/invalidation.
