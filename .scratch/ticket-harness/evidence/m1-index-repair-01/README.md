# M1 caller-index repair and verification

Current status (2026-11-16): repair committed as `e06eeaf` and independently
verified fixed at `88e4cd8`. Fresh Spec, Standards and cumulative Standards each
report zero findings; [originals/capture](../m1-final-review-01/README.md).
[Fresh exact candidate and human QA](../m1-final-review-01/qa-guide.md) are prepared.
[M1 is now accepted](../m1-final-review-01/m1-qa-decision.md); M2 ticket25 is
next eligible but not started. Earlier pending/uncommitted descriptions
below retain their historical verification-stage scope.

## Source and authority

- Authorized scope: [continuation handoff](../../handoff-m1-caller-index-repair-and-final-verification.md)
  and the human's request to continue it according to AGENTS.
- Original F1 report source: `d02e61ea27de4febd17e337bd51529d07861226b`;
  [immutable original](../m1-qa-01/standards-01-original.md) and
  [retained paired reproduction/control](../m1-qa-01/index-routing-repro-01/manifest.json).
- Fixed repair baseline: `e2b0a260fa192a7b51edc5f4cc5692c6340444c2`.
  [Initial capture](starting.json) and [resumed capture](resumed-start.json)
  distinguish the intervening user environment changes and initial regression.
- Fixed cumulative baseline: `1a623bad0b08241367948948b731b9e1f5114671`;
  [provenance](../../reviews/M1-architecture-01.md).
- Actual frozen implementation: [final source/test hashes and instructions](final-implementation.json)
  and [scoped source patch](final-implementation.patch), captured before any
  repair checkpoint commit. The HEAD field alone does not identify the edits.
- [Actual instruction/environment bytes](review-instructions.tar.gz) and
  [external digest manifest](review-instructions.json). The user-authored uv
  environment changes remain separate from the repair; their uncommitted bytes
  are retained, including new frozen requirements. Role-specific assignment
  records will identify the supplied subsets of this inventory.

## Diagnosis, ownership and regression protection

[Worker notes](worker-notes.md) map existing coverage, the red/green loop,
all four process launch sites, caller/target state ownership, writes,
persistence/restoration, invalidation and four No/No architecture triggers.
[Worker check results](worker-checks.json), [source identities](worker-source.json),
[patch](worker-source.patch) and [external capture manifest](worker-capture-manifest.json)
retain commands, outputs and their actual scopes.

The new CLI regression has four distinct cases: harness submission success,
Standards rejection, an external agent staging, and an external candidate check
staging. They assert exact caller index bytes before observer Git commands,
then HEAD and staged/unstaged/untracked values and integration outcomes.
[Eight fresh routing observations](routing-observations/summary.json) extend
the original clean reproduction/control without rewriting it. Temporary fixture
repositories were cleaned; their retained records describe those executions.

## Verification

| Gate | Actual result / evidence |
| --- | --- |
| Initial public-CLI regression | Failed on caller index byte inequality, 0.42s; [original red log](red-caller-index.log) |
| Four final regression cases | Passed, 2.74s; [green log](green-external-processes.log) |
| Affected checks | 125 passed, 563.12s with executable TMPDIR; [result index](worker-checks.json), [log](focused-exec-tmp-pytest.log), [JUnit](focused-exec-tmp-pytest.xml) |
| Final strict mypy | Exit 0, ten package files; [result](final-mypy-result.json) |
| Final Ruff lint | Exit 0; [result](final-lint-result.json) |
| Final Ruff format | Exit 0, 24 files unchanged; [result](final-format-result.json) |
| Whitespace | Exit 0; [result](final-whitespace-result.json); later prose bookkeeping receives its own final whitespace check |
| Final-source full suite | **563 passed**, zero failures/errors/skips, 2878.13s; [completion result](completion-full-suite-retry-result.json), [log](completion-full-suite-retry.log), [JUnit](completion-full-suite-retry.xml). Earlier partial log is not a completion result. |
| Failed baseline observation | Environment outcome, zero attempts, one failed gate, unchanged integration; [retained record](baseline-observation.json), [execution identity/result](baseline-observation-result.json) |

