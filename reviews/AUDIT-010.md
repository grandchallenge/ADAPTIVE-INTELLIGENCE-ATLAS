# AUDIT-010 — From Layered Networks to Residual Systems

## Disposition

**PASS AFTER ONE SCOPE / WORDING REPAIR**

\`ATLAS-CH-ARCHHIST-001\` remains at \`draft-v0.1\`.

The chapter's structural mathematics, exact witness, source scope, Dynamics dependency pin, and figure provenance pass audit.

AUDIT-010 found one bounded issue:

> the Highway section used “interpolates” without stating the tied transform gate's \([0,1]\) range explicitly, and two historical sentences used “introduced” in a way that could be read as a priority claim.

The repair:

- states the tied transform gate is coordinatewise in \([0,1]\);
- keeps \(C=1-T\) explicit in the tied-gate setting;
- changes LSTM/Highway wording from priority-like “introduced” to architecture-scoped “uses” language;
- adds Highway gating explicitly to the source-lock claim boundary.

No source, figure, or witness identities changed.

## Audited baseline

- ARCHHIST-001 merge:
  \`e8ede399667bef614e4dff9b1cecb066447c24dd\`;
- audit issue:
  \`#52\`;
- chapter:
  \`ATLAS-CH-ARCHHIST-001\`.

## 1. Layered composition

PASS.

For

\[
x_{k+1}=F_k(x_k),
\]

the chapter gives

\[
x_L
=
F_{L-1}\circ\cdots\circ F_0(x_0).
\]

For differentiable layers,

\[
J_{\rm total}
=
J_{F_{L-1}}
\cdots
J_{F_0},
\]

with the order matching composition.

## 2. Circular convolution equivariance

PASS.

For periodic convolution

\[
(C_kx)_j
=
\sum_r k_r x_{j-r},
\]

and cyclic shift

\[
(S_mx)_j=x_{j-m},
\]

the derivation proves

\[
C_kS_m=S_mC_k.
\]

Independent Wolfram replay gives zero commutator for the exact witness matrix pair and

\[
CSx=SCx=(10,9,4,7).
\]

The chapter explicitly limits this exact claim to the declared circular-convolution model and lists practical operations that can break full-pipeline equivariance.

## 3. Recurrent closed form

PASS.

For

\[
h_{t+1}=a h_t+b x_t,
\]

the chapter derives

\[
h_T
=
a^T h_0
+
b\sum_{j=0}^{T-1}
a^{T-1-j}x_j.
\]

Independent replay with

\[
a=\frac12,\quad b=2,\quad h_0=1,\quad (x_0,x_1,x_2)=(3,-1,4)
\]

gives

\[
(h_0,h_1,h_2,h_3)
=
\left(
1,\frac{13}{2},\frac54,\frac{69}{8}
\right),
\]

and the closed form gives

\[
h_3=\frac{69}{8}.
\]

## 4. Encoder–decoder information-loss boundary

PASS.

If

\[
E(x_1)=E(x_2)
\]

while required deterministic targets differ, a decoder receiving only \(E(x)\) cannot reconstruct both targets exactly.

The chapter correctly states this as a capability-relative interface-sufficiency condition, not as a requirement that useful encoders be injective.

## 5. Highway transform/carry formulation

PASS AFTER REPAIR.

The chapter uses

\[
y
=
T(x)\odot H(x)
+
C(x)\odot x.
\]

For the tied-gate setting it now states explicitly:

\[
0\le T(x)\le1
\]

coordinatewise, with

\[
C(x)=1-T(x).
\]

Hence:

- \(T=0\) gives exact carry
  \[
  y=x;
  \]
- \(T=1\) gives exact transform
  \[
  y=H(x).
  \]

The word “interpolate” is now justified by the declared gate range.

## 6. Exact Highway witness

PASS.

For

\[
x=2,
\qquad
H(x)=5,
\qquad
T=\frac14,
\qquad
C=\frac34,
\]

independent replay gives

\[
y=\frac{11}{4}.
\]

The carry and transform limits replay exactly as:

\[
2
\]

and

\[
5.
\]

## 7. Highway versus residual algebra

PASS.

The chapter keeps separate:

\[
T\odot H+C\odot x
\]

from

\[
x+F(x).
\]

It treats them as related transport ideas, not identical architectures.

## 8. Residual Jacobian

PASS.

For

\[
x_{k+1}=x_k+F_k(x_k),
\]

the chapter derives

\[
J_k
=
I+J_{F_k}(x_k).
\]

For the linear witness

\[
A=
\begin{pmatrix}
1&2\\
-1&3
\end{pmatrix},
\]

independent replay gives

\[
I+A
=
\begin{pmatrix}
2&2\\
-1&4
\end{pmatrix}.
\]

With zero residual branch, the block Jacobian is exactly

\[
I.
\]

## 9. Residual identity-path scope

PASS.

The chapter explicitly denies that the identity path alone proves:

- easy optimization;
- well-conditioned total Jacobian products;
- harmless arbitrary depth.

The structural claim is only exact identity transport when the residual branch vanishes.

## 10. Residual versus ODE boundary

PASS.

The chapter rewrites

\[
x_{k+1}
=
x_k+h f_k(x_k)
\]

as Euler-like state evolution but requires additional conditions before interpreting a family as a discretization of one autonomous ODE.

It explicitly asks about:

- shared vector field;
- meaningful step size;
- refinement/convergence;
- smoothness compatibility;
- numerical structure preservation.

The conclusion remains:

> residual systems admit an integrator lens.

It does not claim literal ODE identity.

## 11. Neural ODE scope

PASS.

Neural ODEs are described as an explicit architecture family with

\[
\frac{dz}{dt}
=
f(z,t;\theta)
\]

and numerical integration.

The chapter does not use the Neural ODE paper as a theorem about ordinary ResNets.

## 12. Historical/source wording

PASS AFTER REPAIR.

The manuscript now avoids priority-like “introduced” wording for LSTM and Highway claims.

The source lock already states:

> No blanket priority claim is made that any cited paper uniquely invented an entire architecture class.

The chapter uses the cited papers only as influential/primary sources for declared structural mechanisms.

## 13. Chronology is not a ranking

PASS.

The chapter explicitly denies the ordering

\[
\text{MLP}<\text{CNN}<\text{RNN}<\text{ResNet}<\text{ODE}.
\]

The lineage is pedagogical and structural, not a universal performance ordering.

## 14. Dynamics prerequisite provenance

PASS.

The source lock pins the post-AUDIT-008A Dynamics manuscript:

- commit:
  \`c18a5067c29e2c34cfbec770c5220eea51555249\`;
- blob:
  \`f4aa89075f221529401e56a152a6cdfca3dcc47d\`.

Independent re-fetch matches exactly.

The Atlas seed inventory pin also matches:

- blob:
  \`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

## 15. Bibliography closure

PASS.

The canonical bibliography contains:

- \`RumelhartHintonWilliams1986\`;
- \`LeCunBottouBengioHaffner1998\`;
- \`HochreiterSchmidhuber1997\`;
- \`SutskeverVinyalsLe2014\`;
- \`SrivastavaGreffSchmidhuber2015\`;
- \`HeZhangRenSun2016\`;
- \`ChenRubanovaBettencourtDuvenaud2018\`.

## 16. Figure provenance

PASS.

\`ATLAS-FIG-ARCHHIST-001\`:

- generator blob:
  \`057e0da8dabc55045bfd9c3afe3014005c6adc76\`;
- rendered blob:
  \`296afa2a50cb63cce04a91ae9ef7b104f438406d\`;
- rendered bytes:
  \`49,015\`.

The manifest matches the audited Git tree.

The figure is correctly classed schematic.

Its six panels depict structural motifs only and explicitly do not encode priority, performance, parameter count, or architecture quality.

## 17. Chapter status

PASS.

\`ATLAS-CH-ARCHHIST-001\` remains:

\`draft-v0.1\`.

Its hard prerequisite remains:

- \`ATLAS-CH-DYN-001\`.

## 18. Final disposition

AUDIT-010 passes after one scope/wording repair.

The durable structural lineage is:

\[
\text{composition}
\to
\text{shared operators}
\to
\text{persistent state}
\to
\text{interfaces}
\to
\text{gated carry}
\to
\text{residual transport}
\to
\text{explicit continuous depth}.
\]

The chapter is now suitable to unlock its direct consumers, subject to successful repository validation and merge of this audit.
