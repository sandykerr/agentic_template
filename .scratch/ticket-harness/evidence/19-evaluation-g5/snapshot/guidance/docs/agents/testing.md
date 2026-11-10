# Testing policy

This policy governs development of this repository's harness. The reusable
[test-strategy skill](../../.agents/skills/custom/test-strategy/SKILL.md) guides
coverage selection and suite audits; [TDD](../../.agents/skills/matt-pocock/tdd/SKILL.md)
guides implementation. Read [Python environment guidance](python-environment.md)
before Python or checks. The [harness guide](../ticket-harness.md#python-and-checks)
documents the check commands and tool setup.

## Coverage selection

Map acceptance requirements to existing tests before adding cases. Extend or
reuse those tests where they already exercise the required behavior. For a new
case, identify the distinct failure it detects. Keep the short map in the ticket's
existing evidence or implementation report.

The approved harness seam is the public CLI with scripted external processes,
real temporary Git repositories, and observable Git/report outcomes. Preserve that
agreement. A cheaper public module seam is a design proposal to resolve with the
human, not permission to replace behavioral coverage with internal mocks.

Cover meaningful role, attempt, and failure-policy differences and interactions.
Use representative equivalent inputs rather than automatically multiplying every
dimension. Explicit ticket scenarios and demonstrated regressions remain required.
Several acceptance criteria may share one scenario; separate test names do not
necessarily imply separate coverage. Preserve isolated writable repositories even
when sharing fixture builders or setup helpers.

## Which checks to run

| Change or stage | Verification |
| --- | --- |
| Development iteration | Focused tests for the behavior and affected callers/fixtures, plus relevant static checks. Expand when shared impact is uncertain. |
| Implementation ticket checkpoint | The full test suite and required strict type, lint, format, and whitespace checks once the final implementation is ready. Explicit ticket requirements also apply. |
| Further code, test, configuration, or dependency changes | Rerun affected checks and renew the full-suite completion result for the final implementation. |
| Packaging or entry-point changes | Include wheel/install and installed CLI checks. Include other installed scenarios when explicitly required or when they resolve a concrete uncertainty. |
| Standalone documentation or skill changes | Validate the changed documents/skills, links, routing, and relevant workflow decisions. Runtime tests are warranted when executable examples or runtime behavior are affected. |
| Bookkeeping or handoff after verified implementation | Check the changed records, links, and consistency. Preserve the implementation's recorded check provenance; prose-only bookkeeping does not require replaying its suite. |

An implementation ticket's full-suite gate remains required even when focused tests
pass. This policy does not establish selective testing as a substitute for that
gate, or override a ticket's explicit checks. Missing or failing required checks
leave verification incomplete.

For focused runs, select existing files or cases by the behavior under change.
For example, after reading the case to confirm its relevance:

```bash
python -m pytest tests/test_repairs.py -q -k failed_check
```

Use timing output during the required full run when investigating suite cost:

```bash
python -m pytest -q --durations=20
```

Inspect prerequisite completion records and their relationship to the current
implementation. Independently rerun a prerequisite scenario when there is a
specific compatibility uncertainty; the final full suite already includes the
prerequisite regression tests. Fresh reviewers may reproduce selected behavior
without each repeating the full matrix.

## Evidence and review

Arrange required evidence capture before running checks. Record the command,
exit result, actual source/test revision (and relevant uncommitted changes), and
retained logs/artifact locations. Existing test assertions and their results can
support several criteria. Preserve required CLI/Git evidence from that execution
where available; extra saved JSON is not automatically a reason for a second
complete fixture run. If a required observation was not retained, collect the
missing evidence with a scoped run. Report remaining gaps rather than inferring
unobserved results.

Supply the coverage map and this policy to the existing Spec and Standards
reviewers when tests change. Test value, unnecessary combinations, repeated setup,
fixture ownership, isolation, and reliability belong in the existing review.
Optional maintenance suggestions remain optional.

For a requested or measured suite audit, use the test-strategy skill. Propose
consolidations with an explicit mapping to the surviving regression coverage and
before/after check evidence. Runtime and maintenance cost are useful measures;
reducing the test count alone is not a goal.

## Harness verification remains separate

These choices concern how developers verify changes to the harness. During a
harness run, all configured baseline, lightweight, review, and exact-candidate
gates still apply. Source changes invalidate approvals under the existing rules.
A development test selection or a prior passing tree cannot authorize skipping
a required gate or reusing approval for a different candidate revision.
