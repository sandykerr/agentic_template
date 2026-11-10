# G2 declared corpus — evaluator only

Declared before any G2 reviewer assignment. Fixed original whole-ticket baseline:
`f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source:
`e90abb64ab95c5b15cdb0949b03c6a948365339b`.
Final corpus SHA-256 over the sorted path/digest JSON mapping: `ae5ba62e56cb12c1f58f6d5098ac357faf5f1d8a8815383cb1d4471acc5a467c`.
[Exact 36-file manifest](source-manifest.json), [neutral snapshot](snapshot/REVIEW.md),
[explicit revision delta](revision-delta.json).

This is a new complete eight-case corpus and guidance G2, not a replacement of
[G1's declaration](../19-evaluation/declaration.md), source, reports or outcome.
G1's h8 control violates its explicit caller-input isolation guarantee; both
reviewers disclosed a scalar assumption unsupported by contract or validation.
Its clean classification and evaluator match are failed observations, retained
verbatim. The original four concern detections remain valid. The implementation
blocker is `review-ticket-19/spec-01/F1`; no human waiver is requested or inferred.

G2 changes only h8/attempt.py and guidance/docs/agents/ownership-review.md.
All eight case CONTRACT.md files and all other source files are byte-identical
to G1. h8 now deep-copies constructor inputs, transitions and both observations,
including nested dictionaries; it prepares both private values before assignment.
The owned-transition control thus keeps the original isolation promise with no
new caller restriction. G2 ownership guidance adds one generic paragraph requiring
explicit guarantees to be judged against accepted inputs and aliases, and narrower
assumptions to have a contract or enforced-validation basis. This addresses the
observed assumption failure without teaching a case ID, remedy or expected result.
The exact paragraph/digest are disclosed separately in revision-delta.json and the
repair evidence; upstream skills remain unchanged.

| Case | Declared kind / required axis | Expected observation and rationale |
| --- | --- | --- |
| a3 | Required concern / Spec | Restored verified dictionaries detach from canonical gates; invalidation leaves QA stale. Block and rebuild canonical references preserving saved keys. Standards may also detect. |
| b7 | Acceptable control / both | Cohesive Git validation owns failures, branch, dirty state and ancestry behind one operation; no class or richer diagnostic requirement. |
| c2 | Required concern / Spec | Checking attaches to history[-1] despite supplied attempt ID; delayed/unknown reports mutate wrong attempt. Block and restore validation-result/identified-owner operation split. |
| d9 | Acceptable control / both | Pure immutable parsing and local graph traversal own validation and ordering; no lifecycle state or object requirement. |
| e4 | Required concern / Standards | Repair duplicates owning submission guard/mirrored edits; block extra writer/policy propagation breach and delegate to existing submit. |
| f6 | Acceptable control / both | Atomic file replacement and captured argv/process primitives satisfy stated mechanics, failure and timeout contracts; no domain state or excluded fsync demand. |
| g1 | Required concern / Standards | Preparation returns incomplete fields, CLI finishes privately and resume is incomplete; block hidden caller initialization protocol and complete checked result in preparation. |
| h8 | Acceptable control / both | Attempt owns mirrored transitions, validates before mutation, copies inputs and observations deeply; caller delegates. Original dictionary-isolation promise now holds without an assumed scalar restriction. |

Both fresh independent GPT-6.1 Sol High fork-none axes assess all eight cases once
under exact final G2 guidance. Required concern detections need source evidence,
correct declared relevant axis, justified blocking classification and proportionate
remedy. Controls receive no unsupported blocker. A valid contract breach found on
a nominal control is an evaluator/corpus failure, not an unsupported reviewer
blocker. Optional observations are adjudicated from evidence. Explain every match
and mismatch, including additional concerns; finding counts alone do not score.
Retain every failure/report/version. Any further correction requires a newly declared
complete corpus and fresh final-guidance evaluation, without rewriting this trial.

Reviewers receive only the read-only neutral snapshot and pre-saved axis assignment,
never this key/builder, G1 outcomes, repair/review material, ticket19/spec or sibling
report. Readable prompts and hashes are saved before dispatch. Preserve actual
settings, raw finals, tool/source inspection records and source hashes pre/post.
No harness run or production tests. Target <=250000 active-context tokens advisory;
hard enforcement, backend telemetry and measured active context unavailable.
Filesystem isolation remains advisory despite read-only source permission bits.
Finite claim: two guidance versions, two complete eight-case corpora, one report
per axis per version; no reliability rate, future-detection guarantee or runtime
instruction-delivery effectiveness. Later refactors and M1 cumulative QA are separate.
