"""Prepare a candidate complete corpus outside frozen G1/G2 snapshots."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT/'.scratch/ticket-harness/evidence/19-evaluation-g2/snapshot'
TARGET = Path('/tmp/development-review-19-c3-candidate')
assert not TARGET.exists()
shutil.copytree(SOURCE,TARGET)
path = TARGET/'cases/b7/git_ops.py'
text = path.read_text()
text = text.replace('return result.stdout.strip()', 'return result.stdout')
text = text.replace('checked("rev-parse", "--show-toplevel")', 'checked("rev-parse", "--show-toplevel").removesuffix("\\n")')
text = text.replace('checked("symbolic-ref", "--short", "HEAD")', 'checked("symbolic-ref", "--short", "HEAD").removesuffix("\\n")')
path.write_text(text)
(TARGET/'cases/d9/plan.py').write_text('''from dataclasses import dataclass

@dataclass(frozen=True)
class Ticket:
    id: str
    dependencies: tuple[str, ...]

def parse(text):
    tickets = []
    for entry in text.split(","):
        identity, sep, rest = entry.partition(":")
        identity = identity.strip()
        if not identity or not sep:
            raise ValueError("expected id:dependencies")
        dependencies = tuple(d.strip() for d in rest.split("+")) if rest.strip() else ()
        if any(not dependency for dependency in dependencies):
            raise ValueError("empty dependency ID")
        tickets.append(Ticket(identity, dependencies))
    by_id = {t.id: t for t in tickets}
    if len(by_id) != len(tickets):
        raise ValueError("duplicate ID")
    visiting, done = set(), set()
    for ticket in tickets:
        stack = [(ticket.id, False)]
        while stack:
            identity, leaving = stack.pop()
            if leaving:
                visiting.remove(identity)
                done.add(identity)
                continue
            if identity not in by_id:
                raise ValueError("unknown dependency")
            if identity in visiting:
                raise ValueError("cycle")
            if identity in done:
                continue
            visiting.add(identity)
            stack.append((identity, True))
            stack.extend((dependency, False)
                         for dependency in reversed(by_id[identity].dependencies))
    return tuple(tickets)
''')
print('Prepared complete C3 candidate at '+str(TARGET)+'; no declaration or review yet.')
path = TARGET/'cases/f6/io_ops.py'
text = path.read_text().replace('import os\n','import math\nimport os\n')
text = text.replace('def invoke(argv, cwd, timeout):\n', '''def invoke(argv, cwd, timeout):
    try:
        finite = math.isfinite(timeout)
    except (TypeError, ValueError, OverflowError):
        finite = False
    if not finite:
        raise ValueError("finite timeout required")
''')
path.write_text(text)
