"""Git ownership: detached worktrees, submission capture, and candidate promotion."""

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


def require_unchanged(source: Path, revision: str) -> None:
    if git(source, "rev-parse", "HEAD") != revision or git(source, "status", "--porcelain"):
        raise GateFailure(f"Verified source changed at {source}")


def capture(source: Path, base: str, ticket: str) -> tuple[str, list[str]]:
    if git(source, "rev-parse", "HEAD") != base:
        raise GateFailure("Implementation changed HEAD; the harness owns submission commits")
    git(source, "add", "--all")
    if not git(source, "diff", "--cached", "--name-only"):
        raise GateFailure("Implementation submitted no changes")
    git(source, *IDENTITY, "commit", "-m", f"Implement ticket {ticket}")
    revision = git(source, "rev-parse", "HEAD")
    # NUL delimiters preserve filenames containing whitespace or newlines.
    changed = git(source, "diff", "--name-only", "-z", base, revision).rstrip("\0").split("\0")
    return revision, changed


def candidate(repository: Path, source: Path, base: str, submission: str) -> str:
    worktree(repository, source, base)
    git(source, *IDENTITY, "merge", "--no-ff", "-m", "Verified ticket candidate", submission)
    return git(source, "rev-parse", "HEAD")


def promote(repository: Path, branch: str, revision: str, previous: str) -> None:
    git(repository, "update-ref", f"refs/heads/{branch}", revision, previous)
