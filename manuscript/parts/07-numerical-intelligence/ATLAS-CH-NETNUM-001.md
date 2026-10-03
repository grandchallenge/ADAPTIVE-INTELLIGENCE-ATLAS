# Networks as Numerical Schemes
<!-- ATLAS-CH-NETNUM-001 -->

**Epistemic status:** established numerical analysis + primary residual/continuous-depth architecture sources + Atlas synthesis + exact scalar witness.  
**Specification:** manuscript/specifications/ATLAS-CH-NETNUM-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-NETNUM-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-NETNUM-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-NETNUM-001.yaml

A residual block looks like Euler's method.

That resemblance is useful.

It is also one of the easiest analogies in modern deep learning to overstate.

Write a residual layer as

`x_{k+1}=x_k+F_k(x_k)`.

Write one explicit-Euler step for

`dx/dt=f(t,x)`

as

`x_{k+1}=x_k+h_k f(t_k,x_k)`.

The shapes match.

But numerical analysis does not begin with a shape match.

It begins with a reference problem.

To speak meaningfully about consistency, local truncation error, global error, stability, step size, stiffness, or reversibility, we must know what continuous evolution the discrete map is supposed to approximate, how one layer corresponds to one step, what changes when the mesh is refined, and which norm or state metric is being used.

The governing rule of this chapter is therefore:

> residual form opens the numerical lens; it does not, by itself, complete the numerical interpretation.

That distinction lets us use numerical analysis rigorously rather than decoratively.

## 1. From architecture to update map

The Architecture History chapter established the residual form

`x_{k+1}=x_k+F_k(x_k)`

as a structural shift.

The identity path transports the current state forward.

The residual branch computes a change.

This makes depth look less like repeated replacement and more like repeated state update.

The Numerical Methods chapter supplied the corresponding mathematical object:

`x_{n+1}=Psi_h(t_n,x_n)`.

A one-step method takes the current numerical state and advances it by a discrete rule.

These objects align naturally.

The question is not whether they look similar.

The question is what additional assumptions make the alignment mathematically substantive.

## 2. The bridge must be declared

Suppose the intended continuous system is

`dx/dt=f(t,x)`.

Explicit Euler gives

`x_{k+1}=x_k+h_k f(t_k,x_k)`.

A residual layer becomes Euler-compatible after the declaration

`F_k(x)=h_k f(t_k,x)`.

This line performs the bridge.

It says:

- which continuous field is being sampled;
- which layer corresponds to which time;
- which scale is the step size.

Without that bridge, `F_k` is simply a learned residual map.

There is nothing wrong with that.

But numerical-analysis terminology must remain attached to the object it actually describes.

## 3. Residual architecture is not a unique ODE

Could any residual stack be rewritten as some continuous system?

In a loose interpolation sense, often yes.

But that is not the same as saying the network has a unique or canonical underlying ODE.

A finite sequence of maps

`Psi_0,Psi_1,...,Psi_{N-1}`

can be embedded or interpolated in many ways.

Different continuous fields may agree on the sampled layer states.

Different time parameterizations may produce the same discrete sequence.

Different modified equations may explain the same discrete update to a given asymptotic order.

Therefore the ODE is not generally recovered uniquely from residual syntax.

The Architecture History audit already fixed the safe statement:

> residual systems admit an integrator lens.

This chapter sharpens the conditions under which that lens supports numerical claims.

## 4. Autonomous versus nonautonomous depth

Weight sharing is sometimes treated as the dividing line between dynamical and nondynamical networks.

That is too crude.

If

`F_k(x)=h f(x)`

for a common `f`, then the blocks have the direct form of fixed-step Euler applied to an autonomous ODE.

But a continuous system can be explicitly time-dependent:

`dx/dt=f(t,x)`.

Then layer-varying residuals can correspond to

`F_k(x)=h_k f(t_k,x)`.

So untied weights do not rule out an ODE interpretation.

They may correspond to a nonautonomous field.

The real issue is whether there is a declared continuous object and a meaningful sampling/refinement relation.

## 5. A layer is not yet a time step

Suppose we introduce a residual scale:

`x_{k+1}=x_k+alpha_k G_k(x_k)`.

It is tempting to call `alpha_k` the step size.

Sometimes that is exactly right.

If `G_k` samples a declared vector field, then `alpha_k` can play the role of `h_k`.

