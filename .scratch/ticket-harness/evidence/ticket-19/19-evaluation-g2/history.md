# Preserved G1 correction and G2 trial history

The original [G1 history](../19-evaluation/finding-history.md), declaration,
snapshot, reports, results, implementation report and checks remain byte-identical
to rejected commit `e90abb64ab95c5b15cdb0949b03c6a948365339b`. Events below add later
observations rather than editing their classifications. Actual ticket finding
history is separately [review-ticket-19](../19-finding-history.md).

## E01 — Correct G1 invalid-control and adjudication result

Actor: `/root/repair19`, authorized Medium evaluation repair. Scope: G1 corpus
`ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23`, supplied under
original baseline `f2929e79cfd5a68f670862775053ae85ba9582b5` and rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`.

The original h8 contract explicitly promises caller-input dictionary isolation.
Its constructor and transition retain identity/revision references; returned
snapshots are shallow. The [original implementation Spec F1](../19-review-spec.md#f1--blocking-h8-cannot-supply-the-required-fourth-acceptable-control-under-its-frozen-contract)
and [original observation](../19-review-spec-h8-observation.json) establish the
violation with dictionary values accepted by the source. The two original corpus
reviewers mention a scalar assumption without contract or validation support;
the [original evaluator](../19-evaluation/results.md) calls it a match. That clean
classification is an invalid-control/adjudication failure. G1 supplies only three
acceptable controls. The original four seeded required detections remain supported;
h8 is not retroactively recast as a predeclared fifth required concern.

This event supersedes G1's h8 match/no-mismatch/success statements, including the
historical implementation report, original evaluator result and original guidance
summary. It preserves those exact originals. The initial implementation Standards
report's [different judgment](../19-review-standards.md) remains unchanged too.
The actual full blocker key is `review-ticket-19/spec-01/F1`, still open pending
independent verification of the repair commit. No human waiver, blocker deferral,
changed contract or QA acceptance is requested/inferred.

## E02 — Declare complete G2 source and guidance before fresh evaluation

Actor: `/root/repair19`. [Timestamp and declaration hashes](declaration-capture.json)
precede both [actual assignments](assignments.json). The
[complete eight-case key](declaration.md) and [36-file manifest](source-manifest.json)
identify G2 corpus `ae5ba62e56cb12c1f58f6d5098ac357faf5f1d8a8815383cb1d4471acc5a467c`.
All eight contracts and all non-h8 sources remain byte-identical. The
[two-file delta](revision-delta.json) corrects h8 input/observation copying and adds
one generic paragraph to ownership-review guidance. Upstream skills remain unchanged.
The new guidance requires contract/validation support for narrower assumptions
when judging explicit guarantees; it includes no case identities or answer key.

Both source and guidance change together. A successful G2 observation cannot
isolate guidance wording's effect, demonstrate detection of the unchanged flawed
h8, or establish general reviewer effectiveness. This is a corrected valid control
under the same promise, assessed with final guidance on the whole final corpus.
[One disposable observation](control-observation.json) contrasts original versus
corrected dictionary/list aliases and invalid terminal transitions; it is supporting
fixture evidence, not the required reviewer judgment or production coverage.

Fresh independent Spec and Standards assignments each inspect all eight cases on
the neutral read-only snapshot. Their known readable author prompts are saved
before dispatch; no evaluator key, prior outcomes, repair/whole-ticket report,
sibling output or original ticket/spec is supplied. Backend delivery/enforcement,
measured active context and hard 250000-token enforcement are unavailable. Snapshot
permission bits and scope instructions remain advisory filesystem isolation.

## E03 — Preserve failed C2 trial and newly identified invalid controls

Actor: `/root/repair19`, after both original reports were captured. One full-corpus
report per axis, no re-review. [Actual report capture](review-capture.json) and
[per-case adjudication](results.md) preserve all seven original Spec and five
original Standards full keys, including their different d9/f6 interpretations.
All four declared seeded concerns are detected on relevant axes. h8's corrected
source is clean under both assessments. b7's path trimming, d9's missing dependency
operands and f6's unbounded timeout reveal additional valid source/contract breaches;
C2 is therefore another failed invalid-control trial. These are supported findings,
not false blockers. No original report or declaration is revised to match them.

This supplements E01's initial observation that h8 alone defeated G1's fourth
control: b7/d9/f6 source and contracts are shared by G1 and C2, so these later
observations also defeat any current full-validity claim for those original control
slots. G1's original clean reports/classifications remain historical. The four
seeded required concern detections are not invalidated, and extra defects are not
retroactively added to their declared required key.

The evaluator additionally reproduced a valid 1200-node forward dependency chain
raising RecursionError in the unchanged parser, which has no graph-depth bound.
This is a separate [preflight observation](../19-repair-control-preflight-results.json),
not an actual G2 reviewer finding or a further blind trial. Candidate corrections
preserve all contracts: root record-terminator decoding; nonempty dependency-token
checks and iterative local graph traversal; finite-timeout validation without
positive-only policy. Final G2 guidance remains unchanged for the next complete
corpus. All four candidate controls receive substantive preflight and bounded
observations before that next declaration; original source is never edited.
