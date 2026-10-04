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



## 27. Pairwise compatibility needs the sheaf context

A common slogan says:

> pairwise agreement does not imply global agreement.

That slogan is too crude here.

For an actual sheaf over an open cover, agreement on every pairwise overlap is precisely the matching-family condition, and the sheaf axiom supplies a unique global glue.

The correct warning is different:

> pairwise plausibility in an arbitrary constraint system is not enough unless the restriction structure and gluing property are specified.

## 28. Local-to-global claims are model-relative

A global section is global relative to the chosen sheaf.

Change:

- the regions;
- the data spaces;
- the restriction maps;
- the overlap semantics;

and the set of global sections can change.

Therefore a successful glue is evidence about one declared local-to-global model.

It is not universal coherence.

## 29. Exact consistency is brittle by design

If one local sensor reports 2.000 and another reports 2.001, exact equality fails.

That is not a defect in the sheaf condition.

It means the mathematical claim being tested is exact.

If the application tolerates small discrepancies, it needs a different object:

- a metric;
- a tolerance;
- a likelihood;
- a loss;
- an optimization problem.

## 30. Approximate consistency is a second layer

Robinson's sensor-integration work makes this distinction operational.

Local measurements can be compared through a sheaf model even when they are not exactly consistent.

One can then define an approximate-section or fusion problem.

The Atlas keeps the layers separate:

1. exact structural compatibility;
2. approximate repair/fusion.

## 31. An approximate glue is not a sheaf-theoretic equality

Suppose the overlap values are:

`2`

and:

`2.1`.

A least-squares procedure might replace both with:

`2.05`.

That can be sensible.

But it changes the data.

The original family still did not satisfy exact compatibility.

The optimization result and the sheaf-gluing result are different claims.

## 32. Local truth is not required

A section can be mathematically valid while factually wrong.

Suppose two sensors both report 100 when the true value is 0.

Their data can glue perfectly.

The sheaf has checked consistency, not truth.

This distinction will matter whenever sheaf language is used for evidence fusion.

## 33. Global consistency is not semantic adequacy

A software system can satisfy all declared interface equalities and still implement the wrong specification.

A scientific model can integrate all measurements consistently while omitting a latent variable.

A local-to-global formalism checks the contracts it was given.

It does not prove the contracts are complete.

## 34. Local-to-global structure can expose hidden assumptions

The advantage is not only successful reconstruction.

Writing explicit overlaps forces questions such as:

- what must two modules agree on?
- which values are shared?
- which transformations compare them?
- where can inconsistency appear?

That makes assumptions inspectable.

## 35. Graphs provide the skeleton

A graph or hypergraph can organize:

- subsystems;
- agents;
- sensors;
- patches;
- data sources;
- interfaces.

It gives the combinatorial skeleton.

A sheaf-like structure then says what algebra or information moves across that skeleton.

Keeping those layers distinct makes models easier to audit.

## 36. Covers provide another skeleton

Sometimes the natural structure is spatial or semantic rather than graph-first.

A collection:

`{U_i}`

covers a larger domain.

Overlaps:

`U_i intersect U_j`

become the places where local descriptions must agree.

This view is natural for:

- coordinate charts;
- distributed observations;
- overlapping datasets;
- decomposed physical domains.

## 37. Interface data can be lower-dimensional

Two large subsystems may share only a small boundary.

They need not expose all internal state.

Restriction maps formalize this compression:

`F(U_i)->F(U_i intersect U_j)`.

The local-to-global problem can therefore be much smaller than comparing whole subsystem states.

This anticipates later boundary-contract and separator ideas without importing them as prerequisites.

## 38. Compatibility can be transformed rather than literal identity

In the function witness, both sides restrict to the same scalar and equality is literal.

More general sheaves can use maps that translate local coordinates into a common comparison space.

Thus the real principle is not:

> local arrays must be numerically equal.

It is:

> their induced boundary data must agree after the declared restriction maps.

## 39. Coordinate changes fit naturally

Two charts can describe the same underlying object with different coordinates.

The overlap maps translate each local representation before comparison.

This is one reason local-to-global mathematics appears throughout geometry.

The Atlas will use the same structural idea later in more computational settings.

## 40. Composition requires more than adjacency

Connecting modules with arrows is not enough.

A meaningful composition needs:

- compatible types;
- compatible boundary semantics;
- agreement on shared quantities;
- a rule for assembling the composite.

Sheaf gluing provides one mathematically clean archetype for such assembly.

It is not the only possible compositional formalism.

## 41. Obstruction certificates are valuable outputs

When gluing fails, the answer need not be only:

> no.

A useful system should expose:

