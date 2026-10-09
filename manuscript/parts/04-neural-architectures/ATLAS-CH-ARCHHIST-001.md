# From Layered Networks to Residual Systems
<!-- ATLAS-CH-ARCHHIST-001 -->

**Epistemic status:** Primary Architecture History + Established Structural Mathematics + Atlas Synthesis  
**Specification:** manuscript/specifications/ATLAS-CH-ARCHHIST-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-ARCHHIST-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-ARCHHIST-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-ARCHHIST-001.yaml

## 1. Architecture is a choice of mathematical object

A neural architecture is not merely a list of layers.

It declares:

- what counts as state;
- which transformations are shared;
- what information persists;
- where bottlenecks live;
- how depth transports information;
- which symmetries are built in.

The useful historical question is therefore not:

> Which architecture came next?

It is:

> What new mathematical object became worth analyzing?

This chapter compares a selective sequence of mathematical viewpoints: **composition and structured operators**, then **persistent state and interfaces**, followed by **gated carry, residual transport, and explicit continuous depth**. The ordering is pedagogical; it is not a claim that the actual history of neural networks was linear.

## 2. From assembly line to evolving state

A useful allegory is an assembly line.

A feed-forward network moves an object through a sequence of stations.

A convolutional network reuses the same local tool at many spatial locations.

A recurrent network gives the object a notebook that persists through computational time.

An encoder–decoder system forces two subsystems to communicate through an interface.

A highway layer adds learned gates deciding how much to transform and how much to carry.

A residual block carries the current state forward and adds a correction.

A continuous-depth model replaces the discrete sequence with an explicitly parameterized evolution law.

The limit of the allegory is important.

Neural networks are not factories.

The value of the metaphor is only that it makes the change in mathematical object visible.

## 3. Layered composition

A feed-forward network can be written as

\[
x_{k+1}
=
F_k(x_k).
\]

After \(L\) layers,

\[
\boxed{
x_L
=
F_{L-1}\circ\cdots\circ F_0(x_0).
}
\]

The basic object is therefore a composition of learned maps.

This viewpoint is already enough to introduce:

- hidden representations;
- depth;
- nonlinear composition;
- back-propagated derivatives.

Rumelhart, Hinton, and Williams gave one influential formulation of efficient error back-propagation through multilayer networks [@RumelhartHintonWilliams1986].

The historical claim here is deliberately narrow.

The chapter does not assign unique invention of multilayer learning to one paper.

## 4. Composition creates a product of Jacobians

If each \(F_k\) is differentiable, the chain rule gives

\[
J_{\rm total}
=
J_{F_{L-1}}(x_{L-1})
\cdots
J_{F_0}(x_0).
\]

This simple product has enormous consequences.

Signals and gradients can be:

- amplified;
- attenuated;
- rotated;
- collapsed;
- made ill-conditioned.

The architecture therefore determines not only which functions can be represented.

It also shapes how derivatives are transported through depth.

## 5. The early object: a hierarchy of representations

In a layered network, each hidden state

\[
x_k
\]

is both:

- the output of earlier computation;
- the input to later computation.

This creates a hierarchy of internal representations.

The Representation chapter taught us not to assume that a hidden coordinate is intrinsically meaningful.

Architecture adds a further question:

> Which transformations are imposed before that representation even has a chance to form?

Convolution provides the first major structural answer in this lineage.

## 6. Convolution replaces arbitrary connectivity with a structured operator

A dense linear map can connect every input coordinate to every output coordinate.

A convolutional map ties weights across locations.

For a periodic one-dimensional signal, define

\[
(C_kx)_j
=
\sum_r k_r x_{j-r}.
\]

The same kernel coefficients

\[
k_r
\]

are reused across positions.

LeCun and colleagues used local receptive fields and weight sharing in a highly influential convolutional architecture for document recognition [@LeCunBottouBengioHaffner1998].

The structural lesson is broader than the application:

> architecture can encode a symmetry assumption through operator structure.

## 7. Exact translation equivariance in the declared model

Let cyclic shift \(S_m\) act by

\[
(S_mx)_j
=
x_{j-m}.
\]

Then

