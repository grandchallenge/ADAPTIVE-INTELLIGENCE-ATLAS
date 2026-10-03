# Chapter Specification — ATLAS-CH-MAP-001

## Identity

**Title:** How to Read a Mathematical Atlas  
**Part:** Orientation  
**Status:** specification-ready.  
**Epistemic class:** Atlas documentary synthesis.

## Chapter contract

Make the Atlas executable for readers rather than merely navigable.

The chapter explains how to choose routes, read dependency claims, interpret epistemic labels, use proofs/witnesses/figures correctly, and recover documentary provenance.

It must read as part of the monograph rather than repository documentation.

## Dependency contract

Hard prerequisite:

- `ATLAS-CH-THESIS-001`.

Project-internal documentary sources are bound in:

- `sources/source-locks/ATLAS-CH-MAP-001.yaml`.

## Reader outcome

A reader should be able to:

1. explain why stable chapter IDs matter more than fixed numbering;
2. distinguish hard dependency from soft cross-link;
3. choose a reading route appropriate to a goal;
4. interpret the Atlas epistemic labels;
5. distinguish proof, derivation, computational witness, observation, interpretation, conjecture, and programme;
6. read exact, data-derived, and schematic figures correctly;
7. locate the source lock behind a chapter;
8. understand what replay/audit does and does not establish;
9. use allegory as a structural aid without treating it as evidence;
10. move between overview scale and local technical detail without losing claim boundaries.

## Principal pedagogical device

### Allegory: an atlas is not the territory

Use the geographic atlas structurally.

Correspondence:

- territory ↔ the mathematical/scientific subject;
- map ↔ one organized representation of that subject;
- legend ↔ notation and epistemic labels;
- scale ↔ level of mathematical resolution;
- route ↔ reader-selected dependency-respecting path;
- landmark ↔ keystone or conceptually central chapter;
- coordinate grid ↔ stable IDs and cross-references;
- survey record ↔ source locks, witnesses, and audits.

Limits:

- the subject is not exhausted by the Atlas;
- a route is not a unique curriculum;
- a landmark is not a proof of surrounding terrain;
- a legend describes notation/status but does not confer truth;
- changing scale may omit detail but must not silently change claim status.

## Formal/documentary objects

### Stable identity

Chapter identity is the stable `ATLAS-CH-*` ID.

Final numbering and physical order may change.

### Hard dependency

If (A	o B) is a hard dependency, chapter (B) may use the declared content of (A) without rebuilding it from first principles.

### Soft cross-link

A soft cross-link indicates conceptual illumination, not prerequisite authority.

### Epistemic status

Reader-facing claims use the canonical vocabulary in `EPISTEMIC_STATUS.yaml`.

At minimum explain:

- Definition;
- Established Result;
- Atlas Derivation;
- Computational Witness;
- Observation;
- Interpretation;
- GCL Public Project Evidence;
- GCL Programme;
- Conjecture;
- Open Problem;
- Institutional Status.

### Figure classes

Explain:

- exact;
- data-derived;
- schematic.

Every governed figure's literal and nonliteral semantics determine how it may be read.

## Required reader routes

### Route A — linear foundations

Read the Atlas in editorial order.

Use when continuity and broad coverage matter most.

### Route B — dependency-first

Choose a target chapter, follow hard dependencies backward, then read forward.

Use when technical correctness with minimal detour matters most.

### Route C — concept/theme

Follow soft cross-links around a concept such as geometry, memory, operators, or governance.

Use when synthesis matters more than strict sequence.

### Route D — research-frontier

Begin at a frontier/open-problem chapter, then descend through source locks, prerequisite mathematics, and failure boundaries.

Use when evaluating a live research programme.

### Route E — proof/replay

Follow theorem/derivation -> computational witness -> source lock -> audit/replay record.

Use when reconstructability and evidentiary strength matter most.

### Route F — visual/Atlas-plate

Begin from figures and conceptual plates, then descend into literal semantics and mathematics.

Use when geometric or operator intuition is the entry point.

## Evidence reading rule

A mature Atlas claim should let the reader answer:

- What is the object?
- What supports it?
- What does that support route establish?
- What does it not establish?
- What source/version was consumed?
- What downstream chapter is allowed to assume?

## Figure decision

No separate governed figure is required for v0.1.

The chapter's primary visual object is its route table and documentary legend. A decorative map-style plate would add presentation cost without stronger semantics at this stage.

A future Atlas plate may be added if it can encode actual dependency/provenance structure rather than decoration.

## Failure boundaries

Include:

- treating chapter order as dependency order;
- treating a soft link as prerequisite authority;
- treating exact computation as proof;
- treating replay as truth/certification;
- treating schematic geometry as measured data;
- treating internal project status as external scientific authority;
- treating allegory as mechanism;
- assuming the current Atlas is complete.

## Documentary packet

Create:

`mathematics/derivations/ATLAS-CH-MAP-001-DOCUMENTARY.md`

It must map each reader-facing rule to the exact canonical governance object and Git blob that authorizes it.

## Sources

All sources are project-internal and bound by:

`sources/source-locks/ATLAS-CH-MAP-001.yaml`.

## Acceptance

The draft must:

- preserve multi-resolution reading;
- preserve stable identity semantics;
- state hard versus soft dependency exactly;
- enumerate the canonical epistemic vocabulary without changing promotion rules;
- explain figure representation classes and literal/nonliteral semantics;
- explain source lock, replay, and audit boundaries;
- provide all six required routes;
- use the atlas allegory with explicit correspondence and limit;
- remain monograph prose, not repository-operating instructions.
