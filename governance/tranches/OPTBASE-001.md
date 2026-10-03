# OPTBASE-001 — First-Order Optimization

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- audited main at instantiation:
  \`532c076af66c8638c71a7ec91d6335bd8012e94f\`;
- issue:
  \`#58\`;
- hard prerequisite:
  - \`ATLAS-CH-DYN-001\` — audited \`draft-v0.1\`.

## Objective

Establish the conventional first-order optimization baseline that later Atlas chapters will reinterpret through:

- geometry;
- curvature;
- spectra;
- manifolds;
- optimizer-state dynamics;
- variational structure.

## A. Quadratic gradient-descent calibration

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

Therefore

\[
x_k
=
(1-\eta\lambda)^k x_0.
\]

Asymptotic convergence requires

\[
|1-\eta\lambda|<1,
\]

hence

\[
\boxed{
0<\eta<\frac2\lambda.
}
\]

Boundary cases are kept separate:

- \(\eta=0\): no motion;
- \(\eta=2/\lambda\): sign oscillation without decay.

## B. Exact unbiased-SGD toy

Sample losses:

\[
\ell_1(x)=\frac12(x-1)^2,
\qquad
\ell_2(x)=\frac12(x+1)^2.
\]

Uniform sample gradients:

\[
g_1=x-1,
\qquad
g_2=x+1.
\]

Exact replay gives:

\[
\mathbb E[g]=x=\nabla F(x),
\]

and

\[
\operatorname{Var}(g)=1.
\]

Frozen distinction:

\[
\text{unbiased}
\neq
\text{zero variance}.
\]

## C. Momentum and Nesterov-style lookahead

The chapter fixes one heavy-ball convention:

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

It also fixes one Nesterov-style lookahead convention:

\[
g_k
=
\nabla F(\theta_k-\eta\beta v_k),
\]

followed by the same momentum-state update.

The manuscript states explicitly that implementation conventions differ and that names do not substitute for equations.

## D. AdaGrad / RMSProp / Adam baseline

AdaGrad:

\[
G_{k,i}
=
G_{k-1,i}+g_{k,i}^2.
\]

RMSProp:

\[
v_k
=
\rho v_{k-1}
+
(1-\rho)g_k^2.
\]

Adam:

\[
m_k
=
\beta_1m_{k-1}
+
(1-\beta_1)g_k,
\]

\[
v_k
=
\beta_2v_{k-1}
+
(1-\beta_2)g_k^2,
\]

with standard bias corrections.

The original RMSProp source is explicitly labeled non-peer-reviewed course material.

## E. Exact Adam bias-correction witness

Use:

\[
g_1=3,
\qquad
\beta_1=9/10,
\qquad
\beta_2=99/100.
\]

With zero initial moments:

\[
m_1=3/10,
\qquad
v_1=9/100.
\]

Bias correction gives:

\[
\hat m_1=3,
\qquad
\hat v_1=9.
\]

For the calibration \(\varepsilon=0\):

\[
\frac{\hat m_1}{\sqrt{\hat v_1}}
=
1.
\]

The chapter explicitly states that practical Adam implementations use nonzero epsilon and that this witness isolates only the correction algebra.

## F. Exact gradient clipping witness

For

\[
g=(3,4),
\qquad
\|g\|_2=5,
\qquad
\tau=2,
\]

global norm clipping gives

\[
g_{\rm clip}
=
(6/5,8/5),
\]

with

\[
\|g_{\rm clip}\|_2=2.
\]

The chapter explicitly denies any general unbiasedness claim after clipping.

## G. Coupled versus decoupled decay

Coupled adaptive regularization:

\[
\theta_{\rm c}^+
=
\theta
-
\eta p(g+\lambda\theta).
\]

Decoupled weight decay:

\[
\theta_{\rm d}^+
=
(1-\eta\lambda)\theta
-
\eta p g.
\]

Difference:

\[
\theta_{\rm c}^+
-
\theta_{\rm d}^+
=
\eta\lambda\theta(1-p).
\]

Exact calibration:

\[
\theta=2,
\quad
g=3,
\quad
p=1/2,
\quad
\eta=1/10,
\quad
\lambda=1/5.
\]

Wolfram replay gives:

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

and

\[
\theta_{\rm c}^+
-
\theta_{\rm d}^+
=
1/50.
\]

This is the chapter's exact counterexample to blanket L2/weight-decay equivalence under adaptive preconditioning.

## H. Initialization second moments

Under explicit independence and zero-mean assumptions:

\[
z
=
\sum_{i=1}^{n}w_i x_i
\]

satisfies

\[
\mathbb E[z^2]
=
n\sigma_w^2q.
\]

Thus linear second-moment preservation uses

\[
\sigma_w^2=1/n.
\]

For symmetric preactivation and ReLU:

\[
\mathbb E[\operatorname{ReLU}(z)^2]
=
\frac12 n\sigma_w^2q.
\]

Thus second-moment preservation uses

\[
\sigma_w^2=2/n.
\]

The chapter deliberately says **second moment**, not exact post-ReLU variance.

## I. Schedules and warmup

The chapter treats schedules and warmup as algorithmic/training-recipe objects.

Vaswani et al. are used as one influential warmup plus inverse-square-root example.

No universal optimality or necessity theorem is claimed.

## J. Source boundary

Primary/foundational sources:

- Robbins–Monro:
  stochastic approximation;
- Polyak:
  momentum;
- Nesterov:
  accelerated first-order convex optimization;
- Duchi–Hazan–Singer:
  AdaGrad;
- Tieleman–Hinton:
  original RMSProp course material, explicitly non-peer-reviewed;
- Kingma–Ba:
  Adam;
- Loshchilov–Hutter:
  decoupled weight decay;
- Pascanu–Mikolov–Bengio:
  gradient clipping in recurrent-network training;
- Glorot–Bengio:
  variance/saturation-motivated initialization;
- He et al.:
  rectifier-aware initialization;
- Sutskever et al.:
  deep-learning momentum/initialization bridge;
- Vaswani et al.:
  bounded warmup/schedule example.

Atlas-specific synthesis is limited to organizing these mechanisms as components of a stateful update rule and preparing the later geometry/spectral/dynamics chapters.

## K. Figure

\`ATLAS-FIG-OPTBASE-001\`

- generator blob:
  \`61123040326f80ec73a170778ba1140ef3f8fcb9\`;
- rendered blob:
  \`7abd93008e812514667652200ec1d79ba89b5248\`;
- rendered bytes:
  \`176,645\`;
- representation class:
  exact.

Panels:

1. scalar quadratic amplification and convergence interval;
2. exact global-norm clipping geometry;
3. exact coupled/decoupled decay separation.

## L. Durable objects

The branch contains:

- \`sources/source-locks/ATLAS-CH-OPTBASE-001.yaml\`;
- \`manuscript/specifications/ATLAS-CH-OPTBASE-001.md\`;
- \`mathematics/derivations/ATLAS-CH-OPTBASE-001-DERIVATIONS.md\`;
- \`mathematics/computational-witnesses/ATLAS-CW-OPTBASE-001.md\`;
- \`manuscript/parts/05-optimization/ATLAS-CH-OPTBASE-001.md\`;
- Wolfram figure generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## M. Frozen distinctions

\[
\text{gradient}
\neq
\text{optimizer update}.
\]

\[
\text{unbiased}
\neq
\text{low variance}.
\]

\[
\text{momentum label}
\neq
\text{one universal recurrence convention}.
\]

\[
\text{clipping}
\neq
\text{unbiased rescaling}.
\]

\[
\text{coupled L2}
\neq
\text{decoupled weight decay under adaptive scaling}.
\]

\[
\text{second-moment initialization heuristic}
\neq
\text{exact deep-network distribution theorem}.
\]

\[
\text{warmup recipe}
\neq
\text{universal convergence theorem}.
\]

## N. Next step after merge

Run a bounded post-draft audit checking:

- quadratic stability interval and boundary cases;
- unbiased-SGD expectation/variance;
- momentum/Nesterov convention wording;
- Adam bias-correction witness;
- clipping geometry and unbiasedness boundary;
- coupled/decoupled decay counterexample;
- initialization second-moment assumptions;
- source status, including RMSProp;
- bibliography closure;
- Dynamics prerequisite pin;
- figure generator/master/manifest identity;
- chapter remains \`draft-v0.1\`.

Do not begin direct consumers until that audit merges.
