# Running Codex in a persistent Slurm session

This process keeps your home-directory usage low and runs Codex on an allocated compute node. You can **start a clean Codex home** or **restore a completed checkpoint** onto the compute node's temporary local disk; project files remain in shared nobackup storage. Checkpoint the working home before the allocation ends to preserve new conversations.

GNU Screen keeps a session alive when your SSH connection drops. It does not keep a Slurm allocation alive beyond its time limit. Because `/lscratch` is erased after the job ends, you must save Codex's state before releasing the allocation.

## 1. Understand the saved and working locations

### 1a. Identify the three locations

- **Project directory:** your repository or other working folder in `/explore/nobackup`. Code changes and research outputs stay here.
- **Saved Codex home (restore option):** initially `/explore/nobackup/people/ajkerr1/.codex`, which your `~/.codex` symlink points to. Later, use the latest **completed checkpoint** from section 8; this source is not needed when starting fresh.
- **Working Codex home (both options):** a private directory inside the allocation's `/lscratch` space. Codex reads and writes this directory while the allocation runs.
- **Checkpoint destination (both options):** a separate, completed copy written to nobackup **after Codex stops cleanly**; do not use it as an active home.

Do not change your Unix `HOME` variable or replace your existing `~/.codex` symlink. Select the working copy using Codex's `CODEX_HOME` environment variable.

### 1b. Plan to preserve the complete saved state

No copying happens in step 1. In step 5, choose **Option A (new)** to start with no old history, or **Option B (restore)** to copy a completed, quiescent saved state—including databases and session rollouts—into local scratch. Your original shared home remains in place under either option.

A complete restored home may occupy several gigabytes because it includes downloaded packages. This conservative copy avoids assuming that databases such as `thread_history_1.sqlite` are disposable. The fresh-home option avoids carrying old corruption forward. Do not attempt a smaller `sqlite_home`-only migration until verifying which files your installed Codex version relocates.

## 2. Confirm the cluster storage rules

### 2a. Confirm how local scratch is provided

Before the first run, confirm that `/lscratch` is physically local to each compute node, rather than the same network filesystem mounted on every node. Ask the cluster documentation or administrators how to request scratch space and which job-specific scratch directory to use. Some clusters require an explicit scratch resource request.

### 2b. Plan scratch capacity and privacy

Plan for a private directory belonging to `ajkerr1` inside the allocation's assigned scratch area. It must have room for the full working Codex home and growth during the job. Restrict access because the copied home can contain authentication credentials.

## 3. Start screen and optionally identify a saved home

### 3a. Connect and start screen

SSH to a login node and record its hostname. Start a named screen session there:

```bash
screen -S codex-allocation
```

### 3b. Keep the allocation inside screen

Keep the Slurm allocation command inside this screen session. If SSH disconnects later, reconnect to the same login node and attach to this session.

### 3c. Identify the saved home only if restoring

For **Option A (new)** in step 5, skip this step: you do not need an existing `.codex` home. For **Option B (restore)**, identify the source on the login node:

```bash
export CODEX_SAVED_HOME=/explore/nobackup/people/$USER/.codex
readlink -f "$HOME/.codex"
```

The symlink may resolve through the equivalent `/panfs` path. This only records the location; it does not stop Codex writers or make the source safe to copy. On later allocations, set `CODEX_SAVED_HOME` to the **latest completed checkpoint**, not the original shared home. Re-establish the variable in the compute-node shell if it was not inherited.

## 4. Request the allocation and enter the compute node

### 4a. Request the resources

Inside the login-node screen session, request the CPUs, GPU, memory, and runtime you need. For example:

```bash
salloc --partition=compute --nodes=1 --ntasks=1 \
  --cpus-per-task=16 --mem=128G --gres=gpu:1 \
  --time=08:00:00
```

These resource amounts are examples. Add your account and the cluster's required scratch request, and adjust the resources to fit your work and partition limits.

