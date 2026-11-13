"""Retained standalone documentation/example check; never imports the runtime.

Run from the checkout with the documented environment's Python. Outputs are
confined to evidence/16-miniature and evidence/16-check-results.json. A disposable
Git repository supplies actual source commits; all reviewers/decisions are
explicitly synthetic. This checks record mechanics, not reviewer judgment.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / ".scratch/ticket-harness/evidence"
MINI = EVIDENCE / "16-miniature"
BASELINE = "eae64ae6bce4f96aa0e2e7a3d5f63e8aba93da87"
GUIDANCE = [
    "docs/agents/review-records.md",
    "docs/agents/issue-tracker.md",
    "docs/ticket-harness.md",
    ".agents/skills/custom/implement-with-checkboxes/SKILL.md",
    ".agents/skills/custom/create-next-agent-prompt/SKILL.md",
    ".scratch/ticket-harness/reviews/README.md",
    ".scratch/ticket-harness/README.md",
    *[f"docs/templates/reviews/{name}.md" for name in
      ("assessment", "report", "history", "decision")],
]
COMMANDS: list[dict[str, object]] = []


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], cwd: Path = ROOT, **kwargs: object) -> str:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True, **kwargs)
    COMMANDS.append({"argv": args, "cwd": str(cwd), "exit": completed.returncode,
                     "stdout": completed.stdout, "stderr": completed.stderr})
    assert completed.returncode == 0, COMMANDS[-1]
    return completed.stdout.strip()


def save(path: str, body: str) -> None:
    target = MINI / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body.strip() + "\n")


def append(path: str, body: str) -> None:
    target = MINI / path
    before = target.read_bytes()
    with target.open("a") as handle:
        handle.write("\n" + body.strip() + "\n")
    assert target.read_bytes().startswith(before), path


def anchors(path: Path) -> set[str]:
    result: set[str] = set()
    counts: dict[str, int] = {}
    fenced = False
    for line in path.read_text().splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            heading = re.sub(r"[^\w\- ]", "", match[1].lower()).replace(" ", "-")
            count = counts.get(heading, 0)
            counts[heading] = count + 1
            result.add(heading if not count else f"{heading}-{count}")
    return result


def links(paths: list[Path]) -> list[dict[str, str]]:
    observations = []
    for path in paths:
        # Fenced CLI/input examples in existing guidance contain illustrative
        # Markdown destinations, not navigation links in the document itself.
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", path.read_text(), flags=re.M | re.S)
        text = re.sub(r"`[^`\n]+`", "", text)
        for href in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            if re.match(r"[a-z]+://", href):
                continue
            assert "{{" not in href, (path, "placeholder used as live link", href)
            filename, _, fragment = unquote(href).partition("#")
            target = (path.parent / filename).resolve() if filename else path
            assert target.exists(), (path, href, "missing file or directory")
            if fragment:
                assert target.is_file(), (path, href, "anchor target is not a file")
                assert fragment in anchors(target), (path, href, "missing anchor")
            observations.append({"from": str(path.relative_to(ROOT)), "href": href})
    return observations


def verify_process(repo: str, revision: str, fields: list[str]) -> None:
    """Separate mechanical verifier process, independent of the fixture repairer."""
    result = subprocess.run(["git", "show", f"{revision}:source.md"], cwd=repo,
                            text=True, capture_output=True, check=True)
    missing = [field for field in fields if f"{field}: yes" not in result.stdout]
    print(json.dumps({"actor": "synthetic-independent-verifier-process",
                      "revision": revision, "fields": fields, "missing": missing,
                      "result": "fail" if missing else "pass"}))
    raise SystemExit(bool(missing))


def build() -> dict[str, object]:
    assert not MINI.exists(), "Use a new output location or deliberately remove only this generated fixture"
    MINI.mkdir(parents=True)
    fixture_instructions = {
        path: digest(ROOT / path) for path in GUIDANCE
    }
    save("evidence/instructions.md", "# Synthetic assignment instructions\n\n"
         "All fixture assignments are scripted, not actual development reviewers.\n"
         "Intended demo settings: GPT-6.1 Sol / High / 250K context target.\n"
         "Actual executor: retained Python helper and subprocess; no model delivery claimed.\n\n"
         "The following current guidance was read by the builder; these SHA-256 identities\n"
         "identify the source used to author this example, not a captured runtime skill selection.\n\n"
         + "\n".join(f"- `{path}`: `{identity}`" for path, identity in fixture_instructions.items()))
    with tempfile.TemporaryDirectory(prefix="ticket16-source-") as temporary:
        repo = Path(temporary)
        run(["git", "init", "-b", "fixture"], repo)
        run(["git", "config", "user.name", "Synthetic Fixture Repairer"], repo)
        run(["git", "config", "user.email", "synthetic@example.invalid"], repo)
        revisions: dict[str, str] = {}
        source_texts = {
            "A": "# Synthetic source\n\nPreserves captured input: no\nRefreshes changed review: no\n",
            "B": "# Synthetic source\n\nPreserves captured input: yes\nRefreshes changed review: yes\n",
            "C": "# Synthetic source\n\nPreserves captured input: yes\nRefreshes changed review: no\n",
        }
        for label, source in source_texts.items():
            (repo / "source.md").write_text(source)
            run(["git", "add", "source.md"], repo)
            run(["git", "commit", "-m", f"Synthetic source {label}"], repo)
            revision = run(["git", "rev-parse", "HEAD"], repo)
            revisions[label] = revision
            saved_source = run(["git", "show", f"{revision}:source.md"], repo)
            save(f"evidence/source-{label}.md", saved_source)
        a, b, c = (revisions[label] for label in "ABC")
        save("evidence/commits.md", "# Actual disposable Git commits\n\n"
             "These are commits of synthetic Markdown source, not runtime implementations.\n\n"
             + "\n".join(f"- {label}: `{revision}` — [saved source](source-{label}.md)"
                         for label, revision in revisions.items())
             + "\n\n```text\n" + run(["git", "log", "--format=fuller", "--reverse"], repo)
             + "\n```\n")
        for label, fields in (("B", ["Preserves captured input", "Refreshes changed review"]),
                              ("C", ["Preserves captured input"])):
            raw = run([sys.executable, str(Path(__file__).resolve()), "--verify",
                       str(repo), revisions[label], *fields])
            save(f"evidence/verification-{label}.md", f"# Verification {label}\n\n"
                 "Synthetic independent mechanical verifier subprocess; does not establish\n"
                 "actual reviewer judgment. The fixture repairer did not verify its own repair.\n\n"
                 "```json\n" + raw + "\n```\n\n"
                 f"[Exact source](source-{label}.md), [commit identity](commits.md), "
                 "[assessment](../reviews/ticket-01.md).")

    save("README.md", """# Isolated review tracker example