\[
\begin{aligned}
(C_kS_mx)_j
&=
\sum_r k_r(S_mx)_{j-r}\\
&=
\sum_r k_r x_{j-r-m}\\
&=
(S_mC_kx)_j.
\end{aligned}
\]

Therefore

\[
\boxed{
C_kS_m
=
S_mC_k.
}
\]

This is exact translation equivariance for the declared circular-convolution model.

The architecture is not learning this symmetry from scratch.

The operator class already contains it.

## 8. Exact convolution witness

Use

\[
S=
\begin{pmatrix}
0&0&0&1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix},
\]

and

\[
C=I+2S.
\]

Because \(C\) is a polynomial in \(S\),

\[
CS=SC.
\]

For

\[
x=(1,2,3,4),
\]

the exact computational witness gives

\[
CSx
=
SCx
=
(10,9,4,7).
\]

The symmetry is algebraic in this toy model.

It is not an empirical approximation.

## 9. Practical CNNs can break exact equivariance

The exact proof above is intentionally narrow.

Real pipelines may include:

- zero padding;
- asymmetric boundaries;
- striding;
- pooling;
- resizing;
- nonlinear preprocessing;
- position-dependent operations.

Any of these can alter exact equivariance.

So the safe statement is:

> convolution supplies a translation-structured operator, while full-pipeline equivariance must be checked operation by operation.

This distinction matters later when positional information is added deliberately.

## 10. Recurrent systems change the object again

A feed-forward layer consumes a state and passes a new state onward.

A recurrent system makes state persistence explicit:

\[
\boxed{
h_{t+1}
=
F(h_t,x_t;\theta).
}
\]

The same parameter set \(\theta\) can be reused across computational time.

Now the central object is no longer only a composition of distinct maps.

It is a state-transition system.

## 11. Parameter sharing across time

Unrolling a recurrent network produces a deep computation.

But the same transition law can reappear at every time step.

This creates a different kind of depth:

\[
\text{depth by repeated state evolution}.
\]

The distinction becomes important later for:

- recurrent depth;
- weight tying;
- latent clocks;
- iterative reasoning.

A recurrent architecture is naturally read as a discrete dynamical system.

It is not automatically a continuous flow.

## 12. Exact linear recurrence

Consider

\[
h_{t+1}
=
a h_t+b x_t.
\]

Repeated substitution gives

\[
\boxed{
h_T
=
a^T h_0
+
b
\sum_{j=0}^{T-1}
a^{T-1-j}x_j.
}
\]

Earlier inputs are transported by powers of \(a\).

The recurrence therefore exposes a memory law directly.

If

\[
|a|<1,
\]

old contributions decay geometrically in this scalar model.

If

\[
|a|>1,
\]

they can grow.

The architecture creates a temporal transport problem.

## 13. Exact recurrence witness

Take

\[
a=\frac12,
\qquad
b=2,
\qquad
h_0=1,
\]

and

\[
(x_0,x_1,x_2)
=
(3,-1,4).
\]

The direct recurrence gives

\[
(h_0,h_1,h_2,h_3)
=
\left(
1,
\frac{13}{2},
\frac54,
\frac{69}{8}
\right).
\]

The closed form independently gives

\[
h_3
=
\frac{69}{8}.
\]

This is the simplest exact demonstration that recurrent state carries weighted history.

## 14. Long-term memory is not guaranteed by recurrence

A recurrent loop can preserve state in principle.

That does not mean it preserves useful information over long intervals.

Problems can arise from:

- repeated Jacobian products;
- contraction;
- expansion;
- saturation;
- interference;
- optimization difficulty.

This is one reason gated recurrent systems were developed.

## 15. LSTM: persistent state plus gates

The Long Short-Term Memory architecture uses gated recurrent machinery designed to address long-lag learning difficulties [@HochreiterSchmidhuber1997].

The structural shift is important:

> persistence becomes an explicit controlled pathway.

The state is no longer merely whatever survives repeated application of one transition.

Gates regulate:

- what enters;
- what remains;
- what becomes externally visible.

This is an architectural move toward managed state transport.

## 16. Gates are operators on information flow

A gate can be read as a data-dependent multiplicative operator.

Schematically,

\[
g_t\odot v_t.
\]

