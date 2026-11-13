# Append-only G1 fixture finding history

These are original findings against the declared synthetic snapshot, not actual
harness defects. All refer to corpus identity
`ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23`.
Actor for E01–E08: `/root/implement_19`, evaluator, after both initial reports.
Original reports remain immutable; this history records observation/scope only.

| Event | Full finding key | Disposition / source-specific reason | Original evidence |
| --- | --- | --- | --- |
| E01 | development-source-G1/spec-01/F1 | open in fixture; detached restored references are a3's declared concern | [Spec](spec-g1-raw.md#f1--blocking-reconstruct-canonical-gate-references-on-restore) |
| E02 | development-source-G1/spec-01/F2 | open in fixture; positional handoff selection is c2's declared concern | [Spec](spec-g1-raw.md#f2--blocking-attach-a-handoff-to-its-identified-attempt) |
| E03 | development-source-G1/spec-01/F3 | open in fixture; repair's duplicate record edits violate e4 ownership | [Spec](spec-g1-raw.md#f3--blocking-make-repair-submission-delegate-to-attempt) |
| E04 | development-source-G1/spec-01/F4 | open in fixture; incomplete prepared state/external initialization is g1's declared concern | [Spec](spec-g1-raw.md#f4--blocking-return-complete-validated-prepared-state-from-preparation) |
| E05 | development-review-19-g1/standards-original-01/A3-F1 | open in fixture; canonical restoration breach matches a3 | [Standards](standards-g1-raw.md) |
| E06 | development-review-19-g1/standards-original-01/C2-F1 | open in fixture; checker selects/mutates latest owner instead of identified attempt | [Standards](standards-g1-raw.md) |
| E07 | development-review-19-g1/standards-original-01/E4-F1 | open in fixture; extra repair writer duplicates submission policy | [Standards](standards-g1-raw.md) |
| E08 | development-review-19-g1/standards-original-01/G1-F1 | open in fixture; caller completes preparation and resume receives None fields | [Standards](standards-g1-raw.md) |

No repair ticket/commit, fix verification, deferral, risk acceptance, decision,
amendment or milestone assessment exists for these intentionally retained fixture
findings; those links are not applicable to this detection evaluation. They remain
open against their exact source. The next responsible action is for future actual
refactor reviewers to assess actual source, not to repair these frozen seeds.
[Evaluator reasoning](results.md) records expected/observed matches and the h8
input-type limitation. No actual implementation-ticket finding is dispositioned by
this corpus history; the parent's independent Spec/Standards ticket review remains
required. No human QA or milestone authority is inferred.