- which overlap failed;
- by how much;
- under which restriction maps;
- which local sections were involved.

In the witness, the certificate is:

`Delta=-1`

at b.

That is already actionable.

## 42. A larger graph produces a discrepancy vector

For many overlaps, collect all boundary disagreements into:

`Delta(s)`.

Then:

`Delta(s)=0`

means exact compatibility.

Nonzero coordinates localize violated interfaces.

This is a finite linear-algebra pattern that later chapters can reuse.

## 43. Zero discrepancy can have several meanings

A zero discrepancy might arise because:

- the data are genuinely consistent;
- the restrictions are too weak to detect a conflict;
- the comparison space has discarded important information;
- two wrong local models happen to agree.

Therefore the quality of the restriction maps matters.

An easy compatibility test can be weak evidence.

## 44. Richer interfaces detect more and cost more

A boundary representation that exposes more information can detect more incompatibilities.

It can also increase:

- communication;
- storage;
- computation;
- coupling.

This creates a general design tradeoff:

> expose enough boundary structure to protect composition, but not so much that modularity disappears.

The chapter does not solve this tradeoff.

It only makes it visible.

## 45. Sheaf language should earn its keep

The word **sheaf** is useful when the problem genuinely has:

- local data;
- overlaps/incidences;
- restriction maps;
- a local-to-global question.

If those objects are absent, sheaf language can become decorative.

The Atlas therefore applies a discipline:

> name the section spaces and restriction maps before claiming a sheaf viewpoint.

## 46. A practical local-to-global ledger

Before accepting a gluing claim, record:

| Field | Question |
|---|---|
| domain | What is the global object/space? |
| local regions | Which pieces cover or compose it? |
| incidence | Which pieces overlap or meet? |
| local data | What is `F(U_i)`? |
| overlap data | What is `F(U_i intersect U_j)`? |
| restrictions | How is local data mapped to the overlap? |
| compatibility | Which equalities must hold? |
| existence | Does every matching family considered have a glue? |
| uniqueness | Can two global objects have the same local restrictions? |
| obstruction | What records a failure to match? |
| approximation | If disagreement is tolerated, which metric/loss? |
| interpretation | What does a global section mean in the application? |
| boundary | What does consistency not prove? |

This ledger prevents local-to-global language from becoming metaphor.

## 47. Failure modes

### Graph-equals-sheaf

Incidence structure is confused with the data and maps carried over it.

### Local-equals-global

Locally valid pieces are assumed to assemble without overlap checks.

### Pairwise-plausible-equals-matching

Informal compatibility substitutes for exact restriction equations.

### Matching-equals-truth

A global section is treated as factual correctness.

### Approximate-equals-exact

A low-loss fusion is described as exact gluing.

### Zero-obstruction-equals-complete-model

The declared restrictions agree, so omitted constraints are assumed not to exist.

### Sheaf-as-decoration

The terminology is used without explicit section spaces or restriction maps.

## 48. What the exact witness establishes

The companion witness proves:

- the global-to-local map `R:R^3->R^4` is injective;
- the overlap discrepancy is `Delta(u_a,u_b,v_b,v_c)=u_b-v_b`;
- `im(R)=ker(Delta)`;
- `(1,2)` on U and `(2,4)` on V glue uniquely to `(1,2,4)`;
- `(1,2)` on U and `(3,4)` on V have discrepancy `-1` and cannot glue;
- the obstruction is localized to the shared coordinate b.

Nothing about noisy fusion, semantic truth, or global system stability is inferred.

## 49. Downstream handoff

Later chapters may now assume the following local-to-global vocabulary:

- graph/cover incidence;
- local section;
- restriction map;
- matching family;
- gluing existence;
- gluing uniqueness;
- discrepancy/obstruction;
- exact versus approximate compatibility.

They must independently define their domain-specific section spaces, restriction maps, and interpretation.

The local-to-global lesson is simple:

> make the interfaces explicit, compare what each local piece says there, and do not call the whole coherent until the gluing condition is actually satisfied.

## References used in this chapter

- Justin Michael Curry, *Sheaves, Cosheaves and Applications*, University of Pennsylvania doctoral thesis, 2014, arXiv:1303.3255.
- Michael Robinson, *Sheaves are the canonical data structure for sensor integration*, Information Fusion 36 (2017), 208–224, DOI 10.1016/j.inffus.2016.12.002.
- Jakob Hansen and Robert Ghrist, *Toward a spectral theory of cellular sheaves*, Journal of Applied and Computational Topology 3 (2019), 315–358, DOI 10.1007/s41468-019-00038-7.

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-LOCALGLOBAL-001.yaml
