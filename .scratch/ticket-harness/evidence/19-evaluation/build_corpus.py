"""Construct a new isolated review corpus. Evaluator-only: never reviewer input."""
from pathlib import Path
import hashlib
import json
import subprocess
import textwrap

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SNAP = OUT / 'snapshot'
assert not SNAP.exists(), 'Never overwrite a declared corpus'

def put(name, body):
    path = SNAP / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).lstrip())

put('cases/a3/CONTRACT.md', '''
# Saved checks
Run owns durable gates and verified references. `record` registers successful evidence;
`save` and `restore` preserve JSON keys and later source invalidation semantics.
Verified references resolve to the same canonical gate records used by durable
reporting, so changing a source marks both views invalid. QA reads the verified
view. The caller may invalidate source A after restoring a deliberate stop.
Only Run writes these records; consumer functions are read-only. No concurrency.
''')
put('cases/a3/run.py', '''
import json

class Run:
    def __init__(self):
        self.gates = []
        self.verified = []

    def record(self, source):
        gate = {"source": source, "passed": True, "valid": True}
        self.gates.append(gate)
        self.verified.append(gate)

    def invalidate(self, source):
        for gate in self.gates:
            if gate["source"] == source:
                gate["valid"] = False

    def save(self):
        return json.dumps({"gates": self.gates, "verified": self.verified})

    @classmethod
    def restore(cls, saved):
        value = json.loads(saved)
        run = cls()
        run.gates = value["gates"]
        run.verified = value["verified"]
        return run
''')
put('cases/a3/qa.py', '''
def eligible(run, source):
    return any(g["source"] == source and g["passed"] and g["valid"]
               for g in run.verified)

def report(run):
    return [dict(gate) for gate in run.gates]
''')
put('cases/b7/CONTRACT.md', '''
# Repository preflight
`validate` owns the local repository preflight and returns the resolved root and
requested branch. Reject failed Git commands, detached HEAD, an unexpected branch,
a dirty worktree (including untracked files), absent base revision, and a base that
is not an ancestor of HEAD. Read-only; no saved state or mutation. The injected
`git` callable accepts argument lists and returns CompletedProcess-like results;
it runs against the requested checkout with text capture, never a shell. Git
failure details may be reduced to ValueError. No class requirement or generic
validation framework. The caller selects policies through `expected_branch` and
`base`; it should not reproduce these validation decisions.
''')
put('cases/b7/git_ops.py', '''
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
''')
put('cases/b7/caller.py', '''
import subprocess
from git_ops import validate

def preflight(checkout, expected_branch, base):
    def git(args):
        return subprocess.run(["git", "-C", str(checkout), *args],
                              capture_output=True, text=True, check=False)
    return validate(git, expected_branch, base)
''')
put('cases/c2/CONTRACT.md', '''
# Report handoff
An attempt's validated human-decision handoff belongs to that attempt even after
a later attempt starts. History preserves all attempts in start order. Report
work may finish after another attempt has been appended. `attach` receives the
attempt ID supplied by the report command; validation ensures handoff content
is valid for that ID. Checking validates and returns report information; it
must not choose or edit an attempt from shared history. Execution locates the
identified owner and asks it to attach the handoff. Consumers read by attempt ID.
Unknown IDs reject without changing any attempt. No durable checkpoint here.
''')
put('cases/c2/checking.py', '''
def validate_handoff(attempt_id, payload):
    if payload.get("attempt") != attempt_id or not payload.get("decision"):
        raise ValueError("invalid handoff")
    return dict(payload)

def attach(history, attempt_id, payload):
    handoff = validate_handoff(attempt_id, payload)
    history[-1].handoff = handoff
    return handoff
''')
put('cases/c2/execution.py', '''
from dataclasses import dataclass
from checking import attach

@dataclass
class Attempt:
    id: str
    handoff: dict | None = None

class Execution:
    def __init__(self):
        self.history = []

    def start(self, identity):
        self.history.append(Attempt(identity))

    def receive(self, attempt_id, payload):
        return attach(self.history, attempt_id, payload)

    def decision(self, attempt_id):
        return next(a.handoff for a in self.history if a.id == attempt_id)
''')
put('cases/d9/CONTRACT.md', '''
# Plan parsing
`parse` returns a fresh tuple of frozen Ticket values from comma-separated
`id:dependency+dependency` entries, rejecting missing/duplicate IDs, missing
referenced dependencies and cycles. IDs are trimmed nonempty strings; empty
right sides mean no dependencies. Output preserves declaration order and each
dependency's order. No external resources, lifecycle, mutable shared data or
persistence. Configuration contains only this syntax. Readiness calculations
consume the immutable result. Keep ordinary transformations as functions.
''')
put('cases/d9/plan.py', '''
from dataclasses import dataclass

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
        dependencies = tuple(d.strip() for d in rest.split("+") if d.strip())
        tickets.append(Ticket(identity, dependencies))
    by_id = {t.id: t for t in tickets}
    if len(by_id) != len(tickets):
        raise ValueError("duplicate ID")
    visiting, done = set(), set()
    def visit(identity):
        if identity not in by_id:
            raise ValueError("unknown dependency")
        if identity in visiting:
            raise ValueError("cycle")
        if identity in done:
            return
        visiting.add(identity)
        for dependency in by_id[identity].dependencies:
            visit(dependency)
        visiting.remove(identity)
        done.add(identity)
    for ticket in tickets:
        visit(ticket.id)
    return tuple(tickets)
''')
put('cases/e4/CONTRACT.md', '''
# Submission observations
Attempt owns submission and the mirrored current-ticket observation. Both normal
worker and repair entry paths preserve the same transition invariant: only a
running attempt may submit, its revision and status change together, and the
current-ticket fields reflect that attempt. Changes to submission policy must
have one owning operation; entry callers delegate rather than reproduce record
edits. State is in-memory and deliberately exposes records to read-only reporting.
Only the owner may write those records. No concurrent calls or persistence here.
''')
put('cases/e4/attempt.py', '''
class Attempt:
    def __init__(self, identity, ticket):
        self.record = {"id": identity, "status": "running", "revision": None}
        self.ticket = ticket

    def submit(self, revision):
        if self.record["status"] != "running":
            raise ValueError("not running")
        self.record["revision"] = revision
        self.record["status"] = "submitted"
        self.ticket["attempt"] = self.record["id"]
        self.ticket["revision"] = revision
        self.ticket["status"] = "submitted"
''')
put('cases/e4/worker.py', '''
def receive_worker(attempt, revision):
    attempt.submit(revision)
''')
put('cases/e4/repair.py', '''
def receive_repair(attempt, revision):
    if attempt.record["status"] != "running":
        raise ValueError("not running")
    attempt.record["revision"] = revision
    attempt.record["status"] = "submitted"
    attempt.ticket["attempt"] = attempt.record["id"]
    attempt.ticket["revision"] = revision
    attempt.ticket["status"] = "submitted"
''')
put('cases/f6/CONTRACT.md', '''
# Local IO
`atomic_write` replaces a local UTF-8 file with complete text using a temporary
file on the same filesystem. Existing content survives an exception before replace;
temporary files are cleaned on failure. Caller supplies a directory that exists.
No crash durability/fsync or metadata preservation guarantee. `invoke` runs an
argument vector without a shell, in a supplied cwd with text capture and finite
timeout, returning nonzero exits for the caller's domain policy; TimeoutExpired
propagates. These primitives own no run/attempt/review state and perform no domain
record mutations. No persistence beyond the explicitly written file.
''')
put('cases/f6/io_ops.py', '''
import os
from pathlib import Path
import subprocess
import tempfile

def atomic_write(destination, text):
    destination = Path(destination)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=destination.parent, delete=False) as file:
            temporary = Path(file.name)
            file.write(text)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)

def invoke(argv, cwd, timeout):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout, check=False)
''')
put('cases/g1/CONTRACT.md', '''
# Prepared input
Preparation owns configuration validation and normalization. Both CLI and resumed
entry paths must return a complete Prepared result: nonempty selected IDs,
normalized unique membership preserving first order, and a positive repair limit
(default 2). Raw configuration is copied, never mutated. Callers may consume the
prepared result directly; they must not finish its initialization in a particular
order or know derived-field rules. Invalid repair limit rejects during preparation,
not later during execution. Result state is in-memory, no checkpoint serialization.
''')
put('cases/g1/preparation.py', '''
class Prepared:
    def __init__(self, raw):
        self.raw = dict(raw)
        self.selected = None
        self.repair_limit = None

def prepare(raw):
    if not raw.get("selected"):
        raise ValueError("empty selection")
    return Prepared(raw)
''')
put('cases/g1/cli.py', '''
from preparation import prepare

def from_cli(raw):
    prepared = prepare(raw)
    prepared.selected = tuple(dict.fromkeys(raw["selected"]))
    prepared.repair_limit = int(raw.get("repair_limit", 2))
    if prepared.repair_limit < 1:
        raise ValueError("invalid repair limit")
    return prepared
''')
put('cases/g1/resume.py', '''
from preparation import prepare

def from_saved_config(raw):
    return prepare(raw)
''')
put('cases/h8/CONTRACT.md', '''
# Attempt operations
Attempt owns running -> submitted -> completed transitions and mirrored current
observations. Construction sets both views consistently. Submission requires a
running attempt and nonempty revision; completion requires a submitted attempt.
Invalid operations leave both views untouched. Consumers receive copied snapshots;
caller-owned input dictionaries cannot mutate state. No persistence or concurrency.
Caller asks for operations; it does not edit the record. A small class is permitted
because these operations own a real invariant. No general state-machine framework.
''')
put('cases/h8/attempt.py', '''
class Attempt:
    def __init__(self, identity):
        self._record = {"id": identity, "status": "running", "revision": None}
        self._current = dict(self._record)

    def submit(self, revision):
        if self._record["status"] != "running" or not revision:
            raise ValueError("invalid submission")
        self._transition("submitted", revision)

    def complete(self):
        if self._record["status"] != "submitted":
            raise ValueError("invalid completion")
        self._transition("completed", self._record["revision"])

    def _transition(self, status, revision):
        updated = {**self._record, "status": status, "revision": revision}
        self._record = updated
        self._current = dict(updated)

    def snapshot(self):
        return dict(self._record), dict(self._current)
''')
put('cases/h8/caller.py', '''
from attempt import Attempt

def execute(identity, revision):
    attempt = Attempt(identity)
    attempt.submit(revision)
    attempt.complete()
    return attempt.snapshot()
''')
# Preserve paths for ordinary relative guidance links. Do not include key-bearing spec.
guidance = [
    'GLOSSARY.md', 'docs/adr/0001-reusable-harness-and-local-integration.md',
    'docs/adr/0002-human-qa-gates-feature-promotion.md',
    'docs/agents/ownership-review.md', 'docs/agents/review-records.md',
    'docs/agents/architecture-checkpoints.md', 'docs/agents/testing.md',
    '.agents/skills/matt-pocock/codebase-design/SKILL.md',
    '.agents/skills/microsoft/microsoft_oop/SKILL.md',
    '.agents/skills/custom/test-strategy/SKILL.md',
    'docs/templates/reviews/report.md',
]
for name in guidance:
    put('guidance/' + name, (ROOT / name).read_text())
