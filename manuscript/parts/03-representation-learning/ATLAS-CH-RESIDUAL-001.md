# The Residual
<!-- ATLAS-CH-RESIDUAL-001 -->

**Epistemic status:** Atlas/GCL Research Synthesis + Established Supporting Theory + Exact Toy Witness  
**Specification:** manuscript/specifications/ATLAS-CH-RESIDUAL-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-RESIDUAL-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-RESIDUAL-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-RESIDUAL-001.yaml

## 1. What survives when representation changes?

Suppose two systems implement the same useful capability through very different internal coordinates.

One uses dense vectors.

Another uses sparse features.

A third uses an operator basis.

A fourth has been permuted, rescaled, normalized, compressed, or otherwise reparameterized.

What, if anything, must survive?

The Atlas uses the provisional name **Residual** for the answer we are trying to find:

> the smallest transferable structure sufficient to reconstruct a declared capability after admissible changes of representation.

The word is intentionally singular.

The theory is not.

There may be no unique universal Residual.

There may be no finite-dimensional one.

There may be no efficiently computable one.

The object can only be discussed after the capability, transformations, and admissible descriptor class have been declared.

## 2. The thing that cannot be transformed away

A useful GCL phrase is:

> The Residual is the thing that cannot be transformed away.

Taken literally, that phrase is too strong.

Many objects can survive a transformation while being irrelevant.

A constant survives almost everything.

What matters is not survival alone.

The proposed object must satisfy at least three demands:

1. it survives the transformations we have declared irrelevant;
2. it still contains enough structure to reconstruct the capability we care about;
3. among admissible such descriptions, it retains no unnecessary distinctions.

So the stronger working phrase is:

> The Residual is the least admissible structure that survives the declared representational changes while remaining sufficient to reconstruct the declared capability.

That is the object this chapter formalizes.

## 3. The message that survives translation

The pedagogical allegory is a message translated between languages.

The surface symbols change.

Word order may change.

The alphabet may disappear entirely.

Yet a receiver can still recover what is needed to act.

The structural correspondence is:

- language ↔ representation;
- translation ↔ admissible representation change;
- task-relevant meaning ↔ declared capability;
- compact adequate message ↔ Residual.

The limit is important.

Human meaning is not a formal mathematical map.

Translation is rarely invertible.

“Shortest message” depends on the coding language and admissible operations.

The allegory teaches one point only:

> what survives is meaningful here only because it remains reconstructively sufficient for something declared in advance.

## 4. From representation equivalence to reconstruction

The Representation chapter established that coordinate identity is stronger than functional equivalence.

The Quotient chapter established that multiple parameter representatives can encode one function.

Those results remove a common mistake:

\[
\text{different coordinates}
\not\Rightarrow
\text{different capability}.
\]

The Residual question goes further.

It asks:

> Once representation-specific redundancy is removed, what portable structure is still enough to rebuild the capability?

This is not merely a quotient question.

A quotient tells us which distinctions we are willing to ignore.

A Residual must also pass a reconstruction test.

## 5. Declaring the problem

Let

\[
X
\]

be a representation or system-state space.

Let

\[
G
\]

be a declared family of admissible transformations acting on \(X\).

Let

\[
\mathcal Q
\]

be a declared family of capability probes, contexts, or interventions.

Let

\[
B:X\times\mathcal Q\to\mathcal Y
\]

be the declared behavior profile.

For each state \(x\), write

\[
B_x(q)=B(x,q).
\]

Finally, let

\[
\mathfrak D
\]

be a declared class of admissible portable descriptors.

This last object matters more than it first appears.

Without it, the problem can collapse into a tautology.

## 6. Transformation invariance

A descriptor

\[
R:X\to\mathcal Z,
\qquad
R\in\mathfrak D,
\]

is invariant to the declared representation changes when

\[
\boxed{
R(g\cdot x)=R(x)
}
\]

for every admissible \(g\in G\).

Invariance is necessary for the intended notion of transfer.

It is not sufficient.

The constant descriptor

\[
R_0(x)=0
\]

is invariant under every transformation.

It usually preserves no useful capability.

## 7. Capability sufficiency

A descriptor \(R\) is sufficient for the declared behavior profile when there exists a reconstructor

\[
D:\mathcal Z\times\mathcal Q\to\mathcal Y
\]

such that

\[
\boxed{
B(x,q)=D(R(x),q)
}
\]

for every declared state/probe pair.

This is capability reconstruction.

It is weaker than full-state reconstruction.

