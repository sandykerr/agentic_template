> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](source-snapshot.json).

# Reusable ticket-execution harness with milestone QA

**Status:** ready-for-agent

**Plan approval:** The human approved the milestone-QA realignment. This is the canonical current spec; the [implementation plan](ticket-proposal.md) contains its approved decomposition and milestones.

**Implementation status:** Tickets 01–09 are complete under the [previous spec](../spec-before-milestone-qa.md). Their evidence remains valid for that scope. The QA-first remaining definitions are published as 10–28 and gated by the milestone plan; publication does not claim the new QA/background capabilities exist. Start from the [feature index](README.md) for execution status.

## Problem Statement

The developer wants agents to implement approved software changes unattended without relying on a long-lived coordinating conversation. Existing skills provide useful planning, testing, and design practices, but agent-directed scheduling and integration do not provide the deterministic ownership, verification gates, and inspectable outcomes required for this workflow.

The developer also wants reusable repo-owned guidance that incorporates applicable custom skills alongside Matt Pocock's planning, testing, and deep-module practices and Microsoft's OOP guidance. The resulting design policy must support Pythonic combinations of functions and objects, with concrete project decisions taking precedence over general design heuristics.

## Solution

Build a reusable Python command-line harness that executes an approved versioned spec, tickets, and QA milestones in a target Git repository. The first release executes tickets sequentially using fresh Codex processes, independently verifies ticket candidates into a feature branch, and promotes exact tested milestone candidates into the development branch only after human QA acceptance. The eventual CLI normally runs in the background with foreground operation available for debugging.

Completed tickets 01–09 establish the scripted execution, validation, bounded repairs, timeouts, and sequential dependency foundation. Extend that work rather than rebuilding it. The next demonstration uses foreground scripted workers and two milestones in a disposable repository, including approval waiting, stale-approval rejection, tested local promotion, and deliberate continuation from a QA checkpoint. The first usable release adds the unified planning skill, QA-session guidance, approved corrections, background operation, blocked-work isolation, real Codex roles, and access validation.

Concurrency, recovery from arbitrary execution interruptions, hosted PR/GitHub workflow integration, and failure emails are later slices. Deliberate stop and continuation at planned QA checkpoints are in scope.

## User Stories

