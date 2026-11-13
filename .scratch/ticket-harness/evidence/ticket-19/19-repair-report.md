# Ticket 19 bounded repair evidence

Fresh repair actor `/root/repair19`, inherited GPT-6.1 Sol Medium, advisory target
<=250000 active-context tokens. Fixed whole-ticket baseline remains
`f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`. Measured usage and backend/hard context
enforcement telemetry are unavailable. Scope is only ticket 19 development
evaluation/guidance; no production behavior/tests/schema/backend/refactor or harness
run. Parent owns final independent whole-ticket re-review, completion and handoff.

## Original finding and preservation

[Original Spec](19-review-spec.md) reports blocking
`review-ticket-19/spec-01/F1`: h8's by-reference dictionary inputs defeat its
explicit isolation promise. [Original Standards](19-review-standards.md) reports
0 blocking/0 optional with a different scalar-value interpretation. Parent captured
both original reports/instructions/observations/audits before repair in the
[immutable capture manifest](19-review-capture.json). [Actual finding history](19-finding-history.md)
E01 and [assessment](../reviews/ticket-19.md) retain the original open finding;
neither original report is rewritten and no independent fix disposition is claimed.

Every previously committed G1 artifact, source/contract, report/classification,
evaluator result, finding history, implementation report, check/log/result and
helper remains byte-identical to rejected source. Only the current ownership
contract and current guidance summary change among original tracked files.
[Correction history](19-evaluation-g2/history.md) and subsequent versioned records
supersede old complete-calibration claims without altering their observations.
Initial F1 established invalid h8; later findings also expose unchanged original
b7/d9/f6 defects, so no current summary claims exactly three valid G1 controls or
retrospective full-corpus success. All four seeded detections remain supported.
No human waiver, blocker deferral, changed approved contract or acceptance is needed.

## Independent source and guidance versions

