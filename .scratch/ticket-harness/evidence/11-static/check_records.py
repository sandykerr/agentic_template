from pathlib import Path
import hashlib,re,subprocess,json
root=Path('/home/ajkerr1/development/agentic_template')
base='5af3b343ad962b05ce44e359b791b65a8865f05a'
impl='552fcd6b87909b96ac7bcd6a878d0db6bbbd2869'
ticket=Path('.scratch/ticket-harness/issues/11-stop-development-handoffs-at-qa-milestones.md')
def git(*args):
    p=subprocess.run(['git',*args],cwd=root,text=True,capture_output=True)
    assert p.returncode==0,(args,p.stderr)
    return p.stdout
old=git('show',f'{base}:{ticket}')
new=(root/ticket).read_text()
def criteria(s):
    return s.split('## Acceptance criteria\n',1)[1].split('\n## Verification',1)[0]
assert criteria(old).replace('- [ ]','- [x]')==criteria(new)
assert criteria(new).count('- [x]')==6 and '- [ ]' not in criteria(new)
assert '**Status:** completed' in new and 'Previous readiness: `ready-for-agent`' in new
assert re.search(r'^\*\*Blocked by:.*$',old,re.M).group()==re.search(r'^\*\*Blocked by:.*$',new,re.M).group()
index=(root/'.scratch/ticket-harness/README.md').read_text()
assert '**17 open tickets (12–28)**' in index and 'next eligible ticket is **12**' in index
assert 'evidence/11-completion.md' in index and 'M1 has not been accepted.' in index
paths=[ticket,Path('.scratch/ticket-harness/evidence/11-completion.md'),Path('.scratch/ticket-harness/evidence/11-review-spec.md'),Path('.scratch/ticket-harness/evidence/11-review-standards.md')]
count=0
for file in paths:
    for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)',(root/file).read_text()):
        target,_,fragment=href.partition('#')
        resolved=(root/file).parent/target if target else root/file
        assert resolved.exists(),(file,href)
        if fragment:
            headings=re.findall(r'^#{1,6}\s+(.+)$',resolved.read_text(),re.M)
            anchors={re.sub(r'\s','-',re.sub(r'[^\w\-\s]','',h.lower())) for h in headings}
            assert fragment in anchors,(file,href)
        count+=1
for path in re.findall(r'\]\((evidence/11[^)]+)\)',index):
    assert (root/'.scratch/ticket-harness'/path).exists()
observations=json.loads((root/'.scratch/ticket-harness/evidence/11-handoff-observations.json').read_text())
for path,sha in observations['source_sha256'].items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==sha
    committed=git('show',f'{impl}:{path}')
    assert committed==(root/path).read_text()
assert hashlib.sha256((root/'docs/agents/issue-tracker.md').read_bytes()).hexdigest()=='3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce'
changed=git('diff','--name-only',f'{base}...HEAD').splitlines()
assert set(changed)=={'.agents/skills/custom/implement-with-checkboxes/SKILL.md','.agents/skills/custom/create-next-agent-prompt/SKILL.md'}
print(f'PASS: six markers/status/prior readiness/dependency wording/index agree; {count} bookkeeping links/anchors resolve; implementation identities unchanged; unrelated edit preserved.')
