# From Matt Pocock’s AI Workflow to a Custom Codex Harness

Conversation summary and implementation roadmap\
Focus: Skills, context rot, subagents, Markdown tickets, and autonomous implementation\
Prepared: November 5, 2026

> Scope: This document summarizes the Matt Pocock workshop transcript and our subsequent discussion. Recommendations about your Codex setup and the proposed harness are adaptations, not claims that Pocock prescribes every detail. Skill names, Codex commands, model availability, and configuration keys can change; check the versions installed in your environment before automating them.

## Executive summary

The most useful idea from Pocock's workshop is turning ambiguous software work into small, independently verifiable changes while keeping the developer responsible for the design of the system.

His broad workflow is:

```
Idea / request
    ↓
Grill / align (human involved)
    ↓
Specification / PRD = destination
    ↓
Dependency-aware tickets = journey
    ↓
Fresh coding agents (potentially parallel)
    ↓
Automated tests + independent review
    ↓
Human QA → follow-up tickets → integration
```

Our proposed evolution of that workflow is to use Pocock's skills inside coding agents, while eventually moving scheduling, state, retries, isolation, and acceptance gates into a programmatic harness. A harness should not need an LLM to decide whether a ticket is unblocked, a test succeeded, or a retry limit has been reached.

The target architecture: Markdown as durable requirements and task state; Git as the record of changes; tests as executable acceptance criteria; fresh-context subagents as disposable workers; and a small deterministic orchestrator controlling the lifecycle.

## 1. Pocock's central principles

### 1.1 AI development is still software engineering

Pocock argues against treating a specification as code that an agent merely compiles. Developers still need to understand and deliberately shape the codebase. Established practices—small tasks, tracer bullets, modular design, TDD, integration tests, and code review—become more important when code is produced quickly.

The human's responsibilities shift toward:

- Resolving ambiguous requirements and making product/architecture decisions.
- Selecting useful boundaries between modules.
- Designing interfaces, invariants, and acceptance criteria.
- Ensuring tests give realistic feedback.
- Reviewing behavior and maintaining quality standards.

The agent may implement much of the code behind those decisions, but automation cannot turn unclear goals into trustworthy software by itself.

### 1.2 Separate the “day shift” from the “night shift”

Pocock distinguishes two classes of work:

| Human-in-the-loop (“day shift”)      | Potentially AFK (“night shift”)                  |
| ------------------------------------ | ------------------------------------------------ |
| Discussing the actual goal           | Implementing a bounded ticket                    |
| Answering the grill questions        | Writing/running tests                            |
| Deciding scope and architecture      | Making local implementation choices              |
| Reviewing ticket decomposition       | Running static checks                            |
| Evaluating UX or scientific validity | Preparing commits and review artifacts           |
| Performing meaningful QA             | Automatically checking against explicit criteria |

The boundary is conditional, not absolute. An implementation can run unattended only if its requirements and verification methods are sufficiently specific. Ambiguous or consequential decisions should transition a ticket to `blocked` rather than trigger endless agent improvisation.

### 1.3 Align before generating plans

The workshop uses `grill-me`, a small skill that questions the user one decision at a time and gives a recommended answer for each question. Its purpose is not to produce pages of planning prose; it is to reach a shared design concept.

Example decisions for a product feature: What is in scope? What happens to historical data? What are the exceptions? Where is the feature visible? How is success tested? Which choices were rejected?

The same idea applies to Python/ML code: Is data alignment guaranteed? What does `nodata` mean? How are inputs normalized? What numerical tolerance is acceptable? Does a change have to preserve deterministic output?

Takeaway: Spend human attention on decisions that materially influence the final system. Do not spend it endlessly refining the formatting of the PRD.

### 1.4 Specification = destination; tickets = journey

After the grilling session, convert decisions to a PRD/specification containing:

- Problem and intended outcome.
- Functional requirements and user stories.
- Explicit non-goals / out-of-scope behavior.
- Acceptance criteria and testing decisions.
- Proposed modules and interfaces affected by the work.
- Non-obvious assumptions and rejected decisions, when useful.

Then convert the specification into dependency-aware tickets. Each ticket should be independently understandable and testable. This is more useful than a single long sequence of instructions because it provides explicit prerequisites and potential parallelism.

### 1.5 Prefer vertical slices (“tracer bullets”)

Pocock warns that coding agents often decompose work horizontally:

