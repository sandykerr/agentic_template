# Ticket 12 evidence

Current links below identify retained records. Original reports remain byte-identical historical accounts; paths in them may name deliberately retired payloads. See the [historical path guide](../README.md#historical-paths).

## Retained results

- [12-check-results.json](12-check-results.json)
- [12-completion.md](12-completion.md)
- [12-coverage-map.md](12-coverage-map.md)
- [12-final-source-identity.json](12-final-source-identity.json)
- [12-scenario-results.json](12-scenario-results.json)
- [12-review-spec.md](12-review-spec.md)
- [12-review-standards.md](12-review-standards.md)

## Useful verification conclusions

Verified implementation: `14cafef40726eba80d8648d98d9c263fde3a5d0b`.
Original fixed review baseline: `2e15004338b45d61719656de113c2cbfdea56345`.

- Final 499 tests passed; final source identity and result map retained. Interrupted/red-green and environment output is historical noise; source-restoration requirement correction is recorded in completion/development records.

Recorded command results, copied from the retained completion account:

| Command or check | Historical result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **499 passed in 400.57s**, final source/test tree, with retained observations. |
| Reusable Python `-m mypy`, `PYTHONPATH=/tmp/ticket12-tools` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples`, same tool path | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples`, same tool path | Exit 0: 20 files formatted. |
| `git diff --check`; original-baseline committed diff whitespace check | Exit 0. |

## Retired evidence

On 2026-11-13, the human explicitly requested retroactive retirement under the agreed [C1–C10 decisions](../evidence-retention-audit-01/retention-decisions.md); the overseer approved this exact ticket batch. Useful results and identities were recorded before deletion. No replacement archive of discarded payloads was created.

Discarded **12 files / 1,495,949 logical bytes**:

- C2 routine command output; C3 resolved development failures: 11 files / 723,269 bytes.
- C2/C3 duplicated original command-output payload: 1 files / 772,680 bytes.

Routine stdout, repeated synthetic run trees and resolved development-failure detail are intentionally unavailable where selected. Completion, original independent reviews, source identities, structured result records and the linked retained scenario/audit conclusions survive. Original records may contain historical hashes or links to retired files; those hashes no longer imply that a complete original raw audit can be repeated. Preserved scripts document historical work and must not be run as current validators.

This retirement changes retained detail, not implementation verification or approval. No harness or tests were run. Development M1 remains unaccepted; `review-M1-architecture-01/standards-01/F1` remains open, and its independent proof and current QA material remain in the separate protected M1 bundles.

<details>
<summary>Other retained original files</summary>

- [12-bookkeeping-check.py](12-bookkeeping-check.py)
- [12-check-results-interrupted.json](12-check-results-interrupted.json)
- [12-prerequisite-audit.json](12-prerequisite-audit.json)
- [12-source-identity-interrupted.json](12-source-identity-interrupted.json)

</details>

### Compact scenario results, 2026-11-13

Retired original `12-fixture-observations.json` (**2,728,923 bytes**, SHA-256 `ec71c9e30d86a1da514af14795aeb22eb4d3d4f742def7500cb799bbab3df987`). The [executed lossy successor](12-scenario-results.json) retains **78** observed scenario names/pointers, available CLI outcomes, failures, ticket/ref identities, gate outcomes/revisions and recorded assertions, plus source/result/completion references. Missing original observations remain missing; absent attempt lists are not converted to zero.

The replacement deliberately discards full run/input/assignment/QA payloads, repeated stdout/stderr and process detail. It is a derived historical result, not an original transcript, complete run archive, new verification, or development QA acceptance. Exact retired payload cannot be recovered from this extract. The original completion, independent reviews and source/result records retain their historical bytes; their old raw paths/hashes describe evidence available when written. The compact successor records its original path/hash and the executed retirement date. Separate M1 QA/finding proof remains protected; M1 acceptance and the open F1 gate are unchanged.
