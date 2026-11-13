# Ticket 21 evidence

[Completion](21-completion.md) · [Assessment](../../reviews/ticket-21.md) · [Finding history](21-finding-history.md)

These originals preserve their recorded bytes and may embed historical paths. Use the [historical path map](../README.md#historical-paths) to locate moved evidence. Captured scripts retain their original execution assumptions and are not directly rerunnable from this layout.

## Review and verification

- Review originals: [21-review-spec-01.md](21-review-spec-01.md), [21-review-standards-01.md](21-review-standards-01.md)
- Review packets: [21-review-packet.md](21-review-packet.md)
- Criterion evidence: [21-criterion-evidence.md](21-criterion-evidence.md)
- Check records: [21-final-check-results.json](21-final-check-results.json)
- Source identities: [21-final-source.json](21-final-source.json)

## Retained folders

- [21-checkpoint](21-checkpoint/)
- [21-tools](21-tools/)

## Retired evidence

Recorded 2026-11-13.

Implementation `10b7050ec1fc06767e473b90217fa0d0bd100a0f`: 544 tests passed in 775.37s; all six required commands exited 0. The 26 frozen source files match available implementation Git blobs. Keep the [source identity](21-final-source.json), [command results](21-final-check-results.json), [completion](21-completion.md) and original reviews.

Under the human’s C1–C10 retention decisions and the root reviewer’s approval of this exact batch, removed 11 files totaling 6,001,913 bytes (C2, C5: routine command output, repeated synthetic fixture observations and resolved interruption detail as applicable). This retires historical detail; it does not renew verification, resolve the open M1 caller-index finding, accept M1 or change supported compatibility.

Genuine producer/consumer checkpoint folders remain intact. Source hashes identify code; available Git blobs preserve that code, while deleted historical output and temporary fixture identities cannot be reconstructed from hashes or a new execution. Historical originals may still name retired files and digests; those references are historical observations, not retrieval promises.

Removed files:

- `21-final-raw.tar.gz` (3,641,884 bytes)
- `21-raw-manifest.json` (1,361,108 bytes)
- `21-observation-index.json` (147,305 bytes)
- `21-final-check-0.log` (3,354 bytes)
- `21-final-check-1.log` (184 bytes)
- `21-final-check-2.log` (207 bytes)
- `21-final-check-3.log` (227 bytes)
- `21-final-check-4.log` (74 bytes)
- `21-final-check-5.log` (163 bytes)
- `21-focused-raw.tar.gz` (847,135 bytes)
- `21-focused.log` (272 bytes)

### Additional C1 cache retirement — 2026-11-13

Separate from the batch above, the root reviewer approved removal of 1 generated Python cache files totaling 5,712 bytes under C1. The historical capture tools are not in use; their authored source scripts remain. This removes regenerable bytecode without changing original source, results or the protected checkpoint/review evidence.

- `21-tools/__pycache__/capture21.cpython-312-pytest-9.2.0.pyc` (5,712 bytes)
