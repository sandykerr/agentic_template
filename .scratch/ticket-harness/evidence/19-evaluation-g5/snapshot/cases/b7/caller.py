import os
import subprocess
from git_ops import validate

def preflight(checkout, expected_branch, base):
    local = subprocess.run(["git", "rev-parse", "--local-env-vars"],
                           capture_output=True, check=False)
    if local.returncode:
        raise ValueError("Git environment discovery failed")
    env = os.environ.copy()
    for name in os.fsdecode(local.stdout).splitlines():
        env.pop(name, None)
    def git(args):
        result = subprocess.run(["git", "--no-optional-locks", "-C", os.fspath(checkout), *args],
                                capture_output=True, check=False, env=env)
        return subprocess.CompletedProcess(result.args, result.returncode,
                                           os.fsdecode(result.stdout),
                                           os.fsdecode(result.stderr))
    return validate(git, expected_branch, base)
