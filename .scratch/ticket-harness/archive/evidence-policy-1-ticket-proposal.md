# Ticket harness — approved evidence-policy amendment and complete open tickets

**Approved plan version:** evidence-policy-1. **Base:** oop-v2 / review-process-1.

**Publication approval:** [Human decision and scope](evidence-policy-approval.md).

The [feature spec](spec.md), [evidence spec](evidence-policy.md), individual
tickets, [milestones](milestones.md) and [numbering map](archive/evidence-policy-numbering-history.md)
are the coherent approved authoring bundle. The prior approved proposal and all
original bodies are [archived](archive/before-evidence-policy-1/README.md).

## Preferred order, dependencies and membership

Completed 01–24 and M1 acceptance remain intact. New 25–30 precede the former open
25–38, now 31–44. The human requested capture first, then cleanup. EC1 follows
25–26, EC2 follows 27, and EC3 follows 28–30. Existing M2 follows accepted EC3.
E1 remains independent after verified 40. Publication starts no implementation.

<a id="published-slice-to-ticket-mapping"></a>

| Ticket | Prerequisites | Membership | Readiness |
| --- | --- | --- | --- |
| [25: Guide ticket and shared evidence creation](issues/25-guide-ticket-and-shared-evidence-creation.md) | 24 | EC1 | ready-for-agent |
| [26: Review and safely retire routine ticket evidence](issues/26-review-and-safely-retire-routine-ticket-evidence.md) | 25 | EC1 | ready-for-agent |
| [27: Assess evidence in parallel and consolidate fresh review](issues/27-assess-evidence-in-parallel-and-consolidate-fresh-review.md) | 26 | EC2 | ready-for-agent |
| [28: Guide human review of summaries and proposed merges](issues/28-guide-human-review-of-summaries-and-proposed-merges.md) | 27 | EC3 | ready-for-agent |
| [29: Reassess retained evidence during ticket completion](issues/29-reassess-retained-evidence-during-ticket-completion.md) | 28 | EC3 | ready-for-agent |
| [30: Calibrate and adopt the complete evidence workflow](issues/30-calibrate-and-adopt-the-complete-evidence-workflow.md) | 29 | EC3 | ready-for-agent |
| [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md) | 10, 14, 30 | M2 | ready-for-agent |
| [32: Propose a versioned correction plan](issues/32-propose-versioned-qa-corrections.md) | 10, 31 | M2 | ready-for-agent |
| [33: Execute approved QA corrections](issues/33-execute-approved-qa-corrections.md) | 15, 32 | M2 | ready-for-agent |
| [34: Operate the orchestrator in the background](issues/34-operate-the-harness-in-the-background.md) | 15 | M2 | ready-for-agent |
| [35: Continue independent work inside the current milestone](issues/35-continue-independent-work-after-blocks.md) | 12, 06 | M2 | ready-for-agent |
| [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md) | 03, 19 | M3 | ready-for-agent |
| [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md) | 10, 36 | M3 | ready-for-agent |
| [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md) | 37, 19 | M3 | ready-for-agent |
| [39: Enforce traceable runtime review checkpoints](issues/39-enforce-traceable-runtime-review-checkpoints.md) | 19, 24, 36, 37, 38 | M3 | ready-for-agent |
| [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md) | 15, 38, 08, 39 | M3 | ready-for-agent |
| [41: Run the early context-budget comparison](issues/41-compare-configurable-agent-context-limits.md) | 40 | E1 | ready-for-agent |
| [42: Verify runtime write and approval boundaries](issues/42-verify-role-write-boundaries.md) | 31, 40 | M4 | ready-for-agent |
| [43: Run a generated approved plan through the runtime](issues/43-run-a-generated-plan-through-the-runtime.md) | 10, 33, 37 | M4 | ready-for-agent |
| [44: Demonstrate the revised first usable release](issues/44-demonstrate-the-first-usable-release.md) | 11, 34, 35, 42, 43, 07 | M4 | ready-for-agent |

## Shared implementation and verification contract


The accepted spec governs every ticket. Each slice delivers usable behavior,
its structured records, user/agent guidance and verification together. Early
slices explicitly retain unsupported or uncertain material; they cannot claim
the later capabilities or bypass required review to demonstrate deletion.

Approved testing seam: public command-line behavior, scripted external processes
and observable JSON/filesystem/Git outcomes in disposable repositories. This
extends the existing CLI testing approach to the local evidence tool; no new
public internal-module seam is proposed. The human approved this seam as part of local publication. Real agent calibration is separate from scripted contract tests.

