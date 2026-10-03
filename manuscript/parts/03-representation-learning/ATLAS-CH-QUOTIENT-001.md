# Equivalence and Quotient Geometry
<!-- ATLAS-CH-QUOTIENT-001 -->

**Epistemic status:** Established Theory + Atlas Derivation + Open Research Question  
**Specification:** manuscript/specifications/ATLAS-CH-QUOTIENT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-QUOTIENT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-QUOTIENT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-QUOTIENT-001.yaml

## 1. Different parameters can mean the same thing

Suppose two neural networks have different parameter arrays.

Are they different models?

At the level of stored bytes, yes.

At the level of the represented function, perhaps not.

A hidden-unit permutation can reorder internal coordinates without changing the input-output map.

A positive rescaling in a ReLU network can change incoming and outgoing weights while preserving the function exactly.

A basis change can alter a frame without changing the subspace it spans.

These are not numerical coincidences.

They are redundancies in representation.

Quotient geometry asks us to stop treating redundant representatives as distinct objects when the scientific question concerns the underlying equivalence class.

## 2. Many addresses, one place

Imagine one physical location with several valid addresses.

Different naming conventions can point to the same place.

The structural correspondence is:

- address ↔ parameter representative;
- place ↔ represented function or equivalence class;
- address conversion ↔ symmetry action;
- quotient map ↔ forgetting redundant labels.

The analogy is useful because it separates identity of coordinates from identity of the object.

It also has a strict limit.

Neural parameter spaces can contain:

- fixed points;
- singular strata;
- hidden symmetries;
- changing stabilizers;
- regions where a smooth quotient description fails.

The quotient is not automatically one smooth map of a tidy city.

## 3. Equivalence relations

A relation

\[
\sim
\]

on a set \(X\) is an equivalence relation if it is:

- reflexive;
- symmetric;
- transitive.

The equivalence class of \(x\) is

\[
[x]
=
\{y\in X:y\sim x\}.
\]

The quotient set is

\[
\boxed{
X/{\sim}
=
\{[x]:x\in X\}.
}
\]

The quotient keeps the distinctions that survive the chosen equivalence relation and removes the distinctions declared redundant.

Everything depends on that declaration.

Choose an equivalence relation that is too coarse and functionally different objects can be collapsed together.

## 4. Group actions and orbits

Let a group \(G\) act on \(X\).

The orbit of \(x\) is

\[
G\cdot x
=
\{g\cdot x:g\in G\}.
\]

A natural equivalence relation is

\[
x\sim y
\iff
y=g\cdot x
\text{ for some }g\in G.
\]

Then equivalence classes are group orbits.

This construction is central to symmetry reduction.

It also immediately raises a geometric question:

> Does the orbit space inherit a well-behaved smooth structure?

Sometimes yes.

Sometimes only on a regular subset.

Sometimes singularities remain.

## 5. Grassmann: the canonical example

The Geometry chapter distinguished:

\[
\operatorname{St}(n,p),
\]

the space of ordered orthonormal \(p\)-frames, from

\[
\operatorname{Gr}(n,p),
\]

the space of \(p\)-dimensional subspaces.

If

\[
X\in\operatorname{St}(n,p),
\]

and

\[
Q\in O(p),
\]

then

\[
XQ
\]

is another orthonormal frame spanning the same subspace.

Therefore

\[
\boxed{
\operatorname{Gr}(n,p)
\cong
\operatorname{St}(n,p)/O(p).
}
\]

The quotient removes basis choice.

The subspace remains.

This is not merely philosophical.

It changes which directions are treated as genuine motion.

## 6. Parameter equality versus functional equality

Let

\[
f_\theta
\]

denote the function represented by parameters \(\theta\).

Parameter equality is

\[
\theta=\theta'.
\]

Functional equality is

