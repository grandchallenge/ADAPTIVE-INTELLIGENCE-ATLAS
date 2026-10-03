# NUMERICS-001 — Discretization, Stability, and Splitting

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- audited Dynamics merge:
  \`3c5050b50663e16725620dcf236a6bad61841d82\`;
- issue:
  \`#44\`;
- hard prerequisite:
  \`ATLAS-CH-DYN-001\` at audited \`draft-v0.1\`.

## Objective

Draft \`ATLAS-CH-NUMERICS-001\` as the numerical-analysis substrate for later Atlas chapters on:

- adaptive depth;
- split-operator computation;
- network numerics;
- implicit computation;
- Krylov acceleration;
- transport and structure-preserving optimization.

## A. Exact flow versus numerical map

The chapter freezes:

\[
\Phi_h
\neq
\Psi_h
\]

in general.

\(\Phi_h\) is the exact time-\(h\) flow.

\(\Psi_h\) is the update the computer actually executes.

The numerical map therefore defines its own discrete dynamical system.

## B. Local versus global error

One-step defect:

\[
d_{n+1}
=
\Phi_h(y_n)-\Psi_h(y_n).
\]

If

\[
\|d_{n+1}\|
\le
K h^{p+1},
\]

and the one-step map obeys an appropriate finite-time Lipschitz stability bound, discrete Grönwall reasoning gives global error:

\[
\|e_n\|
=
O(h^p)
\]

on a fixed time interval.

The chapter does not promote consistency alone into a universal convergence theorem.

## C. Scalar stability witness

Test equation:

\[
y'=\lambda y,
\qquad
z=h\lambda.
\]

Exact amplification:

\[
R_{\rm exact}(z)=e^z.
\]

Explicit Euler:

\[
R_E(z)=1+z.
\]

Absolute stability:

\[
|1+z|<1.
\]

Thus the explicit-Euler region is the disk centered at \(-1\) with radius \(1\).

Implicit Euler:

\[
R_I(z)=\frac{1}{1-z}.
\]

For

\[
\operatorname{Re}z<0,
\]

\[
|R_I(z)|<1.
\]

Thus implicit Euler is A-stable on the scalar test equation.

## D. Stiff two-timescale witness

System:

\[
\dot x
=
\begin{pmatrix}
-1&0\\
0&-100
\end{pmatrix}
x.
\]

At

\[
h=0.03,
\]

explicit Euler amplification:

\[
\{0.97,-2\}.
\]

The fast numerical mode diverges even though the exact fast mode decays by

\[
e^{-3}\approx0.049787.
\]

Implicit Euler amplification:

\[
\left\{
\frac{1}{1.03},
\frac14
\right\}.
\]

The fast mode is stable, but

\[
\frac14
\]

still poorly approximates

\[
e^{-3}.
\]

The tranche therefore freezes:

\[
\text{stability}
\neq
\text{accuracy}.
\]

## E. Structure-preservation bridge

For the harmonic oscillator, explicit Euler has

\[
M_E
=
\begin{pmatrix}
1&h\\
-h&1
\end{pmatrix},
\]

with

\[
\det M_E=1+h^2.
\]

A symplectic-Euler variant has

\[
M_{SE}
=
\begin{pmatrix}
1-h^2&h\\
-h&1
\end{pmatrix},
\]

with

\[
\det M_{SE}=1,
\]

and exact symbolic replay verifies

\[
M_{SE}^\top J M_{SE}=J.
\]

The chapter also gives an explicit energy counterexample showing:

\[
\text{symplectic}
\not\Rightarrow
\text{exact energy conservation}.
\]

## F. Noncommuting split witness

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

Then

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Lie-Trotter:

\[
\Psi_h^{LT}
=
e^{hA}e^{hB}.
\]

Exact series gives

\[
\Psi_h^{LT}
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3).
\]

Thus local defect begins at:

\[
O(h^2).
\]

Strang:

\[
\Psi_h^S
=
e^{hA/2}e^{hB}e^{hA/2}.
\]

Exact symbolic replay shows local defect beginning at:

\[
O(h^3).
\]

The chapter keeps the global-order conclusion conditional on standard repeated-step stability/regularity assumptions.

## G. Commuting boundary

If

\[
[A,B]=0,
\]

then

\[
e^{h(A+B)}
=
e^{hA}e^{hB}.
\]

Lie splitting is exact in the declared linear commuting case.

Therefore the commutator is a genuine leading noncommutativity signal, not merely a visualization device.

## H. Figure

\`ATLAS-FIG-NUMERICS-001\`

- generator blob:
  \`cd5bb3eeefbf545f33a5fe98460b4abdb6ba09dd\`;
- rendered blob:
  \`127994b7f90403555ef80218ffd5d49bde680ee7\`;
- rendered bytes:
  \`69,708\`;
- representation class:
  \`computed\`.

Panels:

1. explicit/implicit Euler stability geometry;
2. stiff fast-mode magnitude at \(h=0.03\);
3. computed Lie/Strang local defects on the exact split witness.

The symbolic witness, not visual slope estimation, establishes the error orders.

## I. Source boundary

External sources:

- Butcher 2016:
  one-step ODE methods, order, absolute stability;
- Hairer–Nørsett–Wanner 1993:
  consistency, convergence, error propagation;
- Hairer–Wanner 1996:
  stiff systems and implicit stability;
- Hairer–Lubich–Wanner 2006:
  geometric integration and splitting;
- Higham 2002:
  broader numerical stability/conditioning terminology.

Atlas-owned interpretation:

- layers as possible steps;
- depth as computational time/resource;
- stiffness as a lens on multiscale learned computation;
- commutators as later modular diagnostics.

These interpretations are not imported as theorems from the numerical-analysis sources.

## J. Frozen distinctions

\[
\text{exact flow}
\neq
\text{numerical update}.
\]

\[
\text{local error}
\neq
\text{global error}.
\]

\[
\text{dynamical stability}
\neq
\text{absolute stability}
\neq
\text{backward stability}.
\]

\[
\text{stable}
\neq
\text{accurate}.
\]

\[
\text{implicit}
\neq
\text{higher order by definition}.
\]

\[
\text{symplectic}
\neq
\text{exact-energy preserving}.
\]

\[
[A,B]\neq0
\Rightarrow
\text{composition order matters at leading split-error order}.
\]

## K. Durable outputs

The branch contains:

- source lock;
- chapter specification;
- derivation packet;
- exact computational witness;
- complete manuscript;
- Wolfram generator;
- rendered figure;
- figure manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## L. Next step after merge

Run a bounded post-draft audit checking:

- local/global error logic;
- explicit/implicit amplification factors;
- A-stability statement;
- stiff-system witness;
- stability-versus-accuracy distinction;
- symplectic-Euler identity and energy boundary;
- Lie/Strang defect algebra;
- source scope;
- figure provenance;
- no unearned promotion of numerical analogies into claims about neural architectures.
