# Ticket 25 review scope and instructions

Read the canonical [evidence index](25-evidence-index.md) and its actual final
verification records, [coverage/ownership notes](25-work-notes.md), supplied
[ticket snapshot](instructions/ticket.md), [spec snapshot](instructions/spec.md),
[evidence policy snapshot](instructions/evidence-policy.md), and current repository
AGENTS/GLOSSARY/ADRs, docs/agents/testing.md, review-records.md and evidence-capture.md.
Snapshot relative links retain their original source-path semantics; use actual
current sources to follow them. The uncommitted approved plan/skill updates listed
in starting-status.txt are supplied inputs, not implementation changes to assess.

Fixed original review baseline is 2c01fe9fe04c78fa10a2dac11e94826876467562. Reviews
assess the whole ticket since that baseline at the checkpoint commit named in the
assignment, including unchanged collaborators that can defeat the promised outcome.
No previous real finding key for ticket25 exists at round1. Historical M1 findings
retain their accepted-source scope; no calibration or M1 replay is assigned.

Use the repo-owned review envelope and substantive-reasoning requirements.
Trace actual CLI entry, allocation/register writers, flock, source/result identity,
immutable originals and derivations, authoritative JSON save/restore, shared links,
approval-preserving behavior, failure/partial transitions and protection enforcement.
Inspect accepted input values and aliases rather than assuming narrow happy paths.
A counterexample to an explicit guarantee must be reported. Capture records producer
statements; it cannot certify their truth or infer retention/deletion/human authority.

For test review, apply test-strategy: existing full suite protects harness behavior;
new cases use public command/process/real-Git/filesystem/JSON seam with no internal
mocks. Review meaningful missing cases and brittle/unnecessary cases proportionately.
The host's noexec /tmp failures retain original evidence and are diagnosed separately;
the shared-TMPDIR final run must supply actual current-source full passing checks.

Do not change assessed product source or read sibling same-round reports. Save your
original report verbatim to your uniquely assigned producer destination as report.md,
with assessment/report IDs, role/assignment identity, actual settings or unavailable,
source/instruction identities, inspected flows/omissions, substantive assessment,
evidence audit, concrete blocking/optional findings and unresolved assumptions.
No prose cap overrides those required details. Attribute test judgments accurately;
passing tests or digests alone do not prove the architecture. Do not run redundant
full suites; scoped missing evidence may be captured on compute hosts if necessary.

Requested fresh settings: GPT-6.1 Sol High, <=250000 active-context target. Spawn
metadata requests the model/reasoning; enforcement and measured context telemetry
remain unavailable. Report actual availability, not imaginary backend proof.

## Explicitly authorized documentation follow-up

During this work the user also requested persistent Forest SSH sessions and live
Slurm allocation reuse in the ADAPT skill. Commit ec1a1e5 records that standalone
skill update (three initially supplied untracked ADAPT files). Include it in the
whole-baseline diff assessment as this explicit user-requested scope; see
25-compute-guidance-update.md, original/current snapshots, and actual passing
25-compute-guidance-validation.json. It changes no tested executable/test source.
Current full-runtime evidence retains its actual original instruction snapshot;
new compute guidance has separate document/skill/link/bash-syntax validation.
