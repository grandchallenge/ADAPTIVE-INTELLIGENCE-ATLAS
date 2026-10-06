# AUDIT-061 — Joint Uncertainty Propagation

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-JOINTUNC-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #243
- implementation PR: #244
- exact validated implementation head: 1ad4320b548aa08434f8940b88d0c3e9d016add7
- implementation GitHub Actions run: 37536081988
- implementation merge / audited protected baseline: a204fb495994607bd688193210242b9a32d06ce5
- audit issue: #245
- audit branch: audit/a245
- chapter: ATLAS-CH-JOINTUNC-001

Protected implementation artifact identities:

- specification: 0b09fc62d7eacea48c9c0ab0d71971011421d595
- derivation packet: e3aeae34aa3e03f663f1492fe3a9d4d0950c8be2
- computational witness: e3562d3029924cc349aa73bea3b191bfaaef47ba
- reader manuscript: 8d9072371a5d0e168903e04feb232bde93a55447
- source lock: 07e57b2c523baa4297c7cddb6fbf3e1a95cc1c36
- Chapter Ledger: c474886129e0bfb4ae0513bf67ef10cb0b77b3c4
- Source Register: 3f97ca6badf30361bbbab282b55f4aff8eaf8225
- transaction receipt: 5edfe19896d6ea1aeefa0e399e1b25eb8e3daed6

## 1. Hard prerequisites

PASS.

RLBASE-001 is bound exactly:

- manuscript a99f78b788b97bc1bb3346ca1f1b97802c0f84db;
- source lock b29ecea9134227cb5ce3fcd7cc47303a90bd6699;
- AUDIT-017 8b7a1f9b61c15ab9c2c010ea538e25c11a7ed1cc.

INFO-001 is bound exactly:

- manuscript 0fca10cbc7476c5b729ee15dfad0dec563665821;
- source lock ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c;
- AUDIT-004 948f76b3f86d27fa4830efc30d8ef0135134256e.

No downstream chapter is used as hidden authority.

## 2. Source decision

PASS.

No new external academic source is needed for the load-bearing result.

The affine identity

\[
\operatorname{Var}(a^\top\varepsilon)=a^\top\Sigma a
\]

is proved directly from the covariance definition.

The nonlinear formula is not presented as an imported global theorem; the chapter explicitly writes the Taylor remainder and keeps the first-order expression local.

## 3. Uncertainty-coordinate separation

PASS.

The chapter keeps distinct local coordinates for:

- reward error;
- transition-effect error;
- observation/belief error;
- future-value error.

It states that these are declared local scalar coordinates, not universal latent variables.

Observation uncertainty is not silently collapsed into transition uncertainty.

## 4. Exact affine variance identity

PASS.

For mean \(\mu\),

\[
\delta-\mathbb E[\delta]
=
a^\top(\varepsilon-\mu),
\]

hence

\[
\operatorname{Var}(\delta)
=
a^\top
\mathbb E[(\varepsilon-\mu)(\varepsilon-\mu)^\top]
a
=
a^\top\Sigma a.
\]

The expanded form correctly includes:

\[
2\sum_{i<j}a_i a_j\operatorname{Cov}(\varepsilon_i,\varepsilon_j).
\]

## 5. Diagonal-only witness

PASS.

With:

\[
a=(1,1,1,1/2)^\top
\]

and four unit marginal variances:

\[
V_{\rm diag}
=
1+1+1+\frac14
=
\boxed{\frac{13}{4}}.
\]

## 6. Positive common-shock case

PASS.

The construction:

\[
(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)
=
(U,U,U,W)
\]

with independent centered Rademacher \(U,W\) gives:

\[
\delta_+=3U+\frac12W.
\]

Therefore:

\[
V_+
=
9+\frac14
=
\boxed{\frac{37}{4}}.
\]

The correction relative to the diagonal-only calculation is:

\[
\boxed{6}.
\]

Independent exact replay agrees.

## 7. Positive covariance matrix

PASS.

\[
\Sigma_+
=
\begin{pmatrix}
1&1&1&0\\
1&1&1&0\\
1&1&1&0\\
0&0&0&1
\end{pmatrix}
=
bb^\top+e_4e_4^\top
\]

for \(b=(1,1,1,0)^\top\).

Thus \(\Sigma_+\) is positive semidefinite exactly.

## 8. Cancellation case

