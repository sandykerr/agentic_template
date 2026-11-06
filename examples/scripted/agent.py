"""Scripted external agent; reads one assignment, emits one JSON report."""

import json
import os
import sys
from pathlib import Path

assignment = json.load(sys.stdin)
role = assignment["role"]
report = {
    key: assignment[key] for key in ("role", "ticket", "attempt", "base_revision", "revision")
}
report["pid"] = os.getpid()
if role == "implementation":
    Path("value.txt").write_text("2\n")
    report.update(
        result="submitted",
        summary="Changed value to 2",
        changed_files=["value.txt"],
        checks=[],
        acceptance_evidence=["value.txt contains 2"],
        unresolved_questions=[],
    )
else:
    report["findings"] = []
    if sys.argv[1:] == ["--reject", role]:
        report["findings"] = [
            {
                "id": "fixture-blocker",
                "classification": "blocking",
                "location": "value.txt",
                "requirement": "Fixture gate",
                "consequence": "Scripted rejection must prevent integration",
                "evidence": "Explicit fixture rejection requested",
                "resolution": "Remove rejection for a passing fixture",
                "human_decision_needed": False,
            }
        ]
print(json.dumps(report))
