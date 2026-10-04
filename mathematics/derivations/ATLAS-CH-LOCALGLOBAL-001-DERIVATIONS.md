# ATLAS-CH-LOCALGLOBAL-001 — Formal and Derivation Packet

## 1. Local-to-global problem

Let `X` be a space or finite domain and let:

`U = union_i U_i`

be a cover.

A local-to-global problem asks whether local data:

`s_i in F(U_i)`

arise as restrictions of one global object:

`s in F(U)`.

The answer depends on the restriction structure carried by `F`.

## 2. Presheaf restriction structure

For every region `U), assign a set/vector space:

`F(U)`.

For each inclusion:

`V subseteq U`,

assign:

`rho^U_V:F(U)->F(V)`.

Require identity:

`rho^U_U=id`.

Require composition:

`rho^V_W o rho^U_V=rho^U_W`

for:

`W subseteq V subseteq U`.

These laws say restrictions are coherent.

They do not yet imply that compatible local data can be reconstructed globally.

## 3. Matching family

For cover `{U_i}`, local sections `s_i in F(U_i)` are matching when:

`rho^{U_i}_{U_i intersect U_j}(s_i)
=
rho^{U_j}_{U_i intersect U_j}(s_j)`

for every pair `i,j`.

This equality is evaluated in:

`F(U_i intersect U_j)`.

The overlap object is load-bearing.

## 4. Sheaf condition

A sheaf requires:

### Existence

For every matching family `{s_i}`, there exists:

`s in F(U)`

with:

`rho^U_{U_i}(s)=s_i`

for every `i`.

### Uniqueness

If `s,t in F(U)` restrict identically on every member of the cover, then:

`s=t`.

Existence and uniqueness are distinct logical clauses.

## 5. Equalizer form

For a finite cover, define the restriction map:

`R:F(U)->prod_i F(U_i)`.

Define the disagreement map into pairwise overlaps:

`Delta:prod_i F(U_i)->prod_{i,j} F(U_i intersect U_j)`.

For vector-space valued sections, one component is:

`Delta_ij({s_k})
=
rho^{U_i}_{U_i intersect U_j}(s_i)
-
rho^{U_j}_{U_i intersect U_j}(s_j)`.

Matching families satisfy:

`Delta({s_i})=0`.

The sheaf condition identifies global sections with matching families:

`im(R)=ker(Delta)`

and uniqueness requires `R` to be injective.

For general sets one uses equality/equalizer language rather than subtraction.

## 6. Exact finite function sheaf

Let:

`X={a,b,c}`.

Because the topology is discrete, every subset is an allowed region.

Define:

`F(S)=R^S`

for each `S subseteq X`.

Thus a section over `S` is a real-valued function on `S`.

Restriction:

`rho^S_T:R^S->R^T`

for `T subseteq S` simply discards coordinates outside `T`.

## 7. Two-set cover

Take:

`U={a,b}`;

`V={b,c}`;

`W=U intersect V={b}`.

Then:

`F(X)=R^3`;

`F(U)=R^2`;

`F(V)=R^2`;

`F(W)=R`.

Write a global section as:

`(x,y,z)`.

Write a local pair as:

`((u_a,u_b),(v_b,v_c))`.

## 8. Restriction map

The global-to-local map is:

`R:R^3->R^4`

with:

`R(x,y,z)=(x,y,y,z)`.

This map is injective.

Proof:

If:

`R(x,y,z)=R(x',y',z')`,

then coordinate equality gives:

`x=x'`;

`y=y'`;

`z=z'`.

Therefore the global section is uniquely determined by its two local restrictions.

This is the uniqueness side.

## 9. Discrepancy map

Define:

`Delta:R^4->R`

by:

`Delta(u_a,u_b,v_b,v_c)=u_b-v_b`.

Then:

`Delta=0`

iff the two local sections agree on the overlap `{b}`.

Thus:

`ker(Delta)`

is exactly the vector space of matching local pairs.

## 10. Image equals kernel

The image of `R` is:

`im(R)
=
{(x,y,y,z):x,y,z in R}`.

The kernel of `Delta` is:

`ker(Delta)
=
{(u_a,u_b,v_b,v_c):u_b=v_b}`.

Rename:

`x=u_a`;

`y=u_b=v_b`;

`z=v_c`.

Then:

`ker(Delta)
=
{(x,y,y,z):x,y,z in R}
=
im(R)`.

Therefore:

`im(R)=ker(Delta)`.

This is the exact existence statement for the finite function witness.

## 11. Compatible numerical family

Choose:

`s_U=(1,2)`;

`s_V=(2,4)`.

Then:

`Delta(s_U,s_V)=2-2=0`.

Therefore the pair is matching.

Because it lies in `im(R)`, the global section is:

`s=(1,2,4)`.

## 12. Unique glue

Suppose:

`t=(t_a,t_b,t_c)`

also restricts to:

`(1,2)`

on U and:

`(2,4)`

on V.

Then:

`t_a=1`;

`t_b=2`;

`t_c=4`.

Therefore:

`t=s`.

The glue is unique.

## 13. Incompatible numerical family

Choose:

`q_U=(1,2)`;

`q_V=(3,4)`.

Then:

`Delta(q_U,q_V)=2-3=-1`.

Therefore:

`(q_U,q_V) notin ker(Delta)`.

Since:

`im(R)=ker(Delta)`,

there is no global section whose restrictions equal both q_U and q_V.

The nonzero scalar `-1` is the exact overlap obstruction in this witness.

## 14. The obstruction is localized

The values at a and c are not in conflict.

The failure is entirely at shared coordinate b.

This illustrates the local-to-global advantage of explicit interface maps:

the failure can be localized to the overlap where compatibility is required.

## 15. Graph/nerve viewpoint

Associate one vertex to U and one vertex to V.

Connect them because:

`U intersect V != empty`.

The resulting graph records that the local regions interact.

But the graph alone does not know:

- which data live on U or V;
- which data live on the overlap;
- how local data restrict to the overlap;
- what equality must hold.

The graph is incidence structure.

The sheaf-like data include spaces and maps over that structure.

## 16. Cellular viewpoint

On a graph/cell complex, a cellular sheaf assigns data spaces to cells and linear maps along incidences according to a declared convention.

This makes local-to-global constraints computable using finite-dimensional linear algebra.

The present chapter does not require cellular cohomology, sheaf Laplacians, or spectral theory.

## 17. Pairwise matching and the sheaf axiom

For an open cover of a sheaf, equality on all pairwise overlaps is the matching-family condition.

The sheaf axiom then supplies a unique global glue.

Therefore one should not say:

> pairwise compatibility never implies global consistency.

That would be false in this setting.

The correct boundary is:

> pairwise equalities imply global gluing only relative to a restriction system satisfying the sheaf condition.

## 18. Presheaf versus sheaf

A presheaf supplies local data and restriction maps.

A sheaf additionally satisfies unique gluing.

Therefore the existence of sensible local restriction maps alone does not imply:

`im(R)=ker(Delta)`.

That equality is part of the sheaf-level local-to-global property.

## 19. Uniqueness without existence

One can distinguish the two gluing clauses abstractly.

A restriction map R may be injective, so at most one global object can realize a local family, while some matching local families still fail to lie in `im(R)`.

This is the separated-but-not-necessarily-sheaf situation.

The Atlas needs only the logical distinction, not the full categorical terminology.

## 20. Exact versus approximate compatibility

In the incompatible witness:

`Delta=-1`.

Exact sheaf gluing fails.

If the data represent noisy measurements, one may instead seek adjusted local values minimizing:

`||Delta||^2`

possibly together with fidelity penalties.

That produces an optimization/fusion problem.

It is not the same statement as exact gluing.

## 21. Approximate section boundary

Robinson's sensor-fusion setting motivates approximate consistency when heterogeneous observations do not agree exactly.

The Atlas uses this only as an application boundary:

- exact compatibility is an equality constraint;
- approximate compatibility needs a metric, loss, tolerance, or optimization rule.

No one approximate rule is canonical here.

## 22. Interface interpretation

OBJECTS-001 defines an interface as the obligations composition may assume across a boundary.

In the finite witness, the obligation is:

`u_b=v_b`.

The overlap space `F(W)` is the boundary comparison space.

The restriction maps expose what each local object claims at that boundary.

## 23. Compositional interpretation

The construction is compositional because each region can carry its own local section while only overlap data are compared.

Successful assembly requires:

- local validity;
- correct restriction maps;
- overlap agreement;
- a gluing property.

Naive concatenation of local records would not enforce these conditions.

## 24. Global section is not global truth

A global section means the local assignments satisfy the sheaf's compatibility structure.

It does not imply:

- measurements are factually correct;
- the model is semantically adequate;
- the system is stable;
- the chosen restrictions capture every relevant constraint.

Consistency is relative to the sheaf model.

## 25. Downstream interface

Later chapters may consume:

- incidence structure;
- local data spaces;
- restriction maps;
- matching families;
- exact gluing;
- uniqueness;
- discrepancy/obstruction;
- exact versus approximate consistency.

They must independently justify any richer semantics, stability claims, governance conditions, or domain-specific interpretation.
