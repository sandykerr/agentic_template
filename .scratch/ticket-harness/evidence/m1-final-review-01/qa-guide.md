# M1 QA — accepted 2026-11-16

All fifteen development tickets 10–24 are complete. Caller-index repair `e06eeaf`
is independently verified fixed. Fresh Spec, Standards and cumulative all-package
Standards reviews each found zero blockers/optional suggestions. The current
source is `88e4cd8aabc78e76e66efc02983fec3900ab0a23`; all 28 source/test/configuration
hashes match the retained 563-test pass and required static checks.
[Reports and identities](README.md), [cumulative assessment](../../reviews/M1-architecture-01.md).
Your earlier code/documentation review is already recorded as complete.

## Completed final demo and development M1 acceptance

**M1 is accepted.** The human approved the final demo and conditionally accepted
development M1; all exact-promotion/completion/no-replay conditions passed.
[Actual human QA decision](m1-qa-decision.md), [completion checks](m1-acceptance-result.json).

Final fixture request `ca4bffef76d14545869e525dd842fdc5`, candidate
`2338f88cce672b05ca2fb44127f35ce3659a8cfa`, promoted both disposable refs exactly.
The final run exited0/completed/true. Agent launches, attempts and gates remained
unchanged; baseline count stayed one. The earlier first decision could not accept
this final request, and both tickets Done before final acceptance still had
completion false. [Completed record](demo-completed-record.json).

Development M1 request `41a556a9352d44a3922a9c41f30f36af` accepted harness source
`88e4cd8aabc78e76e66efc02983fec3900ab0a23` and its exact manifest/reports/evidence.
[Request](development-m1-request.json), [actual human reply](human-final-demo-and-development-decision.json).
M2 ticket25 is next eligible but not started. Preparation and planned actions
below retain their earlier scope; pending statements are historical.

## First approved demo step (historical preparation)

The fresh disposable two-milestone demonstration is stopped cleanly. It has
rejected a stale decision and resumed in a new process without replaying the
baseline or completed assignments. No approval was consumed; dev is unchanged.

| Identity | Value |
| --- | --- |
| Runtime plan | `v1`, scripted fixture; separate from development oop-v2 / review-process-1 |
| Run | `a339cf523b9141cb920718fe2c6960c8` |
| Fixture milestone | M1, first of two demo groups |
| Request | `af4eea6758044990a06aa5c1504d98d0` |
| Feature | `08aac89bef9e04c5c481affd5a914cc5f055a65b` |
| Development | `5d09935b2bf2c4bf0e533b1e6889963b07c55191` |
| Exact tested candidate | `088f10a7e174fd644b53fa71d9252fe732465474` |
| Deliberate checkpoint | `b73ff025749a41f096dcd8b9554c6652` |

[Exact request](../m1-index-repair-01/qa-candidate/human-checkpoint-request.json),
[stopped record](../m1-index-repair-01/qa-candidate/human-checkpoint-record.json),
[location](../m1-index-repair-01/qa-candidate/demo-location.json),
[actual commands/results](../m1-index-repair-01/qa-candidate/demo-commands.json).

Inspect [value.txt](/tmp/ticket-harness-m1-repaired-qa-lju67ec9/run/worktrees/milestone-candidate/value.txt) (`2`) and
[work-01](/tmp/ticket-harness-m1-repaired-qa-lju67ec9/run/worktrees/milestone-candidate/work-01) (`delivered 01`).
`work-02` is absent, ticket02 has attempt zero, and `feature_complete` is false.
The exact candidate's separate milestone regression passed; all seven recorded
gates passed. A repeated clean stop retains the same request and no active owner.

To exercise the remaining promotion check, the human must approve **this exact
fixture request**. Record the actual reply and atomically write the complete
request with `decision: APPROVED` to `/tmp/ticket-harness-m1-repaired-qa-lju67ec9/run/qa-decision.json`, then
continue the stopped run using the current checkout's `.venv/bin/python`.
The existing decision there is deliberately stale/rejected and is not approval.
This first fixture approval permits the second demo group; it does not accept
development M1. Inspect the separately generated final fixture request before
accepting it. Verify feature completion stays false until that exact final
approval, and only final acceptance exits zero with completion true.

## Other planned checks and their evidence

- Follow the real review concern from [original F1](../m1-qa-01/standards-01-original.md#f1--blocking-inherited-git-index-routing-writes-into-the-callers-index)
  through [Event06 repair/independent verification](../../reviews/M1-architecture-01-history.md#event06--independent-exact-source-repair-verification).
  The original staged-index damage is prevented before writes; both external
  agent/check writers and rejection are covered. No waiver or rollback substitutes
  for preservation. Historical ticket24's concern-to-repair trace remains in the
  [earlier guide](../m1-qa-01/qa-guide.md#human-checks-in-order).
- [Reviewer evaluation guidance/limits](../../../../.agents/skills/custom/evaluate-reviewers/SKILL.md#repository-evaluation-history)
  and [all final declared cases](../ticket-19/19-evaluation-g5/results.md) preserve
  G2/C5's five evolving corpora/two guidance versions, misses and invalid controls.
  This finite historical result is separate from current source review and future
  runtime delivery. Original historical Git object availability is disclosed in
  the cumulative report; inspected retained controls match preserved identities.
- [Refactor assessments 20–24](../../reviews/README.md), current cumulative report
  and prior finding history trace actual owners, writers, saved state, restore
  and invalidation; unresolved findings would hold readiness.
- Current-source [invalid-input observation](../m1-index-repair-01/completion-suite-observations/test_missing_acceptance_requirements_rejects_before_any_execution.json),
  [failed baseline](../m1-index-repair-01/baseline-observation.json),
  [canonical restored-source invalidation](../m1-index-repair-01/completion-suite-observations/test_continued_run_records_invalidation_of_earlier_verified_source.json),
  and [two-milestone exact/final-only test observation](../m1-index-repair-01/completion-suite-observations/test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision.json)
  retain actual behaviors at the frozen repaired source. The last uses scripted
  approvals as regression evidence, not actual human acceptance.
- Genuine pre-refactor checkpoint compatibility remains separately identified in
  [ticket24 completion](../ticket-24/24-completion.md). It is historical evidence,
  not a new execution attributed to this review round.

## Acceptance boundary

[ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md) requires
human acceptance of an exact tested milestone candidate. The approved
[M1 actions/pass conditions](../../milestones.md#m1-a-complete-qa-controlled-git-cycle)
require the promotion/final-only demonstration and actual human observations.
After those checks, record an explicit development M1 acceptance identifying the
source/manifest and completed observations. No such decision is inferred from
this guide, a test pass or a fixture approval. M2 remains ineligible.

Preserve the live demo's exact paths and frozen bytes while continuable. Its
[archive and digest](../m1-index-repair-01/qa-candidate/demo-archive.json) retain the
stopped checkpoint; historical temporary paths from earlier sessions are unrelated.