1. All database changes.
2. All services/APIs.
3. All interface changes.

This delays end-to-end feedback. A better decomposition is a vertical slice that crosses the necessary layers and delivers one observable behavior.

For example:

- Less useful: “Implement the entire data-access layer.”
- More useful: “Complete a lesson, award points, persist the event, and show the updated total on the dashboard.”

For a research pipeline:

- Less useful: “Refactor all preprocessing, then all training code, then all inference code.”
- More useful: “Pass one deterministic sample through feature loading → masking → model input → inference → output verification.”

Vertical slices expose integration failures sooner. The first ticket may have a wider technical footprint than expected, but its scope should be a small observable behavior.

### 1.6 Deep modules and feedback loops

Pocock draws on A Philosophy of Software Design: prefer deep modules (simple public interfaces, substantial implementation hidden behind them) over sprawling sets of shallow, tightly coupled modules. Deep modules:

- Give developers a tractable mental map of the codebase.
- Make tests meaningful at stable module boundaries.
- Reduce how much surrounding code agents need to explore.
- Allow developers to delegate implementation without surrendering interface design.

He strongly recommends test-driven development for agentic coding: red → green → refactor. Without meaningful tests, agents are effectively coding blind. A passing suite is not proof of correct behavior; in the workshop, manual QA still surfaced a database-related failure.

## 2. Context rot: what the 100K-token threshold means

Pocock informally describes a “smart zone” and “dumb zone.” In his experience, very long coding-agent sessions accumulate irrelevant detail, contradictory instructions, repeated failed attempts, and obsolete assumptions. He mentions roughly 100K input tokens as a practical warning point.

Important qualification: 100K is his heuristic, not a universal model limit or scientifically established breakpoint. A model's maximum advertised context length and its ability to use every token reliably are different things. Context quality often matters more than the token count.

Compare two nominally 100K-token sessions:

- Focused: Relevant source files, current requirements, and a coherent implementation discussion.
- Polluted: Long failed attempts, huge logs, abandoned designs, stale decisions, and off-topic history.

The second may perform worse even if both fit comfortably within the context limit.

### 2.1 Why Pocock favors resetting context

Compaction summarizes old conversation history and keeps working; Pocock worries that it preserves “sediment” from stale assumptions. He prefers to write important information into durable artifacts and begin the next task from a clean context.

This preference is useful, but it need not be absolute. A good compacted summary can preserve continuity. The question is whether a fresh worker can reconstruct the state of the task from durable inputs without carrying irrelevant conversation history.

A natural reset boundary is one ticket or one independent review—not automatically every 100K tokens.

### 2.2 What subagents actually buy you

An independently initialized subagent can work in a separate context window. It explores files, executes tools, and reasons through an assigned task, then returns a concise result to its parent.

```
Parent: issue metadata + architecture + decisions
        |
        +── Worker A: ticket 001 + relevant repository files
        |
        +── Worker B: ticket 002 + relevant repository files
        |
        +── Reviewer: diff + spec + standards + tests
```

If three workers each consume 80K tokens, the parent does not inherently need to hold 240K tokens of their entire work. It can receive three short summaries. However:

- Total model token usage can still increase, especially with duplicated exploration.
- The parent can still suffer context rot if it accumulates long worker reports or many review iterations.
- Subagents themselves can become overloaded.
- A forked/inherited agent context may copy history; independent threads do not automatically imply clean starting contexts in every configuration.
- Separate agent contexts do not automatically imply separate filesystems. Parallel writers require file or worktree isolation.

Design requirement: For each ticket, launch a genuinely fresh worker with only the needed spec, ticket, repository instructions, and local code access. Return a compact structured report, not an entire transcript.

### 2.2 Revised: hybrid subagent development

Correct, with one important distinction: Matt Pocock primarily advocates using subagents to work on separate, independently executable tickets within a larger problem, rather than having several agents collaborate on the same implementation task.

He does use subagents for other purposes, such as repository exploration and independent review.

#### Two different multi-agent architectures

1. Collaborative agents — multiple agents on one ticket

Agents coordinate around a single task. This can require more handoffs, shared context, and integration between agents.

2. Ticket parallelism — Pocock's primary approach

Each agent owns an independent vertical slice. The orchestrator handles dependency ordering and integration.

#### What Pocock actually demonstrates

In the workshop, he describes three uses of subagents:

| Use                   | How it works                                        | Purpose                                                    |
| --------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| Exploration           | Main agent delegates repository exploration         | Keep large amounts of research out of the parent's context |
| Ticket implementation | Multiple agents work on different unblocked tickets | Parallelize development while isolating contexts           |
| Code review           | A separate agent reviews completed implementation   | Fresh reasoning context for independent verification       |

His Sandcastle example follows a planner → parallel implementers → reviewer → merger pattern.

The implementers receive different issues, work in isolated Git worktrees, and produce commits. A merger agent then integrates the resulting branches.

This does not mean he opposes collaborative agents. His workshop simply emphasizes ticket-level parallelism as the main way to scale autonomous implementation.

#### Why this distinction matters for your Codex setup

Suppose you're implementing a new model architecture.

You could use collaborative specialization:

- Agent A researches possible architectures.
- Agent B designs the model.
- Agent C writes unit tests.
- Agent D implements the training loop.

But these tasks are tightly coupled. Agent D may need decisions from B, while C needs implementation contracts from both B and D.

Alternatively, you could create a dependency-aware ticket graph:

```
Ticket 1: Define model interface and minimal forward pass
    |
    +── Ticket 2: Integrate model into training pipeline
    |
    +── Ticket 3: Add checkpoint serialization
    |
    +── Ticket 4: Implement inference adapter
                 |
                 v
       Ticket 5: End-to-end validation
```

After Ticket 1 finishes, Tickets 2–4 can potentially run concurrently, provided their interfaces and file ownership are sufficiently independent.

This reduces the need for agents to negotiate implementation details while working.

#### My recommendation

I'd actually combine both approaches, but at different levels:

Across tickets: Use Pocock-style independent parallel workers.

Within a ticket: Allow the implementer to spawn focused exploration or research subagents when useful. Keep a single agent accountable for the implementation and its acceptance criteria.

After implementation: Use a fresh High-reasoning reviewer, ideally isolated from the implementer's history.

That gives you a hierarchy:

```
Deterministic orchestrator
    ├── Ticket A owner
    │     └── Exploration subagent
    ├── Ticket B owner
    │     └── Research subagent
    └── Ticket C owner
          └── Exploration subagent

Independent review → integration
```

The general principle: Parallelize independent outcomes first. Delegate specialized subtasks within an outcome only when doing so actually reduces context load or improves the result. Otherwise, extra agents can increase coordination costs without improving quality.

### 2.3 Reasoning effort and context length are different axes

Your stated Codex arrangement is GPT-6.1 Sol High reasoning for the main agent/review, with lower-reasoning subagents for routine work.

That division is sensible, but lower reasoning does not necessarily mean a smaller input context window. Thinking effort and available context length should be treated independently.

Proposed routing:

| Role                         | Suggested reasoning               | What its context should contain                              |
| ---------------------------- | --------------------------------- | ------------------------------------------------------------ |
| Dispatcher                   | Low/Medium                        | Ticket IDs, status, blockers, worker handles                 |
| Explorer                     | Low                               | Specific investigation question + source files               |
| Implementer                  | Medium; escalate complex work     | One ticket, spec section, relevant interfaces, tests         |
| Independent reviewer         | High                              | Diff, acceptance criteria, standards, verification artifacts |
| Merger / integration checker | Low/Medium + deterministic checks | Branches, conflict details, test outcomes                    |

Caution about your high-reasoning main agent: If the same long-running main thread coordinates 20 workers and performs every review, its review context will accumulate history. Better options:

1. Keep a thin coordinator and dispatch a fresh High-reasoning reviewer per change; or
2. Have the High main agent review only at explicit milestones, with fresh sessions or carefully controlled context.

The coordinator should track what happened, not re-read all implementation details.

### 2.4 Sensible context-management practices

- Keep always-loaded `AGENTS.md` and system-level instructions short.
- Store persistent decisions in specs, tickets, tests, and Git, not only in chat.
- Ask exploration workers for file paths, symbols, decisions, and risks, not full logs.
- Give independent reviewers only the information needed to assess the diff.
- If a task repeatedly needs huge contexts, split it or improve module boundaries.
- Treat context-budget targets as monitoring heuristics, not hard correctness rules.
- Avoid automatically compacting into the next ticket when a clean context can be spawned.

## 3. Skills are workflow building blocks, not the entire automation platform

Names discussed in our conversation and the associated responsibilities:

