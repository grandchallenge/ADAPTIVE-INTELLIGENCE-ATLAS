# Chapter Specification — ATLAS-CH-ARCHHIST-001

## Identity

**Title:** From Layered Networks to Residual Systems  
**Part:** Neural Architectures  
**Status:** specification-ready.  
**Epistemic class:** Primary Architecture History + Established Structural Mathematics + Atlas Synthesis.

## Chapter contract

Use a selective architectural lineage to show how the useful mathematical object of analysis changes.

The chapter is not a chronology of model names.

Each admitted milestone must introduce a structural idea required later in the Atlas:

1. **multilayer networks**:
   composition of learned maps;
2. **convolutional networks**:
   structured local operators and weight sharing tied to translation symmetry;
3. **recurrent/LSTM systems**:
   persistent state and parameter sharing across computational time;
4. **encoder–decoder systems**:
   an explicit representation interface between two computations;
5. **highway systems**:
   learned transform/carry gating across depth;
6. **residual systems**:
   identity transport plus learned increment;
7. **continuous-depth formulations**:
   an explicit later model class in which the evolution law itself is parameterized continuously.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-DYN-001\`.

May assume:

- state, operator, flow, and interface distinctions;
- finite-dimensional linear algebra;
- local Jacobians;
- discrete state evolution.

Must not assume:

- Transformers;
- attention;
- adaptive depth;
- operator splitting;
- network-numerics theory.

Those are downstream.

## Reader outcome

A reader should be able to:

1. write a feed-forward network as a composition of maps;
2. explain why a convolution layer is more structured than an arbitrary dense linear map;
3. prove translation equivariance for the declared circular-convolution model;
4. write an RNN as a state-transition system;
5. unroll an exact linear recurrence;
6. interpret an encoder output as an interface state rather than merely “a vector”;
7. state the information-loss boundary of a noninjective encoder;
8. write a residual block as identity plus learned increment;
9. derive its Jacobian \(I+J_F\);
10. explain what the identity path does and does not prove;
11. distinguish a residual-network dynamical lens from a literal autonomous ODE identity;
12. identify Neural ODEs as an explicit continuous-depth architecture rather than a retrospective theorem about all networks.

## Formal spine

### Layered composition

\[
x_{k+1}=F_k(x_k),
\]

so

\[
x_L
=
F_{L-1}\circ\cdots\circ F_0(x_0).
\]

For differentiable layers,

\[
J_{\rm total}
=
J_{F_{L-1}}
\cdots
J_{F_0}.
\]

### Convolution and translation equivariance

For a periodic discrete signal,

\[
(C_kx)_j
=
\sum_r k_r x_{j-r}.
\]

Let shift \(S_m\) act by

\[
(S_mx)_j=x_{j-m}.
\]

Derive

\[
\boxed{
C_k S_m
=
S_m C_k.
}
\]

This exact statement is for the declared periodic convolution model.

Do not claim arbitrary CNN pipelines remain exactly translation equivariant after boundary handling, striding, pooling, nonlinear preprocessing, or other operations unless those operations are separately checked.

### Recurrent state

\[
h_{t+1}
=
F(h_t,x_t;\theta).
\]

The same \(\theta\) can be reused across time.

For the scalar linear recurrence

\[
h_{t+1}
=
a h_t+b x_t,
\]

derive

\[
h_T
=
a^T h_0
+
b
\sum_{j=0}^{T-1}
a^{T-1-j}x_j.
\]

This exposes both persistent state and temporal credit paths.

### Encoder–decoder interface

\[
z=E(x),
\qquad
\hat y=D(z).
\]

If

\[
E(x_1)=E(x_2)
\]

but the required targets satisfy

\[
y_1\ne y_2,
\]

then no deterministic decoder using only \(z\) can reconstruct both correctly.

This is an interface/bottleneck statement, not a criticism of encoder–decoder architectures.

### Highway update

For coordinatewise transform gate (T_k(x)) and carry gate (C_k(x)), write the structural form

[
x_{k+1}
=
T_k(x_k)odot H_k(x_k)
+
C_k(x_k)odot x_k.
]

For the tied-gate setting used in the chapter, take (0le T_k(x)le1) coordinatewise and (C_k(x)=1-T_k(x)), so the carry path becomes exact identity when transformation is fully suppressed.

Use this only to expose learned carry/transform routing across depth.

Do not claim the gating mechanism is equivalent to a ResNet block.

### Residual update

\[
x_{k+1}
=
x_k+F_k(x_k).
\]

For differentiable \(F_k\),

\[
\boxed{
J_k
=
I+J_{F_k}(x_k).
}
\]

Across \(L\) blocks,

\[
J_{\rm total}
=
\prod_{k=L-1}^{0}
\left(
I+J_{F_k}(x_k)
\right)
\]

with order matching composition.

If the residual branch is zero,

\[
F_k=0,
\]

the block is exactly the identity.

This is the exact identity-transport claim.

Do not promote it into a theorem that arbitrarily deep residual networks are easy to optimize.

### Continuous-depth handoff

A Neural ODE model specifies a state evolution such as

\[
\frac{dz}{dt}
=
f(z,t;\theta)
\]

and obtains outputs through an ODE solver.

Use this as an explicit architecture family that makes the dynamical interpretation literal by construction.

Do not infer from it that ordinary residual networks are exact solutions of a single continuous ODE.

## Principal pedagogical device

### Allegory: from assembly line to evolving state

- MLP:
  an item moves through a sequence of stations;
- CNN:
  the same local tool is reused across spatial locations;
- RNN:
  the item carries a persistent notebook from one time step to the next;
- encoder–decoder:
  two subsystems communicate through a bounded interface;
- residual block:
  the current state is carried forward while a correction is added.

Limit:

Neural architectures are not factories. Weight sharing, state evolution, and identity transport are mathematical structures, not physical machinery. The allegory is only a memory aid for how the computational contract changes.

## Exact computational witness

Use three exact checks.

### W1. Circular convolution equivariance

Take

\[
x=(1,2,3,4),
\qquad
k=(1,2,0,0),
\]

with circular convolution and one-site cyclic shift.

Verify exactly:

\[
C_k S_1 x
=
S_1 C_k x.
\]

### W2. Linear recurrence

Use

\[
a=\frac12,
\qquad
b=2,
\qquad
h_0=1,
\qquad
(x_0,x_1,x_2)=(3,-1,4).
\]

Verify direct recurrence and the closed form agree at \(T=3\).

### W3. Residual identity path

For scalar branch

\[
F(x)=\alpha x,
\]

the plain branch derivative is

\[
\alpha,
\]

while the residual block derivative is

\[
1+\alpha.
\]

At

\[
\alpha=0,
\]

the residual block remains exact identity.

Use a small matrix branch \(F(x)=Ax\) to verify:

\[
J_{\rm residual}=I+A.
\]

## Figure programme

### ATLAS-FIG-ARCHHIST-001

One schematic Atlas plate with six structural panels:

1. composition;
2. spatially shared convolution;
3. recurrent state loop;
4. encoder–decoder interface;
5. highway transform/carry gating;
6. residual identity bypass.

Representation class:
schematic.

Literal labels/equations are exact.

Relative spacing, arrow lengths, and visual chronology are nonliteral.

## Counterexamples and failure boundaries

Include:

- convolutional translation equivariance can be broken by boundary rules or subsampling;
- recurrent parameter sharing does not guarantee long-memory retention;
- a bottleneck can discard target-relevant information;
- highway gating can preserve a carry path without guaranteeing optimization success;
- residual identity transport does not imply every Jacobian product is well-conditioned;
- an RNN is discrete state evolution, not automatically a continuous flow;
- a residual block admits an integrator lens without proving one autonomous underlying ODE;
- architectural chronology is not an accuracy/performance ranking.

## Downstream obligations

Direct consumers:

- \`ATLAS-CH-TRANSFORMER-001\`;
- \`ATLAS-CH-DEPTH-001\`;
- \`ATLAS-CH-NETNUM-001\`.

Important later consumers include:

- split-operator architectures;
- MoE;
- mechanistic diagnostics;
- adaptive depth;
- transport;
- composition.

## Sources

- [@RumelhartHintonWilliams1986]
- [@LeCunBottouBengioHaffner1998]
- [@HochreiterSchmidhuber1997]
- [@SutskeverVinyalsLe2014]
- [@SrivastavaGreffSchmidhuber2015]
- [@HeZhangRenSun2016]
- [@ChenRubanovaBettencourtDuvenaud2018]

Source lock:
\`sources/source-locks/ATLAS-CH-ARCHHIST-001.yaml\`.

## Acceptance

The draft must:

- use architecture history to expose structural changes, not merely dates;
- prove the declared convolution equivariance exactly;
- derive the linear recurrence unrolling;
- state the encoder information-loss boundary;
- derive \(I+J_F\) for residual blocks;
- preserve the residual-network-versus-ODE boundary;
- avoid unsupported priority or universal-superiority claims;
- include one useful allegory with its limit;
- include source lock, witness, and figure provenance.
