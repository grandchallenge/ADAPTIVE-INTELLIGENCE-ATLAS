# Chapter Specification — ATLAS-CH-LOCALGLOBAL-001

## Identity

- Stable ID: `ATLAS-CH-LOCALGLOBAL-001`
- Title: **Local-to-Global Mathematics**
- Part: `ATLAS-PART-MATH`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-OBJECTS-001`
- Implementation issue: #125
- Baseline: `ed3f07a2531c520e0fad43f072340f8099448098`

## Contract

Introduce graphs, sheaves, compatibility, gluing, and compositional viewpoints only to the degree needed later.

## Governing question

Suppose a system is described locally.

When do the local pieces determine one coherent global object?

The answer requires more than collecting local values. It requires:

- an incidence or cover structure;
- data spaces over regions/cells;
- maps that compare data on overlaps/interfaces;
- a compatibility condition;
- a gluing rule.

## Graph versus sheaf

A graph supplies incidence:

`G=(V,E)`.

A sheaf-like structure adds data over cells/regions and restriction maps along incidences.

Therefore:

> topology/combinatorics says which pieces touch; restriction maps say how their data must compare.

## Presheaf-level object

For each region `U`, let `F(U)` be a set/vector space of allowable local sections.

For inclusion `V subseteq U`, provide a restriction map:

`rho^U_V:F(U)->F(V)`.

Require:

`rho^U_U=id`

and for `W subseteq V subseteq U`:

`rho^V_W o rho^U_V=rho^U_W`.

This is restriction consistency.

## Matching family

Let `{U_i}` cover `U`.

A family:

`s_i in F(U_i)`

is matching/compatible when for every pair:

`rho^{U_i}_{U_i intersect U_j}(s_i)
=
rho^{U_j}_{U_i intersect U_j}(s_j)`.

Compatibility is an equality after restriction to the overlap.

## Sheaf gluing condition

A sheaf requires that every matching family over a cover has a unique global section:

`s in F(U)`

such that:

`rho^U_{U_i}(s)=s_i`

for all `i`.

Two logically separate requirements are present:

1. existence of a glue;
2. uniqueness of that glue.

## Exact function-sheaf witness

Let:

`X={a,b,c}`.

Cover:

`U={a,b}`;

`V={b,c}`;

`W=U intersect V={b}`.

For each subset `S subseteq X`, define:

`F(S)=R^S`

as real-valued functions on `S`.

Restriction maps forget coordinates outside the smaller set.

## Compatible family

Choose:

`s_U(a)=1, s_U(b)=2`;

`s_V(b)=2, s_V(c)=4`.

Restrictions to `W` both equal 2.

Therefore the family is compatible.

The unique global glue is:

`s(a)=1, s(b)=2, s(c)=4`.

## Uniqueness

If another global `t in F(X)` restricts to both `s_U` and `s_V`, then:

- `t(a)=1` from U;
- `t(b)=2` from U or V;
- `t(c)=4` from V.

So `t=s`.

Uniqueness is exact.

## Incompatible family

Keep:

`t_U(a)=1,t_U(b)=2`

but set:

`t_V(b)=3,t_V(c)=4`.

Overlap discrepancy:

`d=t_U(b)-t_V(b)=2-3=-1`.

Since `d != 0`, no global function on X can restrict to both local sections.

The discrepancy is an explicit gluing obstruction in this witness.

## Approximate compatibility

If overlap values differ by a small amount, exact gluing still fails.

One may instead solve an optimization problem such as minimizing squared disagreement.

That is approximate fusion, not exact sheaf gluing.

The metric/objective must be stated separately.

## Interfaces

OBJECTS-001 introduced interfaces/contracts as obligations across boundaries.

Here the restriction/equality condition is the simplest mathematical form of such an obligation:

local objects must induce the same boundary data on their shared overlap.

Later chapters may enrich this with semantic or numerical contracts.

## Compositional viewpoint

Local-to-global construction is compositional when:

- local pieces can be inspected independently;
- overlap maps expose what must agree;
- compatible pieces can be assembled;
- incompatibility is localized to explicit interfaces.

This is stronger than naive aggregation.

## Boundary on pairwise compatibility

For an actual sheaf over a cover, equality on all pairwise overlaps is the matching-family condition and the sheaf axiom supplies a unique glue.

For arbitrary local constraint systems, merely saying "the pieces look pairwise plausible" is not enough; the restriction structure and exact matching equations must be specified.

## Downstream handoff

Later composition/data-fusion/boundary-contract chapters may inherit:

- graph/cover incidence versus carried data;
- local sections;
- restriction maps;
- matching families;
- exact gluing;
- uniqueness;
- explicit overlap obstruction;
- exact versus approximate consistency.

They may not infer that every engineering system is naturally a sheaf or that sheaf compatibility alone certifies semantics, stability, or correctness.
