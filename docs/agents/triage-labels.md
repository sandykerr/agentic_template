# Triage labels

Use these labels when evaluating issues and assigning readiness.

| Role | Label | Meaning |
| --- | --- | --- |
| Needs evaluation | `needs-triage` | A maintainer must evaluate the issue. |
| Needs clarification | `needs-info` | More information is required. |
| Ready for an agent | `ready-for-agent` | The work is sufficiently specified for unattended agent implementation. |
| Ready for a human | `ready-for-human` | The work requires human implementation. |
| Declined | `wontfix` | The work will not be actioned. |

Record the applicable label in an open implementation ticket's `Status:` line. These labels describe triage readiness; harness execution state is recorded separately. After verified completion outside an active harness run, the [completion bookkeeping rules](issue-tracker.md#completion-bookkeeping) replace that line with `Status: completed` and retain the previous readiness label in the completion comment. `completed` is a terminal bookkeeping status, not another triage label.