But if changing `alpha_k` is accompanied by retraining `G_k), changing normalization, changing feature geometry, or otherwise changing the update field, then the comparison is not simply "same ODE, smaller step."

A step size has meaning only relative to an underlying evolution.

A residual scale always changes the network map.

It does not automatically refine a fixed continuous problem.

## 6. Local truncation error requires an exact flow

The Numerics chapter defined the exact flow over one step as

`Phi_h`

and the numerical map as

`Psi_h`.

The local defect is computed by starting the numerical step from the exact state:

`delta_{k+1}
=
Phi_{h_k}(t_k,x(t_k))
-
Psi_k(x(t_k))`.

For explicit Euler, under the usual smoothness assumptions,

`delta_{k+1}=O(h_k^2)`.

That statement contains more structure than it first appears.

It assumes:

- a continuous trajectory exists;
- an exact flow is defined;
- the layer is tied to a numerical step;
- `h_k` is a meaningful small parameter.

If a residual block is merely a learned map with no declared continuous reference, then saying it has "small local truncation error" is not merely unproven.

The quantity has not been defined.

## 7. Small residual does not mean small truncation error

Suppose

`||F_k(x)||`

is small.

Does that imply the corresponding Euler defect is small?

No.

A small update norm can arise because:

- the vector field itself is small;
- the step is small;
- the representation is scaled;
- normalization suppresses magnitude;
- the network has learned a near-identity map;
- the local coordinates make the update appear small.

Local truncation error compares a numerical step to the exact flow of a specified continuous problem.

The norm of the residual branch alone does not perform that comparison.

This is a recurring category error:

> small update is not the same statement as accurate discretization.

## 8. Global error is not layerwise error added up

Define the global numerical error as

`e_k=x(t_k)-x_k`.

This error is not simply the sum of local defects.

Each old error is transported through later steps.

For a stable one-step method, the error recursion has the schematic form

`||e_{k+1}||
<=
(1+C h_k)||e_k||
+
||delta_{k+1}||`.

The factor multiplying `e_k` matters.

Repeated amplification can dominate small local defects.

That is why numerical analysis separates:

- consistency;
- stability;
- convergence.

A network analogy that mentions only one-step approximation misses the accumulated-dynamics problem.

## 9. More layers do not automatically mean finer discretization

Take a 12-layer residual network and a 24-layer residual network.

Can we say the second uses half the step size?

Only if the two belong to a declared refinement family.

For a numerical refinement, we normally hold the continuous problem fixed while changing the mesh.

A deeper neural network may instead change:

- all learned parameters;
- residual scaling;
- width;
- normalization;
- activation structure;
- feature coordinates;
- training objective;
- optimizer.

That is a different model, not necessarily a finer mesh.

So the statement

> more layers give smaller discretization error

needs an actual refinement construction.

Depth alone does not supply it.

## 10. The scalar test equation enters neural depth

The Numerical Methods chapter used the scalar test equation

`x'=lambda x`.

This small system exposes stability cleanly.

For explicit Euler,

`x_{k+1}=(1+h lambda)x_k`.

Define

`z=h lambda`.

The amplification factor is

`R(z)=1+z`.

The standard non-growth stability condition is

`|1+z|<=1`.

This exact calculation transfers directly to a linear residual block when the block has been declared to represent the Euler step.

Now numerical stability has architectural meaning:

small perturbations in that scalar mode are multiplied by the same amplification factor across depth.

## 11. A stable continuous mode can become an unstable network step

Set

`lambda=-1`.

The continuous solution decays:

`x(t)=e^{-t}x(0)`.

Euler gives

`x_{k+1}=(1-h)x_k`.

The non-growth condition is

`|1-h|<=1`.

For real nonnegative `h`, the non-growth set is

`0<=h<=2`.

Strict asymptotic decay requires

`0<h<2`.

At `h=2`, the factor is `-1`: bounded but non-decaying.

Now choose

`h=3`.

The exact continuous factor over one step is

`e^{-3}`.

The Euler factor is

`-2`.

The continuous mode decays strongly.

The discrete mode doubles in magnitude and flips sign.

Nothing happened to the ODE.

The discretization changed the dynamics.

This is one of the most useful lessons numerical analysis contributes to neural architecture:

> the update rule has its own dynamics.

## 12. Numerical stability is not training stability

The previous example concerns forward propagation of state perturbations.

That is not the same thing as optimization stability.

Training can be unstable because of:

- exploding gradients;
- vanishing gradients;
- learning-rate choice;
- optimizer state;
- minibatch noise;
- curvature;
- non-normal transients;
- parameterization.

