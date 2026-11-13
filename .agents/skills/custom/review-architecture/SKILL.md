---
name: review-architecture
description: Review code architecture and produce a visual HTML report in plain English, with readable, wrapped flowchart labels. Wrap Matt Pocock's architecture-review workflow; also use when simplifying or fixing figures in an existing architecture report.
---

# Review architecture

Use [Matt Pocock's architecture review](../../matt-pocock/improve-codebase-architecture/SKILL.md)
and its [HTML report reference](../../matt-pocock/improve-codebase-architecture/HTML-REPORT.md).
Read them and perform their procedures directly when no Skill tool is available.
Keep upstream files unchanged. This wrapper adds the presentation rules below;
they take precedence over upstream vocabulary and fixed diagram-size preferences.

When assessing source architecture, apply the shared
[ownership and review-scope contract](../../../../docs/agents/review-records.md#review-assignments-and-scope)
to select affected collaborators, evaluate state ownership and record inspected
and omitted scope. Report-only edits preserve the prior assessment scope and
source identity. This wrapper does not add a ticket reviewer or milestone gate.

## Review and report

Follow the upstream scope selection, domain/ADR checks, evidence gathering,
recommendation strengths, before/after figures and final recommendation. Use
[codebase design](../../matt-pocock/codebase-design/SKILL.md) to judge the work;
translate its terminology into ordinary language for the reader. Preserve the
project's domain terms, code identifiers, source locations and agreed testing
contracts. A long function is a reason to investigate, not a finding by itself.

When the user supplies a current audit or requests edits to a report, reuse that
evidence rather than automatically restarting the scan or interview. Check source
identity before describing old findings as current. Keep an edit at the requested
report path; new reports follow the upstream temporary-file convention.

## Plain English

- Explain what the code does, which code must coordinate it, what can go wrong,
  and what the proposed change makes simpler. Use short, concrete sentences.
- Write headings, badges, captions, diagram labels and benefits for the reader,
  not just the main paragraphs. Prefer “keep these rules in one place” to
  “improve locality,” “other code needs fewer setup steps” to “increase leverage,”
  and “where other code calls in” to “seam.”
- Describe “normalization” as the actual work, such as checking a plan and filling
  in defaults. Describe “canonical records” as the run's actual saved records.
  Keep a technical term when precision needs it, explaining it on first use.
- Keep code names in source references; use short descriptions inside figures.
  Say what changes and why rather than replacing jargon with vague praise.

## Readable figures

Before authoring or editing figures, read [figure layout](figure-layout.md).
Use its wrapping rules for the selected renderer, including any fallback figure.
Let node and figure height grow with their text, and stack before/after figures
on narrow screens. Wrapping, line breaks and readable type must keep the full
meaning; clipping, truncation or squeezing the text are not fixes.

Finish by checking report wording, source links and every rendered before/after
figure at desktop and narrow widths. Correct text that leaves its node, overlaps
other text or arrows, or becomes too small to read. If rendering is unavailable,
use the reference's conservative fallback and state that visual verification was
unavailable; source/markup checks alone do not establish correct wrapping.

Return the report's absolute path and open it using the upstream procedure when
possible. Report a launch failure without claiming it opened. Continue the
upstream selection/grilling workflow when the user wants to explore a finding;
an HTML edit alone does not start a new interview or approve implementation.
