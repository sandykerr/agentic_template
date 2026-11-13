# Ticket 14 Standards review

Baseline: `d67c12d91495af00557b279d0bf0e1da518e6fcc`.
Reviewed HEAD: `29fb5569cf53c75bd351d6bd176bb29889c42a65`.
Diff: `git diff d67c12d91495af00557b279d0bf0e1da518e6fcc...HEAD`.
Commit: `29fb556 Consume exact milestone QA decisions before promotion`.

**Result: 0 blockers; 1 optional suggestion.** Independent Standards review;
the Spec review was not read.

Documented-standard violations: none found. Applied AGENTS.md, domain/testing/
environment/tracker guidance, GLOSSARY.md, ADR-0001/0002, the approved spec's
cohesive responsibilities, exact-revision and testing/design guidance, scoped
ticket 14/R05, and custom test-strategy. Existing functions and cohesive modules
remain appropriate; the approved CLI/external-process/real-Git seam is preserved.
Restart ownership and later OS/backend boundaries are outside this slice.

Optional possible **Duplicated Code**, `tests/test_milestones.py:78–108`:
both `wait_for` and `run_until_wait` repeat
`deadline = time.monotonic() + 45`, the run-record existence/read loop,
`process.poll()` handling, and `time.sleep(0.025)`. Consider sharing the polling
mechanics while preserving their different early-exit/result semantics. Future
deadline, polling, or diagnostics changes currently need two edits and could
drift. This is a maintenance preference, not a documented-standard breach or
integration blocker.

Coverage assessment: the map identifies distinct approval, role/attempt, ref,
source/input/evidence and eligibility failures. The invalid-input sequence shares
one fixture without multiplying equivalent repositories. Shared builders retain
isolated writable repositories; foreground cleanup captures descendants and reaps
the owned runner. No redundant combination warrants removal.

Independent evidence audit: all 21 captured file SHA-256 values match committed
HEAD and current bytes; all five final gate captures share that map and exit 0.
Read actual logs: **524 passed in 684.03s**, strict mypy, Ruff lint/format, and
whitespace passed. Independently reran committed-diff whitespace (exit 0), without
replaying the suite. Inspected 103 retained raw scenario records; audited both
consumed decision hashes, first-promotion/next-worker alignment, final promotion,
and all nine QA-time rejection outcomes against actual retained JSON. Historical
precommit HEAD metadata is preserved; matching content hashes establish provenance.
The unrelated tracker retains SHA-256
`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.
