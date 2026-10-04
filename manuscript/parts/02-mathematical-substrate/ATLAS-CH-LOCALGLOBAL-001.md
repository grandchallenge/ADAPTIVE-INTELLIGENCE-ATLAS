# Local-to-Global Mathematics
<!-- ATLAS-CH-LOCALGLOBAL-001 -->

**Epistemic status:** standard sheaf/local-to-global mathematics + audited Objects prerequisite + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-LOCALGLOBAL-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-LOCALGLOBAL-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-LOCALGLOBAL-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-LOCALGLOBAL-001.yaml

Many systems are easier to understand locally than globally.

A sensor sees one region.

A module exposes one interface.

A worker holds one piece of state.

A chart describes one patch.

A subsystem enforces one constraint.

The difficult question is not whether each piece makes sense by itself.

It is:

> do the pieces agree where they meet, and if they do, is there one coherent global object that realizes them?

That is the local-to-global problem.

This chapter introduces only the amount of graph and sheaf language needed to make that question precise.

## 1. Local validity is not global coherence

Suppose two teams each provide a locally valid configuration.

One says the shared boundary value is 2.

The other says it is 3.

Nothing is wrong inside either local object.

The failure appears only when the objects are compared on their common interface.

This is the central structural lesson:

> consistency lives on overlaps.

## 2. Start with incidence

Before assigning data, we need to know which pieces touch.

A graph:

`G=(V,E)`

can record pairwise incidence.

A cover:

`U=union_i U_i`

can record which local regions together describe a larger region.

These structures answer:

- what is local?
- which pieces overlap?
- which interfaces exist?

They do not yet say what data live there.

## 3. A graph is not a sheaf

A graph can tell us that vertex A is adjacent to vertex B.

It cannot, by itself, tell us:

- what values A and B carry;
- what part of those values is visible at the edge;
- what equality or transformation the edge requires.

A sheaf-like object adds data spaces and maps over the incidence structure.

This is why graph topology and carried algebra must remain distinct.

## 4. Local sections

For a region `U`, let:

`F(U)`

denote the allowable data on that region.

An element:

`s in F(U)`

is called a local section.

The word **section** is useful because it emphasizes that the data belong to a particular region.

The same numerical vector can be a section on one region and not even be well-typed on another.

## 5. Restriction maps

If:

`V subseteq U`,

a restriction map:

`rho^U_V:F(U)->F(V)`

asks:

> what does the data on U say when viewed only on V?

Restriction must be coherent.

Restricting to the same region does nothing:

`rho^U_U=id`.

Restricting in stages must agree with restricting directly:

`rho^V_W o rho^U_V
=
rho^U_W`

for:

`W subseteq V subseteq U`.

## 6. Why restriction is an interface map

OBJECTS-001 introduced interfaces as the obligations composition may assume across a boundary.

Restriction makes that idea mathematical.

Two larger local objects do not need to be identical.

They need to induce compatible data on what they share.

The shared region is the comparison interface.

## 7. Matching families

Let:

`{U_i}`

cover U.

Choose one local section:

`s_i in F(U_i)`

for each region.

The family is matching when every pair agrees after restriction to its overlap:

`rho^{U_i}_{U_i intersect U_j}(s_i)
=
rho^{U_j}_{U_i intersect U_j}(s_j)`.

This is exact compatibility.

## 8. Compatibility is typed

The two local sections may live in different spaces:

`F(U_i)`

and:

`F(U_j)`.

They become comparable only after both are mapped into:

`F(U_i intersect U_j)`.

This prevents a common category error:

> compare whole local states when only boundary data are supposed to agree.

## 9. A presheaf gives the restriction machinery

A presheaf supplies:

- local data spaces;
- restriction maps;
- identity and composition laws.

That is already useful.

It gives a disciplined way to talk about local views.

But it does not yet guarantee that compatible local views come from one global object.

## 10. A sheaf adds unique gluing

A sheaf adds the local-to-global property.

For every matching family over a cover, there must exist a unique:

`s in F(U)`

whose restriction to each `U_i` is `s_i`.

The word **unique** matters.

The condition has two parts:

1. existence;
2. uniqueness.

## 11. Existence and uniqueness answer different questions

Existence asks:

> can these local pieces be assembled at all?

Uniqueness asks:

> if they can, do they determine one global object or several?

A system can fail either way.

Keeping these clauses separate is useful far beyond sheaf theory.

