# Evidence retention audit — physical inventory

Inventory observed 2026-11-12. Read-only inspection; no tests, replay, restoration, retention decision or existing artifact edits. The audit output directory is excluded throughout. Counts describe current checkout contents, not the Git object database.

## Exact physical inventory

| Measure | Result |
|---|---:|
| Regular files | 7,323 |
| Regular-file logical bytes | 178,555,043 |
| Allocated regular-file bytes (`st_blocks × 512`) | 195,706,880 |
| Allocated directory bytes | 3,022,848 |
| Total allocated tree bytes, excluding audit directory | 198,729,728 |
| Symlinks | 1 (9 link bytes; zero allocated blocks) |

The tracked symlink [`17-walkthroughs/case-c/case-c-report.md`](../17-walkthroughs/case-c/case-c-report.md) targets `report.md`. Following it adds one apparent file and 11,143 logical bytes: **7,324 references / 178,566,186 bytes**. That is not the physical regular-file total. No deduplication of hard links or filesystem compression was assumed; block sums are filesystem accounting, not a storage-service bill.

## Meaningful evidence families

| Family | Regular files | Logical bytes |
|---|---:|---:|
| Ticket 01–15 completion/checks/embedded observations/packages | 367 | 19,332,598 |
| Loose scenario observations and captured fixture trees (14–15) | 5,607 | 69,611,235 |
| Synthetic review records and walkthroughs (16–18) | 215 | 921,226 |
| Reviewer calibration, trials, source/guidance snapshots and identity/tool captures (19) | 475 | 27,947,418 |
| Implementation, repair, raw archives, checkpoints and verification tools (20–24) | 524 | 55,793,252 |
| M1 human review bundle | 37 | 4,076,990 |
| M1 QA and regression reproduction | 97 | 864,072 |
| Other root evidence | 1 | 8,252 |

The machine-readable [compressed detailed inventory](worker-inventory-data.json.gz) and [compact summary](worker-inventory-summary.json) gives each file’s path, logical/allocated bytes, SHA-256, Git classification and content format, plus finer top-directory families, archive member samples/largest members and duplicate groups. Family totals are disjoint; archive contents are not counted again as loose files.

## Content and evidentiary purpose

