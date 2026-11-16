# Evidence retention and guided review — shared understanding

Recorded 2026-11-16 from the human/agent policy discussion.

**Approved plan amendment:** evidence-policy-1.

**Publication approval:** [Human decision and scope](evidence-policy-approval.md).

This is the accepted evidence spec, incorporated into the [feature spec](spec.md). Individual tickets and milestone gates govern implementation; publication starts no work and authorizes no evidence deletion.

## Problem Statement

Evidence accumulates as tickets are developed, reviewed, repaired and accepted.
Keeping all raw output makes navigation and repository maintenance expensive.
Deleting it informally can lose useful knowledge or break reviews, later tickets,
QA and stopped runs. Similar but different files make these choices harder.

The previous one-off cleanup demonstrated useful retention choices, but its
execution account is not a standing policy. Existing guidance includes lossless
capture and preservation requirements that must be reconciled with selective,
deliberately lossy retirement.

Agents need concrete criteria and structured records that produce consistent
results. Humans need a manageable way to review unresolved choices and proposed
merges without inspecting every file at the end of a long milestone.

## Solution

Establish one evidence policy for repository development and harness runs in
target repositories, respecting additional requirements of the target repository.
Preserve lasting knowledge and remaining uses while allowing routine evidence to
be removed without asking the human about every batch.

Use a Python tool and JSON records to guide and check the workflow. Inventory
files and references once; assign non-overlapping groups to parallel assessment
agents; have a fresh reviewer perform final checks and cross-file synthesis.
The reviewer approves actions. Python checks those approvals against current
files and performs deletions. Assessment and review agents do not delete files.

Provide a proposed `review-evidence` skill that presents a concise, resumable
human review queue at milestone QA. Agents prepare proposed merged content;
humans approve it or request changes rather than manually merging files.
Evidence-cleanup approval remains separate from exact-candidate QA acceptance.

Provide a complementary `capture-evidence` skill backed by a Python helper that
selects evidence destinations and registers provenance consistently. Capture puts
evidence in the right place; subsequent assessment determines retention.

Begin with an independently usable capture skill/helper slice, followed by a
small complete review-and-cleanup slice using its captured evidence. The first
human checkpoint covers both slices, with early calibration and the local tool.
Automatic cleanup inside the harness is separate future implementation work.

## User Stories

