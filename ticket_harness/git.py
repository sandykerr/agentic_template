"""Git ownership: detached worktrees, submission capture, and candidate promotion."""

import shutil
import subprocess
from pathlib import Path

from ticket_harness.records import GateFailure

IDENTITY = ["-c", "user.name=Ticket Harness", "-c", "user.email=harness@example.invalid"]


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args], capture_output=True, text=True, check=False
    )
    if result.returncode:
        raise GateFailure(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()


def worktree(repository: Path, path: Path, revision: str) -> Path:
    git(repository, "worktree", "add", "--detach", str(path), revision)
    return path


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


def promote(repository: Path, branch: str, revision: str, previous: str) -> None:
    # No user code may run between final validation and the atomic ref update.
    git(
        repository,
        "-c",
        "core.hooksPath=/dev/null",
        "update-ref",
        f"refs/heads/{branch}",
        revision,
        previous,
    )
