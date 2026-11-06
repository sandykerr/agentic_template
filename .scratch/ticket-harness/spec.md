# Reusable ticket-execution harness: first working version

**Status:** ready-for-agent

## Problem Statement

The developer wants agents to implement approved software changes unattended without relying on a long-lived coordinating conversation. Existing skills provide useful planning, testing, and design practices, but agent-directed scheduling and integration do not provide the deterministic ownership, verification gates, and inspectable outcomes required for this workflow.

The developer also wants reusable repo-owned guidance that incorporates applicable custom skills alongside Matt Pocock's planning, testing, and deep-module practices and Microsoft's OOP guidance. The resulting design policy must support Pythonic combinations of functions and objects, with concrete project decisions taking precedence over general design heuristics.

## Solution

Build a reusable Python command-line harness that operates on a target Git repository using approved local Markdown specs and tickets. The first version executes tickets sequentially, launches fresh Codex implementation and review processes, independently verifies submitted changes, tests a candidate merge, and advances a local integration branch only after all required gates pass.

The first tracer bullet demonstrates one complete ticket cycle in a disposable repository using scripted agent responses. Subsequent implementation tickets extend that same cycle with bounded repairs, timeouts, dependency scheduling, real Codex execution, and custom skills. The first usable release includes all those behaviors; a scripted tracer bullet alone is not completion of this spec.

Concurrency, interrupted-run recovery, and failure emails are later slices.

## User Stories

1. As a developer, I want to start a run from a CLI so that I can approve a bounded body of work and leave it executing.
2. As a developer, I want the same harness to operate on different target repositories using each project's commands and standards.
3. As a developer, I want approved specs and tickets to remain unchanged during execution so that agents cannot quietly redefine success.
4. As a developer, I want the harness to record the approved inputs and starting revision so that I can identify exactly what a run attempted.
5. As a developer, I want invalid tickets and dependency graphs rejected before implementation begins.
6. As a developer, I want a baseline test run so that pre-existing failures are distinguished from failures introduced by agents.
7. As a developer, I want each implementation attempt to start with fresh context and an isolated writable worktree.
8. As a developer, I want workers to receive the applicable custom skills even when the target repository differs from the harness repository.
9. As a developer, I want model and reasoning settings configurable by role.
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

## Implementation Decisions

### Public interface and approval

The CLI provides two public operations:

| Operation | Inputs | Observable result |
| --- | --- | --- |
| Run | Target repository, base/integration branch, approved spec and ticket selection, project configuration, and a separate run-output location | Executes the selected work, records artifacts and outcomes, and returns success only when all selected tickets are done. |
| Status | A recorded run | Displays its recorded progress, ticket outcomes, attempts, failures, and artifact locations without launching agents or changing the target repository. |

Starting a run intentionally counts as approval of its selected requirements, configured checks, and skill selections. Record the content identities of those inputs, the base commit, and the role/design instructions supplied to agents. An implementation attempt cannot expand that authorization.

Run returns a nonzero result for incomplete work, invalid inputs, or an execution-environment failure. The report distinguishes these outcomes. Status reports recorded observations; it does not promise live process discovery or interrupted-run recovery.

### Requirements, configuration, and run records

