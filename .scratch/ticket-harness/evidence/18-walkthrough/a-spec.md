# Ticket A original Spec report

| Field | Value |
| --- | --- |
| Assessment | `review-18-walkthrough-a` — isolated miniature ticket A assessment |
| Report identity | `a-spec`, Spec, original attempt; assignment `/root/implement18/fixture_a_spec` |
| Actor | Codex reviewer assigned only the ticket A Spec axis |
| Actual settings | Configured model, reasoning setting, and context target are unavailable in this reviewer's exposed runtime metadata. Assignment requested fresh GPT-6.1 Sol, High reasoning, active context target ≤250k; these requested settings are not independently verified delivery evidence. No sibling report was supplied or read. |
| Original baseline | `36772524659032570d018cc164c5aa4e90068edf` |
| Assessed source | `5fa532d42205f6569918f7584cc2f6c3e52be603`; complete [ticket-a snapshot](ticket-a/) verified byte-for-byte against that commit |
| Supplied contract | [ticket-A.md](ticket-a/ticket-A.md), [CONTRACT.md](ticket-a/CONTRACT.md), assignment message, repository/user AGENTS instructions and guidance identities below |
| Prior observations | None supplied or consulted; no finding dispositions asserted |
| Output | This original report; parent must retain its digest outside this file |

## Inspected scope and substantive assessment

Inspected the full baseline-to-source diff and all six source files: `ticket-A.md`, `CONTRACT.md`, `observe.py`, empty `ticket_harness/__init__.py`, new `ticket_harness/checks.py`, and unchanged `ticket_harness/run.py`. The whole ticket includes the existing state owner, rather than only the new consumer. The baseline contract and owner have identical source identities at the assessed revision.

Ticket A requires the current check status, including after revocation, with no saved representation or new writer and the existing Run/dictionary contract. `checks_ready` (`checks.py:1–2`) returns `run.gates["checks"]` on each call. `Run.__init__` (`run.py:2–3`) establishes both canonical gate keys as false; `Run.record` (`run.py:5–6`) updates the dictionary; `Run.revoke` (`run.py:8–10`) sets the existing gates false. The observer (`observe.py:3–8`) creates a Run, reads initial false, records true through the owner, reads true, revokes through the owner and reads false. Thus the consumer observes later owner mutations with no cached status, copied gates, replacement owner, or additional writer.

The unchanged public dictionary is expressly part of ticket A's approved contract. Its visibility alone is not a Spec defect: the added operation only reads it, while the inspected writer flow uses Run operations. No persistence/restoration or invalidation representation is introduced. Revocation is the relevant invalidation operation and the new reader follows its current result. The fixture contract requires current checks and approval for readiness, but ticket A exposes check status alone; it does not claim candidate readiness or human QA acceptance. No operation in this source advances a milestone or accepts a candidate. There is no conflict with ADR-0001 or ADR-0002 within this miniature scope.

Excluded later `ticket-b`, `risk`, and `clean` source contents, sibling review reports, real harness runtime, full production verification, and future readiness/restore implementations: these are outside this ticket/source assignment. The listing and shared `sources.json` exposed later source names and identity metadata only; later source contents and behavior were not used in the conclusion. No absent future collaborator is treated as a missing ticket A requirement.

## Evidence audit

Repository guidance was read at checkout HEAD `02d76205a1c40e45c607ef2a5d11ec282393edcd`; this is the guidance repository identity, not the miniature assessed source. Read domain, ownership-review, review-records, testing, and python-environment guidance, glossary, both ADRs, report template, and the code-review skill. Applied the already-assigned Spec axis; no additional agents or sibling review were used. No tests were added or changed.

Commands and observed results (all exit 0):