put('REVIEW.md', '''
# Source assessment
Review all eight independent case directories under cases/. Each CONTRACT.md is
its governing approved behavior/ownership contract; inspect every source file and
caller in that directory. They are miniature development snapshots, unrelated to
one another. Assess source as a whole, no changed-hunk restriction. Case identities
are a3, b7, c2, d9, e4, f6, g1, h8. No production package or unprovided repository
context is required. Do not infer requirements from a different case.

Use guidance/docs/agents/ownership-review.md and the report envelope, with the
record and checkpoint contracts as applicable. Follow links only within this
snapshot; absent targets are not supplied and do not authorize broader reads.
The case contracts replace target-specific spec/ticket links. No prior findings
or human decisions are supplied. Standards additionally applies the supplied
codebase-design, microsoft_oop and test-strategy skills. Both axes preserve
optional versus blocking classification and evidence-based proportional remedies.

For each case report inspected files/flows, relevant owner/writers/readers,
restore/invalidation (or absence), approved invariant reasoning, clean reasoning
or findings with local IDs, exact source locations, consequences and remedies.
Separate source judgment from hash/command audits. Identify omitted scope and
assumptions. This is a standalone documentation/source evaluation, no production
tests required. Do not modify the snapshot or run a harness. You may read source
and run read-only checks or disposable observations outside it. Retain complete
reasoning; no 400-word report cap. Return your full original report in final.
''')
manifest = {str(p.relative_to(SNAP)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(SNAP.rglob('*')) if p.is_file()}
(OUT / 'source-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
# A blob hash plus full manifest pins this exact source independently of later commits.
source_id = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
(OUT / 'corpus-identity.txt').write_text(source_id+'\n')
print(json.dumps({'files':len(manifest), 'corpus_sha256':source_id}, indent=2))
