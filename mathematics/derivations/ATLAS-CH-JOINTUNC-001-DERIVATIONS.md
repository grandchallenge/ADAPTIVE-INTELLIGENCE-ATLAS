# ATLAS-CH-JOINTUNC-001 — Derivation Packet

## Scope

This packet proves exact covariance-sensitive propagation for a declared affine local decision-error functional and states the exact remainder boundary for nonlinear first-order propagation.

Let

\[
\varepsilon=(\varepsilon_R,\varepsilon_T,\varepsilon_O,\varepsilon_V)^\top
\]

have finite second moments, mean \(\mu\), and covariance

\[
\Sigma=\mathbb E[(\varepsilon-\mu)(\varepsilon-\mu)^\top].
\]

The coordinates are local scalarized reward, transition-effect, observation/belief, and future-value errors.

## D1. Exact affine identity

For deterministic \(a\) and

\[
\delta=a^\top\varepsilon,
\]

we have

\[
\delta-\mathbb E[\delta]=a^\top(\varepsilon-\mu).
\]

Therefore

\[
\boxed{
\operatorname{Var}(\delta)=a^\top\Sigma a.
}
\]

Expanding,

\[
\boxed{
\operatorname{Var}(a^\top\varepsilon)
=
\sum_i a_i^2\operatorname{Var}(\varepsilon_i)
+
2\sum_{i<j}a_i a_j\operatorname{Cov}(\varepsilon_i,\varepsilon_j).
}
\]

The second sum is the covariance correction.

Define the diagonal-only quantity

\[
V_{\rm diag}=\sum_i a_i^2\operatorname{Var}(\varepsilon_i).
\]

Then diagonal-only propagation is exact when the weighted covariance correction vanishes. Pairwise zero covariance is sufficient; full independence is stronger than necessary.

## D2. Witness sensitivity

Use

\[
a=(1,1,1,1/2)^\top,
\]

so

\[
\delta
=
\varepsilon_R+\varepsilon_T+\varepsilon_O+\frac12\varepsilon_V.
\]

All four witness coordinates have unit marginal variance. Hence

\[
\boxed{
V_{\rm diag}=1+1+1+\frac14=\frac{13}{4}.
}
\]

## D3. Positive common shock

Let \(U,W\) be independent centered Rademacher variables and set

\[
\varepsilon_R=U,\quad
\varepsilon_T=U,\quad
\varepsilon_O=U,\quad
\varepsilon_V=W.
\]

Then

