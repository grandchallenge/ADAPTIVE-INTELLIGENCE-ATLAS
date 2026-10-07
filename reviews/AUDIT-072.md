# AUDIT-072 — Variational and Divergence-Derived Optimization

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-VARIOPT-001 remains at draft-v0.1.

The audit found no mathematical, dependency, external-source, programme-authority, provenance, witness, divergence-geometry, variational, symplectic, MODULUS-boundary, or repository defect requiring repair.

## Audited implementation

- implementation issue: #289
- implementation PR: #290
- exact validated implementation head: 1da24f403f7de118f205c6fab5616f5e27588a57
- implementation GitHub Actions run: 37604276951
- implementation merge / audited protected baseline: bd64ae187346e4ba33266d41067a41478d521be7
- audit issue: #291
- audit branch: audit/a291
- chapter: ATLAS-CH-VARIOPT-001

Protected implementation artifact identities:

- specification: 9023f94675ad4d0144f9b074877c82f62c84909a
- derivation packet: 0862c95b24ea66ca6a6a6d4f1d9d3c031af1354b
- computational witness: 82ac7737ac0718c83db48face1e5fb9d402aebcb
- reader manuscript: 57751af058ee5885e7478e1aa74c1cc50aa2f463
- source lock: 1e20f98009b8828963c9d26aa87323292d6f99b3
- Chapter Ledger: 09a07425e69f67d1113f037aaf62f60fa769dd39
- Source Register: 1910bb5a199cb976b0821e9a1c9d5158556db53d
- transaction receipt: 4628b94d73b217e8377e3aa7019df3a620b4789f

The protected implementation merge has zero file differences from the exact validated implementation head.

## 1. Hard prerequisite — NUMERICS-001

PASS.

Exact binds:

- manuscript: a719a16e86d1feb76679e1f1cda2d9d3393d2e42
- source lock: 7feea1c8ca3026fa1f61f35b87281b4afe9ccd8d
- AUDIT-009: 2bbb1b7687d6c4b8c0bfeed5206de836dac92dca

VARIOPT preserves the inherited numerical-analysis firewalls:

- exact flow versus numerical update;
- local defect versus global error;
- stability versus accuracy;
- structure preservation versus exact invariant preservation;
- conditional order/stability results versus unrestricted analogies.

No variational derivation is used to bypass these conditions.

## 2. Hard prerequisite — MANOPT-001

PASS.

Exact binds:

- manuscript: 62ded6bc72c980feb96dff2c77c122141171f64f
- source lock: e98e655839f521250d25350c33006c9eed60e23c
- AUDIT-045: f6663dde7a93c9ca7a471e3e272759c9c337dfd6

VARIOPT preserves:

- metric-dependent gradients;
- tangent vectors as local legal velocities;
- retraction versus exponential-map distinction;
- constraint preservation versus descent/convergence/global optimality;
- vector transport versus ambient-coordinate reuse.

## 3. Established external authority

PASS.

The source lock separates three established-theory references:

- Bregman (1967), DOI 10.1016/0041-5553(67)90040-7, for the Bregman-divergence/projection lineage;
- Marsden and West (2001), DOI 10.1017/S096249290100006X, for discrete mechanics, discrete variational principles, and variational-integrator symplectic structure;
- Wibisono, Wilson, and Jordan (2016), DOI 10.1073/pnas.1614734113, for the Bregman-Lagrangian variational perspective on accelerated optimization.

The chapter does not extend any source into a universal optimizer-superiority result.

## 4. GCL MODULUS authority typing

PASS.

Protected programme snapshot:

- repository: grandchallenge/MODULUS
- commit: 7ca4ffcdace32d5ff79c27ad557bfb690fac0af3
- programme-context blob: 73af647840f07aa527e98998e0397de240d34e7c
- Hyperball implementation blob: 88b5e2b4c9abe760b8670f7fd2691fee25587b17
- Hyperball test blob: 105d6b4e38fe6d71bef8e7ec28c2f05a5ce08434

GCL repository-profile evidence:

- grandchallenge/gcl-standards commit: b89fc0ab807e69a255760c11ce85b1048d329c81
- MODULUS provider-profile blob: 6d52d66cbc11478c0f0a8872c19160d572dc4396

The provider profile assigns MODULUS versioned implementation, benchmark, and empirical-evidence authority, with no claim-promotion or certification authority.

VARIOPT preserves this distinction throughout.

## 5. Bregman definition

PASS.

For differentiable strictly convex \(\phi\), the chapter uses:

\[
D_\phi(y,x)
=
\phi(y)-\phi(x)-\langle\nabla\phi(x),y-x\rangle.
\]

The ordering of arguments is explicit.

The chapter does not assert symmetry or triangle inequality.

## 6. Exact asymmetry witness

PASS.

For:

\[
\phi(x)=e^x,
\]

independent exact replay gives:

\[
D_\phi(1,0)=e-2,
\]

and:

\[
D_\phi(0,1)=1.
\]

Since these are unequal, the chapter correctly blocks the identification of a Bregman divergence with a metric.

## 7. Local Hessian geometry

PASS.

Taylor expansion gives:

