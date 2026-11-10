# Assignment capture

All three assignments used fresh `fork_turns: none` contexts and saved original
outputs at predetermined unique /tmp paths before parent aggregation/copying.
The tool returns canonical task names, not separate opaque IDs. Model inherited
the parent session; exact backend, active-context and delivered settings telemetry
were unavailable. This record reports configured settings and supplied paths,
not enforced isolation or proof of complete backend delivery. Agents share the
filesystem and were instructed not to read sibling reports or mutate source.

| Assignment | Configuration | Saved input | Original output destination |
| --- | --- | --- | --- |
| `/root/preparation_exercise` | Fresh; reasoning inherited, exact level unavailable | [Scenario facts](scenarios.md), actual implementation/testing/ownership/record instructions; no parent expected answers or conclusions | `/tmp/workflow-efficiency-exercise-original.md`, retained as [exercise original](exercise-01-original.md) |
| `/root/workflow_spec` | Fresh; reasoning High requested | [Spec prompt](spec-01-prompt.md) and [shared brief](review-brief.md) | `/tmp/workflow-efficiency-spec-01-original.md` |
| `/root/workflow_standards` | Fresh; reasoning High requested independently | [Standards prompt](standards-01-prompt.md) and shared brief | `/tmp/workflow-efficiency-standards-01-original.md` |

Spec dispatch text: “Read and execute the saved fresh Spec assignment at
/home/ajkerr1/development/agentic_template/.scratch/workflow-efficiency/evidence/spec-01-prompt.md.
Its review-brief.md supplies the exact committed source, original baseline,
originating requirements, relevant contracts, settings limits and allowed side
effects. No sibling reports or further agents. Keep the source unchanged. Save
original output to the requested /tmp path and return path/result.” Standards
received the same text with its axis and corresponding prompt path.

The exercise dispatch supplied the same scope described in its original report:
read the five hypothetical scenarios and actual required instructions; explain
actions/verification/evidence; no implementation, dispatch, repository writes,
parent conclusions, sibling results or previous campaign; save complete output to
the named /tmp path and report ambiguities/settings limits. The exercise's own
original report records what it inspected and the exact instruction digests.

Reviewers were launched only after checkpoint commit
`221bc551cb931998b0250a806309aa22b8bd41b7`, with fixed baseline
`54acbaad0b101b9f1e13fd3d2e518eed1fd75fb5`. The independent exercise had inspected
the same seven instruction/handoff file bytes before commit, with digests; it
did not inspect or validate the later environment addition. [Source hashes](validation-03-05.stdout)
and [assignment instruction hashes](assignment-instructions.sha256) retain content
identity. Later bookkeeping does not change the assessed procedure.

At dispatch, both review reports were absent. No sibling current-round report was
supplied. Originals will be preserved before aggregation or assessed-source edits.
