# G2 complete development reviewer evaluation

Origin: [ticket 19](../../issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md),
approved oop-v2 / review-process-1, M1 unaccepted. Fixed original whole-ticket baseline
`f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source `e90abb64ab95c5b15cdb0949b03c6a948365339b`.
The [original G1 evaluation](../19-evaluation/README.md) remains preserved verbatim;
[correction/history](history.md) supersedes its invalid fourth-control conclusion.
Actual [implementation finding history](../19-finding-history.md) retains
`review-ticket-19/spec-01/F1`; independent repair verification is pending.

[Declared complete corpus/key](declaration.md), [pre-dispatch timestamp/hash capture](declaration-capture.json),
[36-file source/guidance manifest](source-manifest.json), [neutral snapshot](snapshot/REVIEW.md)
and [two-file revision delta](revision-delta.json) identify G2 separately from G1.
Aggregate `ae5ba62e56cb12c1f58f6d5098ac357faf5f1d8a8815383cb1d4471acc5a467c`
is SHA-256 of `json.dumps(manifest, sort_keys=True)` with default separators and no
trailing newline. All contracts and all source except h8/attempt.py are unchanged.
The single generic ownership-review paragraph is the only substantive guidance
revision. Source and guidance change together, preventing causal attribution of
any fresh outcome to wording alone.

## Actual assignments and preservation

[Settings/assignments](assignments.json) retain fresh independently configured
fork-none GPT-6.1 Sol High roles and the <=250000 active-context advisory target.
[Spec known readable author prompt](spec-g2-input.txt) and
[Standards known readable author prompt](standards-g2-input.txt) were saved by the
builder before dispatch, then passed verbatim as the spawn messages.
[Spec original dispatch](spec-g2-dispatch.json) and
[Standards original dispatch](standards-g2-dispatch.json) retain actual timestamped
settings; serialized message fields may be encrypted. These known author inputs
avoid reconstruction from opaque logs; they do not prove decrypted delivery or
backend instruction effectiveness. The readable prompts contain neither the answer
key nor prior results/repair material. Both roles receive only the same neutral
read-only 36-file snapshot and their respective assignment, with no sibling output.

Evaluation lifecycle: **completed; failed invalid-control trial**. The
[Spec original](spec-g2-raw.md) contains seven blockers and the
[Standards original](standards-g2-raw.md) five. Both detect all four required seeds;
additional b7/d9/f6 contract breaches prevent a passing control corpus. Their
different d9/f6 interpretations remain preserved. [Per-case adjudication](results.md)
explains every match/mismatch from source and contract, not counts. One full-corpus
report per axis occurred. [Capture/digests](review-capture.json) and
[provenance](capture-provenance.json) retain exact original finals and actual
[Spec](spec-g2-source-records.json) / [Standards](standards-g2-source-records.json)
source/settings/tool/received records. Reviewer-generated manifests and a Spec
capture artifact are also retained; no followup judgment occurred.
[Capture helper](capture_reviews_g2.py) refuses changed existing artifacts and
extracts original plaintext finals, model settings and actual calls/outputs/received
records from specifically identified child sessions. It never generates findings.

[Fixture observation](control-observation.json) retains actual old/new nested
input/snapshot mutations and invalid terminal transitions with source hashes.
[Observation helper](observe_control_g2.py) refuses an existing result. It is one
disposable example, not a production test suite or evidence of reviewer judgment.
[Builder](build_corpus_g2.py) refuses an existing G2 destination and preserves G1;
never provide this evaluator-only index, declaration, builder or history to the
blinded corpus reviewers.

## Limits and subsequent use

At this frozen C2 record, two corpora and two guidance versions have been
assessed: G1/C1 and G2/C2, all eight cases with one original report per axis each. G1 and C2 are failed control/adjudication trials even though their four
seed detections remain valid. No trial/report/source is discarded. No reliability
rate, guaranteed future detection, real-package assessment or large-source attention
claim follows. Final G2 source differs from the flawed original h8; a clean new
control cannot demonstrate new detection of that old flaw.

The [current guidance reference](../../../../docs/agents/reviewer-evaluation.md)
routes exact versions, results and limits through planning, implementation/repair
and both next-handoff branches. Real refactors 20–24 still require their own
whole-ticket reviews. M1 cumulative all-package review, actual feature-start
provenance and explicit human QA remain unperformed. Actual ticket F1 remains open
until the parent obtains independent exact-commit whole-ticket verification;
these corpus reviewers do not perform that verification.

No production owner/writer/runtime schema/backend/test/package changes or harness
run occur. Runtime instruction delivery/enforcement belongs to 33/34. Requested
and observed settings are configuration evidence; measured active context, hard
context enforcement and backend telemetry are unavailable. Read-only snapshot
permissions/scope instructions do not establish backend-enforced isolation. No
consequential human decision, milestone acceptance, promotion or push is inferred.
