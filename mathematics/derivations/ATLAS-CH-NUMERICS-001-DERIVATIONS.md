# ATLAS-CH-NUMERICS-001 — Derivation Packet

## D1. Exact flow versus numerical update

Let

\[
\dot x=f(x)
\]

have exact time-\(h\) flow

\[
\Phi_h.
\]

A one-step numerical method defines a generally different map

\[
\Psi_h.
\]

Starting from state \(x_n\),

\[
x_{n+1}
=
\Psi_h(x_n).
\]

Unless equality is proved,

\[
\boxed{
\Psi_h\neq\Phi_h.
}
\]

The numerical method therefore defines its own discrete dynamical system.

## D2. Explicit Euler

Taylor expansion of the exact solution gives

\[
x(t+h)
=
x(t)
+
h f(x(t))
+
O(h^2).
\]

Dropping the higher-order term gives explicit Euler:

\[
\boxed{
x_{n+1}
=
x_n+h f(x_n).
}
\]

The method evaluates the vector field only at the current state.

## D3. Implicit Euler

Backward expansion about the new state motivates

\[
\boxed{
x_{n+1}
=
x_n+h f(x_{n+1}).
}
\]

The new state appears on both sides.

Each step can therefore require solving a nonlinear or linear system.

Implicitness changes computational cost and stability properties.

It does not automatically increase formal order.

## D4. Local defect and global error

Let the exact sampled solution be

\[
y_n=x(t_n).
\]

Define the one-step defect by inserting the exact state into the numerical method:

\[
d_{n+1}
=
\Phi_h(y_n)
-
\Psi_h(y_n).
\]

If

\[
\|d_{n+1}\|
\le
K h^{p+1},
\]

the method has local defect of order \(p+1\).

Suppose additionally the one-step map obeys a finite-time Lipschitz stability bound

\[
\|\Psi_h(u)-\Psi_h(v)\|
\le
(1+Ch)\|u-v\|.
\]

Writing

\[
e_n=y_n-x_n,
\]

we obtain

\[
\begin{aligned}
\|e_{n+1}\|
&=
\|\Phi_h(y_n)-\Psi_h(x_n)\|\\
&\le
\|\Phi_h(y_n)-\Psi_h(y_n)\|
+
\|\Psi_h(y_n)-\Psi_h(x_n)\|\\
&\le
K h^{p+1}
+
(1+Ch)\|e_n\|.
\end{aligned}
\]

Discrete Grönwall reasoning on a fixed interval

\[
nh\le T
\]

then gives

\[
\|e_n\|
=
O(h^p)
\]

under the declared regularity/stability assumptions.

Thus local and global orders differ by one power in this standard one-step setting.

Consistency alone is not asserted as a universal convergence theorem.

## D5. Scalar test equation

Consider

\[
y'=\lambda y.
\]

The exact one-step amplification is

\[
y(t+h)
=
e^{h\lambda}y(t).
\]

Define

\[
z=h\lambda.
\]

Then

\[
R_{\rm exact}(z)=e^z.
\]

A numerical method applied to the test equation has form

\[
y_{n+1}
=
R(z)y_n.
\]

The function \(R\) is its amplification factor.

Absolute stability at \(z\) means

\[
|R(z)|<1.
\]

This is a property of the numerical update on the test equation.

It is not the same statement as Lyapunov stability of a general nonlinear ODE.

## D6. Explicit Euler stability

Explicit Euler gives

\[
y_{n+1}
=
y_n+h\lambda y_n
=
(1+z)y_n.
\]

Therefore

\[
\boxed{
R_E(z)=1+z.
}
\]

Its absolute-stability region is

\[
\boxed{
|1+z|<1.
}
\]

This is the open disk centered at \(-1\) with radius \(1\).

On the negative real axis,

\[
-2<z<0.
\]

For

\[
\lambda<0,
\]

the step-size condition is therefore

\[
0<h<\frac{2}{|\lambda|}.
\]

## D7. Implicit Euler stability

Implicit Euler gives

\[
y_{n+1}
=
y_n+h\lambda y_{n+1}.
\]

Thus

\[
(1-z)y_{n+1}
=
y_n,
\]

so

\[
\boxed{
R_I(z)
=
\frac{1}{1-z}.
}
\]

If

\[
z=x+iy
\]

with

\[
x<0,
\]

then

\[
|1-z|^2
=
(1-x)^2+y^2
>
1.
\]

Hence

