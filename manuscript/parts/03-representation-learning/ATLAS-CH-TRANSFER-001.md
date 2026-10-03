# Reconstruction and Transfer
<!-- ATLAS-CH-TRANSFER-001 -->

**Epistemic status:** Established Transfer Framework + Atlas Synthesis + Exact Toy Witness  
**Specification:** manuscript/specifications/ATLAS-CH-TRANSFER-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-TRANSFER-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-TRANSFER-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-TRANSFER-001.yaml

## 1. Transfer is not reuse

A model begins on one task.

Some of what it learned is reused somewhere else.

That story is often called transfer learning.

But several different phenomena can hide inside the word **transfer**:

- reusing parameters as initialization;
- freezing a feature extractor;
- fine-tuning a whole model;
- adapting to a new domain;
- adapting to a new task;
- reusing architecture but not weights;
- compiling one representation into another;
- reconstructing a capability through a shared latent object.

These are not the same operation.

The Atlas therefore asks a narrower question before discussing methods:

> What structure must remain recoverable for a declared target capability to survive a change of representation, task, or domain?

This chapter connects that question to the Residual.

## 2. Moving a machine through a narrow doorway

A useful allegory is shipping a machine through a doorway.

One option is to push the whole assembled machine through.

Another is to:

1. disassemble it;
2. keep a portable core;
3. carry that core across;
4. rebuild what is needed on the other side.

The structural correspondence is:

- source representation ↔ original assembly;
- compiler ↔ disassembly map;
- Residual ↔ portable core;
- target decoder ↔ reconstruction procedure;
- bottleneck ↔ doorway width.

The limit matters.

Real transfer learning also involves:

- finite data;
- optimization;
- distribution shift;
- task mismatch;
- decoder restrictions;
- stochastic training.

Exact deterministic reconstruction is only one clean special case.

## 3. Standard source and target framing

A common transfer-learning formulation distinguishes a **domain** from a **task** [@PanYang2010].

A domain can be written as

\[
\mathcal D
=
(\mathcal X,P(X)),
\]

where \(\mathcal X\) is an input space and \(P(X)\) a distribution.

A task can be written as

\[
\mathcal T
=
(\mathcal Y,f),
\]

where \(\mathcal Y\) is an output space and \(f\) a predictive object.

A transfer setting then relates:

\[
(\mathcal D_s,\mathcal T_s)
\]

to

\[
(\mathcal D_t,\mathcal T_t).
\]

The source and target may differ in:

- input distribution;
- feature space;
- output space;
- predictive task;
- available labels;
- data volume.

The important point is relational:

transfer is always transfer **from something to something**.

## 4. Transfer needs a target criterion

Suppose we reuse a source model on a target task.

Did transfer succeed?

That question is meaningless without a target criterion.

We need at least:

- a target metric;
- a target data budget;
- an adaptation procedure;
- a baseline.

For a higher-is-better score \(J\), transfer improves the target when

\[
J(M_{\rm transfer})
>
J(M_{\rm target-only}),
\]

under a matched comparison.

If

\[
J(M_{\rm transfer})
<
J(M_{\rm target-only}),
\]

the result is negative transfer.

The sign depends on the metric convention.

The concept depends on the baseline.

## 5. Negative transfer is not paradoxical

Why can previously learned structure hurt?

Because reusable structure can be mismatched.

Possible causes include:

- source-specific features;
- wrong invariances;
- optimization bias;
- insufficient adaptation;
- domain shift;
- label mismatch;
- representational bottlenecks;
- co-adaptation among features.

Pan and Yang discuss negative transfer as a central issue in transfer learning [@PanYang2010].

The Atlas will use the term operationally, not metaphysically.

A source model does not carry a universal transferable essence merely because it learned something useful once.

## 6. Source accuracy is not transferability

A source model can perform extremely well on its original task while encoding features that transfer poorly.

Yosinski and colleagues experimentally studied how feature transferability changes across network depth and task distance [@YosinskiEtAl2014].

Their results show at least two distinct limitations:

