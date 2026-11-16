# Ticket 19 evidence

Original evidence remains in its nested structure, except for the explicitly
retired mixed command captures described below.
Original links, captured paths and scripts retain the historical layout; consult
the [historical path mapping](../README.md#historical-paths) when following them.
Historical scripts are not ready to rerun from these locations.

- [Completion](19-completion.md), [original implementation and coverage](19-implementation-report.md), [final repair report](19-repair-c5-report.md), [final checks](19-repair-c5-checks.log), [final source/check result](19-repair-c5-check-results-20261110T180103445335Z.json).
- [All three independent review rounds](19-review-navigation.md), [append-only actual finding history](19-finding-history.md), [current assessment](#review-assessment); capture manifests for [initial](19-review-capture.json), [second](19-review-round2-capture.json) and [final](19-review-round3-capture.json) rounds.
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

## Review assessment

**review-ticket-19: completed.** Fixed original baseline: `f2929e79cfd5a68f670862775053ae85ba9582b5`, retained through every repair.
Assessed source(s): Initial `e90abb64ab95c5b15cdb0949b03c6a948365339b`; first repair `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`; final `8e2c82679a2314e31ebff69accab3743f55f996d`.

The original reviews, captures and completion record linked above retain the
independent axes, instructions/settings, inspected/omitted scope and results.
Finding dispositions remain in [19-finding-history.md](19-finding-history.md).
This is the historical ticket assessment; current M1 acceptance is recorded in the
[review index](../../reviews/README.md), separately from ticket completion.

<details>
<summary>Historical assessment events (verbatim)</summary>

Copied from the retired `reviews/ticket-19.md`; relative links inside this
historical excerpt use that original location. Use the navigation above and the
[retired-wrapper map](../README.md#retired-review-wrappers) for current destinations.

```markdown

- A01 — `/root` assigned fresh independent High Spec/Standards after checkpoint
  `e90abb6`, with original fixed baseline, actual source/contracts/checks and prior
  finding context; sibling initial outputs excluded.
- A02 — `/root/spec19` saved original spec-01 with F1 and a disposable exact-source
  dictionary-alias reproduction; original assessment complete, finding open.
- A03 — `/root/standards19` saved original standards-01 with no findings and explicit
  scalar-value/capture limits. Parent preserved both reports before aggregation.
- A04 — `/root` captured original reports/instructions/evidence with external
  digests; authorized fresh Medium `/root/repair19` for F1. Renewed whole-ticket
  assessment remains in progress, not a clean initial pass.

- A05 — Fresh Medium `/root/repair19` committed `ce4e57d` after four complete corpus
  versions and preserved failures; current G2/C4 passing result still needed whole-ticket verification.
- A06 — `/root` assigned separate fresh High round2 axes from the original baseline;
  sibling current outputs excluded, original reports/failed trials supplied as history.
- A07 — Both axes independently verify original h8 F1 fixed at exact ce4e57d. Spec
  reports new b7 `spec-02/F1`; Standards reports no new findings. Both accept bounded
  byte-faithful EOF handling. Parent preserves original reports/identities before aggregation.
- A08 — `/root` captures round2 originals with external digests, appends E02–E05 and
  authorizes fresh Medium `/root/repair19_branch`. Assessment remains in progress;
  source/complete-corpus correction and third independent axes required.

- A09 — Fresh Medium `/root/repair19_branch` preserves C4/round2 and declares full
  C5 before fresh independent High corpus axes. Commits final repair/custom skill
  at 8e2c826 after standalone checks and bounded preparation-only skill observation.
- A10 — `/root` assigns fresh High third-round axes on complete f2929e7→8e2c826
  source, both prior keys, all failed trial history, new skill/probe and EOF handling.
- A11 — `/root/spec19_round3` saves spec-03, 0 new blockers/0 optional; independently
  verifies both keys fixed at final source, entire finite evaluation and user-added skill.
- A12 — `/root/standards19_round3` independently saves standards-03 with 0/0 and
  verifies both fixes, unchanged consumers/authority, capture/source identity and limits.
- A13 — `/root` preserves both original reports/identities with external digests,
  appends E06–E08, completes assessment and prepares separate completion bookkeeping.
  No original reports or prior history events edited; no human acceptance inferred.
```

</details>