The Residual is allowed to forget anything the declared capability does not need.

That forgetting is not a bug.

It is the point.

## 8. The factorization preorder

Suppose we have two descriptors,

\[
R_1:X\to Z_1,
\]

and

\[
R_2:X\to Z_2.
\]

Write

\[
R_1\preceq R_2
\]

when there exists an admissible post-processing map \(\phi\) from a declared class \(\mathfrak M\), with

\[
\phi:Z_2\to Z_1
\]

such that

\[
\boxed{
R_1=\phi\circ R_2.
}
\]

Interpretation:

\(R_1\) contains no more distinctions than \(R_2\), because everything in \(R_1\) can be recovered from \(R_2\).

This is a preorder when the declared post-processing class contains identities and is closed under composition.

If \(\mathfrak M\) is the class of all set-theoretic maps, the preorder is purely semantic.

If \(\mathfrak M\) is restricted to efficiently computable, bounded-cost, differentiable, or otherwise admissible maps, the preorder becomes operationally stronger.

The leastness argument below uses unrestricted set-theoretic post-processing. If \(\mathfrak M\) is restricted, an abstract decoder witnessing sufficiency need not belong to \(\mathfrak M\); it cannot be used to certify operational leastness without that additional check.

Two different codings can factor through one another.

That is exactly what we want: coordinate choice should not automatically create a new intrinsic object.

## 9. Least, not merely small

Let

\[
\mathcal S_{B,G,\mathfrak D}
\]

be the admissible descriptors that are both:

- invariant under \(G\);
- sufficient for \(B\).

A provisional Residual is a **least element** of this class under \(\preceq\).

Thus \(R\) must satisfy

\[
R\preceq S
\]

for every

\[
S\in\mathcal S_{B,G,\mathfrak D}.
\]

This is stronger than saying \(R\) is “small.”

It is also stronger than saying no obviously redundant field remains.

Every other admissible invariant sufficient descriptor must be able to produce \(R\).

## 10. Why leastness is useful