- higher-layer specialization can reduce transferability;
- splitting co-adapted representations can create optimization difficulties.

Kornblith, Shlens, and Le later showed that source benchmark quality and transferable-feature quality are not interchangeable, and that training choices can substantially affect transfer behavior [@KornblithShlensLe2019].

The bounded conclusion is:

\[
\boxed{
\text{source performance}
\not\Rightarrow
\text{universal transfer quality}.
}
\]

## 7. Parameter reuse is weaker than capability transfer

Suppose we copy source weights into a target model.

That establishes one fact:

the target optimization began from source parameters.

It does not establish:

- which source capabilities survived;
- which features were reused;
- whether the target behavior improved;
- whether the target could have learned the same behavior from scratch;
- whether the transferred parameters were actually necessary.

Parameter reuse is a mechanism.

Transfer is an outcome relative to a declared target criterion.

## 8. Representation transfer

A common strategy is to reuse an intermediate representation

\[
z=E_s(x)
\]

and learn a new target readout.

This works only if the representation retains distinctions the target task needs.

A feature extractor can be highly sufficient for the source task and still erase information needed by the target.

This is the direct bridge to the Residual formalism.

The target asks:

> Is the transferred representation still sufficient for the capability I now want?

## 9. The common-Residual reconstruction certificate

Let

\[
E_s:X\to Z_s
\]

be a source representation.

Let

\[
E_t:X\to Z_t
\]

be a target representation.

Let

\[
R:X\to\mathcal R
\]

be a declared admissible Residual.

Suppose there exist compilers

\[
C_s:Z_s\to\mathcal R,
\]

and

\[
C_t:Z_t\to\mathcal R,
\]

such that

\[
\boxed{
C_s(E_s(x))
=
C_t(E_t(x))
=
R(x)
}
\]

for every declared state \(x\).

Now let the target capability family be indexed by \(q\in\mathcal Q_t\).

Suppose each target behavior factors through \(R\):

\[
\boxed{
B_t(x,q)
=
D_q(R(x)).
}
\]

Then the target capability can be reconstructed from either representation:

\[
B_t(x,q)
=
D_q(C_s(E_s(x))),
\]

and

\[
B_t(x,q)
=
D_q(C_t(E_t(x))).
\]

This is the **common-Residual reconstruction certificate**.

## 10. What the certificate says

The certificate says:

> source and target coordinates may differ, but if both compile to the same capability-sufficient structure, the declared capability survives.

This is a sufficient condition.

It is not a characterization of all transfer.

A direct adapter

\[
A:Z_s\to Z_t
\]

might exist even when we have not identified a shared Residual.

The common Residual is useful because it separates:

- representation-specific coordinates;
- transferable capability structure.

## 11. Exact linear witness

Let the transferable structure be

\[
r=
\begin{pmatrix}
a\\
b
\end{pmatrix}.
\]

The source representation is

\[
z_s
=
A_s r,
\]

with

