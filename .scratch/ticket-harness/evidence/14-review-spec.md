# Ticket 14 independent Spec review

Baseline: `d67c12d91495af00557b279d0bf0e1da518e6fcc`.
Reviewed HEAD: `29fb5569cf53c75bd351d6bd176bb29889c42a65`.
Diff: `git diff d67c12d91495af00557b279d0bf0e1da518e6fcc...HEAD`.
Commit: `29fb556 Consume exact milestone QA decisions before promotion`.

Reviewed all six ticket criteria, R05, scoped spec requirements, approved handoff boundaries, glossary/ADRs, testing policy and coverage guidance. This review is independent of Standards review.

## Findings

- Missing or partial requirements: **0**.
- Unasked behavior or scope expansion: **0**.
- Implemented requirements that look wrong: **0**.
- Blocking findings: **0**. Optional suggestions: **0**.

Exact separate approval/schema/request matching and indefinite observable waiting are implemented in `ticket_harness/runner.py:542–609`; external-process authority protection is at `:65–74`. Acceptance revalidates approved inputs, verified sources, request bytes and evidence at `:610–626`. `ticket_harness/git.py:165–194` compares both expected tips in one transaction and preserves checked-out caller branches. Consumed records, next-group admission and final-only completion appear at `runner.py:286–296` and `:627–638`. Later-group eligibility validation supports the newly executable groups. The public guide accurately describes this foreground contract and its trusted-process protection boundary.

## Evidence audit

Independently compared all 21 captured file hashes with current bytes and committed HEAD; every final suite/mypy/lint/format/whitespace capture has the same map and exit 0. Suite log records **524 passed in 684.03s**. Captures truthfully identify the precommit working tree; hashes establish its equivalence to the reviewed commit. Verified three original historical red-log hashes and whitespace-only display trimming.

Inspected the consolidated evidence and 103 retained raw scenarios. Independently checked both consumed decision hashes/request identities, the aligned next-worker base, final refs, actual foreground/status exits and all nine QA-time invalidation failures. These observations agree with the root audit. Preparation fixture termination is distinct from successful run completion.

## Actual independent checks

Ran the public two-milestone scenario using the documented environment:
`python -m pytest -q tests/test_qa_promotion.py::test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision` — **1 passed in 9.37s**, exit 0. Also ran committed-diff whitespace validation, exit 0, and independently verified provenance/raw observations with assertion scripts.

No full-suite repeat. Ticket 15 continuation/ownership and real development-milestone human acceptance remain outside this review. The unrelated tracker edit retains its supplied SHA-256 and remains unstaged.
