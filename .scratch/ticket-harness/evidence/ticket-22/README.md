# Ticket 22 evidence

[Completion](22-completion.md) · [Assessment](../../reviews/ticket-22.md) · [Finding history](22-finding-history.md)

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