### 4b. Enter the allocated compute node

If `salloc` already opens a shell on the allocated compute node, use that shell. Otherwise, enter the allocation with:

```bash
srun --pty bash -l
```

### 4c. Verify the node and resource environment

Inside an existing allocation, `srun` selects an allocated node automatically. Check the hostname to confirm where you are. Prefer this route over a separate SSH connection to the compute node, since it runs the shell through Slurm and carries the allocated resource environment. Preserve the assigned `CUDA_VISIBLE_DEVICES` value.

Run these commands in the allocated shell:

```bash
(
  hostname
  printf 'Job ID: %s\nGPU mask: %s\n' \
    "${SLURM_JOB_ID:-unset}" "${CUDA_VISIBLE_DEVICES:-unset}"
  if [ -n "${SLURM_JOB_ID:-}" ]; then
    scontrol show job "$SLURM_JOB_ID"
  fi
  nvidia-smi -L
)
```

Confirm that the hostname belongs to the allocation's `NodeList` and that the job lists the requested CPU, memory, and GPU resources. `SLURM_JOB_ID` alone does not prove that the shell is on a compute node. `nvidia-smi -L` checks GPU discovery; the scheduler's allocation and GPU mask determine which GPUs your work may use. Do not overwrite that mask.

### 4d. Check connectivity and architecture

Confirm that the compute node can reach the services Codex needs. Use a Codex executable built for the node's architecture: the `compute` example above targets AMD64, while `grace` targets ARM64.

```bash
(
  uname -m
  command -v codex
  codex --version
  curl -I --connect-timeout 10 --max-time 20 https://chatgpt.com
  curl -I --connect-timeout 10 --max-time 20 https://auth.openai.com
)
```

Expect `x86_64` on AMD64 or `aarch64` on ARM64. A successful `codex --version` checks that the CLI can execute on this host. The curl commands check DNS, TLS, and HTTP reachability to the listed services; an HTTP error such as 403 still means an HTTP response was received, but does not establish that Codex authentication or model requests will work. Resolve connection failures before continuing. Additional services may be needed for API-key use, plugins, or a custom provider.

## 5. Prepare the working Codex home on local scratch

Choose **one** of two paths for each allocation:

- **Option A — New:** start with an empty Codex home on `/lscratch`. Use this to abandon corrupted history and begin fresh. No copy from PanFS is performed; the old shared home and any login-node Codex sessions remain untouched.
- **Option B — Restore:** copy the latest **completed, quiescent** Codex checkpoint (or a shared home whose writers have been cleanly stopped) to `/lscratch`. Use this to continue previously saved sessions. Do **not** copy live SQLite databases as an ordinary `rsync` snapshot.

Both options use the same private scratch-directory creation (**5b**), a single verification suite (**5d**), and the same activation (**5e–5f**). Choose Option A for your current fresh start; in later allocations, restore the clean checkpoint created in section 8 using Option B.

### 5a. Choose the initialization mode and, if restoring, stop source writers

Run **one** of the following commands in your compute-node shell. This setting is used by the verification suite in 5d.

**Option A — New, no source shutdown required:**

```bash
CODEX_INIT_MODE=new
```

The original `~/.codex` on PanFS may remain in use by a different Codex session. That session is independent of the new scratch home; its state will not be copied or synchronized.

**Option B — Restore from a saved home or completed checkpoint:**

```bash
CODEX_INIT_MODE=restore
# Prefer a completed checkpoint from section 8. For an initial migration,
# this can be the original home ONLY after all its writers are stopped.
CODEX_SAVED_HOME=/explore/nobackup/people/$USER/.codex
```

Before Option B copies a *live shared home*, exit every interactive Codex client and background server that writes to that source, including on login nodes and other compute nodes. Check the relevant hosts (this check is host-local):

```bash
ps -u "$USER" -o pid,ppid,args | grep '[c]odex' || true
```

