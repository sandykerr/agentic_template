from pathlib import Path

def validate(git, expected_branch, base):
    def checked(*args):
        result = git(list(args))
        if result.returncode:
            raise ValueError("Git preflight failed: " + " ".join(args))
        return result.stdout.strip()

    root = Path(checked("rev-parse", "--show-toplevel")).resolve()
    branch = checked("symbolic-ref", "--short", "HEAD")
    if branch != expected_branch:
        raise ValueError("unexpected branch")
    if checked("status", "--porcelain", "--untracked-files=all"):
        raise ValueError("dirty worktree")
    checked("rev-parse", "--verify", base + "^{commit}")
    checked("merge-base", "--is-ancestor", base, "HEAD")
    return root, branch
