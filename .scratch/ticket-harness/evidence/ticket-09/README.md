# Ticket 09 evidence

Current links below identify retained records. Original reports remain byte-identical historical accounts; paths in them may name deliberately retired payloads. See the [historical path guide](../README.md#historical-paths).

## Retained results

- [09-completion.md](09-completion.md)
- [09-scenario-results.json](09-scenario-results.json)

## Useful verification conclusions

Verified implementation: `7f4eac025cfccd0912f25e3bdd602c1e2b3e516f`.


Recorded command results, copied from the retained completion account:

| Command or check | Historical result |
| --- | --- |
| Report the observed state and integrated revision of every selected ticket and return success only when all selected work is Done. | `tickets` maps all four selected IDs to Done and their exact submitted/candidate/Done revisions; `selected_tickets` is canonical numeric order. `integration_revision` is the last verified promoted tip. Global attempts/gates/operations carry ticket identities and exact gate ranges; shared baseline uses null. `ticket` mirrors the active/latest entry for compatibility. All selected Done yields exit 0/completed. Partial-success decision, integrity and external-ref scenarios yield exit 1/incomplete with preserved Done/Blocked/Ready/Pending observations. Every captured CLI output matches durable record bytes; explicit status comparisons match final run output. |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **469 passed in 370.27s**, comprising all 448 existing tests and 21 new cases. Required final run captured the dependency observations without replaying a separate full fixture matrix. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0: strict mode, no issues in 7 source files. Also passed during implementation. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 18 files formatted. |
| `git diff --check`; `git diff --cached --check` before checkpoint; committed diff whitespace review | Exit 0. |
| Reusable Python `-m pip wheel --no-deps --no-build-isolation --wheel-dir /tmp/ticket09-checks/wheels .` | Exit 0: wheel SHA-256 `5a646dd2aa812b22daf84c0d0b171f4a47b9aa0282936e17602e9af377975b84`. |
| Reusable Python `-m pip install --no-deps --no-index --target /tmp/ticket09-checks/installed-final /tmp/ticket09-checks/wheels/ticket_harness-0.1.0-py3-none-any.whl` | Exit 0. Changed installed runtime files match final tested source hashes. |
| Reusable Python `/tmp/ticket09-checks/installed_smoke.py` | Exit 0: installed `--help`, four-ticket graph and exact matching status from `/tmp`, with installed-only `PYTHONPATH`. Actual installed CLI commands are saved in the observations. |
| Focused dependency/preflight/repair checks during development | Passed at their stated development sources; the final full suite supersedes those earlier-source results. Final malformed-snapshot focused case passed before the renewed suite. |

At `7f4eac025cfccd0912f25e3bdd602c1e2b3e516f`, the final full suite passed 469 tests in 370.27s; strict type, lint, format, whitespace and wheel/install checks passed as recorded in completion. These are retained observations, not new executions.

## Retired evidence

On 2026-11-13, the human explicitly requested retroactive retirement under the agreed [C1–C10 decisions](../evidence-retention-audit-01/retention-decisions.md); the overseer approved this exact ticket batch. Useful results and identities were recorded before deletion. No replacement archive of discarded payloads was created.

Discarded **1 files / 7,466 logical bytes**:

- C2 routine command output; C3 resolved development failures: 1 files / 7,466 bytes.

Routine stdout, repeated synthetic run trees and resolved development-failure detail are intentionally unavailable where selected. Completion, original independent reviews, source identities, structured result records and the linked retained scenario/audit conclusions survive. Original records may contain historical hashes or links to retired files; those hashes no longer imply that a complete original raw audit can be repeated. Preserved scripts document historical work and must not be run as current validators.

This retirement changes retained detail, not implementation verification or approval. No harness or tests were run. Development M1 remains unaccepted; `review-M1-architecture-01/standards-01/F1` remains open, and its independent proof and current QA material remain in the separate protected M1 bundles.

### Compact scenario results, 2026-11-13

Retired original `09-fixture-observations.json` (**778,934 bytes**, SHA-256 `7d96aa185bb99c03ecd51ba7b42fa0cff3f8d091d0442a93b27512d46c8630d4`). The [executed lossy successor](09-scenario-results.json) retains **21** observed scenario names/pointers, available CLI outcomes, failures, ticket/ref identities, gate outcomes/revisions and recorded assertions, plus source/result/completion references. Missing original observations remain missing; absent attempt lists are not converted to zero.

The replacement deliberately discards full run/input/assignment/QA payloads, repeated stdout/stderr and process detail. It is a derived historical result, not an original transcript, complete run archive, new verification, or development QA acceptance. Exact retired payload cannot be recovered from this extract. The original completion, independent reviews and source/result records retain their historical bytes; their old raw paths/hashes describe evidence available when written. The compact successor records its original path/hash and the executed retirement date. Separate M1 QA/finding proof remains protected; M1 acceptance and the open F1 gate are unchanged.