Where appropriate, use the manager on the host running the daemon:

```bash
env CODEX_HOME="$CODEX_SAVED_HOME" codex app-server daemon stop
```

A `notRunning` result only describes the managed daemon for that context; it does not prove that all other writers stopped. Never delete a database, WAL file, socket, or lock to force shutdown. If an app-server is not managed by the daemon manager, close its owning process cleanly. A completed, immutable checkpoint needs no shutdown, but must never have been opened as a live Codex home. Keep the source quiescent until the copy finishes. If you cannot ensure this, select Option A instead.

### 5b. Create a private working home (both options)

In the Slurm **compute-node shell**, use the assigned job scratch location confirmed in step 2. On `gpu012`, the user-specific root has been `/lscratch/$USER` and `df -Th` identified XFS; do not assume the same scratch rules on another cluster.

```bash
umask 077
CODEX_SCRATCH_ROOT="/lscratch/$USER"
if [ ! -d "$CODEX_SCRATCH_ROOT" ] || [ -z "${SLURM_JOB_ID:-}" ]; then
  echo "ERROR: Require an assigned scratch directory and active Slurm job" >&2
else
  CODEX_WORK_HOME="$(mktemp -d \
    "$CODEX_SCRATCH_ROOT/codex-home.${SLURM_JOB_ID}.XXXXXX")"
  printf 'Mode: %s\nWorking home: %s\n' "$CODEX_INIT_MODE" "$CODEX_WORK_HOME"
  ls -ld "$CODEX_WORK_HOME"
  df -Th "$CODEX_WORK_HOME"
fi
```

The trailing `XXXXXX` in the `mktemp` template is required. The new directory is private to your user. **Do not reuse the old scratch copy containing corrupted databases** when selecting Option A.

### 5c. Initialize the working home (choose one option)

**Option A — New:** The directory created in 5b is already empty; **do not** copy the old `.codex` home, any databases, WAL/SHM sidecars, session files, or history files. Continue directly to 5d.

**Option B — Restore:** Copy the **contents** of the saved home into the new scratch directory, after verifying that the source is no longer being written. This retains databases, session rollouts, configuration, and credentials. Only transient runtime state is excluded.

```bash
(
  set -euo pipefail
  : "${CODEX_SAVED_HOME:?Set CODEX_SAVED_HOME for restore mode}"
  : "${CODEX_WORK_HOME:?Create CODEX_WORK_HOME in step 5b}"
  test -d "$CODEX_SAVED_HOME"
  test -d "$CODEX_WORK_HOME"
  printf 'Copying from: %s\nCopying to:   %s\n' \
    "$CODEX_SAVED_HOME" "$CODEX_WORK_HOME"
  rsync -a --chmod=go-rwx \
    --exclude='/app-server-daemon/' \
    --exclude='/app-server-control/' \
    --exclude='/thread-writer-locks/' \
    --exclude='/tui-thread-reference-capabilities/' \
    --exclude='/tmp/' \
    --exclude='/.tmp/' \
    --exclude='/*.lock' \
    --exclude='*.sock' \
    "$CODEX_SAVED_HOME/" "$CODEX_WORK_HOME/"
)
```

Do not continue if `rsync` fails. If the source was copied during an active SQLite write, passing file-level checks cannot certify consistency; obtain a clean, quiescent snapshot instead. For a later allocation, point `CODEX_SAVED_HOME` to the latest completed checkpoint from section 8, not to the original corrupted shared home.

### 5d. Verify the working home (one command for either option)

Run the **single parenthesized Bash command below** from your project directory or another directory outside both Codex homes. It generates five private `.txt` reports in `$PWD`. The suite is non-destructive: it does not repair, delete, copy, or checkpoint data. SQLite read-only checks may update transient SHM files in the scratch copy.

