"""Audit versioned repair identities/links/routing/preservation; never score judgment."""
from pathlib import Path
from urllib.parse import unquote
import ast
import datetime
import hashlib
import json
import re
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT/'.scratch/ticket-harness/evidence'
OLD = EV/'19-evaluation'
SECOND = EV/'19-evaluation-g2'
THIRD = EV/'19-evaluation-g3'
CASE = EV/'19-evaluation-g4'
BASE = 'f2929e79cfd5a68f670862775053ae85ba9582b5'
REJECTED = 'e90abb64ab95c5b15cdb0949b03c6a948365339b'
AUTHORING = ['docs/agents/ownership-review.md','docs/agents/reviewer-evaluation.md']
ROUTES = ['.agents/skills/custom/references/planning.md','.agents/skills/custom/implement-with-checkboxes/SKILL.md','.agents/skills/custom/create-next-agent-prompt/SKILL.md']
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()
def identity(case,temp):
    manifest = json.loads((case/'source-manifest.json').read_text())
    value = hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
    assert value == (case/'corpus-identity.txt').read_text().strip()
    assert set(manifest) == {str(p.relative_to(case/'snapshot')) for p in (case/'snapshot').rglob('*') if p.is_file()}
    for name,digest in manifest.items():
        assert sha(case/'snapshot'/name) == digest,(case,name)
        assert sha(temp/name) == digest,('supplied snapshot changed',name)
        assert not (temp/name).stat().st_mode & 0o222,name
    capture = json.loads((case/'declaration-capture.json').read_text())
    assert sha(case/'declaration.md') == capture['declaration_sha256']
    assert sha(case/'source-manifest.json') == capture['source_manifest_sha256']
    for name,digest in json.loads((case/'review-capture.json').read_text())['sha256'].items():
        assert sha(case/name) == digest,(case,name)
    return value,manifest,capture