- **Early completion/check/observation records:** [`01-completion.md`](../01-completion.md) identifies scope, baseline, implementation and saved actual CLI/gate observations. [`14-fixture-observations.json`](../14-fixture-observations.json) contains tested source identity and observations, not simply a manifest. [`12-log-originals.json`](../12-log-originals.json) embeds original failed/interrupted command output. Deleting these removes historical outcome/source association and failure details; a short success summary does not retain those contents.
- **Loose scenario captures:** [`15-observations/final-suite/ticket-harness-test-6gt6q5w9.json`](../15-observations/final-suite/ticket-harness-test-6gt6q5w9.json) names the repeated-stop/checkpoint-lineage scenario and embeds a completed run record, approved-input digests, artifacts and paths. Its sibling `-files/` tree retains actual run/checkpoint/assignment/stdout/stderr material. `15-observations` is 5,443 files / 59,283,087 bytes: 2,612 JSON, 1,487 text and 1,344 empty files. `14-observations` is 164 JSON files / 10,328,148 bytes. Loss removes inspectable run state and outputs; temporary paths in summaries alone do not recover their bytes.
- **Synthetic review/workflow examples:** [`16-miniature/`](../16-miniature/) carries explicitly synthetic tickets, findings, decisions and evidence links; `16-initial-fixture.tar.gz` preserves an earlier version. [`17-walkthroughs/case-a/source.bundle`](../17-walkthroughs/case-a/source.bundle) begins `# v2 git bundle`; six such bundles preserve synthetic Git history. Walkthrough reports explain review/ownership/checkpoint behavior. Loss removes examples and their versioned source, not production execution proof.
- **Reviewer calibration:** [`19-evaluation-g5/`](../19-evaluation-g5/) includes declarations, actual reviewer text, inputs/dispatch/source records, manifests, results and guidance/source snapshots. Five evaluation directories preserve different trials; equal guidance files do not establish whole-trial equivalence. Loss removes independent judgments, failed trials, assessed source and delivered-context provenance.
- **The largest gzip is command evidence:** [`19-review-round2-spec-identities.json.gz`](../19-review-round2-spec-identities.json.gz) stores **17,029,165 compressed bytes / 220,978,737 decoded bytes**. Its decoded JSON includes review/report/source/settings/instruction identities and a large commands collection containing stdout/stderr (root independently counted 13,762 command entries). It is a compressed JSON document, not a tar archive or merely a list of hashes. Discarding or reducing it can lose captured command/tool output as well as provenance. [`19-review-round2-standards-identities.json`](../19-review-round2-standards-identities.json) similarly states exact source, requested scope and telemetry limits.
- **20–24 raw archives and manifests:** [`24-final-raw.tar.gz`](../24-final-raw.tar.gz) contains 10,446 regular members / 51,693,404 uncompressed bytes, including actual `baseline.stdout`, assignments, run artifacts and QA requests. A selected `baseline.stdout` names a Git revision. [`24-raw-manifest.json`](../24-raw-manifest.json) maps paths to hashes/sizes; it proves identity only when the corresponding contents remain accessible. Interrupted, failed, repair and resumed archives preserve distinct attempts. Loss removes exact original observations and failure/repair history.
- **Checkpoint fixture archives:** [`21-checkpoint/stopped-fixture.tar.gz`](../21-checkpoint/stopped-fixture.tar.gz) contains 335 regular files / 299,574 bytes, including a stopped-at-QA `run.json`, checkpoints, live worktree files and launch history. These are packaged live fixtures, not only compressed logs. `m1-qa-01/demo-initial-checkpoint.tar.gz` similarly includes 196 regular files / 247,653 bytes. Loss removes reconstructable inspected state/lineage; archives retaining absolute temporary paths are not claimed to be directly runnable after extraction.
- **Packaged build outputs:** both wheel files under [`15-package/`](../15-package/) and [`15-repair1-package/`](../15-repair1-package/) are ZIP containers with 14 members each: Python modules, distribution metadata, entry points and RECORD. Their same package version is not byte equality. Loss removes the actual distributable examined for installed-CLI checks; source plus build instructions is weaker evidence of those exact wheel bytes.
- **M1 frozen review/QA:** [`m1-human-review-01/renewed-source.tar.gz`](../m1-human-review-01/renewed-source.tar.gz) has 26 regular files / 353,530 bytes, including source, tests and environment. Other bundles preserve guidance, verification tools and interrupted/renewed observations. [`m1-qa-01/index-routing-repro-01/`](../m1-qa-01/index-routing-repro-01/) includes raw fixtures and four Git index binaries (`DIRC` magic), preserving caller-index before/after evidence. Loss can remove frozen exact-candidate/reproduction evidence. An artifact by itself does not establish human milestone acceptance.
- **Empty and generated files:** 1,396 zero-byte files include command stderr/whitespace outputs, which can document an observed empty stream when paired with result/command records. Ten ignored `.pyc` files are generated verification-tool bytecode. Empty files consume no regular-file blocks here, though directories and Git still have overhead. Their evidentiary roles differ; this report authorizes deletion of neither.

## Stored formats and containers

| Content format | Regular files | Stored logical bytes |
|---|---:|---:|
| JSON | 3,464 | 116,125,501 |
| Python bytecode | 10 | 45,474 |
| binary/other | 10 | 14,542 |
| empty | 1,396 | 0 |
| gzip/plain | 7 | 17,058,803 |
| gzip/tar | 49 | 39,553,145 |
| text | 2,367 | 4,996,161 |
| text (JSON-like) | 18 | 705,612 |
| zip/wheel | 2 | 55,805 |

