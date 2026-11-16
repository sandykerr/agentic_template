"""Validate scoped completion/handoff records without replaying runtime checks."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

root = Path.cwd()
feature = root / ".scratch/ticket-harness"
folder = feature / "evidence/ticket-25"
phase = sys.argv[1]
assert phase in {"bookkeeping", "handoff"}
base = [str(root / ".venv/bin/python"), "-m", "ticket_harness.evidence", "--feature", str(feature)]
allocation = json.loads(subprocess.check_output(base + ["allocate", "--ticket", "25",
    "--purpose", f"Scoped ticket25 {phase} consistency and navigation validation",
    "--producer", phase], text=True))
destination = Path(allocation["destination"])
ticket = feature / "issues/25-guide-ticket-and-shared-evidence-creation.md"
original = (folder / "instructions-current/ticket.md").read_text()
current = ticket.read_text()
criteria = lambda text: text.split("## Acceptance criteria\n", 1)[1].split("\n## Verification", 1)[0]
assert criteria(current).replace("- [x]", "- [ ]") == criteria(original)
assert criteria(current).count("- [x]") == 7 and "- [ ]" not in criteria(current)
assert "**Status:** completed" in current and "ready-for-agent" in current
assert "**Blocked by:**" in current and "febd863" in current
binding = json.loads((folder / "25-repair1-committed-source-binding.json").read_text())
assert binding["all_checks_passed"] and binding["all_source_matches"]
for name, identity in binding["committed"].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == identity["tested_sha256"], name
assert not subprocess.check_output(["git", "diff", "febd86321851e2acec994237f9d1a1adea824c55", "--", "ticket_harness", "tests", "pyproject.toml", "requirements-uv.txt"], text=True)
for line in (folder / "25-review-round2-digests.sha256").read_text().splitlines():
    digest, name = line.split("  ", 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest
sources = [ticket, folder / "25-completion.md", feature / "reviews/ticket-25.md",
           feature / "reviews/EC1-capture-architecture-01.md"]
if phase == "handoff":
    prompt = root / "next_agent_prompt.md"
    assert prompt.read_text().startswith("Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/26-")
    assert "EC1" in prompt.read_text() and "250" in prompt.read_text()
    sources.append(prompt)
else:
    with (destination / "prior-next_agent_prompt.md").open("xb") as output:
        output.write((root / "next_agent_prompt.md").read_bytes())
links = []
for source in sources:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text()):
        if "://" in target:
            continue
        path, _, anchor = target.partition("#")
        resolved = (source.parent / path).resolve() if path else source
        assert resolved.exists(), (source, target)
        if anchor and resolved.suffix == ".md":
            headings = [re.sub(r"[^\w\s-]", "", line.lstrip("# ").lower()).replace(" ", "-")
                        for line in resolved.read_text().splitlines() if line.startswith("#")]
            assert anchor in headings, (source, target, "missing anchor")
        links.append({"source": str(source.relative_to(root)), "target": target})
for name in ("ticket-25.md", "EC1-capture-architecture-01.md"):
    text = (feature / "reviews" / name).read_text()
    assert "**Review lifecycle:** completed" in text
    assert "**Unresolved findings:** None" in text
assert "| 24 | completed | EC1 |" in (feature / "README.md").read_text()
result = {"phase": phase, "result": "passed", "assessed_product_revision": binding["implementation_revision"],
    "current_head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    "criterion_count": 7, "links_checked": links,
    "source_files": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    "scope": "Bookkeeping/handoff consistency, original report identities and unchanged verified product. No runtime suite replay or human milestone acceptance."}
with (destination / "validation.json").open("x") as output:
    json.dump(result, output, indent=2)
with (destination / "validator.py").open("xb") as output:
    output.write(Path(__file__).read_bytes())
payloads = [p.name for p in destination.iterdir() if p.is_file() and p.name != "allocation.json"]
registered = subprocess.run(base + ["register", "--allocation", allocation["allocation"],
    *[arg for name in payloads for arg in ("--file", name)],
    "--source-version", f"product {binding['implementation_revision']}; current_head {result['current_head']}; administrative input identities in validation.json",
    "--activity", f"25-validate-records.py {phase}: criterion, status, source/report identity, relative links/anchors and review/index checks",
    "--result", "passed"], capture_output=True, text=True)
assert registered.returncode == 0, registered.stderr
with (folder / f"25-{phase}-validation.json").open("x") as output:
    json.dump({"allocation": allocation, "result": "passed", "registration_returncode": registered.returncode,
               "link_count": len(links)}, output, indent=2)
print(json.dumps({"allocation": allocation, "result": "passed", "link_count": len(links)}))
