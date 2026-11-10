# Agentic Template Repo

Python development uses a reusable micromamba environment. See [Python environment setup and usage](docs/agents/python-environment.md).

This is my template for how I do agentic work. Currently, this uses Matt Pocock's skills which allow humans to "stay in the loop" while also taking advantage of the efficiency gains of automated agentic development. Commands below are in the codex `$skill` format, but other platforms may invoke skills differently.

# Basic workflow for a single feature:

## 1. Setup skills (if this is the first time using the repo)

Run: `$setup-matt-pocock-skills`. This sets up issue tracking, triaging, and documentation standards.

## 2. Brainstorming: the agent "grills" you with questions and you give answers

Run: `$grill-with-docs <prompt>`. This invokes a question-and-answer session with the LLM on a given feature; the agent will continue to ask questions until it feels that there is a "shared understanding" reached. This is useful because of 2 things:

1. It makes you really think about what you want. Sometimes you have a very concrete idea, other times it's less clear; this can make it obvious what you can decide initially versus what needs some further thought/development to develop an answer (i.e. what decisions to defer).

2. It means that the agent doesn't drift away from the intention that you, the human, have. This keeps you in the loop and understanding the code.

## 3. Write our decisions down: create a "spec doc" from the Q&A session

Run: `$to-spec <prompt>` for the issue after grilling. This creates a markdown "spec doc" encompassing the shared understanding reached after step 2.

## 4. Subdividing the project: creating tickets from the spec doc

Run: `$to-tickets <prompt>` to subdivide the spec doc into smaller tasks, designed for a small, efficient context window.

This step is quite crucial in an efficient agentic workflow. Due to context rot, agents are best used when short-lived; they are faster and less prone to confusion/forgetting/hallucinating.

With the tickets, agents can work autonomously on issues after we've brainstormed, given parameters we set. For example, you can require a code review afer a certain number of tickets; this helps keep you in the loop and can give you more clarity on the decisions you deferred in step 2 (grilling). This is a very granular way of batching agent work into parts you care about so that you stay in the loop.

## 5. Implementing the tickets/project spec - MOST OF THE WORKFLOW

For one local Markdown ticket, run `$implement-with-checkboxes <ticket-path>`. This wraps Matt's implementation workflow with independent review and evidence-backed acceptance checkbox updates after verification. See the [skill](.agents/skills/implement-with-checkboxes/SKILL.md) and [completion bookkeeping rules](docs/agents/issue-tracker.md#completion-bookkeeping).

Run: `$implement-spec <prompt>` to start agentic development. At this point, we are ready to start generating code, using subagents to more efficiently manage context. There are multiple advantages to subagent-driven development:

1. Parallel execution: as with any code, often there are unrelated jobs that can be done in parallel. Say that a ticket requires several files to be created and run together; the development of individual elements doesn't have to be done in serial much of the time. If there are elements that are common, one of the subagents can be used as an "oversight" or "reviewer" to make sure that the separate "modules" work together as intended. This can be done incremementally as subagents reach "checkpoints.

2. Focused: this further helps reduce context rot; single agents need to understand the entirety of a ticket's execution, which is often greater than the sum of its parts. Thus, with subagents, they can be lower reasoning, smaller models that can develop things narrowly and avoid this large-scale context demand.

## 6. Code review: see what the agents did

Run: `$code-review <prompt>` to begin the code review. This checks if features adhere to repo-specific standards as well as general code standards, and if they've diverged from the original spec. It generates several documents and a concise summary.

## 7. OPTIONAL: Audit agent execution: what worked, and what needs improvement?

Run: `$retro <prompt>` to find out what the agents had issues with and what they did well.

## Repository storage and push checks

`.scratch/` contains tracked specs, tickets, reviews, and retained evidence. Keep
required records; use lossless compression for large raw evidence and record the
original byte count and SHA-256. Avoid embedding complete command output in
identity manifests when a path and digest suffice.

Enable the repository's pre-push size check in each clone:

```bash
git config --local core.hooksPath .githooks
```

The hook checks blobs throughout outgoing history and rejects files over GitHub's
100 MiB limit, including files deleted by later commits. It requires Bash, Git,
and awk. If you already use a hooks directory, integrate this check into your
existing pre-push hook instead of replacing that configuration.

The ticket 19 round-two Spec identity JSON is now a locator for its adjacent
`.json.gz` archive. Decompress it before checking the original capture hash:

```bash
gzip -dc .scratch/ticket-harness/evidence/19-review-round2-spec-identities.json.gz > /tmp/19-review-round2-spec-identities.json
sha256sum /tmp/19-review-round2-spec-identities.json
```

The expected SHA-256 is
`94736e1eefbee407abcc23e0ece23508f2db1733af895269f332257700d20e47`.
The [history migration record](docs/history/2026-11-10-large-file-rewrite.json)
maps the original unpublished commit IDs to their replacements. Historical review
records retain their original source IDs and hashes; this storage migration does
not renew implementation verification.
