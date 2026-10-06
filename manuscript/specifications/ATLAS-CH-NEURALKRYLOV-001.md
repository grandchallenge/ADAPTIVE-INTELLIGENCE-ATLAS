# Chapter Specification — ATLAS-CH-NEURALKRYLOV-001

## Identity

**Title:** Neural Krylov Transport  
**Part:** Numerical Intelligence  
**Status target:** draft-v0.1  
**Implementation issue:** #255  
**Protected baseline:** c9d5c61bf611327a1ed054206c5d8e778559e28a

## Hard prerequisites

### ATLAS-CH-KRYLOV-001 / AUDIT-039

May inherit:

- Krylov trial spaces;
- Arnoldi/Lanczos projection vocabulary;
- Galerkin/minimum-residual distinctions;
- residual/error conditioning boundaries;
- left/right preconditioning semantics;
- matrix-free operator access;
- restart and finite-precision cautions.

May not inherit a theorem that a learned nonlinear transport block obeys classical Krylov convergence.

### ATLAS-CH-TRANSPORT-001 / AUDIT-053

May inherit:

- declared representation state;
- exact finite state maps;
- local Jacobians;
- base-point semantics;
- constrained update/retraction distinctions;
- shared versus stage-dependent transport;
- discrete-composition versus continuous-flow boundaries.

May not identify a local Jacobian with the global nonlinear map.

Exact prerequisite identities and claim boundaries are frozen in:

sources/source-locks/ATLAS-CH-NEURALKRYLOV-001.yaml

## Chapter contract

Explore short-horizon iterative linear solves as representation computation while keeping the following objects typed:

1. representation state;
2. declared local linear operator;
3. right-hand side / local correction target;
4. preconditioner;
5. Krylov trial space;
6. transformed residual;
7. original-system residual;
8. true linear-solve error;
9. representation error/quality;
10. downstream task quality;
11. global nonlinear transport.

No equality between these objects is inherited by analogy.

## Local linear correction interface

At representation state \(z\), declare a local linear problem

\[
A_z \delta_z=b_z.
\]

The operator \(A_z\) must be named.

Possible constructions include:

- a local Jacobian-derived operator;
- a normal-equation operator;
- a Hessian-like local map;
- a learned linear surrogate.

The chapter does not select one universally.

A representation update can then be written abstractly as

\[
z^+=\Phi(z,\delta_z).
\]

This is only an interface.

A local solve does not become the global nonlinear dynamics of \(\Phi\).

## Fixed left preconditioning

For the exact witness, use