| Skill / concept                              | Responsibility                                       |
| -------------------------------------------- | ---------------------------------------------------- |
| `/grill-me`, `/grill-with-docs`              | Clarify requirements and assumptions                 |
| `/to-spec` (earlier workshop: `write-a-prd`) | Record destination, scope, behavior, tests           |
| `/to-tickets` (earlier: `prd-to-issues`)     | Decompose into dependency-aware vertical slices      |
| `/implement`, `/implement-spec`              | Execute ticket(s), potentially via subagents         |
| `/tdd`                                       | Encourage red–green–refactor implementation          |
| `/code-review`                               | Independent assessment of code changes               |
| `/improve-codebase-architecture`             | Identify better module boundaries and testing seams  |
| `/handoff`                                   | Preserve concise context between sessions            |
| `/retro`                                     | Reflect on recurring failures and refine the process |

> These are the labels discussed earlier, not a guarantee that every installed library version has exactly these names or behaviors. Inspect each skill's instructions and your installed Codex plugin version.

Use skills for judgment-intensive tasks: questioning, planning, decomposition, implementation conventions, and review. Use ordinary scripts for mechanical tasks: reading YAML, validating a DAG, claiming a job, launching workers, collecting exit codes, running tests, enforcing retries, and merging branches in a controlled order.

This follows Pocock's broader point that developers should own the planning and orchestration stack instead of relying on opaque frameworks that are hard to debug.

## 4. Reference architecture for an autonomous ticket-based workflow

```
                     HUMAN / DOMAIN EXPERT
                              |
                   clarify design and scope
                              v
                    spec.md + tickets/*.md
                              |
                              v
                  DETERMINISTIC HARNESS
             parse • validate DAG • queue • retry
                 /            |             \
                v             v              v
          Worktree A      Worktree B      Worktree C
          Fresh agent     Fresh agent     Fresh agent
          ticket 001      ticket 002      ticket 003
                \             |              /
                 v            v             v
                per-ticket tests + status reports
                              |
                       independent review
                       (fresh High agent)
                              |
                        merge one at a time
                              |
                      integration test gates
                              |
                 human QA / blocked decisions
                              |
                  done OR new correction ticket
```

### Responsibility split

Deterministic harness owns:

- Parsing tickets and verifying dependency references.
- Selecting only unblocked tasks.
- Allocating workers and isolated worktrees.
- Tracking `pending → running → verifying → done` or `blocked`.
- Enforcing concurrency, time, cost, and retry budgets.
- Running tests; interpreting actual exit codes.
- Serializing merges and rerunning integration tests.
- Recording durable reports after crashes/restarts.

Agent workers own:

- Reading their specific ticket and related code.
- Making bounded code changes.
- Writing tests, ideally test-first.
- Explaining tradeoffs and reporting uncertainty.
- Committing changes in their isolated branch.

High-reasoning reviewer owns:

- Checking the intended behavior against the implementation.
- Detecting missing tests, unsafe assumptions, bad module boundaries, and scope creep.
- Producing structured blocking or nonblocking findings.

Human owns:

- Ambiguous product, architecture, or scientific decisions.
- Permissions for destructive, expensive, or external actions.
- Final QA for behavior that automated checks cannot reliably establish.

## 5. Markdown structure and ticket contract

A simple repository structure:

```
repo/
├── AGENTS.md                 # Brief repository-wide rules
├── src/
├── tests/
└── .agent-work/
    └── feature-name/
        ├── spec.md           # Destination document
        ├── tickets/
        │   ├── 001.md
        │   ├── 002.md
        │   └── 003.md
        ├── reports/          # Worker/reviewer/test results
        └── state.json        # Harness-owned runtime state (optional)
```

To avoid conflicts, the harness should own status transitions. Workers read tickets and report outcomes but do not edit shared ticket status concurrently. Ticket metadata may be in YAML front matter; authoritative live state can instead be stored in a transaction-safe database when scaling beyond a simple prototype.

### Example ticket

