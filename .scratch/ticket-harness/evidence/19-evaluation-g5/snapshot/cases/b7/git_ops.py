from pathlib import Path

def validate(git, expected_branch, base):
    def checked(*args):
        result = git(list(args))
        if result.returncode:
            raise ValueError("Git preflight failed: " + " ".join(args))
        return result.stdout

    root = Path(checked("rev-parse", "--show-toplevel").removesuffix("\n")).resolve()
    ref = checked("symbolic-ref", "HEAD").removesuffix("\n")
    if not ref.startswith("refs/heads/"):
        raise ValueError("HEAD is not a local branch")
    branch = ref.removeprefix("refs/heads/")
    if branch != expected_branch:
        raise ValueError("unexpected branch")
    if checked("status", "--porcelain", "--untracked-files=all"):
        raise ValueError("dirty worktree")
    checked("rev-parse", "--verify", base + "^{commit}")
    checked("merge-base", "--is-ancestor", base, "HEAD")
    return root, branch
