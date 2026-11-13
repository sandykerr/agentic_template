# Historical planning documents

These files explain the earlier plan; they are not executable assignments.

- [Spec before milestone QA](spec-before-milestone-qa.md): the contract for the completed tickets 01–09. Original source provenance is recorded in the file.
- [Original seven-ticket proposal](ticket-proposal-original.md): early decomposition superseded by the original 17 published tickets and then by the approved realignment.

Use the [feature index](../README.md), [current spec](../spec.md), and [approved implementation plan](../ticket-proposal.md) for current work. Existing completion records and immutable run snapshots retain their own source identities.

- [Open-ticket definitions before QA realignment](issues-before-milestone-qa/): superseded definitions of 10–17, retained for requirement and split provenance. Use the current issue files and published milestone plan for work.

- [Sequential ticket numbering history](ticket-numbering-history.md): previous QA-first IDs mapped to current execution-order IDs. Historical pre-QA definitions retain their original identities.

## Origin context

[Early design conversation and source URL](origin-context.tar.gz) preserve the
original `docs/chatgpt_convo.md` and `docs/context_sources.txt` bytes. These are
historical brainstorming; use the current spec and ADRs for approved decisions.
The archive has two members and is 14,044 bytes, SHA-256
`50ca8e81441db848bbaeb0705563c3296e2ce80b2a5d5b26aa9156b433a6a147`.

| Original member | Bytes | SHA-256 |
| --- | ---: | --- |
| `docs/chatgpt_convo.md` | 38,178 | `def282f588502f6cb32cd859ab339dbbbe7a9871d78f2b010f41cfaf83c99313` |
| `docs/context_sources.txt` | 43 | `3b7d191f28beb31d5091c56cfe65cecf80912070b77c7089e9004f485d99c881` |

Read either original without restoring obsolete files into `docs/`:

```bash
tar -xOzf .scratch/ticket-harness/archive/origin-context.tar.gz docs/chatgpt_convo.md > /tmp/harness-origin-conversation.md
tar -xOzf .scratch/ticket-harness/archive/origin-context.tar.gz docs/context_sources.txt
```
