# AUDIT-032 — Local-to-Global Mathematics

## Disposition

**PASS AFTER TWO FORMAL NOTATION REPAIRS**

ATLAS-CH-LOCALGLOBAL-001 remains at `draft-v0.1`.

The chapter correctly introduces the minimum local-to-global structure needed later: incidence/cover structure, local sections, restriction maps, matching families, gluing existence, gluing uniqueness, and explicit finite incompatibility.

AUDIT-032 found two in-scope notation defects:

1. the general vector-space disagreement map was indexed over all ordered pairs `(i,j)`, redundantly duplicating off-diagonal overlap equations and including trivial diagonal components. The repaired derivation/manuscript use one component for each `i<j`;
2. the exact witness used the placeholder word `xor` for the local product/direct-sum space. It now states `F(U) direct-sum F(V)=R^4`.

Neither repair changes the exact witness, source scope, dependency structure, or chapter thesis.

## Audited baseline

- implementation merge:
  `ca04c7f4dc854c0d5176f2d66c422475ebc0907e`;
- implementation PR:
  #125;
- audit issue:
  #126;
- chapter:
  `ATLAS-CH-LOCALGLOBAL-001`.

## 1. Hard prerequisite

PASS.

The source lock binds exactly:

- OBJECTS manuscript blob:
  `6e8bd13b7d7ec7337e14135f8e9cf0a7fc415054`;
- AUDIT-004 blob:
  `948f76b3f86d27fa4830efc30d8ef0135134256e`;
- OBJECTS source-lock blob:
  `805b06978f08c7efa7add3f36fca0301dca7047b`.

The chapter inherits only the audited role/interface vocabulary.

No downstream composition, boundary-contract, data-fusion, or sheaf-specific chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock identifies:

- Justin Michael Curry, *Sheaves, Cosheaves and Applications*;
- Michael Robinson, *Sheaves are the canonical data structure for sensor integration*;
- Jakob Hansen and Robert Ghrist, *Toward a spectral theory of cellular sheaves*.

Their use is bounded to ordinary/cellular sheaf foundations, local sections/restrictions/gluing language, graph/cell-complex local-to-global structure, and a representative applied consistency/fusion setting.

The chapter does not import derived categories, full cohomology theory, sheaf Laplacians, or a universal claim that every distributed system is naturally a sheaf.

## 3. Presheaf restriction laws

PASS.

For `V subseteq U`, the chapter defines:

`rho^U_V:F(U)->F(V)`.

It requires:

`rho^U_U=id`

and:

`rho^V_W o rho^U_V=rho^U_W`.

These are correctly presented as coherent restriction structure, not yet as a gluing theorem.

## 4. Matching family

PASS.

For a cover `{U_i}`, the local family `s_i in F(U_i)` is matching exactly when both restrictions agree on every overlap.

The comparison is correctly typed in:

`F(U_i intersect U_j)`.

The manuscript explicitly rejects whole-state comparison when only boundary data are supposed to agree.

## 5. Sheaf condition

PASS.

The chapter separates:

- existence of a global glue for a matching family;
- uniqueness of that global glue.

It correctly states that a sheaf supplies both.

## 6. Pairwise-overlap boundary

PASS.

The chapter avoids the false slogan that pairwise compatibility can never imply global consistency.

It correctly states that for a sheaf over a cover, matching on all pairwise overlaps is the matching-family condition and the sheaf axiom supplies the unique glue.

The warning is correctly scoped to arbitrary local constraint systems whose restriction/gluing structure has not been established.

## 7. Discrepancy-map notation

PASS AFTER REPAIR.

For vector-space-valued local data, the repaired map is:

`Delta:prod_i F(U_i)->prod_{i<j}F(U_i intersect U_j)`.

Each component records one oriented overlap difference.

This removes redundant `(j,i)` and diagonal components while preserving the matching kernel.

## 8. Exact finite function sheaf

PASS.

The witness uses:

`X={a,b,c}`;

`U={a,b}`;

`V={b,c}`;

`W={b}`;

and:

`F(S)=R^S`.

Restrictions are coordinate projections.

This is a valid finite/discrete function sheaf.

## 9. Global-to-local map

PASS.

The exact map is:

`R(x,y,z)=(x,y,y,z)`.

It is injective.

Thus at most one global section can realize a given local pair in this witness.

This correctly witnesses gluing uniqueness.

## 10. Overlap discrepancy

PASS.

The discrepancy is:

`Delta(u_a,u_b,v_b,v_c)=u_b-v_b`.

Therefore:

`Delta=0`

iff the two local sections agree on the common coordinate b.

## 11. Image-kernel identity

PASS.

The image is:

`im(R)={(x,y,y,z)}`.

The kernel is:

`ker(Delta)={(u_a,u_b,v_b,v_c):u_b=v_b}`.

Renaming coordinates gives:

`im(R)=ker(Delta)`.

This is the exact gluing-existence statement for the witness.

## 12. Compatible family

PASS.

For:

`s_U=(1,2)`;

`s_V=(2,4)`;

the overlap discrepancy is zero.

The unique global glue is:

`s=(1,2,4)`.

## 13. Incompatible family

PASS.

For:

`q_U=(1,2)`;

`q_V=(3,4)`;

the exact discrepancy is:

`2-3=-1`.

Because the pair is not in `ker(Delta)=im(R)`, no global function restricts to both local sections.

The obstruction is correctly localized to the shared coordinate b.

## 14. Direct-sum notation

PASS AFTER REPAIR.

The witness now identifies the local vector space as:

`F(U) direct-sum F(V)=R^4`.

The earlier `xor` placeholder is removed.

## 15. Graph versus carried data

PASS.

The chapter keeps distinct:

- graph/cover incidence;
- section spaces;
- overlap spaces;
- restriction maps;
- local section values.

It does not treat a graph alone as a sheaf.

## 16. Cellular-sheaf scope

PASS.

The manuscript says only that cellular sheaves assign data spaces to cells and maps along incidences under a declared convention.

It deliberately avoids committing this elementary chapter to a convention-dependent arrow notation or to cohomological/spectral machinery.

## 17. Exact versus approximate consistency

PASS.

The chapter states that nonzero exact discrepancy means exact gluing fails.

A noisy/fusion treatment requires a separately declared:

- metric;
- tolerance;
- loss;
- optimization rule.

Approximate repair is not relabeled as exact sheaf gluing.

## 18. Consistency versus truth

PASS.

A global section certifies consistency relative to the declared restriction model.

It does not establish:

- factual truth;
- semantic adequacy;
- numerical stability;
- completeness of the modeled constraints.

This boundary is explicit.

## 19. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records LOCALGLOBAL-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-LOCALGLOBAL-LOCK-001`.

The computational witness is bound at:

`mathematics/computational-witnesses/ATLAS-CW-LOCALGLOBAL-001.md`.

The witness contains an explicit Claim boundary.

The manuscript has the required epistemic marker, reference section, and source-lock path.

No governed figure is required.

## 20. Downstream handoff

PASS.

Later chapters may inherit:

- graph/cover incidence;
- local section;
- restriction map;
- matching family;
- gluing existence;
- gluing uniqueness;
- overlap discrepancy/obstruction;
- exact versus approximate compatibility.

They must independently define their domain-specific section spaces, restrictions, semantics, stability conditions, and governance obligations.

## 21. Final disposition

AUDIT-032 passes after the two notation repairs above.

The durable local-to-global layer is:

**explicit local regions + typed section spaces + restriction maps -> exact overlap compatibility -> unique gluing when the sheaf condition holds, with nonzero discrepancies serving as localized finite obstructions rather than vague global failure.**
