# ATLAS-CH-SHIFT-001 — Derivation Packet

## D1. Law typing

Let P be the source law and Q the deployment law on (X,Y). For a fixed predictor f,

\[
R_P(f)=\mathbb E_P[L(f(X),Y)],\qquad R_Q(f)=\mathbb E_Q[L(f(X),Y)].
\]

A statement about R_P does not become a statement about R_Q without assumptions relating the laws.

## D2. Covariate shift and reweighting

Assume

\[
P(Y\mid X)=Q(Y\mid X),\qquad Q_X\ll P_X.
\]

Let

\[
w(x)=\frac{dQ_X}{dP_X}(x).
\]

Then

\[
\begin{aligned}
R_Q(f)
&=\int L(f(x),y)Q(dy\mid x)Q_X(dx)\\
&=\int L(f(x),y)P(dy\mid x)w(x)P_X(dx)\\
&=\mathbb E_P[w(X)L(f(X),Y)].
\end{aligned}
\]

The absolute-continuity condition is essential.

## D3. Calibration-failure witness under pure covariate shift

Take X in {a,b}, deterministic conditionals Y(a)=1, Y(b)=0, and constant score s=1/2.

Under source law P_X=(1/2,1/2), the score group s=1/2 has event rate 1/2, so calibration gap is zero.

Under deployment law Q_X=(3/4,1/4), the same score group has event rate 3/4. Hence

\[
|3/4-1/2|=1/4.
\]

The predictor and conditional law Y|X are unchanged.

## D4. Brier-risk control

For s=1/2,

\[
(s-Y)^2=1/4
\]

for both Y=0 and Y=1. Therefore

\[
R_P^{\rm Brier}=R_Q^{\rm Brier}=1/4.
\]

Calibration failure under Q does not force this risk to change.

## D5. Exact importance weights for Witness A

\[
w(a)=\frac{3/4}{1/2}=3/2,\qquad w(b)=\frac{1/4}{1/2}=1/2.
\]

Normalization:

\[
\mathbb E_P[w(X)]=\frac12\frac32+\frac12\frac12=1.
\]

For event Y=1,

\[
\mathbb E_P[w(X)\mathbf 1\{Y=1\}]=\frac12\frac32=\frac34=Q(Y=1).
\]

## D6. Support failure

If P_X(b)=0 but Q_X(b)>0, then Q_X is not absolutely continuous with respect to P_X. No finite ordinary importance weight on source samples can represent target mass at b.

## D7. Benign marginal-shift control

Take X in {u,v}, deterministic Y(u)=0, Y(v)=1, and exact predictor f=Y.

Source marginal P_X=(1/2,1/2). Deployment marginal Q_X=(9/10,1/10).

Total variation is

\[
\operatorname{TV}(P_X,Q_X)=\frac12\left(|1/2-9/10|+|1/2-1/10|\right)=2/5.
\]

But every point is predicted correctly, so

\[
R_P^{0/1}=R_Q^{0/1}=0.
\]

A nonzero marginal shift statistic need not imply increased task risk.

## D8. Concept/conditional-shift control

Keep P_X=Q_X=(1/2,1/2), but reverse the deterministic labels under Q. Then P_X=Q_X while P(Y|X) differs from Q(Y|X). The source-perfect predictor has target error one. This cannot be corrected by an X-density ratio because that ratio is identically one.

## D9. Adversarial separation

Let X in {-1,+1}, Y=1[X=+1], and f(X)=Y. Clean risk is zero.

Let both perturbation sets equal {-1,+1}. Holding the original label fixed, the adversary can choose the opposite input, causing error one. Thus

\[
R_{\rm adv}=1
\]

despite

\[
R_P=0.
\]

## D10. Perturbation-set dependence

If instead Delta(x)={x}, then R_adv=R_P=0. Therefore adversarial robustness is relative to the declared perturbation set.

## D11. Metric firewall

The witnesses jointly show:
- calibration can change while Brier risk does not;
- marginal X-law can change while 0/1 risk does not;
- clean risk can be zero while adversarial risk is one;
- conditional shift can cause risk failure even with unchanged X-marginal.

No single scalar shift severity determines all metrics.

## D12. Structural sensitivity boundary

Let a structural parameter m index a mechanism T_m. A structural-sensitivity statement compares outputs, risks, or states under explicitly different m, e.g.

\[
\|F(T_{m_1})-F(T_{m_0})\|.
\]

Observed distributional change alone does not identify m_1-m_0 or establish a causal structural change.
