# Forest CPU execution

Start with any retained Forest terminal: inspect its current capacity and reuse
it when suitable. Probe candidates only when no suitable live connection exists.
From the base ADAPT login node, probe `forest201` through `forest205` with direct
SSH. Forest access does not use Slurm; no `forest` partition was present in the
Slurm configuration observed when creating this skill.

This lightweight probe shows architecture, CPU count, load, available memory,
and active processes without starting a workload:

```bash
for node in forest201 forest202 forest203 forest204 forest205; do
  ssh -o BatchMode=yes -o ConnectTimeout=5 "$node" '
    hostname
    uname -m
    getconf _NPROCESSORS_ONLN
    uptime
    free -m
    ps -eo user,pid,pcpu,pmem,comm --sort=-pcpu | head -12
  '
done
```

Skip unreachable hosts. Compare load to logical CPU count and use **available**
memory rather than the `free` column. Inspect active processes too: load alone
does not establish that a host is free. Prefer low sustained load, no substantial
competing compute workload, and enough memory for the job plus headroom. Recheck
the chosen host after a short interval, optionally using `vmstat 1 3` for current
CPU activity. Connect to the selected host, for example:

```bash
ssh -tt -o ServerAliveInterval=30 -o ServerAliveCountMax=3 forest201
```

Enter the exact shared checkout and verify host, architecture, directory, and
source before running checks. Keep this terminal open and record its session ID;
send subsequent checks and related follow-up commands through the same session.
An available suitable existing Forest terminal avoids another connection setup.
Recheck current capacity before each workload. Forest hosts are shared; neither
probing nor keeping SSH open reserves CPUs or memory. Bound workers and thread
counts to spare capacity, monitor longer
jobs, and reduce or stop your own work if contention or memory pressure develops.
Avoid duplicate jobs from concurrent agents. If every host is busy or undersized,
report the result instead of running the workload on the login node.

Use the project's prescribed commands. Here, an ordinary test run from the
checkout root is `.venv/bin/python -m pytest`; verification scope still comes
from the testing policy. Retain exit status directly, or use `pipefail` when
streaming output through `tee`.

Check temporary-storage mount options for executable fixtures. Forest203's `/tmp`
and `/var/tmp` were observed with `noexec`; Git hooks and executable-file tests
cannot exercise their intended paths there. An executable node-local directory
such as an owner-private `mktemp -d /dev/shm/TASK-XXXXXX` can avoid shared-storage
I/O overhead when its mount options, free space and memory headroom fit the task.
Set a task-specific `TMPDIR`, bound resource use, and retain required observations
on shared storage before cleaning up temporary files. Recheck the actual host;
the observation above does not establish every node's current mount options.