**Policy:** With `CODEX_INIT_MODE=new`, verify the private empty directory, but skip databases, sessions, and source divergence because nothing has been initialized. With `CODEX_INIT_MODE=restore`, validate copied SQLite and JSONL sessions. The source may intentionally diverge **after** the copy, so its checksum audit is informational only; source divergence cannot make 5d fail. Invalid copied SQLite, malformed sessions, or structural failures still fail the restore. Neither a clean audit nor a passed database check proves that an actively written source was copied consistently.

```bash
(
  set -uo pipefail
  umask 077

  : "${CODEX_INIT_MODE:?Set CODEX_INIT_MODE=new or restore in 5a}"
  : "${CODEX_WORK_HOME:?Create CODEX_WORK_HOME in 5b}"
  [[ "$CODEX_INIT_MODE" == new || "$CODEX_INIT_MODE" == restore ]] || {
    echo "ERROR: CODEX_INIT_MODE must be new or restore" >&2; exit 1;
  }

  DST="$(realpath -e "$CODEX_WORK_HOME")" || exit 1
  OUT="$(pwd -P)"
  SRC=""
  if [[ "$CODEX_INIT_MODE" == restore ]]; then
    : "${CODEX_SAVED_HOME:?Set CODEX_SAVED_HOME for restore mode}"
    SRC="$(realpath -e "$CODEX_SAVED_HOME")" || exit 1
    [[ -d "$SRC" && "$SRC" != "$DST" ]] || {
      echo "ERROR: Invalid or identical source/destination" >&2; exit 1;
    }
  fi
  [[ -d "$DST" ]] || { echo "ERROR: Working home is not a directory" >&2; exit 1; }
  if [[ "$OUT" == "$DST" || "$OUT" == "$DST/"* ||
        ( -n "$SRC" && ( "$OUT" == "$SRC" || "$OUT" == "$SRC/"* ) ) ]]; then
    echo "ERROR: Run outside both Codex homes" >&2; exit 1
  fi

  # 1. STRUCTURE AND PERMISSIONS
  (
    fail=0
    echo "=== Mode: $CODEX_INIT_MODE ==="
    printf 'Source: %s\nDestination: %s\n' "${SRC:-none}" "$DST"
    if [[ "$CODEX_INIT_MODE" == new ]]; then
      if [[ -z "$(find "$DST" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
        echo "PASS: New Codex home is empty"
      else
        echo "FAIL: New Codex home is not empty; create a new directory"
        fail=1
      fi
    else
      for item in config.toml sessions; do
        if [[ -e "$DST/$item" ]]; then
          echo "PASS: $item exists"
        else
          echo "FAIL: Missing expected $item"
          fail=1
        fi
      done
    fi

    echo; echo "=== Ownership and permissions ==="
    if [[ "$(stat -c %u "$DST")" == "$(id -u)" ]]; then
      echo "PASS: Working home is owned by current user"
    else
      echo "FAIL: Working home owner mismatch"; fail=1
    fi
    if insecure=$(find "$DST" \( -type f -o -type d \) -perm /077 -print); then
      if [[ -z "$insecure" ]]; then
        echo "PASS: No group/other access"
      else
        printf 'FAIL: Group/other permissions:\n%s\n' "$insecure"
        fail=1
      fi
    else
      echo "FAIL: Permission scan failed"; fail=1
    fi

    echo; echo "=== Transient runtime state ==="
    for dir in app-server-daemon app-server-control \
               thread-writer-locks tui-thread-reference-capabilities; do
      if [[ -e "$DST/$dir" ]]; then
        echo "FAIL: Transient directory exists: $dir"; fail=1
      fi
    done
    if unexpected=$(find "$DST" \( -type s -o -name '*.sock' -o -name '*.lock' \) \
      ! -path "$DST/packages/app-server-daemon/install.lock" \
      ! -path "$DST/packages/standalone/install.lock" -print); then
      if [[ -z "$unexpected" ]]; then
        echo "PASS: No unexpected sockets/locks"
      else
        printf 'FAIL: Unexpected sockets/locks:\n%s\n' "$unexpected"
        fail=1
      fi
    else
      echo "FAIL: Runtime-file scan failed"; fail=1
    fi

    echo; echo "=== Symlinks (inspect targets in 5e) ==="
    find "$DST" -type l -printf '%p -> %l\n' || fail=1
    echo; echo "=== Filesystem and size ==="
    df -Th "$DST" || fail=1
    du -sh "$DST" || fail=1
    fs_type=$(df -T "$DST" | awk 'END {print $2}')
    case "$fs_type" in
      panfs|nfs|nfs4|lustre)
        echo "FAIL: Working home appears to be on network filesystem: $fs_type"
        fail=1 ;;
      *) echo "INFO: Working filesystem type: $fs_type" ;;
    esac
    echo
    (( fail )) && echo "FAIL: Structure" || echo "PASS: Structure"
    exit "$fail"
  ) > "$OUT/codex_5d_structure.txt" 2>&1
  structure_rc=$?

  # 2. SOURCE DIVERGENCE (INFORMATION ONLY)
  if [[ "$CODEX_INIT_MODE" == restore ]]; then
    (
      echo "=== Informational source/scratch divergence ==="
      echo "Differences after copying are permitted; not a failure gate."
      echo "SQLite -shm excluded; -wal included."
      rsync -a --chmod=go-rwx --dry-run --checksum --itemize-changes \
        --exclude='/app-server-daemon/' \
        --exclude='/app-server-control/' \
        --exclude='/thread-writer-locks/' \
        --exclude='/tui-thread-reference-capabilities/' \
        --exclude='/tmp/' --exclude='/.tmp/' \
        --exclude='/*.lock' --exclude='*.sock' \
        --exclude='*.sqlite-shm' \
        "$SRC/" "$DST/"
    ) > "$OUT/codex_5d_checksum.txt" 2>&1
    audit_rc=$?
  else
    echo "SKIP: New home has no saved source to compare." \
      > "$OUT/codex_5d_checksum.txt"
    audit_rc=0
  fi

  # 3. SQLITE INTEGRITY (RESTORE ONLY)
  if [[ "$CODEX_INIT_MODE" == restore ]]; then
    python3 - "$DST" > "$OUT/codex_5d_sqlite.txt" 2>&1 <<'PY'
import sqlite3
import sys
from pathlib import Path

home = Path(sys.argv[1])
databases = sorted(home.glob("*.sqlite"))
failed = []
print("=== SQLite integrity (scratch only) ===", flush=True)
if not databases:
    sys.exit("FAIL: No top-level SQLite databases found")
for db in databases:
    print(f"\nDatabase: {db.name}", flush=True)
    try:
        with db.open("rb") as stream:
            header = stream.read(16)
        if header != b"SQLite format 3\x00":
            print(f"FAIL: Invalid SQLite header: {header.hex(' ')}")
            failed.append(db.name)
            continue
        with sqlite3.connect(db.as_uri() + "?mode=ro", uri=True, timeout=5) as conn:
            result = [row[0] for row in conn.execute("PRAGMA integrity_check")]
        if result == ["ok"]:
            print("PASS: PRAGMA integrity_check")
        else:
            print(f"FAIL: PRAGMA integrity_check: {result[:10]}")
            failed.append(db.name)
    except (sqlite3.Error, OSError) as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}")
        failed.append(db.name)
print("\n=== WAL/SHM inventory ===")
for pattern in ("*.sqlite-wal", "*.sqlite-shm"):
    for path in sorted(home.glob(pattern)):
        print(f"{path.name}: {path.stat().st_size} bytes")
print(f"Checked: {len(databases)} | Failed: {len(failed)}")
for name in failed:
    print(f"FAILED DATABASE: {name}")
sys.exit(1 if failed else 0)
PY
    sqlite_rc=$?
  else
    echo "SKIP: Fresh home has no databases yet; validate after initialization." \
      > "$OUT/codex_5d_sqlite.txt"
    sqlite_rc=0
  fi

  # 4. JSONL SESSION SYNTAX (RESTORE ONLY)
  if [[ "$CODEX_INIT_MODE" == restore ]]; then
    python3 - "$DST" > "$OUT/codex_5d_sessions.txt" 2>&1 <<'PY'
import json
import sys
from pathlib import Path

home = Path(sys.argv[1])
sessions = sorted((home / "sessions").rglob("*.jsonl"))
valid = invalid = records = 0
print("=== JSONL sessions (scratch only) ===", flush=True)
for path in sessions:
    try:
        count = 0
        with path.open("r", encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"line {line_number}: {exc.msg}") from exc
                count += 1
        if not count:
            raise ValueError("No JSON records")
        print(f"PASS: {path.name} ({count} records)")
        valid += 1
        records += count
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"FAIL: {path.name}: {exc}")
        invalid += 1
print(f"Total: {len(sessions)} | Valid: {valid} | Invalid: {invalid} | Records: {records}")
print("NOTE: Syntax does not establish full history or resumability.")
sys.exit(1 if invalid or not sessions else 0)
PY
    sessions_rc=$?
  else
    echo "SKIP: Fresh home has no conversations yet." \
      > "$OUT/codex_5d_sessions.txt"
    sessions_rc=0
  fi

  # 5. SUMMARY
  {
    echo "=== Codex Step 5d Verification Summary ==="
    date
    echo "Mode: $CODEX_INIT_MODE"
    printf 'Structure:  %s\n' "$([[ $structure_rc -eq 0 ]] && echo PASS || echo FAIL)"
    if [[ "$CODEX_INIT_MODE" == restore ]]; then
      (( audit_rc == 0 )) && \
        echo "Divergence: INFO (no fail gate)" || \
        echo "Divergence: WARNING (audit command failed; no fail gate)"
      printf 'SQLite:     %s\n' "$([[ $sqlite_rc -eq 0 ]] && echo PASS || echo FAIL)"
      printf 'Sessions:   %s\n' "$([[ $sessions_rc -eq 0 ]] && echo PASS || echo FAIL)"
    else
      echo "Divergence: SKIP (new)"
      echo "SQLite:     SKIP (not initialized)"
      echo "Sessions:   SKIP (not initialized)"
    fi
    echo "Reports: $OUT/codex_5d_*.txt"
    echo "NEXT: 5e must inspect config and symlink targets."
    if (( structure_rc || sqlite_rc || sessions_rc )); then
      echo "OVERALL: FAIL - Investigate mandatory failures before running Codex."
    else
      echo "OVERALL: PASS - Proceed to 5e (fresh homes still need post-start checks)."
    fi
  } | tee "$OUT/codex_5d_summary.txt"

  (( structure_rc == 0 && sqlite_rc == 0 && sessions_rc == 0 ))
)
```

