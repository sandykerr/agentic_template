# Ticket 24 evidence

[Completion](24-completion.md) · [Assessment](../../reviews/ticket-24.md) · [Finding history](24-finding-history.md)

These originals preserve their recorded bytes and may embed historical paths. Use the [historical path map](../README.md#historical-paths) to locate moved evidence. Captured scripts retain their original execution assumptions and are not directly rerunnable from this layout.

## Review and verification

- Review originals: [24-review-spec-01.md](24-review-spec-01.md), [24-review-spec-02.md](24-review-spec-02.md), [24-review-spec-03.md](24-review-spec-03.md), [24-review-standards-01.md](24-review-standards-01.md), [24-review-standards-02.md](24-review-standards-02.md), [24-review-standards-03.md](24-review-standards-03.md)
- Review packets: [24-repair1-review-packet.md](24-repair1-review-packet.md), [24-repair2-review-packet.md](24-repair2-review-packet.md), [24-resume-review-packet.md](24-resume-review-packet.md), [24-review-packet.md](24-review-packet.md)
- Check records: [24-final-check-results.json](24-final-check-results.json), [24-focused-check-results.json](24-focused-check-results.json), [24-repair1-final-check-results.json](24-repair1-final-check-results.json), [24-repair2-resumed-repaired-final-check-results.json](24-repair2-resumed-repaired-final-check-results.json)
- Source identities: [24-final-source.json](24-final-source.json), [24-repair1-final-source.json](24-repair1-final-source.json), [24-repair2-final-source.json](24-repair2-final-source.json), [24-repair2-resumed-final-source.json](24-repair2-resumed-final-source.json), [24-repair2-resumed-repaired-final-source.json](24-repair2-resumed-repaired-final-source.json)

## Retained folders

- [24-checkpoint](24-checkpoint/)
- [24-repair1-checkpoint](24-repair1-checkpoint/)
- [24-repair1-tools](24-repair1-tools/)
- [24-repair2-checkpoint](24-repair2-checkpoint/)
- [24-repair2-tools](24-repair2-tools/)
- [24-resume-checkpoint](24-resume-checkpoint/)
- [24-tools](24-tools/)

## Retired evidence

Recorded 2026-11-13.

Final implementation `ab08f7f03b5248709cdde3f5a65e4f632b8198b4`: 559 tests passed in 1284.57s; all six required commands exited 0. The 27 frozen source files match available implementation Git blobs. Keep the [final source identity](24-repair2-resumed-repaired-final-source.json), [final command results](24-repair2-resumed-repaired-final-check-results.json), [committed-source binding](24-repair2-resumed-repaired-final-committed-source.json), [completion](24-completion.md), original reviews and [full finding history](24-finding-history.md). Earlier 544/556 campaigns retain separate [initial source](24-final-source.json)/[results](24-final-check-results.json) and [repair1 source](24-repair1-final-source.json)/[results](24-repair1-final-check-results.json). User-halted repair2 sessions exited 130 incomplete; [interruption](24-repair2-interruption.json), [progress](24-repair2-progress.json) and [diagnosis](24-resume-diagnosis.md) preserve their limits. These are separate from the later complete final suite.

Under the human’s C1–C10 retention decisions and the root reviewer’s approval of this exact batch, removed 35 files totaling 23,458,658 bytes (C2, C3, C5: routine command output, repeated synthetic fixture observations and resolved interruption detail as applicable). This retires historical detail; it does not renew verification, resolve the open M1 caller-index finding, accept M1 or change supported compatibility.

Genuine producer/consumer checkpoint folders remain intact. Source hashes identify code; available Git blobs preserve that code, while deleted historical output and temporary fixture identities cannot be reconstructed from hashes or a new execution. Historical originals may still name retired files and digests; those references are historical observations, not retrieval promises.

The distinct resumed 246-case failed campaign remains protected, including `24-resume-interrupted-failed-raw.tar.gz`, its manifest, index and audit: historical exit 120 remains unexplained. Targeted red/green trials, observer diagnosis, differing original reviewer judgments, immutable-original/display mappings and the genuine old-producer/current-consumer checkpoints remain available for the named M1 QA concern-to-fix and compatibility examples. The open M1 F1 reproduction, instructions and current correction source remain in the separate M1 bundles.

Removed files:

- `24-final-raw.tar.gz` (3,968,518 bytes)
- `24-raw-manifest.json` (1,743,911 bytes)
- `24-observation-index.json` (213,635 bytes)
- `24-final-check-0.log` (3,213 bytes)
- `24-final-check-1.log` (44 bytes)
- `24-final-check-2.log` (19 bytes)
- `24-final-check-3.log` (27 bytes)
- `24-final-check-4.log` (0 bytes)
- `24-final-check-5.log` (0 bytes)
- `24-repair1-final-raw.tar.gz` (4,196,605 bytes)
- `24-repair1-raw-manifest.json` (1,818,796 bytes)
- `24-repair1-observation-index.json` (217,896 bytes)
- `24-repair1-final-check-0.log` (3,211 bytes)
- `24-repair1-final-check-1.log` (44 bytes)
- `24-repair1-final-check-2.log` (19 bytes)
- `24-repair1-final-check-3.log` (27 bytes)
- `24-repair1-final-check-4.log` (0 bytes)
- `24-repair1-final-check-5.log` (0 bytes)
- `24-repair2-resumed-repaired-final-raw.tar.gz` (4,253,135 bytes)
- `24-repair2-resumed-repaired-final-manifest.json` (1,838,672 bytes)
- `24-repair2-resumed-repaired-final-index.json` (218,554 bytes)
- `24-repair2-resumed-repaired-final-check-0.log` (3,190 bytes)
- `24-repair2-resumed-repaired-final-check-1.log` (44 bytes)
- `24-repair2-resumed-repaired-final-check-2.log` (19 bytes)
- `24-repair2-resumed-repaired-final-check-3.log` (27 bytes)
- `24-repair2-resumed-repaired-final-check-4.log` (0 bytes)
- `24-repair2-resumed-repaired-final-check-5.log` (0 bytes)
- `24-repair2-resumed-repaired-final-pytest-reports.jsonl` (344,375 bytes)
- `24-repair2-interrupted-final-raw.tar.gz` (1,957,772 bytes)
- `24-repair2-interrupted-final-manifest.json` (806,301 bytes)
- `24-repair2-interrupted-final-index.json` (52,146 bytes)
- `24-repair2-focused-raw.tar.gz` (1,303,690 bytes)
- `24-repair2-focused-raw-audit.json` (514,424 bytes)
- `24-repair2-final-check-0.log` (249 bytes)
- `24-repair2-focused-check-0.log` (95 bytes)

### Additional C1 cache retirement — 2026-11-13

Separate from the batch above, the root reviewer approved removal of 6 generated Python cache files totaling 23,300 bytes under C1. The historical capture tools are not in use; their authored source scripts remain. This removes regenerable bytecode without changing original source, results or the protected checkpoint/review evidence.

- `24-tools/__pycache__/capture24.cpython-312-pytest-9.2.0.pyc` (5,712 bytes)
- `24-repair1-tools/__pycache__/capture24repair1.cpython-312-pytest-9.2.0.pyc` (5,735 bytes)
- `24-repair2-tools/__pycache__/delay24resume.cpython-312-pytest-9.2.0.pyc` (2,045 bytes)
- `24-repair2-tools/__pycache__/capture24repair2.cpython-312-pytest-9.2.0.pyc` (5,735 bytes)
- `24-repair2-tools/__pycache__/delay24observerentry.cpython-312-pytest-9.2.0.pyc` (2,597 bytes)
- `24-repair2-tools/__pycache__/result24resume.cpython-312-pytest-9.2.0.pyc` (1,476 bytes)
