# Flows, Stability, and Bifurcation
<!-- ATLAS-CH-DYN-001 -->

**Epistemic status:** Established Theory + Atlas Derivation + Atlas Interpretation  
**Specification:** manuscript/specifications/ATLAS-CH-DYN-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-DYN-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-DYN-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-DYN-001.yaml

## 1. From function evaluation to evolution

A function tells us what output corresponds to an input.

A dynamical system asks a different question:

> If the system is in this state now, how does the state change?

That distinction becomes important as soon as computation has internal time.

A residual network has depth.

An optimizer has momentum and accumulated statistics.

A recurrent model carries state forward.

An agent acts, observes, updates memory, and acts again.

A training process couples parameters, optimizer state, data order, and scheduling.

These systems cannot always be understood by inspecting one isolated map.

We need a language for evolution.

That language begins with:

- vector fields;
- trajectories;
- flows;
- fixed points;
- stability;
- bifurcation.

It later extends into numerical integration, optimization dynamics, adaptive depth, and transport.

## 2. Wind field and carried particle

A useful allegory is a wind field.

At every location, imagine an arrow telling a particle which way to move.

The correspondence is:

- state \(x\):
  particle location;
- vector field \(f(x)\):
  local wind;
- trajectory:
  one particle's path;
- flow:
  the transformation carrying every admissible starting point through time;
- equilibrium:
  a location with zero wind;
- bifurcation:
  a qualitative reorganization of the flow as a control parameter changes.

The analogy has a limit.

Neural and optimization dynamics may be:

- discrete;
- stochastic;
- nonautonomous;
- state-dependent in higher-order ways;
- driven by external inputs.

The point is not that computation is literally fluid motion.

The point is to separate:

\[
\boxed{
\text{local evolution law}
\neq
\text{one realized trajectory}
\neq
\text{global flow}.
}
\]

## 3. Continuous autonomous dynamics

A finite-dimensional autonomous system has form

\[
\dot x=f(x),
\qquad
x\in\mathbb R^d.
\]

The vector field

\[
f:\mathbb R^d\to\mathbb R^d
\]

assigns an instantaneous velocity to every state.

Given an initial condition

\[
x(0)=x_0,
\]

a solution trajectory satisfies

\[
\frac{d}{dt}x(t)=f(x(t)).
\]

When existence and uniqueness hold, we can define

\[
\Phi_t(x_0)=x(t).
\]

The family

\[
\Phi_t
\]

is the flow.

For an autonomous flow where both sides are defined,

\[
\Phi_0=\operatorname{id},
\]

and

\[
\boxed{
\Phi_{t+s}
=
\Phi_t\circ\Phi_s.
}
\]

This composition law says that evolving for \(s\) and then \(t\) is the same as evolving for \(t+s\).

## 4. A trajectory is not the flow

One trajectory may look calm.

Another may diverge.

A single observed path does not tell us the behavior of every nearby initial state.

This matters in machine learning.

One successful training run does not by itself characterize the training dynamics.

One stable rollout does not prove robust state evolution.

One sequence of residual updates does not identify the global flow-like structure of the architecture.

Dynamics is partly the study of how neighboring trajectories relate.

## 5. Discrete dynamics

Many computational systems evolve in steps rather than continuous time.

A discrete map has form

\[
x_{k+1}=F(x_k).
\]

The \(k\)-step evolution is

\[
x_k=F^{\circ k}(x_0).
\]

This is already enough to describe:

- iterative optimization;
- recurrent state updates;
- repeated residual blocks;
- fixed-point solvers;
- many agent loops.

Continuous and discrete systems share concepts.

Their stability tests are not identical.

That difference will matter repeatedly.

## 6. Equilibria and fixed points

For the continuous system

\[
\dot x=f(x),
\]

an equilibrium satisfies

\[
\boxed{
f(x_\star)=0.
}
\]

If the system reaches \(x_\star\), it remains there.

For the discrete system

\[
x_{k+1}=F(x_k),
\]

a fixed point satisfies

\[
\boxed{
F(x_\star)=x_\star.
}
\]

An equilibrium is therefore not merely a low-loss point or a visually flat region.

It is defined relative to an evolution law.

Change the law and the fixed points can change.

## 7. Local linearization

Suppose \(f\) is differentiable and

\[
x=x_\star+\delta.
\]

A Taylor expansion gives