1. As a developer, I want clear retention criteria so that cleanup does not depend on an agent's free-form interpretation.
2. As a harness operator, I want the same principles applied to development and run evidence so that both remain manageable.
3. As a target repository maintainer, I want my repository's additional retention requirements respected so that shared tooling does not override them.
4. As an assessment agent, I want an automatically generated inventory so that I do not repeatedly discover the same files.
5. As an assessment agent, I want a shared reference report so that I can identify uses outside my assigned ticket folder efficiently.
6. As an assessment agent, I want fixed criteria, reason codes and required fields so that my recommendations can be checked by code.
7. As an overseer, I want parallel workers assigned separate groups so that they cannot overwrite each other's proposals or delete files.
8. As a reviewer, I want a combined view of proposals and dependencies so that I can resolve relationships individual workers missed.
9. As a developer, I want lasting decisions, approvals and original independent review reports retained so that the authority and reasoning behind work remain understandable.
10. As an operator, I want active and deliberately continuable runs protected so that cleanup does not break their required inputs or evidence.
11. As a developer, I want unique needed content protected so that the only useful copy cannot disappear.
12. As a developer, I want routine output removed after required verification and remaining uses end so that completion does not leave unnecessary captures behind.
13. As a reader, I want retained results tied to exact code versions and actual check outcomes so that summaries do not overstate verification.
14. As a reviewer, I want summaries compared against their originals before replacement so that useful differences and limitations survive.
15. As a developer, I want uncertain files retained with reasons so that uncertainty cannot silently become permission to delete.
16. As a developer, I want temporarily retained evidence linked to a triggering ticket so that reassessment happens during normal ticket completion.
17. As a human reviewer, I want unresolved reassessments brought to the next milestone QA so that they do not disappear between tickets.
18. As a reviewer, I want similar versions compared for their useful differences so that the newest file does not automatically replace earlier knowledge.
19. As a human reviewer, I want agents to prepare proposed merged files and explain omissions so that I can approve a merge without doing it myself.
20. As a human reviewer, I want an overview and small groups of related decisions so that long milestones do not create an overwhelming file-by-file review.
21. As a human reviewer, I want to approve, keep, request changes or defer so that the workflow reflects my actual decision.
22. As a human reviewer, I want to pause and resume review so that I do not repeat completed decisions.
23. As a human reviewer, I want changed proposals to require renewed approval so that prior decisions cannot authorize different content.
24. As an operator, I want file identities rechecked before deletion so that only the assessed files are removed.
25. As an operator, I want actual deletion results recorded separately from approval so that partial or failed execution remains visible.
26. As a maintainer, I want concise cleanup notes so that cleanup does not create another large evidence collection.
27. As a human calibrator, I want to label representative evidence before seeing agent recommendations so that we can fairly compare their decisions with mine.
28. As a maintainer, I want repeated trials to produce consistent decisions so that the workflow is dependable without requiring identical prose.
29. As a milestone reviewer, I want cleanup decisions kept separate from software acceptance so that one approval cannot substitute for another.
30. As a developer, I want new evidence written directly into its ticket folder so that later cleanup rarely needs to reorganize it.
31. As a milestone reviewer, I want shared evidence in descriptively named folders linked from relevant tickets so that it is easy to find without duplicating it.
32. As a reader, I want existing navigation to identify successfully deleted evidence so that a historical reference does not promise an available file.
33. As a reviewer, I want files classified by their contents so that reviews embedded in logs or archives are not mistaken for disposable output.
34. As a reader, I want summaries to distinguish missing information from zero so that compression does not invent facts.
35. As a maintainer, I want protected survivors checked after cleanup so that successful deletion alone cannot hide unintended changes.
36. As an evidence-producing agent, I want a capture skill and Python helper to select the destination so that I do not invent a new folder layout for each task.
37. As a reviewer, I want captured evidence registered with its purpose, source version, activity, result and file identity so that later assessment has reliable provenance.
38. As a parallel worker, I want a separate assigned capture location so that I can save evidence without overwriting another worker or editing shared review decisions.

## Implementation Decisions

### Policy and decision order

Apply the following checks in order, with fixed reason codes and structured
supporting facts rather than an unrestricted explanation alone:

1. Keep durable records: lasting decisions, actual human approvals and original
   independent review reports.
2. Keep evidence with remaining uses: unresolved problems, required reviews,
   acceptance, later work, active runs and deliberately continuable runs.
   Completion records still consumed by later runs remain protected.
3. Keep the only needed copy of source, instructions or substantive results until
   those contents are preserved elsewhere. A verified Git reference may replace
   an extra source copy when it preserves the required version; do not assume
   uncommitted or external content is recoverable from Git.
4. Consider generated caches, routine passing output, redundant observations and
   resolved failure details for deletion. Unexplained failures remain open work;
   later success does not explain an earlier failure by itself.
5. Preserve useful results and their code identities before deletion. Label
   derived, lossy summaries and state what detail is lost. A fresh reviewer checks
   any summary replacing the only retained substantive evidence against originals.
6. Keep uncertain material with a concise reason. Split groups with different
   conditions rather than approving mixed groups together.

Routine output may be retired after required ticket checks and reviews pass,
before milestone acceptance, only if no remaining use protects it. Re-executing
a command creates a new observation; it does not recover discarded historical
output. Hashes identify content but do not prove a result or judgment correct.

The policy governs capture and later retirement as separate stages. Reconcile
existing lossless-capture guidance with these retirement rules; do not silently
relax approved contracts or frozen-input integrity checks.

Classify evidence by its contents and uses, not just its filename, extension or
directory. A checks log can contain an original independent review. Inspect
archive contents and mixed-content files before deciding whether the entire file
is disposable; protect needed content or preserve it through the required reviewed
replacement process first.

