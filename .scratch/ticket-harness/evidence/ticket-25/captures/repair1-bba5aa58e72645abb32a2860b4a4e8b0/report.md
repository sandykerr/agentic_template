# Ticket 25 bounded repair 1

Worker: `/root/repair25_1`. Rejected source:
`3b0c1ab7ec41929d3febab44269f791e55897e70`. Original baseline remains
`2c01fe9fe04c78fa10a2dac11e94826876467562`.
Assignment: [25-repair1-assignment.md](25-repair1-assignment.md).
Original reports and all five distinct finding keys remain preserved in
[the canonical history](25-finding-history.md) and
[evidence index](25-evidence-index.md).

Requested settings: GPT-6.1 Sol, Medium, active-context target <=250000.
Backend enforcement and measured model/reasoning/context telemetry are unavailable;
these are requested settings rather than an assertion of measured delivery.

## Scope and ownership

Only `ticket_harness/evidence.py`, `tests/test_evidence.py` and this repair report
are in this worker's edit scope. `CaptureStore` continues to own allocation,
capture metadata, scope routing and registration integrity under the existing
feature evidence-directory lock. Producers retain their payload-only ownership;
the helper preserves review/approval/execution namespaces and unknown fields.
Receipts, schema, protected paths, atomic replacement, partial-write failure
behavior and runtime run/attempt/QA owners remain unchanged. No ADR conflict or
unresolved human decision is identified by these owner-local corrections.

All four ticket architecture triggers remain YES: capture lifecycle, durable
receipts/JSON, shared mutable metadata and a helper writer. The repair adds no
new owner or writer. Fresh relevant broader assessment and whole-ticket Spec and
Standards reviews remain required; worker checks cannot resolve finding keys.

## Coverage map and TDD

The approved seam is the existing public subprocess CLI with disposable real Git
repositories and observable files/JSON. No internal mocks or new seams are added.

| Failure or invariant | Coverage |
| --- | --- |
| Supplied empty shared or milestone names must fail before output creation | Extend `test_ambiguous_or_unsafe_scope_never_allocates_output` with two demonstrated accepted-input counterexamples; existing assertion requires absent evidence root |
| Valid ticket/shared/milestone destinations and references | Existing ticket capture and shared milestone tests |
| Later registered original must be validated on identical earlier retry | New A/B registration, mutate B, retry identical A regression, requiring nonzero diagnostic and byte-identical authoritative artifact |
| Healthy retry, original identity, no overwrite, metadata mismatch | Existing derived-summary/idempotence and changed-original/metadata tests |
| Locking, namespace preservation, protected paths and malformed metadata | Existing focused evidence suite |

Execution is delegated serially to the parent through retained Forest203 x86_64
PTY10089, checkout-local `.venv/bin/python`, executable `/dev/shm` temporary
storage and one-thread limits. This worker ran no Python, tests, or SSH workload
on adaptlogin202 and opened no new compute session.

## Actual checks

The parent's allocated check destination is
[repair1-bba5aa58e72645abb32a2860b4a4e8b0](captures/repair1-bba5aa58e72645abb32a2860b4a4e8b0/allocation.json).
Its per-stage outputs retain source snapshots, stdout/stderr and exit results.

1. Scope red: `.venv/bin/python -m pytest -q tests/test_evidence.py -k ambiguous_or_unsafe_scope_never_allocates_output`.
   Parent observed exit 1, **2 failed / 6 passed / 17 deselected in 1.18s**.
   The two failures were the empty shared and milestone arguments; product source
   was unchanged from the rejected checkpoint. Retained output: `scope-red.*`.
   Only after receiving that actual red result did this worker change allocation:
   `shared is not None` selects validation/routing/linking, and
   `milestone is not None` selects milestone validation/routing. Supplied empty
   values therefore reach `_slug` before evidence ownership creates output.
2. Scope green: `.venv/bin/python -m pytest -q tests/test_evidence.py -k 'ambiguous_or_unsafe_scope_never_allocates_output or ticket_capture_records_actual_file_and_provenance or shared_milestone_has_one_record_referenced_by_each_ticket'`.
   Parent observed exit 0, **10 passed / 15 deselected in 1.47s**.
   Retained output: `scope-green.*`. This includes valid ticket/shared milestone
   routing and both new prewrite rejection cases.
3. Retry red: `.venv/bin/python -m pytest -q tests/test_evidence.py -k identical_retry_rejects_changed_later_registered_original`.
   Parent observed exit 1, **1 failed / 25 deselected in 1.12s**. The failure
   was the earlier A retry unexpectedly returning CLI exit 0 after registered B
   changed. Retained output: `retry-red.*`; registration source was unchanged.
   Only after that actual result did this worker finish the existing identity
   validation loop before a second matching-ID/metadata/idempotence loop. Both
   stay under the same existing lock and before any artifact append/save.

4. Capture-family green: `.venv/bin/python -m pytest -q tests/test_evidence.py`.
   Parent observed exit 0, **26 passed in 6.03s**. The new retry rejection and
   unchanged-artifact assertion pass, alongside healthy retry, metadata mismatch,
   concurrency, original/derived, protected-path and malformed-record coverage.
5. Parent observed exit 0 for every relevant static check on this repaired source:
   `.venv/bin/python -m mypy`;
   `.venv/bin/python -m ruff check ticket_harness/evidence.py tests/test_evidence.py`;
   `.venv/bin/python -m ruff format --check ticket_harness/evidence.py tests/test_evidence.py`;
   `git diff --check`.

## Handoff and remaining gates

Product edits are frozen after the successful focused/static checks. The final
diff adds consistent optional-name presence checks before allocation writes and
completes prior-file identity validation before matching-ID success. Tests add
two invalid-scope parameter cases and one later-original retry case. Existing
evidence, planning edits, original reports/probes and finding history were not
modified by this worker.

The parent owns final-source full suite, required repository-wide static checks,
installed wheel/CLI gates and source binding, repair checkpoint commit and fresh
independent whole-ticket Spec/Standards plus relevant renewed broader assessment.
Those gates are pending at this handoff; the earlier checkpoint's full-suite pass
does not verify this new repair. No full finding key is dispositioned fixed here,
and no ticket completion, integration readiness, EC1 acceptance or QA decision is
claimed. Register this completed report through the parent-owned capture workflow;
preserve this report and raw red/green observations as originals.
