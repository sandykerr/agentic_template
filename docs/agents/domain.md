# Domain docs

This repository uses one domain context.

## Before exploring or designing

- Read `GLOSSARY.md` at the repository root for domain terms.
- Read the ADRs in `docs/adr/` relevant to the proposed work.
- If a referenced domain document is absent, proceed. Create domain documentation through `domain-modeling` when a real term or decision is resolved.

## Use the domain language

Use the glossary's canonical terms in specs, tickets, hypotheses, design proposals, and test names. If a needed concept is missing, determine whether an existing term fits before proposing a new term through `domain-modeling`.

## Respect recorded decisions

Surface any conflict with an applicable ADR explicitly, with its identifier and the reason to revisit it. Preserve the recorded decision until the human agrees to change it.