The gate value decides how strongly a quantity is passed.

This is distinct from a plain additive update.

The later Highway Networks construction will reuse the same broad design idea across depth rather than only across recurrent time.

## 17. Encoder–decoder architecture introduces an explicit interface

Now separate computation into two subsystems:

\[
z=E(x),
\]

\[
\hat y=D(z).
\]

The encoder produces an interface object \(z\).

The decoder is constrained to work from that object.

Sequence-to-sequence systems made this separation especially visible for variable-length input/output mappings [@SutskeverVinyalsLe2014].

The important Atlas object is the interface itself.

## 18. The interface is a contract

Once the decoder receives only \(z\), every downstream capability must be recoverable from \(z\).

This makes encoder–decoder architecture a concrete instance of a broader principle:

> an interface is sufficient only for the distinctions downstream computation still needs.

The Representation, Residual, and Transfer chapters formalized this idea more generally.

Here it appears as architecture.

## 19. Encoder information-loss boundary

Suppose

\[
E(x_1)
=
E(x_2)
=
z,
\]

but the required outputs satisfy

\[
y_1\ne y_2.
\]

A deterministic decoder receives the same \(z\) in both cases.

Therefore

\[
D(E(x_1))
=
D(E(x_2)).
\]

It cannot equal both distinct targets.

So a noninjective encoder may discard information safely only relative to the downstream capability being preserved.

This is not an argument that useful encoders must be injective.

Compression is often the point.

## 20. Bottleneck is a design decision

The interface can be:

- a fixed-dimensional vector;
- a sequence;
- a memory;
- a graph;
- an operator state;
- a set of retrieved evidence.

What matters is what distinctions it preserves.

Later attention architectures loosen the fixed-vector bottleneck dramatically.

But the encoder–decoder lesson remains:

> communication between subsystems creates an explicit sufficiency boundary.

## 21. Highway Networks: transform or carry

Highway Networks use learned transform and carry gates across depth [@SrivastavaGreffSchmidhuber2015].

A structural form is

\[
\boxed{
y
=
T(x)\odot H(x)
+
C(x)\odot x.
}
\]

A common tied-gate choice is

\[
C(x)=1-T(x).
\]

Then

\[
y
=
T(x)\odot H(x)
+
(1-T(x))\odot x.
\]

The layer can learn how much to transform and how much to carry.

## 22. Highway identity limit

In the tied-gate form, if

\[
T(x)=0,
\]

then

\[
C(x)=1,
\]

so

\[
\boxed{
y=x.
}
\]

The architecture therefore contains an exact carry path.

At the opposite limit,

\[
T(x)=1,
\]

we obtain

\[
y=H(x).
\]

With the tied gate constrained coordinatewise to ([0,1]), the layer interpolates coordinatewise between carried and transformed state.

## 23. Exact highway witness

Take

\[
x=2,
\qquad
H(x)=5,
\]

and

\[
T=\frac14,
\qquad
C=\frac34.
\]

Then

\[
y
=
\frac14\cdot5
+
\frac34\cdot2
=
\frac{11}{4}.
\]

The exact carry limit returns

\[
2.
\]

The exact transform limit returns

\[
5.
\]

This small witness shows the gate algebra without making any claim about training dynamics.

## 24. Gated carry is not residual addition

Highway and residual systems both create a direct path for state transport.

But they do so differently.

A highway layer uses multiplicative gates:

\[
T\odot H
+
C\odot x.
\]

A canonical residual block uses additive identity transport:

\[
x+F(x).
\]

These are related design ideas.

They are not the same algebra.

The distinction matters when analyzing Jacobians and optimization.

## 25. Residual learning

Residual networks made the identity-plus-increment form central:

\[
\boxed{
x_{k+1}
=
x_k
+
F_k(x_k).
}
\]

He and colleagues used residual learning to train very deep image-recognition systems and reported substantial empirical gains in that setting [@HeZhangRenSun2016].

The Atlas uses the architecture for a narrower structural reason:

> depth now looks like repeated state transport plus correction.

## 26. Residual Jacobian

Differentiate:

\[
x_{k+1}
=
x_k
+
F_k(x_k).
\]

Then

\[
\boxed{
J_k
=
I
+
J_{F_k}(x_k).
}
\]

