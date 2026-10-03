# ATLAS-CH-NUMERICS-001 — Derivation Packet

## D1. Exact flow versus one-step map

For

\[
\dot x=f(t,x),
\]

let the exact time-\(h\) flow from \((t_n,x)\) be

\[
\Phi_h(t_n,x).
\]

A numerical one-step method defines another map

\[
\Psi_h(t_n,x).
\]

The exact and numerical maps are different objects.

Define the local defect from an exact state:

\[
\delta_{n+1}
=
\Phi_h(t_n,x(t_n))
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

Under an appropriate finite-time Lipschitz/stability bound for numerical error propagation, local order \(p+1\) yields global order \(p\):

\[
e_n
=
x(t_n)-x_n
=
O(h^p).
\]

Consistency without the needed stability/regularity assumptions is not sufficient by itself.

## D2. Explicit Euler

Taylor-expand the exact solution:

\[
x(t_n+h)
=
x(t_n)
+
h x'(t_n)
+
\frac{h^2}{2}x''(t_n)
+
O(h^3).
\]

Since

\[
x'(t_n)
=
f(t_n,x(t_n)),
\]

explicit Euler uses

\[
\Psi_h^{\rm EE}(t_n,x)
=
x+h f(t_n,x).
\]

Hence the local defect is

\[
\boxed{
\delta_{n+1}^{\rm EE}
=
\frac{h^2}{2}x''(t_n)
+
O(h^3).
}
\]

Therefore explicit Euler is globally first order under standard finite-time assumptions.

## D3. Implicit Euler

Implicit Euler is

\[
x_{n+1}
=
x_n
+
h f(t_{n+1},x_{n+1}).
\]

The unknown future state appears on both sides.

Thus each step generally requires solving a nonlinear or linear equation.

A Taylor expansion around \(t_{n+1}\) similarly gives first-order global accuracy under standard assumptions.

## D4. Scalar test equation

Consider

\[
y'=\lambda y.
\]

Let

\[
z=h\lambda.
\]

### Explicit Euler

\[
y_{n+1}
=
y_n+h\lambda y_n
=
(1+z)y_n.
\]

Thus

\[
\boxed{
R_{\rm EE}(z)=1+z.
}
\]

The standard absolute-stability set uses non-growth:

\[
|R(z)|\le1.
\]

For explicit Euler this is

\[
|1+z|\le1.
\]

Strict asymptotic decay requires

\[
|1+z|<1.
\]

Thus the absolute-stability set is the closed disk centered at \(-1\) with radius \(1\), while its open interior gives strict decay.

### Implicit Euler

\[
y_{n+1}
=
y_n+h\lambda y_{n+1}.
\]

Therefore

\[
(1-z)y_{n+1}=y_n,
\]

so

\[
\boxed{
R_{\rm IE}(z)
=
\frac{1}{1-z}.
}
\]

The standard non-growth stability condition is

\[
\left|\frac{1}{1-z}\right|\le1,
\]

equivalently

\[
|1-z|\ge1.
\]

Every point in the closed left half-plane satisfies this condition.

For \(\operatorname{Re}z<0\), the inequality is strict and the scalar mode decays asymptotically.

Thus implicit Euler is A-stable.

Moreover,

\[
R_{\rm IE}(z)\to0
\]

as \(|z|\to\infty\) within the left half-plane, so implicit Euler is L-stable.

## D5. Exact stiff scalar witness

Take

\[
y'=-100y,
\]

with

\[
h=0.05=\frac1{20}.
\]

Then

\[
z
=
h\lambda
=
-5.
\]

### Exact factor

\[
e^z
=
e^{-5}
\approx
0.00673795.
\]

### Explicit Euler

\[
R_{\rm EE}(-5)
=
1-5
=
-4.
\]

Thus the discrete magnitude grows by factor \(4\).

The method is unstable for this step size.

### Implicit Euler

\[
R_{\rm IE}(-5)
=
\frac{1}{1+5}
=
\frac16.
\]

Thus the mode decays.

The method is stable.

But

\[
\frac16
\approx
0.1667
\]

is far from

\[
e^{-5}
\approx
0.00674.
\]

Therefore:

\[
\boxed{
\text{stability}
\neq
\text{accuracy}.
}
\]

## D6. Stiffness interpretation

A problem is called stiff when numerically stable integration forces a method to use steps much smaller than the timescale of the behavior one wants to resolve, typically because rapidly decaying modes coexist with slower modes.

Stiffness is therefore a property of the problem together with the numerical method and requested accuracy.

It is not simply “a large derivative.”

The scalar example isolates the stability mechanism without pretending to define all stiffness phenomena.

## D7. Linear splitting setup

Consider

\[
\dot x
=
(A+B)x
\]

with constant matrices \(A,B\).

The exact flow is

\[
e^{h(A+B)}.
\]

If the subflows

\[
e^{hA},
\qquad
e^{hB}
\]

are easier to compute or preserve useful structure, one can compose them.

## D8. Lie–Trotter splitting

For the ordering used here,

\[
S_{\rm LT}(h)
=
e^{hA}e^{hB}.
\]

Expand:

\[
e^{hA}
=
I+hA+\frac{h^2}{2}A^2+O(h^3),
\]

\[
e^{hB}
=
I+hB+\frac{h^2}{2}B^2+O(h^3).
\]

Multiplying:

\[
S_{\rm LT}(h)
=
I+h(A+B)
+
h^2
\left(
\frac12A^2+AB+\frac12B^2
\right)
+
O(h^3).
\]

The exact flow expands as

\[
e^{h(A+B)}
=
I+h(A+B)
+
\frac{h^2}{2}
(A^2+AB+BA+B^2)
+
O(h^3).
\]

Subtract:

\[
\boxed{
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}(AB-BA)
+
O(h^3).
}
\]