Guidance **G1** is the original baseline snapshot; **G2** adds only the paragraph
quoted below to the owning [ownership-review contract](../../../docs/agents/ownership-review.md#report-substantive-reasoning).
Corpus labels **C1–C4** are separate from guidance versions; directory suffixes
`g3`/`g4` do not denote new guidance changes.

| Corpus / guidance | Declared source changes and observed outcome |
| --- | --- |
| [C1 / G1](19-evaluation/README.md) | Original four concern/control slots. Four required concern detections per relevant axes; clean h8/scalar assumption and evaluator match fail its explicit isolation promise. Additional unchanged control defects become visible later. Preserve original success labels as rejected historical evidence. |
| [C2 / G2](19-evaluation-g2/results.md) | h8 deep-copies inputs/transitions/outputs; one generic guidance paragraph changes. Both axes find b7 trailing-space root corruption; Spec additionally finds d9 missing operands/f6 unbounded timeout, while Standards' different interpretations stay original. All required seeds detected, corrected h8 clean. Failed invalid-control trial, not false-blocker failure. |
| [C3 / G2](19-evaluation-g3/results.md) | Source-only b7 output decoding, d9 nonempty operand/iterative traversal and f6 finite timeout guard. Both axes detect four required seeds and call controls clean. Independent root preflight shows b7 caller `text=True` changes a valid CR path to newline; complete pass rejected despite clean reports. This is not a C3 reviewer finding. |
| [C4 / G2](19-evaluation-g4/declaration.md) | Caller-only byte capture with explicit filesystem text decoding/os.fspath. Contracts, seeds, other controls and all G2 guidance unchanged. Exact final complete eight-case evaluation is required on this source; no clean result transfers to old sources. |

Every trial declares the full eight-case key and exact 36-file source/guidance
manifest before dispatch. All eight original contracts and four required-concern
source files remain unchanged across stages. [C2 preservation](19-repair-c2-preservation.json)
and [C3 preservation](19-repair-c3-preservation.json) pin every failed-stage file
before the next declaration. Each actual independent report, raw tool/settings
record, known input, mismatch and source revision remains retained. The C4
[final manifest](19-evaluation-g4/source-manifest.json) identifies aggregate
`bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197`.

The exact generic guidance correction, separately identified from fixture source
changes in the [C2 delta](19-evaluation-g2/revision-delta.json), is:

> Check each explicit guarantee against the accepted input values and reference
> aliases in the supplied contract and implementation. A narrower input-domain
> assumption needs support from that contract or enforced validation; disclosing
> an assumption alone cannot establish a clean result when accepted inputs break
> the guarantee. Record a concrete counterexample and classify its consequence
> under the governing contract.

This addresses the observed assumption failure without case IDs, answer-key
classification or a general new framework/checklist. G2 is byte-identical in C2,
C3 and C4. Upstream skills remain unchanged. Source and guidance changed together
from C1 to C2, so final results cannot isolate wording's effect, show detection of
unchanged flawed h8 or establish general reviewer effectiveness. C3/C4 correct
controls under the same guidance, preserving all broad guarantees rather than
inventing path, depth, scalar or timeout-domain restrictions.

## Actual preflight, inputs and judgments

[All-control preflight](19-repair-control-preflight-results.json) inspected the four
control contracts against accepted inputs and ordinary environment behavior before
C3 declaration. It reproduced a real clean trailing-space checkout returning the
wrong root, missing dependency operands being silently dropped, and a valid
1200-node forward chain raising RecursionError without any stated depth bound.
Candidate fixes preserve root characters, validate nonempty dependency tokens,
use local iterative DFS and enforce finite timeout without positive-only policy.
The same bounded observation checks ordinary encoding-failure cleanup/old content,
complete replacement, nonzero process result and zero/negative/positive finite
TimeoutExpired outcomes, plus h8 invalid transitions/nested input/output isolation.
No private production seam or test suite was introduced.

The all-control examples missed a representation defect in the unchanged caller.
Parent's later [root path preflight](19-repair-root-path-capture.json) preserves
exact original command/script/raw-vs-text CR bytes and its source identity. It
observes output translation, not full validate execution. Its initial guessed
snapshot path hash command failed and corrected real-path command passed, with
no source/trial change. Active C3 reviewers received no root result or instruction.
After both originals were captured, [exact caller/owner preflight](19-repair-path-preflight-results.json)
compared C3 with C4 on trailing space, CR, trailing newline, Unicode and non-UTF8
filesystem paths in real temporary Git repositories. C3 changes CR and raises on
non-UTF8; every observed C4 root equals the actual root. The final adapter still
returns text stdout/stderr, uses argv/no shell/check=False, and delegates every
policy decision to validate. No contract narrows those accepted paths.

Each corpus uses separate fresh fork-none GPT-6.1 Sol High Spec and Standards
assignments over read-only neutral snapshots, with no evaluator key/builder,
prior/sibling output, repair material or actual ticket/spec supplied. Known readable
full prompts are saved before each new dispatch; actual session settings, all
source/tool/received records and exact original plaintext finals are retained.
Opaque task serialization is not decrypted delivery/effectiveness proof. Snapshot
permissions/instructions are advisory isolation, not backend enforcement. The
<=250000 active-context target remains advisory with no measured/hard enforcement.

A pre-saved [neutral C4 identity clarification](19-evaluation-g4/audit-clarification.txt)
was sent identically to both axes after Spec initially counted only 33 nonhidden
files. It repeats the all-regular-file/hidden-file/default-spaced-JSON audit rule,
supplying no expected result, source change or sibling conclusion. Spec then
independently reproduced all 36 file identities; originals/tool history preserve
the initial mismatch. It adds no trial or substantive guidance revision. The
[actual followups](19-evaluation-g4/followup-dispatches.json) retain known author
text, dispatches and receipts.

One preparation collector's broad selector matched its own source-writing call,
so its count assertion failed before output creation. [Collector history](19-evaluation-g2/collector-history.json)
retains the actual failure/correction; no trial/source changed. A later capture
helper template altered a session UUID in an unexecuted branch; inspection corrected
it before final capture. Neither event overwrote existing evidence or generated
findings. Versioned collectors refuse changed saved outputs. [Actual preparation/audit/declaration commands](19-repair-workflow-command-records.json) retain the six subsequent tool calls/outputs, alongside C2 preparation evidence. Actual final per-case
judgments, not scripted matching/counts, determine evaluation success.

## Ownership, routing and checkpoint triggers

Shared ownership guidance continues to own substantive inspection; review records
own identity/immutable originals/append-only history/human authority; architecture
checkpoints own timing and gates. Existing authors declare, reviewers assess/save
originals, evaluator adjudicates, and planning/worker/handoff consumers carry the
current version and limitations. Versioned evidence uses existing persistence forms;
no executable owner, writer, restore/invalidation schema or shared runtime state
changes. Immutable source/report identities remain version-specific; mutable
[guidance summary](../../../docs/agents/reviewer-evaluation.md) links them.

Unchanged grill-to-tickets reaches the shared planning reference; the implementation
wrapper supplies the evaluation reference before fresh review/repair; common
next-handoff context supplies both implementation and QA/waiting branches. Existing
conditional routes are retained. New actual refactors still require their own
whole-ticket reviews, original baselines, prior full keys and exact-source checks.
No corpus report grants integration or human QA authority.

| Trigger | Repair start | Post repair | Source reasoning |
| --- | --- | --- | --- |
| New lifecycle | No | No | Existing review/report/finding/evaluator roles and bounded repair retained. |
| New persistence/restoration path | No | No | Existing development snapshots/Markdown/JSON forms; no runtime restore change. |
| New shared mutable state | No | No | Original evidence immutable, current summary references versions; no executable state. |
| Additional writer | No | No | Existing author/reviewer/evaluator/planning/handoff roles retain output ownership. |

No additional real-package assessment is triggered. Intentionally flawed concern
fixtures are inputs, not production responsibilities. Real M1 still requires actual
feature-start provenance, all-package exact-source cumulative assessment and human
QA; all remain unperformed. Review completion, F1 independently verified, ticket
Done, candidate readiness and acceptance stay distinct.

## Requirement map and verification scope

| Criterion / failure | Evidence/verification |
| --- | --- |
| 1: invalid or retrospective corpus | Four full source-identified declarations/keys before actual assignments; failed controls retained; final C4 preserves all contracts with explicit source fixes and preflight. |
| 2: canned/leaked/non-independent reviews | Actual fresh independent axes; pre-saved readable inputs and neutral clarification; exact settings/source/tool/original-final records, no key or sibling context. |
| 3: required concern/control misjudgment | Manual per-case source/contract/classification/remedy comparison for every trial; valid additional concerns not relabeled false blockers; final exact-source reports required. |
| 4: discarded failures/incomplete final corpus | G1 unchanged, C2/C3 full preservation manifests, every mismatch/revision/report retained, all eight cases in final trial; finite limitations/causal confounding disclosed. |
| 5: unusable next handoff | Existing planning/implementation/both-handoff routes point to current G2/C4 identity, old failures and actual evidence; source/link/routing audit. Parent generates handoff only after whole-ticket gates. |
| 6: calibration confused with runtime | No production code/tests/backend/schema/harness/private seam; 33/34 delivery/enforcement, real refactors and actual M1 QA remain separate. |

Standalone document/skill policy applies. [New repair checker](19-repair-check.py)
and [runner](19-repair-run-checks.sh) protect all original rejected artifacts except
the two current guidance owners, verify every versioned manifest and read-only
supplied snapshot, failed-stage preservation maps, declarations/settings/timing,
root original review capture hashes, current links/routing and preflight identities.
Original raw report links retain their recorded origins; the parent capture mapping
locates durable renamed attachments, so new navigation/hash checks preserve those
original texts. Validate the two whole-ticket changed wrappers, helper syntax,
shell and whitespace. Existing CLI/Git runtime suites cannot establish reviewer
judgment; no production/runtime/package change warrants replaying them here.

## Repair result and independent verification boundary

[Final C4 adjudication](19-evaluation-g4/results.md) records all four required
concerns detected on declared axes with proportionate remedies, supported clean
controls and no unsupported blocker, optional suggestion or unresolved required
mismatch. Exact original reports/settings/tools and all failed stages are retained.
Source checks are recorded in [the new log](19-repair-checks.log) and timestamped
`19-repair-check-results-*.json`; those mechanical audits do not score judgment.
The claimed bounded repair is ready for independent exact-commit verification;
no actual F1 fixed disposition, implementation completion or readiness is claimed. Parent must receive the implementation-only checkpoint, retain the original
baseline, and obtain separate fresh High whole-ticket Spec/Standards reports with
independent verification of `review-ticket-19/spec-01/F1`. These corpus reviews do
not replace those reports. Completion bookkeeping and the next prompt remain parent
work after every required gate; no human acceptance, promotion or push is authorized.

## Exact immutable-capture whitespace exception

The first checks passed document/skill/AST/link/routing/identity validation; their
pre-staging default whitespace command did not yet include new untracked files.
After staging, the [full default check](19-repair-stage-check.json) exited **2**:
`19-evaluation-g3/spec-c3-reviewer-saved.md:202: new blank line at EOF`.
That separately saved original reviewer report has exactly two terminal LF bytes.
Its digest is frozen in the C3 preservation map, so trimming it would rewrite
original evidence. The failing command/output remains in the log and JSON; no
unqualified all-path default whitespace pass is claimed.

Parent authorized this precise evidence-handling scope, preserving all bytes:

```text
git diff --check f2929e79cfd5a68f670862775053ae85ba9582b5 -- . ':(exclude).scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md'
git -c core.whitespace=-blank-at-eof diff --check f2929e79cfd5a68f670862775053ae85ba9582b5 -- .scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md
```

The first applies default whitespace checking to every other path. The second
checks every other whitespace rule on this exact immutable saved copy. The source
audit verifies its unchanged frozen digest and exactly two terminal LF bytes.
No other exclusion, repository whitespace policy change, source behavior change
or human risk acceptance is introduced. Both scoped command results and renewed
final-source checks are recorded in the existing append-only repair log. Fresh
whole-ticket High Spec/Standards reviewers must assess this bounded exception.
