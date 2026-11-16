---
name: capture-evidence
description: Save development checks, original reviews, instruction snapshots and derived evidence with ticket or shared milestone destinations and registered provenance. Runtime evidence adoption and evidence retirement are separate work.
---

# Capture evidence

Identify the feature, ticket(s), evidence purpose and producing actor before capture.
Use the repository's [environment](../../../../docs/agents/python-environment.md),
[testing policy](../../../../docs/agents/testing.md),
[test strategy](../test-strategy/SKILL.md) and
[review contract](../../../../docs/agents/review-records.md) for required checks,
original reports and source/instruction identities. Those contracts govern what
must be captured; this skill governs placement and registration. Follow applicable
[compute routing](../adapt-compute/SKILL.md) before Python/check workloads.

Use `.venv/bin/python -m ticket_harness.evidence --help` from the checkout.
The helper accepts an existing `.scratch/<feature>` directory with `issues/`.
Read [the helper contract](../../../../docs/agents/evidence-capture.md) for JSON
ownership, protection and failure behavior when coordinating multiple producers.

1. Identify active approved-input and frozen-evidence paths before writing.
   Pass every applicable file/subtree as `--protect PATH` **before** the subcommand.
   If the feature itself is an active approved input, retain evidence outside that
   input through the authorized run-output workflow; this development helper cannot
   write there. Arbitrary active runs are not automatically discovered. Registration
   retains allocation protections; add newly frozen paths at registration.
2. Ask Python to select the destination with `allocate --ticket ID --purpose TEXT
   --producer ACTOR`. For genuinely shared evidence, repeat `--ticket ID`, add a
   descriptive `--shared NAME`, and use `--milestone ID` for milestone-scoped work.
   Python creates references in each relevant ticket's evidence artifact, with one
   authoritative shared artifact. Include those links in ticket completion evidence
   when bookkeeping is authorized; capture never edits approved ticket bodies.
3. Write new originals into the returned `destination`. Give each parallel producer
   its own allocation and return its receipt. Create payload files exclusively
   (shell `set -o noclobber`, Python `open(..., 'x')`, or equivalent). Preserve stdout,
   stderr and exit results as required by the producing workflow; a failed command
   is still evidence. Never replace a registered file or edit allocation metadata.
4. Register completed files using `register --allocation PATH --file RELATIVE_PATH
   --source-version IDENTITY --activity ACTUAL_COMMAND_OR_ACTIVITY --result OBSERVED_RESULT`.
   Repeat `--file` for a capture's files. Supply the actual tested/assessed revision
   and a retained patch/manifest identity for uncommitted inputs; HEAD alone does not
   identify dirty source. Represent unavailable facts explicitly as unknown. The
   helper hashes bytes but cannot certify the truth of an actor's result statement.
   For derived content add `--kind derived --derived-from ORIGINAL_PATH` (relative
   to the feature; repeat for multiple originals), label losses in the content, and
   retain originals for required review. Derivation registration is no replacement
   approval. Return the artifact link and capture ID to the caller.

Producers edit only their own payloads. Python serializes registrations and preserves
review namespaces. Reviewers return original reports to separately allocated paths;
recording them supplies no finding disposition or human acceptance. Existing source,
reports, historical layouts and embedded paths retain their identities. Capture has
no retention, deletion, promotion or runtime authority; follow later approved tools
for those actions.
