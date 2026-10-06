# AUDIT-058 — Composition Without Catastrophe

## Disposition

**PASS AFTER ONE DOCUMENTARY PROVENANCE REPAIR**

ATLAS-CH-COMPOSE-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, witness, or claim-boundary defect requiring reversal.

One in-scope documentary provenance defect was repaired: the transaction receipt had frozen the manuscript and computational-witness blob identities before the two protocol-marker repairs required by canonical validation. The actual protected implementation merge contained the repaired blobs, while the receipt still named the earlier blobs. AUDIT-058 updates the receipt to the exact merged identities.

No mathematical statement or exact witness arithmetic changed.

## Audited implementation

- implementation issue: #231
- implementation PR: #232
- exact validated implementation head: 6fc852b93cd35b2ca5bad52cff049777fe49d958
- implementation GitHub Actions run: 37472274892
- implementation merge / audited protected baseline: 57542068df60818d05c14b01f1aa2607ca619232
- audit issue: #233
- audit branch: audit/a233
- chapter: ATLAS-CH-COMPOSE-001

Implementation artifact identities at protected merge:

- specification: 9eef5fff041a255f7fc137d24ac7457fcc1db8a7
- derivation packet: f698e1f2ddf35099b53ad85af8e9e357de19166b
- computational witness: 878a85b8b163f99fb68b8a9a5e4f414a14fa8426
- reader manuscript: da94fe5d6106a50b168a4f95fa0765c9c7c6b415
- source lock: c16ab3f6ce67e81cff9f85f2f98a79ad55549cd5
- Chapter Ledger: 210dbb1d892a2cc58756e262457e5696a0d69729
- Source Register: a03c6c3f9ea02fdc74fa20d3a9f6546d46f49824

## 1. Hard prerequisite identity

PASS.

Boundary Contracts is bound exactly:

- manuscript: a270c38cda7ff280e517bd1a09ed196bb48dc759;
- source lock: 80463b18216747650d3ff8e99d6da933173d4486;
- AUDIT-003: 9723fcb3dfa0111829b98f1c9bb416a13dbd714e.

Split-Operator Networks is bound exactly:

- manuscript: bcaf1db6b1fc7144e2472ff2725f7ff561fe7fc0;
- source lock: afb84e2f3ebb941f320c52693b088b0eb078b8ce;
- AUDIT-036: 5e093460550c15fe491ba3214b2f52d48076dc0a.

No downstream chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

COMPOSE adds no new external primary authority.

The source lock inherits only source-bounded interfaces already audited through BCONTRACT-001 and SPLIT-001:

- Higham (2002) for conditioning/perturbation and numerical-error discipline;
- Baydin et al. (2018) for JVP/VJP and derivative-program mechanics;
- McLachlan and Quispel (2002) for classical splitting/order/commutator results;
- Hairer, Lubich, and Wanner (2006) for composition/splitting and bounded structure-preservation semantics.

All four citation keys resolve in the repository bibliography.

The manuscript does not add a global safety theorem, a universal contract calculus, or a neural convergence theorem.

## 3. Product order versus chronology

PASS.

The chapter states explicitly that for column-vector action:

- chronological A then B is represented by BA;
- chronological B then A is represented by AB.

This preserves the exact product-order repair frozen by AUDIT-036.

No ambiguous "AB means A then B" prose remains in the load-bearing witness.

## 4. Component norms

PASS.

For

\[
A=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\]

the singular values are

\[
3/2,\quad 2/3.
\]

Therefore

\[
\|A\|_2=3/2.
\]

For

\[
B=
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix},
\]

\[
B^\top B
=
\operatorname{diag}(4/9,9/4),
\]

so

\[
\|B\|_2=3/2.
\]

Both component-local gain contracts are exact.

## 5. Chronological A-then-B witness

PASS.

\[
BA
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

This is orthogonal, so

\[
\boxed{\|BA\|_2=1.}
\]

For the declared system gain budget

\[
\tau=2,
\]

this chronology passes.

## 6. Reverse chronology witness

PASS.

\[
AB
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}.
\]

Then

\[
(AB)^\top(AB)
=
\operatorname{diag}(16/81,81/16).
\]

Therefore

\[
\boxed{\|AB\|_2=9/4.}
\]

Since

\[
9/4>2,
\]

the reverse chronology violates the same system gain budget.

The witness therefore exactly establishes:

> identical component-local gain ceilings do not determine the system disposition when ordering changes.

## 7. Noncommutativity

PASS.

\[
[A,B]
=
AB-BA
=
\begin{pmatrix}
0&5/4\\
-5/9&0
\end{pmatrix}
\ne0.
\]

The order effect is genuine in the declared finite-dimensional reference system.

No global nonlinear commutator claim is inferred.

## 8. Product-bound tightness

PASS.

The component norm product is

\[
\|A\|_2\|B\|_2=9/4.
\]

For \(AB\), the upper bound is attained:

\[
\|AB\|_2=9/4.
\]

For \(BA\), it is loose:

\[
\|BA\|_2=1<9/4.
\]

The chapter correctly uses this to distinguish a valid conservative bound from the exact composite gain.

## 9. Commuting control

PASS.

For

