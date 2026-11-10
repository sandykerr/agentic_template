# Final corpus C4 under unchanged guidance G2

Origin: [ticket 19](../../issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md),
approved oop-v2 / review-process-1, M1 unaccepted. Fixed whole-ticket baseline
`f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`.

**Evaluation lifecycle: completed; final declared C4 criteria pass under G2.**
[Spec original](spec-c4-raw.md) and [Standards original](standards-c4-raw.md) each
identify the four required concerns and substantively accept the four controls.
[Per-case adjudication](results.md) explains evidence, classification and remedies;
[history](history.md) preserves full fixture keys and the independent-verification
boundary. No unsupported blocker, optional suggestion or unresolved C4 required
mismatch exists. Actual ticket F1 verification and completion remain separate.

## Identity, declaration and blind assignments

[Complete eight-case declaration/key](declaration.md),
[pre-dispatch timestamp/hashes](declaration-capture.json),
[36-file source/guidance manifest](source-manifest.json),
[neutral snapshot](snapshot/REVIEW.md) and [caller-only delta](revision-delta.json)
identify C4 aggregate
`bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197`.
The aggregate hashes `json.dumps(manifest, sort_keys=True)` with default separators
and no terminal newline. Guidance **G2** is byte-identical to C2/C3; corpus labels
and guidance versions are independent. All original contracts and seeded concern
source stay unchanged. The original [G1/C1](../19-evaluation/README.md),
[failed C2](../19-evaluation-g2/results.md) and [failed C3](../19-evaluation-g3/results.md)
remain intact, including clean claims contradicted by later evaluator evidence.
[C2](../19-repair-c2-preservation.json) and [C3](../19-repair-c3-preservation.json)
preservation manifests pin every prior failed-trial file.

[Actual assignments/settings](assignments.json) retain fresh independently
configured fork-none GPT-6.1 Sol High roles. Known readable author prompts for
[Spec](spec-c4-input.txt) and [Standards](standards-c4-input.txt) were saved before
dispatch. [Spec dispatch](spec-c4-dispatch.json) and
[Standards dispatch](standards-c4-dispatch.json) preserve actual configuration and
timestamps. Reviewers receive only the same read-only neutral snapshot and their
axis assignment; no answer key, evaluator/repair material, previous outcomes,
ticket/spec, root audit or sibling report is supplied.

A [known readable neutral identity clarification](audit-clarification.txt) was
saved before sending the same content to both axes, after Spec reported an initial
33-file aggregate excluding hidden supplied guidance. It requests every regular
file, including hidden paths, and the already-specified serialization; it supplies
no source judgment or expected distribution. [Actual followup dispatches/receipts](followup-dispatches.json)
retain this input alongside the original prompts. The Spec reviewer independently
reproduced the exact 36-file aggregate afterward. No source/guidance changed and
no new assessment/review repetition occurred. Opaque received/dispatch fields are
not decrypted-delivery proof; known author inputs are preserved directly.

[Exact report/tool/settings capture](review-capture.json) and
[provenance](capture-provenance.json) retain the first original plaintext finals,
reviewer-saved copies and every actual source/tool/received record. Actual
[Spec source records](spec-c4-source-records.json) and
[Standards source records](standards-c4-source-records.json) preserve original
inspection and initial audit corrections. Original absolute snapshot references
map to identically hashed retained snapshot files; raw report text is unchanged.
Reviewer-generated manifests and the external Standards report digest are retained.

[Capture helper](capture_reviews_c4.py) extracts exact first plaintext child finals,
actual observed settings and all calls/outputs/received records from identified
sessions, refusing changed existing outputs. A template substitution initially
altered a Spec session UUID in its unexecuted final-capture branch; inspection
corrected that path before final capture. No original report/output was overwritten
and no reviewer judgment or source was changed. The collector never generates
findings or scores judgment.

## Source preflight and responsibility

C4 changes only the supplied b7 caller: binary process capture plus explicit
filesystem text decoding preserves CR and non-UTF8 bytes; os.fspath preserves the
checkout representation; returned CompletedProcess stdout/stderr remain text.
The same argument vectors/no shell/check=False mechanics and sole validate policy
owner remain. No input-contract narrowing, domain owner or framework is introduced.
[Exact caller/owner preflight](../19-repair-path-preflight-results.json) uses real
temporary Git repositories for five distinct path representations and compares C3
with C4. The root's earlier [raw/text CR observation](../19-repair-root-path-capture.json)
is separately retained and was not supplied to active reviewers. It was output
translation evidence rather than full validation. C4's later observation invokes
the exact caller and owner, showing wrong C3 CR root/non-UTF8 decode failure and
correct C4 roots for every observed path.

The earlier [all-control source audit](../19-repair-control-preflight-results.json)
remains exact for unchanged d9/f6/h8: missing-operand rejection and iterative graph
traversal, finite timeout guard/ordinary write cleanup, owned transitions and nested
alias isolation. No further generic guidance change occurred. These finite
observations support corpus source validity, not independent reviewer judgment or
exhaustive platform/process behavior.

## Limits and progression

Four complete eight-case corpora, two guidance versions, one original report per
axis per corpus. Sources evolve, so these are not identical-corpus repetitions
or a general reliability rate. Original h8 clean/adjudication failure, supported
additional b7/d9/f6 findings and C3 missed caller representation breach remain
visible. No clean new source result transfers back to those flawed versions.
C1 to C2 changes source and guidance together; no causal effect of wording alone
or proof of unchanged original-flaw detection follows.

The [current published reference](../../../../docs/agents/reviewer-evaluation.md)
carries exact final guidance/corpus and all failed stages through planning,
implementation/repair and both next-handoff branches. Actual implementation
`review-ticket-19/spec-01/F1` remains open pending separate fresh whole-ticket
exact-commit verification; corpus reviews do not replace that review. Original
fixture findings remain open in frozen source, not actual harness defects.

No production runtime behavior/tests/schema/backend, harness run, refactors 20–24,
M1 readiness/acceptance, promotion or push. Actual M1 feature-start provenance,
all-package cumulative review and human QA remain unperformed. Requested/observed
settings, readable known prompts, opaque received-task captures and read-only
permission bits do not prove backend instruction effectiveness, enforced isolation
or hard context limits. Measured usage/enforcement telemetry is unavailable;
<=250000 active-context target advisory. Runtime 33/34 remains separate.