An absent historical temporary directory does not establish that retained evidence
is disposable. Check the actual remaining uses; neither the presence of an archive
nor its retained observations establishes a currently usable continuation environment.

### Evidence placement and historical identity

Write new ticket evidence directly into the corresponding ticket subfolder within
the appropriate evidence location. This applies to development evidence and, when
adopted, run-owned output; it does not permit writes into approved inputs or frozen
files. Preserve useful specialized subfolders within each ticket folder.

Keep genuinely shared evidence in descriptively named shared folders, with
milestone subfolders for milestone-scoped material. Relevant tickets link to those
folders so their agents and human reviewers can find the shared evidence without
duplicating its authoritative copy.

Avoid cosmetic renaming and reorganization during cleanup. Existing historical
material may remain in its current layout, and historical reports retain their
embedded paths and original contents. Eligible historical raw evidence may still
be retired under the policy. Move existing evidence only for a concrete need after
checking readers, relative links, manifests and frozen-path requirements. Verify
necessary moves preserve original bytes and provide a historical-path mapping.
Adapt a separate copy of an old helper for reuse rather than silently rewriting
its historical source or implying it still runs against vanished fixtures.

### Evidence creation skill and helper

Introduce a repo-owned `capture-evidence` skill for creating and saving development
evidence. It identifies the ticket and evidence purpose before capture and uses
a Python helper for path selection and registration. The helper applies the
ticket-folder and shared/milestone-folder rules consistently, including references
from relevant tickets to shared evidence. Future harness adoption remains separate.

Record the source version, producing command or activity, observed result and file
identity. Preserve original captures and clearly distinguish derived summaries.
Capture establishes placement and provenance; it does not approve deletion,
determine final retention, or supply independent review or human acceptance.

Parallel producers receive separate output locations and registrations. They must
not overwrite one another's captures or concurrently edit the consolidated review
artifact. The helper owns registration and path selection; reconcile capture
metadata with later assessment without creating another authoritative review record
or treating a newly captured file as covered by an earlier approval.

Route existing implementation, testing and review workflows through this capture
guidance where applicable. Reuse their verification and original-report requirements
rather than duplicating them in the skill. Respect approved-input, frozen-evidence
and run-owned-output boundaries when selecting destinations.

### Structured records and tool responsibilities

Use JSON rather than CSV as the authoritative interchange format. It supports
multiple paths, references, dependencies and conditional review fields per group.
The exact schema and reason-code names remain implementation design work.

Maintain one authoritative JSON evidence-review artifact per ticket subfolder.
It contains that ticket's assessed file groups, proposed actions, reviewer and
human decisions where required, reassessment entries, and execution results.
Preserve the distinction between proposals, approvals and actual outcomes within
this consolidated artifact. Its exact filename remains an implementation choice.

Parallel workers write separate temporary proposals. The final reviewer
consolidates those proposals into the ticket's single JSON artifact, retaining
their assessment provenance and resolving cross-file relationships. Workers do
not concurrently edit the authoritative artifact. Python records execution
outcomes there after review; approvals and completed deletions remain distinct.

Shared evidence has its own authoritative JSON artifact in the corresponding
shared evidence folder, including milestone subfolders where applicable. Ticket
artifacts reference shared decisions instead of duplicating them. Generate the
milestone QA queue and ticket-triggered reassessment view from these artifacts;
those views are not additional authoritative copies of the decisions.

Records and derived summaries must distinguish unavailable or unknown information
from an observed zero or empty collection. Do not convert a missing attempt list
into zero attempts. The schema must represent these differences explicitly, and
summary validation must compare retained facts with their originals.

Each proposed group records its file paths, sizes and content hashes; evidence
type; proposed action and reason; remaining uses; retained results and code
identity; and required review status and decisions. Groups share a rationale and
retention conditions. Worker proposals, final approval and execution outcomes
must remain distinguishable.

