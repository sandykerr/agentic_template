"""Git ownership: detached worktrees, submission capture, and candidate promotion."""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from ticket_harness.records import GateFailure

IDENTITY = ["-c", "user.name=Ticket Harness", "-c", "user.email=harness@example.invalid"]


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args], capture_output=True, text=True, check=False
    )
    if result.returncode:
        diagnostic = "\n".join(
            part.strip() for part in (result.stderr, result.stdout) if part.strip()
        )
        raise GateFailure(f"git {' '.join(args)}: {diagnostic}")
    return result.stdout.strip()


def worktree(repository: Path, path: Path, revision: str) -> Path:
    git(repository, "worktree", "add", "--detach", str(path), revision)
    return path


def require_direct_branches(repository: Path, *branches: str) -> None:
    """Named integration destinations must not alias another branch."""
    for branch in branches:
        ref = f"refs/heads/{branch}"
        git(repository, "check-ref-format", ref)
        if git(repository, "for-each-ref", "--format=%(symref)", ref):
            raise GateFailure(f"Branch {branch} must not be symbolic")


def carry_changes(previous: Path, source: Path) -> None:
    """Copy current working contents without altering the rejected tree or Git identity."""
    for path in source.iterdir():
        if path.name == ".git":
            continue
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()
    for path in previous.iterdir():
        if path.name == ".git":
            continue
        target = source / path.name
        if path.is_dir() and not path.is_symlink():
            shutil.copytree(path, target, symlinks=True)
        else:
            shutil.copy2(path, target, follow_symlinks=False)


def require_unchanged(source: Path, revision: str) -> None:
    flags = git(source, "ls-files", "-v", "-z").split("\0")
    if any(entry and (entry[0].islower() or entry[0] == "S") for entry in flags):
        raise GateFailure(f"Verified source changed index visibility flags at {source}")
    if git(source, "rev-parse", "HEAD") != revision or git(source, "status", "--porcelain"):
        raise GateFailure(f"Verified source changed at {source}")


def capture(
    source: Path, start: str, ticket: str, base: str | None = None
) -> tuple[str, list[str]]:
    if git(source, "rev-parse", "HEAD") != start:
        raise GateFailure("Implementation changed HEAD; the harness owns submission commits")
    git(source, "add", "--all")
    if base is None and not git(source, "diff", "--cached", "--name-only"):
        raise GateFailure("Implementation submitted no changes")
    git(source, *IDENTITY, "commit", "--allow-empty", "-m", f"Implement ticket {ticket}")
    revision = git(source, "rev-parse", "HEAD")
    # NUL delimiters preserve filenames containing whitespace or newlines.
    changed = git(source, "diff", "--name-only", "-z", base or start, revision).split("\0")
    changed = [path for path in changed if path]
    return revision, changed


def candidate(repository: Path, source: Path, base: str, submission: str) -> str:
    worktree(repository, source, base)
    git(source, *IDENTITY, "merge", "--no-ff", "-m", "Verified ticket candidate", submission)
    return git(source, "rev-parse", "HEAD")


def require_reviewed_candidate(source: Path, revision: str, base: str, submission: str) -> None:
    # In this sequential slice submission descends directly from the starting base.
    # Any different merge tree introduces source that neither reviewer approved.
    parents = git(source, "show", "-s", "--format=%P", revision).split()
    if parents != [base, submission] or git(source, "rev-parse", f"{revision}^{{tree}}") != git(
        source, "rev-parse", f"{submission}^{{tree}}"
    ):
        raise GateFailure(
            f"Candidate {revision} differs from reviewed source; renewed review required"
        )
    require_unchanged(source, revision)


def promote(
    repository: Path,
    branch: str,
    revision: str,
    previous: str,
    development: str | None = None,
) -> None:
    require_direct_branches(repository, branch, *((development,) if development else ()))
    refs: dict[str, tuple[str | None, str]] = {branch: (revision, previous)}
    if development:
        # Development may legitimately have advanced during ticket work. Protect
        # its current identity/topology at this write, rather than pinning the
        # starting development commit used by a later milestone review.
        refs[development] = (None, git(repository, "rev-parse", f"refs/heads/{development}"))
    _update_direct_branches(repository, refs, "git update-ref rejected")


def _transaction_exchange(process: subprocess.Popen[bytes], command: str, expected: bytes) -> None:
    """Read Git's protocol acknowledgement without buffering or stderr deadlocks."""
    assert process.stdin is not None and process.stdout is not None
    process.stdin.write(command.encode())
    process.stdin.flush()
    observed = b""
    while observed != expected:
        chunk = os.read(process.stdout.fileno(), 4096)
        observed += chunk
        if not chunk or not expected.startswith(observed):
            raise GateFailure("Git ref transaction rejected: " + observed.decode(errors="replace"))


