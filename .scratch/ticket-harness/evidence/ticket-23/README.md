# Ticket 23 evidence

[Completion](23-completion.md) · [Assessment](#review-assessment) · [Finding history](23-finding-history.md)

These originals preserve their recorded bytes and may embed historical paths. Use the [historical path map](../README.md#historical-paths) to locate moved evidence. Captured scripts retain their original execution assumptions and are not directly rerunnable from this layout.

## Review and verification

- Review originals: [23-review-spec-01.md](23-review-spec-01.md), [23-review-standards-01.md](23-review-standards-01.md)
- Review packets: [23-review-packet.md](23-review-packet.md)
- Criterion evidence: [23-criterion-evidence.md](23-criterion-evidence.md)
- Check records: [23-final-check-results.json](23-final-check-results.json)
- Source identities: [23-final-source.json](23-final-source.json)

## Retained folders

- [23-checkpoint](23-checkpoint/)
- [23-interrupted](23-interrupted/)
- [23-tools](23-tools/)

## Retired evidence

Recorded 2026-11-13.

Implementation `8b1b37becb544299e8981144e4ad56da42e2d45f`: 544 tests passed in 706.22s (wrapper 706.58s). The 26 frozen source files match available implementation Git blobs. Keep the [source identity](23-final-source.json), [successful suite result](23-final-suite-result.json), [other command results](23-final-check-results.json), [completion](23-completion.md) and original reviews. The initial capture import exited 3 before collection; user-interrupted invocations had no final summary or known exit, and no pass is inferred. The [interruption record](23-interrupted/interruption.json) survives.

Under the human’s C1–C10 retention decisions and the root reviewer’s approval of this exact batch, removed 13 files totaling 6,260,400 bytes (C2, C3, C5: routine command output, repeated synthetic fixture observations and resolved interruption detail as applicable). This retires historical detail; it does not renew verification, resolve the open M1 caller-index finding, accept M1 or change supported compatibility.

Genuine producer/consumer checkpoint folders remain intact. Source hashes identify code; available Git blobs preserve that code, while deleted historical output and temporary fixture identities cannot be reconstructed from hashes or a new execution. Historical originals may still name retired files and digests; those references are historical observations, not retrieval promises.

Removed files:

- `23-final-raw.tar.gz` (3,977,366 bytes)
- `23-raw-manifest.json` (1,743,911 bytes)
- `23-observation-index.json` (213,635 bytes)
- `23-final-check-0.log` (1,922 bytes)
- `23-final-check-1.log` (44 bytes)
- `23-final-check-2.log` (19 bytes)
- `23-final-check-3.log` (27 bytes)
- `23-final-check-4.log` (0 bytes)
- `23-final-check-5.log` (0 bytes)
- `23-interrupted/raw.tar.gz` (320,108 bytes)
- `23-interrupted/23-focused.log` (142 bytes)
- `23-interrupted/23-final-suite.log` (19 bytes)
- `23-final-suite.log` (3,207 bytes)

### Additional C1 cache retirement — 2026-11-13

Separate from the batch above, the root reviewer approved removal of 1 generated Python cache files totaling 5,712 bytes under C1. The historical capture tools are not in use; their authored source scripts remain. This removes regenerable bytecode without changing original source, results or the protected checkpoint/review evidence.

- `23-tools/__pycache__/capture23.cpython-312-pytest-9.2.0.pyc` (5,712 bytes)

## Review assessment

**review-ticket-23: completed.** Fixed original baseline: `851a855889b1ec99ae78ce415da1d66a3cf06687`, captured before edits; unrelated worktree changes preserved.
Assessed source(s): `8b1b37becb544299e8981144e4ad56da42e2d45f`, committed after final checks and before both independent source reviews.

The original reviews, captures and completion record linked above retain the
independent axes, instructions/settings, inspected/omitted scope and results.
Finding dispositions remain in [23-finding-history.md](23-finding-history.md).
This is the historical ticket assessment; current M1 acceptance is recorded in the
[review index](../../reviews/README.md), separately from ticket completion.

<details>
<summary>Historical assessment events (verbatim)</summary>

Copied from the retired `reviews/ticket-23.md`; relative links inside this
historical excerpt use that original location. Use the navigation above and the
[retired-wrapper map](../README.md#retired-review-wrappers) for current destinations.

```markdown

- A01 — Root captured `851a855` as fixed original baseline and preserved unrelated
  edits. Fresh Medium worker produced a genuine pre-edit stopped checkpoint and
  implemented the bounded lifecycle migration. User interruption ended incomplete
  test runs; originals remain retained without a pass.
- A02 — Fresh Medium resumed assignment verified unchanged executable source,
  retained interrupted evidence and completed the full 544-test final-source suite,
  static/whitespace checks and archive/compatibility audit. Committed8b1b37b before
  review. Root independently matched26 committed identities,10,446 files and 544
  scenario entries, plus genuine baseline/consumer identities and preserved work.
- A03 — Root captured common/axis instruction identities and dispatched separate
  fresh High contexts on the same source/baseline. Each traced actual changed and
  unchanged collaborators and saved its original before aggregation, excluding
  its current sibling report. Both independently assessed all four triggers No.
- A04 — Root captured originals unchanged, read and aggregated both clean results,
  completed this assessment and reconciled all seven criteria separately. No code
  change, repair, blocker waiver, human decision or pending revalidation. Real M1
  cumulative work and human QA remain unperformed.
```

</details>
