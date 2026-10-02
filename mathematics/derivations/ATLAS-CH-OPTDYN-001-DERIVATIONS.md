# ATLAS-CH-OPTDYN-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm convention:** spectral/operator (2)-norm unless explicitly stated  
**Source lock:** `sources/source-locks/ATLAS-CH-OPTDYN-001.yaml`

## D1. Momentum is an augmented-state dynamical system

Consider the scalar quadratic

[
L(	heta)=rac h2	heta^2,
qquad
h>0,
]

so

[
g(	heta)=h	heta.
]

Use the momentum recurrence

[
v_{t+1}=eta v_t+h	heta_t,
]

[
	heta_{t+1}=	heta_t-eta v_{t+1}.
]

Define the augmented state

[
z_t=
egin{pmatrix}
	heta_t\
v_t
end{pmatrix}.
]

Then

[
z_{t+1}=Jz_t
]

with

[
oxed{
J=
egin{pmatrix}
1-eta h & -etaeta\
h & eta
end{pmatrix}.
}
]

The optimizer's memory variable is therefore part of the state of the dynamical system, not merely an implementation detail.

## D2. Characteristic polynomial and asymptotic stability

The trace and determinant are

[
operatorname{tr}J
=
1+eta-eta h,
]

[
det J=eta.
]

Therefore

[
oxed{
p(lambda)
=
lambda^2
-
(1+eta-eta h)lambda
+
eta.
}
]

For a real second-order polynomial

[
lambda^2-	aulambda+eta
]

the Jury conditions for roots strictly inside the unit disk are

[
1-	au+eta>0,
]

[
1+	au+eta>0,
]

[
1-eta>0.
]

With (	au=1+eta-eta h), these become

[
eta h>0,
]

[
2(1+eta)-eta h>0,
]

[
eta<1.
]

For the usual momentum range (0leeta<1),

[
oxed{
0<eta h<2(1+eta)
}
]

is therefore the strict linear stability interval for this scalar quadratic recurrence.

## D3. A stable but non-normal optimizer-state example

Choose

[
h=1,qquad
eta=rac1{10},qquad
eta=rac9{10}.
]

Then

[
J=
egin{pmatrix}
0.9&-0.09\
1&0.9
end{pmatrix}.
]

The characteristic polynomial is

[
lambda^2-1.8lambda+0.9,
]

with eigenvalues

[
oxed{
lambda_{pm}
=
0.9pm0.3i.
}
]

Their common modulus is

[
|lambda_pm|
=
sqrt{0.9}
approx0.948683<1.
]

Thus the linear system is asymptotically stable.

Yet (J) is non-normal.

For the general real momentum matrix,

[
J^	op J-JJ^	op
=
egin{pmatrix}
h^2-eta^2eta^2
&
(etaeta+h)(-1+eta+eta h)
\
(etaeta+h)(-1+eta+eta h)
&
(etaeta-h)(etaeta+h)
end{pmatrix}.
]

For the chosen parameters this matrix is nonzero.

## D4. Finite-horizon amplification

Despite (ho(J)<1), Wolfram evaluation gives

[
|J|_2
approx1.5071525555.
]

Over (k=0,ldots,30), the peak is

[
oxed{
max_k|J^k|_2
=
2.61009058596ldots
}
]

at

[
oxed{k=4.}
]

The optimizer state can therefore amplify a perturbation by a factor greater than (2.6) over a short horizon even though both eigenvalues lie inside the unit circle.

This is the exact bridge from the previous Non-normality chapter into optimization.

## D5. Why a parameter-only state is insufficient

If one writes only

[
	heta_{t+1}=	heta_t-eta h	heta_t,
]

the model is ordinary gradient descent and has a one-dimensional state.

Momentum changes the system order. Eliminating (v_t) produces a second-order recurrence in (	heta); retaining (v_t) produces a first-order recurrence in a larger state.

These are equivalent descriptions.

The augmented-state form is preferable for the Atlas because it generalizes directly to optimizers with several memory variables.

## D6. Adam as a richer state system

Adam maintains first- and second-moment estimates:

[
m_t
=
eta_1m_{t-1}
+
(1-eta_1)g_t,
]

[
v_t
=
eta_2v_{t-1}
+
(1-eta_2)g_t^2.
]

With bias corrections

[
hat m_t
=
rac{m_t}{1-eta_1^t},
qquad
hat v_t
=
rac{v_t}{1-eta_2^t},
]

the parameter update is

[
	heta_t
=
	heta_{t-1}
-
alpha
rac{hat m_t}{sqrt{hat v_t}+epsilon}.
]

Thus a natural state contains at least

[
z_t=(	heta_t,m_t,v_t),
]

and, if the explicit bias-correction dependence is not absorbed into a time-varying map, the iteration counter (t) is also part of the state description.

The chapter uses Adam to establish the architectural point that modern optimizers are stateful. It does not use Adam for the exact non-normal example because the scalar momentum system exposes the mechanism with far less algebra.

## D7. Local linearization of a nonlinear optimizer

For a differentiable autonomous augmented update

[
z_{t+1}=F(z_t),
]

a small perturbation obeys locally

[
delta z_{t+1}
approx
J_F(z_t),delta z_t.
]

Over (k) steps,

[
oxed{
delta z_{t+k}
approx
J_F(z_{t+k-1})cdots J_F(z_t),delta z_t.
}
]

For a fixed point with constant Jacobian (J), this reduces to (J^k).

For actual training, the Jacobian is generally time-dependent because the loss curvature, mini-batch, schedule, and optimizer state change. Therefore a fixed-matrix eigenvalue analysis is a local model, not a global predictor.

## D8. Curvature and optimizer state are different objects

For the scalar quadratic, the Hessian is simply

[

abla^2L=h.
]

But the coupled Jacobian depends on

[
h,eta,eta.
]

Thus even in the simplest case the Hessian does not determine the optimizer dynamics by itself.

The loss geometry supplies part of the update. The optimizer introduces memory and gain structure of its own.

## D9. Control-theoretic connection

Optimization algorithms have been analyzed as feedback/dynamical systems, including through integral quadratic constraints. That literature provides rigorous precedent for treating an optimizer as an interconnected dynamical object rather than only as an algebraic rule.

The Atlas uses a simpler local Jacobian language here because its later diagnostic programme needs quantities that can be estimated along training trajectories.

## D10. CPS boundary

The Atlas architecture names **Coupling-Phase Spectroscopy (CPS)** as a downstream GCL programme concerned with optimizer-state Jacobian probes and phase-transition diagnostics.

No separate public GCL source for the exact CPS phrase was found in the organization search performed for this source lock. Therefore this chapter may motivate the instrumentation question but must not attach specific empirical CPS results until an exact source object is bound.

## Source boundary

- Heavy-ball/multistep origin: `OPTDYN-POLYAK-1964`.
- Momentum in deep learning: `OPTDYN-SUTSKEVER-ETAL-2013`.
- Adam formulation: `OPTDYN-KINGMA-BA-2015`.
- Control-theoretic optimization analysis: `OPTDYN-LESSARD-RECHT-PACKARD-2016`.

The augmented-state Jacobian, scalar stability derivation, and stable non-normal worked example are Atlas-owned derivations.