def _update_direct_branches(
    repository: Path, refs: dict[str, tuple[str | None, str]], failure: str
) -> None:
    """Hold all destination locks while validating topology, then commit together.

    A verify entry holds a read-only ref alongside updates. OID verification with
    no-deref alone still accepts same-OID symbolic refs; validate topology after
    prepare, when ordinary Git writers cannot replace any of these names.
    """
    commands = "start\n"
    for branch, (revision, previous) in refs.items():
        commands += "option no-deref\n"
        commands += (
            f"update refs/heads/{branch} {revision} {previous}\n"
            if revision is not None
            else f"verify refs/heads/{branch} {previous}\n"
        )
    with tempfile.TemporaryFile() as diagnostic:
        process = subprocess.Popen(
            [
                "git",
                "-C",
                str(repository),
                "-c",
                "core.hooksPath=/dev/null",
                "update-ref",
                "--stdin",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=diagnostic,
            bufsize=0,
        )
        try:
            _transaction_exchange(process, commands + "prepare\n", b"start: ok\nprepare: ok\n")
            require_direct_branches(repository, *refs)
            _transaction_exchange(process, "commit\n", b"commit: ok\n")
            assert process.stdin is not None
            process.stdin.close()
            process.stdin = None
            process.wait()
            if process.returncode:
                raise GateFailure("Git ref transaction failed")
        except (GateFailure, OSError) as error:
            diagnostic.seek(0)
            detail = diagnostic.read().decode(errors="replace").strip()
            raise GateFailure(f"{failure}: {error}" + (f"\n{detail}" if detail else "")) from error
        finally:
            # An uncommitted transaction is explicitly aborted; EOF is Git's
            # fallback abort if it already rejected input or the pipe is broken.
            try:
                process.communicate(
                    input=b"abort\n" if process.poll() is None else None, timeout=10
                )
            except (OSError, subprocess.TimeoutExpired):
                process.kill()
                process.communicate()


def require_clean_milestone_candidate(
    repository: Path, source: Path, revision: str, base: str, feature: str
) -> None:
    """Compare with a plain Git merge; resolution source needs fresh approval.

    An isolated bare Git directory avoids target hooks, config and info attributes.
    Empty attributes disable custom/union drivers and normalization when computing
    the comparison tree, so conflict resolutions cannot inherit ticket approvals.
    The real candidate remains available for diagnosis, including resolved source.
    """
    empty = git(repository, "hash-object", "-w", "-t", "tree", "/dev/null")
    objects = git(repository, "rev-parse", "--path-format=absolute", "--git-path", "objects")
    object_format = git(repository, "rev-parse", "--show-object-format")
    with tempfile.TemporaryDirectory(prefix="ticket-harness-merge-") as directory:
        isolated = Path(directory)
        git(isolated, "init", "--bare", "--template=", f"--object-format={object_format}")
        environment = {
            key: value for key, value in os.environ.items() if not key.startswith("GIT_")
        }
        environment.update(
            GIT_OBJECT_DIRECTORY=objects,
            GIT_CONFIG_GLOBAL="/dev/null",
            GIT_CONFIG_NOSYSTEM="1",
            GIT_ATTR_NOSYSTEM="1",
        )
        result = subprocess.run(
            [
                "git",
                f"--git-dir={isolated}",
                f"--attr-source={empty}",
                "-c",
                "core.attributesFile=/dev/null",
                "merge-tree",
                "--write-tree",
                base,
                feature,
            ],
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
    if result.returncode:
        raise GateFailure(
            "Milestone merge needs resolution; renewed checks and reviews required: "
            + result.stdout.strip()
            + result.stderr.strip()
        )
    expected_tree = result.stdout.splitlines()[0]
    parents = git(source, "show", "-s", "--format=%P", revision).split()
    if git(source, "rev-parse", f"{revision}^{{tree}}") != expected_tree or (
        revision != base and parents != [base, feature]
    ):
        raise GateFailure(
            "Milestone candidate differs from clean merge; renewed checks and reviews required"
        )
    require_unchanged(source, revision)


def promote_milestone(
    repository: Path,
    feature: str,
    development: str,
    revision: str,
    feature_previous: str,
    development_previous: str,
) -> None:
    """Compare and advance both branches atomically, preserving caller worktrees."""
    require_direct_branches(repository, feature, development)
    checked_out = git(repository, "worktree", "list", "--porcelain").splitlines()
    for branch in (feature, development):
        if f"branch refs/heads/{branch}" in checked_out:
            raise GateFailure(f"Branch {branch} must not be checked out for promotion")
    _update_direct_branches(
        repository,
        {development: (revision, development_previous), feature: (revision, feature_previous)},
        "Milestone branches changed externally; promotion rejected",
    )