\[
f(x_\star+\delta)
=
f(x_\star)
+
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

At an equilibrium,

\[
f(x_\star)=0,
\]

so

\[
\dot\delta
=
J_f(x_\star)\delta
+
O(\|\delta\|^2).
\]

The first-order approximation is

\[
\boxed{
\dot\delta=A\delta,
\qquad
A=J_f(x_\star).
}
\]

Linear algebra now becomes local dynamics.

The Jacobian tells us how infinitesimal perturbations evolve near the equilibrium.

## 8. Continuous-time local stability

For

\[
\dot\delta=A\delta,
\]

the exact linear solution is

\[
\delta(t)=e^{tA}\delta(0).
\]

If every eigenvalue of \(A\) has negative real part, the linearized system decays exponentially.

Under the standard smoothness assumptions, this gives local asymptotic stability of the nonlinear equilibrium.

If at least one eigenvalue has positive real part, the equilibrium is unstable.

The important boundary is the imaginary axis.

If an eigenvalue has zero real part, the first-order test may be inconclusive.

That is not a technical footnote.

It is where nonlinear terms can decide the behavior.

## 9. Two systems, same zero linearization

Consider

\[
\dot x=-x^3.
\]

At the origin,

\[
f'(0)=0.
\]

Now consider

\[
\dot x=x^3.
\]

Again,

\[
f'(0)=0.
\]

The linearization is identical:

\[
\dot\delta=0.
\]

The nonlinear behavior is not.

For

\[
\dot x=-x^3,
\]

positive states decrease and negative states increase toward zero.

For

\[
\dot x=x^3,
\]

positive states increase and negative states decrease away from zero.

Thus:

\[
\boxed{
\text{zero linearization}
\not\Rightarrow
\text{neutral nonlinear stability}.
}
\]

Linearization is powerful precisely where its assumptions make it decisive.

## 10. Discrete-time local stability

For

\[
x_{k+1}=F(x_k),
\]

linearization near a fixed point gives

\[
\delta_{k+1}
=
J_F(x_\star)\delta_k.
\]

The relevant boundary is now the unit circle.

If every eigenvalue satisfies

\[
|\lambda_i|<1,
\]

the linearized perturbations decay.

If at least one eigenvalue satisfies

\[
|\lambda_i|>1,
\]

the fixed point is unstable.

Eigenvalues with

\[
|\lambda_i|=1
\]

can make the linear test inconclusive.

The distinction is fundamental:

\[
\boxed{
\text{continuous stability: real parts}
}
\]

versus

\[
\boxed{
\text{discrete stability: moduli}.
}
\]

Later numerical-analysis chapters will exploit exactly this difference.

## 11. Lyapunov's different question

Linearization asks what infinitesimal perturbations do near a point.

Lyapunov analysis asks whether we can find a scalar function that must move in one direction along trajectories.

Let

\[
V(x)\ge0
\]

measure something like generalized energy or distance from an equilibrium.

Along a trajectory,

\[
\dot V(x)
=
\nabla V(x)^\top f(x).
\]

If \(V\) is positive definite and \(\dot V\) is negative definite in a neighborhood, the equilibrium is locally asymptotically stable under the usual regularity assumptions [@Khalil2002].

The key idea is not that \(V\) must be physical energy.

It is that \(V\) gives a monotone certificate.

## 12. Exact Lyapunov witness

Return to

\[
\dot x=-x^3.
\]

Choose

\[
V(x)=\frac12x^2.
\]

Then

\[
V(x)>0
\]

for \(x\neq0\), and

\[
V(0)=0.
\]

Along trajectories,

\[
\dot V
=
x(-x^3)
=
-x^4.
\]

Therefore

\[
\boxed{
\dot V=-x^4<0
}
\]

for every nonzero \(x\).

The origin is asymptotically stable.

Because this scalar \(V\) is radially unbounded and the derivative remains negative away from zero, the calibration system is globally asymptotically stable.

The exact result is simple.

The methodological lesson is broader:

> when linearization is inconclusive, a nonlinear certificate may still decide stability.

## 13. Local and global are different claims

A locally stable equilibrium controls nearby trajectories.

It does not automatically control:

- distant initial states;
- other basins of attraction;
- other equilibria;
- finite-time excursions;
- behavior under forcing;
- behavior after discretization.

A statement such as

> the fixed point is stable

is incomplete unless the scope is clear.

The Atlas will distinguish:

- local stability;
- global stability;
- finite-time amplification;
- numerical stability;
- robustness to perturbation.

These are related.

They are not synonyms.

## 14. Phase portraits

A phase portrait visualizes how trajectories organize state space.

In one or two dimensions it can reveal:

- equilibria;
- attracting directions;
- repelling directions;
- invariant curves;
- cycles;
- separatrices.

The picture is not a substitute for analysis.

It is a compact map of the evolution geometry.

This is one place where the Atlas metaphor and dynamical-systems practice naturally align.

## 15. Parameterized dynamics

Many systems depend on a parameter

\[
\mu.
\]

Write

\[
\dot x=f(x;\mu).
\]

As \(\mu\) varies, the system can change quantitatively.

More interestingly, it can change qualitatively.

The number of equilibria can change.

Their stability can change.

Cycles can appear or disappear.

The geometry of trajectories can reorganize.

A qualitative change of this kind is a bifurcation [@Strogatz2015].

## 16. Supercritical pitchfork

Consider

\[
\boxed{
\dot x
=
\mu x-x^3.
}
\]

Equilibria satisfy

\[
x(\mu-x^2)=0.
\]

Therefore the origin

\[
x_\star=0
\]

exists for every \(\mu\).

For

\[
\mu>0,
\]

two additional equilibria appear:

\[
x_\star=\pm\sqrt\mu.
\]

The scalar Jacobian is

\[
\frac{\partial f}{\partial x}
=
\mu-3x^2.
\]

At the origin,

\[
\lambda_0=\mu.
\]

Thus:

- \(\mu<0\):
  origin locally asymptotically stable;
- \(\mu>0\):
  origin unstable;
- \(\mu=0\):
  linearization inconclusive.

At the two outer branches,

\[
\lambda_\pm=-2\mu.
\]

For

\[
\mu>0,
\]

both are stable.

## 17. What changes at the bifurcation

At

\[
\mu=0,
\]

the origin becomes nonhyperbolic.

For negative \(\mu\), there is one stable equilibrium.

For positive \(\mu\), there are three equilibria:

- one unstable origin;
- two stable outer states.

The system has changed its qualitative organization.

This is why a bifurcation diagram encodes more than a curve.

It encodes:

- existence;
- multiplicity;
- stability;
- parameter regime.

![A computed two-panel plate showing the supercritical pitchfork equilibrium branches with stable and unstable portions distinguished, beside the harmonic oscillator phase field and a circular constant-energy trajectory.](../../figures/masters/ATLAS-FIG-DYN-001.png)

## 18. The bifurcation point also revisits linearization

At

\[
\mu=0,
\]

the pitchfork system becomes

\[
\dot x=-x^3.
\]

Its linearization at zero is again

\[
0.
\]

Yet the origin is asymptotically stable.

The pitchfork therefore ties two ideas together:

- bifurcations often occur where hyperbolic linear classification fails;
- nonlinear terms become decisive exactly where the first-order margin vanishes.

That does not mean every nonhyperbolic point is a bifurcation.

It means nonhyperbolicity is a place where qualitative change can become possible.

## 19. Stability is not the same as absence of transient growth

Suppose every eigenvalue of a linear system has negative real part.

Does every perturbation shrink monotonically?

No.

For non-normal operators, finite-time amplification can occur even when the system is asymptotically stable.

The existing Non-normality keystone develops this distinction.

The dynamical lesson is:

\[
\boxed{
\text{asymptotic stability}
\neq
\text{monotone finite-time contraction}.
}
\]

This matters for optimization, recurrent computation, and deep compositions where transient amplification can dominate finite-horizon behavior.

## 20. Nonautonomous and forced systems

The autonomous form

\[
\dot x=f(x)
\]

is foundational.

It is not universal.

A forced or nonautonomous system has form

\[
\dot x=f(x,t)
\]

or

\[
\dot x=f(x,u(t)).
\]

Training dynamics can depend explicitly on:

- learning-rate schedules;
- data ordering;
- time-varying regularization;
- curriculum;
- external feedback.

Agent dynamics depend on changing observations and environments.

The autonomous theory provides a base language.

Later applications must state when the stronger autonomous assumptions do not hold.

## 21. Stochastic dynamics

Noise introduces another boundary.

A stochastic update such as

\[
x_{k+1}
=
F(x_k,\xi_k)
\]

is not fully characterized by one deterministic map.

Stochastic gradients are the obvious example.

Then stability can mean:

- almost-sure stability;
- stability in probability;
- bounded moments;
- stationary distributions;
- expected contraction.

This chapter does not develop stochastic stability theory.

It establishes the deterministic substrate that later chapters may extend.

## 22. Hamiltonian dynamics

A different class of dynamical systems is organized not around dissipation but around conserved structure.

Let

\[
z=
\begin{pmatrix}
q\\
p
\end{pmatrix},
\]

and let

\[
H(q,p)
\]

be a Hamiltonian.

Define the canonical matrix

\[
J=
\begin{pmatrix}
0&I\\
-I&0
\end{pmatrix}.
\]

Hamilton's equations can be written

\[
\boxed{
\dot z
=
J\nabla H(z).
}
\]

This compact form exposes the geometry directly.

## 23. Conservation of the Hamiltonian

Because

\[
J^\top=-J,
\]

we have

\[
v^\top Jv=0
\]

for every vector \(v\).

Therefore

\[
\begin{aligned}
\frac{dH}{dt}
&=
\nabla H^\top\dot z\\
&=
\nabla H^\top J\nabla H\\
&=
0.
\end{aligned}
\]

Hence

\[
\boxed{
H(z(t))=H(z(0))
}
\]

along the exact autonomous Hamiltonian flow.

This is a structural conservation law.

It does not say every conserved system is Hamiltonian.

It does not say every machine-learning dynamic should conserve an energy.

## 24. Symplectic structure

Hamiltonian flows preserve more than scalar energy.

Their tangent maps preserve the canonical symplectic form.

For the exact flow \(\Phi_t\),

\[
\boxed{
D\Phi_t(z)^\top
J
D\Phi_t(z)
=
J.
}
\]

This relation constrains how infinitesimal phase-space directions transform.

It is one of the central reasons geometric numerical integration treats Hamiltonian systems differently from generic ODEs [@HairerLubichWanner2006].

## 25. Symplectic is stronger than volume-preserving

Take determinants of

\[
M^\top J M=J.
\]

We obtain

\[
\det(M)^2=1.
\]

For a continuous exact flow connected to the identity,

\[
\det(M)=1.
\]

So symplectic maps preserve phase-space volume.

But determinant one is not generally enough to imply symplecticity in dimensions above two.

The distinction is important:

\[
\boxed{
\text{symplectic}
\Rightarrow
\text{volume-preserving},
}
\]

but not generally the converse.

A single scalar determinant cannot encode the full preserved two-form.

## 26. Harmonic oscillator

Take

\[
H(q,p)
=
\frac12(q^2+p^2).
\]

Then

\[
\dot q=p,
\qquad
\dot p=-q.
\]

Write

\[
z=
\begin{pmatrix}
q\\
p
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

The system is

\[
\dot z=Az.
\]

Because

\[
A^2=-I,
\]

the matrix exponential is

\[
\boxed{
e^{tA}
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
}
\]

The flow is a rotation.

## 27. Exact oscillator witness

Let

\[
M(t)=e^{tA}.
\]

The computational witness verifies

\[
M(t)^\top J M(t)=J.
\]

It also verifies

\[
\det M(t)=1.
\]

For arbitrary initial state

\[
(q,p),
\]

the exact flow preserves

\[
q^2+p^2.
\]

Therefore

\[
H(q_t,p_t)=H(q,p).
\]

The circular trajectories in the figure are not artistic decoration.

They are level sets of the conserved Hamiltonian.

## 28. Dissipative and conservative pictures

The scalar system

\[
\dot x=-x^3
\]

is dissipative toward an attractor.

The harmonic oscillator is conservative.

These are qualitatively different dynamical organizations.

The first loses a Lyapunov quantity.

The second preserves a Hamiltonian and symplectic structure.

Machine-learning dynamics can exhibit:

- contraction;
- expansion;
- conservation;
- forcing;
- stochasticity;
- switching;
- mixed regimes.

The Atlas therefore needs a vocabulary richer than “stable” versus “unstable.”

## 29. Continuous flow versus numerical method

Suppose the exact continuous system is stable.

A numerical discretization can still be unstable.

Suppose the exact Hamiltonian flow is symplectic.

A generic numerical method need not preserve that structure.

This is a critical handoff.

The present chapter establishes the continuous dynamics.

The Numerical Intelligence chapter will ask:

> What properties survive when evolution is approximated computationally?

The answer depends on the method and the step size.

## 30. Depth as computational time

A deep network supplies a sequence

\[
x_0,x_1,\ldots,x_L.
\]

One useful interpretation is to compare this sequence with a time discretization.

For a residual update

\[
x_{k+1}
=
x_k+h f_k(x_k),
\]

the layer index behaves like a discrete computational time.

This interpretation can expose questions about:

- stability;
- step size;
- stiffness;
- reversibility;
- adaptive depth;
- splitting.

It does not mean every residual network is literally sampled from one autonomous ODE.

The analogy must be earned architecture by architecture.

## 31. Training as a coupled dynamical system

Training also evolves state.

Let

\[
\theta_k
\]

be model parameters and

\[
s_k
\]

optimizer state.

A general update can be written

\[
(\theta_{k+1},s_{k+1})
=
F(\theta_k,s_k,\xi_k),
\]

where \(\xi_k\) can encode stochastic gradient information or data dependence.

The important shift is conceptual:

\[
\boxed{
\text{optimizer}
\neq
\text{stateless rule on parameters}.
}
\]

The optimizer-dynamics keystone develops this in detail.

The present chapter supplies the vocabulary it relies on.

## 32. Fixed points of learning

A stationary point of the loss is not automatically a fixed point of every optimizer.

Momentum can continue moving.

Weight decay can move parameters.

Adaptive state can evolve.

Constraints can project or retract.

To ask whether training has reached a fixed point, we must specify the full state and the full update map.

This is another example of the Objects chapter's discipline:

> define the state before defining its dynamics.

## 33. Bifurcation as a lens on adaptive systems

Why should machine-learning researchers care about bifurcation?

Not because every transition is a pitchfork.

The useful lesson is more general.

A small parameter change can produce a qualitative reorganization of:

- fixed points;
- attractors;
- oscillations;
- routing regimes;
- update behavior.

Examples of parameters might include:

- learning rate;
- regularization strength;
- coupling coefficient;
- temperature;
- capacity constraint.

Calling a transition a bifurcation requires a dynamical argument.

The Atlas will not use the word merely as a metaphor for “something changed.”

## 34. Lyapunov functions as certificates

The Atlas repeatedly returns to certificates.

A Lyapunov function is an early mathematical example.

It does not simulate every trajectory.

It provides a structured inequality sufficient to certify a stability property.

That pattern reappears later in:

- numerical stability;
- optimization;
- boundary contracts;
- uncertainty bounds;
- replayable evidence.

The lesson is methodological:

> a good certificate can compress a large family of possible trajectories into one verifiable condition.

## 35. Five distinctions to preserve

### Vector field versus trajectory

The law of motion is not one realization.

### Local versus global stability

Nearby behavior does not determine the entire state space.

### Continuous versus discrete stability

Left-half-plane eigenvalues and unit-disk eigenvalues answer different problems.

### Asymptotic stability versus transient amplification

Eventually decaying dynamics can still exhibit large finite-time growth.

### Exact flow versus numerical approximation

A discretization can destroy properties of the continuous system.

These distinctions are foundational for the rest of the Atlas.

## 36. Failure modes

### Linearization overreach

A zero or imaginary-axis eigenvalue is treated as decisive.

### One trajectory mistaken for stability

A successful run is generalized to neighboring states.

### Local result promoted globally

A neighborhood theorem is used as a whole-space guarantee.

### Bifurcation used metaphorically

A parameter-dependent performance change is called a bifurcation without identifying a qualitative change in the dynamical invariant structure.

### Symplecticity inferred from determinant one

Volume preservation is mistaken for preservation of the symplectic form.

### Continuous stability transferred to arbitrary discretization

The numerical method is assumed to inherit exact-flow behavior without analysis.

## 37. Atlas connections

**Linear algebra.**  
Jacobians convert local nonlinear dynamics into linear operators.

**Non-normality.**  
Eigenvalue stability can coexist with finite-time transient growth.

**Numerical intelligence.**  
Discretization asks which continuous-time properties survive computation.

**Architecture as dynamics.**  
Depth can be studied as repeated evolution.

**Optimization.**  
Parameters and optimizer state form a coupled dynamical system.

**Adaptive depth.**  
Computational time can become a controlled resource rather than a fixed layer count.

**Split operators.**  
Complex evolution laws can be composed from simpler flows.

**Reversible computation.**  
Invertible dynamics constrain information loss.

**Transport.**  
Representation updates can be interpreted as motion through structured state spaces.

## 38. What changed in our picture?

Before this chapter, the Atlas had:

- states;
- operators;
- geometry;
- representations.

Dynamics adds something different:

\[
\boxed{
\text{history}.
}
\]

A state is no longer only a point.

It is a point embedded in an evolution law.

An operator is no longer only a transformation.

Repeated or continuous application creates trajectories, fixed points, attractors, conserved structures, and regime changes.

This changes the questions we can ask.

Instead of only:

> What function does the system represent?

we can also ask:

> Where does it go?

> What perturbations grow?

> What does it preserve?

> When does its qualitative behavior change?

> Which properties survive discretization?

Those questions will organize much of the Atlas that follows.

## References used in this chapter

- [@Strogatz2015]
- [@Khalil2002]
- [@HairerLubichWanner2006]

See \`sources/source-locks/ATLAS-CH-DYN-001.yaml\` for exact source roles and claim scope.