The proposed actions are keep, delete and merge proposed. Eligibility, required
review and execution state are separate from the proposed action. Missing facts,
incomplete assessments, conflicting decisions, changed files and unmet conditions
block deletion of the affected group rather than being interpreted as approval.

The tool generates inventories, reference reports and assignments; validates
records, required retained results and reviews; and reports eligible, blocked and
review-needed groups. Agents assess meaning and remaining uses with supporting
references. A successful schema check does not establish that those judgments
are true, and an absent search match does not prove there are no remaining uses.

### Parallel assessment, fresh review and execution

Workers receive fixed non-overlapping assignments and write separate proposals.
They do not delete files, edit other workers' proposals or make final approvals.
They flag related versions and dependencies outside their assignments.

A fresh reviewer using high reasoning checks the combined proposals, performs
remaining cross-file synthesis, resolves conflicts and verifies required summaries
and merged content. Routine decisions that pass checks do not require rereading
every command log. The reviewer records final approval in each relevant
authoritative JSON artifact, naming exactly which groups may be deleted.
Unresolved disagreements remain protected.

Python performs deletion through a simple guarded execution path. It requires
reviewer approval, any required human merge approval and passing checks against
the current file identities and retention conditions. It acts only on eligible,
explicitly identified files and records actual successes and failures separately
from approvals. Preview performs no deletion. Execution must not invalidate an
active frozen QA request or required continuation evidence.

After execution, reconcile actual removed, added and changed paths against the
approved actions. Verify protected surviving originals and identified protected
files outside the evidence directory remain unchanged. Check affected navigation
and path consumers as well as deletion results; approved file moves must also
preserve their recorded bytes. Preserve the existing symlink target when a
protected symlink is retained.

### Navigation for deleted evidence

Prefer retiring evidence that no longer needs direct navigation. Where maintained
navigation already references an eligible file, replace the missing-file link with
plain text marked `(deleted)`, a short reason, and a link to retained results when
available. Do not create a permanent navigation entry for every discarded log.
Required machine-readable references and frozen paths remain retention dependencies;
a deleted label cannot substitute for content a reader still requires.

Record proposed deletion separately from actual deletion status. Python marks
navigation deleted only after removal succeeds. Failed or unexecuted actions must
not appear as completed deletions. Include affected navigation updates and any
failures in execution outcomes so inconsistencies remain visible.

Update current indexes and other maintained navigation, including misleading
restore instructions. Historical reports, snapshots and manifests remain as written;
their old references do not promise that retired content is still available.
Distinguish preexisting broken links from regressions caused by the cleanup, and
use documented path mappings where needed rather than rewriting historical records.

### Reassessment during ticket completion

Maintain structured reassess-later entries in the authoritative evidence-review
artifacts, recording the remaining use and a triggering ticket identity. Ticket identity
includes its feature/repository context where necessary to avoid number collisions.

After ticket feature development and code/policy integration complete, and before
completion bookkeeping, the development checklist checks the generated reassessment
view for entries
matching the current ticket. Matching entries are reassessed; reaching the trigger
does not itself permit deletion.

If the ticket cannot resolve an entry, keep the evidence and place the unresolved
decision on the next milestone's human QA checklist. Do not silently leave it
behind or require an indefinite chain of future reassessment tickets. Uncertainty
without a usable ticket trigger also remains protected and visible to human QA.

### Similar versions and proposed merges

Detect byte-identical duplicates with hashes while accounting for required paths
and readers. For differing versions, identify useful differences in source,
outcomes, failures, decisions and limitations. Newness alone is insufficient.

Workers may propose merging related artifacts with a concise reason. Agents
prepare the merged file and explain what it preserves and omits. Keep originals
while the proposal awaits review. The fresh reviewer checks the merged content
against originals before human review; the human approves or requests changes at
milestone QA. Python deletes approved originals only after required checks still
pass. Changed merged content or assessed originals requires renewed relevant
review and approval. Durable records do not become disposable merely because a
merged summary exists.

### Guided human evidence review