Suppose \(R\) and \(R'\) are both least.

Then

\[
R=\phi\circ R',
\]

and

\[
R'=\psi\circ R
\]

for some maps \(\phi,\psi\).

On the realized images,

\[
\psi\circ\phi
=
\operatorname{id},
\]

and

\[
\phi\circ\psi
=
\operatorname{id}.
\]

So two least Residuals are equivalent up to invertible recoding on what the system actually realizes.

This is the kind of non-uniqueness the Atlas can tolerate.

Different coordinates need not mean different Residual structure.

## 11. The behavior-table trap

There is an immediate problem.

If \(\mathfrak D\) allows arbitrary descriptors, define

\[
R_B(x)=B_x.
\]

That is, store the complete behavior profile itself.

Then a decoder can simply evaluate

\[
R_B(x)(q).
\]

If \(B_x\) is invariant under the declared representation changes, \(R_B\) is an invariant sufficient descriptor.

And because every sufficient descriptor must be able to reconstruct \(B_x\), the full behavior profile is already least under factorization.

Mathematically, this is fine.

Scientifically, it can be useless.

We wanted transferable mechanism.

We got a behavior table.

## 12. Descriptor admissibility is part of the theorem statement

A nontrivial Residual programme therefore has to declare what counts as an admissible portable descriptor.

Possible restrictions include:

- bounded description length;
- finite-dimensionality;
- efficient computability;
- architectural independence;
- intervention stability;
- bounded reconstruction cost;
- portability across model families;
- composability with a fixed interpreter.

The choice is not housekeeping.

It changes the object.

The Residual is therefore relative to

\[
(B,G,\mathfrak D,\mathcal Q).
\]

Suppressing those arguments may be convenient later.

It is dangerous at the beginning.

## 13. Classical sufficiency as a model

Statistics gives a mature example of this kind of reasoning.

A sufficient statistic preserves all sample information needed for inference about a declared parameter under a declared statistical model.

Minimal sufficiency then asks for a statistic that is no more informative than any other sufficient statistic, in the appropriate factorization sense [@LehmannCasella1998].

The Residual borrows this pattern:

- declare what must be preserved;
- identify nuisance variation;
- compress without losing what matters;
- compare candidate descriptions by factorization.

The Residual is broader.

Therefore classical sufficiency theorems do not automatically apply.

## 14. Minimal sufficient representations

Achille and Soatto study task-relative representations in terms of:

- sufficiency;
- minimality;
- invariance to nuisance factors [@AchilleSoatto2018].

This is close in spirit to the Residual programme.

It supports a key lesson:

> minimality is not meaningful without a declared task and nuisance structure.

The Atlas extends the question beyond one probabilistic representation-learning setup toward transferable computational structure.

That extension is ours.

It is not a theorem imported from the paper.

## 15. Information bottleneck

The information bottleneck programme asks for compressed encodings that preserve information relevant to a declared target [@TishbyPereiraBialek2000].

Again, the structural analogy is strong:

\[
\text{compress}
\quad\text{while preserving what matters}.
\]

But the Residual is not defined here as an information-bottleneck optimum.

A Residual may be:

- symbolic;
- algorithmic;
- operator-valued;
- graph-structured;
- programmatic;
- hybrid.

Mutual information is one possible formalization, not the definition.

## 16. A calibration toy model

Let

\[
X=\mathbb R^2,
\]

with state

\[
x=(s,n).
\]

Interpret:

- \(s\): task-relevant signal;
- \(n\): nuisance.

Let admissible transformations translate only the nuisance coordinate:

\[
g_a(s,n)
=
(s,n+a).
\]

Use a singleton probe family for this calibration example and define capability

\[
B(s,n)=s.
\]

Now define

\[
R(s,n)=s.
\]

This is deliberately simple.

It is a calibration case for the definitions, not evidence for a frontier-model Residual.

## 17. Invariance of the toy Residual

For any \(a\),

\[
R(g_a(s,n))
=
R(s,n+a)
=
s.
\]

Therefore

\[
R(g_a x)=R(x).
\]

The Residual is constant along vertical nuisance orbits.

## 18. Sufficiency of the toy Residual

Choose decoder

\[
D(r)=r.
\]

Then

\[
D(R(s,n))
=
s
=
B(s,n).
\]

The Residual reconstructs the declared capability exactly.

It does not reconstruct \(n\).

It does not need to.

## 19. Leastness in the toy model

Let \(S\) be any sufficient descriptor.

Then by sufficiency there exists a decoder \(D_S\) such that

\[
B=D_S\circ S.
\]

But in this toy model,

\[
R=B.
\]

Therefore

\[
R
=
D_S\circ S.
\]

Hence, for unrestricted semantic post-processing,

\[
R\preceq S.
\]

So \(R=s\) is least among the declared sufficient descriptors in the semantic preorder. For an operational preorder, this argument additionally requires \(D_S\in\mathfrak M\) for every compared sufficient descriptor \(S\).

The proof is almost embarrassingly simple.

That is useful.

It shows exactly what the formal definition does before we ask it to carry frontier complexity.

## 20. Invariance without sufficiency

Now define

\[
S_0(s,n)=0.
\]

This descriptor is invariant.

Take

\[
x_1=(2,0),
\qquad
x_2=(3,0).
\]

Then

\[
S_0(x_1)
=
S_0(x_2)
=
0.
\]

But

\[
B(x_1)=2,
\]

and

\[
B(x_2)=3.
\]

No deterministic decoder from the constant descriptor can produce both capability values.

This is the simplest failure mode:

\[
\boxed{
\text{invariant}
\not\Rightarrow
\text{sufficient}.
}
\]

## 21. Sufficiency without minimality

Consider the full-state descriptor

\[
S_{\rm full}(s,n)
=
(s,n).
\]

It is sufficient for \(B=s\).

A decoder can discard \(n\).

But it stores more than the declared capability needs.

Indeed,

\[
R
=
\pi_1\circ S_{\rm full}.
\]

Full-state reconstruction is stronger than capability reconstruction.

The Residual programme explicitly does not demand the stronger object unless the capability itself requires it.

## 22. Representation change

Now change coordinates.

Let

\[
T=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Define

\[
z=Tx.
\]

If

\[
x=(s,n),
\]

then

\[
z_1=s+n,
\]

and

\[
z_2=s-n.
\]

The original signal is no longer stored in one coordinate.

But it remains reconstructable:

\[
\boxed{
s
=
\frac{z_1+z_2}{2}.
}
\]

This is the first genuinely Residual-like lesson of the toy model.

The transferable object is not a coordinate slot.

It is reconstructable structure.

## 23. Exact recoding witness

Take

\[
x=(2,5).
\]

Then

\[
z
=
T x
=
(7,-3).
\]

Reconstruct:

\[
\frac{7+(-3)}{2}=2.
\]

The exact computational witness also moves

\[
(2,5)
\]

along its nuisance orbit to

\[
(2,2),
\]

while preserving the Residual value \(2\).

![Vertical nuisance orbits in signal-nuisance space collapse to their signal coordinate, while an invertible recoding sends x=(2,5) to z=(7,-3) and the Residual is reconstructed as (z1+z2)/2=2.](../../figures/masters/ATLAS-FIG-RESIDUAL-001.png)

The surface representation changed.

The declared capability did not.

## 24. Task dependence

Now change the capability.

Suppose

\[
B'(s,n)=(s,n).
\]

Then

\[
R(s,n)=s
\]

is no longer sufficient.

The nuisance has stopped being nuisance.

This is why the Residual cannot be declared before the capability is declared.

A structure can be residual for one task and inadequate for another.

## 25. Transformation dependence

The same issue applies to \(G\).

Suppose we enlarge the admissible transformation family to permit changing \(s\).

Then \(R=s\) is no longer invariant.

If the transformation family identifies capability-distinct states, the problem itself becomes inconsistent:

no descriptor can be both invariant to that transformation and exactly sufficient for the capability.

This gives a useful compatibility condition:

> admissible transformations must preserve the declared capability if an exact invariant sufficient Residual is to exist.

## 26. Residual as equivalence class

Sometimes the natural Residual may be an equivalence class rather than a chosen coordinate.

If

\[
x\sim x'
\]

whenever every declared capability probe gives the same result, then one can consider the class

\[
[x].
\]

That quotient is canonical relative to the behavior relation.

But it can be enormous.

It may be impossible to compute.

It may still be a behavior-table object in disguise.

The research challenge is to find a smaller structural representative that supports reconstruction.

## 27. Residual as operator structure

The transferable object need not be a vector.

Suppose capability depends on a transformation rule rather than on a stored state.

Then what survives may be:

- a linear operator;
- an algebra of operators;
- a transition kernel;
- a control law;
- a program;
- a graph of conditional dependencies.

This is why the Atlas calls the target **computational structure** rather than “the minimal vector.”

## 28. Residual as program

Consider two neural systems that implement the same algorithm with different hidden bases.

A basis-independent program or operator composition may transfer more naturally than any activation vector.

This possibility connects the Residual to the Atlas shift:

\[
\text{vectors}
\to
\text{operators}.
\]

It also raises a harder question:

> What is the right language in which minimality should be measured?

Description length depends on representation language.

There is no free universal metric.

## 29. Exact versus approximate Residuals

Frontier systems rarely invite exact equivalence.

A practical Residual may need an error tolerance.

One can imagine requiring

\[
d_{\mathcal Y}
\big(
B(x,q),
D(R(x),q)
\big)
\le
\varepsilon
\]

for all probes in a declared test family, or in expectation under a declared distribution.

Then minimality becomes approximate.

Tradeoffs appear among:

- descriptor size;
- reconstruction error;
- computation cost;
- robustness;
- transfer range.

The exact theory in this chapter is the zero-error baseline.

The approximate theory is a later research problem.

## 30. Reconstruction is stronger than correlation

Suppose a candidate feature correlates strongly with capability.

That is useful evidence.

It is not yet a Residual.

The candidate must support reconstruction under the declared changes of representation.

A feature that predicts capability in one model but disappears under a basis change fails transferability.

A feature that survives transformations but loses task-critical distinctions fails sufficiency.

The Residual standard is deliberately stricter.

## 31. Intervention strengthens the test

A compelling Residual candidate should survive more than passive measurement.

Where possible:

1. isolate the candidate structure;
2. alter non-Residual structure;
3. reconstruct or transplant the candidate;
4. test whether capability returns or remains;
5. repeat across admissible representations.

This turns the question from:

> Can we read the capability from this feature?

into:

> Is this structure enough to rebuild the capability under the transformations we claim should not matter?

That is closer to the intended programme.

## 32. Finite replay can fool us

Suppose a descriptor reproduces outputs on a finite benchmark.

That does not prove it reconstructs the capability.

It may simply encode the benchmark.

The declared probe family \(\mathcal Q\) therefore matters.

A serious reconstruction test must include enough variation to distinguish:

- memorized outputs;
- interpolated behavior;
- genuine transferable mechanism.

The Replayable Evidence chapter tells us how to preserve the test.

It does not tell us that the test family was sufficient.

## 33. Minimal curriculum

The Residual idea connects directly to the minimal-curriculum programme.

If later capability can be efficiently reconstructed from a small early-learned computational basis, then that basis is a candidate Residual across training trajectories.

The question becomes:

> Which early structures survive retraining, recoding, or architectural change while remaining sufficient to rebuild later capability?

That is a reconstruction problem.

## 34. Minimal reasoning basis

The same pattern appears in mathematical reasoning.

Perhaps many surface reasoning traces can be generated from a smaller set of transferable operations.

Then the target is not a canonical chain of thought.

It is a basis of operations sufficient to reconstruct broad reasoning capability.

Again:

- invariance to surface trace;
- sufficiency for capability;
- leastness within an admissible operation language.

The Residual formalism gives the question a shape.

It does not answer it.

## 35. Model interoperability

Suppose two models use incompatible hidden coordinates.

Directly exchanging activations may fail.

A transferable Residual could act as a lingua franca if both systems can:

- compile their internal state into the Residual;
- reconstruct the required capability from it.

This is one possible route to model interoperability that does not require one universal latent coordinate system.

## 36. Memory

The Residual also changes how we think about memory.

A memory store need not preserve every internal activation that produced a result.

It may preserve only the structure required to reconstruct the capability later.

This suggests a compression principle:

> store what future reconstruction needs, not necessarily the historical representation that happened to carry it.

Whether such a sufficient Residual can be identified is the hard part.

## 37. Benign nonconvexity

The Quotient chapter asked which nonconvexity disappears after symmetry reduction.

The Residual asks an adjacent question:

> Which computational distinctions survive after all representation-specific redundancy is removed?

If a capability can be reconstructed from a small quotient-stable object, then large regions of parameter variation may be irrelevant to that capability.

This could help separate:

- representational complexity;
- intrinsic computational complexity.

That remains a research programme.

## 38. Governed adaptation

A self-changing system needs to know what it must preserve.

The Residual offers one possible object for that preservation contract.

If a system can modify:

- architecture;
- parameterization;
- memory layout;
- routing;
- tool topology;

while retaining a certified Residual sufficient for declared capabilities, then adaptation may become safer to reason about.

This is an aspiration.

No such universal certificate is established here.

## 39. What would falsify a proposed Residual?

A candidate fails if any of the following occurs.

### Invariance failure

An admissible representation change alters the descriptor.

### Sufficiency failure

The declared capability cannot be reconstructed.

### Leastness failure

A strictly coarser admissible invariant descriptor remains sufficient.

### Transfer failure

The descriptor works only in one coordinate system or architecture despite the claimed transfer range.

### Intervention failure

Capability disappears when supposedly nonessential structure changes.

### Probe failure

The descriptor passes a narrow benchmark but fails on the declared capability family.

These are operational failure modes.

They make the programme falsifiable.

## 40. What the Residual is not

The Residual is not automatically:

- a hidden neuron;
- a feature direction;
- a latent vector;
- a quotient coordinate;
- a sufficient statistic in the classical sense;
- an information-bottleneck optimum;
- a compressed checkpoint;
- a behavior table;
- a universal invariant of intelligence.

Any of these could instantiate the role in a particular setting.

None is the definition.

## 41. Atlas connections

**Representation.**  
The Residual is defined only after representation equivalence and task-relative structure are explicit.

**Quotient geometry.**  
Symmetry reduction removes representational redundancy but does not by itself identify sufficient reconstructive structure.

**Information.**  
Sufficiency and bottleneck ideas provide formal analogies and possible special cases.

**Memory.**  
A Residual could be what a system stores when historical coordinates are disposable.

**Interoperability.**  
A shared Residual could support translation without a shared latent basis.

**Minimal curriculum / reasoning basis.**  
The target becomes a minimal transferable basis from which capability can be reconstructed.

**Governed adaptation.**  
The Residual may eventually become a preservation contract across self-modification.

## 42. Closing view

The Residual programme begins with a refusal.

We refuse to identify capability with the coordinates that happen to implement it today.

We also refuse the opposite mistake: calling anything invariant “the essence.”

The target has to survive.

It has to reconstruct.

And, within a declared admissible language, it has to be no richer than necessary.

In the toy model, the answer is trivial:

\[
R(s,n)=s.
\]

In frontier systems, we do not know the answer.

That ignorance is the point of naming the problem.

The Residual is not yet a discovered object.

It is a reconstruction test for finding what, after all admissible transformations have done their work, still has to remain.

## References used in this chapter

- [@LehmannCasella1998]
- [@AchilleSoatto2018]
- [@TishbyPereiraBialek2000]

See \`sources/source-locks/ATLAS-CH-RESIDUAL-001.yaml\` for exact source roles, audited Atlas dependencies, and claim boundaries.