```
---
id: "002"
title: "Integrate feature normalization into inference"
status: pending
blocked_by: ["001"]
priority: medium
review_required: true
---

# Goal
Ensure inference applies the same normalization contract as training.

# Context
- Read ../spec.md.
- Ticket 001 introduced the normalization module.
- Do not change input/output band ordering or raster nodata semantics.

# Acceptance criteria
- Inference uses the shared normalization interface.
- Output dimensions, band ordering, and metadata are preserved.
- Invalid pixels never contribute to normalization statistics.
- Existing inference tests continue to pass.

# Validation
- Add a failing regression test before implementation.
- Run pytest and configured type/lint checks.
- Test one small deterministic raster fixture.

# Constraints
- Do not modify unrelated model-training code.
- Do not submit an HPC job or overwrite persistent datasets.
- Do not merge or deploy.

# Completion report
- Commit hash and changed files.
- Commands run with exit codes.
- Acceptance criteria checked.
- Known limitations or remaining risks.
```

### Ticket lifecycle

```
pending --dependencies satisfied--> ready
ready   --claimed by harness-------> running
running --worker produced commit---> verifying
verifying --tests+review+merge pass--> done
any stage --needs decision or fails bounded retries--> blocked
```

Other useful rules:

- No ticket can be `ready` until every blocker is `done` in the relevant integration state.
- Detect dependency cycles before running anything.
- A process exit code of zero is not enough to mark a ticket done.
- A worker cannot mark its own output as independently reviewed.
- Merge conflicts and integration failures create a repair task or `blocked` state.
- Ticket completion is recorded after integration checks, not merely after code generation.

## 6. Migration roadmap: from ordinary skill use to a custom harness

The goal is incremental automation. Avoid building a complicated scheduler before proving that agents can finish one properly scoped ticket reliably.

### Stage 0 — Establish a repeatable repository baseline

Goal: Reliable local checks before introducing autonomy.

1. Keep `AGENTS.md` small: project constraints, key commands, conventions, and safety boundaries.
2. Establish reproducible formatting, linting, type checks, and tests.
3. Create a small deterministic fixture or smoke test for one end-to-end behavior.
4. Ensure an agent can run these checks in an isolated environment.
5. Decide which operations always require human permission (for example deployments, destructive changes, and expensive cluster submissions).

Exit criterion: A clean checkout can execute the same baseline checks with meaningful pass/fail outcomes.

### Stage 1 — Use Pocock's skills interactively, no harness

Goal: Prove that the planning workflow produces good issues.

1. Start with `/grill-me` or `/grill-with-docs` to resolve uncertainty.
2. Convert decisions into a spec using `/to-spec`.
3. Generate tickets with `/to-tickets`.
4. Manually inspect the DAG: correct dependencies, vertical slices, acceptance criteria.
5. Implement one ticket with `/implement` and `/tdd`.
6. Review the result using `/code-review` and perform QA.
7. Add discovered defects as new tickets instead of extending a long chat indefinitely.

Exit criterion: A new agent can complete one ticket from its written inputs without asking for missing context.

### Stage 2 — Use a fresh agent for each ticket, still manually supervised

Goal: Prove context isolation and the reporting contract.

1. Create a fresh session for each ticket.
2. Supply only its ticket, the relevant spec, and repository instructions.
3. Ask the worker for a compact structured result (commit, changed files, tests, unresolved questions).
4. Launch a different fresh reviewer with High reasoning and the diff/spec/standards.
5. Manually inspect failures, review findings, and integration.
6. Tune prompts and ticket format based on repeated failure modes.

Exit criterion: A complete implementation and independent review can be performed with no dependence on the prior conversation history.

### Stage 3 — Create a sequential programmatic harness

Goal: Automate the boring mechanics, keeping the execution loop easy to debug.

1. Write a Python (or TypeScript) CLI that parses Markdown YAML front matter.
2. Validate ticket IDs, dependencies, cycles, and required acceptance fields.
3. Select one ready ticket using deterministic priority rules.
4. Create an isolated branch/worktree for that ticket.
5. Launch a fresh `codex exec` worker process with a bounded prompt.
6. Capture its full machine-readable event log to disk, not the coordinator's context.
7. Run the required deterministic tests.
8. Invoke a fresh reviewer against the resulting diff.
9. Integrate only if all gates pass; otherwise retry within limits or mark blocked.
10. Persist task state and print a concise run report.

Exit criterion: The harness completes several tickets sequentially, survives an interrupted run, and can resume without relying on an LLM conversation.

### Stage 4 — Strengthen isolation and recovery

Goal: Make unattended operation repeatable and safe.

- Use a separate Git worktree per worker.
- Optionally run workers in containers with explicitly mounted inputs.
- Make ticket claims atomic and ensure crashed runs release/recover them.
- Use idempotent state transitions: rerunning the harness must not silently duplicate completed changes.
- Save worker prompt, commit SHA, tool versions, run logs, review results, and test outcomes.
- Introduce timeouts, retry limits, and a terminal `blocked` state.

