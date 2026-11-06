"""Independent target checks: baseline accepts 1, submissions must contain 2."""

import os
import subprocess
import sys
from pathlib import Path

stage = os.environ["TICKET_HARNESS_STAGE"]
print(stage, subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip())
expected = "1\n" if stage == "baseline" else "2\n"
assert Path("value.txt").read_text() == expected
if len(sys.argv) > 2 and stage == sys.argv[2]:
    sys.exit("scripted gate rejection")
