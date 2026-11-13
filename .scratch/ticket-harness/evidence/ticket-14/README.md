# Ticket 14 evidence

Current links below identify retained records. Original reports remain byte-identical historical accounts; paths in them may name deliberately retired payloads. See the [historical path guide](../README.md#historical-paths).

## Retained results

- [14-check-results.json](14-check-results.json)
- [14-completion.md](14-completion.md)
- [14-coverage-map.md](14-coverage-map.md)
- [14-development-notes.md](14-development-notes.md)
- [14-final-source-identity.json](14-final-source-identity.json)
- [14-scenario-results.json](14-scenario-results.json)
- [14-implementation-report.md](14-implementation-report.md)
- [14-review-spec.md](14-review-spec.md)
- [14-review-standards.md](14-review-standards.md)
- [14-root-audit.json](14-root-audit.json)
- [14-root-observation-audit.json](14-root-observation-audit.json)

## Useful verification conclusions

Verified implementation: `29fb5569cf53c75bd351d6bd176bb29889c42a65`.
Original fixed review baseline: `d67c12d91495af00557b279d0bf0e1da518e6fcc`.

- 524 tests passed in 684.03s at 29fb5569cf53c75bd351d6bd176bb29889c42a65; all final static/whitespace gates passed; consolidated 103-scenario observation and independent audits retained. Raw repeated fixture tree is deliberately retired; current M1 approval is absent.

Recorded command results, copied from the retained completion account:

| Command or check | Historical result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **524 passed in 684.03s**; wrapper elapsed 684.962s. |
| Reusable Python `-m mypy` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples` | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples` | Exit 0: 21 files formatted. |
| `git diff --check` | Exit 0; staged implementation and committed original-baseline whitespace checks also exit 0. |

## Retired evidence

On 2026-11-13, the human explicitly requested retroactive retirement under the agreed [C1–C10 decisions](../evidence-retention-audit-01/retention-decisions.md); the overseer approved this exact ticket batch. Useful results and identities were recorded before deletion. No replacement archive of discarded payloads was created.

Discarded **183 files / 10,410,772 logical bytes**:

- C2 routine command output; C3 resolved development failures: 18 files / 44,088 bytes.
- C2/C3 duplicated original command-output payload: 1 files / 38,536 bytes.
- C5 repeated historical fixture observations; C8 inactive fixture operational copies: 164 files / 10,328,148 bytes.

Routine stdout, repeated synthetic run trees and resolved development-failure detail are intentionally unavailable where selected. Completion, original independent reviews, source identities, structured result records and the linked retained scenario/audit conclusions survive. Original records may contain historical hashes or links to retired files; those hashes no longer imply that a complete original raw audit can be repeated. Preserved scripts document historical work and must not be run as current validators.

This retirement changes retained detail, not implementation verification or approval. No harness or tests were run. Development M1 remains unaccepted; `review-M1-architecture-01/standards-01/F1` remains open, and its independent proof and current QA material remain in the separate protected M1 bundles.

<details>
<summary>Other retained original files</summary>

- [14-bookkeeping-audit.json](14-bookkeeping-audit.json)
- [14-check.py](14-check.py)
- [14-committed-whitespace-result.json](14-committed-whitespace-result.json)
- [14-committed-whitespace-source.json](14-committed-whitespace-source.json)
- [14-final-format-result.json](14-final-format-result.json)
- [14-final-format-source.json](14-final-format-source.json)
- [14-final-lint-result.json](14-final-lint-result.json)
- [14-final-lint-source.json](14-final-lint-source.json)
- [14-final-mypy-result.json](14-final-mypy-result.json)
- [14-final-mypy-source.json](14-final-mypy-source.json)
- [14-final-suite-result.json](14-final-suite-result.json)
- [14-final-suite-source.json](14-final-suite-source.json)
- [14-final-whitespace-result.json](14-final-whitespace-result.json)
- [14-final-whitespace-source.json](14-final-whitespace-source.json)
- [14-focused-1-result.json](14-focused-1-result.json)
- [14-focused-1-source.json](14-focused-1-source.json)
- [14-focused-lint-result.json](14-focused-lint-result.json)
- [14-focused-lint-source.json](14-focused-lint-source.json)
- [14-focused-mypy-result.json](14-focused-mypy-result.json)
- [14-focused-mypy-source.json](14-focused-mypy-source.json)
- [14-green-1-result.json](14-green-1-result.json)
- [14-green-1-source.json](14-green-1-source.json)
- [14-green-2-result.json](14-green-2-result.json)
- [14-green-2-source.json](14-green-2-source.json)
- [14-green-3-result.json](14-green-3-result.json)
- [14-green-3-source.json](14-green-3-source.json)
- [14-prerequisite-audit.json](14-prerequisite-audit.json)
- [14-red-1-result.json](14-red-1-result.json)
- [14-red-1-source.json](14-red-1-source.json)
- [14-red-2-result.json](14-red-2-result.json)
- [14-red-2-source.json](14-red-2-source.json)
- [14-red-3-result.json](14-red-3-result.json)
- [14-red-3-source.json](14-red-3-source.json)
- [14-renewed-staged-whitespace-result.json](14-renewed-staged-whitespace-result.json)
- [14-renewed-staged-whitespace-source.json](14-renewed-staged-whitespace-source.json)
- [14-staged-whitespace-result.json](14-staged-whitespace-result.json)
- [14-staged-whitespace-source.json](14-staged-whitespace-source.json)
- [14-tooling.json](14-tooling.json)
- [14-worker-check-audit.json](14-worker-check-audit.json)

</details>

### Compact scenario results, 2026-11-13

Retired original `14-fixture-observations.json` (**6,203,476 bytes**, SHA-256 `a7d615d82b1049345cd89394674c8814eaa38f5a085f37d3dcbc3349900171db`). The [executed lossy successor](14-scenario-results.json) retains **103** observed scenario names/pointers, available CLI outcomes, failures, ticket/ref identities, gate outcomes/revisions and recorded assertions, plus source/result/completion references. Missing original observations remain missing; absent attempt lists are not converted to zero.

The replacement deliberately discards full run/input/assignment/QA payloads, repeated stdout/stderr and process detail. It is a derived historical result, not an original transcript, complete run archive, new verification, or development QA acceptance. Exact retired payload cannot be recovered from this extract. The original completion, independent reviews and source/result records retain their historical bytes; their old raw paths/hashes describe evidence available when written. The compact successor records its original path/hash and the executed retirement date. Separate M1 QA/finding proof remains protected; M1 acceptance and the open F1 gate are unchanged.
