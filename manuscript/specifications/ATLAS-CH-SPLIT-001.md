# Chapter Specification — ATLAS-CH-SPLIT-001

## Identity

**Title:** Split-Operator Networks  
**Part:** Neural Architectures  
**Status:** specification-ready.  
**Epistemic class:** established operator-splitting theory + Atlas architectural synthesis.

## Chapter contract

Apply operator splitting to neural computation and analyze ordering, commutators, and splitting error without pretending that an arbitrary learned block is automatically an exact numerical flow.

The chapter must make operator ordering a visible architectural degree of freedom.

## Dependency contract

Hard prerequisites:

- `ATLAS-CH-NUMERICS-001`;
- `ATLAS-CH-TRANSFORMER-001`.

May assume from Numerics:

- exact flows and one-step maps;
- Lie-Trotter and Strang composition;
- local versus global error;
- stability and stiffness distinctions;
- bounded structure-preserving semantics.

May assume from Transformer:

- residual-stream state;
- attention and FFN sublayers;
- normalization placement;
- masking;
- residual paths;
- baseline block topology.

Must not assume:

- that learned residual updates are exact exponentials;
- that an arbitrary learned submap has a meaningful half-step; a Strang-style neural analogue requires an explicitly declared step-parameterized family \(\Psi_A(h\),\Psi_B(h\)\) with a defined \(h/2\) stage;
- that classical splitting order transfers to arbitrary nonlinear learned maps;
- that a symmetric block is exactly reversible;
- that attention and FFN commute;
- that splitting error subsumes optimization, approximation, or implementation error.

## Reader outcomes

A reader should be able to:

1. distinguish additive and sequential operator composition;
2. write both Lie orderings;
3. derive the leading commutator term for constant finite-dimensional operators;
4. explain why reversing the order changes the sign of that leading term;
5. state the bounded second-order meaning of Strang symmetry;
6. separate exact flow notation from a neural residual-map analogy;
7. identify the role of normalization and residual wrapping in the effective submap;
8. distinguish shared/autonomous from layer-varying/nonautonomous suboperators;
9. separate splitting error from training and modeling errors;
10. state when commuting operators eliminate order dependence.

## Formal object

For a declared reference problem

\[
\dot x=(A+B)x,
\]

with constant matrices \(A,B\), define exact subflows

\[
\Phi_A\(h\)=e^{hA},
\qquad
\Phi_B\(h\)=e^{hB}.
\]

Lie product labels:

\[
S_{AB}\(h\)=e^{hA}e^{hB},
\qquad
S_{BA}\(h\)=e^{hB}e^{hA}.
\]

For column vectors, matrix products act right-to-left. Thus \(S_{AB}\) is a product-order label: it applies the \(B\) subflow first and then the \(A\) subflow. Chronological "A then B" is \(S_{BA}\). The chapter must not use product subscripts as ambiguous execution-order prose.

Symmetric Strang composition:

\[
S_{ABA}\(h\)=e^{hA/2}e^{hB}e^{hA/2}.
\]

Commutator:

\[
[A,B]=AB-BA.
\]

In the declared finite-dimensional analytic setting,

\[
S_{AB}\(h\)-e^{h(A+B)}
=
\frac{h^2}{2}[A,B]+O(h^3),
\]

and reversing the order reverses the sign of the leading commutator term.

The symmetric composition has local defect \(O(h^3)\).

## Neural translation

For a residual-stream state \(H\), define two learned submaps explicitly:

\[
\Psi_A(H\)=H+F_A(N_A(H\)),
\]

\[
\Psi_B(H\)=H+F_B(N_B(H\)).
\]

Then the ordered block

\[
H'=(\Psi_B\circ\Psi_A)\(H\)
\]

is not equivalent in general to

\[
(\Psi_A\circ\Psi_B)\(H\).
\]

Normalization, masking, residual wrapping, parameter sharing, and any stochasticity are part of the submap definition and cannot be removed from the mathematical object without argument.