Read `codex_5d_summary.txt` first. In Option A, the expected result is **structure PASS** and **database/session/divergence SKIP**. In Option B, any invalid database (including the previously observed `thread_history_1.sqlite`) remains a blocker; **do not** relabel corruption as an acceptable divergence. If you want a clean restart, use Option A rather than repairing your old home.

### 5e. Keep all live state on local scratch (both options)

Before launching Codex, inspect configuration and environment for paths that would redirect database, history, logs, or caches back to PanFS. Option A should be empty at this point; Option B may contain a copied `config.toml` with absolute paths or symlinks.

```bash
(
  printf 'Working home: %s\n' "$CODEX_WORK_HOME"
  if [ -f "$CODEX_WORK_HOME/config.toml" ]; then
    grep -nE 'sqlite_home|/panfs|/explore/nobackup|log_dir' \
      "$CODEX_WORK_HOME/config.toml" || true
  fi
  find "$CODEX_WORK_HOME" -type l -printf '%p -> %l\n'
  df -Th "$CODEX_WORK_HOME"
)
```

Inspect any absolute symlink targets; package-version symlinks that resolve within scratch are acceptable. Change only the *working copy* of configuration when needed. For projects and intentional code paths, references to PanFS are expected; live Codex state must remain on `/lscratch`. Do not change Unix `HOME` or the login-node `~/.codex` symlink.