The default `/tmp` is mounted `noexec`. Fifteen hook scenarios failed because
Git ignored their executable hooks; [direct executable probe](hook-execution-diagnostic.json)
and [original failed selection](focused-pytest.log) retain the cause. The first
full run was [interrupted with exit 130](full-suite-interrupted-result.json).
Neither is a completion result. The code was unchanged for the executable-TMPDIR
repeat. No hook assertions, tests or check requirements were removed.

The checkout-local uv `.venv` supplies Python 3.12.15, pytest 9.2.0, mypy 1.19.1
and Ruff 0.14.10; installed dependency consistency passed. Verification uses the
current AGENTS environment policy. The earlier Python 3.12.3 container capture
in `starting.json` was a superseded fallback, not a repository requirement or
an executed repair test. This repair changes no packaging or entry point; no
separate wheel/install campaign is required by the selected policy.

[Verification wrapper](verify.py) captures source/test and instruction hashes,
actual commands, results and relevant environment deltas. The
[suite capture plugin](m1_capture.py) retains selected records at the approved
CLI/Git seam. It neither substitutes processes nor changes assertions.
Unittest cleans its failed-baseline fixture before the plugin report hook;
[one scoped additional capture](capture-baseline.py) retains that missing
observation without replaying the full matrix.

### Verification completed — 2026-11-13

[Outcome and provenance](verification-completion.md) and the
[machine-readable aggregate](verification-completion-result.json) record the
completed full suite and fresh passing mypy/lint/format/whitespace gates.
All 28 source/test/configuration hashes and 50 instruction hashes match the
frozen implementation before and after each check and at final comparison.
The three-file repair remains uncommitted against `e2b0a26`; unrelated changes
were preserved. No production or test edits were made in this verification.

The first completion attempt stopped with an evidence-plugin path-alias error
after 11 passes, exit 3. The separate [adapted capture helper](completion_capture.py)
resolves `/panfs` versus `/explore` aliases and writes fresh observations to
[completion-suite-observations/](completion-suite-observations/). Original helper,
historical observations and failed-run records remain intact. The successful
repeat is the full-suite completion result; this changes no assertions or gates.

## Review and human boundary

[Repair assessment](../../reviews/M1-index-repair-01.md),
[cumulative assessment](../../reviews/M1-architecture-01.md) and
[append-only original finding history](../../reviews/M1-architecture-01-history.md)
own current lifecycle, dispositions and readiness. Independent exact-source
Spec/Standards and fresh High cumulative Standards remain pending. Original
review output will be retained separately before aggregation.

The human completed the earlier code/documentation review. New repair changes
and exact candidate behavior still require the applicable planned human
inspection and request-specific acceptance. No acceptance statement, approval
artifact, promotion, next-ticket selection or M2 implementation is created here.
The [fresh QA preparation script](prepare-qa.py) is prepared but has not run;
it requires a verified source manifest and writes no approval. Historical
temporary QA paths remain historical.

### Current independent verification and fresh candidate — 2026-11-16

[Independent originals and external hashes](../m1-final-review-01/capture.json)
retain all three clean reports at `88e4cd8`. All 28 source/test/configuration and
50 instruction hashes matched frozen verified bytes at review time; no suite was
replayed solely for bookkeeping. [Event06](../../reviews/M1-architecture-01-history.md#event06--independent-exact-source-repair-verification)
records original cumulative F1 fixed without changing severity or prior history.

The previously unexecuted `prepare-qa.py` has now run successfully against
[verified source](verified-candidate.json). [Actual request/location](qa-candidate/demo-location.json),
[seven gates and stopped record](qa-candidate/human-checkpoint-record.json),
[stale rejection and stop/new-process continuation](qa-candidate/demo-commands.json)
and [checkpoint archive/digest](qa-candidate/demo-archive.json) retain fresh
observations. No actual human fixture approval or development acceptance exists.
Further promotion/final-only demonstration awaits the human's exact request decision.

Final QA progression, 2026-11-16: the human approved both exact demo candidates
and conditionally accepted development M1. [All conditions passed](../m1-final-review-01/m1-acceptance-result.json);
[actual development decision](../m1-final-review-01/m1-qa-decision.md). The demo is
completed rather than continuable; initial stopped captures remain historical.