1. As a developer, I want to start a run from a CLI so that I can approve a bounded body of work and leave it executing.
2. As a developer, I want the same harness to operate on different target repositories using each project's commands and standards.
3. As a developer, I want approved specs and tickets to remain unchanged during execution so that agents cannot quietly redefine success.
4. As a developer, I want the harness to record the approved inputs and starting revision so that I can identify exactly what a run attempted.
5. As a developer, I want invalid tickets and dependency graphs rejected before implementation begins.
6. As a developer, I want a baseline test run so that pre-existing failures are distinguished from failures introduced by agents.
7. As a developer, I want each implementation attempt to start with fresh context and an isolated writable worktree.
8. As a developer, I want workers to receive the applicable custom skills even when the target repository differs from the harness repository.
9. As a developer, I want configurable role profiles defaulting implementation/repair to Medium and both independent reviews to High, with ticket overrides inherited by repairs.
10. As a developer, I want lightweight ticket checks rerun independently of a worker's claims.
11. As a developer, I want a fresh Spec reviewer to assess the submitted revision against the approved requirements.
12. As a developer, I want a separate fresh Standards reviewer to assess that revision against project rules and the combined design policy.
13. As a developer, I want reviewers to identify the consequence and evidence for every blocking finding.
14. As a developer, I want optional suggestions reported without starting extra repair cycles.
15. As a developer, I want candidate merges tested with a more extensive repository suite before the integration branch advances.
16. As a developer, I want completion to refer to the exact tested revision so that an unverified merge cannot be marked done.
17. As a developer, I want concrete code, check, and review failures to trigger bounded automatic repair.
18. As a developer, I want scope ambiguity and changes to approved contracts surfaced for a human decision.
19. As a developer, I want exhausted repairs to preserve the work and block the affected ticket.
20. As a developer, I want unrelated ready tickets to continue when another ticket is blocked.
21. As a developer, I want downstream tickets to wait until their prerequisites are integrated and verified.
22. As a developer, I want timeouts to stop stalled processes and their children.
23. As a developer, I want status and final reports to distinguish completed, blocked, and waiting work.
24. As a developer, I want failures and malformed agent reports to prevent false completion.
25. As a developer, I want planning to establish important interfaces, invariants, and testing seams while leaving internal implementation choices to workers.
26. As a developer, I want design guidance that supports functional, object-oriented, and combined Pythonic approaches without prescribing unnecessary classes.
27. As a developer, I want deterministic tests using scripted agents and real Git repositories so that failure behavior can be tested reliably.
28. As a developer, I want a separate small real-Codex test so that process invocation, skill delivery, and structured reports are actually exercised.
29. As a developer, I want project-default skills by role and ticket-specific additions so that each task receives relevant custom guidance.
30. As a developer, I want selected skills and their required references captured for a run so that later library edits cannot silently change its instructions.
31. As a developer, I want one planning conversation to grill decisions, draft a spec, revise ticket/milestone proposals, and publish the approved coherent bundle.
32. As a developer, I want the spec to evolve with proposal feedback before final approval, with targeted grilling for new consequential decisions.
33. As a developer, I want every plan to include final acceptance QA and proposed earlier capability milestones unless I specify a cadence such as every five tickets.
34. As a developer, I want explicit dependency-consistent milestone membership and concrete QA actions and acceptance conditions.
35. As a developer, I want eligible tickets to integrate into the feature branch while later milestone work waits for human acceptance.
36. As a developer, I want QA to assess a regression-tested feature-to-development candidate whose exact inputs cannot change unnoticed.
37. As a developer, I want a separate QA session to guide testing, record my explicit decision, and propose correction tickets without changing product code.
38. As a developer, I want the orchestrator to watch a precisely identified decision artifact without needing the launching terminal.
39. As a developer, I want indefinite QA waits to remain visible without consuming repair attempts or being reported as failures.
40. As a developer, I want the development branch advanced only to the accepted tested candidate and subsequent work based on that commit.
41. As a developer, I want correction tickets and affected plan changes approved as a new version while earlier snapshots and evidence remain intact.
42. As a developer, I want to start execution in the background and inspect status/logs or stop it through the CLI.
43. As a developer, I want to stop cleanly at planned QA checkpoints and continue after validating the stored identities.
44. As a developer, I want ticket Done, milestone accepted/promoted, and feature complete to be reported distinctly.
45. As a developer, I want the context-budget experiment prioritized immediately after real Codex becomes available without waiting for final release packaging.

## Implementation Decisions

### Public interface and approval

The CLI provides two public operations:

| Operation | Inputs | Observable result |
| --- | --- | --- |
| Start/run | Target repository, feature/development branches, approved versioned plan and ticket selection, configuration, and separate run-output location | Executes eligible work in the background by default and returns a run identity; foreground mode is available. |
| Status/logs | A recorded run | Displays ticket, milestone, feature and process observations, decisions, failures, and artifact locations without starting work or mutating source. |
| Stop | An executing run | Provides documented stopping controls and preserves evidence; clean planned QA checkpoints support continuation. |
| Continue | A deliberately stopped planned QA checkpoint | Validates captured inputs and branch/candidate identities, then resumes the eligible workflow without replaying completed assignments. |

Starting a run intentionally counts as approval of its selected requirements, configured checks, and skill selections. Record the content identities of those inputs, the base commit, and the role/design instructions supplied to agents. An implementation attempt cannot expand that authorization.