## 12. The equalizer picture

For a finite cover, gather all local restrictions into a map:

`R:F(U)->prod_i F(U_i)`.

Gather all overlap discrepancies into a map:

`Delta:prod_i F(U_i)->prod_{i,j}F(U_i intersect U_j)`.

Matching families satisfy:

`Delta=0`.

The sheaf condition says, informally:

> the local families that actually come from global sections are exactly the matching families, and the global source is unique.

For vector-space-valued examples:

`im(R)=ker(Delta)`

with R injective.

## 13. Why this is a useful computational form

The equalizer picture turns local-to-global reasoning into explicit operations:

- restrict;
- subtract on overlaps;
- test a kernel condition;
- reconstruct.

That is exactly the amount of sheaf theory needed for many finite engineering examples.

The deeper theory remains available later if needed.

## 14. Exact witness: three points

Let:

`X={a,b,c}`.

Use the cover:

`U={a,b}`

and:

`V={b,c}`.

Their overlap is:

`W={b}`.

This is the smallest example that has:

- two local regions;
- one genuine overlap;
- one global union.

## 15. Sections are functions

For every subset `S` of X, define:

`F(S)=R^S`.

A section is simply a real-valued function on S.

Restriction means forgetting coordinates outside the smaller subset.

Nothing abstract is hidden.

## 16. The global-to-local map

Write a global section as:

`(x,y,z)`.

Its restrictions are:

`(x,y)`

on U and:

`(y,z)`

on V.

So:

`R(x,y,z)=(x,y,y,z)`.

## 17. Uniqueness is injectivity

Suppose two global sections have the same restrictions to U and V.

They agree at:

- a because U contains a;
- b because both regions contain b;
- c because V contains c.

Therefore the global sections are equal.

In matrix language, R has rank 3.

The local restrictions determine at most one global function.

## 18. The overlap-discrepancy map

A general pair of local sections is:

`((u_a,u_b),(v_b,v_c))`.

Define:

`Delta(u_a,u_b,v_b,v_c)
=
u_b-v_b`.

The pair is compatible exactly when:

`Delta=0`.

The discrepancy lives precisely on the overlap coordinate b.

## 19. Image equals kernel

The image of R consists of vectors:

`(x,y,y,z)`.

The kernel of Delta consists of vectors satisfying:

`u_b=v_b`.

These are the same set.

Therefore:

`im(R)=ker(Delta)`.

This is the exact gluing statement in the finite witness.

## 20. A compatible family

Choose:

`s_U=(1,2)`

and:

`s_V=(2,4)`.

The overlap values both equal 2.

So:

`Delta=0`.

The unique global glue is:

`s=(1,2,4)`.

## 21. An incompatible family

Now choose:

`q_U=(1,2)`

and:

`q_V=(3,4)`.

The overlap discrepancy is:

`Delta=2-3=-1`.

It is nonzero.

Therefore the pair is not in the image of R.

No global function can restrict to both local sections.

## 22. The failure is localized

The value at a is not a problem.

The value at c is not a problem.

The incompatibility is entirely at b.

This is one practical virtue of explicit overlap maps:

> they tell us where coherence fails.

## 23. Gluing is stronger than aggregation

Suppose we simply concatenate the two local records:

`(1,2,3,4)`.

We have stored all the data.

We have not resolved the fact that the two copies of b disagree.

Aggregation collects.

Gluing enforces compatibility.

## 24. The graph view of the witness

Represent U and V as two vertices.

Connect them by an edge because their overlap is nonempty.

That graph records interaction.

But the numerical obstruction `-1` does not come from the graph alone.

It comes from:

- data spaces;
- restrictions;
- the two local sections.

The carried algebra matters.

## 25. Cellular sheaves make graph-local algebra explicit

Cellular sheaves assign data spaces to cells and maps along incidences under a declared convention.

This creates a finite algebraic object over a graph or cell complex.

Curry develops cellular sheaves as a computable combinatorial sheaf framework, and Hansen–Ghrist develop further graph/cell-complex structure.

The Atlas needs only the elementary idea here.

## 26. We do not need cohomology yet

Sheaf cohomology is a powerful obstruction and structural tool.

It is not required to understand the basic gluing mechanism.

For this chapter, a nonzero overlap discrepancy already provides an exact finite obstruction.

The more advanced machinery would distract from the foundational idea.

