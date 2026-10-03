# Chapter Specification — ATLAS-CH-NUMERICS-001

## Identity

**Title:** Discretization, Stability, and Splitting  
**Part:** Mathematical Substrate  
**Status:** specification-ready.  
**Epistemic class:** Established Numerical Analysis + Atlas Derivation + Atlas Interpretation.

## Chapter contract

Develop the minimum numerical-analysis language required to reason about computation as an approximation to evolution.

The chapter must establish:

- exact flow versus numerical update;
- local versus global error;
- consistency;
- explicit and implicit one-step methods;
- absolute stability;
- stiffness;
- step-size constraints;
- structure preservation;
- Lie-Trotter splitting;
- Strang splitting;
- commutators as leading noncommutativity signals.

It must not become a general ODE-solver handbook.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-DYN-001\`.

May assume:

- exact flows;
- equilibria and continuous/discrete stability distinction;
- matrix exponentials for constant linear systems;
- Hamiltonian/symplectic language;
- basic operator norms and matrix algebra.

Must not assume:

- adaptive-depth policy;
- SPINDLE-specific architecture;
- Krylov methods;
- general PDE discretization;
- learned preconditioners.

## Reader outcome

A reader should be able to:

1. distinguish an exact time-\(h\) flow \(\Phi_h\) from a numerical update \(\Psi_h\);
2. distinguish local truncation error from accumulated global error;
3. derive explicit and implicit Euler from the ODE;
4. derive their scalar amplification factors;
5. compute absolute-stability regions on the test equation;
6. explain why a stable continuous mode can become numerically unstable;
7. explain stiffness as a timescale/stability constraint rather than merely a large derivative;
8. show why implicit Euler is A-stable on the scalar test equation;
9. separate stability from accuracy;
10. derive Lie-Trotter and Strang compositions;
11. identify the commutator as the first obstruction to exact factorization;
12. explain why symplecticity and energy preservation are different;
13. understand why numerical method choice can change the qualitative computation.

## Formal spine

### Exact flow and one-step method

For

\[
\dot x=f(x),
\]

let

\[
\Phi_h(x)
\]

be the exact time-\(h\) flow.

A numerical one-step method defines

\[
x_{n+1}
=
\Psi_h(x_n).
\]

In general,

\[
\Phi_h
\neq
\Psi_h.
\]

### Local defect

Starting from exact state \(x(t_n)\), define one-step defect

\[
d_{n+1}
=
\Phi_h(x(t_n))
-
\Psi_h(x(t_n)).
\]

For a method of order \(p\),

\[
d_{n+1}
=
O(h^{p+1}).
\]

Under standard regularity/stability assumptions on a fixed finite time interval, global error is

\[
O(h^p).
\]

Do not state consistency alone as a universal convergence theorem.

### Explicit Euler

\[
x_{n+1}
=
x_n+h f(x_n).
\]

### Implicit Euler

\[
x_{n+1}
=
x_n+h f(x_{n+1}).
\]

The implicit step requires a solve.

### Scalar test equation

Use

\[
y'=\lambda y.
\]

Let

\[
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

Implicit Euler:

\[
R_I(z)=\frac{1}{1-z}.
\]

Absolute stability requires

\[
|R(z)|<1.
\]

Thus explicit Euler is stable in

\[
|1+z|<1,
\]

the disk centered at \(-1\) with radius \(1\).

For implicit Euler, if

\[
\operatorname{Re}z<0,
\]

then

\[
|1-z|>1,
\]

hence

\[
|R_I(z)|<1.
\]

This establishes A-stability for the scalar left half-plane.

## Exact stiffness witness

Use

\[
\dot x
=
\begin{pmatrix}
-1&0\\
0&-100
\end{pmatrix}
x.
\]

For explicit Euler,

\[
R_{\rm slow}=1-h,
\qquad
R_{\rm fast}=1-100h.
\]

Along the negative real axis, stability requires

\[
0<h<\frac{2}{100}=0.02
\]

because of the fast mode.

At

\[
h=0.03,
\]

the slow amplification is

\[
0.97,
\]

but the fast amplification is

\[
-2,
\]

so the fast numerical mode diverges even though both exact modes decay.

Implicit Euler gives

\[
R_{\rm slow}=\frac{1}{1+h},
\qquad
R_{\rm fast}=\frac{1}{1+100h}.
\]

At \(h=0.03\),

\[
R_{\rm fast}=\frac14.
\]

The step is stable but not necessarily accurate for the fast transient.

## Consistency witness

For the scalar test equation,

\[
e^z
=
1+z+\frac{z^2}{2}+O(z^3).
\]

Explicit Euler uses

\[
1+z.
\]

Therefore the one-step amplification defect is

\[
\frac{z^2}{2}+O(z^3),
\]

corresponding to local error \(O(h^2)\) and first-order global convergence under standard assumptions.

## Structure-preservation bridge

For harmonic oscillator

\[
\dot q=p,
\qquad
\dot p=-q,
\]

explicit Euler has matrix

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
\det M_E=1+h^2>1.
\]

Thus it is not symplectic and expands phase-space area.

One symplectic-Euler variant,

\[
p_{n+1}=p_n-hq_n,
\]

\[
q_{n+1}=q_n+h p_{n+1},
\]

has update matrix

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
\det M_{SE}=1.
\]

In two canonical dimensions this verifies symplecticity.

Do not claim exact energy conservation.

## Splitting

Suppose

\[
\dot x=(A+B)x.
\]

Exact flow:

\[
e^{h(A+B)}.
\]

Lie-Trotter step:

\[
\Psi^{LT}_h
=
e^{hA}e^{hB}.
\]

Strang step:

\[
\Psi^{S}_h
=
e^{hA/2}e^{hB}e^{hA/2}.
\]

If

\[
[A,B]=AB-BA=0,
\]

then

\[
e^{h(A+B)}
=
e^{hA}e^{hB}
\]

exactly.

For noncommuting \(A,B\), use the expansion

\[
e^{hA}e^{hB}
=
e^{h(A+B)}
+
\frac{h^2}{2}[A,B]
+
O(h^3)
\]

at the level of the direct series difference for the declared ordering.

Strang cancels the second-order asymmetry and has local defect

\[
O(h^3)
\]

under the usual regularity assumptions.

## Exact splitting witness

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
A^2=B^2=0,
\]

and

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\neq0.
\]

Use exact symbolic series to verify:

- Lie defect begins at order \(h^2\);
- Strang defect begins at order \(h^3\).

## Principal pedagogical device

### Allegory: road versus stepping stones

The exact flow is a continuous road through state space.

A numerical method lays down stepping stones.

Correspondence:

- exact flow:
  the road prescribed by the differential equation;
- numerical update:
  one rule for placing the next stone;
- step size:
  spacing between stones;
- local error:
  miss at one step starting from the true road;
- global error:
  accumulated displacement after many stones;
- stability region:
  parameter range in which repeated stepping does not amplify modes the method is meant to damp.

Limit:

A numerical method is not merely a coarser drawing of the same trajectory. It is a distinct discrete dynamical system and can create, destroy, or distort qualitative structure.

## Figure programme

### ATLAS-FIG-NUMERICS-001

Three panels:

1. explicit- and implicit-Euler absolute-stability geometry in the complex \(z=h\lambda\) plane;
2. stiff fast-mode trajectories for exact, explicit Euler, and implicit Euler at \(h=0.03\);
3. log-log splitting defect for the exact \(2\times2\) noncommuting witness, showing Lie \(O(h^2)\) and Strang \(O(h^3)\) local slopes.

Representation class:
computed from declared exact formulas/matrices; styling and sampled plot ranges are nonliteral.

## Counterexamples and failure boundaries

Include:

- exact stable ODE but unstable explicit Euler step;
- stable implicit step that is too inaccurate to resolve the fast transient;
- consistency without a blanket convergence claim;
- determinant one is not generally sufficient for symplecticity above two dimensions;
- symplectic does not mean exact energy-preserving;
- commuting split operators make Lie splitting exact;
- noncommuting operators create commutator-controlled error;
- step size can change the qualitative discrete dynamics.

## Downstream obligations

Direct consumers include:

- \`ATLAS-CH-DEPTH-001\`;
- \`ATLAS-CH-SPLIT-001\`;
- \`ATLAS-CH-NETNUM-001\`;
- later adaptive stepping, transport, and structure-preserving optimization chapters.

## Sources

- [@Butcher2016]
- [@HairerNorsettWanner1993]
- [@HairerWanner1996]
- [@HairerLubichWanner2006]
- [@Higham2002]

Source lock:
\`sources/source-locks/ATLAS-CH-NUMERICS-001.yaml\`.

## Acceptance

The draft must:

- distinguish exact flow from numerical map;
- distinguish local/global error;
- derive explicit/implicit Euler amplification factors;
- derive their scalar absolute-stability conditions;
- include the exact stiff-system witness;
- separate stability from accuracy;
- include the harmonic-oscillator structure-preservation bridge;
- derive commuting versus noncommuting splitting behavior;
- verify Lie and Strang defect orders on the exact matrix witness;
- include one pedagogical allegory with an explicit limit;
- include source lock, witness, and figure provenance.
