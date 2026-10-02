# Optimizer-State Dynamics
<!-- ATLAS-CH-OPTDYN-001 -->

**Epistemic status:** mathematical exposition built from canonical optimizer formulations, control-theoretic optimization analysis, the preceding Non-normality chapter, and Atlas-owned augmented-state derivations.  
**Primary figure:** \`ATLAS-FIG-OPTDYN-001\`  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-OPTDYN-001-DERIVATIONS.md\`

## 1. The optimizer is part of the state

A common picture of training writes

\[
\theta_{t+1}
=
\theta_t-\eta\nabla L(\theta_t).
\]

That picture is exact for plain gradient descent.

For momentum, Adam, and many modern optimizers it is incomplete.

The update at time \(t+1\) depends not only on the current parameters but also on internal state accumulated from previous gradients. Momentum carries velocity-like state. Adam carries first- and second-moment estimates [@KingmaBa2015]. Other methods maintain matrices, preconditioners, or moving statistics.

The mathematical object is therefore not only \(\theta_t\).

It is an augmented state,

\[
z_t=(\theta_t,s_t),
\]

with update

\[
z_{t+1}
=
F_t(z_t,\xi_t),
\]

where \(s_t\) is optimizer state and \(\xi_t\) represents data or stochastic forcing.

This chapter asks:

> what dynamical behavior becomes visible only when the optimizer and model are analyzed as one coupled system?

The useful allegory is a **vehicle with a flywheel**.

Position corresponds to model parameters. The flywheel corresponds to stored optimizer state. A steering command changes position, but the stored motion changes how the same command behaves one step later.

The limit of the allegory is strict. Optimizer state is not physical momentum, adaptive methods have coordinatewise and state-dependent statistics, and no conservation law is implied.

The point is only that memory in the update rule changes the state space.

## 2. Heavy-ball momentum as a state-space map

Polyak’s multistep acceleration is a canonical source for momentum-like iteration [@Polyak1964], and momentum later became central to deep-network optimization [@SutskeverEtAl2013].

Consider the scalar quadratic

\[
L(\theta)
=
\frac h2\theta^2,
\qquad
h>0.
\]

Then

\[
g(\theta)=h\theta.
\]

Use the recurrence

\[
v_{t+1}
=
\beta v_t+h\theta_t,
\]

followed by

\[
\theta_{t+1}
=
\theta_t-\eta v_{t+1}.
\]

Substitution gives

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
z_{t+1}
=
Jz_t,
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

Nothing has been approximated. The optimizer-model pair is literally a two-dimensional linear dynamical system for this quadratic example.

## 3. The characteristic equation belongs to the coupled system

The trace is

\[
\operatorname{tr}J
=
1-\eta h+\beta,
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

The stability boundary depends jointly on

\[
\eta,\qquad
\beta,\qquad
h.
\]

This already changes the conceptual story.

Curvature \(h\) matters, but curvature alone does not determine the update. Learning rate matters, but learning rate alone is not the dynamical system. Momentum matters, but it is not a scalar correction applied outside the dynamics.

The boundary is a property of the coupled recurrence.

## 4. A stable example with transient amplification

Choose

\[
h=1,\qquad
\eta=\frac1{10},\qquad
\beta=\frac9{10}.
\]

Then

\[
J=
\begin{pmatrix}
0.9&-0.09\\
1&0.9
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_\pm
=
0.9\pm0.3i.
\]

Thus

\[
|\lambda_\pm|
=
\sqrt{0.9}
\approx0.9486832981<1.
\]

The fixed point is asymptotically stable.

If eigenvalues were the whole story, one might expect every perturbation simply to decay.

They are not the whole story.

The matrix is non-normal.

Indeed,

\[
J^\top J
=
\begin{pmatrix}
1.81&0.819\\
0.819&0.8181
\end{pmatrix},
\]

while

\[
JJ^\top
=
\begin{pmatrix}
0.8181&0.819\\
0.819&1.81
\end{pmatrix}.
\]

Therefore

\[
J^\top J\neq JJ^\top.
\]

The preceding Non-normality chapter prepared exactly this situation: asymptotic spectral stability can coexist with finite-horizon amplification.

## 5. Four stable steps can amplify by more than \(2.6\times\)

For the same matrix,

\[
J^4
=
\begin{pmatrix}
\frac{567}{2500}&-\frac{729}{3125}\\
\frac{324}{125}&\frac{567}{2500}
\end{pmatrix}.
\]

The largest singular value is

\[
\|J^4\|_2
\approx
2.610090585959495.
\]

So there exists a unit perturbation \(\delta z_0\) such that

\[
\|J^4\delta z_0\|_2
\approx
2.61.
\]

The same system eventually decays because its eigenvalues are inside the unit disk.

This is the mechanism to remember:

\[
\boxed{
\text{asymptotically stable}
\not\Rightarrow
\text{monotone finite-horizon decay}.
}
\]

The claim is exact for this linear example.

It is not yet a claim about a neural training run.

## 6. The Wolfram plate

The primary figure puts three views of the same toy system beside one another.

![Phase trajectories, eigenvalues relative to the unit circle, and finite-horizon spectral norm gain for the exact momentum-state matrix.](../../figures/masters/ATLAS-FIG-OPTDYN-001.png)

The left panel shows trajectories in the augmented \((\theta,v)\) state plane.

The middle panel shows both eigenvalues strictly inside the unit circle.

The right panel shows

\[
\|J^n\|_2
\]

for \(n=0,\ldots,20\), with a peak of approximately

\[
2.61009
\]

at

\[
n=4.
\]

The three panels are not three different stories. They are three descriptions of one matrix.

The figure is therefore a compact warning against using one spectral summary as if it exhausted the dynamics.

## 7. Why the augmented state matters

If one looks only at \(\theta_t\), the optimizer’s memory appears indirectly.

In augmented state, it is explicit.

This matters because the local Jacobian of the full update contains couplings between parameter and optimizer coordinates.

For a general optimizer state \(s_t\),

\[
z_t=
\begin{pmatrix}
\theta_t\\
s_t
\end{pmatrix},
\]

and a local Jacobian has block structure

\[
J_t
=
\begin{pmatrix}
\partial_\theta F_\theta&
\partial_s F_\theta\\
\partial_\theta F_s&
\partial_s F_s
\end{pmatrix}.
\]

The off-diagonal blocks are not decoration. They encode how optimizer memory changes parameter motion and how parameter-space gradients update optimizer memory.

A parameter-only Hessian does not contain all of this information.

## 8. Curvature is not the same as optimizer dynamics

On the quadratic example, curvature appears through \(h\).

But the state Jacobian is

\[
J(\eta,\beta,h)
=
\begin{pmatrix}
1-\eta h&-\eta\beta\\
h&\beta
\end{pmatrix}.
\]

The same \(h\) with different \(\eta\) or \(\beta\) produces a different dynamical system.

Likewise, a large Hessian eigenvalue can matter without being a complete explanation of instability.

The disciplined statement is:

> the loss landscape contributes to the update dynamics, but the update dynamics belong to the combined model-optimizer recurrence.

This is the level at which learning-rate boundaries should be analyzed.

## 9. From an autonomous toy system to time-varying training

The quadratic example has one fixed matrix \(J\).

Training in a neural network is generally nonautonomous.

Write

\[
z_{t+1}
=
F_t(z_t,\xi_t).
\]

Linearizing along a trajectory gives

\[
\delta z_{t+1}
\approx
J_t\delta z_t,
\qquad
J_t
=
\frac{\partial F_t}{\partial z}(z_t,\xi_t).
\]

After \(k\) steps,

\[
\delta z_{t+k}
\approx
J_{t+k-1}\cdots J_t\,\delta z_t.
\]

A single-step eigenvalue calculation cannot in general summarize this product.

The relevant object is the finite-horizon propagator.

This is one reason non-normal and transient-growth thinking is useful: it asks what perturbations can do over a finite horizon, not only what one frozen matrix does asymptotically.

## 10. Adam makes the state richer

Adam maintains first- and second-moment estimates [@KingmaBa2015].

Schematically,

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

followed by a parameter update using bias-corrected moment estimates.

The exact augmented state is therefore larger:

\[
z_t=(\theta_t,m_t,v_t,\ldots).
\]

The present chapter does not derive a universal Adam stability theory. That would obscure the mechanism we are trying to expose.

Momentum is used as the exact microscope because its state is small enough that every coupling can be seen.

Adam is included to show that the augmented-state viewpoint becomes more, not less, relevant as optimizers accumulate richer memory.

## 11. Optimization as a dynamical and control system

There is established precedent for analyzing iterative optimization as a feedback/dynamical system. Lessard, Recht, and Packard use integral quadratic constraints from robust control to analyze methods including gradient descent, heavy-ball momentum, and accelerated schemes [@LessardRechtPackard2016].

The Atlas does not reproduce that full framework here.

The connection is conceptual and mathematical:

- an optimizer is an iterative dynamical system;
- the objective/gradient map enters the loop;
- stability and gain are properties of the interconnection;
- finite-horizon behavior can matter even when asymptotic convergence conditions hold.

The Atlas adds a particular emphasis: in learned systems, optimizer state should be treated as part of the object being diagnosed.

## 12. What a local Jacobian can and cannot tell us

A local augmented-state Jacobian can reveal:

- instantaneous coupling;
- singular amplification directions;
- local spectral structure;
- departure from normality;
- sensitivity to hyperparameters;
- finite-horizon products along a recorded trajectory.

It cannot, by itself, establish:

- the global nonlinear behavior of training;
- the cause of an observed loss spike;
- that one local mode persists over many steps;
- that a toy quadratic captures a frontier model;
- that non-normality is the dominant mechanism in every unstable run.

The distinction between mechanism and prevalence is essential.

A toy example can prove that a mechanism exists.

It cannot prove how often that mechanism matters in practice.

## 13. The flywheel allegory, and where it fails

The flywheel picture is useful because it blocks one mistake: pretending that only current position matters.

The correspondence is:

- position ↔ model parameters;
- stored rotational state ↔ optimizer memory;
- control gain ↔ learning rate;
- coupled overshoot ↔ transient amplification.

But the optimizer is not a physical rigid body.

Adam’s state has no literal angular momentum. Stochastic gradients are not deterministic forces. Coordinatewise normalization has no simple mechanical analogue.

The allegory has done its job once the reader accepts that optimizer memory enlarges the state space.

The mathematics should then take over.

## 14. A handoff to Coupling-Phase Spectroscopy

Suppose a training phase transition is genuinely a property of the augmented state.

Then a parameter-only diagnostic may miss part of the mechanism.

This motivates a later instrumentation question:

> can we probe the Jacobian of the coupled model-optimizer state strongly enough to detect changes in dynamical regime?

The Atlas names the downstream GCL programme **Coupling-Phase Spectroscopy (CPS)**.

At present, this chapter makes no project-specific empirical claim because no exact public source lock for CPS results is bound here. The source-lock manifest records that boundary explicitly.

The chapter therefore contributes the mathematical object and the diagnostic question, not an unverified result.

## 15. Five mistakes to avoid

### Mistake 1: “The Hessian is the optimizer dynamics.”

No. Curvature enters the recurrence, but optimizer memory changes the state and the update Jacobian.

### Mistake 2: “Eigenvalues inside the unit disk mean every perturbation shrinks every step.”

No. The worked non-normal example has spectral radius below one and peak finite-horizon gain above \(2.6\).

### Mistake 3: “A transient spike proves divergence.”

No. Transient amplification and asymptotic divergence are different.

### Mistake 4: “A local linearization predicts the whole training run.”

No. It is local, and realistic training is time-varying and nonlinear.

### Mistake 5: “Optimizer state is implementation detail.”

No. If the next update depends on it, it is part of the dynamical state.

## 16. Atlas connections

**Non-normality.**  
This chapter turns transient-growth mathematics into an optimizer-state mechanism.

**Coupling-Phase Spectroscopy.**  
The augmented-state Jacobian becomes a candidate probe for phase changes.

**Router dynamics.**  
Routing systems with memory can be analyzed through similar coupled-state ideas.

**Spectral diagnostics.**  
Eigenvalues, singular values, pseudospectra, and finite-horizon gains become complementary diagnostic objects.

**Variational optimization.**  
Later chapters will ask whether better update rules can be derived from geometry and discrete variational structure rather than tuned only through heuristics.

The recurring Atlas shift is:

\[
\boxed{
\text{optimizer as update rule}
\longrightarrow
\text{optimizer-model pair as dynamical system}.
}
\]

## 17. Closing view

A modern optimizer remembers.

Once it remembers, its memory becomes part of the state.

Once the optimizer state is part of the state, the natural object is no longer only a loss surface or a gradient. It is a coupled recurrence with its own Jacobian, stability region, transient behavior, and finite-horizon propagator.

The simple quadratic example is small enough to solve exactly and rich enough to expose the point.

Stable eigenvalues do not forbid transient amplification.

The flywheel is only an allegory.

The augmented state is the object.

## References used in this chapter

- [@Polyak1964]
- [@SutskeverEtAl2013]
- [@KingmaBa2015]
- [@LessardRechtPackard2016]

See \`sources/source-locks/ATLAS-CH-OPTDYN-001.yaml\` for exact source identities and claim scope.
