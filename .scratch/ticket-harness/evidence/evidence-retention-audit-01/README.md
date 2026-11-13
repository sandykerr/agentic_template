# Evidence audit and proposed handling cases

Audit date: 2026-11-12. Three workers configured as GPT-6.1 Sol / Medium,
with root reviewing their findings. **Audit complete; the human's case decisions
are recorded in [retention decisions](retention-decisions.md), with design questions
still open.** No existing evidence, approved inputs, runtime source or skills were changed.
This is a factual audit and a discussion aid, not a published spec amendment or
an authorization to delete files.

## Direction established by the human

- Reduce everyday navigation complexity and future GitHub repository growth.
  Removing existing Git history is a separate decision.
- Cover both development evidence and harness-run evidence.
- Preserve lasting development knowledge, including new decisions and directions;
  permit deliberate loss of command noise, unnecessary run records and old bug
  reports when their useful content and dependencies have been addressed.
- Explore an evidence skill that guides recording and cleanup. Handling must be
  specific to the testing/evidence case; ticket completion is one possible release
  condition, not a universal prescription.

The cases below explain the choices considered in that discussion. The
[human's responses](retention-decisions.md) now settle most retention preferences;
compatibility scope, operational handling, cleanup execution/authority and milestone
placement still need resolution. The earlier suggestion of blanket lossless
retention is not an agreed requirement for this revision.

## Audit coverage and measurements

| Area | Regular files | Logical bytes |
| --- | ---: | ---: |
| Existing `evidence/` | 7,323 | 178,555,043 |
| Existing `reviews/` | 13 | 66,104 |
| Historical `archive/` | 93 | 491,823 |
| Planning `drafts/` | 26 | 1,794,254 |

There is also one tracked 9-byte symlink in the evidence tree. These measurements
include ignored files and exclude this new audit directory. Logical bytes differ
from allocated filesystem space; the evidence tree occupies 198,729,728 allocated
bytes including directories. They do not measure GitHub storage or Git history.
Root independently reproduced the counts, logical bytes and tracked-file totals;
see [reviewer checks](reviewer-checks.json).

The largest disjoint evidence families are loose ticket14–15 scenario captures
(69,611,235 bytes), ticket20–24 implementation/repair/checkpoint material
(55,793,252 bytes), and ticket19 calibration/capture material (27,947,418 bytes).
The [physical inventory](worker-inventory.md) contains the complete family table,
[compact measured summary](worker-inventory-summary.json), and
[compressed per-file inventory](worker-inventory-data.json.gz).

Stored formats include 116,125,501 bytes of JSON, 39,553,145 bytes in 49 tar.gz
archives, and 17,058,803 bytes in seven other gzip streams. These are format
categories, not retention categories: JSON can contain decisions, runtime state,
or huge embedded command outputs. The archives contain 104,230 regular members
and 507,846,824 uncompressed member bytes, not additional loose-file storage.

## Root review of the worker findings

1. **Most storage is execution material.** The review index/assessment directory
   itself is only about 66 KB. One nominal identities file,
   [`19-review-round2-spec-identities.json.gz`](../19-review-round2-spec-identities.json.gz),
   is 17,029,165 stored bytes and 220,978,737 decoded bytes. Root inspected its
   structure: it contains 13,762 command records, with stdout/stderr dominating
   its contents. Several large commands read older evidence from Git. A filename
   containing “identities” does not make the entire file essential provenance.

2. **Exact duplication is a limited opportunity on its own.** Independent hashes
   agree on 5,230,393 excess regular-file bytes across identical loose contents.
   The inventory counts 325 duplicate groups including the empty-file group;
   root counts 324 nonempty groups. This is not an estimate of all duplication
   inside compressed containers or embedded command output. Equal content at two
   paths can still participate in a frozen checkpoint or manifest.

3. **Historical uniqueness is a tradeoff, not an automatic retention requirement.**
   The [review/provenance audit](worker-review-provenance.md) traces distinct
   failed trials, mistaken clean reviews, fixes and changed guidance. A later
   summary cannot recreate those original judgments. The human can nevertheless
   choose to retain their lasting conclusions and discard the originals. That
   choice gives up retrospective reconstruction; it need not block the intended
   simplification.

4. **Operational dependencies are stronger than historical usefulness.** Root
   checked [QA freeze/validation](../../../../ticket_harness/qa.py:107) and
   [test observation capture](../../../../tests/test_dependencies.py:177).
   Current QA/continuation requires exact files at recorded paths, including
   already-parsed streams. Copied test output intentionally omits worktrees and
   can reference temporary directories that no longer exist. The
   [runtime audit](worker-runtime.md) distinguishes these observation copies from
   an actual stopped run. Root confirmed that the M1 demonstration target/run/
   candidate directories still exist and its record says `stopped_at_qa`; this
   was not a continuation or integrity validation.

5. **Current preservation policy and future policy are separate.** The
   [approved review contract](../../spec.md#review-work-findings-and-decisions)
   and [development guidance](../../../../docs/agents/review-records.md) currently
   preserve original reports and histories. Lossy retirement therefore requires
   aligning those documents and their skill routes with the newly agreed policy.
   There is no technical need to preserve every historical development log just
   because that is today's policy. Active exact-byte dependencies must either
   end or be deliberately changed in the implementation before cleanup.

## Concrete cases for choosing retention

The human's choices are recorded in [retention decisions](retention-decisions.md).
This section explains their tradeoffs; implementing and applying the revised
policy remains future work. The aim is to agree on rules the harness can follow
without asking a human about every ticket. Each case below explains what the files
contain, what we could keep in a shorter form, and what we would lose by deleting
the originals.

Compressing files keeps their contents and makes later inspection less convenient.
Writing a summary and deleting the originals reduces storage and clutter, but
anything omitted from that summary is gone unless another copy exists.

### C1. Files that tools generate, and scripts written for one task

**What we have:** Python cache files, plus small scripts used to collect or check
evidence. Examples are the `.pyc` files and the `20-tools/` through
`24-repair2-tools/` folders.

**Possible rule:** Delete generated caches when the tool has finished. For a
one-off script, first save its useful result and decide whether the script should
become a maintained tool or test. Delete it only when nothing still needs to run it.

**Tradeoff:** Caches can be recreated from the source. A script may contain the
only explanation of how to reproduce a problem. Automation can easily recognize
cache files; deciding that an authored script has no future value needs more care.

### C2. Output from commands that passed

**What we have:** Test progress, formatting and type-check results, error-output
files that are empty, and other routine command logs.

**Possible rule:** Keep a short record of what ran, which version of the code it
checked, whether it passed, and any important result. Delete the full output after
the review or QA work that needs it has finished.

**Tradeoff:** We would still know that a check passed, but could no longer inspect
everything it printed. A passing command can also print warnings or other useful
observations. The harness needs a rule for capturing those before deleting output.
Some logs are also required to resume a saved run; case C8 covers that restriction.

### C3. Checks that were interrupted or failed because of the tools or environment

**What we have:** A stopped test suite, dependency-installation failures, and logs
from diagnosing problems with the checking tools themselves.

**Possible rule:** Once the cause is understood and the necessary checks have run
successfully, keep the useful explanation and any lasting setup change. Delete
the detailed failed-attempt logs if no unresolved investigation still needs them.

**Tradeoff:** We lose the ability to revisit every step of the diagnosis. The
harness must distinguish a resolved setup problem from a product bug or an
unexplained failure. A later passing run does not, by itself, explain an earlier
failure or prove that it is harmless.

### C4. Bug reports and the attempts to fix them

**What we have:** Reviewers' bug reports, examples that demonstrate bugs, failed
fixes, and checks of later fixes. Ticket24's recursion and branch-alias bugs are
examples; the M1 caller-index bug is still open.

**Possible rule:** After a fix has been independently checked, keep the corrected
requirement, any lasting design decision, and a useful test that catches the bug
if it returns. Delete the old reports and failed-fix logs once no further review
or QA step needs them.

**Tradeoff:** A future investigator loses the original reasoning and unsuccessful
approaches. A test may preserve only one example of a wider problem. The harness
needs evidence that the concern was actually resolved and its useful lessons were
recorded; a worker saying “fixed” is insufficient.

### C5. Saved details from repeated test runs

**What we have:** Large folders and archives containing test inputs, run records,
and outputs from early failures, focused checks, repairs and final full-suite runs.
The `14-observations/` and `15-observations/` folders contain many of these files.

**Possible rule:** For each testing task, identify which saved examples are needed
to explain the result or support later review and QA. Keep those until that work
finishes. Remove earlier captures that add no needed information once a sufficient
final record exists.

**Tradeoff:** Keeping only the final passing run makes it harder to understand
failures that appeared earlier or happened inconsistently. Keeping every run is
expensive. An autonomous harness needs the testing task to say which observations
matter; it cannot reliably choose using filenames such as “final” or “old.”

### C6. Old examples kept to test compatibility, and copies of tested packages

**What we have:** A checkpoint made by older code that newer code must still read,
and the actual installable packages used for installation checks. The
`24-checkpoint/` and `24-resume-checkpoint/` folders show the old/new checkpoint test.

**Possible rule:** Keep an old example while a planned compatibility check needs
it. Keep it longer if future versions must continue to pass that same test.
Otherwise, save the versions tested and the result, then remove the example.
Similarly, decide whether to keep a tested package or just its installation result.

**Tradeoff:** Without the old files, we cannot repeat the same compatibility or
installation check. Generating a new example with today's code does not test what
the older code actually produced. The harness needs to know which examples are
permanent test inputs and which were collected for a single demonstration.

### C7. Records of how agents and reviewers performed

**What we have:** Reviewers' original answers, evaluation examples, instructions,
mistakes, revised guidance, and detailed records of commands agents ran. One file
called an “identities” record contains roughly 221 MB of data before compression,
mostly captured command output.

**Possible rule:** Keep the lessons that changed reviewer guidance, known
limitations, and the evaluation results we still rely on. Remove detailed old
transcripts and superseded evaluation attempts after their useful conclusions
have been recorded, unless we want to reassess those evaluations later.

**Tradeoff:** We would be trusting the saved conclusions. Without the originals,
we could not independently revisit a reviewer's judgment or fully examine how an
evaluation was conducted. The policy must decide how much ability to audit agent
performance matters; the harness should not make that choice anew for every run.

### C8. Files needed to run, pause or resume the harness

**What we have:** The current run record, copies of approved inputs, QA requests
and decisions, saved checkpoints, and working copies of the code.

**Possible rule:** Keep these files intact while the run is active or we intend
to resume it. Once that need ends, remove the working files and retain the agreed
completion and approval records. Keep any run record that a later run still reads
to establish that its prerequisites were completed.

**Tradeoff:** Removing these files too early can prevent continuation or break a
later run. The current harness checks exact saved file contents and locations, so
even compressing or moving a required file can break continuation. Automatic
cleanup needs an explicit way to establish that a run will no longer be resumed
and which records later runs still need. That mechanism does not exist yet.

### C9. Saved copies of code and reviewer instructions

**What we have:** Source archives, patches, copies of the instructions reviewers
received, and lists of file fingerprints used to identify the versions checked.

**Possible rule:** Where Git already preserves the exact required code or
instructions, keep a reference to that commit and remove extra copies after their
testing and review uses finish. Handle uncommitted changes and files outside Git
separately, because the saved copy may be the only copy of the version examined.

**Tradeoff:** A commit reference is useful only while that commit remains
available. A fingerprint identifies content but cannot recreate it. Automation
needs to verify that the surviving reference really contains the required version;
the fact that a similarly named file exists in Git is insufficient.

### C10. Decisions and instructions that future development must follow

**What we have:** Human approvals, reasons for design choices, changed requirements,
new development directions, and unresolved work recorded inside reports or chats.

**Possible rule:** Move this knowledge into the appropriate maintained document
or tracker entry. Record what was decided, why, who authorized it, what it applies
to, and what remains unresolved. Then remove the old surrounding reports or
transcripts when nothing else still needs them.

**Tradeoff:** The shorter record becomes what future agents rely on. If it omits
an exception or turns a tentative suggestion into an approved decision, future work
can go wrong. A skill can guide this extraction, but deciding how to check its
accuracy is part of designing reliable autonomous cleanup. Human approval must
remain distinguishable from an agent's interpretation.

### What these choices mean for unattended cleanup

For each case, we need a standing rule that says **what must be saved, what
observable event permits removal, and what to do when the harness cannot establish
that removal is allowed**. Examples of observable events include a recorded
independent check of a bug fix or the explicit end of a run's continuation support.
“This looks old” and “probably no longer needed” are not dependable automatic rules.

The policy could keep uncertain files, compress them, or ask for a decision at a
planned human checkpoint. Each choice has a cost: storage, retrieval work, or human
attention. We have not selected one yet. Agreeing on these rules in advance would
avoid asking a human to classify files ticket by ticket.

One file may also contain several kinds of information. The large identities file
mixes useful version details with bulk command output. We could save the useful
fields and remove the rest, but that requires checking the extracted record.
Deleting files solely by extension would miss this distinction.

## Implications for an evidence skill

A small initial policy could require every meaningful evidence collection to name:

- its purpose and the acceptance, debugging or reproduction question it answers;
- the lasting knowledge/result to extract and its maintained destination;
- the consumers that still need raw files, including QA/continuation;
- its case-specific release condition and chosen action: discard, compress, or keep;
- the surviving reference after cleanup, so current tracker links do not promise
  deleted original evidence.

This need not introduce another permanent per-command ledger or a new blocking
scheduler. Existing task notes or completion records may hold the information.
Whether a skill alone is sufficient or runtime automation should enforce parts of
the policy remains a design question. Existing skills already contain overlapping
capture rules; a new skill should have a clear responsibility and callers, with
those rules reconciled rather than duplicated.

The current M1 blocker and pending cumulative review are examples of **unreleased
uses**, not reasons to retain all historical evidence forever. The
[recorded case decisions](retention-decisions.md) will guide the revision; remaining
design questions precede changes to the spec, skills or retained files.

## Review record and limits

- Physical inventory worker: [report](worker-inventory.md).
- Review/evaluation/provenance worker: [report](worker-review-provenance.md).
- Runtime artifact lifecycle worker: [report](worker-runtime.md).
- Root: read all three reports, independently counted/hashed loose files,
  reconciled the symlink and empty-duplicate-group distinctions, inspected the
  largest gzip structure, checked runtime freeze/capture source, and checked the
  named temporary paths read-only. Measurements are in [reviewer checks](reviewer-checks.json).

This was an inventory and source review. No harness/test run, acceptance decision,
restore operation, complete archive-member deduplication, exhaustive semantic
review of every historical file, or Git history cleanup was performed. No estimate
of GitHub space reclaimed by deletion is claimed. New outputs are confined to this
audit directory; no spec amendment or skill implementation has been published.
