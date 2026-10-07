# Atlas Editorial Profile

**Profile ID:** `GCL-ATLAS-AI-EDITORIAL-001`  
**Status:** canonical project-local profile, global synthesis phase
**Title:** *A Mathematical Atlas of Adaptive Intelligence*

## Purpose

This profile specializes existing Grand Challenge Labs doctrine for a long-form illustrated mathematical monograph. It does not create a new cross-programme standard and does not enlarge the authority of any upstream document.

## Pinned inheritance

The initial profile binds the following source state exactly:

- `grandchallenge/MATH-PROGRAMME@4a7150d2b3a3c6e7ddac38f4006c69dd9dd7bbf0`
  - `docs/TECHNICAL_WRITING_REFERENCE.md`
  - `docs/GRAND_CHALLENGE_PEDAGOGY_STANDARD.md`
  - `docs/PEDAGOGICAL_STYLE_GUIDE.md`
  - `docs/VISUAL_PEDAGOGY_STANDARD.md`
  - `docs/monographs/type-theory-series/SERIES_STYLE_CONTRACT.md`
- `grandchallenge/gcl-standards@6704b4037161133a1efeedddcb69060a79cb7bc7`
- `grandchallenge/INTELLECT@cacfe1f749b91a335e1d1734352cecff56bad7c1`
- `grandchallenge/AETHER@74b2e322a4453f1665a076bc0682adcd0c5cfb44`

`VISUAL_PEDAGOGY_STANDARD.md` is adopted here as a local Atlas reference/profile. Its upstream document remains scoped by its own bounded-pilot language. The Type Theory series contract is a monograph design reference, not governing authority for this Atlas.

Future upstream revisions do not silently alter this profile. Adoption changes require an Atlas decision record.

## Composition doctrine

The Atlas uses:

`architecture first -> dependency graph -> keystone chapters -> six-keystone synthesis -> chapter families -> global synthesis`

The macro-architecture is stable enough to coordinate work but revisable through explicit ADRs.

### Current phase snapshot

The protected Chapter Ledger records all 80 chapter nodes at `draft-v0.1` and zero at `architecture`. The dependency-driven drafting frontier is therefore exhausted and the current project-local phase is full-manuscript global synthesis.

`governance/CHAPTER_LEDGER.yaml` is authoritative for chapter lifecycle state. A specification document may retain an internal label such as `Status: specification-ready` to describe the maturity of that specification artifact; that wording does not override the ledger's chapter lifecycle state.

Stable chapter IDs and ledger `part_id` values carry semantic identity. Filesystem locations are presentation coordinates. Legacy directory prefixes may therefore remain in place when moving them would create provenance churn without improving mathematical or editorial meaning.

The canonical chapter-level composition grammar is now:

- `governance/CHAPTER_COMPOSITION_PROTOCOL.md`;
- `governance/EPISTEMIC_STATUS.yaml`;
- `governance/COMPUTATIONAL_WITNESS_STANDARD.md`;
- `governance/SOURCE_LOCK_STANDARD.md`.

Chapter-family rollout is dependency-driven through:

- `governance/CHAPTER_FAMILY_ROLLOUT.md`.

These documents were derived from the six audited keystone drafts. They specialize this profile; they do not enlarge upstream GCL authority.

## Governing conceptual spine

`geometry -> operators -> dynamics -> optimization -> composition -> memory -> coordination -> diagnostics -> governed adaptation`

The manuscript is a coherent argument, not an encyclopedia of machine-learning topics.

## Epistemic vocabulary

The canonical machine-readable vocabulary is `governance/EPISTEMIC_STATUS.yaml`.

Reader-facing technical claims must preserve the distinction among established external theory, Atlas derivation, computational witness, observation, interpretation, public GCL project evidence, GCL programme context, conjecture, open problem, and institutional status.

Presentation may reveal status. It does not create status.

## Pedagogical doctrine

Imagination and rigor are complementary.

Preferred allegory discipline:

`allegory -> structural correspondence -> mathematics -> limits of allegory`

A metaphor must disclose its mapping and its failure boundary before it becomes load-bearing.

Use toy cases, counterexamples, multiple representations, and computational witnesses to reveal structure. Formal notation should arrive after the problem it solves is visible, except when the formal object itself is the subject.

## Figure doctrine

Atlas figures inherit the representation classes used by the GCL visual-pedagogy reference:

- exact
- data-derived
- simulation-derived
- schematic
- metaphorical
- historical

Every governed figure manifest must state `literal_semantics` and `nonliteral_semantics`.

Wolfram is preferred when symbolic derivation, exact matrix computation, high-precision numerics, vector fields, phase portraits, stability regions, eigensystems, manifolds, implicit surfaces, or parameter sweeps materially strengthen the exposition.

A reproducible rendering is not a proof. The claim/support route remains separate.

## Evidence routing

- Ordinary exposition: scholarly source and provenance controls.
- Atlas computational witness: reproducible generator, parameters, environment, and claim boundary.
- Material new mathematical claim: may enter MATHFORGE -> MATHSOLVE -> MATHCERT when appropriate.
- Certified mathematical result: cite the exact certification identity and retained qualifications.

## Stable identity

Chapter number and filesystem location are presentation coordinates, not identity.

Stable IDs follow the `ATLAS-*` namespace. Relocation must not sever provenance.

## Completion test for a mature chapter

A mature chapter should make clear:

1. the object;
2. the obstruction or motivating tension;
3. the formal structure;
4. the strongest supported result;
5. the computational or empirical support route where applicable;
6. the figure semantics;
7. the limits of its allegories;
8. the relationship to the Atlas dependency graph;
9. the unresolved boundary;
10. the next useful research question where appropriate.

**Editorial maxim:** Make the mathematics visible without making it smaller.
