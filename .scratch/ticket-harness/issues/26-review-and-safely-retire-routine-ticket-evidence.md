# 26: Review and safely retire routine ticket evidence

**What to build:** Use ticket 25's captured evidence to deliver a narrow complete
assessment, fresh review, preview and Python-controlled deletion workflow. Establish
standing retention guidance and demonstrate execution under the current ADAPT
compute policy rather than assuming historical execution practices still apply.

**Blocked by:** [25: Guide ticket and shared evidence creation.](25-guide-ticket-and-shared-evidence-creation.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence workflow spec](../evidence-workflow-spec.md).

**Milestone:** EC1. Human EC1 acceptance follows both tickets 25 and 26.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared role/testing contract; TDD and test-strategy; skill-writing
guidance for agent instructions; current AGENTS.md compute routing and adapt-compute
when its host conditions apply. Evidence review uses a fresh High reviewer
independently of implementation reviews.

**Context:** Policy and decision order; structured records; fresh review and Python
execution; navigation for deleted evidence; protected originals and frozen inputs;
current execution-host and environment requirements.

## Acceptance criteria

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

## Verification

Use a small routine-output sample with a protected record, unknown content and an
altered-after-assessment file. Observe public command exits, JSON states, actual
files and navigation; include a failed removal with an honest outcome. Run the
shared required implementation checks and reviews on policy-appropriate hosts,
recording actual host/architecture/source/environment provenance and resource
selection. Use the routing appropriate to the workload, not an unnecessary
GPU/architecture matrix. EC1 demonstrates the complete narrow capture-to-cleanup
path across tickets 25–26 without claiming parallel assessment or broad calibration.

## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-workflow-spec.md#policy-and-decision-order), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
