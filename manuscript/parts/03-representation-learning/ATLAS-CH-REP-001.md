# Representations and Invariants
<!-- ATLAS-CH-REP-001 -->

**Epistemic status:** Established Theory + Atlas Synthesis + Computational Witness  
**Specification:** manuscript/specifications/ATLAS-CH-REP-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-REP-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-REP-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-REP-001.yaml

## 1. A representation is not merely a vector

A learned representation is often described as a vector

\[
z\in\mathbb R^d.
\]

That description tells us where the coordinates live.

It does not tell us:

- what transformations preserve meaning;
- which coordinates are arbitrary;
- which symmetries are respected;
- what downstream tasks can recover;
- which latent factors are identifiable;
- whether sparse features exist;
- whether multiple features share dimensions.

The Atlas therefore uses a stronger working definition.

A representation is an information-bearing encoding whose geometry, invariances, equivalences, and downstream transformation laws matter.

This framing is consistent with the broad representation-learning literature [@BengioCourvilleVincent2013], but the exact organization used here is Atlas synthesis.

## 2. Languages that preserve the same message

Consider two languages.

Their words look different.

Their grammar may differ.

Yet a translation can preserve the distinctions needed by a reader.

This is a useful analogy for representation equivalence.

Two encodings may differ coordinate-by-coordinate while preserving the structure needed by downstream computation.

The analogy fails if taken literally.

Natural-language translation is approximate, context-dependent, and not generally invertible.

Representation equivalence must be defined mathematically for the property we care about.

## 3. Representation map

Let

\[
r:\mathcal X\to\mathcal Z
\]

map inputs into a representation space.

A representation is useful only relative to some downstream purpose.

That purpose might involve:

- classification;
- control;
- reconstruction;
- retrieval;
- prediction;
- planning;
- communication.

There is therefore no universal scalar called “representation quality.”

Different tasks can prefer different structures.

## 4. Coordinates versus represented structure

Suppose

\[
z=r(x).
\]

For a finite-dimensional real representation space \(\mathcal Z=\mathbb R^d\), apply an invertible linear transformation

\[
T:\mathbb R^d\to\mathbb R^d
\]

and define

\[
\tilde z
=
Tz.
\]

The coordinates changed.

Did the representation change?

The answer depends on the downstream computation.

If a linear readout is

\[
y=w^\top z,
\]

then choosing

\[
\tilde w
=
T^{-\top}w
\]

gives

\[
\tilde w^\top\tilde z
=
w^\top z.
\]

For this readout class, the recoding is behavior-preserving.

This motivates an important distinction:

\[
\boxed{
\text{coordinate identity}
\neq
\text{functional equivalence}.
}
\]

## 5. Exact recoding witness

Take

\[
T=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\]

\[
z=(2,3),
\]

and

\[
w=(4,-1).
\]

The original readout is

\[
w^\top z=5.
\]

The transformed representation is

\[
\tilde z=Tz=(5,3).
\]

The transformed readout is

\[
\tilde w=T^{-\top}w=(4,-5).
\]

Then

\[
\tilde w^\top\tilde z=5.
\]

Nothing in this example says the two coordinate systems are semantically identical for every possible downstream task.

It establishes one exact equivalence relation for a declared readout class.

## 6. Invariance

Suppose a group \(G\) acts on inputs.

A representation is invariant when

\[
\boxed{
r(g\cdot x)=r(x)
}
\]

for the transformations under consideration.

Invariance intentionally removes distinctions.

That can be useful.

If image classification should not change under a small translation, a translation-invariant feature can reduce unnecessary variability.

But invariance has a cost.

If the downstream task requires the transformed quantity, the information has been erased.

A position-invariant representation is poor for a task that must report position.

## 7. Equivariance

Equivariance preserves transformation structure rather than erasing it.

Let

\[
\rho(g)
\]

be the action of group element \(g\) in representation space.

Then equivariance means

