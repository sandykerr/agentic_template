# Ticket 19 evidence

Original evidence remains in its nested structure, except for the explicitly
retired mixed command captures described below.
Original links, captured paths and scripts retain the historical layout; consult
the [historical path mapping](../README.md#historical-paths) when following them.
Historical scripts are not ready to rerun from these locations.

- [Completion](19-completion.md), [original implementation and coverage](19-implementation-report.md), [final repair report](19-repair-c5-report.md), [final checks](19-repair-c5-checks.log), [final source/check result](19-repair-c5-check-results-20261110T180103445335Z.json).
- [All three independent review rounds](19-review-navigation.md), [append-only actual finding history](19-finding-history.md), [current assessment](../../reviews/ticket-19.md); capture manifests for [initial](19-review-capture.json), [second](19-review-round2-capture.json) and [final](19-review-round3-capture.json) rounds.
- Final original [Spec](19-review-spec-03.md) and [Standards](19-review-standards-03.md) reports; second-round [Spec retirement locator](19-review-round2-spec-identities.json) and [Standards retirement locator](19-review-round2-standards-identities.json).

All five corpora retain their distinct source and guidance snapshots, original reports, failed trials and superseded conclusions. The neutral snapshots remain unchanged.

| Corpus | Overview | Results | History |
| --- | --- | --- | --- |
| C1 / G1 | [Original evaluation](19-evaluation/README.md) | [Adjudication](19-evaluation/results.md) | [History](19-evaluation/finding-history.md) |
| C2 / G2 | [Second corpus](19-evaluation-g2/README.md) | [Adjudication](19-evaluation-g2/results.md) | [History](19-evaluation-g2/history.md) |
| C3 / G2 | [Third corpus](19-evaluation-g3/README.md) | [Adjudication](19-evaluation-g3/results.md) | [History](19-evaluation-g3/history.md) |
| C4 / G2 | [Fourth corpus](19-evaluation-g4/README.md) | [Adjudication](19-evaluation-g4/results.md) | [History](19-evaluation-g4/history.md) |
| C5 / G2 | [Final corpus](19-evaluation-g5/README.md) | [Adjudication](19-evaluation-g5/results.md) | [History](19-evaluation-g5/history.md) |

- C5 [evaluator declaration/key](19-evaluation-g5/declaration.md), [advance capture](19-evaluation-g5/declaration-capture.json), [source manifest](19-evaluation-g5/source-manifest.json), [neutral reviewer snapshot](19-evaluation-g5/snapshot/REVIEW.md), [actual assignments](19-evaluation-g5/assignments.json), original [Spec](19-evaluation-g5/spec-c5-raw.md) and [Standards](19-evaluation-g5/standards-c5-raw.md) reports, [report capture](19-evaluation-g5/review-capture.json).
- [Preparation-only skill observation](19-repair-c5-skill-observation.md), [probe capture](19-repair-c5-skill-probe/capture.json), [actual tested skill snapshot](19-repair-c5-skill-probe/inputs/SKILL.md), [tested/final byte delta](19-repair-c5-skill-final-delta.json). This probe did not dispatch calibration reviewers.

## Retired evidence

On 2026-11-13 the human-authorized C1–C10 cleanup retired two mixed command
captures after root independently checked the extracts. The 17,029,165-byte Spec
gzip was deleted; the 4,341,657-byte Standards payload was replaced with an
explicit retirement locator. The former Spec gzip locator now states retirement.
These locators and extracts have their own identities and are not original captures.

- [Lossy Spec extract](19-review-round2-spec-identities-retirement-extract.json): all 15 original non-command fields, including review/source/settings/instruction identities, corpus declarations and prior-finding verification.
- [Lossy Standards extract](19-review-round2-standards-identities-retirement-extract.json): all 24 original non-command fields, including source/instruction identities, observations, original report identity and the narrow whitespace exception.

The extracts retain command counts/exits, exact non-show command arguments and
output identities, grouped `git show` revision metadata and the sole known C3
EOF-whitespace failure explanation. Bulk stdout/stderr and individual git-show
target lists were deliberately discarded. Original stored/decompressed hashes,
sizes and the previous Spec locator remain historical provenance inside the
extracts; the old gzip restoration command no longer works. This is lossy
retirement, with no lossless replacement archive.

The lasting review result remains distinct: round-two Spec independently verified
the h8 repair and found the b7 branch/tag control defect; round-two Standards
retains its different clean judgment. Final independent reports revalidate both
actual full finding keys. All C1–C5 corpora, neutral source/guidance snapshots,
original judgments, failed-trial conclusions, actual reports and finding histories
remain untouched. The exact C3 saved-report EOF exception remains narrow.

Read-only source checks matched all 323 Spec and 308 Standards recorded source
hashes against `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`. That source, the original
`e90abb64ab95c5b15cdb0949b03c6a948365339b` and baseline
`f2929e79cfd5a68f670862775053ae85ba9582b5` remain reachable from `refs/heads/main`.
These 631 content checks establish retained Git content availability; they do not
renew implementation tests or review judgments. Missing backend/context telemetry
remains unavailable. M1 remains unaccepted and its caller-index finding remains
open. No runtime, source, test, staging or Git-history change is part of retirement.
