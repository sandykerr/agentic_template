# Ticket 24 — repair 1 canonical review packet

Review the whole original ticket from fixed baseline `ed017ae0c2b96769f31c710cfb4ff4708989b446` against the repair commit supplied by root. Rejected source is `65951f6db43fbd2299aa105f3f409eaacd85ec24`. [Implementation/ownership/coverage report](24-repair1-report.md) explains both claimed repairs, changed/unchanged owners, all four start/final risk triggers (No), inspected/omitted scope, new regression value and limits. Worker settings: fresh GPT-6.1 Sol Medium, advisory <=250000 active context; backend delivery/enforcement/telemetry unavailable. Root supplies separate fresh High assignments and actual source identity; this file assigns no reviewer and claims no independent fix verification.

Both original blocking keys remain pending root disposition and independent exact-source verification:

- `review-ticket-24/spec-01/F1`: [immutable original](24-review-spec-01.md), [own audit](24-review-spec-01-audit.json).
- `review-ticket-24/standards-01/F1`: [immutable original](24-review-standards-01.md), [own audit](24-review-standards-01-audit.json).

[Original capture](24-review-round1-capture.json), [append-only finding history](24-finding-history.md), [repair context identity audit](24-repair1-start.json). Original baseline and reports are preserved; neither a worker claim nor a mechanical pass marks a finding fixed. Independently assess the final source and its callers/writers/restoration, including both alias directions/chains, direct-ref guards, actual Git write behavior and its limits; no prescribed result follows from this packet.

Final verification: **556 passed in 842.52s**; strict mypy, Ruff lint/format and both whitespace commands passed. No runtime/test/wayfinding changes followed the freeze.

Final source/check/evidence entry points:

- [27 frozen source identities](24-repair1-final-source.json), [post-commit source audit](24-repair1-committed-source.json).
- [Six final commands/exits/logs](24-repair1-final-check-results.json): full pytest, strict mypy, Ruff lint/format, current and original-baseline whitespace. Exact frozen bytes checked before/after each command.
- [Development red/green commands/observations](24-repair1-development-checks.json), with phase source manifests and raw logs. The first transition red trial was interrupted (exit 130, incomplete); the bounded repeat completed seven intended failures then seven passes. The first deep-decision red trial also had one already-safe request-depth parameter, removed as redundant.
- [Captured scenario index](24-repair1-observation-index.json), [regular-file manifest](24-repair1-raw-manifest.json), [archive stream audit](24-repair1-capture-audit.json), [actual full-suite CLI/status/Git/record archive](24-repair1-final-raw.tar.gz).
- [Genuine pre-refactor checkpoint restoration provenance](24-repair1-checkpoint/restore.json), [final repair-source consumer](24-repair1-checkpoint/continuation-final.json), [consumer log](24-repair1-checkpoint/continue-final.log), [archive/audit](24-repair1-checkpoint/audit.json). Producer source and all original archives remain in [original checkpoint evidence](24-checkpoint/producer.json). New-code checkpoints are covered in the final suite's existing clean/repeated continuation and invalidation cases.
- [Installed Git semantics probe](24-repair1-git-probe.json): no-deref does not redirect the named write to a symbolic referent; matching symbols themselves can be replaced; expected-old mismatches reject. This is not an atomic direct-ref-type lock against arbitrary external mutation. The source guards validate destinations at relevant transitions; assess the actual scope against approved contracts.
- Versioned capture/check/archive/compatibility scripts in [repair tools](24-repair1-tools/prepare-tools.py); initial `24-tools`, original source manifests/review originals and original producer/consumer evidence are unchanged.

The approved public CLI/scripted external process/real isolated Git seam remains unchanged. Added scenarios cover twelve distinct uncovered failures; retained existing scenarios cover normal exact promotion, malformed/stale/replay decisions, expected-old movement, clean stop/restore, canonical gate invalidation and archived lineage. See the report's mapping and apply [testing policy](../../../docs/agents/testing.md) and [test-strategy](../../../.agents/skills/custom/test-strategy/SKILL.md).

G2 and final C5 (`332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`) are finite historical calibration, not runtime enforcement or guaranteed detection. Root still owns independent whole-ticket Spec/Standards, dispositions and completion/bookkeeping/handoff. Actual M1 cumulative assessment and human QA remain separate and unperformed; no actual promotion, push or later-milestone authorization is supplied.
