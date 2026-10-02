# Atlas Source-Lock Standard

**Standard ID:** `GCL-ATLAS-SOURCE-001`  
**Status:** canonical project-local standard

## Purpose

A source lock binds a load-bearing claim to an identifiable source object and records what that object is authoritative for.

The governing rule is:

> source identity and claim authority are separate fields.

A precise citation to the wrong kind of source is still weak evidence.

## Required fields

A chapter source lock should record, where applicable:

- chapter ID;
- source ID;
- title or object name;
- source kind;
- author/institution;
- DOI, arXiv ID, standard URL, repository identity, commit, blob, or content digest;
- authority/scope statement;
- claim boundary;
- date/version where material.

## Source classes

### External scholarly source

Prefer primary literature for specific technical claims and reliable monographs/surveys for established background.

Preserve hypotheses and historical scope.

### Standard or institutional source

Use exact revision/date when the policy, standard, or terminology can change.

### Public GCL project evidence

Bind:

- repository;
- commit;
- path;
- blob/content identity where practical.

Assert only what the public object actually contains.

### GCL programme context

If a remembered GCL term, design, result, or project extension cannot be tied to an exact public object, label it as programme context or research direction.

Do not infer implementation from project memory.

### User-supplied source

Preserve file identity/provenance. A user-supplied inventory can govern design without becoming independent evidence for external factual claims.

## No citation laundering

The following transitions are prohibited without additional evidence:

- memory → public implementation claim;
- project slogan → mathematical theorem;
- secondary summary → primary historical claim when the primary source is available;
- computational observation → universal mathematical statement;
- repository branch name → immutable source identity;
- replay success → certification.

## Mutable sources

If a source is mutable, either:

- bind an immutable revision;
- preserve a source snapshot;
- record that the source is intentionally live and limit claims accordingly.

## Negative source findings

Absence can be material.

When a search for a named public object fails, record:

- search scope;
- inspected revision;
- search terms;
- consequence.

Do not convert “not found” into “does not exist anywhere.”

## Supersession

A newer upstream source does not silently alter an existing Atlas source lock.

Adopting a changed upstream doctrine or project state requires an explicit source-lock update and, when it changes governing doctrine, an ADR.