Follow the [testing policy](../../docs/agents/testing.md),
[Python environment](../../docs/agents/python-environment.md),
[development review contract](../../docs/agents/review-records.md) and applicable
[compute routing](../../AGENTS.md#adapt-compute). Use TDD for new executable
behavior at the public seam; map existing coverage before adding cases. Executable
implementation checkpoints retain the full final-source suite, strict typing,
lint, format, whitespace and separate independent Spec/Standards reviews.
Packaging/entry-point changes also require installed CLI checks. Guidance changes
need skill, routing and link validation and isolated behavioral examples.

Evidence-only cleanup does not itself require replaying historical runtime tests.
Tool implementation still requires its applicable checks. Preserve actual source,
command/result identities and original reviews; do not claim historical results
verify new code. Shared-state, lifecycle, persistence/restoration or additional
writer changes require the existing architecture-trigger assessment; cumulative
architecture review precedes every required milestone QA readiness claim.

### Role configuration

Inherit GPT-6.1 Sol with fresh contexts and the 250,000 active-context target.
Implementation and repair use Medium; Spec and Standards each use independently
configured High. No new implementation/repair overrides are proposed.

The product workflow's evidence assessors use Medium, and its separate fresh final
evidence reviewer uses High. These roles do not replace implementation Spec or
Standards review. Use non-overlapping worker assignments, bounded by the available
execution resources, rather than requiring exactly three workers for every task.
Required workflow guidance comes from the accepted evidence criteria, capture and
review skills as delivered, existing development review/testing guidance, and
skill-creation/writing guidance for skill authors. Calibration follows the existing
[reviewer-evaluation procedure](../../.agents/skills/custom/evaluate-reviewers/SKILL.md).
Unavailable role settings or real assignments are reported, not simulated as proof.

### Ownership and authority

Python owns deterministic routing, inventory, reference discovery, record
validation, guarded deletion and actual execution results. Assessment workers own
separate temporary proposals. The fresh reviewer owns consolidation, cross-file
synthesis and final deletion approvals within each authoritative review artifact.
The human owns merge approval, calibration adjudication and unresolved milestone
choices. Capture and reassessment views confer no deletion authority. Changed
assessed content invalidates applicable prior approvals; execution preserves
approval and actual-result distinctions, including partial failures.


## Approved integration changes

Tickets 25–30 have the accepted new criteria below. Ticket 31 preserves the former 25 criteria and adds consumption of the verified evidence-review skill/queue plus prerequisite 30. Other inherited criteria retain their outcomes with current references remapped. M2 now follows EC3. Final M4 acceptance includes the new evidence capability cumulatively. Captured inputs, historical numbers and completed-ticket evidence remain unchanged.

## Complete open-ticket bodies

## 25: Guide ticket and shared evidence creation

**What to build:** The `capture-evidence` skill and Python routing/registration
workflow that give evidence-producing agents consistent ticket or shared milestone
destinations and reliable provenance. Deliver independently usable capture before
the cleanup workflow is implemented.

**Blocked by:** [24: Own milestone review and checkpoint continuation (completed).](issues/24-own-milestone-review-and-checkpoint-continuation.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC1. M1 acceptance is already recorded; EC1 remains unaccepted.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance; preserve existing independent review/capture requirements and applicable
compute routing from AGENTS.md.

**Context:** Evidence placement and historical identity; evidence creation skill;
authoritative JSON artifacts and protected output boundaries.

### Acceptance criteria

- [ ] Deliver a repo-owned capture skill that identifies the ticket and purpose before capture, delegates destination selection and registration to Python, and reuses existing test/review guidance rather than duplicating it.
- [ ] Write ticket evidence directly into its corresponding folder. Route genuinely shared evidence to descriptively named shared folders and milestone subfolders linked from relevant tickets, keeping one authoritative copy.
- [ ] Register source version, producing command or activity, observed result and file identity; preserve original captures and label derived content. Registration supplies facts, not retention or deletion approval.
- [ ] Allocate distinct capture locations for parallel producers and consolidate registrations without competing edits to authoritative review decisions. Existing captures are not overwritten and newly created files do not inherit old deletion approvals.
- [ ] Establish a JSON review artifact per ticket or shared evidence folder as applicable, with capture metadata clearly separated from later assessments, approvals and execution results. Ticket artifacts reference shared records without duplicating their decisions.
- [ ] Route applicable development workflows through the skill/helper. Respect approved-input and frozen-file boundaries and keep harness runtime adoption separate. Leave historical organization and embedded paths unchanged unless a concrete need and reader checks permit a move.
- [ ] Demonstrate capture through the skill into the correct folders with valid provenance and protected originals, including shared milestone evidence linked from relevant tickets. This ticket neither authorizes deletion nor depends on the later cleanup tool.

### Verification

Exercise ticket and shared capture, parallel producer destinations, provenance,
original/derived distinction and protected destinations through public commands
and filesystem/JSON outcomes. Validate the skill and instruction routing plus the
shared implementation gates. This independently verifiable slice supplies ticket
26 with real captured evidence, without claiming cleanup or runtime adoption.

#### 26: Review and safely retire routine ticket evidence

**What to build:** Use ticket 25's captured evidence to deliver a narrow complete
assessment, fresh review, preview and Python-controlled deletion workflow. Establish
standing retention guidance and demonstrate execution under the current ADAPT
compute policy rather than assuming historical execution practices still apply.

**Blocked by:** 25: Guide ticket and shared evidence creation.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC1. Human EC1 acceptance follows both tickets 25 and 26.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared role/testing contract; TDD and test-strategy; skill-writing
guidance for agent instructions; current AGENTS.md compute routing and adapt-compute
when its host conditions apply. Evidence review uses a fresh High reviewer
independently of implementation reviews.

**Context:** Policy and decision order; structured records; fresh review and Python
execution; navigation for deleted evidence; protected originals and frozen inputs;
current execution-host and environment requirements.

### Acceptance criteria

- [ ] Publish standing evidence policy guidance that preserves the agreed decision order, scope and authority boundaries, reconciling capture versus later retirement with existing preservation guidance. Do not change runtime integrity or continuation contracts.
- [ ] Consume ticket 25's capture registrations to inventory, assess, preview, validate approvals and execute routine evidence cleanup. Preserve useful results tied to the actual source and observed activity.
- [ ] Extend each authoritative JSON artifact with distinct proposed actions, a fresh reviewer's explicit approvals and actual execution outcomes. Consolidate temporary proposals with provenance; do not require parallel assessment yet.
- [ ] Apply required fields and fixed reasons rather than allowing filename-based approval. Keep durable records, unresolved uses, unique needed content and unknown or unsupported evidence. No lossy substantive replacement or merge is authorized by this narrow slice.
- [ ] Preview changes no evidence files. Python deletion requires complete eligible decisions and unchanged assessed identities; missing approvals, missing retained results, changed files or protected uses block affected files. Agents do not perform deletion.
- [ ] Record real successes and failures; update maintained navigation with `(deleted)`, a reason and retained-result reference where available only after successful removal. Do not create a permanent entry for each deleted log or rewrite historical records.
- [ ] Reconcile approved versus actual path changes and protected survivors. Demonstrate eligible deletion as well as protected retention and stale/incomplete rejection through the public CLI on disposable evidence.
- [ ] Before tests, builds, dependency builds or other intensive work, check the current hostname and apply AGENTS.md's ADAPT routing when applicable. Select a suitable compute host using current capacity and workload needs; keep intensive work off login nodes and bound concurrency by available or allocated resources.
- [ ] On the execution host, confirm hostname, architecture, exact checkout/worktree, HEAD and relevant dirty changes; use that checkout's documented uv environment. Capture these facts with commands, results and any Slurm job ID through the evidence workflow, retaining required artifacts in shared storage before releasing resources.
- [ ] Apply the current compute policy to new verification, including checks of previously implemented behavior. Preserve tickets 01–24's historical evidence with its original scope; do not relabel it as ADAPT-policy-compliant or rerun history merely to retrofit provenance. Unavailable compute access/resources leave explicit verification gaps rather than authorizing login-node fallback.
- [ ] Prepare a small early human-calibration sample and inspection instructions for EC1. Human labels stay hidden from the assessor and fresh reviewer until their decisions are saved; disputed content remains protected. Actual human comparison is an EC1 acceptance action, not agent self-approval.

### Verification

Use a small routine-output sample with a protected record, unknown content and an
altered-after-assessment file. Observe public command exits, JSON states, actual
files and navigation; include a failed removal with an honest outcome. Run the
shared required implementation checks and reviews on policy-appropriate hosts,
recording actual host/architecture/source/environment provenance and resource
selection. Use the routing appropriate to the workload, not an unnecessary
GPU/architecture matrix. EC1 demonstrates the complete narrow capture-to-cleanup
path across tickets 25–26 without claiming parallel assessment or broad calibration.

#### 27: Assess evidence in parallel and consolidate fresh review

**What to build:** Tool-guided parallel assessment of ticket evidence with one
shared inventory/reference report and a fresh final reviewer who consolidates
worker proposals and decides eligible cleanup across related files.

**Blocked by:** 26: Review and safely retire routine ticket evidence.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC2; requires human EC1 acceptance.

**Worker reasoning:** Inherit Medium for implementation and repair; workflow
assessors Medium and the fresh evidence reviewer High.

**Role guidance:** Shared contract; TDD and test-strategy; explicit policy criteria
and existing review-evaluation guidance for preparation of the EC2 human comparison.

**Context:** Structured records; parallel assessment; content-based classification;
cross-ticket dependencies, protected survivors and shared evidence.

### Acceptance criteria

- [ ] Generate one inventory/reference report and fixed non-overlapping worker assignments. Workers apply the same criteria/reason codes, save separate temporary proposals and flag external dependencies without deleting files or editing sibling proposals.
- [ ] Supply a fresh final reviewer the proposals and relevant originals for cross-file synthesis, conflict resolution and final approval. Consolidate into one authoritative JSON per ticket/shared folder with worker provenance; shared decisions remain referenced rather than copied.
- [ ] Inspect content and uses of mixed logs, archives and source copies. Preserve original reviews, sole needed content, unexplained failures, active/continuable-run requirements and completion records consumed by later work. Unknown eligibility stays blocked.
- [ ] Treat reference discovery as bounded evidence, not proof of no consumer. A missing temporary run directory does not establish deletion eligibility. Account for cross-assignment and cross-ticket dependencies before approval.
- [ ] Distinguish exact duplicate content from differing versions and required paths. Route substantive replacement/merge candidates to review-needed status with originals retained until the later supported approval path is available.
- [ ] Keep incomplete assignments, conflicts, stale content and unmet conditions visible and protected while independently eligible groups can proceed. Preserve original protected content, historical records and required symlink targets during execution.
- [ ] Demonstrate actual independent parallel worker assessments and a fresh High review on a bounded isolated sample, alongside scripted tool-contract tests. Missing real assignments/settings are a concrete verification gap, not a scripted substitute.
- [ ] Prepare the EC2 blinded human comparison, recording the worker and final-reviewer choices before revealing human labels. Carry disagreement and limitations into QA without claiming general reliability.

### Verification

Exercise disjoint work, conflicting/incomplete proposals, cross-ticket evidence,
embedded reviews in routine-looking files, archive content, differing versions and
stale approvals. Show consolidation and guarded deletion with protected survivors
unchanged. Run shared checks and independent implementation reviews; actual agent
judgments are additionally inspected at EC2 QA.

#### 28: Guide human review of summaries and proposed merges

**What to build:** The `review-evidence` skill and structured review queue that
let humans efficiently inspect proposed replacements, approve reviewed merges,
request changes or defer, with Python executing only still-valid approvals.

**Blocked by:** 27: Assess evidence in parallel and consolidate fresh review.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3; requires human EC2 acceptance.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance. The fresh evidence reviewer independently checks substantive replacements.

**Context:** Similar versions and proposed merges; guided human review; JSON facts,
review decisions, derived views and explicit unknown-versus-zero semantics.

### Acceptance criteria

- [ ] Agents prepare useful summaries or merged files with source identities, retained facts, useful differences, omissions and concise reasons. Label lossy derivatives, preserve unknown/absent values versus observed zero/empty collections and keep originals until applicable checks and approvals pass.
- [ ] A fresh reviewer compares substantive replacements against originals and corrects inaccurate or incomplete content before approval. Do not replace durable original independent reviews or human approvals with summaries.
- [ ] Human milestone QA receives proposed merges, reviewed content and omissions without manually merging. Original deletion requires that human approval plus valid fresh review and current file identities; changes require renewed applicable approval.
- [ ] Deliver a review skill backed by a generated queue, with overview, related groups, small batches, inspectable sources and approve/keep/request-changes/defer choices. Batch approvals name explicit items sharing a rationale; routine eligible cleanup remains inspectable without requiring human approval of every batch.
- [ ] Save human decisions in authoritative review artifacts and resume without repeating unchanged completed items. Unanswered/deferred items remain protected; changed proposals cannot reuse approvals. The queue is a derived view, not another authoritative decision store.
- [ ] Support blinded early calibration before recommendations are revealed, then recommendation-first ordinary review. Cleanup approval never writes candidate acceptance, promotes refs or substitutes for a finding disposition.
- [ ] Demonstrate proposed merge through fresh review, human approval, preview and Python deletion, including correction of a misleading summary and refusal of stale/unapproved replacement. Record execution and navigation truthfully on success and failure.

### Verification

Validate the skill using realistic isolated requests: related groups, bounded
batches, inspect differences, correction, pause/resume, deferral and stale content.
Compare missing attempts against observed zero attempts and verify protected
originals remain intact. Use scripted human decision artifacts for routine tests;
actual human decisions belong to calibration/QA. Run shared implementation gates.

#### 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** 28: Guide human review of summaries and proposed merges.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

### Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

### Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

#### 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** 29: Reassess retained evidence during ticket completion.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#evidence-creation-skill-and-helper), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

## 26: Review and safely retire routine ticket evidence

**What to build:** Use ticket 25's captured evidence to deliver a narrow complete
assessment, fresh review, preview and Python-controlled deletion workflow. Establish
standing retention guidance and demonstrate execution under the current ADAPT
compute policy rather than assuming historical execution practices still apply.

**Blocked by:** [25: Guide ticket and shared evidence creation.](issues/25-guide-ticket-and-shared-evidence-creation.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC1. Human EC1 acceptance follows both tickets 25 and 26.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared role/testing contract; TDD and test-strategy; skill-writing
guidance for agent instructions; current AGENTS.md compute routing and adapt-compute
when its host conditions apply. Evidence review uses a fresh High reviewer
independently of implementation reviews.

**Context:** Policy and decision order; structured records; fresh review and Python
execution; navigation for deleted evidence; protected originals and frozen inputs;
current execution-host and environment requirements.

### Acceptance criteria

- [ ] Publish standing evidence policy guidance that preserves the agreed decision order, scope and authority boundaries, reconciling capture versus later retirement with existing preservation guidance. Do not change runtime integrity or continuation contracts.
- [ ] Consume ticket 25's capture registrations to inventory, assess, preview, validate approvals and execute routine evidence cleanup. Preserve useful results tied to the actual source and observed activity.
- [ ] Extend each authoritative JSON artifact with distinct proposed actions, a fresh reviewer's explicit approvals and actual execution outcomes. Consolidate temporary proposals with provenance; do not require parallel assessment yet.
- [ ] Apply required fields and fixed reasons rather than allowing filename-based approval. Keep durable records, unresolved uses, unique needed content and unknown or unsupported evidence. No lossy substantive replacement or merge is authorized by this narrow slice.
- [ ] Preview changes no evidence files. Python deletion requires complete eligible decisions and unchanged assessed identities; missing approvals, missing retained results, changed files or protected uses block affected files. Agents do not perform deletion.
- [ ] Record real successes and failures; update maintained navigation with `(deleted)`, a reason and retained-result reference where available only after successful removal. Do not create a permanent entry for each deleted log or rewrite historical records.
- [ ] Reconcile approved versus actual path changes and protected survivors. Demonstrate eligible deletion as well as protected retention and stale/incomplete rejection through the public CLI on disposable evidence.
- [ ] Before tests, builds, dependency builds or other intensive work, check the current hostname and apply AGENTS.md's ADAPT routing when applicable. Select a suitable compute host using current capacity and workload needs; keep intensive work off login nodes and bound concurrency by available or allocated resources.
- [ ] On the execution host, confirm hostname, architecture, exact checkout/worktree, HEAD and relevant dirty changes; use that checkout's documented uv environment. Capture these facts with commands, results and any Slurm job ID through the evidence workflow, retaining required artifacts in shared storage before releasing resources.
- [ ] Apply the current compute policy to new verification, including checks of previously implemented behavior. Preserve tickets 01–24's historical evidence with its original scope; do not relabel it as ADAPT-policy-compliant or rerun history merely to retrofit provenance. Unavailable compute access/resources leave explicit verification gaps rather than authorizing login-node fallback.
- [ ] Prepare a small early human-calibration sample and inspection instructions for EC1. Human labels stay hidden from the assessor and fresh reviewer until their decisions are saved; disputed content remains protected. Actual human comparison is an EC1 acceptance action, not agent self-approval.

### Verification

Use a small routine-output sample with a protected record, unknown content and an
altered-after-assessment file. Observe public command exits, JSON states, actual
files and navigation; include a failed removal with an honest outcome. Run the
shared required implementation checks and reviews on policy-appropriate hosts,
recording actual host/architecture/source/environment provenance and resource
selection. Use the routing appropriate to the workload, not an unnecessary
GPU/architecture matrix. EC1 demonstrates the complete narrow capture-to-cleanup
path across tickets 25–26 without claiming parallel assessment or broad calibration.

#### 27: Assess evidence in parallel and consolidate fresh review

**What to build:** Tool-guided parallel assessment of ticket evidence with one
shared inventory/reference report and a fresh final reviewer who consolidates
worker proposals and decides eligible cleanup across related files.

**Blocked by:** 26: Review and safely retire routine ticket evidence.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC2; requires human EC1 acceptance.

**Worker reasoning:** Inherit Medium for implementation and repair; workflow
assessors Medium and the fresh evidence reviewer High.

**Role guidance:** Shared contract; TDD and test-strategy; explicit policy criteria
and existing review-evaluation guidance for preparation of the EC2 human comparison.

**Context:** Structured records; parallel assessment; content-based classification;
cross-ticket dependencies, protected survivors and shared evidence.

### Acceptance criteria

- [ ] Generate one inventory/reference report and fixed non-overlapping worker assignments. Workers apply the same criteria/reason codes, save separate temporary proposals and flag external dependencies without deleting files or editing sibling proposals.
- [ ] Supply a fresh final reviewer the proposals and relevant originals for cross-file synthesis, conflict resolution and final approval. Consolidate into one authoritative JSON per ticket/shared folder with worker provenance; shared decisions remain referenced rather than copied.
- [ ] Inspect content and uses of mixed logs, archives and source copies. Preserve original reviews, sole needed content, unexplained failures, active/continuable-run requirements and completion records consumed by later work. Unknown eligibility stays blocked.
- [ ] Treat reference discovery as bounded evidence, not proof of no consumer. A missing temporary run directory does not establish deletion eligibility. Account for cross-assignment and cross-ticket dependencies before approval.
- [ ] Distinguish exact duplicate content from differing versions and required paths. Route substantive replacement/merge candidates to review-needed status with originals retained until the later supported approval path is available.
- [ ] Keep incomplete assignments, conflicts, stale content and unmet conditions visible and protected while independently eligible groups can proceed. Preserve original protected content, historical records and required symlink targets during execution.
- [ ] Demonstrate actual independent parallel worker assessments and a fresh High review on a bounded isolated sample, alongside scripted tool-contract tests. Missing real assignments/settings are a concrete verification gap, not a scripted substitute.
- [ ] Prepare the EC2 blinded human comparison, recording the worker and final-reviewer choices before revealing human labels. Carry disagreement and limitations into QA without claiming general reliability.

### Verification

Exercise disjoint work, conflicting/incomplete proposals, cross-ticket evidence,
embedded reviews in routine-looking files, archive content, differing versions and
stale approvals. Show consolidation and guarded deletion with protected survivors
unchanged. Run shared checks and independent implementation reviews; actual agent
judgments are additionally inspected at EC2 QA.

#### 28: Guide human review of summaries and proposed merges

**What to build:** The `review-evidence` skill and structured review queue that
let humans efficiently inspect proposed replacements, approve reviewed merges,
request changes or defer, with Python executing only still-valid approvals.

**Blocked by:** 27: Assess evidence in parallel and consolidate fresh review.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3; requires human EC2 acceptance.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance. The fresh evidence reviewer independently checks substantive replacements.

**Context:** Similar versions and proposed merges; guided human review; JSON facts,
review decisions, derived views and explicit unknown-versus-zero semantics.

### Acceptance criteria

- [ ] Agents prepare useful summaries or merged files with source identities, retained facts, useful differences, omissions and concise reasons. Label lossy derivatives, preserve unknown/absent values versus observed zero/empty collections and keep originals until applicable checks and approvals pass.
- [ ] A fresh reviewer compares substantive replacements against originals and corrects inaccurate or incomplete content before approval. Do not replace durable original independent reviews or human approvals with summaries.
- [ ] Human milestone QA receives proposed merges, reviewed content and omissions without manually merging. Original deletion requires that human approval plus valid fresh review and current file identities; changes require renewed applicable approval.
- [ ] Deliver a review skill backed by a generated queue, with overview, related groups, small batches, inspectable sources and approve/keep/request-changes/defer choices. Batch approvals name explicit items sharing a rationale; routine eligible cleanup remains inspectable without requiring human approval of every batch.
- [ ] Save human decisions in authoritative review artifacts and resume without repeating unchanged completed items. Unanswered/deferred items remain protected; changed proposals cannot reuse approvals. The queue is a derived view, not another authoritative decision store.
- [ ] Support blinded early calibration before recommendations are revealed, then recommendation-first ordinary review. Cleanup approval never writes candidate acceptance, promotes refs or substitutes for a finding disposition.
- [ ] Demonstrate proposed merge through fresh review, human approval, preview and Python deletion, including correction of a misleading summary and refusal of stale/unapproved replacement. Record execution and navigation truthfully on success and failure.

### Verification

Validate the skill using realistic isolated requests: related groups, bounded
batches, inspect differences, correction, pause/resume, deferral and stale content.
Compare missing attempts against observed zero attempts and verify protected
originals remain intact. Use scripted human decision artifacts for routine tests;
actual human decisions belong to calibration/QA. Run shared implementation gates.

#### 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** 28: Guide human review of summaries and proposed merges.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

### Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

### Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

#### 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** 29: Reassess retained evidence during ticket completion.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#policy-and-decision-order), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

## 27: Assess evidence in parallel and consolidate fresh review

**What to build:** Tool-guided parallel assessment of ticket evidence with one
shared inventory/reference report and a fresh final reviewer who consolidates
worker proposals and decides eligible cleanup across related files.

**Blocked by:** [26: Review and safely retire routine ticket evidence.](issues/26-review-and-safely-retire-routine-ticket-evidence.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC2; requires human EC1 acceptance.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair; workflow
assessors Medium and the fresh evidence reviewer High.

**Role guidance:** Shared contract; TDD and test-strategy; explicit policy criteria
and existing review-evaluation guidance for preparation of the EC2 human comparison.

**Context:** Structured records; parallel assessment; content-based classification;
cross-ticket dependencies, protected survivors and shared evidence.

### Acceptance criteria

- [ ] Generate one inventory/reference report and fixed non-overlapping worker assignments. Workers apply the same criteria/reason codes, save separate temporary proposals and flag external dependencies without deleting files or editing sibling proposals.
- [ ] Supply a fresh final reviewer the proposals and relevant originals for cross-file synthesis, conflict resolution and final approval. Consolidate into one authoritative JSON per ticket/shared folder with worker provenance; shared decisions remain referenced rather than copied.
- [ ] Inspect content and uses of mixed logs, archives and source copies. Preserve original reviews, sole needed content, unexplained failures, active/continuable-run requirements and completion records consumed by later work. Unknown eligibility stays blocked.
- [ ] Treat reference discovery as bounded evidence, not proof of no consumer. A missing temporary run directory does not establish deletion eligibility. Account for cross-assignment and cross-ticket dependencies before approval.
- [ ] Distinguish exact duplicate content from differing versions and required paths. Route substantive replacement/merge candidates to review-needed status with originals retained until the later supported approval path is available.
- [ ] Keep incomplete assignments, conflicts, stale content and unmet conditions visible and protected while independently eligible groups can proceed. Preserve original protected content, historical records and required symlink targets during execution.
- [ ] Demonstrate actual independent parallel worker assessments and a fresh High review on a bounded isolated sample, alongside scripted tool-contract tests. Missing real assignments/settings are a concrete verification gap, not a scripted substitute.
- [ ] Prepare the EC2 blinded human comparison, recording the worker and final-reviewer choices before revealing human labels. Carry disagreement and limitations into QA without claiming general reliability.

### Verification

Exercise disjoint work, conflicting/incomplete proposals, cross-ticket evidence,
embedded reviews in routine-looking files, archive content, differing versions and
stale approvals. Show consolidation and guarded deletion with protected survivors
unchanged. Run shared checks and independent implementation reviews; actual agent
judgments are additionally inspected at EC2 QA.

#### 28: Guide human review of summaries and proposed merges

**What to build:** The `review-evidence` skill and structured review queue that
let humans efficiently inspect proposed replacements, approve reviewed merges,
request changes or defer, with Python executing only still-valid approvals.

**Blocked by:** 27: Assess evidence in parallel and consolidate fresh review.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3; requires human EC2 acceptance.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance. The fresh evidence reviewer independently checks substantive replacements.

**Context:** Similar versions and proposed merges; guided human review; JSON facts,
review decisions, derived views and explicit unknown-versus-zero semantics.

### Acceptance criteria

- [ ] Agents prepare useful summaries or merged files with source identities, retained facts, useful differences, omissions and concise reasons. Label lossy derivatives, preserve unknown/absent values versus observed zero/empty collections and keep originals until applicable checks and approvals pass.
- [ ] A fresh reviewer compares substantive replacements against originals and corrects inaccurate or incomplete content before approval. Do not replace durable original independent reviews or human approvals with summaries.
- [ ] Human milestone QA receives proposed merges, reviewed content and omissions without manually merging. Original deletion requires that human approval plus valid fresh review and current file identities; changes require renewed applicable approval.
- [ ] Deliver a review skill backed by a generated queue, with overview, related groups, small batches, inspectable sources and approve/keep/request-changes/defer choices. Batch approvals name explicit items sharing a rationale; routine eligible cleanup remains inspectable without requiring human approval of every batch.
- [ ] Save human decisions in authoritative review artifacts and resume without repeating unchanged completed items. Unanswered/deferred items remain protected; changed proposals cannot reuse approvals. The queue is a derived view, not another authoritative decision store.
- [ ] Support blinded early calibration before recommendations are revealed, then recommendation-first ordinary review. Cleanup approval never writes candidate acceptance, promotes refs or substitutes for a finding disposition.
- [ ] Demonstrate proposed merge through fresh review, human approval, preview and Python deletion, including correction of a misleading summary and refusal of stale/unapproved replacement. Record execution and navigation truthfully on success and failure.

### Verification

Validate the skill using realistic isolated requests: related groups, bounded
batches, inspect differences, correction, pause/resume, deferral and stale content.
Compare missing attempts against observed zero attempts and verify protected
originals remain intact. Use scripted human decision artifacts for routine tests;
actual human decisions belong to calibration/QA. Run shared implementation gates.

#### 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** 28: Guide human review of summaries and proposed merges.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

### Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

### Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

#### 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** 29: Reassess retained evidence during ticket completion.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#parallel-assessment-fresh-review-and-execution), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

## 28: Guide human review of summaries and proposed merges

**What to build:** The `review-evidence` skill and structured review queue that
let humans efficiently inspect proposed replacements, approve reviewed merges,
request changes or defer, with Python executing only still-valid approvals.

**Blocked by:** [27: Assess evidence in parallel and consolidate fresh review.](issues/27-assess-evidence-in-parallel-and-consolidate-fresh-review.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC3; requires human EC2 acceptance.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance. The fresh evidence reviewer independently checks substantive replacements.

**Context:** Similar versions and proposed merges; guided human review; JSON facts,
review decisions, derived views and explicit unknown-versus-zero semantics.

### Acceptance criteria

- [ ] Agents prepare useful summaries or merged files with source identities, retained facts, useful differences, omissions and concise reasons. Label lossy derivatives, preserve unknown/absent values versus observed zero/empty collections and keep originals until applicable checks and approvals pass.
- [ ] A fresh reviewer compares substantive replacements against originals and corrects inaccurate or incomplete content before approval. Do not replace durable original independent reviews or human approvals with summaries.
- [ ] Human milestone QA receives proposed merges, reviewed content and omissions without manually merging. Original deletion requires that human approval plus valid fresh review and current file identities; changes require renewed applicable approval.
- [ ] Deliver a review skill backed by a generated queue, with overview, related groups, small batches, inspectable sources and approve/keep/request-changes/defer choices. Batch approvals name explicit items sharing a rationale; routine eligible cleanup remains inspectable without requiring human approval of every batch.
- [ ] Save human decisions in authoritative review artifacts and resume without repeating unchanged completed items. Unanswered/deferred items remain protected; changed proposals cannot reuse approvals. The queue is a derived view, not another authoritative decision store.
- [ ] Support blinded early calibration before recommendations are revealed, then recommendation-first ordinary review. Cleanup approval never writes candidate acceptance, promotes refs or substitutes for a finding disposition.
- [ ] Demonstrate proposed merge through fresh review, human approval, preview and Python deletion, including correction of a misleading summary and refusal of stale/unapproved replacement. Record execution and navigation truthfully on success and failure.

### Verification

Validate the skill using realistic isolated requests: related groups, bounded
batches, inspect differences, correction, pause/resume, deferral and stale content.
Compare missing attempts against observed zero attempts and verify protected
originals remain intact. Use scripted human decision artifacts for routine tests;
actual human decisions belong to calibration/QA. Run shared implementation gates.

#### 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** 28: Guide human review of summaries and proposed merges.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3.

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

### Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

### Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

#### 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** 29: Reassess retained evidence during ticket completion.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#guided-human-evidence-review), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

## 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** [28: Guide human review of summaries and proposed merges.](issues/28-guide-human-review-of-summaries-and-proposed-merges.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC3.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

### Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

### Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

#### 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** 29: Reassess retained evidence during ticket completion.

**Status:** ready-for-agent

**Plan version:** evidence-policy-1.

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#reassessment-during-ticket-completion), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

## 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** [29: Reassess retained evidence during ticket completion.](issues/29-reassess-retained-evidence-during-ticket-completion.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md); [evidence spec](evidence-policy.md).

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Agent context limit:** 250,000 active tokens; [role defaults](ticket-proposal.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping;
historical cleanup account and integration with postponed open work.

### Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Move the completed November cleanup account to repository history documentation, preserving useful authority/scope/loss/verification/exception information, clearly dating historical status and repairing maintained incoming links. Avoid unrelated historical rewrites or blanket evidence relocation.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

### Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills, current links and historical-record relocation; source reviews and final
cumulative architecture assessment remain separate from evidence calibration.


### Shared requirements and handoff

Follow the [scoped evidence contract](evidence-policy.md#testing-decisions), [approved shared verification/ownership contract](ticket-proposal.md#shared-implementation-and-verification-contract), and [milestone gates](milestones.md). Apply the current [AGENTS.md compute routing](../../AGENTS.md#adapt-compute), [environment](../../docs/agents/python-environment.md), [testing policy](../../docs/agents/testing.md) and [development review contract](../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.

<a id="r07-guide-a-human-through-milestone-qa"></a>

## 31: Guide a human through milestone QA

**What to build:** Create the QA-session skill for existing requests. Guide the planned checks, record observed results, and write the exact artifact only after explicit human acceptance. A request to self-approve from passing tests does not authorize acceptance. Findings remain visible and no product code or integration ref is changed by this skill.

**Blocked by:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md); [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md); [30: Calibrate and adopt the complete evidence workflow](issues/30-calibrate-and-adopt-the-complete-evidence-workflow.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R07](ticket-proposal.md#r07-guide-a-human-through-milestone-qa).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [feature to development promotion and human qa](spec.md#feature-to-development-promotion-and-human-qa).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Create a focused QA-session skill that reads the exact request/candidate and guides the human through planned checks, evidence inspection, and observable acceptance conditions.
- [ ] Record findings and withhold acceptance until the human explicitly approves; passing automated tests or an agent recommendation is insufficient.
- [ ] Write only the precise decision artifact for matching current identities, preserving provenance and rejecting stale requests.
- [ ] Do not implement corrections or change product source/integration refs; propose findings for the versioned planning workflow.
- [ ] Validate isolated explicit-approval, withheld-approval, stale-request, and self-approval-request examples without altering actual user work.

- [ ] QA guidance presents source-identified review reports, open findings and human disposition reasons alongside candidate evidence; recording a review decision never substitutes for the exact separate QA acceptance.

- [ ] Use the verified evidence-review skill and derived ticket/shared-artifact queue for applicable milestone evidence choices, without duplicating retention decisions or treating evidence approval as the exact candidate QA decision. Preserve captured/frozen request inputs; proposals made during a frozen wait remain outside frozen evidence and follow renewed readiness rules where applicable.

### Verification

Skill validation and isolated QA examples cover explicit approval, withheld approval, and stale candidate identities using disposable artifacts.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 25 to 31 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r08-propose-a-versioned-correction-plan"></a>

## 32: Propose a versioned correction plan

**What to build:** Extend the unified planning flow for QA feedback: propose focused correction tickets and affected spec/milestone changes, show the changes from the approved version, and obtain targeted approval. Unchanged requirements retain their approval; prior versions and completed-ticket history remain intact.

**Blocked by:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md); [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R08](ticket-proposal.md#r08-propose-a-versioned-correction-plan).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [corrections and safe continuation](spec.md#corrections-and-safe-continuation).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Use the unified planning workflow to turn QA findings into focused correction-ticket and affected spec/milestone proposals.
- [ ] Show changes from the approved version, retain approval of unchanged requirements, and reopen targeted grilling for substantive unresolved decisions.
- [ ] Keep unapproved changes staged; publish only explicitly accepted amendments with a new plan version and stable IDs/history.
- [ ] Preserve prior snapshots, completed-ticket evidence, decisions, and the current milestone's gate on later work.
- [ ] Demonstrate feedback updating both the proposal and staged spec consistently. Runtime execution of amendments belongs to ticket 33.

- [ ] A proposed review follow-up that changes approved scope, ownership or milestone conditions enters the versioned amendment workflow with its originating finding and human rationale linked; captured prior review/plan/QA inputs remain unchanged.

### Verification

A QA feedback example produces a revised proposal, updates the staged spec consistently, leaves unapproved changes unpublished, and publishes only the accepted amendment. Runtime execution belongs to ticket 33.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 26 to 32 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r09-execute-approved-qa-corrections"></a>

## 33: Execute approved QA corrections

**What to build:** Accept an approved amendment at the QA boundary without editing captured prior inputs. Run its corrections through existing ticket gates inside the current milestone, retain version/evidence lineage, prepare a fresh candidate, and require renewed QA. Later groups remain gated.

**Blocked by:** [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md); [32: Propose a versioned correction plan](issues/32-propose-versioned-qa-corrections.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R09](ticket-proposal.md#r09-execute-approved-qa-corrections).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [corrections and safe continuation](spec.md#corrections-and-safe-continuation); [independent checks and exact revisions](spec.md#independent-checks-and-exact-revisions).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Accept an explicitly approved versioned amendment at the current QA boundary without editing captured prior inputs or executing unapproved corrections.
- [ ] Execute correction tickets through fresh implementation/repair assignments, independent checks, both reviews, and exact feature-candidate gates.
- [ ] Retain plan-version lineage, prior Done history, rejected evidence, and the distinction between QA corrections and bounded in-assignment repairs.
- [ ] Prepare a fresh dev candidate and require renewed human acceptance; old approval cannot accept changed source and later groups remain gated.
- [ ] Demonstrate QA rejection, targeted amendment approval, correction, renewed QA, and continuation through the scripted public seam.

- [ ] Approved correction execution links its originating review finding, human amendment decision, repair/implementation revision and renewed review evidence, without relabeling a finding disposition as candidate acceptance.

### Verification

A scripted QA rejection leads to an approved correction, a new candidate and decision, then continuation. Old approval cannot accept the corrected revision; an unapproved amendment cannot run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 27 to 33 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r10-operate-the-orchestrator-in-the-background"></a>

## 34: Operate the orchestrator in the background

**What to build:** Add normal CLI background launch returning a run identity, observational status/log access, documented stopping controls, and foreground mode. QA waiting survives closing the launching terminal; the separate QA session writes its artifact. Specify active-stage stopping behavior without claiming unsupported restart recovery.

**Blocked by:** [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R10](ticket-proposal.md#r10-operate-the-orchestrator-in-the-background).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [public interface and approval](spec.md#public-interface-and-approval); [corrections and safe continuation](spec.md#corrections-and-safe-continuation).

### Acceptance criteria

- [ ] Provide normal CLI background launch returning a run identity, foreground debugging, observational status/log access, and documented stopping controls.
- [ ] Keep execution and QA waiting independent of the launching terminal; the separate QA session writes the approval artifact.
- [ ] Support clean stop/continuation at QA through ticket 15's contract; document active-stage stop outcomes without claiming arbitrary recovery.
- [ ] Preserve durable process/evidence identity and descendant cleanup; background launch success is distinct from feature completion.
- [ ] Verify launch, logs/status, terminal independence, waiting/approval-driven progress, clean QA stop/restart, and cleanup using offline scripted subprocesses.

### Verification

Scripted subprocess tests observe launch, logs/status, waiting, approval-driven continuation, clean QA stop/restart, and descendant cleanup. Do not require model or network access.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 28 to 34 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r11-continue-independent-work-inside-the-current-milestone"></a>

## 35: Continue independent work inside the current milestone

**What to build:** Retain pre-QA ticket 10's blocked-root/waiting-dependent/unrelated-success behavior and shared-environment stopping. Unrelated work is eligible only within the current milestone; a block or exhausted repair cannot bypass a QA boundary or produce feature success.

**Blocked by:** [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md); [06: Stop for decisions outside approved contracts](issues/06-surface-human-decisions-without-retrying.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R11](ticket-proposal.md#r11-continue-independent-work-inside-the-current-milestone).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [ticket lifecycle](spec.md#ticket-lifecycle); [bounded failures and timeouts](spec.md#bounded-failures-and-timeouts).

### Acceptance criteria

- [ ] Keep human-decision/exhausted-repair tickets Blocked and their dependent tickets Pending without implicit retries.
- [ ] Continue unrelated ready work inside the current milestone from the latest verified feature revision; no ticket from a later milestone starts.
- [ ] Stop when no executable current-milestone work remains and accurately distinguish Done, Blocked, dependency-waiting, and QA-waiting states.
- [ ] Return an incomplete outcome for unresolved required work even if unrelated tickets succeeded; shared environment/integrity failures stop the run.
- [ ] Demonstrate a blocked root, waiting dependent, unrelated success, and later-group ticket that remains unstarted, retaining each ticket's evidence.

### Verification

Reuse the pre-QA ticket 10 fixture requirements, adding later-group work that must remain unstarted. Preserve accurate incomplete and waiting outcomes.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R11; the [previous definition](archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 29 to 35 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r12-supply-coherent-design-guidance-to-standards-review"></a>

## 36: Supply coherent design guidance to Standards review

**What to build:** Retain the design-policy and Standards-role portion of pre-QA ticket 11, auditing current custom guidance and synthesizing Matt/Microsoft principles with Pythonic functions and objects. Deliver the required policy/role context explicitly through the existing assignment seam. Evidence-based blockers remain distinct from optional suggestions.

**Blocked by:** [03: Reject invalid agent reports and review evidence](issues/03-validate-agent-reports-and-review-evidence.md); [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R12](ticket-proposal.md#r12-supply-coherent-design-guidance-to-standards-review).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [custom skills and design policy](spec.md#custom-skills-and-design-policy); [cohesive module responsibilities](spec.md#cohesive-module-responsibilities).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Audit current custom guidance and create one combined design authority with focused references for deep modules, information hiding, cohesive responsibility/invariant ownership, composition, substitutability, justified injection, and behavioral tests.
- [ ] Support Pythonic functions, objects and combinations without mandating speculative patterns or class hierarchies.
- [ ] Create Standards guidance respecting project rules and accepted ADRs; blockers need concrete evidence and consequences, while preferences remain optional.
- [ ] Reuse custom test-strategy review guidance without adding a reviewer or gate, and explicitly supply required design/Standards context through the existing assignment seam.
- [ ] Validate skills and concrete design examples; capture Standards inputs in a separate scripted repository. Generic default/addition capture and source-edit stability are owned by ticket 37.

- [ ] Explicitly deliver the evaluated ownership/cross-module review contract and its scope/coverage declaration through the existing Standards assignment seam. Capture actual scripted delivered instruction identities; cumulative runtime scheduling remains ticket 39.

### Verification

Validate skills, inspect concrete design examples, and capture actual Standards-assignment inputs in a separate scripted target repository. Generic additive skill selection is isolated in ticket 37.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R12; the [previous definition](archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 30 to 36 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r13-capture-and-deliver-selected-local-skills"></a>

## 37: Capture and deliver selected local skills

**What to build:** Retain pre-QA ticket 11's generic role/default/addition contract: explicitly resolve local sources and required references, capture origin/source/content identities, reject missing content, and record actual delivery. Repairs receive captured instructions even after source edits. Keep the planning reference aligned with this canonical metadata.

**Blocked by:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md); [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R13](ticket-proposal.md#r13-capture-and-deliver-selected-local-skills).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [skill selection and delivery](spec.md#skill-selection-and-delivery); [agent contracts and access](spec.md#agent-contracts-and-access).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Document one canonical additive skill-selection/source-resolution contract compatible with the planning reference and tickets without additions.
- [ ] Support explicit local harness, target-repository, and installed-library sources; role-specific ticket additions preserve project defaults and mandatory role/access/output contracts.
- [ ] At run start capture selected skills and required local references with role, selection origin, source identity and content identity; reject missing required content before affected assignments.
- [ ] Deliver captured instructions explicitly and record actual delivered content; repairs use captured content despite later source edits.
- [ ] Demonstrate defaults, role-specific additions, missing references and edits after capture in a separate scripted target repository; preserve upstream files and defer discovery/download/installation.

- [ ] Capture the selected shared review contract and required references under the existing role/default/addition mechanism, retaining source identities and stable delivered content across repairs.

### Verification

Scripted cross-repository assignments exercise defaults, role-specific additions, missing references, and source edits after capture without adding live-model variations.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 31 to 37 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r14-deliver-focused-implementation-and-spec-contexts"></a>

## 38: Deliver focused implementation and Spec contexts

**What to build:** Retain pre-QA ticket 12's distinct implementation/repair/Spec guidance and fresh context assembly. Supply milestone and ticket constraints while keeping reviews, commits, promotions, state changes, and human approval under harness control. Reuse shared design and test strategy without copying the whole upstream library.

**Blocked by:** [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md); [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R14](ticket-proposal.md#r14-deliver-focused-implementation-and-spec-contexts).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Create focused implementation/repair guidance for one ticket's contracts, approved behavioral seams, custom test-strategy coverage selection, TDD where needed, evidence, and out-of-scope decisions.
- [ ] Create separate Spec-review guidance for missing, incorrect and unrequested behavior against approved requirements.
- [ ] Provide every assignment fresh role context, captured defaults/additions and scoped references; repairs use the captured version even after source-library edits.
- [ ] Supply exact reviewed revision, relevant source/diff and actual check outcomes to Spec review, with only relevant design guidance for implementers.
- [ ] Keep nested-review orchestration, commits, integration, QA acceptance, state and completion under harness authority; record actual selection origins/content identities and demonstrate a fresh repair.

- [ ] Implementation/repair and Spec contexts include relevant ownership contracts, prior finding identities/dispositions and exact reviewed source/check evidence, while reviewers remain independently assigned and completed prior reports remain immutable.

### Verification

Captured scripted implementation, repair, and Spec assignments show scoped requirements, exact reviewed revisions, stable selected guidance, and role separation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R14; the [previous definition](archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 32 to 38 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

## 39: Enforce traceable runtime review checkpoints

**What to build:** Carry the evaluated review contract into the runtime as traceable per-ticket and cumulative assessment records. Enforce scoped review completion, findings and architecture checkpoints before affected integration and milestone QA readiness, using scripted processes first so the real-agent ticket consumes an already verified lifecycle.

**Blocked by:** [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md); [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md); [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md); [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md); [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M3. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration); [runtime adoption](spec.md#runtime-review-adoption); [exact revisions](spec.md#independent-checks-and-exact-revisions); [QA](spec.md#feature-to-development-promotion-and-human-qa). Respect [domain terms](../../GLOSSARY.md), [ADR-0001](../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Runtime ticket reviews retain separate fresh Spec/Standards reports and exact revision identities, supplied ownership contracts, prior findings/dispositions and actual inspected/omitted scope. Record review/report identities, instruction/settings identities, finding keys and repair/verification links in additive harness-owned artifacts, with observational status/navigation exposing pending reviews and decisions.
- [ ] Implement the shared milestone-boundary and risk-trigger architecture assessments through an explicitly identified cumulative scope using Standards, rather than silently treating it as an ordinary ticket attempt or adding an unconditional third ticket reviewer. Pin source/cumulative baseline and inventory, preserve separate review history, and reject missing, incomplete or stale assessments before affected integration or QA readiness.
- [ ] Ordinary in-scope ticket blockers follow existing bounded repair policy; a cumulative blocker that cannot be corrected under that policy, a proposed scope/ownership change or consequential risk decision preserves work and stops with an incomplete human-decision handoff, without inventing extra repairs. Resolve it through an explicitly authorized amendment/fresh run with prior evidence linked; a disposition alone cannot resume a stopped run. Such work cannot integrate or obtain a consumable QA request while required blocking review work is unresolved. Optional findings retain inspectable dispositions and do not trigger repairs merely for being optional.
- [ ] Human review decisions remain separate from exact-candidate QA acceptance. Validate the review/scope/revision/finding identity and explicit reason before applying a disposition; agents cannot author their own consequential acceptance. Review completion, findings dispositioned, candidate awaiting QA, milestone promoted and feature complete remain distinct recorded outcomes.
- [ ] Keep immutable reports, append-only disposition history and completed work linked across deliberate stop/continue. Produce required review artifacts before freezing QA evidence; during a frozen QA wait, reject edits or preserve new proposals outside the frozen evidence and require renewed readiness/request as applicable. Preserve legacy report identity/finding fields, checkpoint version 1, gate evidence and artifact names; new review state is additive/optional for old records and never creates legacy review attestations retroactively.
- [ ] Verify through the public CLI with scripted external processes and real isolated Git: clean ticket/cumulative review, missing coverage, stale source, duplicate local finding IDs, fixed/deferred/awaiting-decision histories, blocked readiness/integration, rejected unauthorized dispositions, optional-only progress, failed review invocation and deliberate continuation with preserved records. Extend guide/status contracts and retained evidence, with actual live-agent proof left to ticket 40.

### Verification

Map existing report, human-decision, repair, optional-finding, milestone and continuation scenarios first. Add only distinct new runtime review-history/checkpoint/authority cases at the existing public CLI/scripted-process/real-Git seam. Run the full final-source suite and static gates, plus installed CLI checks where this ticket changes entry points or their observable contract. Genuine old checkpoint compatibility remains required; new review artifacts cannot invalidate a frozen old checkpoint merely by being introduced.

Use the [testing policy](../../docs/agents/testing.md), [Python environment](../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

### Comments

#### Related development-workflow evidence

The completed [workflow-efficiency follow-up](archive/workflow-efficiency/README.md)
retains the preparation, repair-diagnosis and evidence-reuse lessons learned after
ticket 19, including original independent reviews. The current
[development procedure](../../docs/agents/review-records.md#prepare-review-and-repair) is reached
through existing skill/handoff routes. Consult the archive for rationale when
implementing this ticket's approved runtime review contract; the development
guidance is not evidence that runtime enforcement already exists. This context
adds no acceptance criterion or dependency.

### Evidence-policy publication history

Renumbered from ticket 33 to 39 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r15-complete-the-workflow-with-real-codex-roles"></a>

## 40: Complete the workflow with real Codex roles

**What to build:** Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Blocked by:** [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md); [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md); [08: Stop stalled assignments and check processes](issues/08-stop-timed-out-process-trees.md); [39: Enforce traceable runtime review checkpoints](issues/39-enforce-traceable-runtime-review-checkpoints.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R15](ticket-proposal.md#r15-complete-the-workflow-with-real-codex-roles).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](spec.md#codex-execution); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Verify installed Codex invocation and launch fresh implementation/repair/review processes with explicit working directory, sandbox, positive timeout, model, and output contract; do not silently substitute models.
- [ ] Apply Medium implementation/repair and High Spec/Standards defaults with independently configurable role profiles; validate ticket worker overrides and inherit them in repairs without changing reviewers.
- [ ] Capture machine-readable events and schema-validated reports with actual model/reasoning settings and supplied instruction identities.
- [ ] Demonstrate cross-repository delivery of required custom role/design guidance, project defaults and a role-specific addition, without assuming automatic discovery.
- [ ] Complete a tiny actual implementation plus two independent actual reviews and exact candidate integration within the established milestone workflow; keep human QA approval separate from model results.
- [ ] Retain scripted offline routine checks and a separate explicit live check. Record actual evidence or a concrete blocker; a skipped live check is not completion.

- [ ] Use ticket 39's enforced review lifecycle with actual real-agent assignments, including an explicitly scoped cumulative assessment and a declared seeded concern plus acceptable control. Retain actual delivered guidance, inspected scope, findings/dispositions and exact readiness/QA outcomes; scripted success or M1 development evaluation cannot substitute for live runtime proof.

### Verification

Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R15; the [previous definition](archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

#### Related development-workflow evidence

The completed [workflow-efficiency follow-up](archive/workflow-efficiency/README.md)
retains original development-instruction reviews and a finite preparation
exercise. It supplies background for the current
[development procedure](../../docs/agents/review-records.md#prepare-review-and-repair), not live
runtime proof or measured cost savings. This ticket still requires its own actual
role-delivery and runtime evidence under the existing acceptance criteria; no
additional calibration campaign or dependency is introduced by this archive.

### Evidence-policy publication history

Renumbered from ticket 34 to 40 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r16-run-the-early-context-budget-comparison"></a>

## 41: Run the early context-budget comparison

**What to build:** Retain pre-QA ticket 17's 100K/150K/200K/250K controls, fixed workload and reasoning settings, genuine context-pressure case, repetitions, raw measurements, and acceptance checks. Distinguish hard enforcement, compaction thresholds, and advisory targets; active occupancy is separate from cumulative/cached usage.

**Blocked by:** [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** E1 (independent context experiment; not a release gate). Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R16](ticket-proposal.md#r16-run-the-early-context-budget-comparison).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](spec.md#codex-execution); [agent contracts and access](spec.md#agent-contracts-and-access).

### Acceptance criteria

- [ ] Expose 100000, 150000, 200000 and 250000 active-context settings, starting at 250000; verify enforcement, compaction signals or advisory behavior without claiming an unsupported hard cap.
- [ ] Measure peak active context separately from cumulative input/output and cached usage, recording role, attempt, model, reasoning, and configured limit.
- [ ] Use a fixed bounded workload and acceptance suite, consistent settings and documented repetitions at every limit.
- [ ] Include both a short control and a task-relevant pressure case capable of approaching thresholds; below-100K runs cannot establish comparative higher-limit effects.
- [ ] Report verified outcomes, failures, repairs, compactions/handoffs, elapsed time and raw usage evidence; context pressure cannot bypass gates.
- [ ] Publish reproducible findings and limitations without silently changing defaults. Execute immediately after ticket 40 under independent experiment checkpoint E1; do not add release, comprehensive access, background, or completed planning-integration gates.

### Verification

Preserve the current ticket's explicit experiment evidence requirements. Prioritize immediately after ticket 40, before comprehensive boundary probes or release packaging. It remains independent of first-release acceptance dependencies.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R16; the [previous definition](archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 35 to 41 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r17-verify-runtime-write-and-approval-boundaries"></a>

## 42: Verify runtime write and approval boundaries

**What to build:** Retain pre-QA ticket 14's real sandbox probes and add QA decisions, dev, and feature refs to the protected authority checks. Implementers may edit assigned source; reviewers remain read-only; implementation/repair cannot authorize promotion. Do not silently widen permissions or treat a prompt instruction as proof of enforcement.

**Blocked by:** [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md); [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R17](ticket-proposal.md#r17-verify-runtime-write-and-approval-boundaries).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [feature to development promotion and human qa](spec.md#feature-to-development-promotion-and-human-qa).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Verify an implementer can edit only assigned source while reviewers have read-only source sufficient to produce their reports.
- [ ] Probe disposable sentinels for sibling source, approved inputs, authoritative records, QA decisions, and feature/development refs; refuse or detect out-of-scope effects before acceptance.
- [ ] Keep submission capture, both integration destinations, QA decision consumption and execution state under harness authority; implementation/repair cannot authorize acceptance.
- [ ] Reject assignments when required access/instruction guarantees cannot be established; do not silently widen permissions or substitute prompt claims for probes.
- [ ] Record actual backend/sandbox/file/ref observations while preserving caller work and approved inputs.

- [ ] Exercise reviewer read-only source/report/disposition authority and protection of human review decisions separately from QA acceptance, including attempts to rewrite review history or self-accept a consequential risk.

### Verification

Existing disposable sentinel probes plus QA/ref targets provide concrete access evidence without touching caller work. A failed access guarantee leaves verification incomplete.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R17; the [previous definition](archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 36 to 42 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r18-run-a-generated-approved-plan-through-the-runtime"></a>

## 43: Run a generated approved plan through the runtime

**What to build:** Complete the remaining integration portion of pre-QA ticket 15. Produce a small plan through the unified skill, validate it against the now-implemented milestone/skill contracts, and execute it through the scripted public seam. Demonstrate project-default guidance and a role-specific ticket addition, preserving required contracts.

**Blocked by:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md); [33: Execute approved QA corrections](issues/33-execute-approved-qa-corrections.md); [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R18](ticket-proposal.md#r18-run-a-generated-approved-plan-through-the-runtime).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Generate a small human-approved spec/ticket/milestone bundle through the unified planning skill and validate it against the implemented canonical contracts.
- [ ] Demonstrate explicit project defaults and an applicable role-specific ticket addition, plus a ticket requiring no additions, preserving mandatory role guidance.
- [ ] Run the approved example through intentional scripted CLI execution, reaching planned QA and exact local promotion with captured/delivered instruction identities.
- [ ] Keep publishing distinct from execution and QA planning distinct from acceptance; preserve original inputs and evidence.
- [ ] Include interfaces, invariants, testing seams, Pythonic shared design, and appropriate test strategy without replaying all selection validation already covered by ticket 37.

- [ ] Run a generated approved plan carrying ownership/review metadata and required checkpoint scope, verifying backward-compatible tickets without additions and exact linkage of review history to implementation and milestone evidence.

### Verification

A generated example reaches QA and promotion with recorded selection/content identities. Planning publication does not itself launch execution; the example uses an explicit run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Evidence-policy publication history

Renumbered from ticket 37 to 43 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

<a id="r19-demonstrate-the-revised-first-usable-release"></a>

## 44: Demonstrate the revised first usable release

**What to build:** Expand pre-QA ticket 16's clean-checkout acceptance to planning, background operation, two QA milestones, corrections, safe checkpoint continuation, exact local promotions, blocked/waiting work, optional findings, selected guidance, and actual Codex/access evidence. Clearly document deferred concurrency, arbitrary crash recovery, hosted PRs/GitHub checks, and email.

**Blocked by:** [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md); [34: Operate the orchestrator in the background](issues/34-operate-the-harness-in-the-background.md); [35: Continue independent work inside the current milestone](issues/35-continue-independent-work-after-blocks.md); [42: Verify runtime write and approval boundaries](issues/42-verify-role-write-boundaries.md); [43: Run a generated approved plan through the runtime](issues/43-run-a-generated-plan-through-the-runtime.md); [07: Report optional review suggestions without rework](issues/07-report-optional-suggestions-without-repair.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](spec.md), extending oop-v2 / review-process-1.

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R19](ticket-proposal.md#r19-demonstrate-the-revised-first-usable-release).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [testing decisions](spec.md#testing-decisions); [out of scope](spec.md#out-of-scope).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Document installation, actual CLI/background/foreground/status/log/stop/continue interfaces, role settings, limits, requirements, skill selections and artifact/decision inspection.
- [ ] Provide a clean-checkout disposable example covering two milestones, planned QA waits, explicit approval, correction-plan amendment, safe continuation and exact feature-to-dev promotion.
- [ ] Retain repaired/blocked/dependent/unrelated/optional-finding examples and final feature acceptance without bypassing any QA boundary.
- [ ] Run the complete deterministic suite and required static/packaging/installed CLI checks without routine model credentials or network access.
- [ ] Retain actual small Codex/skill/access evidence or report its blocker; show immutable approved inputs and exact candidate-bound branch advancement.
- [ ] Clearly separate sequential operation and planned-QA continuation from deferred concurrency, arbitrary crash recovery, hosted PR/GitHub checks, and email. Context experiment 35 is prioritized separately, not a release gate.

- [ ] The final walkthrough includes navigable review work, immutable reports, a concern-to-human-decision-to-change-to-verification history, cumulative architecture assessment and unresolved-finding visibility across stop/continue; human final acceptance remains separate.

### Verification

Run the existing required complete suite and packaging/installed CLI checks, follow the documented disposable-repository walkthrough, and retain actual live evidence or its explicit blocker. Ticket 41 is scheduled early but is not a prerequisite for release acceptance.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R19; the [previous definition](archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Evidence-policy publication history

Renumbered from ticket 38 to 44 by the [approved amendment](evidence-policy-approval.md). Prior comments describe their original publication; [the numbering map](archive/evidence-policy-numbering-history.md) and original authoring snapshot preserve those identities.

## Completed stable slices

<a id="r01-turn-one-grilling-session-into-an-approved-plan"></a>

[10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md) — completed; original evidence and identities unchanged.

<a id="r02-stop-development-handoffs-at-human-checkpoints"></a>

[11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md) — completed; original evidence and identities unchanged.

<a id="r03-execute-only-the-first-eligible-milestone"></a>

[12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md) — completed; original evidence and identities unchanged.

<a id="r04-present-a-tested-feature-to-dev-candidate"></a>

[13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md) — completed; original evidence and identities unchanged.

<a id="r05-consume-approval-promote-and-continue"></a>

[14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md) — completed; original evidence and identities unchanged.

<a id="r06-continue-after-a-deliberate-qa-stop"></a>

[15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md) — completed; original evidence and identities unchanged.

<a id="comparison-with-the-pre-qa-open-tickets"></a>

Prior decompositions and their comparisons remain in the [original approved proposal](archive/before-evidence-policy-1/ticket-proposal.md).