\[
\Sigma_+
=
\begin{pmatrix}
1&1&1&0\\
1&1&1&0\\
1&1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

With

\[
b=(1,1,1,0)^\top,\qquad e_4=(0,0,0,1)^\top,
\]

we have

\[
\Sigma_+=bb^\top+e_4e_4^\top\succeq0.
\]

Also

\[
\delta_+=3U+\frac12W,
\]

so

\[
\boxed{
\operatorname{Var}(\delta_+)=9+\frac14=\frac{37}{4}.
}
\]

The exact covariance correction is

\[
\frac{37}{4}-\frac{13}{4}
=
\boxed{6}.
\]

Equivalently, the three unit positive pairwise covariances among \(R,T,O\) contribute

\[
2(1+1+1)=6.
\]

## D4. Cancellation common shock

Let \(U,W\) again be independent centered Rademacher variables and set

\[
\varepsilon_R=U,\quad
\varepsilon_T=U,\quad
\varepsilon_O=-U,\quad
\varepsilon_V=W.
\]

Then

\[
\Sigma_-
=
\begin{pmatrix}
1&1&-1&0\\
1&1&-1&0\\
-1&-1&1&0\\
0&0&0&1
\end{pmatrix}.
\]

With

\[
c=(1,1,-1,0)^\top,
\]

\[
\Sigma_-=cc^\top+e_4e_4^\top\succeq0.
\]

Now

\[
\delta_-=U+\frac12W,
\]

so

\[
\boxed{
\operatorname{Var}(\delta_-)=1+\frac14=\frac54.
}
\]

The correction is

\[
\frac54-\frac{13}{4}
=
\boxed{-2}.
\]

Explicitly,

\[
2(1-1-1)=-2.
\]

## D5. Independence control

Let \(U_R,U_T,U_O,U_V\) be mutually independent centered Rademacher variables and set

\[
\varepsilon=(U_R,U_T,U_O,U_V)^\top.
\]

Then

\[
\Sigma_0=I_4
\]

and

\[
\boxed{
\operatorname{Var}(\delta_0)=a^\top I_4a=\frac{13}{4}.
}
\]

Thus the diagonal-only result is exact in the independence control.

## D6. Same marginals, different propagated uncertainty

All three cases have marginal variance vector

\[
(1,1,1,1).
\]

Yet their propagated variances are

\[
\boxed{
V_+=\frac{37}{4},\qquad
V_-=\frac54,\qquad
V_0=\frac{13}{4}.
}
\]

Therefore

\[
\boxed{
\text{same marginal variances}
\not\Rightarrow
\text{same propagated variance}.
}
\]

The difference is in the joint dependence structure.

## D7. Zero covariance versus independence

If the relevant pairwise covariances vanish, then the covariance correction is zero and

\[
\operatorname{Var}(a^\top\varepsilon)=V_{\rm diag}.
\]

But uncorrelated variables need not be independent.

Hence

\[
\boxed{
\text{zero covariance}
\not\Rightarrow
\text{independence}.
}
\]

Independence is sufficient, not necessary, for the witness cross terms to vanish.

## D8. Functional relativity

For another sensitivity vector \(b\),

\[
\delta_b=b^\top\varepsilon
\]

has variance

\[
\boxed{
\operatorname{Var}(\delta_b)=b^\top\Sigma b.
}
\]

Thus the same joint uncertainty state can propagate differently through different decision functionals.

Uncertainty propagation is functional-relative.

## D9. Nonlinear local propagation

Let \(F:\mathbb R^n\to\mathbb R\) be differentiable at nominal state \(x\). Write

\[
F(x+\varepsilon)-F(x)
=
g^\top\varepsilon+R,
\qquad
g=\nabla F(x),
\]

with Taylor remainder \(R\).

Then exactly,

\[
\boxed{
\operatorname{Var}(F(x+\varepsilon)-F(x))
=
g^\top\Sigma g
+
\operatorname{Var}(R)
+
2\operatorname{Cov}(g^\top\varepsilon,R).
}
\]

Therefore the familiar first-order expression

\[
\boxed{
\operatorname{Var}(F(x+\varepsilon)-F(x))
\approx
\nabla F(x)^\top\Sigma\nabla F(x)
}
\]

is justified only when the remainder terms are controlled.

It is not an exact global identity for arbitrary nonlinear systems.

## D10. Sequential boundary

For a sequential system

\[
x_{t+1}=F_t(x_t,\eta_t),
\]

multi-step uncertainty depends on local sensitivities, cross-time disturbance dependence, state-dependent covariance, policy feedback, and changing visitation.

The single-step identity

\[
a^\top\Sigma a
\]

is an exact local algebraic building block, not a global multi-step solution.

## D11. Object boundaries

Observation uncertainty is not transition uncertainty. In a partially observed system, latent-state evolution and observation generation are distinct stochastic objects even when dependent.

Reward uncertainty may reflect stochastic reward, learned reward error, measurement error, or misspecification; the witness collapses these only into a declared local coordinate.

Future-value uncertainty can combine next-state uncertainty, value estimation, approximation, and model error; the witness again uses one declared scalarized coordinate only after that modeling choice is made.

## D12. Expected value, variance, and full risk

Expected return and uncertainty are distinct. Two actions may have the same expectation and different uncertainty, or equal variance and different expectation.

Variance is also not the full risk distribution. Equal mean and variance do not imply equal tails, support, skewness, or multimodality.

Any decision rule combining expected value and uncertainty must state the combination explicitly.

## D13. Dependence is not causality

A nonzero covariance is a property of the declared joint probability model. It does not identify causal direction, intervention effect, or mechanism.

Therefore

\[
\boxed{
\text{statistical dependence}
\not\Rightarrow
\text{causal attribution}.
}
\]

## Durable propositions

1. \(\operatorname{Var}(a^\top\varepsilon)=a^\top\Sigma a\) exactly.
2. Marginal variances alone do not determine propagated variance.
3. Positive covariance can make diagonal-only propagation understate uncertainty.
4. Cancellation can make it overstate uncertainty.
5. Independence recovers the diagonal witness exactly.
6. Zero covariance is weaker than independence.
7. Propagation depends on the declared decision functional.
8. Nonlinear \(\nabla F^\top\Sigma\nabla F\) propagation is local first order unless remainder terms vanish.
9. Dependence is not causal direction.
10. Variance is not a complete distributional risk description.

## Claim boundary

This packet proves exact finite second-moment identities and exact Rademacher witnesses. It does not assert that real reward, transition, observation, and value errors have these toy covariance structures, that variance fully describes decision risk, or that a local first-order calculation remains valid globally through nonlinear multi-step control.