\[
\boxed{
r(g\cdot x)
=
\rho(g)r(x).
}
\]

The input transforms.

The representation transforms predictably.

Group-equivariant neural architectures provide concrete examples of this principle [@CohenWelling2016].

## 8. Reflection witness

![A reflection example showing an equivariant vector and invariant norm beside an invertible coordinate recoding that preserves a linear readout.](../../figures/masters/ATLAS-FIG-REP-001.png)

Let

\[
G=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

reflect the first coordinate.

For

\[
x=(2,3),
\]

\[
Gx=(-2,3).
\]

The identity representation

\[
r(x)=x
\]

is equivariant:

\[
r(Gx)=Gr(x).
\]

The scalar representation

\[
r_{\rm inv}(x)
=
\|x\|_2^2
\]

is invariant:

\[
r_{\rm inv}(Gx)
=
r_{\rm inv}(x)
=
13.
\]

These are different design choices.

One preserves the transformation.

The other removes it.

## 9. Invariance and equivariance are not synonyms

The difference matters.

Invariance says:

> the representation should not change.

Equivariance says:

> the representation should change in a predictable corresponding way.

A system that confuses these can destroy useful structure.

The right choice depends on the task.

## 10. Geometry enters representation

The Geometry chapter established that admissible states can live on constrained spaces.

Representation learning inherits that fact.

Examples include:

- unit-normalized embeddings;
- orthogonal frames;
- quotient representations;
- spherical positions;
- subspace-valued features.

A representation is therefore not always best modeled as an unconstrained point in \(\mathbb R^d\).

Its geometry can carry semantics.

This is the direct handoff from the Geometry keystone.

## 11. Information enters representation

The previous chapter supplied probability and information structure.

Representation learning often asks whether an encoding preserves or discards statistically relevant information.

But an information measure does not completely determine representation quality.

Two encodings can have the same mutual information with a target and still differ in:

- geometry;
- robustness;
- linear accessibility;
- sparsity;
- causal role;
- compositional compatibility.

Information is one axis.

Representation structure is richer.

## 12. Identifiability

Suppose latent variables \(z\) generate observations through a decoder

\[
x=f(z).
\]

Now choose an invertible transformation \(T\) and define

\[
\tilde z=Tz.
\]

The decoder can be rewritten as

\[
\tilde f(\tilde z)
=
f(T^{-1}\tilde z).
\]

The same observations can therefore be explained through different latent coordinates.

Without additional assumptions, there may be no unique latent representation.

This is an identifiability problem.

## 13. Disentanglement needs assumptions

A common hope is that unsupervised learning will recover independent or semantically meaningful generative factors automatically.

That hope requires care.

Locatello et al. show that unsupervised disentanglement is not identifiable without inductive biases under the setting they analyze [@LocatelloEtAl2019].

The Atlas uses that result as a boundary.

It does not conclude that disentanglement is useless.

It concludes that claims of uniquely recovered semantic factors require assumptions, supervision, or other structure.

## 14. Sparse representations

A representation is sparse when relatively few coefficients are active.

One classical model writes

\[
x\approx D\alpha,
\]

where \(D\) is a dictionary and \(\alpha\) is sparse.

Olshausen and Field gave a historically influential example in which sparse coding of natural images produced localized oriented receptive-field-like structures [@OlshausenField1996].

This is evidence for one representation regime.

It is not proof that neural representations are universally sparse.

## 15. Dictionaries and features

A dictionary representation introduces another distinction.

The coordinates \(\alpha_i\) are meaningful only relative to dictionary elements \(d_i\).

Changing the dictionary changes the coordinate interpretation.

The Atlas will later use this observation when discussing:

- feature dictionaries;
- sparse autoencoders;
- superposition;
- reconstruction;
- transferable residual structure.

Again, coordinates and represented structure are not identical objects.

## 16. Superposition

If the number of potentially useful features exceeds the number of representational dimensions, a system may encode multiple features non-orthogonally.

Toy Models of Superposition studies this phenomenon in deliberately simplified systems and provides geometric and empirical toy-model evidence [@ElhageEtAl2022Superposition].

The source is useful.

Its scope is narrow.

The Atlas does not infer:

> all frontier neural networks store features exactly according to the toy model.

The chapter uses superposition as a research concept, not a universal established law.

## 17. Representation equivalence

What does it mean for two representations to be “the same”?

There is no single answer.

Possible equivalence relations include:

- exact coordinate equality;
- invertible linear recoding;
- invertible nonlinear recoding;
- equality up to group action;
- equality of pairwise distances;
- equality of downstream predictions;
- equality of recoverable sufficient statistics.

Different scientific questions require different equivalence relations.

The Atlas therefore treats “representation equivalence” as a declaration, not a default.

## 18. Quotient thinking

If multiple coordinates represent the same object, the mathematically natural object may be an equivalence class.

That leads toward quotient spaces.

For example, the Geometry chapter distinguished orthonormal frames from the subspaces they span.

Different frames can represent the same subspace.

The later Quotient Representations chapter generalizes this lesson.

## 19. Representation collapse

A representation can discard too much.

If

\[
r(x)=c
\]

for every input, the representation is perfectly invariant to everything.

It is also useless for tasks that need to distinguish inputs.

This is the simplest counterexample to the idea that more invariance is always better.

The useful question is:

> invariant to what, while preserving what?

## 20. Identical task performance does not imply identical mechanism

Two representations can support the same benchmark score.

That does not mean they encode the same internal structure.

One may use:

- sparse features;
- distributed features;
- different symmetries;
- different causal pathways;
- different robustness margins.

Behavioral equivalence on one task is therefore a weak equivalence relation.

Mechanistic claims require stronger evidence.

## 21. The Residual question

The Atlas later asks a more ambitious question:

> What is the minimal transferable structure that survives relevant representational changes?

That programme uses the provisional term **Residual**.

This chapter does not answer the question.

It prepares the mathematics required to ask it correctly.

If representations can differ under recoding while preserving capability, then the transferable object may not be any one coordinate system.

## 22. Five failure modes

### Coordinates mistaken for meaning

A basis component is treated as a semantic primitive without an identifiability argument.

### Invariance mistaken for universal virtue

Task-relevant variation is erased.

### Equivariance claimed without group action

The transformation law is not specified.

### Disentanglement claimed without assumptions

Non-identifiability is ignored.

### Toy superposition promoted to universal mechanism

A bounded research model is treated as established empirical prevalence.

## 23. Atlas connections

**Normalized representations.**  
Once geometry matters, unit-norm and hyperspherical representations become natural special cases.

**Quotient representations.**  
Equivalence under transformations suggests quotient structure.

**Attention and position.**  
Representations are acted on by state-dependent and position-dependent operators.

**Memory.**  
External stores may preserve semantic objects under different internal encodings.

**Diagnostics.**  
Interpretability must distinguish coordinate features from invariant or causally relevant structure.

**Residual programme.**  
Transfer under representation change becomes a first-class question.

## 24. Closing view

A representation is not just where a vector lives.

It is a contract between an input, an encoding, a transformation law, and a downstream use.

Its coordinates can change while capability survives.

Its invariances can help or destroy.

Its latent factors may not be identifiable.

Its features may be sparse, distributed, or superposed.

The Atlas therefore asks a stronger question than:

> What is the representation?

It asks:

> Which properties of the representation survive the transformations that should not matter, and which distinctions remain available to the computations that do?

That question opens the path to normalized geometry, quotient spaces, and the search for transferable residual structure.

## References used in this chapter

- [@BengioCourvilleVincent2013]
- [@CohenWelling2016]
- [@LocatelloEtAl2019]
- [@OlshausenField1996]
- [@ElhageEtAl2022Superposition]
