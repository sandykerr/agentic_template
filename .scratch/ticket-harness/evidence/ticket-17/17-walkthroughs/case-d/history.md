# Case D fixture finding history

This is representative-source review history, not a real harness finding or
milestone acceptance. Original reports/source snapshots remain immutable.

## E01 — observed open

- Full key: `walkthrough-case-d/standards-01/F1`.
- Actor: fresh High Standards `/root/implement_17/walkthrough_d`.
- Source: `8647da4cd28a01ea060027df087554df3bf73161`.
- Disposition: open, blocking; sparse acceptance slots evade validation and
  normalize to undefined entries. [Original report](report.md) records source,
  contract, executed witness, consequence and proportionate remedy.
- No decision, repair or independent verification existed at this observation.

## E02 — fixture-only repair claimed; independent verification pending

- Full key: `walkthrough-case-d/standards-01/F1`; follows E01.
- Actor: Medium fixture preparer `/root/implement_17`.
- Source/repair commit: `45e518804a7b4011861940065d07237287454e14`.
- Authority: authorized isolated walkthrough preparation/correction within the
  unchanged representative contract; no harness implementation repair or new owner.
- Change: validate `Array.from(ticket.acceptance)` so holes are visited as
  undefined and rejected before publishing success. All other source/contract
  content is unchanged from the original assessed candidate.
- Disposition: remains open pending independent exact-source verification; a
  worker's claimed fix and matching Git hashes do not establish fixed.
- [Repair source/bundle/diff](../case-d2/change.diff) retains original baseline
  `49ae60016d513a35c22f7139994da144929cdf88`. No human decision or amendment needed
  for this correction within the already explicit contract. No milestone
  assessment exists; this fixture does not establish M1 readiness.

## E03 — independent exact-source fixture verification

- Full key: `walkthrough-case-d/standards-01/F1`; follows E02 and preserves E01.
- Actor: fresh High Standards `/root/implement_17/walkthrough_d2`, independent of
  the fixture preparer and original D evaluator.
- Exact repaired source: `45e518804a7b4011861940065d07237287454e14`.
- Disposition: fixed for this exact fixture source, established by the separate
  [supplemental verification](../case-d2/verification.md). Sparse acceptance is
  rejected and the unchanged caller returns failure; ordinary validation remains
  acceptable. The verification records executed checks and observation limits.
- Its [initial independent report](../case-d2/report.md) was preserved before the
  prior report/finding/repair claim entered its context; initial whole-ticket
  assessment from original baseline was clean. Later verification does not rewrite
  that initial report or the original D blocker.
- No human risk acceptance, contract amendment or milestone assessment exists or
  is implied. Further source changes require relevant independent revalidation.
