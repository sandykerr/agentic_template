"""One-off read-only inventory, not a retirement executor."""
import gzip
import hashlib
import json
import os
import re
import stat
import subprocess
import tarfile
from datetime import datetime, timezone
from pathlib import Path

root = Path.cwd()
feature = root / '.scratch/ticket-harness'
dest = feature / 'evidence/historical-evidence-assessment/captures/inventory-root-72f0b403e93345f0a95967f008f9b99a'
def git(*args):
    return subprocess.check_output(['git', *args])
def sha(data):
    return hashlib.sha256(data).hexdigest()
def rel(path):
    return str(path.relative_to(root))
excluded = ('evidence/historical-evidence-assessment/',)
files = []
texts = {}
for base in [feature, root / 'docs', root / '.agents/skills/custom', root / 'ticket_harness', root / 'tests']:
    for parent, dirs, names in os.walk(base, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d != '.git')
        for name in sorted(names):
            path = Path(parent) / name
            if path.is_relative_to(dest.parent.parent):
                continue
            s = path.lstat()
            kind = 'symlink' if stat.S_ISLNK(s.st_mode) else 'regular' if stat.S_ISREG(s.st_mode) else 'other'
            data = os.readlink(path).encode() if kind == 'symlink' else path.read_bytes() if kind == 'regular' else b''
            item = dict(path=rel(path), kind=kind, size=s.st_size, sha256=sha(data), mode=oct(s.st_mode), nlink=s.st_nlink)
            if kind == 'symlink': item['target'] = os.readlink(path)
            files.append(item)
            if kind == 'regular' and len(data) <= 8_000_000 and b'\0' not in data:
                try: texts[rel(path)] = data.decode('utf-8')
                except UnicodeDecodeError: pass
for name in ['AGENTS.md', 'GLOSSARY.md', 'README.md', 'pyproject.toml', 'next_agent_prompt.md']:
    p = root / name
    data = p.read_bytes()
    files.append(dict(path=name, kind='regular', size=len(data), sha256=sha(data)))
    texts[name] = data.decode()
print('File identities complete', len(files), flush=True)
evidence = [f for f in files if f['path'].startswith('.scratch/ticket-harness/evidence/')]
by_name = {}
for f in evidence:
    name = Path(f['path']).name
    if len(name) > 10: by_name.setdefault(name, []).append(f['path'])
tokens = re.compile(r'[A-Za-z0-9_][A-Za-z0-9_.-]{9,}')
refs = []
for path, text in texts.items():
    for line_no, line in enumerate(text.splitlines(), 1):
        targets = sorted({target for m in tokens.finditer(line) for target in by_name.get(m.group(), []) if target != path})
        if targets:
            refs.append(dict(reader=path, line=line_no, targets=targets, excerpt=line[:900], status='lexical candidate; human assessment required'))
print('Reference candidates complete', len(refs), flush=True)
archives = []
for f in evidence:
    p = root / f['path']
    if f['kind'] != 'regular' or not (p.name.endswith('.tar.gz') or p.name.endswith('.tgz')): continue
    members = []
    with tarfile.open(p, 'r:*') as archive:
        for m in archive:
            entry = dict(path=m.name, size=m.size, kind='regular' if m.isfile() else 'symlink' if m.issym() else 'directory' if m.isdir() else 'other', linkname=m.linkname or None)
            if m.isfile(): entry['sha256'] = sha(archive.extractfile(m).read())
            members.append(entry)
    archives.append(dict(path=f['path'], members=members, inspection='Member identities only; not a semantic clearance. Assessors inspect protected contents before any proposal.'))
tracked = set(git('ls-files', '-z').decode().split('\0'))
missing = [p for p in sorted(tracked) if p and not (root / p).exists() and not (root / p).is_symlink()]
old_path = feature / 'evidence/evidence-retention-audit-01/worker-inventory-data.json.gz'
old = json.loads(gzip.decompress(old_path.read_bytes()))
with (dest / 'historical-inventory-shape.json').open('w') as out:
    json.dump(dict(type=type(old).__name__, keys=list(old)[:20] if isinstance(old, dict) else None, sample=str(old)[:1200]), out, indent=2)
patch = git('diff', '--binary', 'HEAD')
(dest / 'checkout-dirty.patch').write_bytes(patch)
status = git('status', '--short').decode()
result = dict(schema_version=1, created_at=datetime.now(timezone.utc).isoformat(), checkout=str(root), head=git('rev-parse','HEAD').decode().strip(), branch=git('branch','--show-current').decode().strip(), host=os.uname().nodename, architecture=os.uname().machine, dirty_patch_sha256=sha(patch), status_at_inventory=status, ticket_ids=[p.name.split('-')[0] for p in sorted((feature/'issues').glob('*.md')) if 0 <= int(p.name.split('-')[0]) <= 24], absent_requested_ids=['00'], files=files, evidence_count=len(evidence), evidence_logical_bytes=sum(f['size'] for f in evidence if f['kind']=='regular'), references=refs, archives=archives, preexisting_tracked_missing=missing, historical_path_rule='.scratch/ticket-harness/evidence/NN-suffix -> .scratch/ticket-harness/evidence/ticket-NN/NN-suffix; ticket16-standards-identities.json exception', limits=['References are lexical candidates, never proof that unmatched files have no consumers.', 'No external run registry is available; run intent requires retained QA/continuation context.', 'Archives have member identities, not blanket semantic approval.', 'Fresh capture metadata and this assessment folder are excluded; final verification checks these separately.', 'No runtime suite or historical helper was executed.'])
print('Archive identities complete; serializing', len(archives), flush=True)
payload = json.dumps(result, separators=(',', ':')).encode()
(dest / 'inventory-reference.json.gz').write_bytes(gzip.compress(payload, compresslevel=1))
print(json.dumps(dict(files=len(files), evidence_count=len(evidence), evidence_bytes=result['evidence_logical_bytes'], references=len(refs), archives=len(archives), archive_members=sum(len(a['members']) for a in archives), missing_tracked=len(missing), destination=str(dest))))