Across \(L\) residual blocks,

\[
J_{\rm total}
=
\left(I+J_{F_{L-1}}\right)
\cdots
\left(I+J_{F_0}\right).
\]

The identity contribution is exact.

The product can still be badly conditioned.

## 27. Identity transport

If the residual branch vanishes,

\[
F_k(x)=0,
\]

then

\[
x_{k+1}=x_k.
\]

The block becomes exactly the identity map.

That is the precise identity-transport claim.

It does not prove:

- all residual networks optimize easily;
- all gradients remain well conditioned;
- arbitrary depth is harmless.

The architecture creates an identity route.

Training still determines what happens around it.

## 28. Exact residual witness

For

\[
F(x)=Ax,
\qquad
A=
\begin{pmatrix}
1&2\\
-1&3
\end{pmatrix},
\]

the residual block Jacobian is

\[
I+A
=
\begin{pmatrix}
2&2\\
-1&4
\end{pmatrix}.
\]

If

\[
A=0,
\]

the block Jacobian is exactly

\[
I.
\]

The computational witness checks both identities.

## 29. Structural lineage plate

![Six schematic panels showing layered composition, convolutional weight sharing, recurrent state, encoder-decoder interface, highway transform/carry gating, and residual identity bypass.](../../figures/masters/ATLAS-FIG-ARCHHIST-001.png)

The plate is deliberately schematic.

It does not encode:

- historical priority;
- benchmark quality;
- parameter count;
- compute;
- architectural superiority.

Its only job is to show how the mathematical object changes.

## 30. Residual systems invite a dynamical lens

Rewrite the residual update as

\[
x_{k+1}-x_k
=
F_k(x_k).
\]

If

\[
F_k(x)
=
h f_k(x),
\]

then

\[
x_{k+1}
=
x_k
+
h f_k(x_k).
\]

This resembles an explicit Euler step.

That resemblance is useful.

It is not an identity theorem.

## 31. The ODE analogy has conditions

To interpret a residual system as a discretization of one autonomous ODE,

\[
\dot x=f(x),
\]

we would need more than the residual form.

Questions include:

- Is there one shared \(f\)?
- Is there a meaningful small step \(h\)?
- Does the discrete family converge as \(h\to0\)?
- Are the layer operations compatible with a smooth vector field?
- Does the numerical method preserve the relevant structure?

Generic ResNets do not answer these automatically.

So the safe statement is:

> residual systems admit an integrator lens.

## 32. Neural ODEs make continuous depth explicit

Neural Ordinary Differential Equations specify the evolution law directly:

\[
\frac{dz}{dt}
=
f(z,t;\theta),
\]

and obtain outputs through numerical integration [@ChenRubanovaBettencourtDuvenaud2018].

Here continuous depth is part of the model definition.

The numerical solver is therefore an architectural component.

This is categorically different from retrospectively declaring every residual network to be an ODE.

## 33. Continuous depth changes where approximation lives

In a discrete network, learned layer maps are explicit model components.

In a Neural ODE, the learned object is the vector field, while finite-time transport is produced by a numerical solver.

Approximation therefore enters in two places:

- function approximation in \(f\);
- numerical approximation of the flow.

This creates the bridge to the Numerical Intelligence chapter.

## 34. Architecture as transport

The lineage can now be restated.

A layered network says:

\[
\text{apply another map}.
\]

A recurrent system says:

\[
\text{update persistent state}.
\]

A highway system says:

\[
\text{learn how much state to carry}.
\]

A residual system says:

\[
\text{carry state and add an increment}.
\]

A continuous-depth system says:

\[
\text{specify a law of motion and integrate it}.
\]

The object has shifted from static composition toward transport.

## 35. Architecture can encode invariance

Convolution encodes translation structure.

Recurrence encodes temporal parameter sharing.

Encoder–decoder systems encode a communication bottleneck.

Highway layers encode gated carry.

Residual blocks encode identity transport.

These are architectural priors.

They reduce the set of possible computations before training begins.

Architecture is therefore a form of inductive bias expressed through operators and state organization.

## 36. Architecture also creates failure modes

Every structural prior excludes something.

