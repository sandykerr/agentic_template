import subprocess
from git_ops import validate

def preflight(checkout, expected_branch, base):
    def git(args):
        return subprocess.run(["git", "-C", str(checkout), *args],
                              capture_output=True, text=True, check=False)
    return validate(git, expected_branch, base)