Exit criterion: A crash/restart and a failed worker produce a recoverable state rather than a corrupt backlog or workspace.

### Stage 5 — Add dependency-aware parallelism

Goal: Increase throughput without destabilizing integration.

1. Compute the DAG's ready set.
2. Start with two concurrent workers that touch mostly independent modules.
3. Keep each worker in its own worktree.
4. Run ticket-local checks independently.
5. Review each result in fresh context.
6. Serialize merges into the integration branch.
7. Rerun integration checks after every merge; rebase or repair stale branches.
8. Only unlock downstream tasks after upstream changes are integrated and verified.
9. Increase concurrency when measurements show a net improvement.

Exit criterion: Parallel execution completes faster than sequential execution without causing excessive merge conflicts, false-positive completions, or rework.

### Stage 6 — Harden it for genuinely AFK development

Goal: Support longer runs with bounded autonomy.

- Cost/token/time budgets per worker and per run.
- Protected file paths and operations; no unattended production deployment or destructive dataset changes.
- Controlled network/tool permissions and secret exposure.
- Explicit review thresholds and escalation rules.
- Human approval checkpoints for uncertain or consequential changes.
- Reproducible final integration checks and a human-readable final report.
- Periodic retrospectives that update skills/instructions only after failure patterns are confirmed.

Exit criterion: The system can stop safely, explain exactly what happened, and hand off unresolved problems without inventing success.

## 7. Minimal harness algorithm (illustrative pseudocode)

The exact Codex invocation and configuration options should be verified against your installed CLI. This sample expresses the orchestration contract, not a runnable production program.

```python
while True:
    tickets = load_tickets()
    ready = find_unblocked_tickets(tickets)

    if all_done(tickets):
        break

    if not ready and no_workers_running():
        report_blocked_state()
        break

    for ticket in ready[:available_worker_slots()]:
        claim_ticket(ticket)
        spawn_fresh_worker(
            ticket=ticket,
            isolated_worktree=True,
        )

    for result in collect_completed_workers():
        if not result.success:
            retry_or_block(result)
            continue

        if not run_required_checks(result):
            retry_or_block(result)
            continue

        review = run_fresh_review(result)

        if review.has_blocking_findings:
            create_fix_ticket(review)
            continue

        merge_to_integration_branch(result)
        run_integration_checks()
        mark_ticket_done(result.ticket_id)

run_final_review()
produce_summary()
```

### Worker report contract

Prefer machine-readable results over a long natural-language transcript:

```
{
  "ticket_id": "002",
  "status": "implemented",
  "commit": "<commit-sha>",
  "changed_files": ["src/normalization.py", "tests/test_normalization.py"],
  "checks": [
    {"command": "pytest tests/test_normalization.py", "exit_code": 0}
  ],
  "acceptance_criteria": [
    {"criterion": "invalid pixels excluded", "evidence": "test_invalid_mask"}
  ],
  "risks": []
}
```

Never trust this report alone. The harness should verify the commit actually exists and rerun required commands itself. Structured outputs are coordination artifacts, not evidence of correctness until independently checked.

## 8. Context policy for the harness

### Parent/coordinator input

Keep the coordinator's active information small:

```
Current spec ID
Ticket DAG: ID, status, blocked_by, priority
Active workers: ticket ID, PID/job handle, worktree
Last verification outcomes
Budget and concurrency limits
```

The coordinator generally does not need full diffs, entire logs, or internal worker reasoning. Store those on disk and pass specific artifacts to fresh reviewers when needed.

### Worker input

```
Repo rules / AGENTS.md
One ticket
Relevant spec sections
Relevant files discovered by the worker
Permitted commands and file boundaries
Required checks and output schema
```

### Reviewer input

```
Ticket acceptance criteria
Original spec (or relevant section)
Diff and changed-file summaries
Coding and architecture standards (explicitly supplied)
Actual check results
Specific request for findings with severity + locations
```

This reflects Pocock's push vs. pull distinction: let an implementer pull extra standards or knowledge when needed, but push the required standards to the reviewer so they are guaranteed to be checked.

### Operational measures to track