Convolution can mishandle boundaries or nonstationary spatial structure.

Recurrence can forget.

Bottlenecks can erase task-relevant distinctions.

Gates can saturate or route poorly.

Residual products can still become ill-conditioned.

Continuous-depth models inherit numerical-solver choices.

There is no architecture without a failure surface.

## 37. History is not a ranking

The sequence in this chapter should not be read as:

\[
\text{MLP}<\text{CNN}<\text{RNN}<\text{ResNet}<\text{ODE}.
\]

Different architectures solve different structural problems.

A simple MLP may be exactly right for one task.

A recurrent state may be unnecessary.

A continuous-depth solver may add cost without benefit.

The Atlas uses history only to expose reusable mathematical ideas.

## 38. What changes in the object of analysis?

The structural transitions can be summarized as follows.

### Layered networks

Analyze:

\[
\text{composition}.
\]

### CNNs

Analyze:

\[
\text{structured shared operators}.
\]

### RNNs and LSTMs

Analyze:

\[
\text{persistent state evolution}.
\]

### Encoder–decoders

Analyze:

\[
\text{interfaces and sufficiency}.
\]

### Highway systems

Analyze:

\[
\text{gated transform/carry paths}.
\]

### Residual systems

Analyze:

\[
\text{identity transport plus increment}.
\]

### Neural ODEs

Analyze:

\[
\text{explicit continuous evolution plus numerical solution}.
\]

This is the architecture lineage the downstream Atlas needs.

## 39. Bridge to Transformers

Transformers will introduce another decisive shift.

Instead of propagating only through fixed local connectivity or recurrent state, a token representation can dynamically aggregate information from other positions through attention.

The next architecture chapter will therefore add:

\[
\text{content-dependent global interaction}.
\]

But it inherits everything here:

- composition;
- state;
- interfaces;
- residual paths;
- normalization;
- depth.

Transformers are not outside this lineage.

They reorganize it.

## 40. Bridge to adaptive depth

Once depth is read as accumulated state transformation, a new question becomes natural:

> Why must every input receive the same number of updates?

Adaptive-depth systems make computational horizon input-dependent.

That chapter depends on the distinction established here between:

- layer count;
- state evolution;
- computational time.

## 41. Bridge to network numerics

Residual and continuous-depth systems invite numerical questions:

- What is the effective step size?
- Is the update stable?
- Which invariants drift?
- How does splitting affect the trajectory?
- Can a better integrator improve computation?

Those are not metaphorical questions once the architecture is explicitly organized as state evolution.

The Network Numerics chapter will take them literally.

## 42. What would falsify an architectural analogy?

A structural analogy should make testable predictions.

If we claim convolutional equivariance, test the commutator with translation.

If we claim recurrence stores long-term information, perturb old inputs and measure influence.

If we claim a bottleneck is sufficient, search for target-distinct states it merges.

If we claim residual transport improves conditioning, inspect the Jacobian product rather than the identity term alone.

If we claim a network approximates a continuous flow, test refinement and solver dependence.

Architecture should constrain observation.

## 43. Closing view

The important history is not a procession of brand names.

It is a progression in what computation is allowed to remember, share, preserve, and transport.

We began with

\[
x_{k+1}=F_k(x_k).
\]

Then architecture learned to express:

- spatial symmetry;
- temporal persistence;
- bounded interfaces;
- gated carrying;
- identity transport;
- explicit continuous evolution.

The Atlas thesis becomes clearer here.

A modern neural model is not merely a large static function.

It is increasingly useful to treat it as an organized computational system whose state is transformed under architectural rules.

The next chapters will keep asking what those rules buy us, what they destroy, and which mathematical tools can certify the difference.

## References used in this chapter

- [@RumelhartHintonWilliams1986]
- [@LeCunBottouBengioHaffner1998]
- [@HochreiterSchmidhuber1997]
- [@SutskeverVinyalsLe2014]
- [@SrivastavaGreffSchmidhuber2015]
- [@HeZhangRenSun2016]
- [@ChenRubanovaBettencourtDuvenaud2018]

See \`sources/source-locks/ATLAS-CH-ARCHHIST-001.yaml\` for exact source roles, internal Atlas pins, and claim boundaries.
