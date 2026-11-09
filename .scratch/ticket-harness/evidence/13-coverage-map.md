# Ticket 13 coverage map

Fixed baseline: fd292a988cde79532bb84714b5800e4baa5de127.
Agreed seam: public CLI, external scripted processes, isolated real Git repositories,
and persisted report/Git artifacts. Use test-strategy and one-slice TDD.

- Existing milestone two-group/single-final tests: extend success expectations to
  exact candidate/QA request, preserve ticket gates, immutable inputs/caller work,
  later Pending/zero attempts, false feature completion and observational status.
- New passing divergent-development scenario: candidate contains development-only
  changes and completed feature work; current dev base is captured at preparation.
- New rejected milestone regression: ticket candidates pass, milestone gate fails;
  Done remains Done, no request, dev unchanged, retained gate evidence.
- External development/feature movement during milestone regression: preserve
  external refs, reject QA readiness with exact stale identities retained.
- Candidate/earlier verified source mutation: invalidate approvals, preserve source,
  no request. Reuse transaction suite for existing per-ticket mutations/repairs.
- Real unresolved conflict and source-changing merge-driver/hook resolutions:
  stop with renewal required, preserve tree/diagnostics, no QA request or ref write.
  Automatic conflict repair is outside this slice; no renewed review is claimed.

Focused iteration: tests/test_milestones.py plus relevant transaction/dependency
cases. Final required: full pytest, strict mypy, Ruff lint/format, git diff --check.
No packaging/entry-point changes planned. Capture actual commands/exits and hashes
before execution, and scenario observations during required runs.

## Final coverage ownership

`tests/test_milestones.py` extends the existing two-group success case rather than
retaining a duplicate happy-path case. It now verifies the full request identity,
passing exact regression evidence and separate ticket gates while preserving dirty
caller work. The existing single-final-group case proves all Done still waits.
Ten added cases cover merge-hook changes (1), failed milestone regression (1),
external feature/development movement (2), candidate/prior-source mutation (2),
changed development with a clean same-file merge (1), unresolved/custom-driver
conflict source (2), and already-contained feature regression/QA (1). The last
case protects the no-new-merge candidate branch. Existing transaction, dependency,
repair, report and timeout suites retain ownership of shared per-ticket behavior.

The check helper captures source/test/document/config hashes and git status before
execution, sets command-local `PYTHONPATH=/tmp/ticket12-tools`, and saves actual
command/exit/time and unmodified output. Each run has its own observation folder;
only `13-observations/renewed-final-suite` is final full-suite evidence. Temporary fixture
repositories are cleaned after retaining their record, CLI, Git, assignment and
output observations; milestone fixtures additionally retain QA requests and
candidate source/status/history.

The already-contained feature case also observes the durable report from inside
its scripted regression process, asserting `outcome: preparing_milestone` and
milestone state `preparing` before QA. This caught and fixed a transient false
completed outcome through red/green behavior. The initial interrupted full run
is historical; only `13-observations/renewed-final-suite` supplies final scenarios.
