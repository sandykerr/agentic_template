# Ticket 13 evidence

Current links below identify retained records. Original reports remain byte-identical historical accounts; paths in them may name deliberately retired payloads. See the [historical path guide](../README.md#historical-paths).

## Retained results

- [13-check-results.json](13-check-results.json)
- [13-completion.md](13-completion.md)
- [13-coverage-map.md](13-coverage-map.md)
- [13-development-notes.md](13-development-notes.md)
- [13-final-source-identity.json](13-final-source-identity.json)
- [13-scenario-results.json](13-scenario-results.json)
- [13-implementation-report.md](13-implementation-report.md)
- [13-review-spec.md](13-review-spec.md)
- [13-review-standards.md](13-review-standards.md)
- [13-root-audit.json](13-root-audit.json)

## Useful verification conclusions

Verified implementation: `19ea4f1b0bbdc601653468212aaaa0a7211d5c6f`.
Original fixed review baseline: `fd292a988cde79532bb84714b5800e4baa5de127`.

- Only renewed-final captures verify final 19ea4f1 source; 509 tests passed. Preserve preparation-state explanation, current final result map and source identity; earlier/interrupted attempts are superseded.

Recorded command results, copied from the retained completion account:

| Command or check | Historical result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **509 passed in 795.92s**; wrapper elapsed 796.788s. |
| Reusable Python `-m mypy` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples` | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples` | Exit 0: 20 files formatted. |
| `git diff --check`; committed original-baseline diff whitespace | Exit 0. |

## Retired evidence

On 2026-11-13, the human explicitly requested retroactive retirement under the agreed [C1–C10 decisions](../evidence-retention-audit-01/retention-decisions.md); the overseer approved this exact ticket batch. Useful results and identities were recorded before deletion. No replacement archive of discarded payloads was created.

Discarded **21 files / 93,188 logical bytes**:

- C2 routine command output; C3 resolved development failures: 20 files / 51,073 bytes.
- C2/C3 duplicated original command-output payload: 1 files / 42,115 bytes.

Routine stdout, repeated synthetic run trees and resolved development-failure detail are intentionally unavailable where selected. Completion, original independent reviews, source identities, structured result records and the linked retained scenario/audit conclusions survive. Original records may contain historical hashes or links to retired files; those hashes no longer imply that a complete original raw audit can be repeated. Preserved scripts document historical work and must not be run as current validators.

This retirement changes retained detail, not implementation verification or approval. No harness or tests were run. Development M1 remains unaccepted; `review-M1-architecture-01/standards-01/F1` remains open, and its independent proof and current QA material remain in the separate protected M1 bundles.

<details>
<summary>Other retained original files</summary>

- [13-check.py](13-check.py)
- [13-consolidate.py](13-consolidate.py)
- [13-final-format-result.json](13-final-format-result.json)
- [13-final-format-source.json](13-final-format-source.json)
- [13-final-lint-result.json](13-final-lint-result.json)
- [13-final-lint-source.json](13-final-lint-source.json)
- [13-final-mypy-result.json](13-final-mypy-result.json)
- [13-final-mypy-source.json](13-final-mypy-source.json)
- [13-final-whitespace-result.json](13-final-whitespace-result.json)
- [13-final-whitespace-source.json](13-final-whitespace-source.json)
- [13-focused-1-result.json](13-focused-1-result.json)
- [13-focused-1-source.json](13-focused-1-source.json)
- [13-focused-2-result.json](13-focused-2-result.json)
- [13-focused-2-source.json](13-focused-2-source.json)
- [13-focused-3-result.json](13-focused-3-result.json)
- [13-focused-3-source.json](13-focused-3-source.json)
- [13-focused-4-result.json](13-focused-4-result.json)
- [13-focused-4-source.json](13-focused-4-source.json)
- [13-green-1-result.json](13-green-1-result.json)
- [13-green-1-source.json](13-green-1-source.json)
- [13-green-2-result.json](13-green-2-result.json)
- [13-green-2-source.json](13-green-2-source.json)
- [13-green-3-result.json](13-green-3-result.json)
- [13-green-3-source.json](13-green-3-source.json)
- [13-interrupted-suite-result.json](13-interrupted-suite-result.json)
- [13-interrupted-suite-source.json](13-interrupted-suite-source.json)
- [13-prerequisite-audit.json](13-prerequisite-audit.json)
- [13-process-audit.json](13-process-audit.json)
- [13-red-1-result.json](13-red-1-result.json)
- [13-red-1-source.json](13-red-1-source.json)
- [13-red-2-result.json](13-red-2-result.json)
- [13-red-2-source.json](13-red-2-source.json)
- [13-red-3-result.json](13-red-3-result.json)
- [13-red-3-source.json](13-red-3-source.json)
- [13-renewed-final-format-result.json](13-renewed-final-format-result.json)
- [13-renewed-final-format-source.json](13-renewed-final-format-source.json)
- [13-renewed-final-lint-result.json](13-renewed-final-lint-result.json)
- [13-renewed-final-lint-source.json](13-renewed-final-lint-source.json)
- [13-renewed-final-mypy-result.json](13-renewed-final-mypy-result.json)
- [13-renewed-final-mypy-source.json](13-renewed-final-mypy-source.json)
- [13-renewed-final-suite-result.json](13-renewed-final-suite-result.json)
- [13-renewed-final-suite-source.json](13-renewed-final-suite-source.json)
- [13-renewed-final-whitespace-result.json](13-renewed-final-whitespace-result.json)
- [13-renewed-final-whitespace-source.json](13-renewed-final-whitespace-source.json)
- [13-tooling.json](13-tooling.json)

</details>

### Compact scenario results, 2026-11-13

Retired original `13-fixture-observations.json` (**4,297,835 bytes**, SHA-256 `daaea87fbc36ce201dff7ac2bc800b1ac9943f70a445833d18e01f9405e53486`). The [executed lossy successor](13-scenario-results.json) retains **88** observed scenario names/pointers, available CLI outcomes, failures, ticket/ref identities, gate outcomes/revisions and recorded assertions, plus source/result/completion references. Missing original observations remain missing; absent attempt lists are not converted to zero.

The replacement deliberately discards full run/input/assignment/QA payloads, repeated stdout/stderr and process detail. It is a derived historical result, not an original transcript, complete run archive, new verification, or development QA acceptance. Exact retired payload cannot be recovered from this extract. The original completion, independent reviews and source/result records retain their historical bytes; their old raw paths/hashes describe evidence available when written. The compact successor records its original path/hash and the executed retirement date. Separate M1 QA/finding proof remains protected; M1 acceptance and the open F1 gate are unchanged.