\[
|R_I(z)|<1
\]

for the entire open left half-plane.

Implicit Euler is therefore A-stable on the scalar test equation.

## D8. Consistency witness for explicit Euler

The exact amplification has expansion

\[
e^z
=
1+z+\frac{z^2}{2}
+\frac{z^3}{6}
+\cdots.
\]

Explicit Euler uses

\[
1+z.
\]

Therefore

\[
e^z-(1+z)
=
\frac{z^2}{2}
+
O(z^3).
\]

Since

\[
z=h\lambda,
\]

the one-step defect is

\[
O(h^2)
\]

for fixed \(\lambda\).

Under the standard finite-time stability assumptions above, this yields first-order global convergence.

## D9. Exact stiff calibration system

Consider

\[
\dot x
=
\begin{pmatrix}
-1&0\\
0&-100
\end{pmatrix}
x.
\]

The exact modes are

\[
e^{-t}
\]

and

\[
e^{-100t}.
\]

Both decay.

Explicit Euler has modal amplification factors

\[
R_{\rm slow}=1-h,
\]

and

\[
R_{\rm fast}=1-100h.
\]

The fast mode requires

\[
|1-100h|<1.
\]

Hence

\[
0<h<0.02.
\]

At

\[
h=0.03,
\]

\[
R_{\rm slow}=0.97,
\]

but

\[
R_{\rm fast}=-2.
\]

The exact fast mode decays by

\[
e^{-3}
\approx
0.049787.
\]

The explicit numerical fast mode doubles in magnitude and flips sign each step.

## D10. Implicit Euler on the stiff witness

Implicit Euler gives

\[
R_{\rm slow}
=
\frac{1}{1+h},
\]

and

\[
R_{\rm fast}
=
\frac{1}{1+100h}.
\]

At

\[
h=0.03,
\]

\[
R_{\rm slow}
=
\frac{1}{1.03}
\approx
0.970874,
\]

and

\[
\boxed{
R_{\rm fast}
=
\frac14.
}
\]

The fast mode is numerically stable.

But compare:

\[
e^{-3}
\approx
0.049787
\]

versus

\[
\frac14
=
0.25.
\]

The step is stable while substantially misrepresenting the fast transient.

Thus

\[
\boxed{
\text{stability}
\neq
\text{accuracy}.
}
\]

## D11. Stiffness interpretation

The calibration system contains two decay timescales:

\[
\tau_{\rm slow}=1,
\]

and

\[
\tau_{\rm fast}=0.01.
\]

A method may need a step size governed by the fast stable mode even when the scientific behavior of interest evolves on the slow scale.

This mismatch between dynamical timescales and explicit stability restrictions is the central numerical phenomenon illustrated here.

Stiffness has several formal characterizations across numerical analysis.

The Atlas uses the term only with the problem/method context stated.

## D12. Harmonic oscillator: explicit Euler

For

\[
\dot q=p,
\qquad
\dot p=-q,
\]

explicit Euler gives

\[
\begin{pmatrix}
q_{n+1}\\
p_{n+1}
\end{pmatrix}
=
M_E
\begin{pmatrix}
q_n\\
p_n
\end{pmatrix},
\]

with

\[
M_E
=
\begin{pmatrix}
1&h\\
-h&1
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{
\det M_E
=
1+h^2
>
1
}
\]

for nonzero \(h\).

The exact oscillator flow is symplectic and area-preserving.

Explicit Euler is not.

## D13. Harmonic oscillator: symplectic Euler

Use the update order

\[
p_{n+1}
=
p_n-hq_n,
\]

then

\[
q_{n+1}
=
q_n+h p_{n+1}.
\]

The resulting matrix is

\[
M_{SE}
=
\begin{pmatrix}
1-h^2&h\\
-h&1
\end{pmatrix}.
\]

Its determinant is

\[
\det M_{SE}=1.
\]

For the canonical two-dimensional matrix

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

direct multiplication gives

\[
\boxed{
M_{SE}^\top J M_{SE}=J.
}
\]

Thus this update is symplectic.

## D14. Symplectic does not mean exact-energy preserving

Start from

\[
(q_0,p_0)=(1,0).
\]

One symplectic-Euler step gives

\[
p_1=-h,
\]

and

\[
q_1=1-h^2.
\]

The original oscillator energy is

\[
H_0=\frac12.
\]

The new energy is

\[
H_1
=
\frac12
\left[
(1-h^2)^2+h^2
\right].
\]

Therefore