### 5f. Select the working home (both options)

Run in the **same compute-node shell** where you'll start Codex:

```bash
export CODEX_HOME="$CODEX_WORK_HOME"
export CODEX_SQLITE_HOME="$CODEX_WORK_HOME"
printf 'CODEX_HOME=%s\nCODEX_SQLITE_HOME=%s\n' \
  "$CODEX_HOME" "$CODEX_SQLITE_HOME"
```

The `CODEX_HOME` path selects this allocation's working state. Keep the variables specific to this allocation rather than placing an ephemeral path in `.bashrc`. If your Codex version honors `CODEX_SQLITE_HOME`, the second export also points it to scratch; inspect any `sqlite_home` override in `config.toml` in 5e instead of relying on the variable alone. An entirely new home will require fresh authentication or a selective, carefully reviewed copy of authentication/configuration files—**never copy old databases or history just to avoid logging in**.

### 5g. Keep saved and working histories independent

You may operate a separate Codex session on a login node using the original PanFS home while using a **different** scratch home on the compute node. They are two independent histories: changes will **not** synchronize. Never run simultaneous writers against the **same** Codex home, and never merge live homes or treat a changing one as a completed checkpoint. Keeping the original login-node session active does not make it safe from PanFS-related SQLite risks; the scratch workflow avoids those risks for the new instance.


