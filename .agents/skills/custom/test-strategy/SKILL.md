---
name: test-strategy
description: Choose coverage and verification scope when adding or changing tests, or audit a slow, redundant, or flaky test suite. Use alongside TDD while preserving required checks and approved testing seams.
---

# Test strategy

Manage the value and cost of regression coverage. [TDD](../../matt-pocock/tdd/SKILL.md) owns the red/green loop;
this skill owns which behaviors need tests, which existing tests suffice, and
which checks to run. Read the repository's testing policy and required checks
before choosing verification scope. Follow applicable glossary and ADR guidance.

## During implementation

Before adding tests, inspect the existing coverage at the approved seams. Make a
brief map from each changed requirement or failure mode to an existing test, an
extension, or a missing case. Keep this map in the current task notes or completion
evidence; a separate document is usually unnecessary. Existing tests can satisfy
a requirement without adding tests or manufacturing a failure in working code.

For each additional case, identify the plausible regression it would catch that
the existing cases would miss. Expand combinations when they exercise different
decisions or meaningful interactions. Equivalent inputs usually need representative
cases rather than every permutation. Preserve explicitly required scenarios and
regressions from demonstrated bugs; test counts and coverage percentages alone do
not establish redundancy.

Choose the least expensive approved public seam that can detect the actual
failure, preserving behavior rather than internal structure. If the agreed seam
makes necessary coverage impractical, surface the design tradeoff through the
project's design workflow. A new seam requires the existing approval process;
internal mocks are not a shortcut around it. Then use TDD for the missing behavior.

## Verification and evidence

For ticket review/repair preparation, apply
[efficient ticket development](../../../../docs/agents/development-efficiency.md).
Use the existing worker and canonical check artifacts for mechanical work;
fresh reviewers still provide the required independent source assessment.

Choose focused checks from the changed behavior and its callers, shared fixtures,
configuration, and dependencies. Broaden selection when impact is uncertain. Run
the repository's required completion checks, including any required full-suite gate.
Rerun checks when a failure, a relevant change, or a remaining uncertainty
invalidates their evidence. Required exact-revision verification always takes
precedence over reusing earlier results.

Plan evidence collection before verification. Retain the required run's command,
exit result, tested source/test identity, logs, and necessary artifacts so the
same run supports completion bookkeeping. If required evidence is missing, collect
it with a scoped additional check and explain the gap. Saving a second report
does not by itself justify replaying the entire scenario matrix. Refer to earlier
results with their actual provenance; do not relabel them as tests of a new revision.

## Suite audits

Audit the wider suite when requested or when measured runtime, flakiness, or
maintenance friction warrants it. Ordinary feature work needs only the local
coverage assessment above. Scope an audit to the affected area or observed cost.

Use existing timing/failure records first; collect missing timings during the
next required run where possible. Group tests by behavior and failure mode,
including parameterized cases, and examine repeated setup and expensive processes.
For a proposed deletion or consolidation, identify the surviving test and explain
which regression protections it retains. Verify the affected behavior and required
completion checks after changing tests. Share fixture builders where useful while
preserving scenario isolation. Keep uncertain coverage until it can be evaluated.

## Existing implementation reviews

Give the existing reviewers the coverage map, actual check evidence, and repository
testing policy. Spec review checks required behavior and regressions. Standards
review considers redundant coverage, unnecessary scenario combinations, costly
setup, fixture ownership, isolation, and brittle assertions. A blocker needs a
concrete correctness, reliability, or maintenance consequence; a preference alone
remains optional. This adds review guidance, not another reviewer or completion gate.
