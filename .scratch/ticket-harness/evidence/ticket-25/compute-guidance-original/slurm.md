# Slurm execution through gpulogin1

From the base ADAPT login node:

```bash
ssh gpulogin1
sinfo --all -o '%P %a %l %D %t %N'
sinfo --partition=compute,grace,grace-cpuonly -o '%P %c %m %G %f'
```

Select `compute` for AMD64 GPU work, `grace` for ARM64 GPU work, or
`grace-cpuonly` for ARM64 CPU work. Refresh live configuration rather than
assuming availability, GPU types, or resource defaults. Inspect the selected
partition with `scontrol show partition compute` (substitute its name).

## Allocate, then enter a compute node

These are small examples; size CPUs, memory, time, and GPUs for the actual task.
Run **one** matching command from `gpulogin1`:

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

## Finish and release

Save logs and required outputs to persistent shared storage and capture the
workload's exit status. Exit the `srun` shell, then the allocation shell to
relinquish resources. Confirm the recorded job ID has left the queue with
`squeue -j JOB_ID`. After a lost connection or an allocation that remains,
inspect that specific job and use `scancel JOB_ID` to release your allocation.
Limit cleanup to this task's jobs. Neither allocation success nor a closing
shell proves workload success.
