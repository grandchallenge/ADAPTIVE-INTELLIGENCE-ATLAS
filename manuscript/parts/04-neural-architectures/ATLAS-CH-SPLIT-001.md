# Split-Operator Networks

**Epistemic status:** established operator-splitting theory + Atlas architectural synthesis.

A neural block can contain the same named ingredients and still compute a different map when their order changes.

That sounds obvious when stated in ordinary language. It becomes more consequential when the block is described as if attention, an MLP, normalization, gating, transport, or another update were merely ingredients in a bag. They are not. They are transformations applied to state. A later transformation sees the state produced by the earlier one.

The mathematics of operator splitting gives us a disciplined way to talk about this fact.

It also gives us a trap.

Classical splitting theory studies compositions of flows or operators under explicit assumptions. A Transformer sublayer is not automatically one of those exact flows. If we borrow the notation without preserving the assumptions, an architectural metaphor quietly turns into a false numerical theorem.

This chapter keeps the useful part and blocks the overclaim.

The central lesson is:

> **When subcomputations do not commute, ordering is part of the architecture. Classical splitting theory can explain that structure exactly in declared reference systems, but learned neural maps inherit its convergence orders only when the required flow and regularity assumptions are actually established.**

The numerical substrate comes from the audited Numerics chapter and standard splitting references [@McLachlanQuispel2002; @HairerLubichWanner2006]. The baseline neural anatomy comes from the audited Transformer chapter and the original Transformer architecture [@VaswaniEtAl2017].

## 1. The smallest place order can matter

Suppose a state \(x\) is acted on by two transformations.

Call them \(A\) and \(B\).

There are at least three different things one might mean by "use both."

One is an additive update:

\[
x^+
=
x+F_A(x)+F_B(x).
\]

Another is sequential composition:

\[
x_1=\Psi_A(x),
\qquad
x^+=\Psi_B(x_1).
\]

A third is the reversed sequence:

\[
\tilde x_1=\Psi_B(x),
\qquad
\tilde x^+=\Psi_A(\tilde x_1).
\]

These are different constructions.

Even when the two transformations are small residual increments, the sequential map contains cross terms that the additive map does not.

Take the linear residual increments

\[
F_A(x)=hAx,
\qquad
F_B(x)=hBx.
\]

The additive update is

\[
x^+
=
\left(I+h(A+B)\right)x.
\]

If \(A\) acts first and \(B\) acts on the resulting state,

\[
x^+
=
(I+hB)(I+hA)x,
\]

so

\[
x^+
=
\left(I+h(A+B)+h^2BA\right)x.
\]

The \(h^2BA\) term is not decoration. It records that \(B\) saw a state already changed by \(A\).

Reverse the order and the cross term becomes \(h^2AB\).

This is the first split-operator fact worth carrying into neural architecture design:

> **Sequential composition creates interaction terms that depend on order.**

## 2. A telescope with two lenses

A useful picture is a telescope with two different lenses.

Passing light through lens A and then lens B need not produce the same transformation as B then A. If the lenses implement transformations that commute, the order does not matter. If they do not commute, the ordering is part of the instrument.

The analogy maps cleanly onto operator composition:

- the incoming light corresponds to the current state;
- each lens corresponds to one state transformation;
- lens order corresponds to composition order;
- order independence corresponds to commutation.

The analogy stops there.

A neural attention sublayer is not literally an optical lens, and this picture does not prove numerical convergence, reversibility, or stability. Its job is only to make one structural point visible before we formalize it.

## 3. The exact reference problem

Start with the declared linear system

\[
\dot x=(A+B)x,
\]

where \(A\) and \(B\) are constant matrices.

The exact combined flow over a step \(h\) is

\[
e^{h(A+B)}.
\]

If we can solve the two parts separately, we can form the Lie-Trotter compositions

\[
S_{AB}(h)=e^{hA}e^{hB},
\]

and

\[
S_{BA}(h)=e^{hB}e^{hA}.
\]

The first means one exact \(B\)-subflow and one exact \(A\)-subflow in the composition order encoded by the matrix product. The second reverses them.

