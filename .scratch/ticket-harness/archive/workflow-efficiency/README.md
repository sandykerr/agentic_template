# Workflow-efficiency follow-up

## Archive location and current guidance

This completed follow-up was moved from `.scratch/workflow-efficiency/` into the
ticket-harness archive so the feature's tickets and supporting history share one
tracker. Use the current [development procedure](../../../../docs/agents/development-efficiency.md)
for new work. This archive records the original implementation and validation;
its references to ticket 20 being next describe that earlier checkpoint.

The originating [ticket 19](../../issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md)
remains completed. Later runtime adoption belongs to
[ticket 33](../../issues/33-enforce-traceable-runtime-review-checkpoints.md) and
[ticket 34](../../issues/34-run-a-real-codex-ticket-cycle.md). This follow-up
introduced development instructions, not runtime enforcement or new ticket gates.

All files under `evidence/`, including original reports, captured instructions,
scripts, logs and manifests, were relocated without changing their contents.
Historical absolute paths and manifest entries beginning
`.scratch/workflow-efficiency/` map to
`.scratch/ticket-harness/archive/workflow-efficiency/` with the suffix unchanged.
Resolve other paths in captured evidence against its original location; for
example, the installation record's original relative environment link refers to
the root [environment.yml](../../../../environment.yml). Retained scripts and
validation results describe the historical source, not checks to rerun for a new
ticket. The review assessment retains its original identity and source scope.

## Original completion record

Authorized development-workflow update following completed ticket 19; this is
separate from that ticket's frozen campaign and does not start ticket 20.
The original request and outstanding work are retained in the
[session handoff](evidence/request-handoff.md). The subsequent user instruction
was: “Install pyyaml in the env”. Fixed review baseline:
`54acbaad0b101b9f1e13fd3d2e518eed1fd75fb5`.

## Scope and requirement map

| Required outcome | Implementation and verification |
| --- | --- |
| Ordinary ticket agents reach the procedure | [Development procedure](../../../../docs/agents/development-efficiency.md), linked from implementation, planning, test strategy, calibration preparation and handoff generation; current handoff gains only that routing paragraph. [Mechanical checks](evidence/validation-03.json) identify all eight changed source files. |
| Move cheap discovery before costly review | Current worker finishes checks/capture, traces contract risks, and supplies one canonical index before fresh committed-source reviews. [Exercise scenarios](evidence/scenarios.md) 1–2 and [original evaluator response](evidence/exercise-01-original.md). |
| Repair the complete authorized cause before another round | Preserve both original reports; fresh repair gets full keyed history and original baseline; trace related in-scope paths; investigate recurring patterns before further dispatch. Exercise scenarios 3–4. |
| Preserve accuracy and authority | Required fresh independent whole-ticket axes, final-source checks, repair bounds, scope and human QA remain authoritative. No numeric cap or automatic calibration campaign for ordinary tickets. Exercise scenarios 2–5 and independent source reviews (pending at checkpoint). |
| Reuse evidence honestly | Source/input/scope/policy must permit reuse; implementation changes renew required checks and reviews; bookkeeping gets its own consistency checks. Exercise scenario 5. |
| Keep ticket 19 and runtime work unchanged; do not start 20 | [Protection check](evidence/validation-03-05.stdout): 6,911 existing paths outside the permitted source changes protected; ticket 19/runtime unchanged; handoff selection still 20, with only preparation routing inserted. No harness run, push, milestone acceptance or ticket implementation. |
| Install PyYAML in reusable environment | [Installation record](evidence/environment-install.md); declared shared development tool in [environment.yml](../../../../environment.yml). |

## Ownership and checkpoint scope

The shared procedure owns review preparation, complete diagnosis and evidence
reuse guidance; existing skills own role assignments, review/check gates and
handoff eligibility. The changed entry routes link that one procedure rather
than duplicating it. Workers/orchestrators write existing preparation records;
reviewers independently write original reports under the unchanged record
contract. Persistence, finding history, runtime state/schema and invalidation
remain owned by the existing contracts and executable harness.

At start and after this implementation, all four architecture triggers are No:
no new lifecycle, persistence/restoration path, shared mutable state or additional
writer of existing state is introduced, including guidance state. The procedure
uses existing workers, evidence and report lifecycle. PyYAML supplies the existing
external skill validator only. No broader architecture checkpoint is triggered;
this is not a milestone-readiness or QA request.

## Verification and limits

Standalone skill/document validation follows [testing policy](../../../../docs/agents/testing.md).
There are no runtime example, package, entry-point, test or production dependency
changes; the environment addition supports the existing skill validator. Runtime
suite/packaging replay would not validate this instruction change.

[Attempt 01](evidence/validation-01.json) retains missing-PyYAML failures;
[attempt 02](evidence/validation-02.json) passes with the pre-existing system
module; [attempt 03](evidence/validation-03.json) passes with the requested
environment installation and no PYTHONPATH workaround. Each captures commands,
exits and stdout/stderr before execution. Attempt 03 checks four official skill
validators, 88 local links/anchors, routing, source digests, protected paths and
whitespace. The retained [helper](evidence/check.py) checks mechanical facts, not
prose quality. Its implementation derives anchor parsing read-only from an
unchanged historical helper; it does not execute that helper's main routine or
alter historical evidence. [Validation runner](evidence/validate.py) is a retained
local tool, not a production test.

One fresh independent preparation exercise, assignment
`/root/preparation_exercise`, answered five hypothetical decisions using the actual
instructions and scenario facts, without expected answers or prior conclusions.
Its [original](evidence/exercise-01-original.md) records instruction digests and
omitted telemetry. Parent assessment: all five decisions preserve preparation,
fresh roles, original-baseline review and source-specific evidence. Its noted
pause-versus-fresh-repair boundary is resolved by diagnosing first and then making
a purposeful required fresh assignment; no instruction change was needed.
This is reasoning through finite scenarios, not an executed ticket lifecycle or
measured speed improvement. No future efficiency/reliability guarantee is made.

The [independent assessment](reviews/workflow.md) is complete at exact source
`221bc551cb931998b0250a806309aa22b8bd41b7`: Spec and Standards each report zero
blocking and zero optional findings. Both fresh High-configured axes trace actual
instructions and unchanged collaborators; originals, settings limits and source
identities are retained. No repair or instruction change was needed. No previous
ticket 19 result is claimed as validation of these later instructions.

[Final record checks](evidence/final-audit.json) verify unchanged assessed-source
hashes, assignment identities, links across all changed Markdown and whitespace.
The [artifact manifest](evidence/artifacts.sha256) identifies retained originals
and checks. The first record check ran before that manifest existed and stopped
on its missing link; its [failure](evidence/final-audit-01.stderr) is retained.
The manifest was then created before the successful check. These subsequent files
are assessment/completion bookkeeping; they
do not relabel the source review or runtime evidence as tests of another revision.
The follow-up is complete once this bookkeeping commit exists. The current
[handoff](../../../../next_agent_prompt.md) pointed to ticket 20, which had not been
begun at that checkpoint; the linked file now carries the current assignment.