- Median and tail context use per worker; context growth in coordinator.
- First-pass test success rate.
- Number of agent review findings per ticket.
- Human-discovered regressions after automated review.
- Retry rate and blocked-ticket causes.
- Merge conflict and rebase time.
- Wall-clock throughput and model cost per accepted ticket.

Avoid optimizing merely for token count; optimize for verified work per unit time/cost with an acceptable defect rate.

## 9. Special considerations for Python, ML, and HPC

This conversation focused on software development generally, but your Python/ML environment adds constraints that ticket templates should explicitly capture.

Scientific invariants: shape and dtype, spatial metadata and georeferencing, valid-mask behavior, no-data handling, feature ordering, random seeds, tolerances, and prevention of train/validation leakage.

Fast feedback: small synthetic or deterministic fixtures; unit tests for transformation logic; a short end-to-end inference smoke test; static checks. Separate these from expensive benchmark or training jobs.

Resource safety: a worker should not submit expensive SLURM jobs, overwrite persistent `/panfs` data, remove large artifacts, or mutate shared production environments unless the ticket explicitly authorizes it. Prefer temporary directories, ephemeral containers, and bounded resource quotas.

Reproducibility: record environment/container identifier, config hash, random seed, input-data version, code commit, and metric definition for meaningful ML changes.

Scope control: an agent fixing a normalization bug should not opportunistically redesign the entire training pipeline unless the ticket was explicitly expanded and re-reviewed.

## 10. Failure modes and remedies

| Failure                                    | Likely cause                                            | Remedy                                                          |
| ------------------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------- |
| Main agent becomes forgetful               | Too many verbose worker results                         | Thin coordinator + persisted reports + fresh High reviewer      |
| Subagents repeat old mistakes              | Parent context inherited or insufficient ticket details | Explicit fresh sessions; stable ticket/spec inputs              |
| Workers write conflicting changes          | Shared working tree or overlapping tickets              | Independent worktrees; dependency/DAG checks                    |
| Tests pass but feature fails               | Tests cover shallow units, not behavior                 | Vertical slices, integration tests, manual QA                   |
| Agents endlessly retry                     | No bounded failure state                                | Retry caps, blocked state, human escalation                     |
| Completed tickets become misleading        | Spec/ticket drift or stale docs                         | Code/tests remain authoritative; archive/close old tickets      |
| Parallelism makes work slower              | Conflicts and duplicated exploration                    | Measure throughput; limit concurrency                           |
| Codebase becomes difficult to reason about | Shallow modules and uncontrolled agent refactoring      | Define deep module interfaces; architecture reviews             |
| Dangerous automation                       | Excessive permissions                                   | Sandboxing, scoped credentials, protected paths, approval gates |

## 11. What to do next (recommended first experiment)

Use a small, self-contained real feature that can be validated locally without external side effects. Keep it to approximately 3–5 vertical tickets.

- Confirm the installed Pocock skills and existing Codex subagent routing.
- Establish deterministic baseline tests and a minimal `AGENTS.md`.
- Grill the requirements; produce a spec with concrete acceptance criteria.
- Generate and review the ticket DAG, especially the first vertical slice.
- Implement one ticket manually using a fresh lower-reasoning worker.
- Run checks and use a fresh High-reasoning reviewer on the diff.
- Repeat for the remaining tickets, recording where human intervention was needed.
- Build a sequential dispatcher only for the steps already demonstrated to work.
- Add crash recovery and isolated worktrees.
- Run two tickets in parallel and compare throughput, defects, and integration work.

### Decision rule for when to build a custom harness

Stay with the skills library alone if `/implement-spec` (or your equivalent workflow) reliably finishes bounded work and manual coordination costs little.

Build a harness when you specifically need durable state between sessions, unattended retries, crash recovery, strict permission budgets, repeatable ticket scheduling, reliable merging, or cross-run telemetry. Those are primarily orchestration problems; adding more prompt instructions usually does not solve them.

## Bottom line

Pocock's most valuable lesson is not a particular prompt or a hard 100K-token cutoff. It is an engineering architecture: clarify the goal with humans, specify observable outcomes, split work into vertical slices, give disposable agents isolated tasks, and make quality measurable through tests and review.

Your lower-reasoning Codex subagents can make context isolation practical; your High-reasoning review layer can focus attention on correctness. The next improvement is to stop relying on a long-lived main conversation to remember execution state. Make Markdown, Git, tests, and a small deterministic scheduler the durable backbone, and treat each agent's context as temporary working memory.