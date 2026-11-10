# G1 expected / observed evaluation

Evaluator: `/root/implement_19`, after both independent original reports arrived.
Compare the [pre-assignment key](declaration.md) to [Spec original](spec-g1-raw.md)
and [Standards original](standards-g1-raw.md), not to finding counts. Both inspected
all eight source cases. Relevant-axis observations below establish this finite
trial's judgment outcome; mechanical checks merely audit retained identity.

| Case / declared expectation | Observed reasoning and classification | Evaluator judgment |
| --- | --- | --- |
| a3 / required Spec concern | Spec F1 traces shared pre-save dictionaries, independent JSON-loaded arrays at run.py:23–26, canonical-only invalidation at :13–16 and stale eligibility in qa.py:1–3. Blocking consequence is restored QA approval of invalidated evidence. Remedy reconstructs canonical references preserving schema and repeated records. Standards A3-F1 independently agrees. | Match. Directly demonstrates the required restored-evidence concern with a bounded repair; neither asks QA to compensate for broken ownership. |
| b7 / acceptable both | Both trace caller.py's process adapter into validate/checked; nonzero exit, branch, dirty/untracked, commit and ancestry checks remain local to git_ops.py:3–18. Both explain small caller interface and cohesive functional implementation, no saved state. Neither requires classes, frameworks or richer diagnostics. | Match. No unsupported blocker. This short example does not calibrate every large cohesive Git function or prove actual Git execution. |
| c2 / required Spec concern | Spec F2 identifies checking.py:8 selecting history[-1] after ID validation, execution.py forwarding history, and ID-based consumers. Delayed A after B and unknown-ID mutation are concrete failures. Remedy keeps checking pure and execution/identified Attempt responsible for attachment. Standards C2-F1 agrees. | Match. Correct ownership and attribution, proportionate remedy; replacing positional selection with checker-owned ID mutation alone would not satisfy the contract. |
| d9 / acceptable both | Both inspect frozen values, order-preserving parse, duplicate-ID lookup, DFS active/completed sets, missing dependency and cycle rejection. Local mutation stays invocation-local; returned values are immutable. Neither demands a parser class. | Match. No blocker or optional suggestion. Malformed syntax beyond the stated grammar is not silently added as a requirement. |
| e4 / required Standards concern | Standards E4-F1 names repair.py:2–8 as a second writer duplicating Attempt.submit and worker.py's correct delegation. It explicitly distinguishes present matching assignments from the violated single-owner contract and policy propagation risk. Remedy delegates repair to existing submit. Spec F3 agrees. | Match. A source-specific ownership blocker, not a class/function preference or invented present behavioral divergence. |
| f6 / acceptable both | Both follow same-directory temporary creation, close-before-replace and finally cleanup; argv-based capture/check=False/timeout pass-through. They apply documented exclusions for fsync/metadata and no domain state. | Match. No unsupported blocker. Existing-directory, finite-timeout and ordinary filesystem/process assumptions remain explicit; no runtime failure injection was performed. |
| g1 / required Standards concern | Standards G1-F1 traces None fields in preparation.py:2–10, CLI-owned normalization/default/validation and resume.py returning incomplete state. Broken resumed fields and unrejected nonpositive limit establish correctness plus hidden caller protocol. Remedy completes validation/construction inside preparation for both callers. Spec F4 agrees. | Match. Required external-initialization concern detected with exact affected flows and a small owner correction. |
| h8 / acceptable both | Both trace pre-mutation checks, one internal mirrored transition and copied snapshots; caller delegates. They justify the small class's real invariant ownership. Both disclose shallow-copy behavior for unspecified nested mutable identity/revision values; no such flow is supplied, so neither invents a blocker. | Match within ordinary scalar domain values. The type ambiguity is a finite limitation, not proof of nested-payload isolation and not an unsupported blocking finding. |

There are no required judgment misses, unsupported blockers, optional suggestions,
or unresolved classification/remedy mismatches in G1. Eight fixture findings remain
open in their original reports—four per axis—because the corpus deliberately retains
its problems. They are not actual ticket_harness findings or barriers to this
evaluation's completion. Their [full-key history](finding-history.md) preserves
scope and does not mark them fixed, defer blockers without authority or invent
human acceptance. No seeded fixture was repaired or silently replaced.

## Actual repetitions, revisions and non-judgment limits

One declared corpus; one guidance version G1; one independent Spec assignment and
one independent Standards assignment, each covering all eight cases. Thus each
case has one observation per axis, not repeated statistical trials. No judgment
failure triggered a correction/retrial. Evidence-only followups saved prior reports
and received inputs; these are not additional reviews or reruns. All original
reports, opaque session records, plaintext preservation attestations and hashes
remain available. No failed reviewer trials were discarded because none occurred.

Spec computed a separately defined compact cases-only aggregate rather than the
assignment's aggregate. This is an explicitly disclosed identity-audit limitation,
not a detection miss: its 36 individual file digests identify the same snapshot.
Standards reproduced the exact all-file aggregate using sorted JSON with default
separators, and the collector independently verifies every byte against the
predeclared manifest. The original Spec report remains unchanged.

Serialized dispatch-message fields are encrypted. Those opaque captures are not
usable plaintext instruction-delivery proof. Reviewers preserved readable initial
inputs and reports on evidence-only followup, without answer-key information.
The collector then found the original assistant reports in plaintext session
`final_answer` items and captured their exact content directly. Its earlier
unexecuted final-capture branch incorrectly looked for phase `final`; that collector
error was corrected before original report capture. The reviewer-preserved reports
match original content apart from one terminal newline, and both representations
are retained. Readable initial inputs remain reviewer-attested transcriptions,
not byte-verified decrypted dispatches. [Capture provenance](capture-provenance.json)
keeps these distinctions explicit; none proves backend instruction effectiveness.
The initial tool collector selected only ordinary function-call records; the
[supplement](review-capture-supplement.json) retains the actual custom-tool calls,
outputs and received-message records without changing earlier captures. An attempted
plaintext comparison failed because received payloads are also encrypted; the
collector records that limit rather than asserting a match. This was a collection
failure, not a reviewer judgment failure or guidance correction.

## Guidance and extrapolation

G1 is the frozen substantive guidance at baseline f2929e7, identified file-by-file
in [source-manifest.json](source-manifest.json). No substantive guidance correction
was made. New planning/worker/handoff pointers publish the result and its limits;
they were not supplied to the blinded reviewers and do not claim fresh judgment
validation of those authoring routes. Document/skill/routing checks and the later
independent implementation reviews assess the routing addition separately.

The corpus is eight short synthetic designs under explicit contracts, selected by
the evaluator. It does not assess actual package architecture, long-file attention,
production tests, later refactor correctness, unconstrained inputs, or every possible
failure variant. No randomization, repeated-trial reliability, guaranteed future
detection or general quality rate is inferred. Real refactors 20–24 require their
own whole-ticket reviews and retained finding/decision history; real M1 needs its
actual cumulative assessment and explicit human QA. Backend role/instruction
availability, delivery and enforcement belong to runtime tickets 33/34. No harness
run, runtime schema change or production private-module tests were used here.
