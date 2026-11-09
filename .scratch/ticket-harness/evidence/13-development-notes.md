# Ticket 13 development provenance

The fixed starting baseline is fd292a988cde79532bb84714b5800e4baa5de127.
The root agent owns prerequisite audit, independent reviews and completion/handoff
bookkeeping. The implementation assignment owns only ticket 13 implementation,
behavioral tests, public contracts and check evidence. The unrelated tracker edit
is preserved and excluded from staging.

- `13-red-1` failed because the baseline stopped at preparation_pending without a
  request. `13-green-1` passed the first exact tested QA request slice.
- `13-red-2` demonstrated a merge hook could change source and still reach QA;
  `13-green-2` passed after independent plain-merge validation.
- `13-focused-1` passed six failure/movement/source/current-dev cases.
- `13-focused-2` was a development-only run: 38 passed, one assertion failed
  because the diagnostic includes Git identity flags between `git` and `merge`.
  The assertion now checks the actual CONFLICT diagnostic. Source formatting/docs
  and diagnostics were edited while this historical run was active; its recorded
  identity is start-only and its traceback display uses subsequently formatted
  source. Do not use it as final source verification.
- `13-focused-3` passed all 108 affected milestone/transaction/dependency tests.
- `13-focused-4` passed five final merge/request cases after the last source edits.

Only renewed-final-* checks establish the frozen final source. Development scenario
observations retain their own run directories and must not be consolidated as
final observations. Raw logs are unmodified; if bookkeeping needs whitespace
normalization, preserve original strings separately before normalizing display.

No automatic conflict repair or renewed-review assignment is claimed. Unresolved
conflicts and source-changing merge-driver/hook resolutions stop before QA with
preserved source and explicit renewed-check/review requirements. Clean plain Git
merges are supported, including nonoverlapping changes within the same file.
Approval consumption/promotion, continuation and human acceptance remain later
work. The canonical merge requires Git's global --attr-source option and fails
closed on unsupported Git; the local Git is 2.53.0.

Development/focused raw scenario directories were moved to
`/tmp/ticket13-checks/archived-observations/` before final-suite consolidation;
all original scenario JSON remains there. The final full-run raw directory is
kept separate until the consolidation audit. Historical display logs with
trailing whitespace/extra blank lines were normalized for Git, with their exact
original strings retained in `13-log-originals.json`. Source identities and
command/result JSON are unchanged.

A self-audit found the transient outcome was `completed` while planned regression
was running. The initial full-suite wrapper was stopped via SIGINT (observed
wrapper exit 130; no child pytest completion/count was observed). Its unchanged
source capture is `13-interrupted-suite-source.json`, actual interruption record
is `13-interrupted-suite-result.json`, and partial scenarios are archived under
`/tmp/ticket13-checks/archived-observations/interrupted-suite`. It is superseded.
The no-new-merge external suite tracer then failed in `13-red-3`, demonstrating
that transient state, and passed in `13-green-3` after setting
`outcome: preparing_milestone`. Final full/static checks use fresh
`renewed-final-*` identities and observations; original captures are not rewritten.

Final implementation checkpoint: `19ea4f1b0bbdc601653468212aaaa0a7211d5c6f`.
All five renewed final checks passed; the full suite reports **509 passed in
795.92s**, actual wrapper elapsed 796.788s. `13-check-results.json` and
`13-checks.log` consolidate the actual final commands/exits/output. The final
20-file source/test identity is copied unchanged to `13-final-source-identity.json`.
All 20 hashes match every final command capture, current bytes and committed HEAD.
`13-fixture-observations.json` contains exactly 88 distinct final-run scenarios;
all consolidated observations were compared to their raw JSON, excluding only the
added `retained_file` provenance field. Final raw observations are archived at
`/tmp/ticket13-checks/archived-observations/renewed-final-suite/`; development and
interrupted directories remain separate alongside it. No source changes followed
final checks. Git index was empty before staging; only the five implementation
files entered the checkpoint. Initial sandbox Git metadata writes failed read-only;
a scoped approved escalation created the authorized local checkpoint. Staged and
original-baseline committed whitespace checks passed. Tracker hash is unchanged.

The root agent owns fresh independent Spec/Standards reviews and subsequent
completion/bookkeeping/handoff. This implementation checkpoint is not a completed
ticket or human milestone acceptance. No ticket/index/handoff input was edited,
no decision artifact was synthesized, and no push occurred.