\[
D_\phi(x+\delta,x)
=
\frac12\delta^\top\nabla^2\phi(x)\delta
+
O(\|\delta\|^3).
\]

For \(\phi(x)=e^x\) at \(x=0\):

\[
D_\phi(\delta,0)
=
e^\delta-1-\delta
=
\frac12\delta^2+\frac16\delta^3+\cdots.
\]

The manuscript correctly treats the Hessian as local quadratic geometry and does not promote it into a global metric.

## 8. Mirror/Bregman proximal stationarity

PASS.

For the declared local problem:

\[
\Psi(x)
=
\eta\langle g_k,x\rangle
+
D_\phi(x,x_k),
\]

interior stationarity gives:

\[
\nabla\phi(x_{k+1})
=
\nabla\phi(x_k)-\eta g_k.
\]

The chapter correctly identifies this as a dual-coordinate relation depending on the generator, domain, local covector, and step.

## 9. Euclidean special case

PASS.

For:

\[
\phi(x)=\frac12\|x\|^2,
\]

the divergence is:

\[
D_\phi(y,x)=\frac12\|y-x\|^2,
\]

and stationarity reduces to:

\[
x_{k+1}=x_k-\eta g_k.
\]

Euclidean gradient descent is therefore presented as a special case rather than the definition of divergence-derived optimization.

## 10. Entropic exact update

PASS.

For \(x>0\):

\[
\phi(x)=x\log x-x,
\qquad
\nabla\phi(x)=\log x.
\]

The dual-coordinate relation yields:

\[
x_{k+1}
=
x_k e^{-\eta g_k}.
\]

At:

\[
x_k=1,\quad
\eta=1,\quad
g_k=\log2,
\]

independent replay gives:

\[
x_{k+1}=\frac12.
\]

## 11. Divergence-derived non-descent control

PASS.

For:

\[
f(x)=\frac12(x-2)^2,
\qquad
x_0=0,
\]

the gradient is:

\[
g_0=-2.
\]

With Euclidean Bregman geometry and \(\eta=3\):

\[
x_1=6.
\]

The exact objective values are:

\[
f(x_0)=2,
\qquad
f(x_1)=8.
\]

The objective increases.

Thus the chapter correctly establishes:

\[
\text{divergence-derived update}
\not\Rightarrow
\text{automatic one-step descent}.
\]

## 12. Action versus objective

PASS.

The continuous action is declared as:

\[
\mathcal A[q]
=
\int L(q,\dot q,t)\,dt.
\]

Euler-Lagrange stationarity concerns \(\mathcal A\), not automatically an optimization objective \(f\).

The chapter explicitly preserves this type distinction.

## 13. Bregman-Lagrangian source scope

PASS.

The reader states the Wibisono-Wilson-Jordan Bregman Lagrangian in the source-scoped form:

\[
\mathcal L(X,V,t)
=
e^{\alpha_t+\gamma_t}
\left[
D_h(X+e^{-\alpha_t}V,X)
-
e^{\beta_t}f(X)
\right].
\]

It uses the source only for the continuous-time variational organization of accelerated optimization families.

It does not infer that arbitrary discretizations are accelerated, stable, accurate, descending, or optimal.

## 14. Continuous-versus-discrete firewall

PASS.

The manuscript explicitly reuses the audited Numerics rule:

\[
\text{continuous theorem}
\not\Rightarrow
\text{arbitrary discrete theorem}.
\]

The discrete map is treated as an independent mathematical object requiring independent analysis.

## 15. Discrete action

PASS.

The chapter defines:

\[
\mathcal A_d
=
\sum_k L_d(q_k,q_{k+1};h).
\]

Interior variation yields the discrete Euler-Lagrange equation:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1})
=
0.
\]

This is correctly distinguished from objective-function stationarity.

## 16. Exact oscillator discrete Lagrangian

PASS.

The declared continuous Lagrangian is:

\[
L(q,\dot q)
=
\frac12\dot q^2-\frac12q^2.
\]

The discrete Lagrangian is:

\[
L_d(q_k,q_{k+1};h)
=
\frac{(q_{k+1}-q_k)^2}{2h}
-
\frac h2q_k^2.
\]

Exact differentiation gives:

\[
D_2L_d(q_{k-1},q_k)
=
\frac{q_k-q_{k-1}}h,
\]

and:

\[
D_1L_d(q_k,q_{k+1})
=
-\frac{q_{k+1}-q_k}h-hq_k.
\]

## 17. Discrete recurrence

PASS.

Setting the discrete Euler-Lagrange equation to zero yields:

\[
q_{k+1}
=
(2-h^2)q_k-q_{k-1}.
\]

The derivation is algebraically exact.

## 18. Momentum lift

PASS.

With:

\[
p_k
=
\frac{q_k-q_{k-1}}h,
\]

the recurrence becomes:

\[
p_{k+1}=p_k-hq_k,
\]

\[
q_{k+1}=q_k+h p_{k+1}.
\]

This is the declared symplectic-Euler ordering.

## 19. Exact symplectic matrix

PASS.

The state matrix is:

