# Reusable harness with authority over local integration

This repository will own a reusable harness and shared role skills that can operate on other Git repositories. Each target repository supplies its project commands, standards, and constraints, so the execution workflow can be improved across projects while project-specific decisions stay with the project.

Once the human approves a spec and its tickets, the harness may implement tickets, run checks, request bounded repairs, and merge passing work into a local integration branch without further approval. Publishing changes remains a separate step; missing requirements, incompatible architectural choices, and exhausted repair attempts stop the affected ticket and surface a decision for the human. This permits unattended progress within approved work while preserving human ownership of scope and consequential design decisions.
