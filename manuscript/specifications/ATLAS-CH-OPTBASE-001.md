# Chapter Specification — ATLAS-CH-OPTBASE-001

## Identity

**Title:** First-Order Optimization  
**Part:** Optimization  
**Status:** specification-ready.  
**Epistemic class:** established first-order optimization + bounded deep-learning practice.

## Chapter contract

Establish the conventional first-order optimization baseline that later Atlas chapters will reinterpret geometrically, spectrally, dynamically, and compositionally.

The chapter must be precise enough that later chapters can say exactly what they modify.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-DYN-001\`.

May assume:

- discrete dynamical-system language;
- local stability terminology;
- basic linear algebra and probability.

Must not assume:

- second-order methods;
- natural gradient;
- manifold optimization;
- Shampoo/Muon/spectral shaping;
- optimizer-state Jacobian analysis;
- benign-nonconvexity theory.

## Reader outcome

A reader should be able to:

1. derive the scalar quadratic gradient-descent stability condition;
2. distinguish full-batch and unbiased stochastic gradients;
3. write heavy-ball and Nesterov-style updates without conflating conventions;
4. explain AdaGrad, RMSProp, and Adam as coordinatewise adaptive scaling mechanisms;
5. derive Adam's first-step bias correction in an exact scalar example;
6. distinguish coupled L2 regularization from decoupled weight decay under adaptive preconditioning;
7. derive exact norm clipping for a vector;
8. distinguish clipping from unbiased stochastic estimation;
9. derive fan-in second-moment preservation under explicit independence assumptions;
10. explain why warmup and schedules are optimization recipes, not universal theorems.

## Formal spine

### Gradient descent

For differentiable objective \(F(\theta)\),

\[
\theta_{k+1}
=
\theta_k-\eta\nabla F(\theta_k).
\]

### Scalar quadratic calibration

Use

\[
F(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]

Then

\[
x_{k+1}
=
(1-\eta\lambda)x_k.
\]

Asymptotic convergence to zero requires

\[
|1-\eta\lambda|<1,
\]

hence

\[
\boxed{
0<\eta<\frac{2}{\lambda}.
}
\]

Boundary values should be interpreted separately.

### Unbiased SGD toy

Define sample losses

\[
\ell_1(x)=\frac12(x-1)^2,
\qquad
\ell_2(x)=\frac12(x+1)^2,
\]

sampled uniformly.

The population/finite-average objective is

\[
F(x)
=
\frac12(\ell_1(x)+\ell_2(x)).
\]

Sample gradients are

\[
g_1=x-1,
\qquad
g_2=x+1.
\]

Verify

\[
\mathbb E[g_i]=x=\nabla F(x).
\]

Also compute nonzero variance.

### Heavy-ball momentum

Use one explicit convention:

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

State that momentum conventions differ by scaling/sign choices.

### Nesterov-style lookahead

Use the convention

\[
g_k
=
\nabla F(\theta_k-\eta\beta v_k),
\]

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

Treat this as one common implementation-equivalent parameterization, not the only canonical formula.

### AdaGrad

Coordinatewise accumulator

\[
G_{k,i}
=
G_{k-1,i}+g_{k,i}^2,
\]

and update

\[
\theta_{k+1,i}
=
\theta_{k,i}
-
\eta\frac{g_{k,i}}{\sqrt{G_{k,i}}+\varepsilon}.
\]

### RMSProp

Exponential second-moment estimate

\[
v_k
=
\rho v_{k-1}
+
(1-\rho)g_k^2
\]

coordinatewise, followed by inverse-root scaling.

Label the original RMSProp source as non-peer-reviewed course material.

### Adam

Use

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

with

\[
\hat m_k
=
\frac{m_k}{1-\beta_1^k},
\qquad
\hat v_k
=
\frac{v_k}{1-\beta_2^k}.
\]

## Exact witness A — Adam first step

Take

\[
g_1=3,
\qquad
\beta_1=\frac9{10},
\qquad
\beta_2=\frac{99}{100},
\]

with zero initial moments.

Then

\[
m_1=\frac3{10},
\qquad
v_1=\frac9{100},
\]

and

\[
\hat m_1=3,
\qquad
\hat v_1=9.
\]

For the calibration \(\varepsilon=0\), the normalized direction is exactly

\[
\frac{\hat m_1}{\sqrt{\hat v_1}}=1.
\]

The chapter must state that practical implementations use nonzero epsilon.

## Exact witness B — gradient clipping

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
g\min\left(1,\frac{\tau}{\|g\|_2}\right)
=
\left(\frac65,\frac85\right),
\]

with

\[
\|g_{\rm clip}\|_2=2.
\]

## Exact witness C — coupled versus decoupled decay

Let scalar preconditioner be \(p>0\).

Coupled regularization:

\[
\theta_{\rm c}^+
=
\theta-\eta p(g+\lambda\theta).
\]

Decoupled weight decay:

\[
\theta_{\rm d}^+
=
(1-\eta\lambda)\theta-\eta p g.
\]

Difference:

\[
\theta_{\rm c}^+-\theta_{\rm d}^+
=
\eta\lambda\theta(1-p).
\]

Use

\[
\theta=2,\quad
g=3,\quad
p=\frac12,\quad
\eta=\frac1{10},\quad
\lambda=\frac15.
\]

Then

\[
\theta_{\rm c}^+=\frac{183}{100},
\qquad
\theta_{\rm d}^+=\frac{181}{100}.
\]

Thus adaptive preconditioning breaks the general equivalence.

## Initialization derivation

Let

\[
z=\sum_{i=1}^{n}w_i x_i,
\]

with:

- independent \(w_i\) and \(x_i\);
- zero means;
- identical input second moment \(q=\mathbb E[x_i^2]\);
- identical weight variance \(\sigma_w^2\).

Then

\[
\mathbb E[z^2]
=
n\sigma_w^2q.
\]

For linear/approximately symmetric propagation, choosing

\[
\sigma_w^2=\frac1n
\]

preserves the second moment.

For symmetric preactivation \(z\) and ReLU,

\[
\mathbb E[\operatorname{ReLU}(z)^2]
=
\frac12\mathbb E[z^2].
\]

Thus choosing

\[
\sigma_w^2=\frac2n
\]

preserves the second moment across the ReLU under the declared assumptions.

The chapter must not silently call this exact variance preservation after ReLU because the ReLU output generally has nonzero mean.

## Learning-rate schedules and warmup

Include:

- constant schedule;
- piecewise/cosine/decay examples at descriptive level;
- warmup as a deliberate early low-step-size regime;
- Vaswani et al. as one influential warmup/inverse-square-root example.

No universal optimality claim.

## Principal pedagogical device

### Allegory: steering versus changing the road

The raw gradient points downhill in the coordinate system of the parameters.

Momentum, adaptive scaling, clipping, schedules, and decay alter how that direction is converted into motion.

Correspondence:

- gradient ↔ local slope signal;
- learning rate ↔ step scale;
- preconditioner ↔ coordinate-dependent steering;
- clipping ↔ speed limiter;
- momentum ↔ inertial state;
- weight decay ↔ shrinkage mechanism.

Limit:

Optimization is not literal mechanics, and different optimizer conventions can encode the same recurrence with different state variables.

## Figure programme

### ATLAS-FIG-OPTBASE-001

Three panels:

1. scalar quadratic amplification \(|1-\eta\lambda|\) versus \(\eta\lambda\), marking convergence interval \(0<\eta\lambda<2\);
2. exact norm-clipping geometry for \(g=(3,4)\), \(\tau=2\);
3. coupled versus decoupled scalar decay under \(p=1/2\), displaying exact next iterates.

Representation class: exact/data-derived.

## Failure boundaries

Include:

- a stable quadratic step size need not be stable for another curvature scale;
- unbiased gradient does not mean low-variance gradient;
- clipping changes the gradient estimator;
- adaptive scaling can magnify small-gradient coordinates;
- Adam bias correction does not make Adam universally convergent;
- coupled L2 and decoupled weight decay differ under adaptive preconditioning;
- initialization calculations are assumption-dependent;
- warmup/schedule choices are recipes, not general theorems.

## Downstream obligations

Direct consumers:

- \`ATLAS-CH-SECOND-001\`;
- \`ATLAS-CH-MANOPT-001\`;
- \`ATLAS-CH-CONTINUAL-001\`;
- \`ATLAS-CH-CURRICULUM-001\`.

Also supports:

- \`ATLAS-CH-OPTDYN-001\`;
- \`ATLAS-CH-MUON-001\`;
- \`ATLAS-CH-BENIGN-001\`.

## Sources

- [@RobbinsMonro1951]
- [@Polyak1964]
- [@Nesterov2004]
- [@DuchiHazanSinger2011]
- [@TielemanHinton2012]
- [@KingmaBa2015]
- [@LoshchilovHutter2019AdamW]
- [@PascanuMikolovBengio2013]
- [@GlorotBengio2010]
- [@HeEtAl2015]
- [@SutskeverEtAl2013]
- [@VaswaniEtAl2017]

Source lock: \`sources/source-locks/ATLAS-CH-OPTBASE-001.yaml\`.

## Acceptance

The draft must:

- derive quadratic GD stability exactly;
- include an exact unbiased-SGD witness and variance;
- state one explicit heavy-ball and Nesterov convention;
- distinguish AdaGrad/RMSProp/Adam state;
- replay Adam first-step bias correction exactly;
- replay clipping exactly;
- prove coupled/decoupled decay difference under adaptive scaling;
- derive second-moment initialization under explicit assumptions;
- keep schedules/warmup at bounded recipe status;
- include source lock, computational witness, figure provenance, and post-draft audit.