All reports, reviewer assignments, plan approvals and human decisions here are
**synthetic**. Only disposable Git commits, source snapshots and mechanical check
observations are real. This is saved Markdown illustrating the
[record contract](../../../../docs/agents/review-records.md); it neither accepts
real risk nor completes ticket 16, calibration or a development milestone.

## Originating work

- [Ticket 01](issues/01-preserve-input.md) and [optional follow-up 02](issues/02-polish.md).
- [Milestone MX](milestones.md), with a separate QA decision still absent.
- [Ticket assessment](reviews/ticket-01.md): Spec and Standards reports share one work item.
- [Cross-ticket assessment](reviews/architecture-MX.md): its own review ID, no ticket number.
- [Exact source commits](evidence/commits.md) and [instruction identities](evidence/instructions.md).

## Six navigable histories

| Case | Concern | History and outcome |
| --- | --- | --- |
| Fixed finding | [Spec F1](evidence/spec-01.md#f1) | [Independent exact repair and revalidation](reviews/history.md#e05) |
| Deferred optional finding | [Spec F2](evidence/spec-01.md#f2) | [Linked follow-up](reviews/history.md#e06) |
| Explicit human risk decision | [Spec F3](evidence/spec-01.md#f3) | [Awaiting decision](reviews/history.md#e07) then [synthetic decision](reviews/risk-decision.md) |
| Duplicate local IDs | [Spec F1](evidence/spec-01.md#f1) and [Standards F1](evidence/standards-01.md#f1) | [Distinct full keys](reviews/ticket-01.md#current-findings) |
| Reopened changed source | [Standards F1](evidence/standards-01.md#f1) | [Original fix](reviews/history.md#e04), [new report](evidence/standards-02.md#f1), [reopened event](reviews/history.md#e09) |
| Completed review, outstanding findings | [Ticket assessment](reviews/ticket-01.md) | [Unresolved current concern](reviews/history.md#e09) and [pending milestone assessment](milestones.md) |

The helper records hashes before history/index changes and verifies original
reports/evidence stay unchanged. It records append-only prefix preservation for
history events, resolves these links/anchors, and retains commands/results in
the [check output](../16-check-results.json). Scripted observations test record
mechanics only, not reviewer effectiveness or runtime enforcement.
""")
    save("issues/01-preserve-input.md", f"""# 01: Preserve captured input (synthetic)

**Status:** ready-for-agent

**Plan:** synthetic-plan-v1, synthetic approval assumed only for this example.
**Milestone:** [MX](../milestones.md).

Authorized repair changes the two synthetic source statements to yes. Initial
source `{a}`, repair `{b}`, later changed source `{c}` are [saved](../evidence/commits.md).
This readiness label is unaffected by the review lifecycle.

## History

- [Ticket assessment](../reviews/ticket-01.md), [original concern](../evidence/spec-01.md#f1),
  [repair and verification](../reviews/history.md#e03).
- [Cross-ticket assessment](../reviews/architecture-MX.md) links this ticket and follow-up.
""")
    save("issues/02-polish.md", """# 02: Polish optional wording (synthetic)

**Status:** ready-for-agent
**Milestone:** [MX](../milestones.md).

Optional follow-up to [Spec F2](../evidence/spec-01.md#f2),
[deferral reason](../reviews/history.md#e06) and [originating ticket](01-preserve-input.md).
No implementation or completion is claimed. Creating this linked follow-up
does not invent a blocker or authorize scope expansion.
""")

    report_header = f"""**Synthetic report:** scripted snapshot; not an actual reviewer assessment.

**Assessment:** [review-ticket-01](../reviews/ticket-01.md).
**Fixed baseline:** `{a}`.
**Instructions:** [retained instruction identities](instructions.md).
**Settings:** intended GPT-6.1 Sol / High / 250K; actual executor is the
retained scripted helper, no real model assignment claimed.
**Evidence/source identities:** [commits and snapshots](commits.md); SHA-256
capture identities are retained in the [external manifest](../manifest.json).
"""
    save("evidence/spec-01.md", f"""# Spec report spec-01

{report_header}
**Report/assignment:** spec-01 / synthetic-spec-assignment-01 / Spec attempt 1.
**Assessed source:** `{a}`.
**Inspected:** source.md, captured-input preservation statement.
**Omitted:** runtime, all real code; not part of this synthetic record example.
**Assumptions:** source statements stand in for behavior; no runtime proof.

## F1

Full key: `review-ticket-01/spec-01/F1`. Blocking: captured inputs can change.
Source A says preservation is no. Repair the authorized statement to yes and
verify the exact source independently. [Disposition history](../reviews/history.md#e01).

## F2

Full key: `review-ticket-01/spec-01/F2`. Optional: clearer wording would help.
No correctness consequence or integration blocker. [History](../reviews/history.md#e06).

## F3

Full key: `review-ticket-01/spec-01/F3`. Optional consequential risk: humans may
mistake simulated evidence for runtime proof. Require an explicit decision for
the demo's labelled presentation at C. [History](../reviews/history.md#e07).

## Result

Assessment report completed. F1 requires repair; F2/F3 remain visible. This is
the original observation, independent of later dispositions.
""")
    save("evidence/standards-01.md", f"""# Standards report standards-01

{report_header}
**Report/assignment:** standards-01 / synthetic-standards-assignment-01 / Standards attempt 1.
**Assessed source:** `{a}`.
**Inspected:** source.md, changed-source review freshness statement.
**Omitted:** real ownership/workflow analysis and runtime; synthetic record scope.
**Assumptions:** the source statement represents freshness for this example only.

## F1

Full key: `review-ticket-01/standards-01/F1`. Blocking: changed-source review is
not refreshed. Source A says refresh is no. Authorized repair sets it to yes.
This local F1 is distinct from Spec F1. [History](../reviews/history.md#e02).

## Result

Report complete with F1 outstanding at A. Later observations append separately.
""")
    immutable_before = {str(p.relative_to(MINI)): digest(p)
                        for p in (MINI / "evidence").glob("*.md")}
    save("reviews/history.md", "# Finding history: review-ticket-01\n\n"
         "All actors/decisions are synthetic. Events append in order; current view is in\n"
         "the [assessment](ticket-01.md). Source IDs and commit evidence are\n"
         "[retained](../evidence/commits.md). The real contract is\n"
         "[here](../../../../../docs/agents/review-records.md).")
    events: list[dict[str, str]] = []

    def event(number: str, report: str, local: str, disposition: str,
              revision: str, reason: str, previous: str, verification: str,
              decision: str = "Not required: authorized repair or optional in-scope follow-up.",
              ticket: str = "[Authorized repair ticket 01](../issues/01-preserve-input.md)",
              commit: str = "Pending: no repair committed for this observation.") -> None:
        key = f"review-ticket-01/{report}/{local}"
        body = f"""## {number}

| Field | Value |
| --- | --- |
| Finding | `{key}` — [original concern](../evidence/{report}.md#{local.lower()}) |
| Disposition | {disposition} |
| Actor and role | synthetic-record-author, evidence recorder; human decisions separately attributed |
| Affected revision | `{revision}` |
| Reason and evidence | {reason} |
| Previous / superseded observation | {previous} |
| Repair or implementation ticket | {ticket} |
| Repair commit | {commit} |
| Independent verification | {verification} |
| Human decision / amendment | {decision} |
| Milestone assessment | [MX review status](../milestones.md#assessment); cumulative assessment not yet performed |
| Next action | See disposition reason and [current summary](ticket-01.md#current-findings); eligibility remains separate |
"""
        append("reviews/history.md", body)
        events.append({"event": number, "key": key, "disposition": disposition,
                       "revision": revision})

    event("E01", "spec-01", "F1", "open", a,
          "Blocking: source A fails preservation. Worker-only assertion would not justify fixed.",
          "Initial immutable observation.", "Pending independent exact-revision verification.")
    event("E02", "standards-01", "F1", "open", a,
          "Blocking: source A does not refresh changed-source review.",
          "Initial immutable observation; distinct from Spec F1.", "Pending.")
    event("E03", "spec-01", "F1", "fixed", b,
          "Blocking concern repaired within ticket 01's authorized scope; source B preserves input.",
          "[E01](#e01)", "[Independent verifier process at exact B](../evidence/verification-B.md)",
          commit=f"`{b}` — [actual Git commit](../evidence/commits.md)")
    event("E04", "standards-01", "F1", "fixed", b,
          "Blocking freshness concern repaired at B.", "[E02](#e02)",
          "[Independent verifier process at exact B](../evidence/verification-B.md)",
          commit=f"`{b}` — [actual Git commit](../evidence/commits.md)")
    event("E05", "spec-01", "F1", "fixed", c,
          "Source changed to C: relevant independent revalidation confirms preservation at C; B evidence alone was insufficient.",
          "[E03](#e03)", "[Independent verifier process at exact C](../evidence/verification-C.md)",
          commit=f"Repair `{b}`, revalidated current commit `{c}` — [identities](../evidence/commits.md)")
    event("E06", "spec-01", "F2", "deferred to linked ticket", c,
          "Optional wording suggestion deferred within approved demo scope; no blocker or risk accepted.",
          "Initial immutable optional observation.", "Not applicable: follow-up is unimplemented.",
          ticket="[Optional ticket 02](../issues/02-polish.md)",
          commit="Not applicable: optional deferral, no implementation claimed.")
    event("E07", "spec-01", "F3", "awaiting human decision", c,
          "Optional consequential demo-presentation risk: agent can propose labels but cannot accept the risk.",
          "Initial immutable optional risk observation.", "Not applicable: risk decision, not a fix.",
          decision="[Question and proposed options](risk-decision.md); decision pending at this event.",
          commit="Not applicable: decision requested, no repair claimed.")
    save("reviews/risk-decision.md", f"""# Human review decision DEMO-RISK-01

**SYNTHETIC HUMAN DECISION — NO REAL HUMAN ACCEPTANCE.**

| Field | Value |
| --- | --- |
| Origin | [Assessment](ticket-01.md), `review-ticket-01/spec-01/F3`, [concern](../evidence/spec-01.md#f3), [ticket](../issues/01-preserve-input.md), [MX](../milestones.md) |
| Affected source and contract | `{c}`, synthetic-plan-v1; labelled record example only |
| Question and consequence | May simulated record evidence be shown with explicit labels despite risk of confusing it with runtime proof? |
| Evidence and options | [Original report](../evidence/spec-01.md#f3); either retain labelled simulation or postpone presentation |
| Human attribution and context | Fictional Human Demo Owner, synthetic conversation; no real human or timestamp attributed |
| Actual decision | Synthetic statement: “Accept the presentation risk only for this clearly labelled example; runtime correctness and real milestones remain unaccepted.” |
| Required amendment | Not required: optional presentation risk within existing synthetic scope; no blocker deferral, ownership change or expanded scope. A real contract change would need explicit approved amendment. |
| Recorded by | synthetic-record-author; distinct from fictional decision-maker |
| Follow-through | [E08](history.md#e08); no repair/commit/verification claimed for risk acceptance |
| Milestone assessment / QA | [MX assessment pending](../milestones.md#assessment); QA decision absent |

This example does not accept any real risk or authorize integration/promotion.
""")
    event("E08", "spec-01", "F3", "accepted with reason", c,
          "Synthetic human accepts only explicitly labelled demo presentation risk, not runtime correctness.",
          "[E07 awaiting decision](#e07)", "Not applicable: human risk decision, not repair verification.",
          decision="[Attributed synthetic decision, reason and limits](risk-decision.md)",
          commit="Not applicable: no fix asserted.")
    save("evidence/standards-02.md", f"""# Standards report standards-02

{report_header}
**Report/assignment:** standards-02 / synthetic-standards-assignment-02 / Standards attempt 2.
**Assessed source:** `{c}`.
**Inspected:** source.md at C, refresh statement and prior finding history.
**Omitted:** real code/runtime and all other concerns; synthetic record scope.
**Assumptions:** source statements model the concern only.

## F1

Full key: `review-ticket-01/standards-02/F1`. Blocking: C again says refresh is no.
Reopens/supersedes the current observation of
[`review-ticket-01/standards-01/F1`](standards-01.md#f1).
[B verification](verification-B.md) remains valid only for B, not C.
[Reopened history](../reviews/history.md#e09) retains the old fixed event.

## Result

Assessment complete with current blocker. Source-change revalidation finds the
concern persists; a further authorized repair and independent verification are pending.
""")
    event("E09", "standards-01", "F1", "open", c,
          "Blocking concern reopened after changed source C; [new independent scripted observation](../evidence/standards-02.md#f1) has full key review-ticket-01/standards-02/F1. B verification is stale for current source.",
          "[E04 prior fixed observation](#e04)",
          "Revalidation at C reports failure in standards-02; exact repaired-C verification pending.",
          decision="No human decision/amendment authorizes blocker deferral; blocker remains.",
          commit=f"Prior repair `{b}`, changed commit `{c}` — [identities](../evidence/commits.md)")
    save("reviews/ticket-01.md", f"""# Review assessment review-ticket-01

**Review lifecycle:** completed

| Field | Value |
| --- | --- |
| Identity, purpose and scope | review-ticket-01; ticket assessment; preserve input and review freshness |
| Origin | [Ticket 01](../issues/01-preserve-input.md), synthetic-plan-v1, [MX](../milestones.md) |
| Fixed baseline | `{a}` retained across all reports |
| Assessed source | spec-01/standards-01 at `{a}`; repair observations at `{b}`; standards-02/revalidation at `{c}` |
| Reviewer assignments | Synthetic Spec/Standards assignments identified in immutable reports; intended model High GPT-6.1 Sol / 250K, actual scripted executor; no real model delivery |
| Instructions | [Current guidance paths and SHA-256 identities](../evidence/instructions.md) |
| Inspected scope | Synthetic source preservation and freshness statements; report-specific scope below |
| Omitted scope and assumptions | All real runtime/code; statements stand in for behavior; no reviewer judgment proven |
| Reports and evidence | [Spec 01](../evidence/spec-01.md), [Standards 01](../evidence/standards-01.md), [Standards 02](../evidence/standards-02.md), [capture manifest](../manifest.json) |
| History and decisions | [Append-only finding history](history.md), [synthetic risk decision](risk-decision.md) |
| Milestone assessment | [Separate cross-ticket work item](architecture-MX.md), [MX pending assessment](../milestones.md#assessment) |

## Current findings

Mutable summary as of C; original classifications and snapshots remain visible.

| Full key and original concern | Original classification | Current disposition / source | Latest history | Next action |
| --- | --- | --- | --- | --- |
| [review-ticket-01/spec-01/F1](../evidence/spec-01.md#f1) | blocking | fixed at C, independently revalidated | [E05](history.md#e05) | No current preservation repair |
| [review-ticket-01/spec-01/F2](../evidence/spec-01.md#f2) | optional | deferred to linked ticket at C | [E06](history.md#e06) | [02](../issues/02-polish.md) remains outstanding |
| [review-ticket-01/spec-01/F3](../evidence/spec-01.md#f3) | optional consequential risk | accepted with reason at C | [E08](history.md#e08) | Preserve synthetic decision limits |
| [review-ticket-01/standards-01/F1](../evidence/standards-01.md#f1), [superseding review-ticket-01/standards-02/F1](../evidence/standards-02.md#f1) | blocking | open at C; B fix stale | [E09](history.md#e09) | Further authorized repair and independent verification |

**Unresolved findings:** review-ticket-01/standards-01/F1 (reopened observation
review-ticket-01/standards-02/F1); review-ticket-01/spec-01/F2 remains deferred and
tracked in ticket 02. No disappearance merely because assessment is completed.

**Integration/milestone eligibility:** blocked by reopened freshness concern;
cumulative MX assessment and real human QA absent. Completion grants no authority.

## Assessment history

- synthetic-record-author: planned assessment against A, fixed original baseline.
- synthetic-record-author: in progress; independent scripted Spec/Standards reports saved.
- synthetic-record-author: completed at C after standards-02; [E01–E09](history.md)
  retain fixes, deferral, decision and reopening; unresolved work remains visible.
""")
    save("reviews/architecture-MX.md", f"""# Review assessment review-MX-architecture-01

**Review lifecycle:** planned

| Field | Value |
| --- | --- |
| Identity, purpose and scope | review-MX-architecture-01; cross-ticket cumulative assessment, not an implementation ID |
| Origin | [Ticket 01](../issues/01-preserve-input.md), [02](../issues/02-polish.md), synthetic-plan-v1, [MX](../milestones.md) |
| Fixed baseline | `{a}` |
| Assessed source | Proposed C `{c}`; assessment not performed |
| Reviewer assignments | Not assigned; intended fresh Standards High, GPT-6.1 Sol, 250K; no actual assignment/settings claimed |
| Instructions | [Guidance identities](../evidence/instructions.md); supplied assignment absent |
| Inspected scope | None yet; planned preservation/freshness and optional wording across 01/02 |
| Omitted scope and assumptions | Entire assessment pending; no clean result inferred |
| Reports and evidence | None yet; [ticket evidence](ticket-01.md) is prior context, not this assessment's report |
| History and decisions | Carry [ticket finding history](history.md), [risk limits](risk-decision.md) |
| Milestone assessment | [MX assessment](../milestones.md#assessment), not performed |

## Current findings

Own report findings: none yet because assessment is unperformed. Carried unresolved
keys: review-ticket-01/standards-01/F1 (reopened via standards-02/F1) and deferred
review-ticket-01/spec-01/F2. [Current evidence](ticket-01.md#current-findings).

**Integration/milestone eligibility:** pending; no QA request/acceptance or promotion.

## Assessment history

- synthetic-record-author: planned at C; retained baseline A; no review performed.
""")
    save("milestones.md", """# Synthetic milestone MX

**Approved plan:** synthetic-plan-v1 (synthetic assumption only).
**Membership:** [01](issues/01-preserve-input.md), [02](issues/02-polish.md).
**QA status:** not requested or accepted; no candidate or human QA decision exists.

## Assessment

[Cumulative work item](reviews/architecture-MX.md) is planned, not performed.
[Ticket assessment](reviews/ticket-01.md) is completed with
[reopened blocking concern](reviews/history.md#e09), optional deferred work and
[limited synthetic risk decision](reviews/risk-decision.md). Further authorized
repair/independent verification and cumulative assessment remain pending.
No integration, QA readiness or promotion is authorized by these labels.
""")
    immutable_after = {path: digest(MINI / path) for path in immutable_before}
    assert immutable_before == immutable_after, "Original report/evidence was rewritten"
    report_paths = list((MINI / "evidence").glob("*.md"))
    manifest = {str(path.relative_to(MINI)): digest(path) for path in report_paths}
    (MINI / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return {"source_revisions": revisions, "events": events,
            "immutable_before": immutable_before, "immutable_after": immutable_after,
            "manifest": manifest}


def check_saved() -> dict[str, object]:
    assert "{{" not in "".join(path.read_text() for path in MINI.rglob("*.md"))
    manifest = json.loads((MINI / "manifest.json").read_text())
    assert all(digest(MINI / path) == expected for path, expected in manifest.items())
    history = (MINI / "reviews/history.md").read_text()
    summary = (MINI / "reviews/ticket-01.md").read_text()
    for event_id in range(1, 10):
        assert f"## E{event_id:02}" in history
    keys = set(re.findall(r"Full key: `([^`]+)`", "\n".join(
        path.read_text() for path in (MINI / "evidence").glob("*.md"))))
    assert len(keys) == 5, keys
    assert {"review-ticket-01/spec-01/F1", "review-ticket-01/standards-01/F1",
            "review-ticket-01/standards-02/F1"} <= keys
    assert "**Review lifecycle:** completed" in summary
    assert "open at C; B fix stale" in summary
    assert "**Status:** ready-for-agent" in (MINI / "issues/01-preserve-input.md").read_text()
    assert "**Review lifecycle:** planned" in (MINI / "reviews/architecture-MX.md").read_text()
    verification_b = (MINI / "evidence/verification-B.md").read_text()
    verification_c = (MINI / "evidence/verification-C.md").read_text()
    for verification in (verification_b, verification_c):
        assert '"result": "pass"' in verification
        assert "synthetic-independent-verifier-process" in verification
    assert "Refreshes changed review" in verification_b
    assert "Refreshes changed review" not in verification_c
    assert "Refreshes changed review: no" in (MINI / "evidence/source-C.md").read_text()
    # Exercise navigation from entry points through evidence/history to repairs,
    # exact commits, independent verification, decisions and pending milestone.
    paths = [ROOT / path for path in GUIDANCE] + list(MINI.rglob("*.md")) + [
        EVIDENCE / "16-implementation-report.md"]
    observations = links(paths)
    for path in paths:
        assert not re.search(r"^(<<<<<<< |=======\s*$|>>>>>>> )", path.read_text(), re.M), path
        assert all(line == line.rstrip() for line in path.read_text().splitlines()), path
    return {"full_keys": sorted(keys), "resolved_links": observations,
            "six_cases": {
                "fixed": "E03 exact B, E05 independent revalidation at C",
                "optional_deferred": "E06 -> issues/02-polish.md",
                "human_risk": "E07 awaiting -> synthetic decision -> E08 accepted",
                "duplicate_local_ids": "spec-01/F1, standards-01/F1, standards-02/F1 remain distinct",
                "reopened": "E04 fixed B -> standards-02 C -> E09 open; B snapshot retained",
                "completed_outstanding": "ticket assessment completed; freshness blocker + deferred optional tracked; MX pending",
            }}


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--verify":
        verify_process(sys.argv[2], sys.argv[3], sys.argv[4:])
    protected = [path for directory in ("issues", "archive")
                 for path in (ROOT / ".scratch/ticket-harness" / directory).rglob("*.md")]
    protected_hashes = {str(path.relative_to(ROOT)): digest(path) for path in protected}
    before_head = run(["git", "rev-parse", "HEAD"])
    starting_worktree = run(["git", "status", "--short"])
    (EVIDENCE / "16-check-results.json").write_text(
        json.dumps({"status": "in progress", "checked_head": before_head}) + "\n")
    generated = build() if "--build" in sys.argv else {"mode": "validate saved artifacts"}
    if "--build" in sys.argv:
        (EVIDENCE / "16-build-results.json").write_text(json.dumps(
            {"generated": generated, "commands": COMMANDS}, indent=2) + "\n")
    observations = check_saved()
    assert run(["git", "rev-parse", "HEAD"]) == before_head
    assert protected_hashes == {path: digest(ROOT / path) for path in protected_hashes}
    # Preserve upstream source byte-for-byte against the original baseline.
    assert not run(["git", "diff", BASELINE, "--", ".agents/skills/matt-pocock",
                    ".agents/skills/microsoft", "ticket_harness", "tests", "examples"])
    source_paths = [ROOT / path for path in GUIDANCE] + [Path(__file__).resolve(),
                   EVIDENCE / "16-run-checks.sh", EVIDENCE / "16-implementation-report.md"]
    result = {"baseline": BASELINE, "checked_head": before_head,
              "worktree_before_check": starting_worktree,
              "source_sha256": {str(path.relative_to(ROOT)): digest(path) for path in source_paths},
              "protected_tracker_files": len(protected_hashes), "protected_unchanged": True,
              "runtime_tests_upstream_unchanged": True, "generated": generated,
              "observations": observations, "commands": COMMANDS,
              "fixture_sha256": {str(p.relative_to(MINI)): digest(p) for p in MINI.rglob("*") if p.is_file()},
              "result": "pass"}
    (EVIDENCE / "16-check-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": "pass", "links": len(observations["resolved_links"]),
                      "cases": observations["six_cases"], "protected": len(protected_hashes)}, indent=2))


if __name__ == "__main__":
    main()