\[
A_c=\operatorname{diag}(3/2,2/3),
\qquad
B_c=\operatorname{diag}(2/3,3/2),
\]

\[
[A_c,B_c]=0,
\]

and

\[
A_cB_c=B_cA_c=I.
\]

Each component still has norm \(3/2\), while either composition has norm \(1\).

This is a valid matched control demonstrating that equal local norm ceilings do not determine compositional geometry.

## 10. Two-stage error propagation

PASS.

Under the stated connecting-domain assumptions,

\[
\|\widehat f(x)-f(x)\|
\le
\varepsilon_f,
\]

\[
\|\widehat g(y)-g(y)\|
\le
\varepsilon_g,
\]

and

\[
\|g(y_1)-g(y_2)\|
\le
L_g\|y_1-y_2\|,
\]

the derivation uses the triangle inequality to obtain

\[
\boxed{
\|\widehat g(\widehat f(x))-g(f(x))\|
\le
\varepsilon_g+L_g\varepsilon_f.
}
\]

The connecting-domain assumption is explicit and correctly identified as load-bearing.

## 11. Exact scalar error-budget witness

PASS.

With

\[
\varepsilon_f=\varepsilon_g=1/10,
\qquad
L_g=3/2,
\]

the derived composition error budget is

\[
1/10+(3/2)(1/10)=1/4.
\]

The declared system requirement is

\[
E\le1/5.
\]

Thus

\[
1/4>1/5.
\]

The witness correctly shows that individually acceptable local error ceilings can yield a derived composition bound that violates a stricter system budget.

## 12. n-stage recurrence

PASS.

Given

\[
E_k\le L_kE_{k-1}+\varepsilon_k,
\qquad E_0=0,
\]

the induction correctly yields

\[
\boxed{
E_n
\le
\sum_{j=1}^{n}
\varepsilon_j
\prod_{k=j+1}^{n}L_k.
}
\]

The empty product convention is stated.

The result is scoped to the declared connecting domains and bounds.

## 13. Uniform-chain specialization

PASS.

For \(L_k=L\) and \(\varepsilon_k=\varepsilon\),

\[
E_n
\le
\varepsilon\sum_{r=0}^{n-1}L^r.
\]

The chapter correctly specializes this to:

\[
E_n\le n\varepsilon
\]

when \(L=1\), and the geometric expression when \(L\ne1\).

It does not assert that the worst-case bound is attained.

## 14. Certificate hierarchy

PASS.

The chapter separates:

1. component-local certificate;
2. interface compatibility certificate;
3. derived composition certificate;
4. system-level guarantee.

No level is automatically promoted to the next.

This is consistent with the audited BCONTRACT local-to-global firewall.

## 15. Local versus global scope

PASS.

The manuscript explicitly rejects the inference

\[
\|J_f(x_0)\|\le L
\Rightarrow
f\text{ is globally }L\text{-Lipschitz}.
\]

It correctly states that a global result requires control over the relevant region and sufficient regularity/path assumptions.

## 16. Interface versus closed-loop scope

PASS.

The chapter marks repeated feedback/iteration as a boundary rather than importing a hidden stability theory.

It does not infer boundedness, convergence, transient-growth control, or invariant-set preservation from one-pass interface compatibility.

## 17. Error-type separation

PASS.

The manuscript keeps distinct:

- semantic mismatch;
- numerical approximation error;
- local sensitivity amplification;
- splitting/order error;
- optimization/modeling error;
- finite-precision error;
- stochasticity;
- distribution shift.

No single bound is claimed to subsume all of them.

## 18. Classical splitting firewall

PASS.

The manuscript uses SPLIT-001 only for bounded order/noncommutativity language.

It explicitly denies automatic transfer of Lie/Strang convergence, exact-flow, reversibility, or structure-preservation claims to arbitrary learned modules.

## 19. Transaction-receipt provenance

PASS AFTER REPAIR.

The implementation receipt originally recorded:

- witness: afae55764c1fb8bd97f61e182bc8fd7f224cd298;
- manuscript: ef1584366386c8764f31d013fd587ec81a27293b.

Those were the blobs before canonical validation required two documentary protocol-marker repairs.

The protected implementation merge actually contains:

- witness: 878a85b8b163f99fb68b8a9a5e4f414a14fa8426;
- manuscript: da94fe5d6106a50b168a4f95fa0765c9c7c6b415.

AUDIT-058 repairs governance/tranches/COMPOSE-001.md to those exact merged identities and records why they changed.

No mathematical content changed in the protocol-marker repair.

## 20. Repository integrity

PASS subject to audit-PR validation.

The audit branch preserves:

- 80 chapters;
- the original 126 hard dependency edges;
- COMPOSE status draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths;
- no new governed figure;
- registered COMPOSE source lock;
- inherited bibliography keys;
- no new external source authority.

The implementation exact head passed GitHub Actions run 37472274892.

The protected implementation merge passed canonical repository validation.

## Final disposition

AUDIT-058 passes after one documentary provenance repair.

The durable COMPOSE rule is:

**local guarantees compose only through an explicit compatibility and budget argument; order, domain, error propagation, and certificate scope remain part of the proof obligation.**
