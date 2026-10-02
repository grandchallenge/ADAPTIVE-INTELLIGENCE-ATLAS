# ATLAS-CH-OPTDYN-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm convention:** spectral/operator \(2\)-norm unless explicitly stated  
**Source lock:** \`sources/source-locks/ATLAS-CH-OPTDYN-001.yaml\`

## D1. Momentum is an augmented-state dynamical system

Consider the scalar quadratic

\[
L(\theta)=\frac h2\theta^2,
\qquad h>0,
\]

so

\[
g(\theta)=h\theta.
\]

Use the momentum recurrence

\[
v_{t+1}=\beta v_t+h\theta_t,
\]

\[
\theta_{t+1}=\theta_t-\eta v_{t+1}.
\]

Substituting the first equation into the second gives

\[
\theta_{t+1}
=
(1-\eta h)\theta_t-\eta\beta v_t.
\]

Define

\[
z_t=
\begin{pmatrix}
\theta_t\\
v_t
\end{pmatrix}.
\]

Then

\[
z_{t+1}=Jz_t,
\]

with

\[
\boxed{
J=
\begin{pmatrix}
1-\eta h&-\eta\beta\\
h&\beta
\end{pmatrix}.
}
\]

Optimizer state is therefore part of the state of the dynamical system, not merely bookkeeping.

## D2. Characteristic polynomial

The trace is

\[
\operatorname{tr}J=1-\eta h+\beta,
\]

and

\[
\det J=\beta.
\]

Therefore

\[
\boxed{
p(\lambda)
=
\lambda^2-(1-\eta h+\beta)\lambda+\beta.
}
\]

For the worked example

\[
h=1,\qquad
\eta=\frac1{10},\qquad
\beta=\frac9{10},
\]

we obtain

\[
J=
\begin{pmatrix}
\frac9{10}&-\frac9{100}\\
1&\frac9{10}
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
\lambda^2-\frac95\lambda+\frac9{10}.
\]

Hence

\[
\lambda_{\pm}
=
\frac9{10}\pm\frac3{10}i.
\]

Their magnitude is

\[
|\lambda_\pm|
=
\sqrt{\frac9{10}}
\approx0.9486832981<1.
\]

The linear fixed point is asymptotically stable.

## D3. The stable Jacobian is non-normal

For the same \(J\),

\[
J^\top J
=
\begin{pmatrix}
\frac{181}{100}&\frac{819}{1000}\\
\frac{819}{1000}&\frac{8181}{10000}
\end{pmatrix},
\]

whereas

\[
JJ^\top
=
\begin{pmatrix}
\frac{8181}{10000}&\frac{819}{1000}\\
\frac{819}{1000}&\frac{181}{100}
\end{pmatrix}.
\]

Therefore

\[
J^\top J\neq JJ^\top,
\]

so \(J\) is non-normal.

Asymptotic stability and normality are different properties.

## D4. Exact finite-horizon amplification

The fourth power is

\[
J^4
=
\begin{pmatrix}
\frac{567}{2500}&-\frac{729}{3125}\\
\frac{324}{125}&\frac{567}{2500}
\end{pmatrix}.
\]

Its singular values are approximately

\[
\sigma(J^4)
\approx
(2.610090585959495,\;0.251370585959495).
\]

Thus

\[
\boxed{
\|J^4\|_2\approx2.610090585959495>1.
}
\]

Even though every eigenvalue lies strictly inside the unit disk, there exists a unit perturbation amplified by more than \(2.6\times\) after four steps.

A Wolfram sweep over \(n=0,\ldots,20\) verifies that the peak in this range occurs at

\[
n=4.
\]

## D5. Eigenvalue stability does not bound transient gain

For a normal matrix \(N\),

\[
\|N^n\|_2=\rho(N)^n.
\]

For the non-normal \(J\), no such equality holds.

This is the exact bridge from the earlier Non-normality chapter: the optimizer-state update can be asymptotically stable while still having a large finite-horizon gain.

The conclusion is bounded to the linearized state map.

## D6. Fixed-point linearization versus trajectory-dependent dynamics

For a general augmented state

\[
z_{t+1}=F_t(z_t,\xi_t),
\]

a perturbation satisfies locally

\[
\delta z_{t+1}
\approx
J_t\,\delta z_t,
\qquad
J_t=
\frac{\partial F_t}{\partial z}(z_t,\xi_t).
\]

Over \(k\) steps,

\[
\delta z_{t+k}
\approx
J_{t+k-1}\cdots J_t\,\delta z_t.
\]

When \(J_t\) changes with \(t\), no single local eigenvalue calculation controls the whole product.

The autonomous quadratic example therefore demonstrates a mechanism, not a complete theory of nonlinear training.

## D7. Adam enlarges the state further

Adam maintains first- and second-moment state, schematically

\[
m_{t+1}
=
\beta_1m_t+(1-\beta_1)g_t,
\]

\[
v_{t+1}
=
\beta_2v_t+(1-\beta_2)g_t^2,
\]

followed by a parameter update using normalized moment estimates [@KingmaBa2015].

The exact state map is therefore higher-dimensional and state-dependent. The chapter uses momentum for its exact worked example because the mechanism is visible without hiding it inside a large Jacobian.

## D8. Relation to control-theoretic optimization analysis

Viewing iterative optimization as a feedback/dynamical system has a substantial literature. Lessard, Recht, and Packard analyze optimization algorithms with integral quadratic constraints from robust control [@LessardRechtPackard2016].

The Atlas use is narrower: it treats the optimizer-model pair as an augmented state and asks what finite-horizon behavior the local or time-varying Jacobian permits.

## D9. Learning-rate boundaries are coupled-state boundaries

For the scalar momentum quadratic, the characteristic polynomial depends jointly on

\[
\eta,\quad \beta,\quad h.
\]

Thus the linear stability boundary is not solely a property of curvature \(h\), nor solely a property of the learning rate \(\eta\), nor solely a property of momentum \(\beta\).

It is a property of the coupled recurrence.

This does not imply that every empirical learning-rate failure is explained by this local model.

## Claim boundary

This packet proves and computationally replays an exact one-dimensional quadratic momentum example and states the local Jacobian product for general augmented-state training. It does not claim that local linearization globally predicts nonlinear training, that every training spike is caused by non-normality, or that the toy parameters are representative of frontier-scale optimization.
