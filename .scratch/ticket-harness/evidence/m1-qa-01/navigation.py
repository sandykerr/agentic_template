from pathlib import Path

feature=Path('.scratch/ticket-harness')
review=feature/'reviews/README.md'
row='| [review-M1-architecture-01](M1-architecture-01.md) | Cumulative M1, baseline `1a623ba`, assessed source `d02e61e` | in progress | New Git environment/index blocker under final assessment; [QA preparation](../evidence/m1-qa-01/qa-guide.md) | Readiness held; no human acceptance |\n'
with review.open('a') as stream:
    stream.write('\n'+row)
with (feature/'README.md').open('a') as stream:
    stream.write('\n## Current M1 QA preparation\n\nHuman requested beginning QA after ticket24 on 2026-11-12. [QA guide and observations](evidence/m1-qa-01/qa-guide.md), [cumulative work item](reviews/M1-architecture-01.md), [captured source/baseline/instructions](evidence/m1-qa-01/start.json). Required assessment is in progress; a new Git environment/index finding is being retained. Candidate readiness is held and M1 remains unaccepted. The isolated demonstration is deliberately stopped. M2 stays ineligible. Historical completion evidence above retains its original scope.\n')
with (feature/'milestones.md').open('a') as stream:
    stream.write('\n## M1 QA preparation history\n\n2026-11-12: human requested beginning QA after ticket24. [Current cumulative work](reviews/M1-architecture-01.md) assesses `d02e61e` from established starting snapshot `1a623ba`; [QA guide/evidence](evidence/m1-qa-01/qa-guide.md) retains the stopped disposable demonstration. Required assessment/finding gate is pending; readiness held, no human acceptance and no M2 authorization. Approved membership, setup, actions and pass conditions above remain unchanged.\n')
for ticket in sorted((feature/'issues').glob('*.md')):
    number=int(ticket.name[:2])
    if 10<=number<=24:
        with ticket.open('a') as stream:
            stream.write('\nM1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.\n')
print('Added cumulative navigation to review index, feature index, milestones and all 15 M1 origin tickets; preserved requirements/checkboxes and existing dirty contents.')
