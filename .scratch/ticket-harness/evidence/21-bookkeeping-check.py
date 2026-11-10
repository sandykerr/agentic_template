"""Validate ticket-21 bookkeeping without replaying runtime checks or historical writers."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import subprocess

ROOT = Path('/home/ajkerr1/development/agentic_template')
FEATURE = ROOT / '.scratch/ticket-harness'
EV = FEATURE / 'evidence'
TICKET = '.scratch/ticket-harness/issues/21-own-ticket-execution-and-bounded-repairs.md'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def criteria(text):
    return text.split('## Acceptance criteria\n', 1)[1].split('\n## Verification', 1)[0]

def anchors(path):
    result = set()
    counts = {}
    fenced = False
    for line in path.read_text().splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
        if match:
            heading = re.sub(r'[^\w\- ]', '', match[1].lower()).replace(' ', '-')
            count = counts.get(heading, 0)
            counts[heading] = count + 1
            result.add(heading if not count else f'{heading}-{count}')
    return result

def main():
    instruction = json.loads((EV/'21-review-round1-instructions.json').read_text())
    source = instruction['source']
    before = git('show', source+':'+TICKET).decode()
    after = (ROOT/TICKET).read_text()
    assert criteria(before).replace('- [ ]', '- [x]') == criteria(after)
    assert criteria(after).count('- [x]') == 7 and '- [ ]' not in criteria(after)
    assert '**Status:** completed' in after
    assert 'Previous readiness: `ready-for-agent`' in after
    assert next(x for x in before.splitlines() if x.startswith('**Blocked by:**')) == next(x for x in after.splitlines() if x.startswith('**Blocked by:**'))
    index = (FEATURE/'README.md').read_text()
    for expected in ('17 open tickets 22–38', 'twelve completed 10–21 and three remaining 22–24', 'next eligible implementation ticket is 22, backed by completed 02, 12 and 19', '21-completion.md'):
        assert expected in index, expected
    assert '| 20 | completed | M1 |' in index
    capture = json.loads((EV/'21-review-round1-capture.json').read_text())
    assert capture['source'] == source
    for name, digest in capture['files_sha256'].items():
        assert sha((EV/name).read_bytes()) == digest, name
    for name, digest in instruction['instructions_and_packet_sha256'].items():
        data = git('show', source+':'+name) if name == TICKET else (ROOT/name).read_bytes()
        assert sha(data) == digest, name
    tested = json.loads((EV/'21-final-source.json').read_text())
    for name, digest in tested['files'].items():
        assert sha((ROOT/name).read_bytes()) == digest, name
        assert sha(git('show', source+':'+name)) == digest, name
    checks = json.loads((EV/'21-final-check-results.json').read_text())
    assert len(checks['results']) == 6 and all(r['exit_code'] == 0 for r in checks['results'])
    mutable = {TICKET, '.scratch/ticket-harness/README.md', '.scratch/ticket-harness/reviews/README.md', 'next_agent_prompt.md'}
    changed = set(git('diff', '--name-only', source).decode().splitlines())
    changed.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    for name in changed:
        assert name in mutable or name.startswith('.scratch/ticket-harness/evidence/21-') or name == '.scratch/ticket-harness/reviews/ticket-21.md', name
        if name not in mutable:
            assert not git('ls-tree', source, '--', name), ('changed reviewed artifact', name)
    docs = [ROOT/TICKET, FEATURE/'README.md', FEATURE/'reviews/README.md', FEATURE/'reviews/ticket-21.md', *[EV/name for name in ['21-completion.md','21-finding-history.md','21-review-common.md','21-review-spec-instructions.md','21-review-standards-instructions.md','21-review-spec-01.md','21-review-standards-01.md','21-review-packet.md','21-implementation-report.md']]]
    handoff = ROOT/'next_agent_prompt.md'
    selected = None
    if handoff.read_text().startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/22-'):
        selected = 22
        docs.append(handoff)
        assert '**Status:** ready-for-agent' in next((FEATURE/'issues').glob('22-*.md')).read_text()
        for expected in ('G2', 'C5', 'M1', 'architecture-checkpoints.md', 'reviewer-evaluation.md','02-completion.md','12-completion.md','19-completion.md','21-completion.md'):
            assert expected in handoff.read_text(), expected
    count = 0
    for path in docs:
        content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M|re.S)
        content = re.sub(r'`[^`\n]+`', '', content)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', content):
            if re.match(r'[a-z]+://', href):
                continue
            name, _, fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$', '', name)
            target = (path.parent/name).resolve() if name else path
            assert target.exists(), (path, href)
            if fragment:
                if re.fullmatch(r'L\d+(?:-L\d+)?', fragment):
                    assert max(map(int, re.findall(r'\d+', fragment))) <= len(target.read_text().splitlines()), (path, href)
                else:
                    assert fragment in anchors(target), (path, href)
            count += 1
    subprocess.run(['git','-C',str(ROOT),'diff','--check',source],check=True)
    print(json.dumps({'result':'pass','implementation_source':source,'criteria':7,'criterion_wording_dependencies_preserved':True,'tested_git_blob_identities':len(tested['files']),'source_instructions_original_reports_preserved':True,'local_links':count,'handoff_selected':selected},indent=2))

if __name__ == '__main__':
    main()