Distinguish successful background launch from completed feature execution. A feature succeeds only after all required tickets and milestones pass and the final candidate enters the development branch. Invalid inputs, blocked/incomplete work, environment failure, and an intentional planned QA wait have distinct recorded meanings; waiting alone is not failure. Document command exit semantics for these cases. Status is observational and must not start execution; general interrupted-run recovery remains deferred.

### Requirements, configuration, and run records

Use the configured local issue-tracker conventions: one spec and one Markdown file per ticket, with a title, triage Status, declared dependencies, and acceptance criteria. Give every ticket a stable identifier. A ticket may additionally declare skills for the roles that need them, under the [skill-selection contract](#skill-selection-and-delivery). Normalize the Markdown into one documented input contract; preserve compatibility with the approved authoring conventions and reject conflicting metadata instead of choosing a silent interpretation.

Ticket readiness is separate from dependency satisfaction and execution status. Only approved, agent-ready work is eligible to execute. Validate unique identifiers, existing dependency references, cycles, required acceptance content, check references, and executable configuration before starting workers. Selected work with missing prerequisite completion must not silently run.

Project configuration supplies:

- The target revision, feature branch, development branch, approved plan version, and explicit milestone membership/QA conditions.
- Named lightweight ticket checks and the broader baseline/integration suite.
- Applicable project standards, architecture decisions, and design-policy references.
- Default skill selections by role, with explicit local source references.
- Codex role profiles for implementation, repair, Spec review, and Standards review; profiles may share settings. Defaults are Medium for implementation/repair and High for reviews. Validate ticket worker overrides and apply them to both implementation and repair without altering reviewer profiles.
- Positive stage timeouts and the maximum number of repair attempts, defaulting to two.
- The output location for records and artifacts, separate from approved requirements and agent-editable source.

Store statuses, attempts, observed revisions, check results, review findings, and final outcomes in harness-owned run records. Full prompts, machine-readable process events, final reports, and command output are artifacts; they do not accumulate in a coordinating model's context. Records remain inspectable and include milestone candidates, QA requests/decisions, promotion identities, safe checkpoints, and plan-version lineage. Only continuation from deliberately persisted QA checkpoints is initially supported.

The initial implementation may use simple local files for records. Atomic record writes must avoid reporting a partially written result as successful. Atomic records also support deliberate QA checkpoint continuation. They do not imply recovery from an arbitrary interrupted worker, review, check, or merge.

### Cohesive module responsibilities

Keep the public CLI as the main caller-facing seam. Behind it, use cohesive modules for:

- Requirements and configuration validation.
- Ticket lifecycle and readiness decisions.
- Agent-process invocation and report validation.
- Git worktree preparation and candidate integration.
- Check execution and artifact recording.

These are responsibilities, not a requirement for one class, interface, or source file per item. Group what changes together; create internal seams only where actual variation or external dependencies justify them. Use functions and classes together where that is the simpler Python design.

### Ticket lifecycle

The harness is the sole authority over execution state:

| State | Meaning |
| --- | --- |
| Pending | Waiting for verified prerequisite completion. |
| Ready | Eligible for the next implementation attempt. |
| Running | An initial or repair implementation attempt is active. |
| Verifying | The submission is being checked, reviewed, or tested as a candidate merge. |
| Done | All required ticket evidence passed and the feature branch contains the verified ticket candidate. This does not imply milestone acceptance or feature completion. |
| Blocked | Human input is required or the bounded failure policy has been exhausted. |

A repair transitions the ticket back into implementation with a new attempt identity. A blocking review finding normally triggers repair; it does not itself imply the Blocked state. A dependent ticket remains Pending when its prerequisite is Blocked.

The normal cycle is baseline verification, fresh implementation, independent lightweight checks, fresh Spec and Standards reviews, candidate merge, extensive integration checks, integration-branch advancement, and Done. Dependencies unlock only after Done.

Run one ticket at a time within the current milestone. Choose ready tickets using a documented stable ordering and continue unrelated eligible work after a ticket becomes Blocked; blocked dependencies and later milestones remain waiting. Do not cross a QA boundary. When no executable work remains, distinguish completed, blocked, waiting-for-dependency, and awaiting-human-QA outcomes accurately.

### Independent checks and exact revisions

Run the broader suite on the starting integration revision before ticket work. A failed baseline stops the run as a pre-existing/environment problem and does not consume ticket repair attempts.

After a worker submits, the harness derives the changed files and submitted revision from Git rather than trusting report claims. The harness owns the capture of the submitted changes into a ticket commit. Preserve approved input contents and leave the caller's existing work outside harness-owned worktrees untouched.

Run lightweight checks against that revision before the reviewers assess it. Reviews identify the exact revision and base they assessed. Prepare a candidate merge and run the more extensive suite against that candidate. Advance the integration branch to the exact tested candidate only if the expected previous integration revision is still current.

A failed check, rejected review, failed merge, or failed candidate suite cannot advance the integration branch or mark the ticket Done. If the integration branch changes externally during verification, preserve the evidence and stop the affected operation instead of overwriting that change.

Changed source invalidates earlier check/review approvals. A repaired submission repeats the applicable verification cycle. Any resolution that changes the code after review must return through review.

### Planning and milestone contract

One user-facing custom workflow reuses grilling, domain modeling, to-spec, and to-tickets principles. It settles milestone/QA decisions during grilling, confirms shared understanding, drafts or updates the spec, presents ticket/milestone proposals, revises both from feedback, and publishes only the approved coherent bundle. Substantive new decisions reopen targeted grilling. Leave upstream skills unchanged; reuse shared custom policy and augmented templates rather than adding separate user commands for the internal stages.

Every approved plan has a final milestone covering all required work and overall acceptance. Propose earlier meaningful capabilities by default. Honor an explicit every-N-ticket cadence through fixed, dependency-consistent groups, including any smaller final group. Record stable milestone IDs, ticket membership, testing instructions, and observable acceptance conditions. Validate missing/duplicate membership, missing final coverage, invalid dependencies across groups, and contradictory settings before execution.

### Feature-to-development promotion and human QA

After the current milestone's required tickets are Done on the feature branch, hold later tickets. Prepare a candidate combining that feature revision with the current development branch and run its configured broader regression gates locally. Only a passing candidate can be presented for QA.

Write a QA request identifying the run, approved plan version, milestone, feature revision, development base, candidate revision, evidence, and planned human checks. Keep the candidate stable during assessment. A separate QA skill guides the human, inspects results, records findings, and proposes correction tickets; it cannot self-approve, implement changes, or advance branches.

The background orchestrator watches a human/QA-session-written decision artifact outside approved requirements and implementation worktrees. Require an explicit field such as Decision: APPROVED and matching request identities, not substring search. Missing, malformed, stale, mismatched, and replayed approvals cannot promote or unlock subsequent work. Record the actual decision consumed. Implementation/repair workers cannot authorize this artifact.

QA acceptance authorizes expected-old-checked advancement of development to the exact tested candidate and alignment of the feature branch to that commit before the next milestone. Do not overwrite concurrent branch movement. Changed feature or development inputs require a fresh candidate, renewed checks, and renewed human acceptance. Code changes during conflict resolution additionally renew affected reviews.

QA waits are indefinite and observable, without repair-budget consumption or failure classification. Distinguish ticket Done, milestone accepted/promoted, and feature complete. All tickets Done while awaiting final QA is not feature completion.

### Corrections and safe continuation

When QA requests corrections, propose focused tickets and affected spec/milestone changes. Obtain approval of those changes as a new plan version without reapproving unchanged requirements. Preserve old snapshots, evidence, completed-ticket history, and decision lineage; do not mutate an active version's approved inputs. Execute approved corrections through the existing gates, prepare a new candidate, and repeat QA before admitting later work.

Persist a deliberate safe QA checkpoint that can be stopped cleanly and continued later. Validate approved identities, branch/candidate state, and relevant recorded evidence before continuation. Prevent duplicate active ownership and repeated promotion/approval consumption for one run. Do not rerun completed assignments merely because the orchestrator restarts at this checkpoint. An arbitrary interruption during execution remains outside this initial continuation promise.

Provide CLI background launch, run identity, observational status/logs, stopping controls, and a foreground mode. Document lifecycle and exit semantics using implemented interfaces; routine background tests remain scripted and offline. Planned QA waiting is separate from worker/check timeouts.

### Agent contracts and access

Use the [agent context policy](README.md#agent-context-policy): target 250K active tokens per fresh assignment, with headroom for checks and the handoff. The independent early experiment compares 100K, 150K, 200K, and 250K settings as soon as the real backend is available; distinguish enforced limits, compaction thresholds, and advisory targets from cumulative/cached usage.

Every implementation, repair, and review assignment uses a fresh process/session without inherited development conversation history. Supply the approved ticket, relevant spec, repository instructions, applicable policy, required checks, and role-specific output contract.

Implementation workers write only within their assigned source worktree. Reviewers have read-only source access and inspect the relevant code, requirements, standards, diff, and actual check outcomes. The harness owns Git integration, execution-state updates, and report storage. Role access must be exercised in the disposable fixture rather than inferred from instructions alone.

The implementation report includes the ticket and attempt identity, a result of implementation submitted or human decision needed, a summary, claimed changed files/checks, acceptance evidence, and unresolved questions. It cannot declare the ticket Done. Git and harness-run checks independently establish the revision and verification evidence.

Each review report includes its axis, ticket/attempt/revision identity, and findings. A finding includes:

- A stable identifier within the review and classification as blocking or optional.
- The relevant code location, or the missing behavior's closest applicable location.
- The requirement, project rule, or concrete design risk involved.
- The consequence and supporting evidence.
- A proportionate suggested resolution and whether a human decision is needed.

Reject missing, malformed, mismatched, or incomplete reports. A zero process exit code does not substitute for a valid report, and an empty findings list is meaningful only in a complete review for the correct revision.

### Custom skills and design policy

Maintain repo-owned skills with distinct responsibilities for planning, implementation, Spec review, Standards review, and shared code design. Audit existing custom skills for reusable guidance before creating new role instructions. Their exact packaging can remain small; the combined policy has one authoritative source with focused references.

Planning records important interfaces, invariants, and testing seams with the human, then produces independently verifiable tickets and their dependency graph. Implementation follows those contracts while choosing its internals. Standards review receives the applicable policy explicitly; workers receive the policy and references relevant to their assignment.

Synthesize the upstream guidance around:

- Deep modules with small, useful interfaces and hidden implementation decisions.
- Cohesive responsibilities and localized changes.
- Explicit ownership and enforcement of invariants.
- Composition and behavioral substitutability where interchangeable implementations exist.
- Injected external dependencies where they provide actual testability or variation.
- Behavioral tests through agreed interfaces.
- Functions, objects, and combinations appropriate to the problem and Python.
- Evidence for abstractions and design criticisms; speculative layers and pattern preferences do not become requirements by themselves.

Project requirements, standards, and accepted architecture decisions govern the target project. General policy is a default design lens. A reviewer must connect a blocking concern to behavior, an agreed rule, or a concrete maintenance problem. Optional suggestions are reported without delaying integration.

Keep Matt's and Microsoft's upstream skills as references. Incorporate useful changes deliberately instead of maintaining duplicate competing assessments.

Use this initial role mapping, with focused references to the applicable guidance:

| Role | Initial guidance |
| --- | --- |
| Planning | The unified grilling/spec/proposal/publication workflow, using [Grilling](../../../../.agents/skills/matt-pocock/grilling/SKILL.md), [domain modeling](../../../../.agents/skills/matt-pocock/domain-modeling/SKILL.md), the shared design policy, and custom test strategy to establish contracts and produce independently verifiable tickets with the human. |
| Implementation and repair | Approved contracts, applicable shared design constraints, custom test strategy, and [TDD](../../../../.agents/skills/matt-pocock/tdd/SKILL.md) when behavior needs new coverage. |
| Spec review | Required behavior, scope, acceptance evidence, and regression protection. |
| Standards review | The combined Matt Pocock/Microsoft design policy and the custom test-strategy review guidance. |

Reuse [test-strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) for coverage and verification decisions. The [development implementation wrapper](../../../../.agents/skills/custom/implement-with-checkboxes/SKILL.md) and [next-agent handoff](../../../../.agents/skills/custom/create-next-agent-prompt/SKILL.md) contain useful practices, but their commit, nested-review orchestration, completion-bookkeeping, and handoff responsibilities belong to the development workflow or harness. Expose applicable shared guidance through focused references or shared resources rather than assigning those workflows wholesale to runtime workers. Harness-owned verification gates, role access, integration, and execution records remain authoritative.

### Skill selection and delivery

Each assignment receives its required role instructions and project-default skills, supplemented by any ticket-specific skills for that role. Ticket additions preserve defaults and required role/output/access contracts. Planning follows these selection conventions when producing approved inputs; this does not introduce an autonomous planning stage into a run.

Select skills explicitly from local sources: the harness library, the target repository, or an already installed skills library. Project configuration declares role defaults; optional ticket metadata declares additions and their applicable roles. Document one canonical format and source-resolution convention. An unlisted installed skill does not become part of a run merely because it is available. Automatic discovery, downloading, and installation are outside this release.

At run start, resolve and capture the selected skill content and its required local references in harness-owned artifacts. Record each selection's role, whether it came from required guidance, a project default, or a ticket addition, its source identity, and its content identity. Validate that selected skills and required references are available before affected work starts; missing required content is an input error, not permission to omit guidance.

Use the captured content for every applicable implementation, repair, and review assignment. Later edits to source skills or references do not change an active run's instructions. Preserve the approved selection and captured inputs, and record the content actually delivered to each assignment. Changing the selection requires a newly approved run. Failure to deliver captured required instructions during an assignment remains a failed assignment under the bounded failure policy.

Selected guidance operates within target-project requirements, standards, accepted architecture decisions, and harness role contracts. Incompatible guidance that requires changing those contracts is a human decision rather than an expansion of worker authority.

### Codex execution

Use the installed Codex CLI as the first backend. Capture machine-readable events and schema-validated final reports. Build process arguments directly and supply the intended working directory, role settings, sandbox, timeout, and prompt as explicit inputs.

Do not assume custom skills in the harness repository are automatically discovered in another target repository. The implementation must explicitly deliver the applicable role/design instructions and necessary references, record what was delivered, and demonstrate their availability in the real-Codex fixture. Failure to deliver required instructions is a failed assignment.

The scripted external-agent test process and the real Codex process satisfy the same observable assignment/report contract. Additional model providers are outside this release.

### Bounded failures and timeouts

Allow an initial implementation plus at most two repair attempts by default. A worker's own edit/test iterations within its assignment do not each consume a repair attempt.

When checks or reviews reject submitted work, give a fresh repair worker the current changes and concrete failure evidence. Unavailable requirements or changes to approved contracts require a human decision immediately. Preserve the attempt history and rejected revisions.

Missing reports, invalid reports, nonzero agent exits, and stage timeouts must have bounded outcomes and never be converted into success. A local assignment failure either enters the remaining repair allowance or blocks its ticket; it cannot gain an unlimited separate retry loop. A failed shared baseline or unavailable shared execution environment stops the run with an environment outcome.

Every worker, reviewer, and check command has a positive configured timeout. On timeout, terminate the affected process and its descendants, collect available output, and record the failed stage. After exhausted repairs, preserve the work, mark the ticket Blocked, leave its dependents waiting, and continue unrelated ready tickets.

## Testing Decisions

Use the agreed public CLI seam and observable Git/report outcomes. Drive real temporary Git repositories through the complete cycle, using a scripted external-agent process for deterministic outcomes. Assert behavior and invariants rather than private helpers, internal call order, or the implementation's class structure.

The process dependency is the justified external seam: scripted and real Codex executions provide two concrete implementations. Routine tests require neither model access nor network access. Run a separate small real-Codex test explicitly to validate actual invocation, skill delivery, role access, and reports.

Acceptance scenarios include:

- A passing ticket traverses every required gate and the integration branch advances to the tested candidate.
- Lightweight checks fail, a review blocks, or the candidate suite fails: no failed candidate is integrated.
- One repair resolves a demonstrated issue; exhausted repairs block the ticket and preserve evidence.
- Optional review suggestions appear in the report without triggering repairs.
- Malformed reports, absent commits, incorrect revision identities, nonzero exits, and timeouts cannot produce Done.
- Timed-out processes and their children are stopped; failure output remains inspectable.
- Invalid tickets, cycles, missing prerequisites, and invalid check configuration are rejected.
- A failed starting baseline is reported without consuming ticket repairs.
- Dependency ordering is respected; blocked prerequisites leave dependents waiting while unrelated work completes.
- Approved inputs, reviewer source trees, and unrelated caller work remain unchanged.
- Different role profiles and project commands reach the intended assignments and stages.
- A repair's changed revision requires renewed checks and both reviews.
- An externally changed integration branch is not overwritten.
- Status accurately exposes recorded results without starting execution.
- The real-Codex fixture receives the required custom role/design guidance in a different target repository.
- Project-default skills and a ticket-specific addition reach only the applicable roles while required role contracts remain present.
- Missing selected skills or required references are reported before affected work starts.
- Edits to source skills or required references after run capture leave assignment content unchanged; artifacts identify the captured and actually delivered content, including repairs.

Tickets 01–09 already establish a verified implementation and regression suite; preserve their [completion evidence](README.md#completion-evidence). Extend the existing public CLI/process/Git/report seam rather than rebuilding the foundation. Add two-milestone foreground tests for approval waiting, rejection of stale/malformed/replayed decisions, exact feature-to-development promotion, externally moved development, source-changing conflict resolution, safe checkpoint continuation, approved corrections, and feature-versus-ticket completion. Validate planning/QA/development skills and handoff eligibility separately; test background lifecycle without live model calls. Exercise the real backend explicitly and keep the context-limit comparison immediately after its availability.

## Out of Scope

- Concurrent ticket execution.
- Recovery from arbitrary interrupted execution or automatic crash recovery; deliberate continuation at planned QA checkpoints is in scope.
- Hosted PR creation/approval and required GitHub workflow integration; initial milestone regressions execute locally.
- Automated failure emails and notification-provider setup.
- Additional agent backends, issue-tracker connectors, dashboards, and automatic model-selection algorithms.
- Automatic changes to approved scope, interfaces, requirements, or project standards.
- Publishing, pushing, production deployment, or external side effects beyond the approved project checks.
- A general actor framework, plugin framework, or class hierarchy without a present requirement.
- Automatic skill discovery, downloading, or installation during ticket execution.

## Further Notes

The [domain glossary](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md), and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md) supply vocabulary and architectural rationale. This spec is the requirements authority; the former design summary now points here.

The [approved implementation plan](ticket-proposal.md) records the skill/ticket/milestone mapping. Reconcile issue files against it while preserving existing IDs and completed evidence. This bundle's approval does not start execution or authorize external publishing. Runtime schemas, exact CLI names, file encoding, and polling details are implementation choices to document and verify.

Numeric timeout defaults, physical record encoding, internal source layout, and the installed CLI's exact invocation details are implementation choices to document and verify against the fixture. They must preserve the observable contracts above.