def main():
    changed = set(git('diff','--name-only',REJECTED).splitlines())
    # Every original tracked artifact (including rejected conclusions/checks/G1)
    # is byte-preserved; only the explicit current guidance owners may change.
    old_paths = set(git('ls-tree','-r','--name-only',REJECTED).splitlines())
    modified = changed & old_paths
    assert modified <= set(AUTHORING), sorted(modified-set(AUTHORING))
    new_paths = (changed-old_paths) | set(git('ls-files','--others','--exclude-standard').splitlines())
    for name in new_paths:
        assert (name.startswith('.scratch/ticket-harness/evidence/19-evaluation-g2/')
                or name.startswith('.scratch/ticket-harness/evidence/19-evaluation-g3/')
                or name.startswith('.scratch/ticket-harness/evidence/19-evaluation-g4/')
                or name.startswith('.scratch/ticket-harness/evidence/19-repair-')
                or name.startswith('.scratch/ticket-harness/evidence/19-review-')
                or name in ['.scratch/ticket-harness/evidence/19-finding-history.md','.scratch/ticket-harness/reviews/ticket-19.md']),name
    for commit in ['4814eabd4bf2f196f7fb6915667c4305b7c2d0b9','91e285ff3cb1b46f4404b7fc534625637bdff015','816aecbaa67f79ca5fd97c78f40593cdb007c45a','aef9625c3d155815df22f3e827559ef23fcdcf03']:
        subprocess.run(['git','merge-base','--is-ancestor',commit,BASE],cwd=ROOT,check=True)
    old_id,old_manifest,_ = identity(OLD,Path('/tmp/development-review-19-g1'))
    second_id,second_manifest,_ = identity(SECOND,Path('/tmp/development-review-19-g2'))
    third_id,third_manifest,_ = identity(THIRD,Path('/tmp/development-review-19-c3'))
    corpus,manifest,declared = identity(CASE,Path('/tmp/development-review-19-c4'))
    delta = {name for name in manifest if old_manifest[name] != manifest[name]}
    assert delta == {'cases/h8/attempt.py','guidance/docs/agents/ownership-review.md',
                     'cases/b7/git_ops.py','cases/b7/caller.py','cases/d9/plan.py','cases/f6/io_ops.py'},delta
    assert {name for name in manifest if second_manifest[name] != third_manifest[name]} == {'cases/b7/git_ops.py','cases/d9/plan.py','cases/f6/io_ops.py'}
    assert {name for name in manifest if third_manifest[name] != manifest[name]} == {'cases/b7/caller.py'}
    for label,case in [('c2',SECOND),('c3',THIRD)]:
        preserved = json.loads((EV/f'19-repair-{label}-preservation.json').read_text())['sha256']
        assert set(preserved) == {str(p.relative_to(case)) for p in case.rglob('*') if p.is_file()}
        for name,digest in preserved.items():
            assert sha(case/name) == digest,(label,name)
    assert json.loads((THIRD/'declaration-capture.json').read_text())['C2_preservation_sha256'] == sha(EV/'19-repair-c2-preservation.json')
    assert declared['C3_preservation_sha256'] == sha(EV/'19-repair-c3-preservation.json')
    saved_capture = THIRD/'spec-c3-reviewer-saved.md'
    original_c3 = json.loads((EV/'19-repair-c3-preservation.json').read_text())['sha256']
    assert sha(saved_capture) == original_c3[saved_capture.name]
    saved_bytes = saved_capture.read_bytes()
    assert len(saved_bytes)-len(saved_bytes.rstrip(b'\n')) == 2
    for name in manifest:
        if name.startswith('guidance/'):
            assert sha(ROOT/name.removeprefix('guidance/')) == manifest[name],name
            assert manifest[name] == second_manifest[name] == third_manifest[name],name
    assert not list((CASE/'snapshot').rglob('*declaration*'))
    assert not (CASE/'snapshot/guidance/.scratch').exists()
    for case,value in [(SECOND,second_id),(THIRD,third_id),(CASE,corpus)]:
        rows = json.loads((case/'assignments.json').read_text())['assignments']
        declared_at = json.loads((case/'declaration-capture.json').read_text())['declared_at_utc']
        assert len(rows) == 2
        for row in rows:
            assert row['settings'] == {'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'}
            assert datetime.datetime.fromisoformat(declared_at) < datetime.datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'))
            assert sha(case/row['dispatch_path']) == row['dispatch_sha256']
            assert sha(case/row['known_readable_prompt_path']) == row['known_readable_prompt_sha256']
            prompt = (case/row['known_readable_prompt_path']).read_text()
            assert value in prompt and '/tmp/development-review-19-' in prompt
    for axis,digest in declared['known_prompt_sha256'].items():
        assert sha(CASE/f'{axis}-c4-input.txt') == digest,axis
    followup = json.loads((CASE/'followup-dispatches.json').read_text())
    assert sha(CASE/followup['known_readable_author_text_path']) == followup['known_readable_author_text_sha256']
    parent = json.loads((EV/'19-review-capture.json').read_text())
    for name,digest in parent['sha256'].items():
        assert sha(EV/name) == digest,name
    for row in parent['capture_mapping']:
        assert sha(EV/row['retained_path']) == row['sha256'],row
    root_observation = json.loads((EV/'19-repair-root-path-capture.json').read_text())
    for row in root_observation['mapping']:
        assert sha(EV/row['retained_path']) == row['sha256'],row
    assert root_observation['caller_source_sha256'] == old_manifest['cases/b7/caller.py']
    anchors = runpy.run_path(str(EV/'16-check.py'))['anchors']
    docs = [ROOT/name for name in AUTHORING+ROUTES]
    docs += [EV/'19-repair-report.md',EV/'19-finding-history.md',ROOT/'.scratch/ticket-harness/reviews/ticket-19.md']
    docs += list(SECOND.glob('*.md')) + list(THIRD.glob('*.md')) + list(CASE.glob('*.md'))
    # Original raw reports retain original link origins/renamed capture mapping;
    # validate their attachment hashes above, never rewrite or reinterpret links.
    docs = [p for p in docs if not p.name.endswith(('-raw.md','-reviewer-saved.md'))]
    links = []
    for path in docs:
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$','',path.read_text(),flags=re.M|re.S)
        text = re.sub(r'`[^`\n]+`','',text)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',text):
            if re.match(r'[a-z]+://',href):
                continue
            name,_,fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$','',name)
            target = (path.parent/name).resolve() if name else path
            assert target.exists(),(path,href)
            if fragment:
                assert fragment in anchors(target),(path,href)
            links.append({'from':str(path.relative_to(ROOT)),'href':href})
    for name in ROUTES:
        assert 'reviewer-evaluation.md' in (ROOT/name).read_text(),name
    assert '19-evaluation-g4' in (ROOT/'docs/agents/reviewer-evaluation.md').read_text()
    observed = json.loads((SECOND/'control-observation.json').read_text())
    assert observed['G2']['input_isolated'] and observed['G2']['snapshot_isolated']
    assert observed['G2']['source_sha256'] == manifest['cases/h8/attempt.py']
    preflight = json.loads((EV/'19-repair-control-preflight-results.json').read_text())['sources']
    assert preflight == third_manifest
    assert json.loads((EV/'19-repair-path-preflight-results.json').read_text())['candidate_sources'] == manifest
    syntax_paths = list(EV.glob('19-repair-*.py'))
    syntax_paths += [p for case in [SECOND,THIRD,CASE] for p in case.glob('*.py')]
    syntax_paths += list((CASE/'snapshot/cases').rglob('*.py'))
    for path in syntax_paths:
        ast.parse(path.read_text(),filename=str(path))
    result = {'result':'pass','recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'baseline':BASE,'rejected_source':REJECTED,'head_before_checkpoint':git('rev-parse','HEAD'),
        'scope':'Standalone guidance/evaluation repair; no production behavior/tests/runtime changes or judgment scoring',
        'protected_rejected_paths':len(old_paths-set(AUTHORING)),'changed_original_paths':sorted(modified),
        'corpora':{'C1_G1':old_id,'C2_G2':second_id,'C3_G2':third_id,'C4_G2':corpus},'corpus_files_each':len(manifest),'exact_snapshot_delta':sorted(delta),
        'checked_sources':{str(p.relative_to(ROOT)):sha(p) for p in docs},'local_links':links,
        'retained_new_evidence':{str(p.relative_to(ROOT)):sha(p) for case in [SECOND,THIRD,CASE] for p in sorted(case.rglob('*')) if p.is_file()},
        'repair_evidence_identities':{p.name:sha(p) for p in sorted(EV.glob('19-repair-*'))
                                      if p.is_file() and p.suffix != '.log'
                                      and not p.name.startswith('19-repair-check-results-')},
        'repair_helpers':{p.name:sha(p) for p in [Path(__file__),EV/'19-repair-run-checks.sh']},
        'python_syntax_files':len(syntax_paths),
        'immutable_capture_whitespace_exception':{'path':str(saved_capture.relative_to(ROOT)),
            'sha256':sha(saved_capture),'trailing_LF_bytes':2,
            'scope':'Only blank-at-EOF allowance on this exact frozen saved report; all other whitespace checked, every other path uses default check. Full staged default exit2 retained in 19-repair-stage-check.json/log.'},
        'initial_review_capture_sha256':sha(EV/'19-review-capture.json'),
        'limits':'Hash/link/routing/protection audits and one fixture observation do not establish reviewer judgment; actual independent reports and manual adjudication are separate.'}
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    target = EV/f'19-repair-check-results-{stamp}.json'
    assert not target.exists()
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':'pass','protected_paths':result['protected_rejected_paths'],'corpus':corpus,'local_links':len(links),'result_path':str(target.relative_to(ROOT))},indent=2))
if __name__ == '__main__':
    main()