## 6. Run Codex in your project folder

### 6a. Open the project and start or resume Codex

Change to the desired repository or working directory in shared nobackup storage. The `CODEX_HOME` export from 5f selects the private scratch home.

**Option A (new):** Sign in if needed, then start a new conversation. This initializes fresh databases and session files inside the scratch home:

```bash
cd /explore/nobackup/people/$USER/agentic_template/agentic_template
codex login
codex --no-daemon
```

Use `codex login --help` for headless/device-auth alternatives supported by your installation. After exiting the initial session cleanly, run `codex doctor --summary` with the same `CODEX_HOME` to check the initialized state. If Doctor flags a problem, investigate before checkpointing.

**Option B (restore):** Open the resume picker from the project directory:

```bash
cd /explore/nobackup/people/$USER/agentic_template/agentic_template
codex --no-daemon resume --all
```

### 6b. Start a new conversation or select a session ID

With a restored home, the resume picker lets you choose an existing conversation. To start a separate new conversation at any time, omit `resume --all`. To resume a recorded session, use its session ID:

```bash
codex --no-daemon resume SESSION_ID
```

### 6c. Keep the home and project locations consistent

Use the same scratch home for every Codex invocation during this allocation. `--no-daemon` keeps the process lifecycle explicit; it does not itself make SQLite safe on shared storage. Do not use an existing login-node Codex process to test the scratch home.

Codex's home and its project directory are separate. Project edits remain in your shared repository, even though conversation state is being written locally.

## 7. Disconnect and reconnect during the allocation

### 7a. Detach without ending the allocation

To leave temporarily, press **Ctrl-a, then d** to detach from the login-node screen session. Do not type `exit` in the allocation shell merely to disconnect; ending that shell can release the allocation.

### 7b. Reconnect to screen

To return, SSH to the same login node and run:

```bash
screen -r codex-allocation
```

If a dropped connection leaves the session marked as attached, detach the previous terminal and reattach with:

```bash
screen -d -r codex-allocation
```

To list your screen sessions on that login node, run `screen -ls`.

### 7c. Continue the running session

You should return to the existing compute-node shell and Codex process. This is reattaching to a running session, rather than restoring a saved conversation. You do not need a second screen session on the compute node for this arrangement.