Forward numerical stability and training stability can interact.

They can share Jacobian structure.

But they are not interchangeable.

Haber and Ruthotto explicitly use dynamical-systems and discrete-ODE stability ideas to motivate stable deep architectures [@HaberRuthotto2018].

That bridge is useful precisely because the notions are related.

It should not be read as an identity between all numerical and optimization stability concepts.

## 13. The residual Jacobian is a perturbation propagator

For

`Psi_k(x)=x+F_k(x)`,

the Jacobian is

`J_{Psi_k}(x)=I+J_{F_k}(x)`.

For a small perturbation `delta x_k`,

`delta x_{k+1}
approximately
J_{Psi_k}(x_k) delta x_k`.

Across many layers,

`delta x_N
approximately
J_{Psi_{N-1}}
...
J_{Psi_0}
delta x_0`.

This is a discrete tangent evolution.

It is one reason residual systems are naturally analyzed dynamically.

But again the claim must remain scoped.

The Jacobian product describes local first-order perturbation propagation along the realized discrete trajectory.

It is not, by itself, a theorem about generalization or optimization success.

## 14. Exact finite witness: same flow, different discretization behavior

Consider

`x'=-x`,
`x(0)=1`.

The exact solution at time `1` is

`e^{-1}`.

Use explicit Euler with `N` equal steps:

`h=1/N`.

Then

`x_N=(1-1/N)^N`.

For `N=2`:

`x_2=1/4`.

For `N=4`:

`x_4=81/256`.

For `N=8`:

`x_8=5764801/16777216`.

These values move toward

`e^{-1}`

over the declared finite sequence.

The exact witness records both the rational values and their error against the exact flow.

But the finite table is not the convergence theorem.

The theorem that Euler is globally first order under standard assumptions comes from numerical analysis [@Iserles2008].

The witness only makes the mechanism visible.

## 15. Refinement is a family, not a single network

The exact witness contains something ordinary neural-network comparisons often lack.

It contains a controlled family:

- same ODE;
- same initial state;
- same final time;
- same numerical method;
- only the mesh changes.

That is what gives the phrase **refinement** mathematical force.

If a neural architecture study wants to make an analogous convergence claim, it needs a corresponding family.

For example, it might declare:

- a continuous target field;
- a sequence of grids;
- parameter interpolation across grids;
- a residual scaling rule;
- a common output time;
- a norm for comparing trajectories.

Without such a construction, comparing depths is architecture comparison, not numerical convergence analysis.

## 16. A modified-equation viewpoint

Numerical analysts often ask a different question:

> which nearby continuous equation is the discrete method solving more accurately?

This leads to modified-equation reasoning.

Lu, Zhong, Li, and Dong explicitly connect deep architectures with numerical differential-equation discretizations and use numerical ideas to motivate architecture design [@LuZhongLiDong2018].

This perspective can be more realistic than insisting on one exact underlying ODE.

A trained network may be profitably studied through a nearby effective flow.

But the same boundary remains:

the modified equation is an analytical construction under declared assumptions.

It is not automatically the network's unique hidden physical law.

## 17. Residual networks and Neural ODEs are related but different

The Architecture History chapter source-locks both residual networks and Neural ODEs [@HeZhangRenSun2016; @ChenRubanovaBettencourtDuvenaud2018].

A residual network directly defines finitely many maps.

A Neural ODE directly defines a continuous vector field and asks a numerical solver to construct the trajectory.

Those directions of definition differ.

For a ResNet:

`discrete architecture -> possible continuous interpretation`.

For a Neural ODE:

`continuous dynamics -> chosen numerical discretization at execution`.

The two meet through numerical analysis.

They should not be collapsed.

## 18. The discretization can become part of the model

In a classical numerical simulation, changing the solver while refining the mesh is often intended to preserve the same underlying physical model.

In learned systems, the situation can be more entangled.

The architecture, solver, parameterization, and training process may adapt to one another.

A change of discretization may change:

- optimization geometry;
- parameter sharing;
- expressive bias;
- compute cost;
- numerical error;
- learned representation.

So the phrase **discretization error** should be reserved for error relative to a declared continuous reference.

Performance change after changing architecture is a broader empirical phenomenon.

## 19. Reversibility has three meanings

The word **reversible** causes another common collision.

We must distinguish:

### Map invertibility

A layer map `Psi` is one-to-one and has an inverse.

### Computational reversibility

Earlier states can be reconstructed from later states, perhaps to reduce activation storage.

### Time reversibility of a numerical method