\[
A_s
=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The target representation is

\[
z_t
=
A_t r,
\]

with

\[
A_t
=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

Both matrices are invertible.

Therefore define

\[
C_s=A_s^{-1},
\]

and

\[
C_t=A_t^{-1}.
\]

Both recover the same \(r\).

## 12. Exact numeric reconstruction

Take

\[
r=(3,1).
\]

Then

\[
z_s
=
A_s r
=
(4,2).
\]

And

\[
z_t
=
A_t r
=
(6,1/2).
\]

The exact witness verifies:

\[
C_s z_s=(3,1),
\]

and

\[
C_t z_t=(3,1).
\]

Different coordinates.

Same reconstructive core.

## 13. Two target tasks

Now define two target tasks:

\[
D_1(a,b)=a+b,
\]

and

\[
D_2(a,b)=2a-b.
\]

For

\[
r=(3,1),
\]

we obtain

\[
D_1=4,
\]

and

\[
D_2=5.
\]

Both source and target representations reconstruct both outputs exactly through the same \(r\).

![Two different representations compile to the same exact Residual r=(3,1) and reconstruct target outputs 4 and 5; a second panel shows a lossy bottleneck P(r)=1 merging two states that require different D2 outputs.](../../figures/masters/ATLAS-FIG-TRANSFER-001.png)

## 14. Exact recoding is the easy case

In the witness above, both representations are invertible transforms of the Residual.

No information is lost.

This is the easiest kind of transfer.

It isolates one concept:

\[
\text{coordinate change}
\neq
\text{capability loss}.
\]

But exact invertibility is not required in general.

A target representation can discard information as long as it preserves everything needed for the declared target task family.

That brings us to bottlenecks.

## 15. A lossy bottleneck

Define

\[
P(a,b)=a.
\]

The second coordinate is discarded.

This can still be sufficient for tasks that depend only on \(a\).

For example,

\[
D_0(a,b)=3a
\]

can be reconstructed from \(P\).

But the same bottleneck can fail for another task.

## 16. Exact bottleneck failure

Take

\[
r_A=(1,0),
\]

and

\[
r_B=(1,1).
\]

Then

\[
P(r_A)=1,
\]

and

\[
P(r_B)=1.
\]

The bottleneck makes the states identical.

Now evaluate

\[
D_2(a,b)=2a-b.
\]

We get

\[
D_2(r_A)=2,
\]

and

\[
D_2(r_B)=1.
\]

One bottleneck value would have to decode to two different outputs.

That is impossible for a deterministic decoder.

## 17. The fiber criterion

The bottleneck example is a special case of a general exact criterion.

Let

\[
Z:X\to\mathcal Z
\]

be a representation.

Let

\[
B:X\to\mathcal Y
\]

be a deterministic capability map.

A deterministic decoder

\[
D:\mathcal Z\to\mathcal Y
\]

with

\[
B=D\circ Z
\]

exists if and only if \(B\) is constant on every fiber of \(Z\).

That is:

\[
\boxed{
Z(x_1)=Z(x_2)
\Rightarrow
B(x_1)=B(x_2).
}
\]

This is the exact reconstruction test.

## 18. Why the fiber criterion is necessary

Suppose

\[
B=D\circ Z.
\]

If

\[
Z(x_1)=Z(x_2),
\]

then

\[
B(x_1)
=
D(Z(x_1))
=
D(Z(x_2))
=
B(x_2).
\]

So any representation that merges capability-distinct states cannot support exact deterministic reconstruction.

This is information loss in the most concrete possible sense.

## 19. Why the fiber criterion is sufficient

Now suppose \(B\) is constant on each realized fiber of \(Z\).

For each realized representation value \(z\), choose any state \(x\) with

\[
Z(x)=z.
\]

Define

\[
D(z)=B(x).
\]

This is well-defined because every state in the same fiber has the same \(B\)-value.

Therefore

\[
B=D\circ Z.
\]

This is a semantic existence result.

It does not guarantee that the decoder is simple or efficiently learnable.

## 20. One-task sufficiency is not task-family sufficiency

A representation may preserve exactly the information needed for one task and destroy information needed by another.

The bottleneck

\[
P(a,b)=a
\]

is sufficient for any target depending only on \(a\).

It is insufficient for

\[
D_2(a,b)=2a-b.
\]

Therefore transferability should often be indexed by a task family:

\[
\mathcal Q_t.
\]

A representation that transfers to task \(q_1\) need not transfer to \(q_2\).

There is no contradiction.

The target changed.

## 21. Universal representation quality is underspecified

People often ask whether a representation is “good.”

Good for what?

Possible criteria include:

- linear separability;
- reconstruction;
- invariance;
- robustness;
- compression;
- adaptation speed;
- transfer across tasks;
- transfer across domains.

These objectives can disagree.

The Transfer chapter therefore refuses to assign one universal scalar quality to a representation without a declared target family and adaptation setting.

## 22. Information bottleneck connection

The Information Bottleneck programme asks for compression while preserving information relevant to a declared target [@TishbyPereiraBialek2000].

That is structurally close to transfer through a bottleneck.

A representation can discard source variation while retaining target-relevant structure.

But mutual information is not the definition of transfer.

Transfer also depends on:

- decoder class;
- optimization;
- sample size;
- shift;
- task geometry;
- adaptation cost.

Information preservation is one piece.

## 23. Minimal sufficient representation connection

Achille and Soatto frame representations through task sufficiency, minimality, and nuisance invariance [@AchilleSoatto2018].

The Transfer chapter inherits a compatible lesson:

> compressing away nuisance can help only if the target does not later require what was removed.

The target task determines which variation is nuisance.

A source-task nuisance can become a target-task signal.

## 24. Transfer across domains

Suppose source and target use the same task but different input distributions:

\[
P_s(X)\neq P_t(X).
\]

A source representation can preserve all distinctions needed on the source support while behaving poorly on target regions.

The exact fiber criterion must therefore be evaluated over the declared target domain.

A certificate over the wrong support is not a reconstruction certificate.

This is one reason domain shift matters.

## 25. Transfer across tasks

Suppose source and target share the same domain but differ in target function.

A source representation can be sufficient for

\[
f_s
\]

but insufficient for

\[
f_t.
\]

This is exactly what the bottleneck witness demonstrates in miniature.

Task change can turn discarded variation into required information.

## 26. Transfer across representation systems

The Residual framing is most distinctive when the source and target do not share coordinates.

One model may encode a capability in:

- a dense hidden state;
- a sparse dictionary;
- an operator basis;
- a normalized manifold state;
- external memory.

If both can compile to the same admissible Residual, transfer does not require one universal latent basis.

This is the bridge to model interoperability.

## 27. Exact information preservation does not imply easy learning

Suppose source and target representations are related by an invertible matrix.

No information is lost.

But the adapter may still be hard to learn because of:

- poor conditioning;
- limited samples;
- nonlinear parameterization;
- restricted decoder class;
- optimization failure.

Therefore:

\[
\boxed{
\text{semantic transfer path}
\neq
\text{guaranteed learnable adapter}.
}
\]

The Atlas keeps semantic sufficiency and computational attainability separate.

## 28. Transfer can fail at the interface

Suppose a source representation contains the required information.

Suppose the target decoder class could in principle use it.

Transfer can still fail if the interface contract is wrong.

Examples include:

- unit mismatch;
- scaling mismatch;
- permutation mismatch;
- unsupported uncertainty semantics;
- precision loss;
- stale memory schema.

Transfer is therefore also a composition problem.

The Boundary Contracts chapter will later make this more explicit.

## 29. Architecture transfer versus feature transfer

Kornblith and colleagues provide a useful empirical warning [@KornblithShlensLe2019].

An architecture can transfer well even when a particular set of source-trained features is less transferable than source performance might suggest.

This separates two objects:

- reusable architecture;
- reusable representation state.

The Atlas treats them differently.

Architecture is a transformation/composition template.

Features are instantiated states.

Transfer can occur through either.

## 30. Fine-tuning changes the object

When a transferred representation is fine-tuned, it does not simply “remain transferable.”

It becomes a new target-adapted state.

The causal story now includes:

- initialization;
- optimization path;
- target data;
- regularization;
- adaptation schedule.

A post-fine-tuning representation cannot be treated as unchanged source structure.

Transfer attribution requires care.

## 31. A reconstruction certificate is not a training algorithm

The common-Residual certificate proves that exact target reconstruction is possible under declared maps.

It does not tell us how to learn:

\[
C_s,
\qquad
C_t,
\qquad
D_q.
\]

Those may be known analytically in a toy setting and unknown in practice.

A future Atlas programme can distinguish:

- **existence of transfer path**;
- **identifiability of transfer path**;
- **learnability of transfer path**;
- **efficiency of transfer path**.

These are different questions.

## 32. Reconstruction tests

A practical transfer claim can be stress-tested with reconstruction.

Given source and target representations:

1. declare the target capability family;
2. declare admissible compilers/adapters;
3. attempt to reconstruct capability from each representation;
4. search for target states collapsed by the representation;
5. compare transfer against a matched target-only baseline;
6. intervene on supposedly irrelevant source structure;
7. repeat under domain and representation changes.

Failure at different stages means different things.

## 33. What would falsify a transfer claim?

### Sufficiency failure

Two target states share the same transferred representation but require different outputs.

### Domain failure

A certificate holds on source support but not target support.

### Adapter failure

An admissible adapter class cannot recover the required object.

### Baseline failure

Transfer underperforms a matched target-only baseline.

### Robustness failure

The transferred capability disappears under allowed representation changes.

### Attribution failure

Target performance comes from relearning rather than transferred structure.

These failure modes should not be collapsed into one number.

## 34. Transferable Residual versus universal Residual

The Residual chapter was task-relative.

Transfer does not remove that relativity.

A shared Residual sufficient for one target family may fail for another.

The useful object is therefore:

\[
R_{\mathcal Q}
\]

for a declared family of capability probes \(\mathcal Q\), not an assumed universal essence of the model.

The search for broader Residuals is an empirical and mathematical programme.

It is not a free theorem.

## 35. Minimal curricula

Transfer connects directly to curriculum design.

If an early mechanism can reconstruct many later capabilities with limited adaptation, it has high transfer value.

A minimal curriculum therefore asks:

> Which learned structures create the broadest reconstructive reuse across later tasks?

This is stronger than asking which examples reduce next-step training loss fastest.

The later Minimal Curricula chapter will combine this transfer criterion with learning-progress search.

## 36. Minimal reasoning basis

A reasoning operation is transferable if it can be reused across problem families without carrying problem-specific surface structure.

The Residual/Transfer pair suggests a test:

- identify a candidate reasoning operation;
- recode the problem;
- change surface notation;
- change task family;
- test whether the operation still supports reconstruction of successful reasoning behavior.

This is how “canonical reasoning transformations” can become falsifiable rather than rhetorical.

## 37. Model interoperability

Two models need not share hidden coordinates if both can compile to a common transferable object.

This suggests an interoperability architecture:

\[
\text{Model A state}
\to
R
\to
\text{Model B capability}.
\]

The hard questions are:

- what is \(R\)?
- which tasks does it preserve?
- how costly are the compilers?
- what semantics must the interface expose?
- how do we certify reconstruction?

Transfer becomes a systems problem.

## 38. Memory and transfer

Persistent memory is another transfer surface.

A model may write an object today and another model may consume it later.

If memory stores representation-specific coordinates, the second model may not understand them.

If memory stores a transferable Residual or sufficient evidence object, reconstruction can survive model change.

This is one reason external memory should preserve semantics and provenance rather than raw activations alone.

## 39. Compression as a transfer probe

A bottleneck tests what can be discarded.

If a compressed object still transfers across many target tasks, it may have isolated reusable structure.

If transfer collapses after one additional compression step, that step removed capability-relevant information.

Compression can therefore become an empirical probe for transfer structure.

This connects directly to the later Compression as Discovery chapter.

## 40. Closing view

Transfer learning is often described as reuse.

The Atlas asks a stricter question.

What, exactly, survived?

A copied parameter is not yet evidence.

A reused architecture is not the same thing as a reused feature.

A high source score is not a transfer guarantee.

A common Residual gives one clean sufficient answer:

\[
\text{different representation}
\to
\text{same reconstructive core}
\to
\text{target capability}.
\]

And the fiber criterion gives the corresponding impossibility test:

if a representation merges states the target must distinguish, exact reconstruction is gone.

Transfer therefore sits at the intersection of:

- representation;
- information;
- reconstruction;
- optimization;
- composition.

The practical question is not whether knowledge was reused in some vague sense.

It is whether the structure that crossed the boundary was sufficient for what the target still needed to do.

## References used in this chapter

- [@PanYang2010]
- [@YosinskiEtAl2014]
- [@KornblithShlensLe2019]
- [@AchilleSoatto2018]
- [@TishbyPereiraBialek2000]

See \`sources/source-locks/ATLAS-CH-TRANSFER-001.yaml\` for exact source roles, Atlas dependencies, and claim boundaries.