The proposed `review-evidence` skill uses the structured records and tool-generated
queue. It starts with counts and a short overview, groups related decisions across
tickets, and presents a small batch at a time. Each item explains what the files
establish, the proposed action, information that would be lost and the reviewer's
recommendation, with originals and proposed merges available for inspection.

Offer approve, keep, request changes and defer. Permit batch approval only for
explicitly listed items sharing a rationale. Routine eligible cleanup appears in
a concise inspectable summary; uncertain cases and proposed merges receive direct
human attention. Routine policy-compliant deletion does not require human approval
for each batch.

Save decisions as review proceeds and resume without repeating unchanged completed
items. Unanswered or deferred items remain protected. Changed proposals require
renewed approval. The skill records decisions; Python performs deletion.

In early calibration, collect human judgments before revealing agent recommendations.
After calibration, show recommendations first to reduce review effort. Evidence
cleanup approval is a separate review decision, never exact-candidate QA acceptance,
permission to promote, or a finding disposition that substitutes for either.

### Concise bookkeeping and historical account

Record ordinary cleanup in existing ticket completion records or evidence indexes:
removed categories, retained results, eligibility reasons and checks performed.
Avoid another large narrative report or permanent inventory of every deleted log.
The detailed working JSON supports execution; its long-term retention is itself
subject to the policy while required approval and result records survive.

Use a separate historical account for larger migrations. The completed November
cleanup belongs in repository history documentation with incoming links repaired
and historical M1 status clearly dated. Its useful authority, scope, losses,
verification and exceptions should survive relocation or shortening. This draft
does not move or delete that account.

If reporting cleanup size, distinguish working-tree file counts and logical bytes
from allocated filesystem space. None of these establishes Git-history reduction
or remote storage savings; deleting tracked files does not remove historical blobs.

## Testing Decisions

Use the existing public CLI, scripted external processes and real disposable Git
repositories as the proposed highest testing seam. Exercise the local cleanup tool
through its public command-line behavior with disposable evidence directories and
observable JSON/filesystem outcomes. The exact command surface is not yet chosen.
Confirm this proposed seam during ticket planning; a public internal-module testing
seam is not assumed or authorized by this draft.

Prior art includes existing CLI/report validation, human-decision, milestone,
QA-promotion and continuation tests. Reuse relevant existing coverage instead of
duplicating the full matrix. Required final-source checks and independent reviews
remain governed by the repository testing policy.

The first cleanup-capable slice must consume evidence from the preceding capture
slice and cover inventory, assessment, review, preview and guarded deletion on a
small representative sample. Creation is delivered first rather than deferring
the capture skill until after cleanup exists.
Test observable outcomes and meaningful failures, not implementation details or
whether generated prose matches a template.

Include eligible routine output, durable/protected evidence, a substantive summary
needing correction, related versions requiring a merge proposal, a cross-assignment
dependency, incomplete/conflicting approvals and a file changed after assessment.
Show that eligible material can be deleted and protected or stale material cannot.
Keeping everything is not a passing result. Cover reassessment flowing from ticket
completion to milestone QA and actual execution outcomes differing from approvals.

Add representative cases for a log or archive containing protected review content,
unknown/missing values versus observed zero or empty values, direct ticket-folder
placement and linked shared milestone evidence. Check that existing navigation is
marked deleted only for successful removals, failures remain visible, historical
records stay unchanged, and protected survivors retain their identities. A missing
temporary run directory alone must not cause deletion eligibility. For necessary
moves, verify byte preservation, path mapping and affected readers.

For judgment calibration, the human labels a representative initial sample delete,
keep, merge proposed or unsure, with short reasons. Keep those answers hidden from
workers and the fresh reviewer until their decisions are recorded. Compare human
judgments against both worker proposals and final reviewer decisions, resolve
disagreements with the human, revise criteria and repeat. Disputed evidence is not
deleted during calibration. Repeat assessment on unchanged samples to evaluate
decision consistency without requiring identical wording. Scripted agents can test
tool contracts but cannot establish the quality of real agent judgment.

