# ATLAS-CH-MAP-001 — Documentary Reconstruction Packet

## Purpose

This packet reconstructs the chapter's reading semantics from exact project-internal canonical objects.

It contains no external scientific claim.

## Baseline

Repository:

`grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`

Baseline commit:

`48f7615e4955b3aadab2cd61f94cf5d714d68bac`

## D1. Stable chapter identity

Source:

- `governance/ATLAS_MAP.md`
- Git blob:
  `03b9475696f3f3b75806b3ebe44dd84780f01439`

The map states that it records purpose and hard dependency rather than final numbering, and that stable IDs survive reordering.

Therefore the chapter may teach:

[
	ext{chapter identity}
=
	ext{stable ATLAS ID},
]

not final ordinal position.

## D2. Hard dependency versus soft cross-link

Source:

- `governance/DEPENDENCY_GRAPH.md`
- Git blob:
  `e4a460e2e9cb37a2a01ea34996c471668670eaa6`

Canonical semantics:

- a hard dependency authorizes the downstream chapter to use source material without rebuilding it;
- a soft cross-link expresses conceptual illumination but does not authorize prerequisite assumption.

Therefore:

[
A	o B
]

in the hard dependency graph is not equivalent to a thematic cross-reference.

The graph also states that it is a dependency structure rather than the book's narrative.

## D3. Default chapter grammar

Source:

- `governance/CHAPTER_COMPOSITION_PROTOCOL.md`
- Git blob:
  `52f1d77e80e516cea179550f966383b0b06900af`

Canonical grammar:

1. opening problem;
2. bounded pedagogical device;
3. formal/documentary object;
4. exact derivation or reconstruction;
5. computational witness when material;
6. governed figure when material;
7. counterexamples/failure boundaries;
8. downstream handoff;
9. source lock/provenance;
10. epistemic status/promotion boundary.

The protocol's compact doctrine is:

> make the object visible, make the mathematics exact, make the evidence reconstructable, and make the claim boundary explicit.

## D4. Allegory rule

Sources:

- `governance/CHAPTER_COMPOSITION_PROTOCOL.md`;
- `governance/ATLAS_EDITORIAL_PROFILE.md`.

Canonical discipline:

[
	ext{allegory}
	o
	ext{structural correspondence}
	o
	ext{mathematics}
	o
	ext{limit of allegory}.
]

An allegory cannot carry a claim not supported by the mathematics/documentary object.

This authorizes the atlas/map allegory only when its correspondence and limit are explicit.

## D5. Epistemic vocabulary

Source:

- `governance/EPISTEMIC_STATUS.yaml`
- Git blob:
  `c64f7376bf21447d73c277ba3758be7490bcdaf8`

Reader-facing classes include:

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

Two canonical nonpromotion rules are load-bearing:

[
	ext{presentation}

otRightarrow
	ext{epistemic status},
]

and

[
	ext{replay}

otRightarrow
	ext{truth, independent replication, formal verification, or certification}.
]

A reproducible or exact computational witness also does not become proof merely through reproducibility.

## D6. Figure semantics

Sources:

- `governance/ATLAS_EDITORIAL_PROFILE.md`;
- `governance/FIGURE_REGISTER.yaml`.

Canonical representation classes:

- exact;
- data-derived;
- schematic.

Governed figure manifests declare:

- literal semantics;
- nonliteral semantics;
- generator/render identity where applicable;
- claim boundary.

Therefore a reader must distinguish the visual marks that encode declared mathematical/data content from layout/presentation choices.

## D7. Source locks

Sources:

- `governance/SOURCE_REGISTER.yaml`;
- chapter-local source-lock files registered there.

A source lock binds the exact source objects consumed by a chapter and states their authority/claim boundary.

Therefore:

[
	ext{citation}

eq
	ext{unbounded authority}.
]

A chapter may only use a source for the role declared in the lock.

## D8. Audit and replay

The composition protocol and epistemic vocabulary separate:

- reconstructability;
- replay;
- verification;
- certification;
- institutional authority.

A post-draft audit can repair mathematical, documentary, or provenance defects and record disposition.

It does not transform every claim in the audited chapter into an externally certified theorem.

## D9. Multi-resolution reading

The Atlas Map provides the macro-architecture.

The Dependency Graph provides hard prerequisite structure.

Individual chapters provide local mathematical resolution.

Source locks and audit records provide evidentiary resolution.

Therefore a reader can legitimately move among scales:

[
	ext{Atlas}
	o
	ext{Part}
	o
	ext{Chapter}
	o
	ext{claim}
	o
	ext{support object}.
]

Changing scale changes detail.

It must not silently change epistemic status.

## D10. Reader-route derivation

The six reading routes in the chapter are not new governance authorities.

They are documentary syntheses of the canonical structures:

- editorial order from the Atlas Map;
- hard dependencies from the Dependency Graph;
- soft conceptual bridges from the Dependency Graph;
- frontier/open-problem labels from the epistemic protocol;
- proof/witness/source/audit path from the composition and provenance machinery;
- figure-first route from the Figure Register and editorial figure doctrine.

They are therefore navigation strategies, not unique curricula.

## Claim boundary

This packet establishes that the chapter's navigation rules accurately reconstruct the repository's declared Atlas semantics at the pinned baseline.

It does not establish that the Atlas architecture is complete, optimal, immutable, or externally authoritative.
