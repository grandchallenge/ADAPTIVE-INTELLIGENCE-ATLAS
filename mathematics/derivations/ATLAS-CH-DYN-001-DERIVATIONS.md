# ATLAS-CH-DYN-001 — Derivation Packet

## D1. Vector field, trajectory, and flow

Consider the autonomous ODE

\[
\dot x=f(x),
\qquad
x(0)=x_0.
\]

The vector field \(f\) assigns a local velocity to each state.

A trajectory is one solution

\[
t\mapsto x(t;x_0).
\]

Where existence and uniqueness hold, define the flow map

\[
\Phi_t(x_0)=x(t;x_0).
\]

For an autonomous true flow,

\[
\boxed{
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
}
\]

The composition identity is understood only wherever all maps are defined; in a one-sided forward semiflow it is restricted to \(s,t\ge0\).

A sampled trajectory is not the same object as the flow law.

A numerical update is not automatically the exact flow map.

## D1a. Constant linear flow

For

\[
\dot x=Ax
\]

with constant matrix \(A\), define

\[
e^{tA}
=
\sum_{k=0}^{\infty}
\frac{(tA)^k}{k!}.
\]

Termwise differentiation gives

\[
\frac{d}{dt}e^{tA}
=
Ae^{tA},
\]

and

\[
e^{0A}=I.
\]

Hence

\[
x(t)
=
e^{tA}x_0
\]

satisfies the initial-value problem.

This matrix-exponential construction is introduced here; it is not imported as a documented result from the upstream Linear Algebra manuscript.

## D2. Equilibrium and linearization

An equilibrium \(x_\star\) satisfies

\[
f(x_\star)=0.
\]

Let

\[
x=x_\star+\delta.
\]

If \(f\) is differentiable,

\[
f(x_\star+\delta)
=
J_f(x_\star)\delta
+
o(\|\delta\|).
\]

Hence locally

\[
\dot\delta
=
J_f(x_\star)\delta
+
o(\|\delta\|).
\]

The little-\(o\) estimate requires only differentiability at the equilibrium. Upgrading it to \(O(\|\delta\|^2)\) requires stronger regularity, for example a locally Lipschitz Jacobian.

For a hyperbolic equilibrium:

- if all eigenvalues of \(J_f(x_\star)\) have strictly negative real part, the equilibrium is locally exponentially stable;
- if at least one eigenvalue has positive real part, the equilibrium is unstable.

If one or more eigenvalues have zero real part, the linearization alone can be inconclusive.

## D3. Lyapunov stability

For an equilibrium at the origin, a continuously differentiable function \(V\) can certify stability when it is positive definite and its orbital derivative

\[
\dot V(x)
=
\nabla V(x)^\top f(x)
\]

has the required sign.

A standard local result is:

\[
V(x)>0
\]

for \(x\neq0\) near the origin and

\[
\dot V(x)<0
\]

for \(x\neq0\) in that neighborhood imply local asymptotic stability.

Global conclusions require stronger global hypotheses.

## D4. Exact scalar stable flow

Consider

\[
\dot x=-2x,
\qquad
x(0)=3.
\]

The exact solution is

\[
\boxed{
x(t)=3e^{-2t}.
}
\]

Choose

\[
V(x)=\frac12x^2.
\]

Then

\[
\dot V
=
x\dot x
=
-2x^2.
\]

Thus

\[
\dot V<0
\]

for every nonzero \(x\), and the origin is exponentially stable.

## D5. Saddle-node normal form

Consider

\[
\dot x
=
\mu-x^2.
\]

Equilibria satisfy

\[
\mu-x^2=0.
\]

For

\[
\mu>0,
\]

there are two real equilibria:

\[
x_\pm
=
\pm\sqrt{\mu}.
\]

For

\[
\mu=0,
\]

the two equilibria collide at

\[
x=0.
\]

For

\[
\mu<0,
\]

there are no real equilibria.

The derivative is

\[
f'(x)
=
-2x.
\]

Therefore for \(\mu>0\),

\[
f'(+\sqrt{\mu})
=
-2\sqrt{\mu}<0,
\]

so the positive branch is locally stable.

And

\[
f'(-\sqrt{\mu})
=
2\sqrt{\mu}>0,
\]

so the negative branch is unstable.

The collision at \(\mu=0\) is nonhyperbolic.

## D6. Pitchfork normal form

Consider

\[
\dot x
=
\mu x-x^3.
\]

Equilibria satisfy