A one-step method is symmetric if

`Psi_{-h}=Psi_h^{-1}`.

These properties can overlap.

They are not identical.

A layer can be invertible without being a symmetric integrator.

## 20. Explicit Euler is invertible and not time reversible

Return to

`x'=-x`.

Euler gives

`Psi_h(x)=(1-h)x`.

For

`h!=1`,

the map is invertible.

Its inverse is

`Psi_h^{-1}(x)=x/(1-h)`.

Now apply Euler with negative step:

`Psi_{-h}(x)=(1+h)x`.

Compose:

`Psi_{-h}(Psi_h(x))
=
(1-h^2)x`.

Except at `h=0`, this is not the identity.

So the same update formula run with `-h` does not undo the forward step.

The method is not time reversible.

## 21. Exact reversibility witness

Choose

`h=1/2`.

The forward step multiplies by

`1/2`.

Its true inverse multiplies by

`2`.

The negative-step Euler map multiplies by

`3/2`.

Forward followed by negative-step Euler gives

`3/4`.

That one line separates the concepts:

- invertible map: yes;
- same method with negative step is inverse: no;
- time-symmetric method: no.

The exact flow behaves differently:

`e^{h}e^{-h}=1`.

## 22. Why this matters for reversible neural networks

A reversible neural architecture may guarantee that activations can be reconstructed.

That is valuable for memory.

But it does not follow that the architecture is a reversible numerical integrator for an underlying differential equation.

Conversely, a symmetric numerical integrator has a time-reversal property tied to its step map.

Its software implementation may still use memory in an ordinary irreversible way.

The adjective is the same.

The mathematical objects are different.

## 23. Stability also has several meanings

The same linguistic problem appears with **stability**.

In this chapter we need at least:

- absolute stability of a numerical method;
- perturbation stability of a discrete map;
- Lyapunov stability of a dynamical system;
- conditioning/sensitivity;
- optimization stability;
- robustness under data or distribution perturbation.

The Numerics chapter already warned that the scalar stability region is not a universal nonlinear certificate.

NETNUM adds a second warning:

> the word "stable" should not move between numerical analysis and training dynamics without an explicit bridge.

This is especially important because deep-learning papers often use one term for several phenomena.

## 24. Stiffness in networks needs a declared dynamical problem

Can a neural network be stiff?

Sometimes the numerical analogy is useful.

If a declared continuous model has widely separated decay scales, an explicit discretization may face severe step restrictions.

But "the network has large Jacobian eigenvalues" is not, by itself, a complete stiffness statement.

Stiffness is partly problem-relative and method-relative [@HairerWanner1996].

To use the term rigorously we should identify:

- the continuous or effective dynamical problem;
- the numerical method;
- the scale separation;
- the step restriction or solver difficulty it induces.

Otherwise **stiff** risks becoming a synonym for "hard to train."

## 25. The numerical lens suggests architecture questions

Once the bridge is explicit, numerical analysis supplies useful design questions.

For a residual architecture, ask:

- Is the forward map in a stable regime?
- Does the update approximate a declared flow?
- What changes under depth refinement?
- Is the residual scale acting like a step size?
- Would an implicit update enlarge the stable region?
- Would a symmetric or structure-preserving composition protect an invariant?
- Does operator splitting isolate meaningful subdynamics?
- Does adaptive depth correspond to local error control?

These questions do not answer themselves.

They create disciplined hypotheses.

That is more valuable than merely calling a network an ODE.

## 26. What Haber–Ruthotto adds

Haber and Ruthotto develop deep architectures from the perspective of nonlinear dynamical systems and discrete ODE stability [@HaberRuthotto2018].

The important Atlas lesson is methodological.

Numerical analysis can be used not just to interpret an existing network after the fact, but to constrain architecture design.

If a discrete forward model has undesirable stability properties, modify the architecture.

This turns the numerical lens into engineering.

Still, source scope matters.

The paper motivates particular stable constructions.

It does not establish that every network instability is a numerical ODE instability.

## 27. What Lu et al. adds

Lu et al. connect several deep architectures to numerical differential-equation schemes and propose architectures inspired by numerical methods [@LuZhongLiDong2018].

This widens the design vocabulary.

A network block need not be compared only with forward Euler.

One can ask about analogues of:

- multistep methods;
- higher-order schemes;
- implicit methods;
- splitting methods;
- modified equations.

The Atlas uses this as a bridge, not as a license to label any multi-branch network with a numerical-method name.