\[
H_1-H_0
=
\frac12(-h^2+h^4).
\]

This is nonzero for generic nonzero \(h\).

So

\[
\boxed{
\text{symplectic}
\not\Rightarrow
\text{exact energy conservation}.
}
\]

The value of symplectic integration lies in preserving phase-space structure and often favorable long-time qualitative behavior, not in exactly conserving every Hamiltonian at every step.

## D15. Operator splitting

Suppose the evolution generator decomposes as

\[
A+B.
\]

The exact linear flow is

\[
e^{h(A+B)}.
\]

If the individual flows are easier to compute, one can compose them.

Lie-Trotter splitting is

\[
\boxed{
\Psi^{LT}_h
=
e^{hA}e^{hB}.
}
\]

A symmetric Strang step is

\[
\boxed{
\Psi^{S}_h
=
e^{hA/2}
e^{hB}
e^{hA/2}.
}
\]

## D16. Commuting case

If

\[
[A,B]
=
AB-BA
=
0,
\]

then the exponentials commute and

\[
\boxed{
e^{h(A+B)}
=
e^{hA}e^{hB}.
}
\]

Lie splitting is exact in this linear commuting case.

The splitting error therefore measures more than step size.

It also measures noncommutativity.

## D17. Exact noncommuting witness

Take

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

and

\[
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

Their commutator is

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

Thus the split components do not commute.

## D18. Lie defect

Because

\[
e^{hA}=I+hA,
\]

and

\[
e^{hB}=I+hB,
\]

the Lie step is

\[
e^{hA}e^{hB}
=
I+h(A+B)+h^2AB.
\]

The exact exponential satisfies

\[
e^{h(A+B)}
=
I+h(A+B)
+\frac{h^2}{2}(A+B)^2
+O(h^3).
\]

Since

\[
(A+B)^2=AB+BA,
\]

the second-order difference is

\[
h^2
\left(
AB-\frac12(AB+BA)
\right)
=
\frac{h^2}{2}[A,B].
\]

Therefore

\[
\boxed{
e^{hA}e^{hB}
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3).
}
\]

For the declared witness, symbolic replay gives leading diagonal defect

\[
\frac{h^2}{2}
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

## D19. Strang defect

The symmetric step is

\[
e^{hA/2}e^{hB}e^{hA/2}.
\]

For the same witness, exact symbolic expansion gives

\[
\Psi^S_h-e^{h(A+B)}
=
h^3
\begin{pmatrix}
0&1/12\\
-1/6&0
\end{pmatrix}
+
O(h^4).
\]

Thus the local defect begins at

\[
\boxed{
O(h^3).
}
\]

Under standard repeated-step stability/regularity assumptions, this corresponds to second-order global accuracy.

The symmetry cancels the \(O(h^2)\) local defect present in Lie-Trotter splitting.

## D20. Why commutators matter

If

\[
[A,B]\neq0,
\]

the order in which subflows are applied matters.

The commutator measures the leading failure of interchangeability.

This connects numerical analysis to later Atlas themes:

- split neural operators;
- routing order;
- optimizer component coupling;
- lifted commutator diagnostics;
- SPINDLE-style computation.

The present chapter establishes the numerical mechanism only.

## D21. Adaptive step intuition

If local error grows with step size or with changing local dynamics, a fixed \(h\) can be wasteful in easy regions and unsafe in difficult ones.

Adaptive stepping uses an error estimate to adjust \(h\).

The conceptual loop is:

1. propose a step;
2. estimate local error;
3. accept/reject or rescale;
4. continue.

Later adaptive-depth chapters reinterpret this pattern in computational-depth terms.

This chapter does not yet specify a learned depth controller.

## D22. Numerical stability terminology

The word "stability" is overloaded.

This chapter uses at least three distinct notions:

1. **dynamical stability**:
   property of the underlying continuous/discrete system;
2. **absolute stability**:
   bounded decay/amplification behavior of a numerical method on the scalar test equation;
3. **algorithmic/backward stability**:
   sensitivity of a numerical algorithm to perturbations and whether the computed result solves a nearby problem.

These should not be silently interchanged.

## Claim boundary

This packet establishes standard finite-dimensional ODE discretization, absolute-stability, stiffness, structure-preservation, and linear splitting identities in declared settings.

It does not establish that a neural layer is literally an ODE step, that implicit architectures are automatically superior, or that split neural computation inherits a numerical order theorem without matching the theorem's assumptions.