Use the configured local issue-tracker conventions: one spec and one Markdown file per ticket, with a title, triage Status, declared dependencies, and acceptance criteria. Give every ticket a stable identifier. A ticket may additionally declare skills for the roles that need them, under the [skill-selection contract](#skill-selection-and-delivery). Normalize the Markdown into one documented input contract; preserve compatibility with the approved authoring conventions and reject conflicting metadata instead of choosing a silent interpretation.

Ticket readiness is separate from dependency satisfaction and execution status. Only approved, agent-ready work is eligible to execute. Validate unique identifiers, existing dependency references, cycles, required acceptance content, check references, and executable configuration before starting workers. Selected work with missing prerequisite completion must not silently run.

Project configuration supplies:

- The target code revision and integration destination.
- Named lightweight ticket checks and the broader baseline/integration suite.
- Applicable project standards, architecture decisions, and design-policy references.
- Default skill selections by role, with explicit local source references.
- Codex role profiles for implementation, repair, Spec review, and Standards review; profiles may share settings.
- Positive stage timeouts and the maximum number of repair attempts, defaulting to two.
- The output location for records and artifacts, separate from approved requirements and agent-editable source.

Store statuses, attempts, observed revisions, check results, review findings, and final outcomes in harness-owned run records. Full prompts, machine-readable process events, final reports, and command output are artifacts; they do not accumulate in a coordinating model's context. Records remain inspectable even though resuming execution is deferred.

The initial implementation may use simple local files for records. Atomic record writes must avoid reporting a partially written result as successful. This is diagnostic durability, not a promise of crash recovery.

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
| Done | All required evidence passed and the integration branch references the verified candidate. |
| Blocked | Human input is required or the bounded failure policy has been exhausted. |

A repair transitions the ticket back into implementation with a new attempt identity. A blocking review finding normally triggers repair; it does not itself imply the Blocked state. A dependent ticket remains Pending when its prerequisite is Blocked.

The normal cycle is baseline verification, fresh implementation, independent lightweight checks, fresh Spec and Standards reviews, candidate merge, extensive integration checks, integration-branch advancement, and Done. Dependencies unlock only after Done.

Run one ticket at a time. Choose ready tickets using a documented stable ordering, and continue unrelated ready work after a ticket becomes Blocked. When no executable work remains, report the completed, blocked, and waiting tickets accurately.

### Independent checks and exact revisions

Run the broader suite on the starting integration revision before ticket work. A failed baseline stops the run as a pre-existing/environment problem and does not consume ticket repair attempts.

After a worker submits, the harness derives the changed files and submitted revision from Git rather than trusting report claims. The harness owns the capture of the submitted changes into a ticket commit. Preserve approved input contents and leave the caller's existing work outside harness-owned worktrees untouched.

Run lightweight checks against that revision before the reviewers assess it. Reviews identify the exact revision and base they assessed. Prepare a candidate merge and run the more extensive suite against that candidate. Advance the integration branch to the exact tested candidate only if the expected previous integration revision is still current.

A failed check, rejected review, failed merge, or failed candidate suite cannot advance the integration branch or mark the ticket Done. If the integration branch changes externally during verification, preserve the evidence and stop the affected operation instead of overwriting that change.

Changed source invalidates earlier check/review approvals. A repaired submission repeats the applicable verification cycle. Any resolution that changes the code after review must return through review.

### Agent contracts and access

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
| Planning | [Grilling](../../.agents/skills/matt-pocock/grilling/SKILL.md), [domain modeling](../../.agents/skills/matt-pocock/domain-modeling/SKILL.md), the shared design policy, and custom test strategy to establish contracts and produce independently verifiable tickets with the human. |
| Implementation and repair | Approved contracts, applicable shared design constraints, custom test strategy, and [TDD](../../.agents/skills/matt-pocock/tdd/SKILL.md) when behavior needs new coverage. |
| Spec review | Required behavior, scope, acceptance evidence, and regression protection. |
| Standards review | The combined Matt Pocock/Microsoft design policy and the custom test-strategy review guidance. |

Reuse [test-strategy](../../.agents/skills/custom/test-strategy/SKILL.md) for coverage and verification decisions. The [development implementation wrapper](../../.agents/skills/custom/implement-with-checkboxes/SKILL.md) and [next-agent handoff](../../.agents/skills/custom/create-next-agent-prompt/SKILL.md) contain useful practices, but their commit, nested-review orchestration, completion-bookkeeping, and handoff responsibilities belong to the development workflow or harness. Expose applicable shared guidance through focused references or shared resources rather than assigning those workflows wholesale to runtime workers. Harness-owned verification gates, role access, integration, and execution records remain authoritative.

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

This repository currently has no Python harness implementation or test suite to extend. Establish a reproducible Python project/check setup as part of the first tracer bullet, and keep the fixture small.

## Out of Scope

- Concurrent ticket execution.
- Resuming interrupted runs or automatic crash recovery.
- Automated failure emails and notification-provider setup.
- Additional agent backends, issue-tracker connectors, dashboards, and automatic model-selection algorithms.
- Automatic changes to approved scope, interfaces, requirements, or project standards.
- Publishing, pushing, production deployment, or external side effects beyond the approved project checks.
- A general actor framework, plugin framework, or class hierarchy without a present requirement.
- Automatic skill discovery, downloading, or installation during ticket execution.

## Further Notes

The confirmed [design decisions](../../docs/harness-design.md), [domain glossary](../../GLOSSARY.md), and [ADR-0001](../../docs/adr/0001-reusable-harness-and-local-integration.md) supply the context and vocabulary.

The implementation ticket breakdown is proposed separately for human review. Ticket publication does not start harness execution or authorize publishing changes externally.

Numeric timeout defaults, physical record encoding, internal source layout, and the installed CLI's exact invocation details are implementation choices to document and verify against the fixture. They must preserve the observable contracts above.
