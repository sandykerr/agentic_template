# Evidence cleanup and organization decisions

Recorded 2026-11-13. This is the working account for the manual cleanup requested
by the human, beginning with `/tmp/evidence-cleanup-handoff-20261113T155737Z.md`.
It distinguishes human direction, overseer recommendations and observed facts.
It does not amend approved harness requirements or record milestone acceptance.

## Human direction and order of work

- Use the existing [C1–C10 retention decisions](evidence/evidence-retention-audit-01/retention-decisions.md)
  rather than reopening agreed preferences. Preserve lasting knowledge and remaining
  operational/review uses; unnecessary historical detail may eventually be discarded.
- Organize evidence before deleting it. The human selected one folder per ticket,
  for example `evidence/ticket-15/`, containing its loose files and existing
  specialized folders. Subfolders may be used where they make navigation easier.
- The human requested three GPT-6.1 Sol workers at Medium reasoning, with the root
  agent as overseer/reviewer making decisions. Worker findings inform the root's
  decisions; they do not supply independent authority to discard evidence.

## Overseer decisions and recommendations

- Keep current filenames and existing specialized subtrees initially. Consolidate
  ticket material under `evidence/ticket-NN/`; avoid simultaneous cosmetic renaming.
  Keep cross-ticket M1 bundles and the retention audit separate from ticket folders.
- Preserve original evidence identity during organization. Check actual readers,
  relative links, manifests and frozen paths before moving a family. Distinguish
  maintained navigation from immutable reports, historical snapshots and approvals.
- Do not resume runs to inspect eligibility, alter approved contracts, stage the
  mixed worktree broadly, rewrite Git history, or treat this work as M1 acceptance.
- Earlier recommendation: consider ticket 14–15 loose observations first for later
  selective retirement, because they dominate file count. This is deferred while
  organization takes priority; no deletion batch has been selected or executed.
- Verification should cover relocation completeness, original file bytes, surviving
  navigation and affected path consumers. Preserve prior test results with their
  actual source identity; file organization does not itself justify suite replay.

## Rechecked inventory and facts

The read-only inventory check on 2026-11-13 compared every regular file from the
previous compressed inventory against its SHA-256. All 7,323 matched, with none
missing or added outside the nine-file retention-audit directory. Including that
directory, `evidence/` contained 7,332 regular files, 178,981,804 logical bytes, and
one symlink. Allocated space including directories was 199,180,288 bytes. These
are filesystem measurements, not Git history or GitHub storage savings.

| Family | Regular files | Logical bytes |
| --- | ---: | ---: |
| Ticket 14–15 loose observations | 5,607 | 69,611,235 |
| Ticket 20–24 implementation/repair/checkpoint material | 524 | 55,793,252 |
| Ticket 19 calibration and telemetry | 475 | 27,947,418 |
| M1 human review and QA | 134 | 4,941,062 |
| Earlier evidence and other | 583 | 20,262,076 |
| Retention audit | 9 | 426,761 |

- The recorded temporary M1 demonstration run at
  `/tmp/ticket-harness-m1-human-qa-yjwh5cr2/run` is now absent. Retained observations
  and its archive survive; they do not establish a currently usable continuation
  environment. This supersedes the earlier audit's path-existence observation.
- Both original documentation-audit directories remain absent:
  `/tmp/agents-docs-audit-20261112-current/` and
  `/tmp/ticket-harness-docs-audit-20261112/`. Their original reports cannot be cited
  as available or recreated by this record.
- All 26 current files in the M1 human correction's
  [renewed source manifest](evidence/m1-human-review-01/renewed-source.json)
  match its hashes. The retained 559-test result remains an observation of that
  recorded source; no new test execution or cumulative review is claimed.
- [M1 architecture work](reviews/M1-architecture-01.md) retains open blocker
  `review-M1-architecture-01/standards-01/F1`. Protect the original report,
  reproduction/control, relevant source/instruction identities and finding history.
  M1 remains unaccepted and M2 remains gated.
- Ticket 19 evaluations, ticket 24 concern-to-fix history and genuine old-producer
  checkpoints are named inputs in the [M1 QA guide](evidence/m1-qa-01/qa-guide.md).
  Ticket completion alone does not release these uses.
- Existing historical navigation links to removed
  `docs/agents/development-efficiency.md` and `docs/agents/reviewer-evaluation.md`.
  A path migration must distinguish preexisting broken links from new regressions.
- Current QA validators require frozen files at exact paths with exact bytes;
  completion records can also be consumed as prerequisite evidence. Historical
  fixture copies are not automatically live runs, but an actual active or deliberately
  continuable run must retain its required files until that use ends.

## Organization execution

The three workers first inventoried tickets 01–15, 16–19 and 20–24 read-only.
The root reviewed their findings and selected byte-preserving relocation with
new navigation, rather than editing historical reports or executable captures.
The workers then moved their disjoint families and independently checked their
original bytes against a pre-migration root snapshot.

