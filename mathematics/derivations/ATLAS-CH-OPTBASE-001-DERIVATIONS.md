# ATLAS-CH-OPTBASE-001 — Derivation Packet

## D1. Gradient descent as a discrete dynamical system

For differentiable objective

\[
F:\mathbb R^d\to\mathbb R,
\]

gradient descent is

\[
\theta_{k+1}
=
\theta_k-\eta\nabla F(\theta_k).
\]

The optimizer therefore defines a discrete map

\[
\Psi(\theta)
=
\theta-\eta\nabla F(\theta).
\]

Its stability depends on both the objective geometry and the step size.

## D2. Scalar quadratic stability

Take

\[
F(x)
=
\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]

Then

\[
\nabla F(x)
=
\lambda x,
\]

so

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

Asymptotic convergence to zero requires

\[
|1-\eta\lambda|<1.
\]

Solving:

\[
-1
<
1-\eta\lambda
<
1.
\]

Subtract one:

\[
-2
<
-\eta\lambda
<
0.
\]

Multiply by \(-1\) and reverse inequalities:

\[
0
<
\eta\lambda
<
2.
\]

Hence

\[
\boxed{
0<\eta<\frac2\lambda.
}
\]

At

\[
\eta=0,
\]

the state does not move.

At

\[
\eta=\frac2\lambda,
\]

the amplification factor is \(-1\), producing non-decaying sign oscillation.

The strict interior is the asymptotically convergent region.

## D3. Finite unbiased-SGD witness

Define two sample losses:

\[
\ell_1(x)
=
\frac12(x-1)^2,
\]

\[
\ell_2(x)
=
\frac12(x+1)^2.
\]

Sample uniformly from the two losses.

The finite-average objective is

\[
F(x)
=
\frac12\left(\ell_1(x)+\ell_2(x)\right).
\]

Expanding,

\[
F(x)
=
\frac14\left((x-1)^2+(x+1)^2\right)
=
\frac12x^2+\frac12.
\]

Thus

\[
\nabla F(x)=x.
\]

The sample gradients are

\[
g_1=x-1,
\]

\[
g_2=x+1.
\]

Their expectation is

\[
\mathbb E[g]
=
\frac12(g_1+g_2)
=
x
=
\nabla F(x).
\]

Thus the stochastic gradient is unbiased.

The deviations from the mean are

\[
g_1-x=-1,
\]

and

\[
g_2-x=1.
\]

Therefore

\[
\operatorname{Var}(g)
=
\frac12(1^2+1^2)
=
1.
\]

Hence:

\[
\boxed{
\text{unbiased}
\not\Rightarrow
\text{zero variance}.
}
\]

## D4. Heavy-ball momentum convention

Use the explicit state convention

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

The optimizer state is now

\[
s_k=(\theta_k,v_k).
\]

Momentum is therefore not merely “a larger gradient step.”

It adds memory.

Alternative sign/scaling conventions are common.

The chapter treats equations, not names, as the canonical object.

## D5. Nesterov-style lookahead convention

One common deep-learning parameterization evaluates the gradient at a lookahead state:

\[
g_k
=
\nabla F(\theta_k-\eta\beta v_k),
\]

then applies

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

Classical Nesterov acceleration has several equivalent forms after changes of variables in appropriate settings.

The chapter does not identify all implementation conventions as algebraically identical without stating the transformation.

## D6. AdaGrad

For coordinate \(i\), define accumulated squared gradient

\[
G_{k,i}
=
G_{k-1,i}+g_{k,i}^2.
\]

Then

\[
\theta_{k+1,i}
=
\theta_{k,i}
-
\eta
\frac{g_{k,i}}
{\sqrt{G_{k,i}}+\varepsilon}.
\]

Coordinates with historically large squared gradients receive smaller effective step scales.

This is an adaptive diagonal preconditioner.

## D7. RMSProp

RMSProp replaces unbounded accumulation by an exponential moving average:

\[
v_k
=
\rho v_{k-1}
+
(1-\rho)g_k^2.
\]

Then, coordinatewise,

\[
\theta_{k+1}
=
\theta_k
-
\eta
\frac{g_k}
{\sqrt{v_k}+\varepsilon}.
\]

