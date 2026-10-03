# Chapter Specification — ATLAS-CH-MAP-001

## Identity

**Title:** How to Read a Mathematical Atlas  
**Part:** Orientation: What Adaptive Intelligence Is  
**Status:** specification-ready.  
**Epistemic class:** Atlas documentary synthesis.

## Chapter contract

Teach the reader how to navigate the Atlas without confusing:

- table-of-contents order with dependency order;
- a stable chapter ID with a fixed chapter number;
- a hard prerequisite with a soft conceptual cross-link;
- an epistemic label with a truth score;
- a computational witness with a proof;
- a figure with the thing represented;
- a source identity with claim authority;
- CI/audit status with scientific certification.

The chapter must read as part of the monograph rather than as repository documentation.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-THESIS-001\`.

Primary downstream consumer:

- \`ATLAS-CH-EVIDENCE-001\`.

The chapter may refer to later chapter IDs and routes as navigational landmarks without assuming those chapters have been read.

## Reader outcome

A reader should be able to:

1. choose an appropriate reading route for a declared goal;
2. recursively follow hard prerequisites without treating soft links as prerequisites;
3. read a chapter at several resolutions;
4. interpret all canonical epistemic labels;
5. interpret the four figure representation classes;
6. distinguish literal from nonliteral figure semantics;
7. understand what a computational witness can and cannot establish;
8. inspect a source lock and distinguish source identity from authority;
9. understand why stable IDs survive editorial reordering;
10. understand why version control, review, and CI preserve documentary provenance without proving scientific claims.

## Principal pedagogical device

### Allegory: the atlas

The Atlas is a map of mathematical and computational territory.

Structural correspondence:

- territory ↔ the mathematical, computational, and empirical phenomena under study;
- map ↔ the organized exposition;
- legend ↔ epistemic and figure semantics;
- route ↔ a reader-selected dependency/theme/proof path;
- scale ↔ reading resolution;
- landmarks ↔ recurring concepts, keystones, and stable IDs;
- fault lines ↔ failure boundaries, contested claims, or places where a model breaks.

Limits:

- the map is not the territory;
- the legend is not a theorem;
- a route is not the unique curriculum;
- changing scale does not relax rigor;
- landmarks are not complete coverage;
- the Atlas can be revised when better evidence changes the map.

## Multi-resolution reading

Define five practical resolution levels.

### Resolution 0 — orientation

Read:

- opening problem;
- chapter contract;
- closing view.

Purpose: understand why the chapter exists.

### Resolution 1 — formal object

Read:

- definitions;
- principal equations;
- established results;
- claim boundaries.

Purpose: know what mathematical/documentary object is actually being discussed.

### Resolution 2 — derivation and failure boundary

Read:

- derivations;
- proofs/proof sketches;
- counterexamples;
- failure modes.

Purpose: know why the claim holds and where it stops.

### Resolution 3 — witness and figure

Read:

- computational witness;
- replay route;
- figure manifest;
- literal/nonliteral semantics.

Purpose: inspect reproducible support and visual interpretation.

### Resolution 4 — provenance and frontier

Read:

- source lock;
- source roles;
- audit/review record;
- downstream handoff;
- open problems / programme context.

Purpose: understand authority, maturity, and where the Atlas deliberately becomes exploratory.

The chapter must state explicitly:

> A reader may stop at a lower resolution for orientation, but must not promote a claim beyond the evidence layers actually inspected.

## Dependency semantics

The canonical hard adjacency lives in \`governance/CHAPTER_LEDGER.yaml\`.

Hard dependency:

> the target chapter may use material from the source without rebuilding it from first principles.

Soft cross-link:

> the chapters illuminate one another, but neither is entitled to assume the other has been read.

Stable IDs are persistent conceptual addresses.

Displayed order and chapter numbering may change.

## Six reading routes

### Route 1 — linear foundations

A coherent foundational route beginning at Thesis and moving through the load-bearing mathematical substrate before later systems chapters.

Example spine:

\[
\text{THESIS}
\to
\text{OBJECTS}
\to
\{\text{LINALG},\text{INFO},\text{DYN}\}
\to
\text{REP}
\to
\cdots
\]

The exact graph, not this schematic, remains canonical.

### Route 2 — dependency-first

Start from a target chapter.

Recursively follow hard prerequisites until reaching already-understood nodes.

Then read forward.

This is the safest route when the goal is mastery of one advanced topic.

### Route 3 — concept/theme

Follow one recurring idea through different parts.

Examples:

- geometry → normalized representations → manifold optimization;
- operators → attention → relative-position operators → Krylov methods;
- dynamics → numerics → depth → adaptive depth;
- memory → retrieval → polity coordination.

Theme routes can include soft links.

They must not conceal missing hard prerequisites.

### Route 4 — research-frontier

Begin with the established substrate required by a frontier question.

Then read the Atlas derivations, GCL public evidence/programme context, conjectures, and open problems.

The epistemic boundary must stay visible.

### Route 5 — proof/replay

For a load-bearing claim, trace:

\[
\text{source}
\to
\text{derivation}
\to
\text{witness}
\to
\text{figure/manuscript}
\to
\text{review}.
\]

Not every claim needs every stage.

Where a stage exists, the identities must agree.

### Route 6 — visual / Atlas-plate

Begin with a figure or Atlas plate.

Read:

1. representation class;
2. literal semantics;
3. nonliteral semantics;
4. supported claim;
5. underlying derivation/witness.

The image is an entry point, not standalone authority.

## Epistemic legend

The chapter must explain all canonical labels.

### Formal / mathematical

- **Definition** — stipulated object or terminology; not evidence of external existence.
- **Established Result** — externally supported result with preserved hypotheses.
- **Atlas Derivation** — derivation carried out in the Atlas from stated assumptions.

### Evidence / observation

- **Computational Witness** — reproducible computation supporting a bounded claim; not automatically a proof.
- **Observation** — empirical or documentary observation tied to evidence.

### Interpretation / programme

- **Interpretation** — explanatory reading of established/derived/observed material.
- **GCL Public Project Evidence** — what an exact public GCL object contains; not external theory.
- **GCL Programme Context** — project/research direction not yet tied to a public evidence object strong enough for a factual implementation claim.
- **Conjecture** — proposition believed worth testing but not established.
- **Open Problem** — unresolved question.
- **Institutional Status** — governed/documentary state such as draft/audited/accepted; not scientific truth.

The chapter must state that the labels classify support, not rank importance.

## Figure legend

Current representation classes:

- **exact** — literal mathematical/data values are generated exactly from declared objects;
- **data-derived** — visual object derived from recorded data;
- **simulation-derived** — generated from a declared simulation/model run;
- **schematic** — visual organization is pedagogical rather than metrically/data literal.

Every figure should also distinguish:

- literal semantics;
- nonliteral semantics;
- claim boundary.

A schematic figure can contain exact annotations.

An exact figure can still use arbitrary layout, line thickness, or labels.

## Computational witnesses

A computational witness is a reproducible symbolic, numerical, graphical, finite-search, simulation, or documentary computation that supports a bounded claim.

The chapter must explain the required ideas:

- identity;
- inputs;
- environment;
- conventions;
- method;
- result object;
- replay route;
- hashes/revisions where material;
- claim boundary;
- figure relationship.

A witness is evidence.

It is not automatically a theorem.

## Source locks

A source lock records:

- what the source object is;
- its stable identity/revision;
- what claim class it is authoritative for;
- what it does not support.

Governing distinction:

\[
\text{source identity}
\neq
\text{claim authority}.
\]

A perfectly pinned weak or irrelevant source remains weak or irrelevant evidence.

## Version control and audit

Explain:

- stable IDs;
- immutable Git objects;
- branch/PR review;
- audit records;
- recorded repairs;
- CI integrity checks.

Boundary:

\[
\text{documentary integrity}
\neq
\text{scientific certification}.
\]

CI can establish that the repository satisfies declared machine-checkable rules.

It cannot prove that an empirical interpretation is true.

## Chapter grammar

Expose the default recurring grammar:

1. opening problem;
2. bounded pedagogical device;
3. formal/documentary object;
4. exact derivation/reconstruction;
5. computational witness;
6. figure with semantics;
7. counterexamples/failure boundaries;
8. downstream handoff;
9. source lock/provenance;
10. epistemic status/promotion.

Readers should learn to use this grammar as navigation.

## Figure programme

### ATLAS-FIG-MAP-001 — Route, Scale, and Evidence

A restrained three-panel Atlas plate:

1. **Route** — six reader routes converging on stable chapter IDs and hard dependency edges;
2. **Scale** — vertical five-level reading ladder from orientation to provenance/frontier;
3. **Evidence** — bounded evidence path from source/derivation/witness/figure-review, with a visual warning that labels classify support rather than truth.

Representation class: schematic.

Literal semantics:

- the six named reading routes;
- the five reading-resolution levels;
- the declared documentary/evidence relations.

Nonliteral semantics:

- node placement;
- arrow length;
- spacing;
- grayscale;
- apparent hierarchy beyond the declared arrows.

## Documentary packet

The packet should reconstruct from pinned governance objects:

- canonical hard-dependency semantics;
- current chapter/edge/root counts from the dependency supplement;
- epistemic label set;
- figure representation classes;
- canonical chapter grammar;
- witness/source-lock rules;
- dependency-driven rollout principle.

No external bibliography is required.

## Failure boundaries

Include:

- reading TOC order as dependency order;
- treating a soft link as a prerequisite;
- treating a witness as proof;
- treating a figure layout as quantitative geometry;
- treating a source lock as authority promotion;
- treating audit/CI as scientific certification;
- treating a frontier/GCL programme label as established external theory;
- treating one recommended route as the unique curriculum.

## Downstream handoff

\`ATLAS-CH-EVIDENCE-001\` may assume the reader already understands:

- epistemic labels;
- source locks;
- witnesses;
- figures and semantics;
- documentary versus scientific status.

It can therefore focus on claims, evidence objects, replay, and adjudication rather than reteaching navigation.

## Acceptance

The draft must:

- explain the atlas allegory and its limits;
- define hard versus soft dependency;
- distinguish stable IDs from display order;
- include all six required routes;
- include all eleven canonical epistemic labels;
- include all four current figure classes;
- distinguish witness from proof;
- distinguish source identity from claim authority;
- distinguish CI/audit status from scientific certification;
- include exact documentary source pins;
- include the Route/Scale/Evidence Atlas plate;
- remain monograph prose rather than repository instructions;
- pass repository validation and a bounded post-draft audit.
