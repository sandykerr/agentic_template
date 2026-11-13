"""Audit retained identities, routing, links and preservation; never score judgment."""
from pathlib import Path
from urllib.parse import unquote
import datetime
import hashlib
import json
import re
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / '.scratch/ticket-harness/evidence'
CASE = EV / '19-evaluation'
BASE = 'f2929e79cfd5a68f670862775053ae85ba9582b5'
DOCS = ['docs/agents/reviewer-evaluation.md',
        '.agents/skills/custom/references/planning.md',
        '.agents/skills/custom/implement-with-checkboxes/SKILL.md',
        '.agents/skills/custom/create-next-agent-prompt/SKILL.md']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()

def main():
    changed = set(git('diff', '--name-only', BASE).splitlines() + git('ls-files', '--others', '--exclude-standard').splitlines())
    for name in changed:
        assert name in DOCS or name.startswith('.scratch/ticket-harness/evidence/19-'), name
    protected = set(git('ls-tree', '-r', '--name-only', BASE).splitlines()) - set(DOCS)
    assert not protected & changed, sorted(protected & changed)
    for commit in ['4814eabd4bf2f196f7fb6915667c4305b7c2d0b9', '91e285ff3cb1b46f4404b7fc534625637bdff015', '816aecbaa67f79ca5fd97c78f40593cdb007c45a', 'aef9625c3d155815df22f3e827559ef23fcdcf03']:
        subprocess.run(['git', 'merge-base', '--is-ancestor', commit, BASE], cwd=ROOT, check=True)
    manifest = json.loads((CASE/'source-manifest.json').read_text())
    identity = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    assert identity == (CASE/'corpus-identity.txt').read_text().strip()
    assert set(manifest) == {str(p.relative_to(CASE/'snapshot')) for p in (CASE/'snapshot').rglob('*') if p.is_file()}
    temp = Path('/tmp/development-review-19-g1')
    for name, digest in manifest.items():
        assert sha(CASE/'snapshot'/name) == digest, name
        assert sha(temp/name) == digest, ('supplied snapshot changed', name)
        assert (temp/name).stat().st_mode & 0o222 == 0, name
        if name.startswith('guidance/'):
            # Routing docs added by this ticket are not substantive G1 reviewer instructions.
            original = subprocess.check_output(['git', 'show', BASE+':'+name.removeprefix('guidance/')], cwd=ROOT)
            assert original == (CASE/'snapshot'/name).read_bytes(), name
    declaration = json.loads((CASE/'declaration-capture.json').read_text())
    assert sha(CASE/'declaration.md') == declaration['declaration_sha256']
    assert sha(CASE/'source-manifest.json') == declaration['source_manifest_sha256']
    assignments = json.loads((CASE/'assignments.json').read_text())['assignments']
    assert len(assignments) == 2
    declared_at = datetime.datetime.fromisoformat(declaration['declared_at_utc'])
    for row in assignments:
        assert declared_at < datetime.datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'))
        assert row['settings'] == {'fork_turns':'none', 'model':'gpt-6.1-sol', 'reasoning_effort':'high'}
        assert sha(CASE/row['prompt_path']) == row['prompt_sha256']
        # Serialized dispatch messages are opaque; the recipient preserves readable input.
        prompt = (CASE/(row['label']+'-input.txt')).read_text()
        assert str(temp) in prompt and identity in prompt
    captured = json.loads((CASE/'review-capture.json').read_text())
    for name, digest in captured['sha256'].items():
        assert sha(CASE/name) == digest, name
    supplement = json.loads((CASE/'review-capture-supplement.json').read_text())
    for row in supplement['axes'].values():
        assert sha(CASE/row['source_records_path']) == row['source_records_sha256']
        assert row['custom_tool_call_count'] == row['custom_tool_output_count'] > 0
    anchors = runpy.run_path(str(EV/'16-check.py'))['anchors']
    docs = [ROOT/name for name in DOCS] + [EV/'19-implementation-report.md'] + list(CASE.glob('*.md'))
    links = []
    for path in docs:
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M|re.S)
        text = re.sub(r'`[^`\n]+`', '', text)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            if re.match(r'[a-z]+://', href):
                continue
            name, _, fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$', '', name)
            target = (path.parent/name).resolve() if name else path
            assert target.exists(), (path, href)
            if fragment:
                assert fragment in anchors(target), (path, href)
            links.append({'from':str(path.relative_to(ROOT)), 'href':href})
    for name in DOCS[1:]:
        assert 'reviewer-evaluation.md' in (ROOT/name).read_text(), name
    # The retained guidance deliberately has unsupplied outgoing context pointers.
    # REVIEW.md bounds their resolution; never pull key-bearing specs into reviewer input.
    assert not list((CASE/'snapshot').rglob('*declaration*'))
    assert not (CASE/'snapshot/guidance/.scratch').exists()
    result = {'result':'pass', 'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'baseline':BASE, 'head_before_checkpoint':git('rev-parse','HEAD'),
              'scope':'standalone documentation/skill evidence; no runtime tests or judgment scoring',
              'source_identities':{str(p.relative_to(ROOT)):sha(p) for p in docs if not p.name.endswith('-raw.md')},
              'helpers':{str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__),EV/'19-run-checks.sh',CASE/'build_corpus.py',CASE/'capture_reviews.py']},
              'retained_evidence_identities':{str(p.relative_to(ROOT)):sha(p) for p in sorted(CASE.rglob('*')) if p.is_file()},
              'corpus_identity':identity, 'corpus_files':len(manifest),
              'protected_baseline_paths':len(protected), 'local_links':links,
              'review_capture':captured, 'assignments':assignments,
              'limits':'Link/hash/routing audits do not establish reviewer judgment. See manual per-case adjudication and original reports.'}
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    target = EV/f'19-check-results-{stamp}.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':'pass','source_manifest':identity,'corpus_files':len(manifest),'protected_paths':len(protected),'local_links':len(links),'result_path':str(target.relative_to(ROOT))},indent=2))

if __name__ == '__main__':
    main()
