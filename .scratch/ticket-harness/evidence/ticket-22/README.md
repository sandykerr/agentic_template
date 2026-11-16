# Ticket 22 evidence

[Completion](22-completion.md) · [Assessment](#review-assessment) · [Finding history](22-finding-history.md)

These originals preserve their recorded bytes and may embed historical paths. Use the [historical path map](../README.md#historical-paths) to locate moved evidence. Captured scripts retain their original execution assumptions and are not directly rerunnable from this layout.

## Review and verification

- Review originals: [22-review-spec-01.md](22-review-spec-01.md), [22-review-standards-01.md](22-review-standards-01.md)
- Review packets: [22-review-packet.md](22-review-packet.md)
- Criterion evidence: [22-criterion-evidence.md](22-criterion-evidence.md)
- Check records: [22-final-check-results.json](22-final-check-results.json)
- Source identities: [22-final-source.json](22-final-source.json)

## Retained folders

- [22-checkpoint](22-checkpoint/)
- [22-tools](22-tools/)

## Retired evidence

Recorded 2026-11-13.

Implementation `33fa0ea6e667a3879564ed4628c10f6d59ada21b`: 544 tests passed in 709.21s; all six required commands exited 0. The 26 frozen source files match available implementation Git blobs. Keep the [source identity](22-final-source.json), [command results](22-final-check-results.json), [source audit](22-root-source-audit.json), [completion](22-completion.md) and original reviews.

Under the human’s C1–C10 retention decisions and the root reviewer’s approval of this exact batch, removed 11 files totaling 5,678,066 bytes (C2, C5: routine command output, repeated synthetic fixture observations and resolved interruption detail as applicable). This retires historical detail; it does not renew verification, resolve the open M1 caller-index finding, accept M1 or change supported compatibility.

Genuine producer/consumer checkpoint folders remain intact. Source hashes identify code; available Git blobs preserve that code, while deleted historical output and temporary fixture identities cannot be reconstructed from hashes or a new execution. Historical originals may still name retired files and digests; those references are historical observations, not retrieval promises.

Removed files:

- `22-final-raw.tar.gz` (3,638,454 bytes)
- `22-raw-manifest.json` (1,361,239 bytes)
- `22-observation-index.json` (147,305 bytes)
- `22-final-check-0.log` (3,414 bytes)
- `22-final-check-1.log` (184 bytes)
- `22-final-check-2.log` (207 bytes)
- `22-final-check-3.log` (227 bytes)
- `22-final-check-4.log` (74 bytes)
- `22-final-check-5.log` (163 bytes)
- `22-focused-raw.tar.gz` (526,607 bytes)
- `22-focused.log` (192 bytes)

### Additional C1 cache retirement — 2026-11-13

Separate from the batch above, the root reviewer approved removal of 1 generated Python cache files totaling 5,712 bytes under C1. The historical capture tools are not in use; their authored source scripts remain. This removes regenerable bytecode without changing original source, results or the protected checkpoint/review evidence.

- `22-tools/__pycache__/capture22.cpython-312-pytest-9.2.0.pyc` (5,712 bytes)

## Review assessment

**review-ticket-22: completed.** Fixed original baseline: `803c6ff9a4e5e057124aefc5bb96f2c9518162dd`, captured before edits; existing unrelated changes preserved.
Assessed source(s): `33fa0ea6e667a3879564ed4628c10f6d59ada21b`, committed after final checks and before both fresh reviews.

The original reviews, captures and completion record linked above retain the
independent axes, instructions/settings, inspected/omitted scope and results.
Finding dispositions remain in [22-finding-history.md](22-finding-history.md).
This is the historical ticket assessment; current M1 acceptance is recorded in the
[review index](../../reviews/README.md), separately from ticket completion.

<details>
<summary>Historical assessment events (verbatim)</summary>

Copied from the retired `reviews/ticket-22.md`; relative links inside this
historical excerpt use that original location. Use the navigation above and the
[retired-wrapper map](../README.md#retired-review-wrappers) for current destinations.

```markdown

- A01 — `/root` captured the original baseline and preserved unrelated changes.
  Fresh Medium `/root/implement22` retained a genuine pre-edit deliberate checkpoint,
  implemented only the assigned slice and committed verified source at `33fa0ea`.
  [Checkpoint history](../evidence/ticket-22/22-checkpoint/history.md) preserves the initial
  pre-format continuation and final-source continuation from the genuine saved
  archive as separate observations.
- A02 — `/root` independently matched all 26 tested identities to committed Git
  blobs, all six required exits, all 10,446 raw files and genuine producer/final
  continuation evidence. Saved common/axis instructions and their identities before
  dispatching separate fresh High contexts on the same source and fixed baseline.
  Both originals pending; review lifecycle in progress.

- A03 — `/root/spec22` and `/root/standards22` independently saved clean original
  reports on the same committed source, excluding the current sibling report.
  Both traced actual owners/callers/writers/saved/restore/invalidation paths and
  independently confirmed all four No triggers. Spec additionally streamed all
  raw identities; Standards retained its reuse limits. Neither replayed tests.
- A04 — `/root` independently captured each original unchanged before combining
  hashes and aggregating; completed this assessment and reconciled all seven
  criteria separately. No repair, blocker waiver, source change, human decision
  or pending relevant revalidation. M1 cumulative work/human QA remain unperformed.
```

</details>
