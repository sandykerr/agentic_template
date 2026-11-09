# Ticket 14 implementation checkpoint report

Scope: foreground QA-decision watching/consumption/promotion/next-group cycle.
Baseline: d67c12d91495af00557b279d0bf0e1da518e6fcc.
Implementation commit: `29fb5569cf53c75bd351d6bd176bb29889c42a65`.
No development milestone QA acceptance is claimed.

## Behavior

- `runner.py` executes fixed groups in order, retaining the existing complete
  per-ticket lifecycle. Successful preparation publishes an exact QA request and
  remains active indefinitely. Later tickets stay Pending at attempt zero.
- `qa-decision.json` is separate from approved inputs and worktrees. Only exactly
  `decision: APPROVED` and a complete strictly JSON-equal current `request` object
  can authorize consumption. Missing/unreadable artifacts and invalid content
  remain observable waits. Regular-file checking avoids blocking on FIFO artifacts.
- Distinct read decision bytes/hash/request identity and rejection diagnostics are
  retained; consumed decision artifacts remain durable and protected. A previous
  group's decision cannot accept the next group's unique request. Worker/repair
  processes cannot write QA authority without failing protected-path integrity.
- Acceptance revalidates captured sources/snapshots, all applicable verified source
  worktrees, original request bytes and retained actual evidence bytes. Stale
  source/request/evidence stops for renewed checks and acceptance.
- `git.py` uses one expected-old `update-ref --stdin` transaction for dev and feature,
  disables hooks and rejects either checked-out branch. Either tip mismatch leaves
  both refs untouched. Both refs become the exact tested candidate before a later
  worker starts. Current branch movement while tickets execute remains included
  in the next freshly tested development candidate.
- Only final accepted promotion sets feature_complete true/completed. All Done
  while final acceptance waits remains awaiting_human_qa/false. QA waiting uses no
  ticket attempts/repairs or configured process timeout.
- `inputs.py` validates readiness and prerequisites for every required ticket
  before execution, preserving the legacy selected-only plan-free contract.
- Public docs describe current foreground operation, exact decision schema,
  observable records, stale-state rejection and deferred planned restart.

## Verification evidence

See [the coverage map](14-coverage-map.md) for old/new requirement coverage at the approved public seam.
See [development provenance](14-development-notes.md) for incremental red/green commands and historical checks.
All actual commands/exits/logs/source hashes are `14-*-result.json`, `.log` and `-source.json`.
The full suite passed **524 tests in 684.03s** (wrapper 684.962s).
[Actual final checks](14-check-results.json), [logs](14-checks.log),
[committed source identity](14-final-source-identity.json) and
[103 consolidated observations](14-fixture-observations.json) retain verification.
Only `14-final-*` establish the final implementation's required checks; final-suite
was started after all executable/test/public-guide changes. Final strict mypy,
Ruff lint/format and whitespace pass with identical 21-file source maps.

Raw observations: [14-observations/final-suite/](14-observations/final-suite/). New QA scenarios preserve actual
foreground commands/exits/output or explicit fixture termination, status reads,
Git refs/history, role launches/assignments, gate outputs and request/decision bytes.
The main two-group scenario consumes two decisions, rejects stale candidate and
replay, observes later worker base after alignment and completes only on final
acceptance. Other cases reject changed refs/source/input/request/log evidence,
checked-out branches, worker/repair authority writes and later-group ineligibility.

Packaging and entrypoint files did not change; packaging checks are not required.
The unrelated tracker edit remains untouched and is excluded from staging.

## Limits

Ticket 15 owns supported planned stop/restart/continuation and ownership locking.
Arbitrary interruption recovery, background operation, real human QA, QA session
skills/corrections, live backend/profile enforcement and OS role enforcement remain
outside this ticket. The decision artifacts here are isolated scripted fixture
acceptances and never accept this repository's development milestone.

No automatic regeneration/review repair is attempted after stale state or
source-changing conflict resolution: retained evidence and explicit renewed gates
remain required. Protection continues the existing trusted-process boundary;
it does not claim an OS sandbox or arbitrary hostile concurrent-writer guarantees.
Parent owns independent Spec/Standards review and completion/handoff bookkeeping.