Use exact-flow notation \(e^{hA}\) only for the linear witness and other settings where an exact flow has actually been declared.

## Additive versus sequential witness

For linear residual increments \(F_A(x\)=hAx\), \(F_B(x\)=hBx\):

additive update:

\[
x^+=\left(I+h(A+B)\right)x;
\]

A-then-B sequential residual update:

\[
x^+
=
(I+hB)(I+hA)x
=
\left(I+h(A+B)+h^2BA\right)x.
\]

The cross term is the first visible reason additive and sequential composition differ.

## Exact noncommuting witness

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

Then \(A^2=B^2=0\) and

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

At \(h=1/2\),

\[
e^{hA}e^{hB}
=
\begin{pmatrix}
5/4&1/2\\
1/2&1
\end{pmatrix},
\]

while

\[
e^{hB}e^{hA}
=
\begin{pmatrix}
1&1/2\\
1/2&5/4
\end{pmatrix}.
\]

Their difference is exactly

\[
\frac14[A,B].
\]

Also

\[
e^{h(A+B)}
=
\begin{pmatrix}
\cosh h&\sinh h\\
\sinh h&\cosh h
\end{pmatrix}.
\]

For Strang,

\[
e^{hA/2}e^{hB}e^{hA/2}
=
\begin{pmatrix}
1+h^2/2&h+h^3/4\\
h&1+h^2/2
\end{pmatrix}.
\]

Its Taylor defect begins at cubic order.

## Commuting control

Use diagonal matrices

\[
A_c=\operatorname{diag}(1,2),
\qquad
B_c=\operatorname{diag}(3,4).
\]

Since \([A_c,B_c]=0\),

\[
e^{hA_c}e^{hB_c}
=
e^{hB_c}e^{hA_c}
=
e^{h(A_c+B_c)}
\]

exactly for every \(h\).

## Principal pedagogical device

### Allegory: two lenses in a telescope

Passing light through lens A and then lens B need not produce the same transformation as B then A. If the two transformations commute, order disappears. If not, the order itself is part of the instrument.

Limit:

Neural sublayers are not literal optical lenses, and the allegory does not establish any numerical order or convergence property.

## Failure boundaries

Include:

- residual update is not automatically exact flow;
- sequential is not additive;
- symmetry is not the same as invertibility;
- commuting toy matrices do not imply learned sublayers commute;
- Strang order does not automatically survive arbitrary state dependence, normalization, discontinuous routing, stochasticity, or learned approximation;
- layer-varying operators require a nonautonomous reading;
- splitting error is distinct from model, data, estimation, optimization, finite-precision, and implementation error;
- small commutator in one local linearization is not a global theorem;
- the same-state Jacobian commutator \(J_B(x\)J_A(x\)-J_A(x\)J_B(x\)\) is a local diagnostic, not the derivative of the nonlinear composition defect in general.

## Downstream obligations

Direct consumers:

- `ATLAS-CH-COMPOSE-001`;
- `ATLAS-CH-TRANSPORT-001`.

The chapter may also inform boundary-contract and architecture-design discussions, but soft conceptual links do not become hard dependencies.

## Sources

- [@McLachlanQuispel2002]
- [@HairerLubichWanner2006]
- [@VaswaniEtAl2017]

Source lock:

`sources/source-locks/ATLAS-CH-SPLIT-001.yaml`.

## Acceptance

The draft must:

- derive both Lie product orderings and the commutator sign with an explicit right-to-left application convention;
- include a bounded Strang derivation and require a declared step-parameterized family before using neural half-step notation;
- include the exact noncommuting witness and commuting control;
- distinguish exact-flow mathematics from neural architectural synthesis;
- model normalization/residual wrapping as part of the submaps;
- distinguish additive from sequential updates;
- distinguish shared from layer-varying suboperators;
- separate splitting error from training/modeling errors;
- update the ledger and source register;
- include a tranche receipt and pass repository validation.