All 49 tar.gz member lists were read in memory without extraction over originals: **104,230 regular archive members / 507,846,824 uncompressed member bytes**. Container metadata/symlinks/directories are not added to regular-member byte sums. Seven gzip streams are plain compressed text/JSON/JSONL rather than tar archives; two wheel ZIPs were listed and METADATA read. Decoded/member bytes are separate from the physical stored-file total. Format labels use magic bytes, UTF-8 decode and JSON parse, then representative content inspection; “text” is deliberately broad (Markdown, code, logs, stdout/stderr and manifests). “Binary/other” comprises six Git bundles and four Git index files. This is not exhaustive semantic validation of every JSON document.

## Exact duplication and distinct snapshots

SHA-256 over every stored regular file found **325 exact-content duplicate groups**, with **5,230,393 repeated logical bytes beyond one copy per group**. Zero-byte files participate. The symlink is excluded. This is a content-equality bound for loose stored files, not a lossless-deletion proposal: distinct paths can be part of manifests, historical snapshots or fixture identities. No complete archive/wheel files are exact loose-file duplicates.

Examples:

- Five copies of `19-evaluation*/snapshot/guidance/.agents/skills/microsoft/microsoft_oop/SKILL.md` each hash to `7d9fb19811bc83bffa964746e70e1b85757773576b5a5373ffa6edbd8ae5e481` (32,824 bytes). This demonstrates identical guidance, not identical trials.
- The final-suite repeated-stop fixture’s `checkpoints/853dd4e7eef44654b5e7f34b00ad2680.json` and `qa-checkpoint.json` are 83,036 bytes with SHA-256 `fd844a81a3bccab15c5252aab394d237c949c27d3e4823e853fe2766b1cca4c7`. Preserving both names can matter to the captured fixture.
- Selected archived `16-miniature/issues/02-polish.md` equals its loose counterpart: SHA-256 `f4e6c7f20797c1d953c7c5349d1e229460c18dc7dd16b923b3c819b60123c5cc`. Selected archived `24-review-spec-03.md` equals the loose original: `7f07c388c965c89ccdad0e546ba39bbe08604b6d25ca22839e0f0bfc46821e45`. These are individual member checks, not whole-archive equivalence.
- `23-raw-manifest.json` and `24-raw-manifest.json` have the same size (1,743,911) but different SHA-256 values (`04f5545d43ed235dbc681fac1ca9ac07b0f85a319752f258a262e0df37570aa1` and `bb969eaae3a1178e29fe0ad327b1b6f590c1b8aaef6e2d3356ae1493ed638a81`). The wheels likewise differ (`96a0b234cb8287890d957179684994e2483e24d4f2f342dbc1b1593f968f2f08` versus `1dc83a2df7a10737d415c6c3638e5dc1edbbd7e109a9753bbbc995c729b54bae`). Repeated names/sizes/versions are not duplication evidence.

Archive-member cross-container deduplication was not exhaustively hashed; no savings estimate for that is claimed. Exact matches do not determine whether path-preserving repackaging would satisfy existing manifests/history.

## Largest individual files

| Path | Stored bytes |
|---|---:|
| [19-review-round2-spec-identities.json.gz](../19-review-round2-spec-identities.json.gz) | 17,029,165 |
| [14-fixture-observations.json](../14-fixture-observations.json) | 6,203,476 |
| [19-review-round2-standards-identities.json](../19-review-round2-standards-identities.json) | 4,341,657 |
| [13-fixture-observations.json](../13-fixture-observations.json) | 4,297,835 |
| [24-repair2-resumed-repaired-final-raw.tar.gz](../24-repair2-resumed-repaired-final-raw.tar.gz) | 4,253,135 |
| [24-repair1-final-raw.tar.gz](../24-repair1-final-raw.tar.gz) | 4,196,605 |
| [23-final-raw.tar.gz](../23-final-raw.tar.gz) | 3,977,366 |
| [24-final-raw.tar.gz](../24-final-raw.tar.gz) | 3,968,518 |
| [21-final-raw.tar.gz](../21-final-raw.tar.gz) | 3,641,884 |
| [22-final-raw.tar.gz](../22-final-raw.tar.gz) | 3,638,454 |
| [20-final-raw.tar.gz](../20-final-raw.tar.gz) | 3,205,784 |
| [12-fixture-observations.json](../12-fixture-observations.json) | 2,728,923 |
| [24-resume-interrupted-failed-raw.tar.gz](../24-resume-interrupted-failed-raw.tar.gz) | 2,350,434 |
| [24-repair2-interrupted-final-raw.tar.gz](../24-repair2-interrupted-final-raw.tar.gz) | 1,957,772 |
| [24-repair2-resumed-repaired-final-manifest.json](../24-repair2-resumed-repaired-final-manifest.json) | 1,838,672 |

