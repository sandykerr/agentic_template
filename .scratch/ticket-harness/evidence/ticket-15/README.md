# Ticket 15 evidence

Current links below identify retained records. Original reports remain byte-identical historical accounts; paths in them may name deliberately retired payloads. See the [historical path guide](../README.md#historical-paths).

## Retained results

- [15-check-results.json](15-check-results.json)
- [15-completion.md](15-completion.md)
- [15-coverage-map.md](15-coverage-map.md)
- [15-final-source-identity.json](15-final-source-identity.json)
- [15-fixture-observations.json](15-fixture-observations.json)
- [15-implementation-report.md](15-implementation-report.md)
- [15-repair1-check-results.json](15-repair1-check-results.json)
- [15-repair1-final-source-identity.json](15-repair1-final-source-identity.json)
- [15-repair1-fixture-observations.json](15-repair1-fixture-observations.json)
- [15-repair1-implementation-report.md](15-repair1-implementation-report.md)
- [15-repair1-installed-invalidation.json](15-repair1-installed-invalidation.json)
- [15-repair1-root-audit.json](15-repair1-root-audit.json)
- [15-repair1-root-observation-audit.json](15-repair1-root-observation-audit.json)
- [15-review-spec-initial.md](15-review-spec-initial.md)
- [15-review-spec.md](15-review-spec.md)
- [15-review-standards-initial.md](15-review-standards-initial.md)
- [15-review-standards.md](15-review-standards.md)
- [15-root-audit.json](15-root-audit.json)
- [15-root-observation-audit.json](15-root-observation-audit.json)

## Useful verification conclusions

Original fixed review baseline: `90255aaf6faf9aedce18f7159093f5dbfde294b7`.
Final implementation and review repair: `d11f0bc60a2c11c40683e58581dffa10e36a91be`.

- 544 tests passed in 910.17s at d11f0bc60a2c11c40683e58581dffa10e36a91be; all ten repaired final gates passed. Only repair1-final verifies final source. STD15-01 was independently fixed by binding restored verification to durable canonical gates; regression test_continued_run_records_invalidation_of_earlier_verified_source and separate installed invalidation proof remain. Preserve original initial/final differing reviews and repair report. Final 123 consolidated scenarios and 1,242-file historical audit result remain as observations, not a claim deleted payload is replayable.

Recorded command results, copied from the retained completion account:

| Command or check | Historical result |
| --- | --- |
| `python -m pytest -q --durations=20` | Exit 0: **544 passed in 910.17s**; wrapper 910.693s. |
| Strict `python -m mypy` | Exit 0. |
| `python -m ruff check ticket_harness tests examples` | Exit 0. |
| `python -m ruff format --check ticket_harness tests examples` | Exit 0. |
| Working, actual staged and committed original-baseline whitespace | All exit 0. Empty-index staging captures are explicitly historical and excluded from final gate consolidation. |
| Pinned-backend wheel, isolated target install, installed console script | All exit 0. All nine installed/wheel Python members match repaired source. |

## Retired evidence

On 2026-11-13, the human explicitly requested retroactive retirement under the agreed [C1–C10 decisions](../evidence-retention-audit-01/retention-decisions.md); the overseer approved this exact ticket batch. Useful results and identities were recorded before deletion. No replacement archive of discarded payloads was created.

Discarded **5,485 files / 59,331,731 logical bytes**:

- C2 routine command output; C3 resolved development failures: 41 files / 36,475 bytes.
- C2/C3 duplicated original command-output payload: 1 files / 12,169 bytes.
- C5 repeated historical fixture observations; C8 inactive fixture operational copies: 5,443 files / 59,283,087 bytes.

Routine stdout, repeated synthetic run trees and resolved development-failure detail are intentionally unavailable where selected. Completion, original independent reviews, source identities, structured result records and the linked retained scenario/audit conclusions survive. Original records may contain historical hashes or links to retired files; those hashes no longer imply that a complete original raw audit can be repeated. Preserved scripts document historical work and must not be run as current validators.

This retirement changes retained detail, not implementation verification or approval. No harness or tests were run. Development M1 remains unaccepted; `review-M1-architecture-01/standards-01/F1` remains open, and its independent proof and current QA material remain in the separate protected M1 bundles.

<details>
<summary>Other retained original files</summary>

- [15-check.py](15-check.py)
- [15-final-committed-whitespace-result.json](15-final-committed-whitespace-result.json)
- [15-final-committed-whitespace-source.json](15-final-committed-whitespace-source.json)
- [15-final-format-result.json](15-final-format-result.json)
- [15-final-format-source.json](15-final-format-source.json)
- [15-final-implementation-whitespace-result.json](15-final-implementation-whitespace-result.json)
- [15-final-implementation-whitespace-source.json](15-final-implementation-whitespace-source.json)
- [15-final-install-result.json](15-final-install-result.json)
- [15-final-install-source.json](15-final-install-source.json)
- [15-final-installed-result.json](15-final-installed-result.json)
- [15-final-installed-source.json](15-final-installed-source.json)
- [15-final-lint-result.json](15-final-lint-result.json)
- [15-final-lint-source.json](15-final-lint-source.json)
- [15-final-mypy-result.json](15-final-mypy-result.json)
- [15-final-mypy-source.json](15-final-mypy-source.json)
- [15-final-staged-whitespace-result.json](15-final-staged-whitespace-result.json)
- [15-final-staged-whitespace-source.json](15-final-staged-whitespace-source.json)
- [15-final-suite-result.json](15-final-suite-result.json)
- [15-final-suite-source.json](15-final-suite-source.json)
- [15-final-wheel-result.json](15-final-wheel-result.json)
- [15-final-wheel-source.json](15-final-wheel-source.json)
- [15-final-whitespace-result.json](15-final-whitespace-result.json)
- [15-final-whitespace-source.json](15-final-whitespace-source.json)
- [15-focused-continuation-result.json](15-focused-continuation-result.json)
- [15-focused-continuation-source.json](15-focused-continuation-source.json)
- [15-focused-gates-result.json](15-focused-gates-result.json)
- [15-focused-gates-source.json](15-focused-gates-source.json)
- [15-focused-lint-result.json](15-focused-lint-result.json)
- [15-focused-lint-source.json](15-focused-lint-source.json)
- [15-focused-mypy-result.json](15-focused-mypy-result.json)
- [15-focused-mypy-source.json](15-focused-mypy-source.json)
- [15-green-1-result.json](15-green-1-result.json)
- [15-green-1-source.json](15-green-1-source.json)
- [15-green-1b-result.json](15-green-1b-result.json)
- [15-green-1b-source.json](15-green-1b-source.json)
- [15-green-2-result.json](15-green-2-result.json)
- [15-green-2-source.json](15-green-2-source.json)
- [15-green-3-result.json](15-green-3-result.json)
- [15-green-3-source.json](15-green-3-source.json)
- [15-installed-observations.json](15-installed-observations.json)
- [15-installed-scenario.py](15-installed-scenario.py)
- [15-package-manifest.json](15-package-manifest.json)
- [15-package/ticket_harness-0.1.0-py3-none-any.whl](15-package/ticket_harness-0.1.0-py3-none-any.whl)
- [15-prerequisite-audit.json](15-prerequisite-audit.json)
- [15-red-1-result.json](15-red-1-result.json)
- [15-red-1-source.json](15-red-1-source.json)
- [15-red-2-result.json](15-red-2-result.json)
- [15-red-2-source.json](15-red-2-source.json)
- [15-red-3-result.json](15-red-3-result.json)
- [15-red-3-source.json](15-red-3-source.json)
- [15-repair1-consolidate.py](15-repair1-consolidate.py)
- [15-repair1-final-actual-staged-whitespace-result.json](15-repair1-final-actual-staged-whitespace-result.json)
- [15-repair1-final-actual-staged-whitespace-source.json](15-repair1-final-actual-staged-whitespace-source.json)
- [15-repair1-final-committed-whitespace-result.json](15-repair1-final-committed-whitespace-result.json)
- [15-repair1-final-committed-whitespace-source.json](15-repair1-final-committed-whitespace-source.json)
- [15-repair1-final-format-result.json](15-repair1-final-format-result.json)
- [15-repair1-final-format-source.json](15-repair1-final-format-source.json)
- [15-repair1-final-install-result.json](15-repair1-final-install-result.json)
- [15-repair1-final-install-source.json](15-repair1-final-install-source.json)
- [15-repair1-final-installed-result.json](15-repair1-final-installed-result.json)
- [15-repair1-final-installed-source.json](15-repair1-final-installed-source.json)
- [15-repair1-final-lint-result.json](15-repair1-final-lint-result.json)
- [15-repair1-final-lint-source.json](15-repair1-final-lint-source.json)
- [15-repair1-final-mypy-result.json](15-repair1-final-mypy-result.json)
- [15-repair1-final-mypy-source.json](15-repair1-final-mypy-source.json)
- [15-repair1-final-staged-whitespace-result.json](15-repair1-final-staged-whitespace-result.json)
- [15-repair1-final-staged-whitespace-source.json](15-repair1-final-staged-whitespace-source.json)
- [15-repair1-final-suite-result.json](15-repair1-final-suite-result.json)
- [15-repair1-final-suite-source.json](15-repair1-final-suite-source.json)
- [15-repair1-final-wheel-result.json](15-repair1-final-wheel-result.json)
- [15-repair1-final-wheel-source.json](15-repair1-final-wheel-source.json)
- [15-repair1-final-whitespace-result.json](15-repair1-final-whitespace-result.json)
- [15-repair1-final-whitespace-source.json](15-repair1-final-whitespace-source.json)
- [15-repair1-focused-result.json](15-repair1-focused-result.json)
- [15-repair1-focused-source.json](15-repair1-focused-source.json)
- [15-repair1-green-result.json](15-repair1-green-result.json)
- [15-repair1-green-source.json](15-repair1-green-source.json)
- [15-repair1-installed-observations.json](15-repair1-installed-observations.json)
- [15-repair1-installed-scenario.py](15-repair1-installed-scenario.py)
- [15-repair1-package-manifest.json](15-repair1-package-manifest.json)
- [15-repair1-package/ticket_harness-0.1.0-py3-none-any.whl](15-repair1-package/ticket_harness-0.1.0-py3-none-any.whl)
- [15-repair1-raw-artifact-hashes.json](15-repair1-raw-artifact-hashes.json)
- [15-repair1-red-result.json](15-repair1-red-result.json)
- [15-repair1-red-source.json](15-repair1-red-source.json)
- [15-root-prerequisite-audit.json](15-root-prerequisite-audit.json)
- [15-spec-final-audit.json](15-spec-final-audit.json)
- [15-spec-final-audit.py](15-spec-final-audit.py)
- [15-standards-audit.json](15-standards-audit.json)
- [15-standards-audit.py](15-standards-audit.py)
- [15-standards-repair1-audit.json](15-standards-repair1-audit.json)
- [15-standards-repair1-audit.py](15-standards-repair1-audit.py)
- [15-standards-restored-evidence-repro.json](15-standards-restored-evidence-repro.json)
- [15-standards-restored-evidence-repro.py](15-standards-restored-evidence-repro.py)
- [15-tooling-result.json](15-tooling-result.json)
- [15-tooling-source.json](15-tooling-source.json)
- [15-wheel-result.json](15-wheel-result.json)
- [15-wheel-source.json](15-wheel-source.json)

</details>