All immediate evidence entries named `NN-*` for tickets 01–24 moved into
`evidence/ticket-NN/`, retaining their basename and complete nested tree. The
exceptional `ticket16-standards-identities.json` moved into `ticket-16/`. This
relocated 917 top-level entries: 887 files and 30 directories, containing 7,189
regular files (173,613,981 bytes) and one symlink. The existing M1 bundles and
retention audit stayed in place. No evidence was discarded or recompressed.

Added [current evidence navigation and historical path mapping](evidence/README.md)
and 24 ticket READMEs. Updated 40 existing maintained navigation files: the root
README/handoff, feature index, ticket completion-comment links, current review
assessments/index and evaluate-reviewers skill references. Four preexisting dead
guidance links in the feature index and tickets 19/33/34 now route to the current
review-preparation procedure or evaluation history. The feature index also
links this decision record and the evidence index. Original approved requirement
wording, snapshots, reports, histories, manifests, scripts, archives, logs and raw
observations were not rewritten. Historical archive/draft publication records,
the retention audit and M1 QA guide retain their original paths and bytes; the
new index supplies current M1 QA destinations.

### Interpretation and limits

Original relative links to other ticket families, tracker files or repository
guidance can require the documented historical-path mapping. This is explicit:
new READMEs and maintained tracker references are the current navigation, while
original artifacts preserve historical identity. The captured scripts may depend
on their original directory depth, old output paths or vanished `/tmp` fixtures;
moving them does not make them newly runnable. Future reuse needs a separately
adapted copy, not a silent rewrite of the preserved original.

The bounded source/config search found no current executable/configuration
consumer of ticket 20–24 evidence paths outside historical evidence. The named
producer homes for those checkpoints and the M1 demonstration home are absent.
This does not establish the absence of every possible external consumer. Frozen
archive internals and the open M1 finding evidence remain unchanged.

Original evidence file count and bytes are preserved; navigation files add a
small amount of content. No storage reclamation or Git history reduction is
claimed. No staging, commit, publishing, harness continuation, runtime changes,
test execution, new source review or QA acceptance occurred.

### Verification

All three workers passed SHA-256/size checks for every original file in their
assigned family, plus the unchanged symlink target for ticket 17. Each worker
checked the new ticket README targets. Root reviewed the combined layout and
representative ticket navigation and independently verified:

- All 7,189 moved original regular files match the pre-migration hashes, the
  symlink target is unchanged, and all 917 old entry paths are absent.
- All 7,323 regular files in the prior audit inventory, including untouched M1
  material, still match their recorded hashes after applying the relocation map.
- Current navigation checks cover 1,648 local link targets across 55 maintained
  documents and the 25 new evidence/ticket indexes. The initial check found four
  preexisting dead guidance links; these were repaired. New index anchors resolve.
- All 26 files in the retained M1 renewed-source manifest still match their hashes.
- `git diff --check` passed. Runtime tests and historical helpers were not run;
  the changes affect placement and navigation, not runtime implementation.

Organization is complete. The evidence root now contains the navigation README,
24 ticket folders and the three cross-ticket bundles. Selective evidence
retirement remains a separate next step under the recorded human decisions.

## Retroactive archival and selective retirement

On 2026-11-13, after organization completed, the human instructed: “Ok, let's now
proceed with our retroactive archival of evidence. Use subagents to execute our
previous ticket archival decisions.” This authorizes this one-off application
of the recorded C1–C10 choices, including deliberate retirement of unnecessary
raw history after useful results and remaining dependencies are addressed.

This session-specific authorization supersedes blanket lossless-preservation
instructions for the selected retired artifacts. It does not publish a general
retention contract, revise approved harness requirements, remove compatibility
support, accept M1 or authorize a Git history rewrite. Retained original reports,
approval/finding histories and frozen active inputs keep their original identity.

The same three Medium-configured workers first propose bounded batches for
tickets 01–15, 16–19 and 20–24. The root reviews each concrete selection before
execution. Each worker records useful results and code identity in its current
ticket navigation before releasing raw files, updates its current links and
states what historical inspection/replay is lost. Uncertain subsets stay explicit
while independent eligible cleanup proceeds. A root pre-cleanup snapshot records
file counts/hashes and source/review/checkpoint protection for final verification.

### Approved batches

Root approved the first ticket 01–15 batch: 5,712 files / 71,399,405 bytes,
consisting of the 5,607 historical ticket 14–15 raw observation files, 100 routine
command logs and five duplicated original-command-output JSON payloads. The
worker records retained results and identities in ticket READMEs before removal.
Completion records, original independent reviews, source/result maps, consolidated
scenario observations, packaging proof and repair narratives remain. In particular,
`10-checks.log` remains because it contains original independent reviews;
`11-static/identities.log` also remains. None of the 752 original temporary fixture
paths checked by the worker exists, and the current M1 guide does not name the
14–15 raw trees. Current M1 open-finding proof remains in its untouched bundle.