\[
f_\theta(x)=f_{\theta'}(x)
\]

for every admissible input \(x\).

The second is weaker.

A parameterization can therefore be many-to-one:

\[
\theta
\mapsto
f_\theta.
\]

When that happens, Euclidean geometry in parameter space contains directions that may change coordinates without changing the represented function.

This is the opening for quotient analysis.

## 7. Hidden-unit permutation symmetry

Consider

\[
f(x)
=
W_2\sigma(W_1x),
\]

with elementwise activation \(\sigma\).

Let \(P\) permute hidden units.

Define

\[
W_1'=PW_1,
\]

and

\[
W_2'=W_2P^{-1}.
\]

Because elementwise activation commutes with permutation,

\[
\sigma(Pz)=P\sigma(z).
\]

Therefore

\[
\begin{aligned}
f'(x)
&=
W_2P^{-1}\sigma(PW_1x)\\
&=
W_2P^{-1}P\sigma(W_1x)\\
&=
f(x).
\end{aligned}
\]

The hidden units were relabeled.

The function did not change.

## 8. Exact two-unit example

Take scalar input and

\[
W_1=
\begin{pmatrix}
1\\
2
\end{pmatrix},
\qquad
W_2=
\begin{pmatrix}
3&4
\end{pmatrix}.
\]

With ReLU activation,

\[
f(x)
=
3\operatorname{ReLU}(x)
+
4\operatorname{ReLU}(2x).
\]

For positive \(x\),

\[
f(x)=11x.
\]

For nonpositive \(x\),

\[
f(x)=0.
\]

Swap the hidden units:

\[
W_1'=
\begin{pmatrix}
2\\
1
\end{pmatrix},
\qquad
W_2'=
\begin{pmatrix}
4&3
\end{pmatrix}.
\]

The parameter arrays change.

The function remains

\[
f(x)=11\max(0,x).
\]

## 9. Positive-rescaling symmetry

ReLU is positively homogeneous:

\[
\operatorname{ReLU}(cz)
=
c\operatorname{ReLU}(z),
\qquad
c>0.
\]

For positive diagonal \(D\),

\[
\operatorname{ReLU}(Dz)
=
D\operatorname{ReLU}(z).
\]

Define

\[
W_1''=DW_1,
\]

and

\[
W_2''=W_2D^{-1}.
\]

Then

\[
f''(x)=f(x).
\]

For

\[
D=\operatorname{diag}(2,1/3),
\]

the exact witness becomes

\[
W_1''=
\begin{pmatrix}
2\\
2/3
\end{pmatrix},
\]

\[
W_2''=
\begin{pmatrix}
3/2&12
\end{pmatrix}.
\]

These parameters look very different.

They still compute the same function.

![Three distinct parameter representatives, original, hidden-unit permuted, and positively rescaled, all mapping to the exact same ReLU function f(x)=11 max(0,x).](../../figures/masters/ATLAS-FIG-QUOTIENT-001.png)

## 10. Exact replay

The computational witness evaluates all three parameterizations on

\[
\{-2,-3/2,-1,-1/2,0,1/2,1,3/2,2\}.
\]

Every representative gives

\[
\{0,0,0,0,0,11/2,11,33/2,22\}.
\]

That finite replay is a check.

The algebra above is the reason equality holds for every real input.

This distinction mirrors the Atlas evidence doctrine:

computation and proof can support one another without becoming the same object.

## 11. Why quotienting is tempting

Suppose an optimizer moves through parameter space.

If many parameter directions correspond only to symmetry motion, then ambient Euclidean distance can overstate meaningful change.

Two far-separated parameter vectors may compute the same function.

This suggests a cleaner object:

\[
[\theta]
\in
\Theta/G.
\]

Instead of asking how far parameters moved, ask how far the equivalence class moved.

This can remove redundancy from the description.

It does not automatically remove difficulty from the optimization problem.

## 12. Vertical and horizontal directions

On a regular quotient manifold, tangent directions can be separated conceptually into:

- **vertical directions**, tangent to the symmetry orbit;
- **horizontal directions**, transverse directions that represent quotient motion.

The terminology is standard in quotient geometry [@AbsilMahonySepulchre2008].

A vertical move changes the representative.

A horizontal move changes the equivalence class.

This distinction is especially useful when the scientific object is the represented function rather than the raw parameter vector.

## 13. Local null directions

Suppose

\[
F(\theta)
\]

is constant along a smooth symmetry orbit

\[
\theta(s).
\]

Then

\[
F(\theta(s))
=
F(\theta(0)).
\]

Differentiating at zero gives

\[
J_F(\theta)
\dot\theta(0)
=
0.
\]

The orbit tangent lies in the local null space of the function map.

If a loss depends only on \(F(\theta)\), the loss is also constant along that exact symmetry orbit.

At a smooth critical point, continuous exact symmetries can therefore contribute Hessian-degenerate directions.

This does not mean every flat direction is a symmetry direction.

## 14. Hidden symmetries

Permutation and positive scaling are not necessarily the whole story.

Grigsby, Lindsey, and Rolnick study hidden symmetries in ReLU networks and show that the redundancy structure can be richer and parameter-dependent [@GrigsbyLindseyRolnick2023].

This matters for quotient reasoning.

If the symmetry group changes across parameter space, a single globally regular manifold model may fail.

The orbit space can have different local structure in different regions.

## 15. Symmetry can affect learning dynamics

Symmetry is not only a bookkeeping problem.

It can constrain optimization and interact with regularization and noise.

Ziyin studies consequences of loss symmetries for learned parameter structure under explicit assumptions [@Ziyin2024Symmetry].

The Atlas uses this literature to support a limited point:

> symmetry can influence learning dynamics.

It does not infer that one universal quotient geometry determines all neural training.

## 16. Quotienting removes declared redundancy

Suppose the group \(G\) captures an exact functional symmetry.

Then moving within one orbit does not change the function.

Passing to

\[
\Theta/G
\]

removes those orbit directions from the represented object.

This is a genuine simplification of description.

It can reduce:

- redundant coordinates;
- gauge-like degrees of freedom;
- ambiguity in comparing models.

That is already useful.

A stronger claim would be:

> the quotient objective is easier to optimize.

That does not follow automatically.

## 17. Redundancy removed does not mean convexity

A quotient can still contain:

- multiple functionally distinct minima;
- saddles;
- barriers;
- poor conditioning;
- bifurcations;
- singular regions.

Therefore

\[
\boxed{
\text{symmetry removed}
\not\Rightarrow
\text{convex landscape}.
}
\]

The quotient can be the more intrinsic object while remaining mathematically difficult.

## 18. Singular quotients

A group action is easiest to quotient when it acts freely and regularly.

Neural networks can violate that simplicity.

Examples include:

- a hidden unit with zero incoming or outgoing weights;
- two hidden units that become identical;
- parameter points with extra stabilizer symmetries;
- architecture-dependent hidden symmetries.

At such points, orbit dimension can change.

The quotient can develop singular structure.

This is why the chapter refuses to speak of “the neural-network quotient manifold” without qualifications.

## 19. Function space is an even stronger quotient

One possible equivalence relation is

\[
\theta\sim\theta'
\iff
f_\theta=f_{\theta'}.
\]

This identifies every parameterization of the same function.

Conceptually, that is attractive.

Practically, it may be difficult to characterize.

The exact function-equivalence relation can include more than the obvious architecture symmetries.

The quotient can also lose useful information about optimization trajectories, regularization, or implementation cost.

The most intrinsic representation is not automatically the most useful operational representation.

## 20. Quotienting by the wrong relation

Suppose we declare two models equivalent because they agree on a finite training set.

That relation can merge functions that differ elsewhere.

If the intended object is global predictor behavior, the equivalence is too coarse.

A quotient is only as meaningful as its equivalence relation.

This is the quotient analogue of the boundary-contract question:

> sufficient for what?

## 21. Gauge language

Physics often uses the word **gauge** for representational freedom that does not change observable quantities.

That language can be useful in machine learning when parameter transformations leave the represented function invariant.

But it should be used carefully.

Not every neural symmetry has the full mathematical structure of a gauge theory.

The safe statement is:

> some neural parameter redundancies are gauge-like in the limited sense that multiple representatives encode the same functional object.

The exact group action should be stated.

## 22. Representation equivalence revisited

The Representation chapter introduced invertible recoding:

\[
\tilde z=Tz,
\]

with compatible downstream transformation.

Quotient thinking generalizes the lesson.

A representation is often meaningful only up to some family of transformations.

Possible equivalences include:

- orthogonal basis change;
- invertible linear recoding;
- permutation;
- positive scaling;
- group action;
- exact functional equivalence.

Different questions require different quotients.

There is no universal “correct quotient” for every analysis.

## 23. The benign-nonconvexity question

The Atlas now reaches a frontier question:

> What portion of neural nonconvexity is merely redundancy induced by representation or parameter symmetries, and what portion remains intrinsic after those redundancies are removed?

This is a central motivation for the constructive benign-nonconvexity programme.

The hope is not that quotienting magically makes every problem convex.

The more modest possibility is:

- identify symmetry-induced degeneracy;
- remove it explicitly;
- measure the remaining landscape;
- separate representational difficulty from intrinsic optimization difficulty.

That programme remains open.

## 24. A reconstruction test

Suppose two parameter vectors are declared equivalent.

A useful test is:

> Can every downstream property we intend to preserve be reconstructed from the equivalence class?

If not, the quotient discarded too much.

This reconstruction test connects quotient geometry to the Atlas's broader Residual programme:

find the smallest structure that can change representation while preserving the capability of interest.

## 25. Six failure modes

### Parameter difference mistaken for functional difference

Symmetry-related representatives are counted as distinct models.

### Quotient relation too coarse

Functionally relevant distinctions are erased.

### Quotient relation too narrow

Redundant coordinates remain and contaminate geometry.

### Regular quotient assumed globally

Singular orbit structure is ignored.

### Flat direction assumed to be symmetry

Other sources of degeneracy are overlooked.

### Quotienting assumed to solve optimization

Redundancy removal is promoted into an unsupported global simplicity theorem.

## 26. Atlas connections

**Geometry.**  
Grassmann is the canonical quotient example.

**Representation.**  
Functional or task-relative equivalence can survive coordinate change.

**Normalized representations.**  
Normalization removes one radial degree of freedom, but a sphere cross-section and a quotient by positive scaling should be distinguished mathematically.

**Optimization.**  
Symmetry directions can create redundant ambient motion and local degeneracy.

**Diagnostics.**  
Comparing models may require symmetry alignment before interpreting parameter distance.

**Residual.**  
The next chapter asks what transferable structure survives representation and parameter changes.

**Benign nonconvexity.**  
Quotient structure provides a constructive route for separating redundant from intrinsic landscape complexity.

## 27. Closing view

A parameter vector is often an address, not the place itself.

Two different addresses can point to one function.

Quotient geometry gives us a disciplined way to say which distinctions are representational and which remain intrinsic.

That discipline is already valuable.

It prevents parameter distance from being mistaken for functional distance.

It exposes exact symmetry directions.

It clarifies why some flatness is coordinate-dependent.

But the deeper question remains open.

After we remove the redundancy we understand, what difficulty is left?

That remainder is where the Atlas turns next.

## References used in this chapter

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@EdelmanAriasSmith1998]
- [@GrigsbyLindseyRolnick2023]
- [@Ziyin2024Symmetry]

See \`sources/source-locks/ATLAS-CH-QUOTIENT-001.yaml\` for exact source roles and claim scope.