## Git classification and adjacent record sizes

| Current evidence regular-file status | Files | Logical bytes |
|---|---:|---:|
| ignored | 10 | 45,474 |
| tracked | 7,179 | 173,568,507 |
| untracked | 134 | 4,941,062 |

Tracked means path present in current index, without claiming contents committed or unchanged. The one tracked symlink is additional. Ignored files are the ten tool `.pyc` files. Untracked means neither in the index nor reported ignored. No evidence is presumed expendable from Git status alone.

| Adjacent tree | Files | Logical bytes | Allocated file bytes |
|---|---:|---:|---:|
| `reviews/` | 13 | 66,104 | 94,208 |
| `archive/` | 93 | 491,823 | 638,976 |
| `drafts/` | 26 | 1,794,254 | 1,851,392 |

`du -s -B1` for these adjacent trees was 98,304 (`reviews`), 667,648 (`archive`) and 1,867,776 (`drafts`), including directories. Their content was not retention-audited by this worker.

## Future policy inputs (no eligibility assigned)

Generated tool `__pycache__`/`.pyc` files are recognizable temporary cache candidates. Wheel outputs are reproducible packaging candidates in principle, but here they also identify the actual tested distributions; rebuilding does not reproduce historical observation by itself. Raw logs, failed/interrupted attempts, source/guidance snapshots and checkpoint fixtures carry historical evidence. Red/green/focused/final/repair/resume captures correspond to separate stages, sources or outcomes, so repetition is not enough to classify them as temporary. A future evidence skill can name a ticket/milestone gate, required surviving record and path-preserving archival rules for each type; this inventory assigns no cleanup eligibility or deletion authorization.

## Method, commands and limits

Read [`AGENTS.md`](../../../../AGENTS.md), [`GLOSSARY.md`](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md), [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md), [review-records guidance](../../../../docs/agents/review-records.md) and [Python environment guidance](../../../../docs/agents/python-environment.md). The guidance requires preserving original evidence and historical source identity; no retention change was requested or performed.

Used the existing absolute `.micromamba/envs/dev/bin/python` interpreter with standard-library modules only (`pathlib`, `json`, `hashlib`, `gzip`, `tarfile`, `zipfile`, `collections`, `subprocess`). Shell discovery used `find`, `rg --files`, `du`, `git ls-files` and `git status`. No dependency installation, existing helper-script execution or tests occurred.

Core measurement equivalents:

```sh
find .scratch/ticket-harness/evidence -type f -not -path '*/evidence-retention-audit-01/*' -printf '%s\t%p\n'
find .scratch/ticket-harness/evidence -type d -not -path '*/evidence-retention-audit-01*' -printf '%b\n'
git ls-files -z
git ls-files --others --ignored --exclude-standard -z .scratch/ticket-harness/evidence
du -s -B1 .scratch/ticket-harness/reviews .scratch/ticket-harness/archive .scratch/ticket-harness/drafts
```

Inventory reads each regular file and calculates `sha256(bytes)`, `len(bytes)` and `stat().st_blocks * 512`; symlinks are separated using `is_symlink()`/`lstat()`. Archive member listings use `tarfile.getmembers()` and `ZipFile.infolist()`; selected members are read with `extractfile()`/`read()`, never extracted onto originals. Plain gzip streams are decoded in memory. Filesystem measurements are not an atomic snapshot; root independently reproduced totals and identified the symlink distinction. No claim is made about validity of every reported observation, intact Git history, exact model backend delivery, complete archive reproducibility, or human acceptance. This report records what content exists and what losing it would remove.
