# Explicit follow-up: persistent ADAPT sessions

The user requested during ticket25 implementation: "Update the adapt compute
skills file to keep connection to forest open, and salloc and keep reusing for the
other nodes; that way we only get connection overhead once."

Updated only the ADAPT skill and its Forest/Slurm references. Existing content was
previously supplied as untracked user work; [original copies](compute-guidance-original/)
and [new copies](compute-guidance-current/) preserve the narrow update's provenance.
The new guidance prefers persistent SSH/terminal sessions; reuses compatible live
salloc/srun allocations with state/resource/time checks; records session/job IDs in
handoffs; and releases allocations at the end of related work or on user request.
It preserves shared Forest capacity checks and distinguishes SSH from reservation.
The Forest reference additionally records the actual noexec temporary-storage
observation and bounded executable node-local scratch alternative.

[Actual validation](25-compute-guidance-validation.json): skill validator, links,
and all bash example syntax checks pass. Current persistent Forest203 PTY session
10089 has been reused for host/checkout/resource inspection and the validation
command. No Slurm job was requested and no live Slurm reuse test is claimed.
This standalone documentation update changes no tested runtime or test source;
it requires scoped guidance validation, not a full-suite replay.

The user separately clarified that adding packages is permitted when needed, with
updated environment definitions and an original-version backup. "Frozen" requirements
mean version-pinned reproducibility, not a ban on dependency changes. No package
addition is currently needed: the declared isolated build backend succeeded.