Thus

\[
\boxed{
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3).
}
\]

The leading local defect is governed by noncommutativity.

If

\[
[A,B]=0,
\]

then

\[
e^{hA}e^{hB}
=
e^{h(A+B)}
\]

exactly for constant matrices.

## D9. Exact split witness matrices

Choose

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
A^2=B^2=0,
\]

and

\[
AB
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]

\[
BA
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
}
\]

Wolfram expansion gives

\[
S_{\rm LT}(h)-e^{h(A+B)}
=
\begin{pmatrix}
h^2/2&-h^3/6\\
-h^3/6&-h^2/2
\end{pmatrix}
+
O(h^4),
\]

with the expected \(h^2[A,B]/2\) leading term.

## D10. Strang splitting

Define the symmetric composition

\[
S_{\rm S}(h)
=
e^{hA/2}
e^{hB}
e^{hA/2}.
\]

Symmetry cancels the second-order local defect.

For sufficiently regular bounded operators, the local defect is

\[
\boxed{
S_{\rm S}(h)
-
e^{h(A+B)}
=
O(h^3).
}
\]

Thus the global method is second order under standard stability/regularity assumptions.

For the exact witness matrices, Wolfram gives

\[
S_{\rm S}(h)-e^{h(A+B)}
=
\begin{pmatrix}
O(h^4)&h^3/12+O(h^5)\\
-h^3/6+O(h^5)&O(h^4)
\end{pmatrix}.
\]

The first nonzero terms are order \(h^3\).

## D11. Splitting order versus commutativity

Lie–Trotter and Strang are not merely different ways to arrange code.

Their error is controlled by operator algebra.

If suboperators commute, the split can become exact.

If they do not, commutators and nested commutators determine leading errors.

This is the mathematical handoff to the later split-operator architecture chapter.

## D12. Structure preservation

Suppose each subflow preserves some structure.

A composition can sometimes preserve that structure exactly.

For example, a composition of symplectic maps is symplectic.

But this is structure-specific.

A method that is symplectic need not preserve the original Hamiltonian exactly.

A method that preserves positivity need not preserve a norm.

The phrase “structure-preserving” is incomplete unless the preserved structure is named.

## D13. Adaptive-depth handoff

If a neural block is interpreted as a numerical step, then:

- depth resembles number of steps;
- layer scale resembles step size;
- local residual can resemble a local defect estimate;
- adaptive depth can resemble error-controlled integration.

These are architectural hypotheses.

They require an actual correspondence between learned update and numerical model.

The present chapter supplies the numerical vocabulary but does not validate a neural architecture by analogy alone.

## Claim boundary

This packet establishes standard one-step stability facts, a stiff scalar witness, the Lie–Trotter commutator defect for the declared ordering, and the Strang local error order for bounded matrix examples.

It does not claim universal convergence from consistency alone, universal stiffness diagnostics, or that neural residual blocks are automatically numerical integrators.
