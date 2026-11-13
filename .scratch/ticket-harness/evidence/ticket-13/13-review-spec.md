# Ticket 13 independent Spec review

Verdict: pass. No blocking findings, missing/partial requirements, incorrectly implemented requirements, or unasked implementation scope identified. No optional suggestions.

Reviewed ticket 13, proposal R04, the spec's “Independent checks and exact revisions” and “Feature-to-development promotion and human QA,” glossary, applicable ADRs, public documentation, coverage map, testing policy and test-strategy guidance.

The requirement “Only a passing candidate can be presented for QA” is implemented with a separate exact-candidate regression gate followed by input/source/branch validation (`ticket_harness/runner.py:451`, `ticket_harness/runner.py:476`). The request captures run/plan/milestone/source/base/candidate identities, human checks and actual gate evidence (`ticket_harness/runner.py:484`). Existing per-ticket gates remain independent, development is not advanced, and later work remains Pending.

“Changed source invalidates earlier check/review approvals” is preserved through source validation and independent plain-merge comparison (`ticket_harness/git.py:106`). Conflict resolutions or merge-hook edits stop with preserved source and explicit renewal requirements before any QA request; this slice does not claim to execute renewed reviews. Approval consumption/promotion and continuation remain outside ticket 13.

Public fixture observations demonstrate passing preparation, rejected regression, changed development base, concurrent feature/development movement, source mutation, unresolved/custom-driver conflicts and hook edits. Assertions exercise observable CLI/Git/report behavior at the approved seam.

Verification metadata:

- Fixed baseline: `fd292a988cde79532bb84714b5800e4baa5de127`; implementation: `19ea4f1b0bbdc601653468212aaaa0a7211d5c6f`; reviewed `git diff fd292a988cde79532bb84714b5800e4baa5de127...HEAD`.
- Independently compared every captured file hash for all five renewed-final checks with committed HEAD and disk: 20 files per capture, zero mismatches. Recorded pytest: 509 passed in 795.92s; strict mypy, Ruff lint/format and whitespace checks all exited 0.
- Audited all 88 consolidated observations against their retained raw JSON: zero structural mismatches after excluding the added `retained_file` locator. Inspected representative requests, exact gate evidence, branch identities and failure outcomes.
- Independently reproduced `python -m pytest tests/test_milestones.py -q -k 'changed_development_base or failed_milestone_regression'` with the documented reusable interpreter: 2 passed, 38 deselected in 12.89s.
- No implementation, ticket status, acceptance checkbox, or unrelated tracker edit changed by this review. Human milestone acceptance is not claimed.