Expanding both exponentials gives

\[
e^{hA}e^{hB}
=
e^{h(A+B)}
+
\frac{h^2}{2}[A,B]
+
O(h^3),
\]

where

\[
[A,B]=AB-BA.
\]

The reversed order gives

\[
e^{hB}e^{hA}
=
e^{h(A+B)}
-
\frac{h^2}{2}[A,B]
+
O(h^3).
\]

So the first commutator is the leading object that records noncommutation.

If

\[
[A,B]=0,
\]

the two constant matrix exponentials commute and

\[
e^{hA}e^{hB}
=
e^{hB}e^{hA}
=
e^{h(A+B)}
\]

exactly.

This is not a vague statement that "order sometimes matters." It tells us what object measures the leading order difference in the declared smooth finite-dimensional setting.

## 4. The exact two-by-two witness

Use

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Both are nilpotent:

\[
A^2=B^2=0.
\]

Therefore

\[
e^{hA}=I+hA,
\qquad
e^{hB}=I+hB.
\]

Their products are

\[
AB=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
BA=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\]

so

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The two Lie steps are exactly

\[
S_{AB}(h)
=
\begin{pmatrix}
1+h^2&h\\
h&1
\end{pmatrix},
\]

and

\[
S_{BA}(h)
=
\begin{pmatrix}
1&h\\
h&1+h^2
\end{pmatrix}.
\]

Subtract:

\[
S_{AB}(h)-S_{BA}(h)
=
h^2[A,B].
\]

At \(h=1/2\),

\[
S_{AB}
=
\begin{pmatrix}
5/4&1/2\\
1/2&1
\end{pmatrix},
\]

while

\[
S_{BA}
=
\begin{pmatrix}
1&1/2\\
1/2&5/4
\end{pmatrix}.
\]

The two computations contain the same two exact subflows. They differ only in order. Yet the result is different.

That is the architectural fact we want.

## 5. The combined flow is not either Lie step

For this witness,