\[
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

The exact solution is

\[
x^\star=A^{-1}b=
\begin{pmatrix}
1\\1/4
\end{pmatrix}.
\]

Use fixed left preconditioner

\[
M=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
M^{-1}=
\begin{pmatrix}
1&0\\
0&1/2
\end{pmatrix}.
\]

The transformed system is

\[
Bx=c,
\]

with

\[
B=M^{-1}A=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\]

and

\[
c=M^{-1}b=
\begin{pmatrix}
1\\1/2
\end{pmatrix}.
\]

The exact solution remains \(x^\star\).

## Krylov spaces

With \(x_0=0\), define

\[
\mathcal K_m(B,c)
=
\operatorname{span}
\{
c,Bc,\ldots,B^{m-1}c
\}.
\]

For the witness:

\[
c=
\begin{pmatrix}
1\\1/2
\end{pmatrix},
\qquad
Bc=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Therefore:

\[
\mathcal K_1(B,c)=\operatorname{span}\{c\}.
\]

And because

\[
\det
\begin{pmatrix}
1&1\\
1/2&1
\end{pmatrix}
=
\frac12\neq0,
\]

we have:

\[
\boxed{
\mathcal K_2(B,c)=\mathbb R^2.
}
\]

## Best one-dimensional transformed-residual solution

Restrict:

\[
x=\alpha c.
\]

Choose \(\alpha\) to minimize transformed residual norm:

\[
\|c-Bx\|_2^2
=
\|c-\alpha Bc\|_2^2.
\]

Because

\[
c=
(1,1/2)^\top,
\qquad
Bc=(1,1)^\top,
\]

the objective is:

\[
(1-\alpha)^2+(1/2-\alpha)^2.
\]

The exact minimizer is:

\[
\boxed{
\alpha=\frac34.
}
\]

Thus:

\[
x_1=
\frac34 c
=
\begin{pmatrix}
3/4\\
3/8
\end{pmatrix}.
\]

## Transformed residual

The transformed residual is:

\[
\widehat r_1
=
c-Bx_1
=
\begin{pmatrix}
1/4\\
-1/4
\end{pmatrix}.
\]

Hence:

\[
\boxed{
\|\widehat r_1\|_2^2=\frac18.
}
\]

## Original-system residual

The original-system residual is:

\[
r_1
=
b-Ax_1
=
\begin{pmatrix}
1/4\\
-1/2
\end{pmatrix}.
\]

Therefore:

\[
\boxed{
\|r_1\|_2^2=\frac5{16}.
}
\]

The transformed residual and original residual are not the same quantity.

## True solution error

The true error is:

\[
e_1
=
x^\star-x_1
=
\begin{pmatrix}
1/4\\
-1/8
\end{pmatrix}.
\]

Hence:

\[
\boxed{
\|e_1\|_2^2=\frac5{64}.
}
\]

Residual norm and true error norm are different objects.

## Two-dimensional Krylov exactness

Because:

\[
\mathcal K_2(B,c)=\mathbb R^2,
\]

the exact solution lies in the trial space.

Indeed:

\[
\boxed{
x^\star
=
\frac32 c
-
\frac12 Bc.
}
\]

Therefore a full residual-minimizing solve over \(\mathcal K_2\) can achieve:

\[
\boxed{
\widehat r_2=0,
\qquad
r_2=0,
\qquad
e_2=0.
}
\]

This is exact finite-dimensional algebra.

It is not a general learned-system convergence theorem.

## Short-horizon improvement

The exact positive witness establishes:

\[
\mathcal K_1
\subsetneq
\mathcal K_2
=
\mathbb R^2,
\]

and:

\[
\|r_2\|_2^2
=
0
<
\frac5{16}
=
\|r_1\|_2^2.
\]

Likewise:

\[
\|e_2\|_2^2
=
0
<
\frac5{64}
=
\|e_1\|_2^2.
\]

Thus one additional operator-generated direction can strictly improve the declared local solve.

## What this positive witness does not prove

It does not prove:

- fast convergence in high dimensions;
- that two steps suffice in general;
- that learned operators have favorable spectra;
- that a local solve improves downstream task quality;
- that learned preconditioners are stable;
- that the global nonlinear representation map is linear.

## Low-dimension failure control

Use a separate operator:

\[
B_{\rm bad}
=
\begin{pmatrix}
1&0\\
0&10
\end{pmatrix},
\qquad
c_{\rm bad}
=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Again:

\[
\mathcal K_1(B_{\rm bad},c_{\rm bad})
=
\operatorname{span}\{c_{\rm bad}\},
\]

which is one-dimensional.

Restrict:

\[
x=\alpha c_{\rm bad}.
\]

The minimum-residual scalar is:

\[
\boxed{
\alpha=\frac{11}{101}.
}
\]

The residual is:

\[
r_{\rm bad}
=
c_{\rm bad}
-
\alpha B_{\rm bad}c_{\rm bad}
=
\begin{pmatrix}
90/101\\
-9/101
\end{pmatrix}.
\]

Therefore:

\[
\boxed{
\|r_{\rm bad}\|_2^2
=
\frac{81}{101}.
}
\]

The trial space is tiny.

The residual remains large.

Hence:

\[
\boxed{
\text{low Krylov dimension}
\not\Rightarrow
\text{good one-step solve}.
}
\]

## Metric firewall: exact task readout despite solve error

For the positive witness, define downstream scalar readout:

\[
w=
\begin{pmatrix}
1\\2
\end{pmatrix}.
\]

For the exact solution:

\[
w^\top x^\star
=
1+2(1/4)
=
\frac32.
\]

For the non-exact one-step solution:

\[
w^\top x_1
=
3/4+2(3/8)
=
\frac32.
\]

Thus:

\[
\boxed{
w^\top x_1=w^\top x^\star
}
\]

even though:

\[
r_1\neq0
\]

and:

\[
e_1\neq0.
\]

Therefore:

\[
\boxed{
\text{exact task readout}
\not\Rightarrow
\text{exact solve}.
}
\]

And conversely, no general theorem says a smaller residual must improve every downstream task metric.

## Representation quality remains separate

If \(x\) is used as a representation correction, one may evaluate:

- Euclidean error;
- angular error;
- constraint violation;
- retained information;
- probe performance;
- task reward.

None is automatically equal to residual norm.

The chapter must name the metric actually being optimized.

## Preconditioner semantics

The witness uses a fixed linear left preconditioner.

Left preconditioning means solving:

\[
M^{-1}Ax=M^{-1}b.
\]

It changes the effective operator:

\[
A\mapsto M^{-1}A.
\]

A right preconditioner would define a different transformed problem.

A learned, state-dependent, flexible, or nonlinear preconditioner requires separate semantics.

## Learned preconditioner boundary

If a neural module outputs:

\[
M_\theta(z),
\]

then the effective operator may vary with state.

Classical fixed-preconditioner identities may no longer apply unchanged.

The chapter may describe the architecture.

It may not import a fixed-linear convergence theorem without proving the required conditions.

## Local Jacobian construction

Suppose:

\[
z^+=\Phi(z).
\]

At base state \(z_0\), a local differential object is:

\[
J_\Phi(z_0).
\]

A declared local correction operator might be built from it, for example:

\[
A_{z_0}
=
I-J_\Phi(z_0)
\]

or another explicitly defined map.

The choice must be stated.

The chapter must not silently replace:

\[
\Phi
\]

by:

\[
J_\Phi(z_0).
\]

## Local versus global

A local linear solve can describe:

- one correction;
- one tangent approximation;
- one local inference step.

It does not by itself establish global convergence of repeated nonlinear updates.

If the operator changes after each representation update, the process is no longer one fixed classical Krylov problem.

## Shared versus stage-dependent operators

If:

\[
A_k=A
\]

for all stages, one can reason about repeated action of a fixed operator.

If:

\[
A_k
\]

depends on \(k\) or \(z_k\), then the operator family is nonstationary.

A subspace generated under one operator need not remain a classical Krylov space for the next.

## Matrix-free access

The chapter may permit operator actions such as:

\[
v\mapsto A_zv
\]

without explicitly forming \(A_z\).

For a Jacobian-derived operator, this may correspond to a declared JVP/VJP interface.

Matrix-free access is computational semantics.

It does not change the mathematical operator that must be named.

## Residual versus error

For:

\[
Ax=b,
\]

the residual is:

\[
r=b-Ax.
\]

The error is:

\[
e=x^\star-x.
\]

They satisfy:

\[
Ae=r.
\]

Thus any bound relating them depends on properties of \(A\), for example:

\[
\|e\|
\le
\|A^{-1}\|\|r\|
\]

when \(A\) is invertible.

Residual and error are not numerically interchangeable.

## Preconditioned residual versus original residual

For left preconditioning:

\[
\widehat r=M^{-1}r.
\]

A small transformed residual need not have the same numerical scale as the original residual.

Both should be reported when their distinction matters.

## Finite precision

Exact Krylov identities assume exact arithmetic unless stated otherwise.

In finite precision:

- orthogonality can degrade;
- generated directions can lose independence;
- recurrence behavior can change;
- residual estimates may drift from explicitly recomputed residuals.

A neural implementation inherits these numerical issues if it explicitly relies on Krylov basis geometry.

## Restart/truncation

A short-horizon architecture may deliberately truncate after \(m\) directions.

That is a compute/memory choice.

It may discard a direction that would have improved the solve.

The exact positive witness demonstrates one such possibility:

- horizon \(m=1\): nonzero error;
- horizon \(m=2\): exact solve.

No universal optimal horizon follows.

## Architecture template

A bounded Neural Krylov Transport block may be described as:

1. receive representation state \(z\);
2. define local operator \(A_z\);
3. define local right-hand side \(b_z\);
4. define preconditioner \(M_z\) if any;
5. generate at most \(m\) operator-action directions;
6. solve/project in the declared trial space;
7. obtain correction \(\delta_z^{(m)}\);
8. update representation through declared map \(\Phi(z,\delta_z^{(m)})\);
9. expose residual/error/task diagnostics separately.

This is an architecture contract.

It is not a convergence theorem.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{low subspace dimension}
\not\Rightarrow
\text{small residual},
\]

\[
\text{small residual}
\not\Rightarrow
\text{small true error without conditioning information},
\]

\[
\text{small solve error}
\not\Rightarrow
\text{good representation/task quality},
\]

\[
\text{exact task readout}
\not\Rightarrow
\text{exact solve},
\]

\[
\text{local Jacobian Krylov step}
\not\Rightarrow
\text{global nonlinear convergence},
\]

\[
\text{representation transport}
\not\Rightarrow
\text{Krylov convergence theorem},
\]

and:

\[
\text{learned preconditioner}
\not\Rightarrow
\text{fixed-linear preconditioner guarantees}.
\]

## Reader outcomes

A reader should be able to:

1. declare the operator underlying a Neural Krylov construction;
2. distinguish original and left-preconditioned systems;
3. reproduce the exact \(K_1\) minimizer \(\alpha=3/4\);
4. reproduce transformed residual \(1/8\), original residual \(5/16\), and true error \(5/64\);
5. prove \(K_2=\mathbb R^2\) and reconstruct the exact solution;
6. reproduce the bad-control residual \(81/101\);
7. explain why low dimension alone is not a convergence certificate;
8. reproduce the exact task-readout equality at the non-exact one-step solution;
9. distinguish local linear operator semantics from global nonlinear transport;
10. explain why learned/state-dependent preconditioners require new analysis.

## Required artifacts

- source lock;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## Downstream handoff

Later adaptive-depth, systems, diagnostics, or optimization chapters may inherit:

- explicit local-solve interface;
- fixed-left-preconditioned finite witness;
- Krylov-horizon semantics;
- residual/error/task-quality firewall;
- operator-identity requirement;
- learned-preconditioner boundary.

They may not inherit a learned nonlinear convergence theorem.

## References used in this chapter

No new external academic authority is added.

Classical numerical-linear-algebra authority is inherited through audited ATLAS-CH-KRYLOV-001.

Representation-transport authority is inherited through audited ATLAS-CH-TRANSPORT-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-NEURALKRYLOV-001.yaml