PASS.

The construction:

\[
(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)
=
(U,U,-U,W)
\]

gives:

\[
\delta_-=U+\frac12W.
\]

Therefore:

\[
V_-=
1+\frac14
=
\boxed{\frac54}.
\]

The covariance correction is:

\[
\boxed{-2}.
\]

Independent exact replay agrees.

## 9. Cancellation covariance matrix

PASS.

\[
\Sigma_-
=
\begin{pmatrix}
1&1&-1&0\\
1&1&-1&0\\
-1&-1&1&0\\
0&0&0&1
\end{pmatrix}
=
cc^\top+e_4e_4^\top
\]

for \(c=(1,1,-1,0)^\top\).

Thus \(\Sigma_-\) is positive semidefinite exactly.

## 10. Independence control

PASS.

Four mutually independent centered Rademacher coordinates give:

\[
\Sigma_0=I_4
\]

and:

\[
V_0
=
a^\top I_4a
=
\boxed{\frac{13}{4}}.
\]

The control therefore recovers the diagonal-only result exactly.

## 11. Same marginals, different propagated variance

PASS.

All three regimes have marginal variance vector:

\[
(1,1,1,1).
\]

Yet:

\[
V_+=\frac{37}{4},
\qquad
V_-=\frac54,
\qquad
V_0=\frac{13}{4}.
\]

The manuscript correctly concludes that marginal variances alone do not determine the propagated variance.

## 12. Independence versus zero covariance

PASS.

The exact variance expansion requires the relevant covariance correction to vanish.

Full independence is sufficient but not necessary.

The manuscript explicitly rejects:

\[
\text{zero covariance}
\Rightarrow
\text{independence}.
\]

## 13. Functional relativity

PASS.

The chapter states that for another sensitivity vector \(b\),

\[
\operatorname{Var}(b^\top\varepsilon)=b^\top\Sigma b.
\]

Thus propagated uncertainty is relative to the declared decision functional.

No universal scalar uncertainty score is inferred.

## 14. Nonlinear remainder identity

PASS.

For differentiable \(F\):

\[
F(x+\varepsilon)-F(x)
=
g^\top\varepsilon+R,
\qquad g=\nabla F(x).
\]

The chapter correctly gives the exact variance decomposition:

\[
\operatorname{Var}(F(x+\varepsilon)-F(x))
=
g^\top\Sigma g
+
\operatorname{Var}(R)
+
2\operatorname{Cov}(g^\top\varepsilon,R).
\]

Therefore:

\[
g^\top\Sigma g
\]

is only the first-order propagated term unless the remainder contribution is controlled.

## 15. Local/global boundary

PASS.

The chapter explicitly blocks promotion from a local first-order covariance calculation to a global theorem for nonlinear multi-step control.

It names failure modes including policy switching, changing visitation, large perturbations, changing covariance, and higher-order effects.

## 16. Expected value versus uncertainty

PASS.

The chapter preserves RLBASE's distinction between expected return/value and uncertainty.

It does not redefine value as a risk-adjusted scalar.

Any expectation/uncertainty tradeoff must be separately declared.

## 17. Variance versus full risk

PASS.

The manuscript states that equal variance does not imply equal tail probability, support, skewness, or multimodality.

Second moments are therefore not presented as a complete risk representation.

## 18. Dependence versus causality

PASS.

The chapter treats covariance as statistical dependence in a declared probability model and explicitly refuses causal-direction inference.

This is consistent with INFO-001.

## 19. Transaction-receipt provenance

PASS.

Every implementation artifact identity in governance/tranches/JOINTUNC-001.md matches the exact protected implementation merge.

No post-receipt repair changed any implementation artifact.

## 20. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- JOINTUNC status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- hard dependencies remain RLBASE-001 and INFO-001;
- the JOINTUNC source lock is registered;
- no governed figure is introduced;
- no new bibliography key is required;
- implementation exact head passed GitHub Actions run 37536081988;
- protected implementation merge passed canonical repository validation;
- independent audit replay returned JOINTUNC_AUDIT_WITNESS_OK.

## Final disposition

AUDIT-061 passes with no repair.

The durable JOINTUNC rule is:

**propagate uncertainty through the joint covariance structure of the declared decision functional; do not assume marginal error bars add independently, and do not promote local statistical propagation into global or causal claims without additional evidence.**
