import os
import subprocess
from git_ops import validate

def preflight(checkout, expected_branch, base):
    def git(args):
        result = subprocess.run(["git", "-C", os.fspath(checkout), *args],
                                capture_output=True, check=False)
        return subprocess.CompletedProcess(result.args, result.returncode,
                                           os.fsdecode(result.stdout),
                                           os.fsdecode(result.stderr))
    return validate(git, expected_branch, base)
