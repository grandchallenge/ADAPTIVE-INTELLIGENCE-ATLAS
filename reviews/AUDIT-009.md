# AUDIT-009 — Discretization, Stability, and Splitting

## Disposition

**PASS AFTER ONE STABILITY-CONVENTION REPAIR**

\`ATLAS-CH-NUMERICS-001\` remains at \`draft-v0.1\`.

The chapter's error analysis, Euler stability calculations, stiff witness, splitting algebra, source scope, and figure provenance pass audit.

AUDIT-009 found one terminology/convention ambiguity:

> the chapter used strict \(|R(z)|<1\) for asymptotic decay and called that the absolute-stability region, then used the open left half-plane to justify A-stability.

The calculations were correct, but the standard numerical-analysis convention is clearer if the non-growth stability set is written

\[
\mathcal S=\{z:|R(z)|\le1\},
\]

while strict

\[
|R(z)|<1
\]

is reserved for asymptotic decay of the scalar discrete mode.

The specification, derivation packet, manuscript, source lock, and figure metadata now make this distinction explicit.

No numerical witness changed.

## Audited baseline

- NUMERICS-001 merge:
  \`b7d8b8716cd4079e679311cc75bb1ad2f77cee21\`;
- audit issue:
  \`#46\`;
- chapter:
  \`ATLAS-CH-NUMERICS-001\`.

## 1. Exact flow versus numerical update

PASS.

The chapter distinguishes the exact transport

\[
\Phi_h
\]

from the numerical one-step map

\[
\Psi_h.
\]

It explicitly treats

\[
\Phi_h\ne\Psi_h
\]

as the generic case.

The chapter also states that the numerical method defines a distinct discrete dynamical system whose stability, invariants, and long-time behavior may differ from the exact flow.

## 2. Local defect versus global error

PASS.

The local defect is defined by starting one step from the exact state:

\[
\delta_{n+1}
=
\Phi_h(t_n,x(t_n))
-
\Psi_h(t_n,x(t_n)).
\]

The global error is

\[
e_n=x(t_n)-x_n.
\]

The manuscript does not claim that consistency alone implies convergence.

It states the bounded one-step result correctly:

- local defect:
  \[
  O(h^{p+1});
  \]
- suitable finite-time Lipschitz error propagation / stability;
- global error:
  \[
  O(h^p).
  \]

This is appropriately scoped to the required smoothness and stability assumptions.

## 3. Explicit Euler

PASS AFTER CONVENTION REPAIR.

For

\[
y'=\lambda y,
\qquad
z=h\lambda,
\]

explicit Euler gives

\[
R_{\rm EE}(z)=1+z.
\]

The standard non-growth absolute-stability set is now written

\[
|1+z|\le1.
\]

Strict asymptotic decay uses

\[
|1+z|<1.
\]

Thus the stability set is the closed disk centered at \(-1\) with radius \(1\), while its interior gives strict decay.

## 4. Implicit Euler

PASS AFTER CONVENTION REPAIR.

Implicit Euler gives

\[
R_{\rm IE}(z)
=
\frac{1}{1-z}.
\]

The standard non-growth condition is

\[
|R_{\rm IE}(z)|\le1,
\]

equivalently

\[
|1-z|\ge1.
\]

Every point in the closed left half-plane satisfies this condition.

For

\[
\operatorname{Re}z<0,
\]

the inequality is strict, so the scalar mode decays asymptotically.

The chapter can therefore state A-stability using the standard closed-half-plane convention without conflating it with strict decay.

## 5. L-stability

PASS.

For implicit Euler,

\[
R_{\rm IE}(z)=\frac{1}{1-z}.
\]

As

\[
|z|\to\infty
\]

within the left half-plane,

\[
R_{\rm IE}(z)\to0.
\]

Together with A-stability, this supports the chapter's L-stability statement.

The claim remains specific to the method/test-equation stability function.

## 6. Stiff scalar witness

PASS.

The merged chapter uses

\[
y'=-100y,
\qquad
h=0.05.
\]

Therefore

\[
z=-5.
\]

Independent replay gives:

\[
e^{-5}
\approx
0.006737946999,
\]

\[
R_{\rm EE}(-5)=-4,
\]

and

\[
R_{\rm IE}(-5)=\frac16.
\]

Thus:

- explicit Euler is unstable at the declared step;
- implicit Euler is stable;
- implicit Euler is substantially inaccurate for that one fast transient.

The chapter correctly freezes

\[
\text{stability}
\ne
\text{accuracy}.
\]

## 7. Stiffness scope

PASS.

The manuscript explicitly rejects the shorthand

> stiffness = large derivative.

It uses an operational problem/method-relative description involving rapidly decaying modes that impose step restrictions much smaller than the slower behavior of interest would otherwise require.

The source lock likewise states that stiffness is problem/method-relative.

## 8. Lie–Trotter commutator algebra

PASS.

For

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
\end{pmatrix},
\]

independent replay gives

\[
[A,B]
=
AB-BA
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

For the declared ordering

\[
S_{\rm LT}(h)
=
e^{hA}e^{hB},
\]

independent symbolic replay gives the exact \(h^2\) coefficient

\[
\frac12[A,B].
\]

Therefore

\[
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3)
\]

with the stated sign and ordering convention.

## 9. Commuting case

PASS.

For constant bounded matrices with

\[
[A,B]=0,
\]

the chapter states

\[
e^{hA}e^{hB}
=
e^{h(A+B)}.
\]

This is exact.

The manuscript does not generalize this finite-dimensional statement to arbitrary unbounded operators without domain assumptions.

## 10. Strang splitting

PASS.

For

\[
S_{\rm S}(h)
=
e^{hA/2}
e^{hB}
e^{hA/2},
\]

independent symbolic replay gives zero \(h^2\) coefficient.

For the exact witness, the \(h^3\) coefficient is

\[
\begin{pmatrix}
0&1/12\\
-1/6&0
\end{pmatrix}.
\]

Thus the first nonzero local defect is cubic:

\[
O(h^3).
\]

The chapter keeps the second-order global conclusion conditional on the usual repeated-step stability and regularity assumptions.

## 11. Structure-preserving claims

PASS.

The merged chapter does **not** contain the symplectic-Euler matrix claim listed in the initial AUDIT-009 issue.

That checklist item came from a parallel pre-merge draft and is inapplicable to the actual merged chapter.

The merged manuscript makes the narrower established statement:

> a composition of symplectic subflows is symplectic.

It also explicitly requires every "structure-preserving" claim to name the structure being preserved.

No repair is required.

## 12. Backward-error scope

PASS.

The chapter introduces backward error analysis only as a later viewpoint:

> ask whether the discrete path can be interpreted through nearby modified dynamics.

It does not claim an exact globally convergent modified equation for every method.

## 13. Neural-computation boundary

PASS.

The chapter repeatedly separates numerical theorem from ML analogy.

It states that:

- a residual layer can admit an integrator interpretation without being a literal ODE step;
- adaptive depth as error control is a research programme;
- split neural modules inherit splitting theory only after an underlying evolution/operator model and required assumptions are declared;
- a scalar stability region is a diagnostic object, not a nonlinear certificate.

No numerical order or stability theorem is promoted automatically to an arbitrary learned architecture.

## 14. External source scope

PASS.

The merged source lock uses:

### Iserles 2008

Consistency, convergence, one-step methods, and numerical stability.

### Hairer–Wanner 1996

Stiff systems, implicit methods, and absolute-stability reasoning.

### McLachlan–Quispel 2002

Splitting/composition methods and structure-preserving applications.

### Hairer–Lubich–Wanner 2006

Geometric/structure-preserving integration as a bounded handoff.

The chapter does not use these sources as authority for Atlas-specific claims about adaptive depth or learned computation.

## 15. Bibliography closure

PASS.

The canonical bibliography contains:

- \`Iserles2008\`;
- \`HairerWanner1996\`;
- \`McLachlanQuispel2002\`;
- \`HairerLubichWanner2006\`.

All reader-facing chapter citations resolve.

## 16. Atlas provenance

PASS.

Pinned audited Dynamics manuscript:

\`a2a908264d119ef44c502f53f32798b83e16696d\`.

Pinned source inventory:

\`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

Both match the source-lock records.

## 17. Figure provenance

PASS.

\`ATLAS-FIG-NUMERICS-001\` uses:

- generator:
  \`figures/wolfram/ATLAS-FIG-NUMERICS-001.wl\`;
- generator Git blob:
  \`c7095b46e2ab622eba1e06cc2a19fa6d83e7fa84\`;
- rendered master:
  \`figures/masters/ATLAS-FIG-NUMERICS-001.png\`;
- rendered Git blob:
  \`7f23da82f51ac006cccf1be2e055b06ac8a2b715\`;
- rendered bytes:
  \`46,057\`.

The audit changes only the figure's textual stability semantics:

- standard non-growth sets include their boundaries;
- shaded strict interiors/exteriors denote asymptotic decay.

The rendered geometry itself is unchanged.

Repository validation recomputes the recorded source/master Git blob identities and rendered byte count.

## 18. Chapter status

PASS.

\`ATLAS-CH-NUMERICS-001\` remains:

\`draft-v0.1\`.

Its hard prerequisite remains:

- \`ATLAS-CH-DYN-001\`.

## 19. Final disposition

AUDIT-009 passes after one numerical-stability convention repair.

The chapter now cleanly distinguishes:

\[
\text{exact flow}
\ne
\text{numerical map},
\]

\[
\text{local defect}
\ne
\text{global error},
\]

\[
\text{absolute non-growth}
\ne
\text{strict asymptotic decay},
\]

\[
\text{stable}
\ne
\text{accurate},
\]

and

\[
\text{module composition}
\ne
\text{numerical splitting theorem without declared assumptions}.
\]

After this audit merges, the dependency graph may be recomputed from current \`main\` to choose the next Numerics-enabled chapter by transitive unlock value.
