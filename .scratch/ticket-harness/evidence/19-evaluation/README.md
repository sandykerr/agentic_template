# Ticket 19: declared development reviewer evaluation

Evaluation lifecycle: **completed** for the finite G1 corpus assessment. This is
not implementation-ticket completion, real-package cumulative assessment, candidate
readiness or human QA acceptance. Final independent implementation Spec/Standards,
completion bookkeeping and next prompt belong to the parent workflow.

Originating [ticket 19](../../issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md),
[approved oop-v2 / review-process-1](../../approval.md), M1 unaccepted.
Original ticket baseline: `f2929e79cfd5a68f670862775053ae85ba9582b5`.
Exact 36-file corpus/guidance identity:
`ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23`.
It is SHA-256 of the all-file path→SHA-256 mapping serialized by
`json.dumps(manifest, sort_keys=True)` (default separators, no trailing newline).
The [full manifest](source-manifest.json) and [snapshot](snapshot/REVIEW.md) retain
actual bytes independently of any eventual implementation commit.

## Original inputs and actual assignments

- [Declaration/key](declaration.md), fixed **before** dispatch;
  [timestamp/hash capture](declaration-capture.json) records 16:22:16.526151 UTC.
- [Assignments](assignments.json) retain independent fork-none GPT-6.1 Sol High
  configuration, <=250000 active-context target. Spec dispatched 16:22:35.384 UTC,
  Standards 16:22:48.070 UTC. Both inspected all eight cases.
- [Spec dispatch serialization](spec-g1-assignment.json) and
  [Standards dispatch serialization](standards-g1-assignment.json) preserve the
  original log records. Message values are opaque encrypted text, not readable
  plaintext or proof of delivery.
- [Spec readable input](spec-g1-input.txt) and [Standards readable input](standards-g1-input.txt)
  are reviewer-attested transcriptions of the initial assignment actually received,
  saved on evidence-only followup. [Capture provenance](capture-provenance.json)
  distinguishes original opaque records and readable preservation.
- [Spec original report](spec-g1-raw.md), original reviewer-assigned review ID
  `development-source-G1`, report `spec-01`;
  [Standards original report](standards-g1-raw.md), review ID
  `development-review-19-g1`, report `standards-original-01`.
  Reports retain their original identities and statements; they are linked as one
  evaluation trial rather than retroactively renamed as a real ticket assessment.
  These raw files are byte-exact first plaintext `final_answer` content from the
  verified child sessions. Separate reviewer-preserved copies differ only by a
  terminal newline; neither replaces or edits the original content.
- [Spec selected session evidence](spec-g1-tool-evidence.json),
  [Standards selected session evidence](standards-g1-tool-evidence.json),
  [capture/digests](review-capture.json), and [evidence-only followups](capture-followups.json).
  Opaque fields remain opaque; full unrelated developer context is excluded.
  [Readable followup transcription](capture-followups-readable.json) retains the
  implementer's sent messages separately from their opaque serialized records.
  [Original-tool supplement](review-capture-supplement.json) preserves all actual
  `custom_tool_call`/output and received `agent_message` records in
  [Spec source records](spec-g1-source-records.json) and
  [Standards source records](standards-g1-source-records.json). The first narrow
  collector omitted those record types; its saved output remains unchanged.
  Received-message wrappers are plaintext but task payloads remain encrypted.
  [Collector history](collector-history.json) retains the failed attempt to compare
  an empty plaintext payload to the readable input and its corrected limitation.

Reviewers received only `/tmp/development-review-19-g1`, with files 0444 and
directories 0555, ordinary case contracts and frozen scoped guidance. No key,
builder, ticket19/spec key passages, prior fixture reports or sibling report was
supplied. Missing outgoing guidance links were explicitly outside input scope.
Both attest their reads stayed inside the snapshot. Shared filesystem access is
technically possible; permissions/instructions do not demonstrate backend-enforced
isolation. Collector verifies supplied/retained bytes unchanged after assessment.

## Outcome, history and reproduction

[Expected/observed adjudication](results.md) explains every case, classification,
remedy and limitation. Both axes detected a3/c2/e4/g1 with source-specific blocking
findings and justified b7/d9/f6/h8 as clean. [Full-key fixture history](finding-history.md)
retains all eight original open seed observations. No actual ticket_harness finding
is created/fixed by this evidence. No required judgment miss, false blocker, optional
suggestion, guidance correction or full-corpus retrial occurred. This records one
observation per axis per case, not repeated reliability evidence.

[Published guidance reference](../../../../docs/agents/reviewer-evaluation.md)
carries G1 through planning, implementation/repair and both handoff branches.
Refactors 20–24 must obtain new whole-ticket reviews; real M1 needs actual cumulative
source review and human QA. The h8 scalar-value assumption, Spec aggregate-audit
limitation, encrypted capture and unavailable backend enforcement remain explicit.

[build_corpus.py](build_corpus.py) is evaluator-only construction history. It refuses
to overwrite the declared snapshot; never supply it or this index/key/results to a
blinded corpus reviewer. [capture_reviews.py](capture_reviews.py) extracts selected
real session records and reviewer-preserved files without overwriting originals.
Neither script generates findings or establishes judgment quality. The
[implementation evidence](../19-implementation-report.md), [checks](../19-checks.log)
and [check helper](../19-check.py) record standalone document/skill/source/routing
validation. No production code/tests/dependencies or runtime schemas changed, no
harness run/backend, promotion, acceptance or push was launched. Runtime delivery
and enforcement remain tickets 33/34.