\[
x(\mu-x^2)=0.
\]

Thus

\[
x_0=0
\]

always exists.

For

\[
\mu>0,
\]

two additional equilibria appear:

\[
x_\pm
=
\pm\sqrt{\mu}.
\]

The derivative is

\[
f'(x)
=
\mu-3x^2.
\]

At the origin,

\[
f'(0)=\mu.
\]

Hence:

- \(x=0\) is locally stable for \(\mu<0\);
- \(x=0\) is unstable for \(\mu>0\).

At the nonzero branches,

\[
f'(\pm\sqrt{\mu})
=
-2\mu<0
\]

for \(\mu>0\).

Thus both nonzero branches are locally stable.

## D7. Hopf normal form handoff

A standard supercritical Hopf normal form in polar coordinates is

\[
\dot r
=
\mu r-r^3,
\]

\[
\dot\theta
=
\omega,
\qquad
\omega\neq0.
\]

The radial equilibria satisfy

\[
r(\mu-r^2)=0.
\]

For

\[
\mu<0,
\]

the origin is radially stable.

For

\[
\mu>0,
\]

the origin becomes unstable and a nonzero stable radius appears:

\[
r_\star=\sqrt{\mu}.
\]

The corresponding Cartesian trajectory is periodic.

This packet uses the normal form illustratively.

It does not prove the general Hopf bifurcation theorem.

## D8. Hamiltonian dynamics

In canonical coordinates

\[
z=
\begin{pmatrix}
q\\
p
\end{pmatrix},
\]

define

\[
J
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

For Hamiltonian \(H(q,p)\),

\[
\boxed{
\dot z
=
J\nabla H(z).
}
\]

The Hamiltonian derivative along the exact flow is

\[
\frac{dH}{dt}
=
\nabla H^\top J\nabla H.
\]

Since \(J^\top=-J\),

\[
v^\top Jv=0
\]

for every real vector \(v\).

Therefore

\[
\boxed{
\frac{dH}{dt}=0
}
\]

for an autonomous canonical Hamiltonian system.

## D9. Harmonic oscillator

Take

\[
H(q,p)
=
\frac12(q^2+p^2).
\]

Then

\[
\nabla H
=
\begin{pmatrix}
q\\
p
\end{pmatrix},
\]

so

\[
\dot q=p,
\]

\[
\dot p=-q.
\]

The system matrix is

\[
A=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

Since

\[
A^2=-I,
\]

the exact matrix exponential is

\[
\boxed{
M(t)
=
e^{tA}
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
}
\]

Thus

\[
z(t)=M(t)z(0).
\]

## D10. Symplectic identity

For the canonical matrix \(J\),

\[
M(t)^\top J M(t)
=
J.
\]

Therefore the exact harmonic-oscillator flow is symplectic.

Direct symbolic replay gives

\[
M(t)^\top J M(t)-J
=
0.
\]

The energy is also exactly conserved:

\[
H(M(t)z)
-
H(z)
=
0.
\]

Symplecticity and energy conservation are related structural facts here, but they are not identical properties in general numerical methods.

## D11. Continuous flow versus discrete update

Suppose a numerical method produces

\[
x_{n+1}
=
\Psi_h(x_n).
\]

Even if

\[
\Psi_h(x)
=
\Phi_h(x)
+
O(h^{p+1}),
\]

the numerical map \(\Psi_h\) is a different dynamical system from the exact flow map \(\Phi_h\).

It can have different:

- fixed points;
- stability region;
- conserved quantities;
- invariant measures;
- long-time geometry.

This distinction is the entry point to \`ATLAS-CH-NUMERICS-001\`.

## D12. Relevance to neural computation

A depth-indexed residual architecture may admit the heuristic form

\[
x_{k+1}
=
x_k+h f_k(x_k).
\]

If

\[
f_k=f
\]

and the step is interpreted consistently, this resembles an explicit Euler discretization of

\[
\dot x=f(x).
\]

But generic neural layers may vary with \(k\), contain discontinuities, stochasticity, normalization, attention state, or other structure incompatible with one autonomous ODE.

Thus:

\[
\boxed{
\text{flow interpretation}
\neq
\text{literal autonomous ODE identity}.
}
\]

## Claim boundary

This packet establishes standard deterministic continuous-time dynamical-systems facts and exact toy witnesses.

It does not claim that arbitrary neural architectures are exact flows, that local linearization determines global behavior, or that a numerical discretization inherits the qualitative structure of its continuous model automatically.
