---
name: adapt-compute
description: Run tests and CPU, GPU, or memory-intensive work on ADAPT compute hosts. Use Forest via SSH for AMD64 CPU work, or Slurm via gpulogin1 for AMD64 GPUs and ARM64 CPU/GPU work.
---

# ADAPT compute

Run tests, builds, benchmarks, dependency builds, and other intensive processes
on a suitable compute host. Use login nodes for editing, SSH, scheduler commands,
and lightweight inspection.

## Choose the destination

| Workload | Access from an ADAPT login node | Destination |
| --- | --- | --- |
| AMD64 CPU, including ordinary tests and memory-intensive CPU work | Direct SSH | Least busy suitable host among `forest201` through `forest205` |
| AMD64 GPU | `ssh gpulogin1`, then Slurm | `compute` partition |
| ARM64 GPU | `ssh gpulogin1`, then Slurm | `grace` partition |
| ARM64 CPU | `ssh gpulogin1`, then Slurm | `grace-cpuonly` partition |

AMD64 means `x86_64`, including Intel processors; ARM64 means `aarch64`.
Default ordinary CPU checks to Forest. Choose ARM64 when the task requires it.
Memory requirements also govern host choice and allocation size.

1. Identify the required architecture, accelerator, CPUs, memory, and runtime.
   Read the target repository's environment and testing instructions. In this
   repository these are [python-environment.md](../../../../docs/agents/python-environment.md)
   and [testing.md](../../../../docs/agents/testing.md).
2. For Forest, follow [references/forest.md](references/forest.md). For Slurm,
   follow [references/slurm.md](references/slurm.md). Check current capacity;
   an existing terminal or earlier observation does not establish availability.
3. On the execution host, enter the exact checkout or worktree being changed.
   Shared storage exposes this project at
   `/panfs/ccds02/nobackup/people/ajkerr1/agentic_template/agentic_template`;
   use the actual worktree path when different. Confirm `hostname`, `pwd`,
   `uname -m`, `git rev-parse HEAD`, and `git status --short`.
4. Run the repository's commands there. Bound concurrency by spare Forest
   capacity or allocated Slurm CPUs, accounting for subprocesses, test workers,
   and BLAS/OpenMP threads. Retain output and exit status.
5. Report host, architecture, checkout/revision and relevant dirty changes,
   commands, results, and any Slurm job ID. Release allocations when finished;
   retain SSH terminals when the user requests it.

## Environments and shared storage

Follow the target checkout's environment policy. For this repository, use its
uv-managed `.venv` and explicit `.venv/bin/python`, installing dependencies on
the execution host. Set `UV_CACHE_DIR` as documented.

An AMD64 environment cannot execute on ARM64. Use a separate checkout/worktree
with its own environment for another architecture; preserve the exact source
and uncommitted changes requiring verification. Confirm the interpreter and
native dependencies work on that host. Keep architecture-specific environments,
build outputs, and caches separate; never overwrite an environment used by an
active run on shared storage. Report unavailable ARM64 dependencies as a blocker
rather than claiming verification on another architecture.

Retain required logs and artifacts in shared storage. Node-local scratch is
temporary; copy results back before releasing a job. A lost connection does not
prove a workload stopped: inspect its process or job before retrying.

If access or resources are unavailable, report the limitation and alternatives.
Keep intensive work off login nodes; change architecture or accelerator only
when it still satisfies the task. For sandbox network failures, request the
tool's execution escalation for SSH instead of bypassing it.