\[
A+B
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

and

\[
(A+B)^2=I.
\]

Hence

\[
e^{h(A+B)}
=
\begin{pmatrix}
\cosh h&\sinh h\\
\sinh h&\cosh h
\end{pmatrix}.
\]

At \(h=1/2\), neither Lie ordering equals this exact combined flow.

Their Frobenius errors are equal in this symmetric witness, approximately

\[
0.1793148494.
\]

The equality of those two error norms is incidental to this example. The important structural result is the signed leading commutator term.

This distinction matters when translating the picture into neural networks. The fact that an ordered block is a useful decomposition does not imply that it is the exact flow of some sum operator.

## 6. Symmetry cancels the quadratic defect

A standard symmetric composition is Strang splitting:

\[
S_{ABA}(h)
=
e^{hA/2}e^{hB}e^{hA/2}.
\]

For sufficiently regular problems, Strang splitting has a local defect of order \(O(h^3)\), corresponding to second-order global accuracy under the usual numerical-analysis assumptions [@McLachlanQuispel2002; @HairerLubichWanner2006].

Our witness shows the cancellation directly.

Because \(A^2=B^2=0\),

\[
S_{ABA}(h)
=
\begin{pmatrix}
1+h^2/2&h+h^3/4\\
h&1+h^2/2
\end{pmatrix}.
\]

The exact combined-flow series is

\[
e^{h(A+B)}
=
\begin{pmatrix}
1+h^2/2+h^4/24+O(h^6)&
h+h^3/6+O(h^5)\\
h+h^3/6+O(h^5)&
1+h^2/2+h^4/24+O(h^6)
\end{pmatrix}.
\]

The quadratic mismatch has disappeared.

At \(h=1/2\),

\[
S_{ABA}
=
\begin{pmatrix}
9/8&17/32\\
1/2&9/8
\end{pmatrix},
\]

whose Frobenius error against the exact flow is approximately

\[
0.02370487547.
\]

This one number is not the reason Strang is second order. The series derivation is the reason. The numeric checkpoint only witnesses the declared finite case.

## 7. A commuting control

Now choose

\[
A_c=\operatorname{diag}(1,2),
\qquad
B_c=\operatorname{diag}(3,4).
\]

Then

\[
[A_c,B_c]=0.
\]

Because the matrices commute,

\[
e^{hA_c}e^{hB_c}
=
e^{hB_c}e^{hA_c}
=
e^{h(A_c+B_c)}
\]

for every \(h\).

This control is important.

Without it, the chapter could leave the impression that every composition order must differ. The correct statement is narrower:

> **Noncommutation creates order dependence. Commutation removes it in the exact setting.**

The question for a learned architecture is therefore not "does order matter in principle?" but "what are the actual submaps, and how strongly do they fail to commute on the states that matter?"

That later empirical question is not answered by this chapter.

## 8. From exact flows to neural sublayers

Return to the Transformer residual stream.

Let \(H\) be the current residual-stream state. A simplified pre-normalized pair of learned submaps might be written as

\[
\Psi_A(H)=H+F_A(N_A(H)),
\]

\[
\Psi_B(H)=H+F_B(N_B(H)).
\]

Here \(F_A\) might stand for attention-like computation and \(F_B\) for an FFN-like computation.

The ordered block is then

\[
H'
=
(\Psi_B\circ\Psi_A)(H).
\]

The reversed block is

\[
\tilde H'
=
(\Psi_A\circ\Psi_B)(H).
\]

In general,

\[
H'\neq\tilde H'.
\]

Why?

Because the second submap receives a different input state.

This remains true even before we invoke any continuous-time interpretation.

The split-operator lens is therefore useful at two levels.

At the exact mathematical level, it gives the established theory of flows, commutators, Lie products, symmetric compositions, and splitting error.

At the architectural level, it gives a disciplined language for asking how named subcomputations are isolated and ordered.

Those two levels must not be collapsed.

## 9. Normalization belongs inside the submap

A common source of false simplification is to write "attention operator \(A\)" and "MLP operator \(B\)" while quietly omitting normalization.

In a pre-LN block, the actual maps look more like

\[
H_1
=
H+
\operatorname{Attn}(\operatorname{LN}(H)),
\]

\[
H_2
=
H_1+
\operatorname{FFN}(\operatorname{LN}(H_1)).
\]

If we call these two stages \(\Psi_A\) and \(\Psi_B\), then LayerNorm is part of the maps.

It affects the state dependence.

The same rule applies to:

- masking;
- gating;
- clipping;
- routing;
- residual scaling;
- stochastic dropout when active;
- state-dependent normalization;
- data-dependent control flow.

A commutator or order argument that drops these operations is analyzing a different system unless an explicit approximation justifies the omission.

## 10. Symmetry is not exact reversibility

The word "symmetric" is dangerous because it has several meanings.

Strang composition is symmetric in the step sequence:

\[
A/2
\to
B
\to
A/2.
\]

For exact flows, this time-symmetric composition has important numerical consequences.

To even write a neural analogue of that sequence, one must first define a step-parameterized family of learned maps
\[
\Psi_A(h),\qquad \Psi_B(h),
\]
with a meaningful half-stage \(\Psi_A(h/2)\). Only then can one form
\[
\Psi_A(h/2)\circ\Psi_B(h)\circ\Psi_A(h/2).
\]

For a generic learned block \(\Psi_A\) with no declared step parameter, the symbol "half of A" is not defined by the architecture. Halving a residual coefficient or duplicating a block is a new design choice, not automatically the classical half-flow.

Even when a valid step-parameterized family is declared, the resulting neural palindromic block is not automatically invertible.

If \(\Psi_A\) or \(\Psi_B\) loses information, clips state, normalizes non-injectively, uses non-invertible activation, drops tokens, or otherwise fails to be bijective on the relevant domain, the palindromic ordering does not repair that.

So we must distinguish:

- symmetric ordering;
- self-adjoint numerical composition under a declared flow model;
- exact invertibility;
- practical reconstructability;
- reversible-network implementation.

These are related ideas, not synonyms.

## 11. Shared operators and changing operators

Classical notation often suggests one fixed pair \(A,B\).

Neural networks often do not behave that way.

Layer \(k\) may use

\[
A_k,
\qquad
B_k,
\]

with different learned parameters at every depth.

Then the architecture is better viewed as stage-dependent or nonautonomous.

A commutator such as

\[
[A_k,B_k]
\]

may still be meaningful in a local linearized model, but it does not become one global autonomous commutator for the entire network.

This distinction separates two regimes:

### Shared operators

The same submaps recur across depth.

This is structurally closer to repeated stepping of one declared dynamical system.

### Layer-varying operators

Each stage has different submaps.

This is closer to a time-dependent system or a general composition chain.

Both can be studied with operator language. Their mathematical contracts differ.

## 12. Splitting error is only one error

Suppose a network is motivated by splitting a reference evolution.

Even then, "the error" is not one scalar object.

At minimum distinguish:

1. **splitting/discretization error**: difference between a numerical composition and the declared reference flow;
2. **approximation error**: learned submaps may not represent the intended component dynamics exactly;
3. **estimation error**: finite data limits what can be learned;
4. **optimization error**: training may not reach the intended parameter solution;
5. **stochastic variation**: minibatching, initialization, routing, or noise may change outcomes;
6. **implementation error**: finite precision, kernels, masking details, and system behavior may differ from the mathematical model.

Classical Lie or Strang order controls the first category under its assumptions.

It does not automatically control the others.

This is the same epistemic discipline used throughout the Atlas: one support route does not acquire authority over neighboring claims merely because the notation is convenient.

## 13. Ordering as an architectural degree of freedom

With those boundaries in place, the design lesson becomes stronger, not weaker.

A network designer can ask:

- Which transformations should be isolated as distinct submaps?
- Which state does each submap receive?
- Should they be applied sequentially, additively, or in a symmetric composition?
- Are parameters shared across depth?
- Is there a declared continuous reference problem?
- Is the architecture trying to preserve a structure?
- Where can noncommutation be measured?
- Does reversing order alter useful behavior?
- Is a small local commutator associated with robustness, stability, or transfer?
- When does symmetric composition help, and when is it merely extra compute?

These are empirical and mathematical questions.

The splitting framework organizes them without answering them in advance.

## 14. A Transformer block through the split lens

A baseline Transformer already presents an ordered pair of major subcomputations: attention and position-wise feed-forward transformation [@VaswaniEtAl2017].

In a pre-LN form,

\[
H_1
=
H+
\operatorname{Attn}(\operatorname{LN}(H)),
\]

\[
H_2
=
H_1+
\operatorname{FFN}(\operatorname{LN}(H_1)).
\]

A split-operator reading does not claim that these are exponentials of two known generators.

It asks instead:

> What changes if we treat these as two named state transformations whose order and composition law are explicit design choices?

That question exposes several architecture variants immediately:

- attention then FFN;
- FFN then attention;
- additive parallel updates from the same input state;
- explicitly step-parameterized palindromic attention-like / FFN-like compositions, when a meaningful half-step family is actually defined;
- shared repeated submaps;
- depth-varying submaps;
- submaps with measured or constrained local interaction.

Whether any of these is better is an experimental question.

The Atlas does not promote an architectural rearrangement from mathematical elegance alone.

## 15. What a neural commutator could mean

For linear operators, the commutator is unambiguous:

\[
[A,B]=AB-BA.
\]

For nonlinear maps, several related objects are possible.

One can compare compositions directly:

\[
\Psi_B(\Psi_A(x))
-
\Psi_A(\Psi_B(x)).
\]

One can also differentiate the nonlinear composition defect. If
\[
C_\Psi(x)
=
\Psi_B(\Psi_A(x))
-
\Psi_A(\Psi_B(x)),
\]
then, when the maps are differentiable,
\[
DC_\Psi(x)
=
J_B(\Psi_A(x))J_A(x)
-
J_A(\Psi_B(x))J_B(x).
\]

A same-state algebraic Jacobian commutator
\[
J_B(x)J_A(x)-J_A(x)J_B(x)
\]
can still be used as a local diagnostic, but it is generally not the derivative of \(C_\Psi\). Intermediate-state evaluation matters.

One can work with vector-field Lie brackets when actual differentiable vector fields have been declared.

These are not interchangeable.

A future diagnostic chapter may define a specific operational noncommutation probe. SPLIT-001 only establishes why such a probe could be informative and what mathematical distinctions it must preserve.

## 16. Failure modes

### 16.1 Calling every residual block an integrator

A residual form

\[
x_{k+1}=x_k+F_k(x_k)
\]

resembles an Euler step.

Resemblance is not identity.

Without a declared reference vector field, step-size semantics, and refinement family, "integrator" is an interpretation rather than a convergence theorem.

### 16.2 Treating Strang order as architectural magic

A palindromic block can be aesthetically attractive.

The \(O(h^3)\) local defect belongs to the classical splitting setting under the required assumptions. It does not automatically apply to arbitrary learned nonlinear sublayers. A neural half-step must itself be defined by a declared step-parameterized family before Strang language has mathematical content.

### 16.3 Ignoring normalization

If normalization is present in the executed block, dropping it from the operator model changes the object.

### 16.4 Confusing symmetry and invertibility

A symmetric sequence of non-invertible maps is still non-invertible.

### 16.5 Measuring one local commutator and claiming global control

A small commutator at one state, one layer, or one linearization does not establish global near-commutation.

### 16.6 Folding training error into splitting error

Optimization failure is not a discretization defect.

### 16.7 Assuming shared-operator formulas for layer-varying networks

A different \(A_k,B_k\) at every layer is a different mathematical object from repeated application of fixed \(A,B\).

## 17. What later chapters may now assume

The downstream Composition chapter may assume:

- additive and sequential composition are distinct;
- operator ordering can be architecturally load-bearing;
- the commutator is the leading finite-dimensional Lie-order object in the declared exact setting;
- symmetric composition has stronger cancellation properties under classical assumptions;
- neural submaps must include their actual normalization, routing, masking, and residual semantics.

The downstream Transport chapter may assume:

- split computation can be interpreted as staged transport only when the stage maps are explicitly declared;
- an exact-flow interpretation is stronger than a generic residual-composition interpretation;
- layer-varying stages require nonautonomous semantics.

Neither chapter may inherit a claim that Transformer sublayers are exact flows or that Strang-style neural blocks are automatically second order.

## 18. Epistemic status

Established theory:

- Lie-Trotter and Strang splitting;
- commutator-controlled order effects in the appropriate operator setting;
- composition and structure-preserving numerical methodology [@McLachlanQuispel2002; @HairerLubichWanner2006];
- baseline Transformer sublayer anatomy [@VaswaniEtAl2017].

Atlas-owned derivation:

- the exact nilpotent two-matrix witness;
- the additive-versus-sequential residual comparison;
- the explicit claim firewall connecting operator-splitting theory to neural architecture.

Computational witness:

- exact matrix products;
- exact commutator;
- exact Lie and Strang formulas;
- bounded \(h=1/2\) error values;
- commuting control.

Not established here:

- empirical superiority of split-operator neural architectures;
- small commutators in trained Transformers;
- exact flow semantics for attention or FFN sublayers;
- global reversibility from symmetric ordering;
- general convergence guarantees for learned split networks.

That boundary is deliberate.

The value of the split-operator lens is not that it turns a neural network into a numerical theorem.

It is that it forces us to say what the transformations are, what order they act in, what state each sees, and which mathematical claims survive the translation.


## References used in this chapter

- [@McLachlanQuispel2002] for Lie-Trotter/Strang splitting, commutators, composition, and order conditions.
- [@HairerLubichWanner2006] for geometric/composition-method boundaries and structure-preserving semantics.
- [@VaswaniEtAl2017] for baseline Transformer attention/FFN residual-block anatomy.

Exact provenance and authority boundaries are locked in:

`sources/source-locks/ATLAS-CH-SPLIT-001.yaml`.
