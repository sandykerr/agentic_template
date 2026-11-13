# Ticket 14 development provenance

Fixed review baseline: d67c12d91495af00557b279d0bf0e1da518e6fcc.
Root separately audited ticket 13 prerequisites; [14-prerequisite-audit.json](14-prerequisite-audit.json) is root-owned.
The unrelated docs/agents/issue-tracker.md bytes remain unchanged and unstaged.

Applied implement-with-checkboxes/upstream implement, test-strategy and TDD with
all mandated references. Parent owns independent reviews, completion bookkeeping
and next handoff. No other development ticket or real human QA was executed.

- Red 1: foreground two-milestone CLI scenario failed because the old runner exited
  after preparing M1 rather than observing decisions. Green 1 implemented strict
  separate authority, exact acceptance, atomic two-ref promotion/alignment and
  continuation; 1 passed in 23.65s. Both exact commands/exits/source hashes retained.
- Red 2: malformed decision directory ended the run. Green 2: unreadable/missing
  artifacts remain indefinite observable waits; 1 passed in 7.75s. Same scenario
  exercises malformed/incidental/duplicate/mismatched approval values and waiting
  longer than every configured agent/check timeout without new attempts.
- Focused 1: 55 milestone/QA cases passed in 133.73s. Later cleanup/type/FIFO/public-doc
  edits mean this is development evidence; final gates establish final source.
- Red 3: a FIFO decision blocked watcher reads and left missing status. Green 3:
  regular-file validation reports unreadable without reading FIFO; 1 passed in 9.69s.
  The scenario also rejects boolean exit_code replacing numeric zero.
- Focused strict mypy and Ruff lint passed. [Tool verification](14-tooling.json) retains actual versions,
  including a failed standalone mypy launcher probe and corrected documented
  module invocation using PYTHONPATH=/tmp/ticket12-tools. No shared environment
  installation/change was made.

Final full-suite and static commands capture fresh source/test hashes and retained
raw observations through [14-check.py](14-check.py); only `14-final-*` establish final verification.
Packaging/entrypoints are unchanged, so installed packaging checks are inapplicable.

Preparation scenarios intentionally terminate/reap an active foreground wait after
reading actual status. Their run termination is retained separately from successful
status exit. Fixture-owned process-group descendants are cleaned on bounded failure.
This is not supported runtime stop/restart behavior; ticket 15 owns that contract.

Final suite: **524 passed in 684.03s**, exit 0 (wrapper 684.962s).
Final strict mypy, Ruff lint/format and whitespace all passed; all five final
captures match the committed/current 21-file hash map. See [actual checks](14-check-results.json)
and [worker identity/consolidation audit](14-worker-check-audit.json).

Initial staging failed on the read-only .git sandbox mount. Automatic permission
review for narrow git add timed out once, explicitly permitting a retry; the retry
succeeded. The initial staged-whitespace capture inspected an empty index and is
not used for verification. Renewed staged whitespace and original-baseline committed
diff whitespace both passed. Only the seven implementation/test/public-guide paths
were committed; the unrelated tracker and all evidence remain outside that checkpoint.
