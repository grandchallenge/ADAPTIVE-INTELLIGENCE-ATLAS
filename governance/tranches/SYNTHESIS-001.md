# SYNTHESIS-001 — Six-Keystone Composition Grammar

## Status

Tranche state: implemented on branch pending merge validation.

## Baseline

AUDIT-003 merge: 6f71826e5d0c56fb2a1e27aec3b42d6bea9d17c8

At baseline:

- 80 chapter nodes;
- 126 hard dependency edges;
- six audited keystones at draft-v0.1;
- six rendered keystone witnesses;
- 74 chapters remain undrafted;
- synthesis issue: #15.

## Purpose

The architecture bootstrap established doctrine before substantial manuscript material existed.

The six audited keystones now provide enough actual manuscript evidence to distinguish durable authoring rules from bootstrap assumptions.

SYNTHESIS-001 freezes only the practices that survived work across mathematical, computational, compositional, and documentary chapters.

## Canonical outputs

### Chapter composition

governance/CHAPTER_COMPOSITION_PROTOCOL.md

The protocol freezes these chapter functions:

1. opening problem;
2. bounded pedagogical device where useful;
3. formal or documentary object;
4. exact derivation or reconstruction;
5. computational witness where material;
6. figure semantic contract;
7. counterexample or failure boundary;
8. downstream handoff;
9. source/provenance route;
10. epistemic status and promotion boundary.

This is a functional grammar, not a mandatory heading template.

### Epistemic vocabulary

governance/EPISTEMIC_STATUS.yaml

Canonical labels distinguish:

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

Presentation does not create epistemic status.

### Computational witnesses

governance/COMPUTATIONAL_WITNESS_STANDARD.md

This freezes identity, inputs, environment, mathematical conventions, method, expected/result object, replay route, hashes or immutable revisions where meaningful, claim boundary, and figure linkage.

### Source locking

governance/SOURCE_LOCK_STANDARD.md

This freezes:

- source identity versus claim authority;
- immutable revision/content identity where appropriate;
- external source versus public GCL evidence versus programme context;
- mutable-source handling;
- negative source findings;
- prohibition on citation laundering.

### Editorial profile

governance/ATLAS_EDITORIAL_PROFILE.md now records:

architecture first -> dependency graph -> keystone chapters -> six-keystone synthesis -> chapter families -> global synthesis.

### Mathematical lexicon

governance/MATHEMATICAL_LEXICON.yaml advances to schema v0.2.0 and adds durable meanings for:

- source lock;
- replay;
- certification;
- epistemic status;
- representation class.

It also reconciles operator-norm, transpose/adjoint, Jacobian, JVP, and VJP conventions.

### Chapter-family rollout

governance/CHAPTER_FAMILY_ROLLOUT.md

An initial staged rollout began from Geometry's downstream cone. A final dependency audit showed that several undrafted prerequisites have greater architectural reach:

- ATLAS-CH-THESIS-001: 79 descendants;
- ATLAS-CH-OBJECTS-001: 68;
- ATLAS-CH-LINALG-001: 63;
- ATLAS-CH-DYN-001: 48;
- ATLAS-CH-INFO-001: 28;
- ATLAS-CH-ARCHHIST-001: 28.

The rollout was corrected to begin with Family 0: Orientation and load-bearing mathematical spine.

This is the practical consequence of treating the dependency graph as executable editorial architecture rather than decoration.

### Decision record

governance/decisions/ADR-0005-six-keystone-composition-grammar.md makes later changes to canonical composition grammar, epistemic labels, source-lock doctrine, or witness doctrine ADR-controlled.

## Frozen distinctions

The synthesis preserves these distinctions as load-bearing:

- ambient coordinates are not the same thing as admissible state;
- score or representation is not the same thing as operator action;
- asymptotic stability is not the same thing as finite-horizon amplification;
- a toy mechanism does not establish frontier prevalence;
- a local contract does not establish global safety;
- replay does not imply truth, formal verification, independent replication, certification, or authority;
- public project evidence is distinct from programme context;
- literal figure semantics are distinct from schematic or metaphorical presentation.

## CI extension

The Atlas validator now additionally checks the machine-verifiable subset:

- canonical synthesis governance artifacts exist;
- canonical epistemic label IDs are unique and complete;
- the Mathematical Lexicon contains the synthesis-era provenance terms;
- every drafted keystone manuscript contains a reader-facing epistemic-status marker;
- every drafted keystone computational witness contains a claim boundary;
- canonical governance Markdown is free of hidden C0 control characters.

Existing DAG, citation, replay, manuscript/math control-character, artifact, and figure checks remain active.

The validator deliberately does not require identical headings, equal numbers of figures, or identical source-lock schemas.

## Promotion state

No chapter is promoted by this synthesis.

All six keystones remain draft-v0.1.

SYNTHESIS-001 promotes editorial protocol, not mathematical or institutional status.

## Next executable phase

Begin Family 0 with the smallest high-leverage foundation tranche:

1. ATLAS-CH-THESIS-001;
2. ATLAS-CH-OBJECTS-001;
3. ATLAS-CH-LINALG-001;
4. ATLAS-CH-DYN-001.

The first two establish the Atlas thesis and object vocabulary. Linear algebra and dynamics then discharge the highest-leverage mathematical prerequisites.

Before full drafting, source-lock and specify these four together so notation and thesis language are reconciled once rather than independently.
