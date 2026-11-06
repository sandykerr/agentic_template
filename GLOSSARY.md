# Ticket Execution

The workflow for carrying approved software work through implementation, verification, and local integration.

## Language

**Spec**:
The agreed description of intended behavior, constraints, and acceptance requirements for a body of work.
_Avoid_: Plan (when referring to required outcomes)

**Ticket**:
A bounded piece of work under an approved spec, with its own acceptance requirements and declared dependencies on other tickets.

**Approved plan**:
The human-accepted version of a spec, its tickets, milestone membership, and acceptance conditions.

**Milestone**:
A planned group of ticket outcomes with human acceptance conditions that gates further feature work and promotion.

**QA decision**:
The human's recorded acceptance or request for corrections for a specific milestone candidate.

**Skill selection**:
The skills approved for a role's work, combining its required role skills, project defaults, and any applicable ticket additions.

**Run**:
An execution of the harness against an approved spec and selected tickets, together with its recorded outcomes.

**Implementation attempt**:
A worker assignment to produce a ticket implementation and submit its result. Development and testing iterations within that assignment belong to the same attempt.

**Repair attempt**:
An implementation attempt made in response to a rejected submission, using the current changes and the reported failures as its starting point.

**Blocking finding**:
A reviewer-reported issue that must be resolved before a ticket may be integrated. It can trigger repair without immediately putting the ticket into the blocked state.

**Optional suggestion**:
A reviewer-reported improvement that does not prevent integration or require an automatic repair attempt.

**Harness**:
The system responsible for coordinating ticket execution, verification, bounded repairs, and integration for approved work.
_Avoid_: Coordinator agent, dispatcher agent

**Target repository**:
The Git repository in which the harness carries out approved work. Its project commands, standards, and constraints govern that work.
_Avoid_: Client repository

**Integration branch**:
The local destination branch into which verified changes are combined. Its role may be a feature branch or a development branch; integration does not imply permission to publish.

**Feature branch**:
The integration branch that accumulates verified ticket changes for one approved feature before milestone acceptance.

**Development branch**:
The shared integration branch that receives accepted milestone candidates from feature branches, conventionally named `dev`.

**Promotion**:
The advancement of the development branch to a verified milestone candidate accepted by the human.

**Candidate merge**:
The proposed combination of source changes and a destination branch, evaluated before that destination advances. A ticket candidate targets the feature branch; a milestone candidate targets the development branch.

