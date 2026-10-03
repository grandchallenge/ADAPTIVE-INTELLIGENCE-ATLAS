# Chapter Specification — ATLAS-CH-NUMERICS-001

## Identity

**Title:** Discretization, Stability, and Splitting  
**Part:** Mathematical Substrate  
**Status:** specification-ready.  
**Epistemic class:** established numerical analysis + Atlas synthesis.

## Chapter contract

Develop exactly the numerical-analysis language later Atlas chapters need to reason about depth, integration, split operators, adaptive computation, and structure-preserving updates.

This chapter must keep three questions separate:

1. Does a method approximate the exact flow locally?
2. Is the discrete method stable for the regime being integrated?
3. Does the resulting global trajectory converge at the claimed order?

It must also distinguish ordinary one-step integration from operator splitting.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-DYN-001\`.

May assume:

- exact flow maps;
- equilibria/stability language;
- matrix exponentials for constant linear systems;
- Hamiltonian/symplectic vocabulary.

Must not assume:

- adaptive-step algorithms;
- backward error analysis beyond an introductory handoff;
- neural architecture claims;
- PDE-specific splitting theory.

## Reader outcome

A reader should be able to:

1. define a one-step numerical method;
2. distinguish local defect from global error;
3. explain consistency and convergence under stated assumptions;
4. derive explicit and implicit Euler;
5. derive their scalar stability functions;
6. interpret absolute-stability regions;
7. distinguish stability from accuracy;
8. explain stiffness as a problem/method interaction;
9. derive the exact stiff scalar example;
10. define Lie–Trotter and Strang splitting;
11. show how noncommutativity enters the Lie defect;
12. explain why symmetric Strang composition cancels the second-order defect;
13. understand that structure preservation is method-specific.

## One-step framework

For

\[
\dot x=f(t,x),
\]

write a one-step method as

\[
x_{n+1}
=
\Psi_h(t_n,x_n).
\]

Define local defect from an exact state:

\[
\delta_{n+1}
=
x(t_{n+1})
-
\Psi_h(t_n,x(t_n)).
\]

A method of order \(p\) has

\[
\delta_{n+1}
=
O(h^{p+1})
\]

under the required smoothness assumptions.

On a finite interval, with a suitable Lipschitz/stability bound for the numerical propagation, this leads to global error

\[
e_n
=
x(t_n)-x_n
=
O(h^p).
\]

Do not state consistency alone as sufficient for convergence.

## Explicit Euler

\[
x_{n+1}
=
x_n
+
h f(t_n,x_n).
\]

Taylor expansion gives local defect

\[
\delta_{n+1}
=
\frac{h^2}{2}x''(t_n)
+
O(h^3),
\]

so the method is first order globally under standard regularity/stability conditions.

## Implicit Euler

\[
x_{n+1}
=
x_n
+
h f(t_{n+1},x_{n+1}).
\]

Emphasize that this generally requires solving an equation at each step.

## Scalar test equation

Use

\[
y'=\lambda y,
\qquad
z=h\lambda.
\]

Explicit Euler:

\[
R_{\rm EE}(z)
=
1+z.
\]

Implicit Euler:

\[
R_{\rm IE}(z)
=
\frac{1}{1-z}.
\]

Use the standard non-growth absolute-stability set

\[
\mathcal S
=
\{z:|R(z)|\le1\}.
\]

Strict asymptotic decay of the scalar discrete mode requires

\[
|R(z)|<1.
\]

State:

- explicit Euler absolute-stability set:
  \[
  |1+z|\le1,
  \]
  with strict decay in the open disk \(|1+z|<1\);
- implicit Euler is A-stable because the entire closed left half-plane lies in its non-growth stability set, with strict decay for \(\operatorname{Re}z<0\);
- implicit Euler is L-stable because
  \[
  R_{\rm IE}(z)\to0
  \]
  as \(z\to-\infty\) along the negative real axis / in the stiff limit.

## Exact stiff witness

Use

\[
y'=-100y,
\qquad
h=0.05.
\]

Exact one-step factor:

\[
e^{-5}.
\]

Explicit Euler:

\[
1-5=-4.
\]

Implicit Euler:

\[
\frac{1}{1+5}
=
\frac16.
\]

Emphasize:

- explicit Euler is unstable;
- implicit Euler is stable;
- \(1/6\) is still a poor approximation to \(e^{-5}\), so stability is not accuracy.

## Splitting framework

For

\[
\dot x
=
(A+B)x,
\]

with exactly solvable subflows:

### Lie–Trotter

\[
S_{\rm LT}(h)
=
e^{hA}e^{hB}.
\]

For bounded matrices,

\[
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3),
\]

for this ordering convention, where

\[
[A,B]
=
AB-BA.
\]

Thus commuting operators split exactly in the linear constant-coefficient setting.

### Strang

\[
S_{\rm S}(h)
=
e^{hA/2}
e^{hB}
e^{hA/2}.
\]

The symmetric composition has local defect

\[
O(h^3),
\]

and therefore second-order global accuracy under the usual smoothness/stability assumptions.

## Exact split witness

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

Wolfram series should verify:

\[
S_{\rm LT}(h)-e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3),
\]

and

\[
S_{\rm S}(h)-e^{h(A+B)}
=
O(h^3).
\]

## Principal pedagogical device

### Allegory: navigating with a map versus walking the terrain

The exact flow is the terrain's true route.

A numerical method is a map-based stepping rule.

Consistency says each small step points approximately the right way.

Stability says small errors are not catastrophically amplified by the stepping process.

Convergence says the whole route approaches the true route as the step is refined.

Limit:

Numerical analysis is not literally navigation; the analogy does not replace norms, error bounds, or method-specific assumptions.

## Figure programme

### ATLAS-FIG-NUMERICS-001

Three panels:

1. explicit Euler stability disk \(|1+z|<1\);
2. implicit Euler stability region boundary \(|1-z|=1\), emphasizing the left half-plane is included in the stable exterior;
3. log-log local defect versus \(h\) for the exact split witness, showing Lie slope 2 and Strang slope 3 asymptotically.

Representation class: exact/data-derived.

## Computational witness

Wolfram exact/symbolic checks of:

- Euler stability functions;
- stiff amplification factors;
- exact split-system commutator;
- exact and split Taylor series;
- Lie leading defect;
- Strang leading order.

## Failure boundaries

Include:

- consistency without suitable stability does not ensure convergence;
- absolute stability does not ensure accuracy;
- implicit does not mean unconditionally accurate;
- stiffness is method/problem relative;
- splitting order can degrade outside its regularity assumptions;
- commuting and noncommuting splits behave qualitatively differently;
- structure-preserving claims must name the structure.

## Downstream obligations

Immediate consumers:

- \`ATLAS-CH-DEPTH-001\`;
- \`ATLAS-CH-SPLIT-001\`;
- \`ATLAS-CH-VARIOPT-001\`;
- \`ATLAS-CH-NETNUM-001\`.

## Sources

- [@Iserles2008]
- [@HairerWanner1996]
- [@McLachlanQuispel2002]
- [@HairerLubichWanner2006]

Source lock: \`sources/source-locks/ATLAS-CH-NUMERICS-001.yaml\`.

## Acceptance

The draft must:

- distinguish local defect, stability, and global convergence;
- derive explicit/implicit Euler stability functions;
- include the exact stiff witness and stability-versus-accuracy warning;
- derive the Lie commutator term for the declared ordering;
- verify Strang local \(O(h^3)\) defect;
- keep splitting and structure-preservation claims bounded;
- include source lock, derivation packet, computational witness, and reproducible figure.
