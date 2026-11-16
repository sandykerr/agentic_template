# Slurm execution through gpulogin1

Reuse the retained gpulogin1 terminal, or open a persistent connection from the
base ADAPT login node:

```bash
ssh -tt -o ServerAliveInterval=30 -o ServerAliveCountMax=3 gpulogin1
sinfo --all -o '%P %a %l %D %t %N'
sinfo --partition=compute,grace,grace-cpuonly -o '%P %c %m %G %f'
```

Select `compute` for AMD64 GPU work, `grace` for ARM64 GPU work, or
`grace-cpuonly` for ARM64 CPU work. Refresh live configuration rather than
assuming availability, GPU types, or resource defaults. Inspect the selected
partition with `scontrol show partition compute` (substitute its name).

## Reuse a live allocation or allocate, then enter a compute node

Keep the gpulogin1 SSH terminal open and record its session ID. Before requesting
resources, inspect this task's recorded allocation, if any, with `squeue -j JOB_ID`
and `scontrol show job JOB_ID`. Reuse its existing compute shell when job state,
architecture, partition, CPUs, memory, GPUs and remaining time fit the next workload.
An SSH connection to a node without a live matching allocation grants no resources.
If a compute shell was lost but the allocation remains live, verify ownership and
running steps before attaching a new step from the persistent gpulogin1 terminal;
for example, `srun --jobid=JOB_ID --ntasks=1 --pty bash -l`. Avoid duplicating a
still-running workload or competing with an existing step for its resources.

If no suitable allocation exists, size CPUs, memory, time, and GPUs for the actual
task. These are small examples. Run **one** matching command from `gpulogin1`:

```bash
# AMD64 GPU
salloc --partition=compute --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=16G --gres=gpu:1 --time=00:30:00 --immediate=60

# ARM64 GPU
salloc --partition=grace --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=16G --gres=gpu:1 --time=00:30:00 --immediate=60

# ARM64 CPU
salloc --partition=grace-cpuonly --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=16G --time=00:30:00 --immediate=60
```

Explicit GPU requests are required for GPU work; choosing a GPU partition alone
does not establish device access. CPU-only ARM64 jobs omit GPU resources. Use
`--account` or `--qos` only when required by current site configuration and the
user's authorized association. Preserve scheduler errors instead of guessing
privileged values. The examples bound allocation waiting to 60 seconds. If
resources are unavailable, report the failure; queue a longer wait only when
appropriate to the task, keeping the user informed while waiting.

Wait for an actual allocation grant. The `salloc` shell may still be on the login
host. Inspect the allocation and start a job step:

```bash
printf 'job=%s nodes=%s\n' "$SLURM_JOB_ID" "$SLURM_JOB_NODELIST"
scontrol show job "$SLURM_JOB_ID"
srun --ntasks=1 --pty bash -l
hostname
uname -m
```

Confirm the hostname belongs to allocated nodes and the architecture matches the
task. Enter the exact shared checkout. For GPU work, check `nvidia-smi -L` inside
the job step and verify the application's backend actually uses the allocated
device. A passing CPU fallback does not verify a GPU requirement. Keep workers
and thread pools within `SLURM_CPUS_PER_TASK`, including nested parallelism.

Keep both the `salloc` allocation shell and the `srun` compute shell open between
related commands. Send subsequent work through the same terminal; do not run a
new `ssh`/`salloc`/`srun` sequence for each check. Record terminal ID, job ID, node,
resources and expiry/remaining time so a later assignment can verify and reuse
them. Before each workload, refresh job state and time remaining from the live
allocation and confirm the checkout and required devices still match.

## Finish and release

Save logs and required outputs to persistent shared storage and capture the
workload's exit status. Exit the `srun` shell, then the allocation shell to
relinquish resources when related work is complete or the user requests release.
Keep a suitable live allocation for planned follow-up work within its time limit;
do not release and reacquire it between checks. Confirm the recorded job ID has left the queue with
`squeue -j JOB_ID`. After a lost connection or an allocation that remains,
inspect that specific job and use `scancel JOB_ID` to release your allocation.
Limit cleanup to this task's jobs. Neither allocation success nor a closing
shell proves workload success.