\[
M_h
=
\begin{pmatrix}
1-h^2 & h\\
-h & 1
\end{pmatrix}.
\]

Independent symbolic replay gives:

\[
\det M_h=1,
\]

and for:

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

\[
M_h^\top J M_h=J.
\]

The finite map is therefore exactly symplectic.

## 20. Energy non-conservation control

PASS.

At:

\[
h=\frac12,
\qquad
(q_0,p_0)=(0,1),
\]

the exact update is:

\[
p_1=1,
\qquad
q_1=\frac12.
\]

For:

\[
H(q,p)=\frac12(q^2+p^2),
\]

independent replay gives:

\[
H_0=\frac12,
\qquad
H_1=\frac58.
\]

Thus exact symplecticity does not imply exact energy conservation.

## 21. Objective non-descent control

PASS.

For:

\[
F(q)=\frac12q^2,
\]

the same exactly symplectic step gives:

\[
F(q_0)=0,
\qquad
F(q_1)=\frac18.
\]

Thus exact symplecticity does not imply one-step objective descent.

## 22. Structure-preservation boundaries

PASS.

The reader explicitly denies the implications:

- variational derivation -> numerical accuracy;
- symplecticity -> exact energy conservation;
- symplecticity -> stability;
- symplecticity -> descent;
- constraint preservation -> convergence;
- stationarity -> global optimality.

These are consistent with the audited prerequisites.

## 23. MODULUS tangent projection

PASS.

The protected Hyperball implementation receives a base optimizer proposal \(u\) and parameter group \(w\), and computes the radial/tangent decomposition:

\[
u_\parallel
=
\frac{\langle u,w\rangle}{\|w\|^2}w,
\]

\[
u_\perp
=
u-u_\parallel,
\]

modulo the implementation's declared epsilon and grouping axes.

For the exact witness:

\[
w=(1,0),
\qquad
u=(1,1),
\]

the tangent proposal is:

\[
u_\perp=(0,1).
\]

## 24. MODULUS target-angle implementation semantics

PASS.

The protected implementation's target-angle branch sets the desired tangent-update norm to:

\[
\alpha\|w\|.
\]

The chapter correctly reports this implementation fact rather than silently replacing it by an exponential-map update.

## 25. Exact finite MODULUS angle control

PASS.

For unit:

\[
w=(1,0),
\qquad
v=(0,1),
\qquad
\alpha=1,
\]

sphere retraction gives:

\[
w_+
=
\frac{(1,1)}{\sqrt2}.
\]

The exact post-retraction angle satisfies:

\[
\theta=\frac\pi4,
\]

not one radian.

More generally:

\[
w_+
=
\frac{w+\alpha v}{\sqrt{1+\alpha^2}}
\]

gives:

\[
\theta=\arctan\alpha
\]

for \(\alpha\ge0\).

Thus:

\[
\theta
=
\alpha-\frac{\alpha^3}{3}+O(\alpha^5)
\]

for small \(\alpha\).

The manuscript correctly describes the current parameter as first-order angular control through tangent-update norm, not an exact finite geodesic-angle parameter.

## 26. MODULUS variational non-claim

PASS.

No discrete action, Bregman objective, or Bregman Lagrangian is identified in the protected Hyperball implementation evidence.

The chapter therefore does not call Hyperball a variational integrator or a discretization of the Bregman Lagrangian.

It calls it a programme example of explicit geometry-to-update construction.

That is the supported claim.

## 27. Programme authority boundary

PASS.

The chapter repeatedly distinguishes:

- established external mathematical theory;
- Atlas exact derivations;
- GCL implementation facts;
- empirical claims;
- architectural proposals.

No GCL programme observation is promoted into certified or universal theory.

## 28. Receipt provenance

PASS.

Every implementation artifact identity recorded in governance/tranches/ATLAS-CH-VARIOPT-001.md matches the protected implementation tree.

The receipt itself is bound at:

4628b94d73b217e8377e3aa7019df3a620b4789f.

## 29. Chapter Ledger and Source Register

PASS.

The Chapter Ledger records VARIOPT-001 at draft-v0.1 with:

- specification;
- manuscript;
- derivation packet;
- source lock;
- computational witness.

The Source Register contains ATLAS-SRC-VARIOPT-LOCK-001.

No governed figure is required for this bounded chapter.

## 30. Repository integrity

PASS subject to audit-PR validation.

The exact implementation head:

1da24f403f7de118f205c6fab5616f5e27588a57

passed the full repository validator in GitHub Actions run:

37604276951.

The protected implementation merge:

bd64ae187346e4ba33266d41067a41478d521be7

has zero file differences from the exact validated implementation head.

Independent post-merge replay returned:

VARIOPT_AUDIT_WITNESS_OK.

The audit record itself must pass the full repository validator on its own exact head before protected merge.

## Final disposition

AUDIT-072 passes with no repair, subject to exact-head audit-PR validation.

The durable VARIOPT rule is:

**declare the geometry or action, derive the update, identify exactly what structure it preserves, then separately prove or measure descent, convergence, stability, accuracy, invariants, and empirical utility; programme-specific geometry machinery remains programme evidence rather than universal theory.**
