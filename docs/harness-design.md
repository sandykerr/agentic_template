# Harness design decisions

The design decisions below were confirmed by the human after the grilling session. The [implementation spec](../.scratch/ticket-harness/spec.md) captures the resulting contracts. The [implementation ticket breakdown](../.scratch/ticket-harness/ticket-proposal.md) is proposed for human review before the individual issues are published.

## First milestone

Deliver a vertical slice through one complete ticket cycle: read the ticket, launch a fresh implementation worker, independently check its changes, obtain independent Spec and Standards reviews, prepare a candidate merge, run broader integration checks, advance the local integration branch, and record completion. Completion requires passing the applicable gates.

The harness is implemented in Python. Its first interface is a command-line tool for starting work and inspecting ticket progress, results, and failure details.

The first usable version processes one ticket at a time, honoring dependencies and continuing with unrelated ready tickets when another is blocked. Later slices target concurrent ticket execution.

Resuming interrupted runs and crash recovery are deferred to a later slice. The first milestone does not promise that an interrupted run can be resumed.

## Verification authority

The harness independently runs checks defined by the target repository and approved ticket. Worker reports alone are insufficient evidence of success. Spec and Standards reviewers assess the submitted version of the code; repairs require renewed verification.

Run the broader repository suite once before starting ticket work to establish the baseline. Report pre-existing failures separately so workers do not spend repair attempts on them. Per-ticket checks before review should be lighter weight. After preparing the candidate merge, run the more extensive repository-level integration suite before advancing the integration branch. The target repository supplies the actual check commands.

The candidate merge must pass integration checks before the integration branch advances. A failed candidate goes through repair while the integration branch stays at its last verified commit.

## Reuse and authority

The harness and shared role skills are maintained in this repository and can operate on other target repositories. Each target repository supplies its commands, standards, and constraints.

After a human approves a spec and its tickets, the harness may implement tickets, run checks, request bounded repairs, and integrate passing changes locally. Publishing remains separate. Missing requirements, incompatible architectural choices, and exhausted repair attempts stop the affected ticket and surface a human decision.

Intentionally starting the CLI run counts as approval of the selected spec, tickets, and configured checks. Record those approved inputs; no additional per-ticket confirmation is required within that scope.

See [ADR-0001](adr/0001-reusable-harness-and-local-integration.md) for the architectural decision and rationale.

## Design review policy

Combined design guidance from Matt Pocock's skills and the Microsoft OOP skill applies by default. Explicit project rules are enforceable; general principles require judgment and evidence.

Each ticket receives separate fresh Spec and Standards reviews. Spec review assesses the implementation against approved requirements. Standards review assesses project standards and the combined design guidance.

The intended result is a unified custom skill or set of skills for good OOP and code design, synthesizing the useful guidance from both upstream libraries. Its exact organization remains open; it should provide coherent guidance rather than require separate Matt-specific and Microsoft-specific design assessments.

Reviewers must explain why a design concern should block completion, connecting it to behavior, an agreed architectural rule, or a concrete maintenance problem. A preference for a different pattern alone is an optional suggestion. The implementation spec will define the structured finding fields.

Blocking review findings trigger automatic repair and prevent integration until resolved. Optional suggestions are collected in the final report without delaying integration or starting repair attempts. A blocking finding does not immediately put a ticket into the blocked state: the normal repair process runs first unless the finding requires a human decision.

## Design ownership and Python style

Planning establishes the important module interfaces, invariants, and testing seams with the human. Workers choose the internal implementation while preserving those approved contracts. Changes to those contracts require a human decision.

The combined code-design guidance supports functional and object-oriented code, including combinations where applicable and Pythonic. Choose the simplest structure that keeps responsibilities and rules clear. A cohesive module owns lifecycle rules; its internal implementation may use functions, classes, or both. No particular pattern or class hierarchy is required merely to satisfy an OOP preference.

## Inputs and skill ownership

The first version reads specs and tickets from local Markdown files. Ticket metadata provides structured IDs, dependencies, and acceptance requirements.

Custom harness skills live in their own directory and reference one shared design-policy document. Matt Pocock's and Microsoft's installed skills remain upstream references; useful upstream changes are incorporated deliberately. Workers receive ticket-specific constraints, and reviewers receive the applicable broader policy.

Approved specs and tickets remain unchanged during execution. The harness owns separate run records containing statuses, attempts, commits, check outcomes, and review findings. Workers report outcomes rather than modifying execution state. Changes to approved requirements require a human decision.

## Agent backend

The first version uses the installed Codex CLI. Model and reasoning settings are configurable separately for implementation and review. Reliable delivery of the custom skills to workers in a different target repository must be validated in the disposable repository experiment.

Implementation workers receive isolated writable worktrees. Reviewers receive read-only source access. The harness alone updates execution state and integrates changes. This ownership and isolation model also supports later concurrent execution.

## First validation target

Prove the first cycle against a small, disposable Git repository with controlled success and failure cases. A passing ticket must integrate successfully, a failed check must prevent completion, and a blocking review finding must trigger repair or a blocked outcome.

Routine harness tests use scripted agent responses against real temporary Git repositories. A separate small test uses actual Codex workers to validate execution, custom-skill delivery, and structured reports together.

## Repair policy

Each ticket initially allows two repair attempts after its first implementation submission; the limit is configurable. Development iterations within a worker assignment do not each count as a repair attempt.

Exhausting repairs preserves the ticket's changes and marks the ticket blocked. Its dependent tickets remain waiting, while unrelated ready tickets may continue. The run reports unresolved tickets at the end. A failure affecting the entire execution environment stops the run.

Each worker, reviewer, and check command has a configurable timeout. On timeout, stop the affected process and its children, preserve available evidence, and apply the bounded failure policy. Broader integration suites can have longer limits than lightweight ticket checks.

## Future failure notifications

A long-term goal is automated email notification when the harness fails. Notification triggers, timing, recipients, and delivery mechanism remain undecided. Email delivery is outside the first vertical slice.

