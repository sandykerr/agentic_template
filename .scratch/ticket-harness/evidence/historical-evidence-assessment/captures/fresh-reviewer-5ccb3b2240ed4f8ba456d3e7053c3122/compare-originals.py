"""Read-only fresh evidence comparison; never imports/replays historical helpers."""
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

ROOT = Path.cwd()
HERE = Path(__file__).parent
CAPTURES = HERE.parent
INV = CAPTURES / 'inventory-root-72f0b403e93345f0a95967f008f9b99a/inventory-reference.json.gz'
SHA = 'f8aa9c90b82bcc4e34205c8159af1f38469d65e37a8e706836c9c90986124919'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
assert digest(INV) == SHA
inventory = json.loads(gzip.decompress(INV.read_bytes()))
print('inventory keys:', list(inventory))
files = inventory['files']
if isinstance(files, dict): lookup = files
else: lookup = {f['path']: f for f in files}
def repo(p):
    return p if p.startswith('.scratch/') else '.scratch/ticket-harness/' + p
result = {'kind': 'fresh read-only comparisons; not tests or retirement execution', 'inventory_sha256': SHA, 'identities': [], 'checks': [], 'omissions': []}
proposals = sorted(CAPTURES.glob('assessor-*/proposal.json')) + [INV.parent / 'shared-proposal.json']
for p in proposals:
    for g in read(p)['groups']:
        gid = g.get('group_id', g.get('id'))
        for f in g['files']:
            path = repo(f['path']); identity = lookup[path]
            item = {'group': gid, 'path': path, 'inventory': identity}
            for key in ('size', 'sha256', 'kind'):
                if key in f and key in identity and not (key == 'sha256' and len(f[key]) != 64):
                    assert f[key] == identity[key], (gid, path, key)
            if g['proposed_action'] != 'keep':
                item['current_identity_matches'] = Path(path).stat().st_size == identity['size'] and digest(Path(path)) == identity['sha256']
                assert item['current_identity_matches'], path
            result['identities'].append(item)

b = CAPTURES / 'assessor-09-16-d100832579c14d66a22bc1bce5de27b3'
def projection(original, projected, location):
    assert projected['present_fields'] == {k:original[k] for k in projected['present_fields']}, location
    assert all(k not in original for k in projected['unavailable_fields']), location
    if 'omitted_fields' in projected:
        assert set(projected['omitted_fields']) == set(original) - set(projected['present_fields']) - {'gates','attempts'}, location
    for key in ('gates','attempts'):
        if key not in projected: continue
        if projected[key] is None:
            assert key not in original or original[key] is None, (location,key,'unavailable is not empty')
            result['omissions'].append({'location':location,'field':key,'original_presence':key in original,'retained':'unavailable null, not zero or []'})
            continue
        assert len(projected[key]) == len(original.get(key, [])), (location,key)
        for old,new in zip(original.get(key, []),projected[key]):
            assert all(k in old and old[k] == v for k,v in new.items()), (location,key,new)
candidate = read(b / 'ticket-15-installed-results.merge-proposed.json')
for v in candidate['versions']:
    old = read(Path(v['original_path']))
    for key in ('feature','development','installed_sha256','import_path'):
        assert v[key] == old.get(key), key
    assert len(v['commands']) == len(old['commands'])
    for i,(oc,nc) in enumerate(zip(old['commands'],v['commands'])):
        for key in ('command','cwd','exit_code','stderr','terminated_by_fixture'):
            assert (key in oc) == (key in nc) and oc.get(key) == nc.get(key), (v['original_path'],i,key)
        if nc['stdout_state'] == 'observed empty': assert oc['stdout'] == ''
        elif 'stdout_result' in nc: projection(json.loads(oc['stdout']), nc['stdout_result'],(v['original_path'],i))
        else: result['omissions'].append({'command':i,'projection_keys':list(nc)})
    projection(old['final_record'],v['final_record'],v['original_path'])
    for key in ('gates','attempts'): assert v['final_record'][key] == old['final_record'][key], key
    result['checks'].append({'comparison':'ticket15 projected values/field presence/final gates and attempts match original','path':v['original_path'],'outcome':old['final_record'].get('outcome'),'omitted':v['final_record']['omitted_fields']})

wheel = read(b / 'ticket-15-wheel-inspection.json')
for v in wheel['versions']:
    with zipfile.ZipFile(v['path']) as z:
        python_members = {m['member'] for m in v['python_members']}
        assert set(z.namelist()) == python_members | set(v['metadata'])
        for name in python_members:
            cp = subprocess.run(['git','show',v['verified_git_revision']+':'+name],capture_output=True,check=True)
            assert cp.stdout == z.read(name), name
        for name,content in v['metadata'].items(): assert z.read(name).decode() == content, name
    result['checks'].append({'comparison':'all wheel source members equal exact Git; full dist-info retained','path':v['path'],'revision':v['verified_git_revision']})

archive = read(b / 'ticket-16-archive-results.merge-proposed.json')
current = Path(archive['retained_current_fixture'])
current_commits = re.findall(r'- ([ABC]): `([0-9a-f]{40})`',(current/'evidence/commits.md').read_text())
def normalize(txt, pairs):
    for alias,sha in pairs: txt = txt.replace(sha,'<synthetic-'+alias+'>')
    return txt
for v in archive['versions']:
    with tarfile.open(v['original_path']) as tar:
        members = [m for m in tar.getmembers() if m.isfile()]
        assert len(members) == v['regular_members']
        assert all(m.isfile() or m.isdir() for m in tar.getmembers())
        assert [m.name for m in members] == v['member_names']
        payload = {m.name:tar.extractfile(m).read().decode() for m in members}
    assert payload['16-miniature/evidence/commits.md'] == v['exact_commit_record']
    assert payload['16-miniature/evidence/instructions.md'] == v['exact_instruction_record']
    pairs = list(v['synthetic_commit_identities'].items())
    expected = {d['member']:d['normalized_diff_to_retained_current'] for d in v['substantive_changes_after_normalizing_commit_aliases']}
    actual = {}
    for member,old in payload.items():
        new = (current/Path(member).relative_to('16-miniature')).read_text()
        old = normalize(old,pairs);new = normalize(new,current_commits)
        if old != new:
            diff = ''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=Path(v['original_path']).name+'/'+member,tofile='retained-current/'+member))
            actual[member] = diff
    assert actual == expected, (v['original_path'],set(actual),set(expected))
    result['checks'].append({'comparison':'all archive members reviewed; exact instruction/commit records and all normalized differences retained','path':v['original_path'],'different_members':list(actual),'synthetic_only':True})

for ticket,driver in [('20','20-final-checks.log'),('21','21-final-runner.log'),('22','22-final-runner.log')]:
    d = Path('.scratch/ticket-harness/evidence/ticket-'+ticket)
    decoder=json.JSONDecoder();remaining=(d/driver).read_text();values=[]
    while remaining.strip():
        value,end=decoder.raw_decode(remaining.lstrip());values.append(value);remaining=remaining.lstrip()[end:]
    retained=read(d/(ticket+'-final-check-results.json'))
    assert values == retained['results'], ticket
    result['checks'].append({'comparison':'all driver values exactly equal retained result list','ticket':ticket,'commands':len(values)})
with (HERE/'comparison-results.json').open('x') as out: json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(result['identities']),'group-file identities;',len(result['checks']),'substantive comparisons')