Structural correspondence must be shown.

## 28. Architecture analogy versus numerical theorem

This distinction deserves a compact table.

| Statement | Status |
|---|---|
| `x_{k+1}=x_k+F_k(x_k)` resembles Euler form | algebraic observation |
| `F_k=h_k f(t_k,.)` for declared `f,h_k` | modeling declaration |
| local defect is `O(h^2)` | numerical theorem under smoothness assumptions |
| global error is `O(h)` | numerical theorem under stability/regularity assumptions |
| deeper network has smaller error | not implied without refinement semantics |
| residual Jacobian is `I+J_F` | exact differential identity |
| stable scalar Euler factor | exact for declared linear mode |
| training is stable | separate empirical/mathematical claim |

The point is not to weaken the analogy.

It is to give each statement the correct support route.

## 29. A practical numerical-network contract

Before using numerical language for a network, record:

| Field | Question |
|---|---|
| reference flow | What continuous evolution is being approximated? |
| step map | What network block corresponds to one numerical step? |
| mesh | What are `t_k` and `h_k`? |
| refinement | How is depth increased while preserving the same reference problem? |
| error | What norm and exact reference define local/global error? |
| stability | Which perturbation and which stability notion are intended? |
| reversibility | Invertibility, reconstruction, or numerical symmetry? |
| scope | Which claims are theorem, interpretation, or empirical observation? |

This contract prevents the numerical lens from silently changing categories.

## 30. Failure modes

### Residual-equals-Euler

A skip connection is treated as proof that the network is Euler discretization.

Failure: no continuous reference problem is specified.

### Depth-equals-time

Layer index is silently relabeled time.

Failure: no mesh or refinement relation exists.

### Small-residual-equals-small-error

A small residual update is treated as a small truncation defect.

Failure: no exact flow comparison is made.

### Stable-forward-equals-stable-training

A forward amplification argument is promoted into an optimizer theorem.

Failure: the objects differ.

### Invertible-equals-reversible-integrator

An invertible layer is called time reversible.

Failure: `Psi_{-h}=Psi_h^{-1}` was never checked.

### More-layers-equals-convergence

A deeper model is assumed closer to a continuous limit.

Failure: the target model and discretization family changed together.

## 31. Downstream handoff: Adaptive Depth

**Adaptive Depth as Error Control — ATLAS-CH-ADAPTDEPTH-001** may now assume:

- exact-flow versus step-map distinction;
- local versus global error;
- refinement-family discipline;
- step-size versus residual-scale distinction;
- scalar stability-function reasoning.

That chapter can ask whether learned stopping or variable compute can be interpreted as adaptive time stepping or local error control.

It must establish that bridge itself.

A stopping score is not automatically a local truncation-error estimator.

## 32. Downstream handoff: Boundary Probes

**Boundary Probes — ATLAS-CH-BOUNDARYPROBE-001** may now assume:

- one-step map `Psi_k`;
- local Jacobian `J_{Psi_k}`;
- first-order perturbation propagation;
- accumulated Jacobian products;
- the distinction between local sensitivity and global dynamics.

This prepares the language needed for JVPs, VJPs, power iteration, and interface sensitivity.

## 33. What this chapter establishes

The numerical interpretation of neural depth is strongest when it is conditional and explicit.

A residual architecture can be read as a numerical scheme when the continuous problem, step semantics, and refinement family are supplied.

Then numerical analysis contributes exact distinctions:

- local defect versus global error;
- consistency versus stability versus convergence;
- residual scale versus step size;
- forward stability versus optimization stability;
- invertibility versus time reversibility.

Without those declarations, the same vocabulary remains metaphor.

The goal is not to ban the metaphor.

It is to know when the metaphor has become mathematics.

## References used in this chapter

- Iserles, *A First Course in the Numerical Analysis of Differential Equations* [@Iserles2008].
- Hairer and Wanner, *Solving Ordinary Differential Equations II* [@HairerWanner1996].
- He et al., *Deep Residual Learning for Image Recognition* [@HeZhangRenSun2016].
- Chen et al., *Neural Ordinary Differential Equations* [@ChenRubanovaBettencourtDuvenaud2018].
- Haber and Ruthotto, *Stable Architectures for Deep Neural Networks* [@HaberRuthotto2018].
- Lu et al., *Beyond Finite Layer Neural Networks: Bridging Deep Architectures and Numerical Differential Equations* [@LuZhongLiDong2018].

Exact prerequisite identities and source-authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-NETNUM-001.yaml
