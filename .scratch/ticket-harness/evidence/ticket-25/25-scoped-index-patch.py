"""Stage only task-owned index additions, preserving supplied authoring edits.

The feature index already carries a large uncommitted planning amendment. Its
new completion section is independently stageable against HEAD; the remaining
authoring/status changes stay intact in the shared worktree.
"""
import difflib
import subprocess
from pathlib import Path

patch = []
for name in [".scratch/ticket-harness/README.md", ".scratch/ticket-harness/evidence/README.md"]:
    before = subprocess.check_output(["git", "show", f"HEAD:{name}"], text=True)
    current = Path(name).read_text()
    if name.endswith("evidence/README.md"):
        marker = "| 19–24 |"
        previous = next(line for line in before.splitlines() if line.startswith(marker))
        addition = next(line for line in current.splitlines() if line.startswith("| 25 |"))
        after = before.replace(previous + "\n", previous + "\n" + addition + "\n")
    else:
        marker = "\n## Ticket 25 capture completion\n"
        assert current.count(marker) == 1
        after = before.rstrip() + "\n" + marker + current.split(marker, 1)[1]
    patch.extend(difflib.unified_diff(before.splitlines(keepends=True), after.splitlines(keepends=True),
                                    fromfile="a/" + name, tofile="b/" + name))
with Path(".scratch/ticket-harness/evidence/ticket-25/25-scoped-index.patch").open("x") as output:
    output.writelines(patch)