```text
git bundle list-heads .scratch/ticket-harness/evidence/18-walkthrough/source.bundle
  Bundle readable; advertised branch identities are fixture metadata only.

review_fixture_git=$(mktemp -d /tmp/a-spec-review.XXXXXX)
git clone --bare --quiet .scratch/ticket-harness/evidence/18-walkthrough/source.bundle "$review_fixture_git/source.git"
  Inspection object database: /tmp/a-spec-review.6hR6AX/source.git

git --git-dir=/tmp/a-spec-review.6hR6AX/source.git rev-parse 36772524659032570d018cc164c5aa4e90068edf 5fa532d42205f6569918f7584cc2f6c3e52be603
  Both exact IDs resolve.
git --git-dir=/tmp/a-spec-review.6hR6AX/source.git log --oneline 36772524659032570d018cc164c5aa4e90068edf..5fa532d42205f6569918f7584cc2f6c3e52be603
  5fa532d Ticket A check consumer
git --git-dir=/tmp/a-spec-review.6hR6AX/source.git diff 36772524659032570d018cc164c5aa4e90068edf...5fa532d42205f6569918f7584cc2f6c3e52be603
  Adds only observe.py (9 lines), ticket-A.md (3 lines), checks.py (2 lines).

# cwd: .scratch/ticket-harness/evidence/18-walkthrough/ticket-a
PYTHONDONTWRITEBYTECODE=1 /home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python observe.py
  A check status and revocation: PASS

# cwd: repository root; same absolute interpreter, inline identity audit
# Read sources.json['ticket-a']; for every file, assert snapshot bytes equal
# git show <source>:<path> and hashlib.sha256(bytes).hexdigest() equals manifest.
  ticket-a: 6/6 snapshot files match exact committed source and manifest SHA-256
```

The inline identity audit used `pathlib`, `json`, `hashlib`, and `subprocess.check_output` with `git --git-dir=/tmp/a-spec-review.6hR6AX/source.git show` for each of the six ticket A files. It made no source changes. `PYTHONDONTWRITEBYTECODE=1` prevented observation/audit bytecode writes. The temporary Git copy is separate from the preserved snapshot.

The passing observer demonstrates only the explicit initial/record/revoke sequence. The source inspection establishes why repeated reads follow canonical state; hashes establish source identity only. No full harness suite, packaging checks, malformed-input policy, concurrency behavior, or production acceptance is claimed or required for this assigned miniature review.

SHA-256 identities captured with `sha256sum`:

| Instruction or source path | Digest |
| --- | --- |
| `docs/agents/domain.md` | `ade77403240a3a8b863ab1740b01e2e6ef12234b08b0d4f87a83897d72269876` |
| `docs/agents/ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `docs/agents/review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `docs/agents/testing.md` | `6b6b498a718205bb5fd1f0b12410623807e708f784e7d09a4bd72343b229a4ff` |
| `docs/agents/python-environment.md` | `dc357dd6bf10406d9a16b3beb40455f9262a7d3922fa4f1e138a6547a45efd8d` |
| `GLOSSARY.md` | `4b45856348181d3383d3b2416d56eb0261243ddab8507fb869dd4bdee39bdefc` |
| `docs/adr/0001-reusable-harness-and-local-integration.md` | `6e4adc64a9a454d00ca4d16649796daf525783e554d1dc892bd0654b5990e603` |
| `docs/adr/0002-human-qa-gates-feature-promotion.md` | `7f9ef955940b6a4315d9a5fc7c7279cc367043310ebd4575cee450dffd0e4982` |
| `docs/templates/reviews/report.md` | `bb0c4613964f1dc60f4ee7a618119997cf96ac3fafc3b810ed95002b2f787e76` |
| `.agents/skills/matt-pocock/code-review/SKILL.md` | `9c921a8d88138a41401d8897ca1bb852088ab1b7b605cdd04edc13e3e8aab6dd` |
| `source.bundle` | `5c8626d8074871fee2e7bdb37d13bb1628af36f535d93404341d499be457531e` |
| `ticket-a/CONTRACT.md` | `0fb78af44c59c817b758f04629a2e126ab51ee08295b2eeacf55e7224f329771` |
| `ticket-a/ticket-A.md` | `2489d63a308f3a0e6572baa283148240c1af4dbd4ba704407cb1ec4ddc349c67` |
| `ticket-a/observe.py` | `c36950e61251c05ea58e3d71ce9138fc12bab56eff2094d4ad55f4928fb8fb41` |
| `ticket-a/ticket_harness/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `ticket-a/ticket_harness/checks.py` | `9e9c2cc8052ad0477e436af4a31bb4508f4db6ad73030919fbd879babf81078c` |
| `ticket-a/ticket_harness/run.py` | `a8116ffa6a128852fb19a145abc5bef11e81ba168bee092aa5dff1ea9c7cdaaa` |

## Findings and result

Blocking findings: none. Optional suggestions: none. Consequently no report-local finding IDs or full finding keys are created.

Assessment complete for the assigned ticket A Spec scope. The implementation satisfies the inspected ticket contract at the exact assessed source. Model/reasoning/context delivery remains unverified as stated above. This report is an isolated miniature observation, not real harness acceptance, integration authorization, or human milestone QA approval.