Root approved the ticket 20–24 batch: 82 files / 46,249,646 bytes. This retires
selected routine full/focused-suite archives, bulk manifests/scenario indexes,
passing command streams and resolved user-interrupted captures. Retained source,
command/result, audit, completion and original independent review records carry
their actual scope. The worker inspected all 13 selected tar archives (87,231
regular members): authored-like content was synthetic fixture input, with no
project source/instruction packs. The 26 recorded source blobs for each of tickets
20–23 and 27 final ticket 24 blobs match the available implementation commits.
This preserves code identity/reconstruction, not the discarded historical output.
All genuine checkpoint families and ticket 24 concern-to-fix evidence remain.
The distinct resumed 246-observation failed campaign stays because its historical
exit 120 remains unexplained; later success does not explain that failure.

Root approved retirement of ticket 19's two command-heavy identity payloads:
21,370,822 stored bytes. Before deletion, root independently decoded both
originals, verified their recorded original hashes, and compared all 15 Spec and
24 Standards non-command fields against the proposed extracts: every value
matches. The worker also matched all 323 Spec and 308 Standards source hashes
against reachable Git content. The extracts retain identity/settings/instruction
metadata, meaningful limitations, command counts and selected command metadata;
bulk stdout/stderr and the per-command Git-show target list are deliberately lost.
They are labeled derived lossy extracts, not original captures. Current locators
identify retirement and the successors rather than promising decompression. All
five reviewer-evaluation corpora, original judgments and useful failure history
remain intact for named M1 uses.

Root also approved ten compact historical scenario extracts for tickets 03–09
and 12–14, replacing 15,163,200 bytes of full-record/command-output JSON with
about 1.24 MB of explicitly derived results. The first candidates incorrectly
turned missing attempt lists into a count of zero; the root required correction
before approval. The worker then validated 413 scenarios and 25,869 scalar facts,
omitting 34 unavailable attempt lists. Root independently compared 19,516
record/gate/ticket scalar facts against the originals and verified the original
hashes. Summaries retain observed outcomes, identities, relevant failures and
authority limits; raw stdout, full run/input/assignment data are deliberately
discarded. Small already-bounded ticket 01/02 and ticket 15 summaries remain.

Under C1, root approved removal of the ten generated historical capture-tool
`.pyc` files (45,474 bytes) under tickets 20–24. Their authored source remains;
the tools were not in use. This removes generated caches rather than retiring
original source or useful diagnosis.

### Completed archival result

All approved batches completed. This is selective, deliberately lossy archival:
lasting conclusions and needed originals survive, while selected raw history was
discarded rather than losslessly repackaged. The current ticket READMEs identify
retired categories and relevant original identities; twelve distinct extracts
are labeled derived historical results. The two ticket 19 locators explicitly
describe retired original payloads. Current tracker links to retired artifacts
now identify a retirement summary or compact results, and the root README no
longer advertises a working gzip restore command for the retired capture.

| Evidence-tree measure | Before retirement | After retirement |
| --- | ---: | ---: |
| Regular files | 7,357 | 1,554 |
| Logical bytes | 179,024,894 | 26,255,890 |
| Approximate MiB | 170.73 | 25.04 |

Net reduction: **152,769,004 logical bytes (85.33%)**. There were 5,815 physical
file removals and twelve new extract files; one original Standards payload was
replaced in place by a retirement locator. The retained symlink is unchanged.
Allocated size after the cleanup was approximately 31.2 MB including directories.
These figures cover the working evidence tree, not existing Git history or a
GitHub storage bill. No history rewrite or publishing occurred.

Root independently reconciled every removed/new/changed evidence path against
the explicit approved batches. All 1,521 unchanged surviving original files
match the pre-cleanup hashes; all 168 protected non-evidence source, review,
archive, draft and contract files also match. The only existing evidence bytes
changed are current navigation and the two explicitly replaced locator records.
All twelve extracts parse as JSON. Current navigation validation covered 84
documents and 1,632 local targets, with no missing targets or checked retirement/
mapping anchors. Whitespace checks passed; no runtime suite or historical helper
was executed, and prior results retain their original source and scope.

### Retained exceptions and remaining design work

- M1 open finding `review-M1-architecture-01/standards-01/F1`, its original report,
  reproduction/control, instructions, history and current uncommitted correction
  sources/checks remain untouched. M1 is unaccepted and M2 stays gated.
- All five ticket 19 evaluation corpora, neutral source/guidance snapshots,
  original judgments and useful failed-trial conclusions remain for M1 QA.
- Genuine checkpoint producer/consumer evidence, ticket 24 concern-to-fix
  reports/history and targeted diagnostic trials remain. The distinct resumed
  failure with unexplained historical exit 120 remains explicit and retained.
- Ticket 10's log containing original independent reviews, small already-compact
  scenario records, actual tested package copies and authored historical tools
  remain. Reuse of those tools needs adaptation; retention grants no new execution
  or compatibility guarantee.
- Runtime ticket-completion cleanup, compatibility-support removal, autonomous
  retention enforcement/skill design and treatment of other small historical
  bundles remain separately scoped decisions. This completed one-off archival
  does not claim those mechanisms were implemented or their contracts amended.

Nothing was staged or committed by this archival session.
