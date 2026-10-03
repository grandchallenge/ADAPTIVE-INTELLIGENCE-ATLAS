# AUDIT-012 — First-Order Optimization

## Disposition

**PASS AFTER TWO PRECISION REPAIRS**

\`ATLAS-CH-OPTBASE-001\` remains at \`draft-v0.1\`.

The chapter's quadratic stability calculation, stochastic-gradient witness, momentum/adaptive-update definitions, Adam bias correction, coupled/decoupled decay counterexample, initialization second-moment derivation, source scope, and figure provenance pass audit.

Two local precision repairs were required:

1. the opening “gradient = steepest direction” language is now explicitly scoped to the Euclidean inner product / unit Euclidean directions;
2. global norm clipping is now defined piecewise with \(\operatorname{clip}(0)=0\), avoiding an implicit division-by-zero convention.

No optimizer is promoted as universally superior.

## Audited baseline

- OPTBASE-001 merge:
  \`712dcc370b3ad0813a22c9cbec998acbc05e16b1\`;
- audit issue:
  \`#60\`;
- chapter:
  \`ATLAS-CH-OPTBASE-001\`.

## 1. Euclidean gradient / steepest direction

PASS AFTER REPAIR.

The chapter now states the metric explicitly.

For nonzero Euclidean gradient,

\[
D F(\theta)[u]
=
\nabla F(\theta)^\top u.
\]

By Cauchy--Schwarz, among directions satisfying

\[
\|u\|_2=1,
\]

the maximal directional derivative occurs at

\[
u_\star
=
\frac{\nabla F(\theta)}
{\|\nabla F(\theta)\|_2}.
\]

Thus

\[
-\nabla F(\theta)
\]

is the Euclidean steepest-descent direction.

The manuscript now explicitly points forward to later geometry chapters, where changing the metric changes what “steepest” means.

## 2. Scalar quadratic gradient descent

PASS.

For

\[
F(x)
=
\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]

gradient descent gives

\[
x_{k+1}
=
(1-\eta\lambda)x_k.
\]

Independent symbolic replay solves

\[
|1-\eta\lambda|<1
\]

as

\[
\boxed{
0<\eta<\frac2\lambda.
}
\]

Boundary cases are handled correctly:

- \(\eta=0\): no motion;
- \(\eta=2/\lambda\): non-decaying sign alternation.

## 3. Unbiased-SGD witness

PASS.

Sample gradients:

\[
g_1=x-1,
\qquad
g_2=x+1.
\]

Uniform expectation:

\[
\mathbb E[g]=x.
\]

The finite-average objective has gradient

\[
\nabla F(x)=x.
\]

Independent replay gives

\[
\operatorname{Var}(g)=1.
\]

The manuscript therefore correctly freezes:

\[
\text{unbiased}
\not\Rightarrow
\text{low variance}.
\]

## 4. Momentum convention

PASS.

The chapter fixes one explicit heavy-ball convention:

\[
v_{k+1}
=
\beta v_k+g_k,
\]

\[
\theta_{k+1}
=
\theta_k-\eta v_{k+1}.
\]

It explicitly states that sign/scaling conventions differ across implementations and that the recurrence, not the label, is the canonical object.

## 5. Nesterov-style lookahead

PASS.

The chapter uses the declared convention

\[
g_k
=
\nabla F(\theta_k-\eta\beta v_k),
\]

then

\[
v_{k+1}
=
\beta v_k+g_k,
\]

\[
\theta_{k+1}
=
\theta_k-\eta v_{k+1}.
\]

It does not claim that every implementation convention is literally identical without a change of variables, nor does it transfer convex acceleration guarantees to generic deep nonconvex networks.

## 6. AdaGrad

PASS.

The coordinatewise accumulator

\[
G_{k,i}
=
G_{k-1,i}+g_{k,i}^2
\]

and inverse-root update scaling are stated correctly.

The chapter describes this as an adaptive diagonal preconditioner, not as exact curvature inversion.

## 7. RMSProp

PASS.

The chapter uses

\[
v_k
=
\rho v_{k-1}
+
(1-\rho)g_k^2
\]

with inverse-root coordinate scaling.

The original Tieleman--Hinton source is explicitly labeled:

- course lecture material;
- non-peer-reviewed.

No stronger source status is implied.

## 8. Adam moment and bias-correction algebra

PASS.

With

\[
g_1=3,
\qquad
\beta_1=9/10,
\qquad
\beta_2=99/100,
\]

and zero initial moments, independent replay gives

\[
m_1=3/10,
\]

\[
v_1=9/100,
\]

\[
\hat m_1=3,
\]

\[
\hat v_1=9.
\]

For the deliberately simplified calibration

\[
\varepsilon=0,
\]

the normalized direction is

\[
1.
\]

The manuscript explicitly states that practical implementations use nonzero epsilon and that the witness isolates only the bias-correction algebra.

## 9. Gradient clipping

PASS AFTER REPAIR.

The general global Euclidean norm-clipping definition is now

\[
g_{\rm clip}
=
\begin{cases}
0, & g=0,\\[4pt]
g\min\left(
1,
\frac{\tau}{\|g\|_2}
\right), & g\neq0.
\end{cases}
\]

Thus the definition is total.

For

\[
g=(3,4),
\qquad
\tau=2,
\]

independent replay gives

\[
\|g\|_2=5,
\]

\[
g_{\rm clip}
=
(6/5,8/5),
\]

and

\[
\|g_{\rm clip}\|_2=2.
\]

## 10. Clipping and unbiasedness

PASS.

The chapter states that clipping is nonlinear and therefore in general

\[
\mathbb E[\operatorname{clip}(g)]
\neq
\operatorname{clip}(\mathbb E[g]).
\]

It does not treat a clipped stochastic gradient as automatically unbiased.

## 11. Coupled L2 versus decoupled decay

PASS.

The chapter compares

\[
\theta_{\rm c}^+
=
\theta-\eta p(g+\lambda\theta)
\]

with

\[
\theta_{\rm d}^+
=
(1-\eta\lambda)\theta-\eta p g.
\]

Their difference is

\[
\boxed{
\theta_{\rm c}^+
-
\theta_{\rm d}^+
=
\eta\lambda\theta(1-p).
}
\]

For

\[
\theta=2,
\quad
g=3,
\quad
p=1/2,
\quad
\eta=1/10,
\quad
\lambda=1/5,
\]

independent replay gives

\[
\theta_{\rm c}^+
=
183/100,
\]

\[
\theta_{\rm d}^+
=
181/100,
\]

with exact difference

\[
1/50.
\]

The manuscript correctly confines plain L2/weight-decay equivalence to the simple unpreconditioned setting.

## 12. Initialization second moment

PASS.

Under the declared assumptions:

- independent zero-mean weights;
- independent zero-mean inputs;
- weight/input independence;
- common input second moment \(q\);
- weight variance \(\sigma_w^2\);

the chapter derives

\[
\mathbb E[z^2]
=
n\sigma_w^2q.
\]

Thus

\[
\sigma_w^2=1/n
\]

preserves the linear second moment.

## 13. ReLU second moment

PASS.

For symmetric preactivation distribution,

\[
\mathbb E[\operatorname{ReLU}(z)^2]
=
\frac12\mathbb E[z^2].
\]

Hence

\[
\sigma_w^2=2/n
\]

preserves the second moment under the declared model.

The manuscript explicitly avoids calling this exact post-ReLU variance preservation because the ReLU output generally has nonzero mean.

## 14. Schedules and warmup

PASS.

The chapter treats schedules and warmup as time-dependent algorithm/training-recipe choices.

Vaswani et al. are used only as one influential warmup plus inverse-square-root example.

No universal necessity or optimality theorem is claimed.

## 15. Source scope

PASS.

The source roles are bounded as follows:

- Robbins--Monro:
  stochastic approximation;
- Polyak:
  momentum;
- Nesterov:
  accelerated first-order convex optimization;
- Duchi--Hazan--Singer:
  AdaGrad;
- Tieleman--Hinton:
  RMSProp algorithmic source, non-peer-reviewed;
- Kingma--Ba:
  Adam update and bias corrections;
- Loshchilov--Hutter:
  decoupled weight decay;
- Pascanu--Mikolov--Bengio:
  gradient clipping in recurrent-network training;
- Glorot--Bengio:
  initialization/variance motivation;
- He et al.:
  rectifier-aware initialization;
- Sutskever et al.:
  bounded deep-learning momentum/initialization bridge;
- Vaswani et al.:
  one schedule/warmup example.

No source is used to establish a universal optimizer ranking.

## 16. Internal provenance

PASS.

The source lock pins the audited Dynamics manuscript at

\`f4aa89075f221529401e56a152a6cdfca3dcc47d\`.

The seed inventory pin is

\`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

Both were independently re-fetched from baseline

\`532c076af66c8638c71a7ec91d6335bd8012e94f\`

and match exactly.

## 17. Bibliography closure

PASS.

All declared citation keys resolve:

- \`RobbinsMonro1951\`;
- \`Polyak1964\`;
- \`Nesterov2004\`;
- \`DuchiHazanSinger2011\`;
- \`TielemanHinton2012\`;
- \`KingmaBa2015\`;
- \`LoshchilovHutter2019AdamW\`;
- \`PascanuMikolovBengio2013\`;
- \`GlorotBengio2010\`;
- \`HeEtAl2015\`;
- \`SutskeverEtAl2013\`;
- \`VaswaniEtAl2017\`.

## 18. Figure provenance

PASS.

\`ATLAS-FIG-OPTBASE-001\`:

- generator blob:
  \`61123040326f80ec73a170778ba1140ef3f8fcb9\`;
- rendered blob:
  \`7abd93008e812514667652200ec1d79ba89b5248\`;
- rendered bytes:
  \`176,645\`.

The manifest matches the audited Git tree.

The panels encode exact toy quantities only:

1. scalar quadratic amplification;
2. norm clipping;
3. coupled/decoupled adaptive decay.

## 19. Chapter status

PASS.

\`ATLAS-CH-OPTBASE-001\` remains:

\`draft-v0.1\`.

Its hard prerequisite remains:

- \`ATLAS-CH-DYN-001\`.

## 20. Final disposition

AUDIT-012 passes after two precision repairs.

The durable first-order baseline now explicitly separates:

\[
\text{Euclidean gradient signal}
\neq
\text{optimizer motion},
\]

\[
\text{unbiased stochastic gradient}
\neq
\text{low-variance gradient},
\]

\[
\text{clipping}
\neq
\text{unbiased transformation},
\]

and

\[
\text{coupled L2 regularization}
\neq
\text{decoupled weight decay under adaptive scaling}.
\]

Direct consumers may now be unlocked once this audit merges.