The original algorithmic description is from non-peer-reviewed course material [@TielemanHinton2012].

## D8. Adam

Adam combines a first-moment estimate

\[
m_k
=
\beta_1m_{k-1}
+
(1-\beta_1)g_k
\]

with a second raw-moment estimate

\[
v_k
=
\beta_2v_{k-1}
+
(1-\beta_2)g_k^2.
\]

With zero initialization, early moments are biased toward zero.

Bias corrections are

\[
\hat m_k
=
\frac{m_k}{1-\beta_1^k},
\]

\[
\hat v_k
=
\frac{v_k}{1-\beta_2^k}.
\]

A standard update is

\[
\theta_{k+1}
=
\theta_k
-
\eta
\frac{\hat m_k}
{\sqrt{\hat v_k}+\varepsilon}.
\]

## D9. Exact Adam first-step witness

Take

\[
g_1=3,
\]

\[
\beta_1=\frac9{10},
\]

and

\[
\beta_2=\frac{99}{100},
\]

with

\[
m_0=v_0=0.
\]

Then

\[
m_1
=
\left(1-\frac9{10}\right)3
=
\frac3{10}.
\]

Also

\[
v_1
=
\left(1-\frac{99}{100}\right)3^2
=
\frac9{100}.
\]

Bias correction gives

\[
\hat m_1
=
\frac{3/10}{1/10}
=
3,
\]

and

\[
\hat v_1
=
\frac{9/100}{1/100}
=
9.
\]

For the calibration

\[
\varepsilon=0,
\]

the normalized Adam direction is

\[
\frac{\hat m_1}{\sqrt{\hat v_1}}
=
1.
\]

Practical Adam implementations use nonzero epsilon.

The zero-epsilon witness isolates the bias-correction algebra only.

## D10. Gradient clipping

Global Euclidean norm clipping at threshold \(\tau>0\) is

\[
g_{\mathrm{clip}}
=
g
\min\left(
1,
\frac{\tau}{\|g\|_2}
\right).
\]

Take

\[
g=(3,4).
\]

Then

\[
\|g\|_2=5.
\]

For

\[
\tau=2,
\]

the scale factor is

\[
\frac25.
\]

Therefore

\[
g_{\mathrm{clip}}
=
\left(
\frac65,
\frac85
\right),
\]

and

\[
\|g_{\mathrm{clip}}\|_2=2.
\]

Clipping is nonlinear in \(g\).

Therefore, in general,

\[
\mathbb E[\operatorname{clip}(g)]
\neq
\operatorname{clip}(\mathbb E[g]).
\]

The chapter does not treat clipped stochastic gradients as unbiased.

## D11. Coupled L2 regularization

Suppose an optimizer applies scalar adaptive preconditioner \(p>0\).

If an L2 penalty

\[
\frac{\lambda}{2}\theta^2
\]

is added to the loss, the gradient becomes

\[
g+\lambda\theta.
\]

A coupled adaptive update is

\[
\boxed{
\theta_{\mathrm c}^+
=
\theta
-
\eta p(g+\lambda\theta).
}
\]

The preconditioner scales both the task gradient and regularization gradient.

## D12. Decoupled weight decay

Decoupled weight decay instead applies shrinkage separately:

\[
\boxed{
\theta_{\mathrm d}^+
=
(1-\eta\lambda)\theta
-
\eta p g.
}
\]

Subtract:

\[
\begin{aligned}
\theta_{\mathrm c}^+
-
\theta_{\mathrm d}^+
&=
\theta
-
\eta p g
-
\eta p\lambda\theta
-
\theta
+
\eta\lambda\theta
+
\eta p g\\
&=
\eta\lambda\theta(1-p).
\end{aligned}
\]

Therefore

\[
\boxed{
\theta_{\mathrm c}^+
=
\theta_{\mathrm d}^+
}
\]

only in special cases such as

\[
p=1,
\]

or zero decay/state.

Adaptive scaling generally breaks the equivalence.

## D13. Exact coupled/decoupled counterexample

Take