Validate the review skill with realistic isolated use: a small batch, grouped
approval, disputed merge, deferred item, changed proposal and pause/resume. Check
that the human can inspect relevant details without reviewing unrelated raw files,
and that cleanup approval cannot produce milestone acceptance.

Validate the capture skill and helper through their public command-line and
observable filesystem/record outcomes: ticket capture, shared milestone capture
linked from relevant tickets, separate parallel-producer destinations, provenance
registration and original-versus-derived labeling. Demonstrate capture feeding
later inventory and assessment without concurrent changes to review decisions or
accidental reuse of prior approval. Check routing through existing development
guidance and preservation of protected input/output boundaries. Include capture
in an early complete vertical slice rather than treating it as an isolated layer.

Keep validation efficient: one shared inventory/reference report, bounded worker
assignments, targeted reviewer inspection and representative behavioral scenarios.
Record observed limitations rather than claiming universal consistency from a finite
trial. No runtime tests or agent calibration have been performed for this draft.

Apply the current AGENTS.md ADAPT compute policy during implementation and new
verification, with explicit acceptance criteria in proposed ticket 26. Before
tests or intensive work, check the hostname, use the applicable compute-routing
skill and current capacity to select the host/resources, and bound concurrency.
Confirm actual execution host, architecture, checkout/worktree, source revision
and relevant dirty changes; use the documented checkout-local environment.
Capture those facts with commands/results and any Slurm job ID, and preserve
required node-local results in shared storage before releasing resources. Missing
access or capacity leaves a stated verification gap rather than justifying
intensive work on a login node. No unnecessary GPU/architecture matrix is required.
Historical tickets 01–24 retain their original execution provenance; do not relabel
their evidence or rerun historical work solely to retrofit this newer policy.

For evidence-only cleanup, verify relevant file identities, retained summaries,
navigation and affected readers rather than automatically replaying the runtime
suite or historical helper scripts. Preserve earlier test results with their
actual source and scope. Implementing or changing executable cleanup tooling still
requires the repository's applicable behavioral and final-source checks.

## Out of Scope

- Unapproved changes to ticket scope, dependencies, milestone membership or frozen inputs.
- Automatic evidence cleanup within the harness lifecycle. Local tooling and
  development guidance come first; runtime adoption needs separate approved work.
- Executing cleanup, launching assessment workers, committing changes or rewriting
  Git history merely because this draft exists.
- Removing compatibility support, wrappers, formats or stopped-run support under
  the guise of evidence retention.
- Replacing original independent review reports or human approvals with summaries.
- Treating cleanup approval as software acceptance, promotion permission or an
  amendment to active frozen inputs.

## Further Notes

Tickets 25–30 deliver this spec before the postponed operator work. The
[ticket index](README.md#complete-ticket-index), [milestones](milestones.md) and
[numbering map](archive/evidence-policy-numbering-history.md) define the sequence.
Completed 01–24 and accepted M1 remain intact. The former open tickets 25–38 are
now 31–44. General QA guidance in 31 consumes the evidence-review capability;
correction planning/execution in 32–33 preserve versioned amendments; runtime
review enforcement in 39 and real-agent proof in 40 retain their original scope.
Automatic cleanup inside the harness remains separate future work. E1 ticket 41
remains independent, immediately after verified 40, and is not a release gate.

The current lossless-capture guidance remains applicable until the implementation
tickets reconcile it with selective retirement. A planning amendment is not proof
that the local tool, skills or runtime adoption have already been implemented.

Sources: [human C1–C10 choices](evidence/evidence-retention-audit-01/retention-decisions.md),
[previous cleanup account](evidence-cleanup-and-organization-decisions.md),
[evidence navigation](evidence/README.md),
[development review contract](../../docs/agents/review-records.md),
[ADR-0001](../../docs/adr/0001-reusable-harness-and-local-integration.md) and
[ADR-0002](../../docs/adr/0002-human-qa-gates-feature-promotion.md).
The amendment preserves both ADRs' authority and human acceptance boundaries.
