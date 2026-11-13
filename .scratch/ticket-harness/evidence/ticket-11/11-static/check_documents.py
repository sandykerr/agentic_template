"""Standalone ticket-11 evidence helper, not a harness test or runtime module."""

from pathlib import Path
import hashlib
import re
import subprocess

baseline = "5af3b343ad962b05ce44e359b791b65a8865f05a"
files = [
    Path(".agents/skills/custom/implement-with-checkboxes/SKILL.md"),
    Path(".agents/skills/custom/create-next-agent-prompt/SKILL.md"),
]
reference = Path(".agents/skills/custom/references/planning.md")
links = 0
for source in [*files, reference]:
    content = source.read_text()
    assert content.endswith("\n"), source
    assert all(line == line.rstrip() for line in content.splitlines()), source
    assert not re.search(r"^(<<<<<<< |=======|>>>>>>> )", content, re.M), source
    for href in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        location, _, fragment = href.partition("#")
        target = (source.parent / location).resolve() if location else source.resolve()
        assert target.is_file(), (source, href, target)
        if fragment:
            headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
            anchors = {
                re.sub(r"\s", "-", re.sub(r"[^\w\-\s]", "", h.lower()))
                for h in headings
            }
            assert fragment in anchors, (source, href)
        print(f"LINK {source}: {href}")
        links += 1
    print(f"SHA256 {hashlib.sha256(source.read_bytes()).hexdigest()} {source}")
    print(f"PASS whitespace/conflict markers: {source}")

unchanged_paths = [
    ".agents/skills/matt-pocock",
    ".agents/skills/microsoft",
    str(reference),
]
result = subprocess.run(
    ["git", "diff", "--exit-code", baseline, "--", *unchanged_paths],
    check=False,
)
assert result.returncode == 0, "Upstream/shared planning guidance changed"
print("PASS upstream skills and shared planning reference unchanged from baseline")
print(f"PASS {links} local file/anchor links across both skills and shared reference")