\[
\theta=2,
\qquad
g=3,
\qquad
p=\frac12,
\qquad
\eta=\frac1{10},
\qquad
\lambda=\frac15.
\]

Coupled:

\[
\theta_{\mathrm c}^+
=
2
-
\frac1{10}\frac12
\left(
3+\frac15\cdot2
\right).
\]

Thus

\[
\theta_{\mathrm c}^+
=
\frac{183}{100}.
\]

Decoupled:

\[
\theta_{\mathrm d}^+
=
\left(
1-\frac1{10}\frac15
\right)2
-
\frac1{10}\frac12\cdot3,
\]

so

\[
\theta_{\mathrm d}^+
=
\frac{181}{100}.
\]

Difference:

\[
\boxed{
\theta_{\mathrm c}^+
-
\theta_{\mathrm d}^+
=
\frac1{50}.
}
\]

This is an exact counterexample to blanket equivalence under adaptive preconditioning.

## D14. Initialization and second moments

Consider a preactivation

\[
z
=
\sum_{i=1}^{n}w_i x_i.
\]

Assume:

- \(w_i\) are mutually independent;
- \(x_i\) are mutually independent;
- weights and inputs are independent;
- \(\mathbb E[w_i]=0\);
- \(\mathbb E[x_i]=0\);
- \(\mathbb E[x_i^2]=q\);
- \(\operatorname{Var}(w_i)=\sigma_w^2\).

Then cross terms vanish and

\[
\mathbb E[z^2]
=
\sum_{i=1}^{n}
\mathbb E[w_i^2]
\mathbb E[x_i^2].
\]

Hence

\[
\boxed{
\mathbb E[z^2]
=
n\sigma_w^2 q.
}
\]

To preserve input second moment through a linear preactivation, choose

\[
\sigma_w^2
=
\frac1n.
\]

This is the core fan-in scaling idea behind variance-oriented initialization.

## D15. ReLU second moment

Suppose the preactivation distribution is symmetric about zero.

Then

\[
\operatorname{ReLU}(z)^2
=
z^2\mathbf 1_{\{z>0\}}.
\]

By symmetry,

\[
\mathbb E[z^2\mathbf 1_{\{z>0\}}]
=
\frac12\mathbb E[z^2].
\]

Therefore

\[
\mathbb E[\operatorname{ReLU}(z)^2]
=
\frac12 n\sigma_w^2q.
\]

Choosing

\[
\boxed{
\sigma_w^2
=
\frac2n
}
\]

preserves the second moment:

\[
\mathbb E[\operatorname{ReLU}(z)^2]=q.
\]

This is a second-moment statement under the declared assumptions.

Because ReLU generally produces nonzero mean, the chapter does not silently replace “second moment” with “variance.”

## D16. Learning-rate schedules

A schedule replaces constant \(\eta\) with

\[
\eta_k.
\]

Examples include:

- piecewise decay;
- cosine decay;
- inverse-power decay;
- warmup followed by decay.

A warmup phase deliberately begins with smaller effective step sizes before reaching the main scale.

Vaswani et al. provide one influential warmup plus inverse-square-root schedule [@VaswaniEtAl2017].

This is an architecture/training recipe example, not a universal convergence theorem.

## D17. First-order baseline and later geometry

The baseline optimizer can be written schematically as

\[
\theta_{k+1}
=
\theta_k
-
\eta_k P_k g_k
+
\text{other state-dependent terms}.
\]

Here:

- \(g_k\) is the gradient signal;
- \(P_k\) is an identity or adaptive diagonal preconditioner;
- momentum introduces extra state;
- clipping alters the signal before update;
- decay adds shrinkage;
- schedules alter time-dependent scale.

Later Atlas chapters will replace or generalize these pieces using:

- matrix geometry;
- spectral shaping;
- manifold constraints;
- variational principles;
- optimizer-state diagnostics.

## Claim boundary

This packet establishes exact toy facts about first-order updates and derives second-moment initialization under explicit assumptions.

It does not claim universal optimizer rankings, global nonconvex convergence, unbiasedness after clipping, equivalence of coupled and decoupled decay under adaptive scaling, or exact deep-network distribution preservation by fan-in heuristics.