## 8. Save a checkpoint before the allocation ends

### 8a. Schedule time for a checkpoint

Leave enough time before the Slurm time limit to exit Codex and copy its state. For a long allocation, repeat this checkpoint process periodically.

### 8b. Record the session and project

Before exiting Codex, record the conversation's session ID and project directory somewhere in shared nobackup storage, outside the scratch home. Keep this record with the completed checkpoint so you can select the same conversation in the next allocation.

### 8c. Stop Codex cleanly

Exit Codex cleanly. Ensure no Codex process or daemon is writing the scratch home.

### 8d. Choose a new checkpoint destination

Choose a new, private, dated checkpoint directory in `/explore/nobackup/people/ajkerr1`, outside the working home and outside any source directory being copied. Do not start copying yet.

### 8e. Preserve SQLite sidecar files

Do not copy open SQLite databases using ordinary file-copy commands. Include database sidecar files if any remain after clean shutdown; do not delete WAL files as a cleanup shortcut.

### 8f. Copy and verify the incomplete checkpoint

Copy the complete working home into the new destination directory, marked as incomplete. Preserve hidden files, permissions, and any remaining database sidecar files; omit transient sockets and process locks. Check that the copy completed successfully and contains the expected databases and session files.

### 8g. Mark the checkpoint complete

Only after successful verification, mark the new checkpoint as complete and record it as the latest checkpoint. Keep the previous completed checkpoint until the new one has successfully resumed.

### 8h. Manage checkpoint storage

A full checkpoint currently requires approximately 6 GB, so retaining several copies can consume substantial nobackup space. Retain a small number of verified checkpoints and retire older ones deliberately. Do not overwrite your only known-good checkpoint during a copy.

### 8i. Continue working if needed

If you want to continue working after checkpointing, restart Codex against the same scratch home. Treat the completed checkpoint as read-only saved state. Before ending the allocation, repeat the checkpoint process to save any further conversation changes and stop Codex again.

## 9. End the allocation

### 9a. Understand what termination can lose

GNU Screen cannot preserve a compute process after Slurm terminates its allocation. A shutdown hook can help automate normal checkpointing, but cannot guarantee a save after a node failure or forced kill. Conversation changes since the last completed checkpoint may be lost in those cases. Project files already written to shared nobackup remain there.

### 9b. Release the allocation after saving

After the checkpoint succeeds, exit the compute-node shell and finish the allocation. Expect the job's scratch contents to be erased.

## 10. Resume in the next allocation

### 10a. Restore the latest checkpoint (or deliberately start anew)

To continue previous conversations after *either* Option A or B, use **Option B** in section 5 with `CODEX_SAVED_HOME` pointing to the latest verified checkpoint from section 8. Restore it to the new node's scratch directory and resume the recorded session ID from the recorded project directory. To discard prior sessions again, select **Option A** instead and start empty.

### 10b. Keep a single conversation history across nodes

The compute node and scratch pathname can change between allocations. Continuity comes from restoring the same complete saved state, using a compatible Codex version, and selecting the intended conversation. An active login-node PanFS home and a compute-node scratch home are **separate branches**, not a shared synchronized history. Do not merge independently modified Codex homes from different nodes.

## References

- [Slurm allocation behavior](https://slurm.schedmd.com/salloc.html)
- [Slurm job steps](https://slurm.schedmd.com/srun.html)
- [GNU Screen manual](https://www.gnu.org/software/screen/manual/screen.html)
- [Codex configuration reference, including sqlite_home](https://learn.chatgpt.com/docs/config-file/config-reference)
- [SQLite network filesystem considerations](https://www.sqlite.org/useovernet.html)
- [SQLite WAL requirements](https://www.sqlite.org/wal.html)

This process uses local live databases because your shared destination is PanFS and you have already observed database corruption. It does not assume that Codex's experimental NFS migration command applies to PanFS.
