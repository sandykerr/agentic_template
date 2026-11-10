# Evaluated development reviewers

Use this reference for ownership-refactor 20–24 implementation, repair, review and
handoff context. Apply [ownership/scope](ownership-review.md),
[review records](review-records.md), [architecture checkpoints](architecture-checkpoints.md)
and approved role-specific design/testing guidance. Existing planning and both
next-handoff branches carry the exact version, corpus, failures and finite limits;
corpus evidence does not replace review of new source.

## Current guidance and exact final corpus

**Guidance G2**, unchanged since the C2 trial, is paired with **corpus C4**.
The [complete pre-assignment declaration](../../.scratch/ticket-harness/evidence/19-evaluation-g4/declaration.md),
[36-file source/guidance manifest](../../.scratch/ticket-harness/evidence/19-evaluation-g4/source-manifest.json)
and [neutral retained snapshot](../../.scratch/ticket-harness/evidence/19-evaluation-g4/snapshot/REVIEW.md)
identify final aggregate
`bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197`.
The directory suffixes `g3`/`g4` identify corpus stages, not additional guidance
revisions. C4 contains all eight original case contracts, four required concerns
and four controls; source corrections and each preceding failed trial are explicit.

The [final evaluation record](../../.scratch/ticket-harness/evidence/19-evaluation-g4/README.md)
retains known readable prompts saved before dispatch, actual fresh settings, exact
original independent reports, tool/source evidence, per-case adjudication and
limits. [Final per-case adjudication](../../.scratch/ticket-harness/evidence/19-evaluation-g4/results.md)
records all four required concerns detected on declared axes, supported clean
control reasoning and no unsupported blocker or optional suggestion. C4's finite
criteria pass. Actual ticket completion and independent whole-ticket repair verification remain
separate from this finite corpus result.

## Preserved failures and revisions

No historical full-corpus pass stands. Original reports, declarations, source,
classifications, evaluator results, histories, implementation report and checks
remain preserved, including earlier incorrect success claims. The current
[repair record](../../.scratch/ticket-harness/evidence/19-repair-report.md) and
[implementation finding history](../../.scratch/ticket-harness/evidence/19-finding-history.md)
supersede those claims without rewriting their evidence.

| Corpus / guidance | Original observation and later adjudication |
| --- | --- |
| [C1 / G1](../../.scratch/ticket-harness/evidence/19-evaluation/README.md) | Both axes detect the four required seeds and call controls clean. Initial implementation Spec F1 demonstrates h8 violates its dictionary-isolation contract; both corpus reviewers/evaluator used an unsupported scalar restriction. Later b7/d9/f6 findings also apply to their identical original bytes. Preserve the different clean initial implementation Standards judgment. [Correction](../../.scratch/ticket-harness/evidence/19-evaluation-g2/history.md). |
| [C2 / G2](../../.scratch/ticket-harness/evidence/19-evaluation-g2/results.md) | h8 and one generic guidance paragraph change. Four seeds detected; both axes identify b7 path trimming. Spec also identifies d9 missing operands and f6 unbounded timeout; Standards' differing interpretations remain original. These are supported contract findings, not false blockers; controls remain invalid. Separate evaluator preflight also demonstrates unbounded parser depth fails a valid chain. |
| [C3 / G2](../../.scratch/ticket-harness/evidence/19-evaluation-g3/results.md) | Source-only b7/d9/f6 corrections, unchanged contracts/guidance. Both axes detect four seeds and call controls clean. Independent root preflight exposes b7 caller universal-newline corruption of a valid CR path, so C3 still fails. This is a separate evaluator observation, not a C3 reviewer finding; active reviewers received none of it. |
| [C4 / G2](../../.scratch/ticket-harness/evidence/19-evaluation-g4/declaration.md) | Caller-only source correction preserves filesystem path characters through byte capture and explicit text decoding. Original contracts, seeds, other controls and guidance remain unchanged. Fresh complete-source observations belong only to this exact corpus; no retrospective pass is inferred. |

G1 freezes baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`. G2 adds exactly one
paragraph in the owning ownership-review contract: check explicit guarantees
against accepted inputs/aliases; narrower assumptions need contract or enforced
validation support. The [first delta](../../.scratch/ticket-harness/evidence/19-evaluation-g2/revision-delta.json)
identifies this guidance change separately from h8's copying correction. The
[C3 delta](../../.scratch/ticket-harness/evidence/19-evaluation-g3/revision-delta.json)
and [C4 delta](../../.scratch/ticket-harness/evidence/19-evaluation-g4/revision-delta.json)
are source-only; every original case contract and required concern source remains
unchanged. Upstream skills and production behavior/schemas remain unchanged.

C1 to C2 changes both source and guidance; passing corrected controls cannot
isolate wording's effect or show detection of an unchanged original flaw. C3/C4
add no further guidance correction. The source fixes avoid input-contract
narrowing: deep alias isolation, root-character preservation, nonempty dependency
operands, iterative graph validation and finite timeout enforcement. Bounded
[evaluator control preflight](../../.scratch/ticket-harness/evidence/19-repair-control-preflight-results.json)
and [exact caller/path preflight](../../.scratch/ticket-harness/evidence/19-repair-path-preflight-results.json)
support source validity but do not establish reviewer judgment or exhaustive behavior.

## Use in subsequent work and limits

Supply both fresh reviewers with approved contracts, original ticket baseline,
exact committed source, affected callers/owners/writers/readers, save/restore and
invalidation paths, coverage/check evidence and full prior finding keys/history.
Apply exact G2 substantive reasoning/reporting guidance. Corpus classifications
are evaluator material, not an answer pattern to reproduce on new source. Record
actual inspected scope, clean reasoning, omissions and assumptions. Optional
suggestions remain optional; authorized in-scope repairs proceed under existing
bounds. Consequential design/risk/scope decisions and exact-candidate acceptance
remain human-owned.

Substantive guidance/source corrections need identified new versions and complete
final-corpus evaluation before claiming success. Preserve invalid controls,
adjudication failures, misses, supported extra concerns and unsupported blockers;
a narrower assumption or disposition label cannot waive a guarantee. Carry unresolved
actual keys, missing/stale reports and human decisions with the next responsible
action. Frozen fixture seeds remain open at their own source and are not actual
harness blockers. Real refactors 20–24 require their own whole-ticket reviews;
M1 feature-start provenance/all-package cumulative assessment and explicit human
QA remain unperformed.

Finite history: four complete eight-case corpora, two guidance versions, one
independent Spec and one independent Standards report per corpus. G1 preservation
followups add no trials. Sources evolve between stages, so these are not four
identical-corpus reliability repetitions. No general detection rate, guaranteed
future quality, large-file attention, actual package architecture or runtime
behavior follows. Known pre-saved author prompts and actual configured/observed
settings do not prove decrypted instruction delivery/effectiveness, enforced
filesystem isolation or hard context limits. Backend telemetry/measured active
context is unavailable; <=250000 active-context tokens is advisory. Tickets 33/34
separately prove runtime delivery/enforcement and behavior. No harness run,
production private-module tests, milestone acceptance, promotion or push occurs.
