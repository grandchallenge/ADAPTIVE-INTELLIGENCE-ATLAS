# Representation as Transport
<!-- ATLAS-CH-TRANSPORT-001 -->

**Epistemic status:** established geometry and dynamics + audited prerequisite inheritance + Atlas synthesis.  
**Specification:** `manuscript/specifications/ATLAS-CH-TRANSPORT-001.md`  
**Derivation packet:** `mathematics/derivations/ATLAS-CH-TRANSPORT-001-DERIVATIONS.md`  
**Computational witness:** `mathematics/computational-witnesses/ATLAS-CW-TRANSPORT-001.md`  
**Source lock:** `sources/source-locks/ATLAS-CH-TRANSPORT-001.yaml`

A representation does not merely exist. In a deep adaptive system it is repeatedly changed.

The same hidden state may be:

- mixed by attention;
- transformed by a feed-forward map;
- normalized;
- gated;
- routed;
- projected;
- constrained;
- carried through a residual path;
- or updated by a continuous-depth evolution law.

The useful question is therefore not only:

> What is the representation?

It is also:

> How is the representation moved?

This chapter develops a disciplined answer.

The word **transport** will mean the evolution of a declared representation state through declared maps.

That definition is deliberately broad enough to cover finite neural compositions and constrained updates, but deliberately narrow enough to block several false identifications.

Representation transport is not automatically:

- optimal transport of probability mass;
- parallel transport under a connection;
- vector transport of tangent data;
- geodesic motion;
- an exact ODE flow.

Those objects may enter a model when their assumptions are actually present. They are not consequences of the word “transport.”

## 1. The primary object is a sequence of maps

Let the representation state at stage \(k\) be

\[
z_k\in\mathcal Z_k.
\]

A stage map is

\[
\Phi_k:\mathcal Z_k\to\mathcal Z_{k+1}.
\]

The update is

\[
z_{k+1}=\Phi_k(z_k).
\]

After \(K\) stages,

\[
z_K
=
(\Phi_{K-1}\circ\cdots\circ\Phi_0)(z_0).
\]

This composition is exact as written.

It does not require:

- an ODE;
- an infinitesimal step;
- a manifold;
- invertibility;
- a metric;
- a probability distribution.

That is the first transport object of the Atlas:

> **a finite representation trajectory is the ordered composition of the maps that actually execute.**

This sounds elementary. It is also where many conceptual mistakes begin.

If the executed map contains normalization, masking, routing, clipping, stochasticity, or projection, those operations belong to \(\Phi_k\). Omitting them means analyzing another system.

## 2. Residual transport

A residual stage has the familiar form

\[
\Phi_k(z)
=
z+F_k(z).
\]

The identity term gives a direct state path. The learned residual modifies it.

Residual networks made this identity-plus-increment structure an explicit architecture [@HeZhangRenSun2016].

At the discrete level, the statement is exact:

\[
\text{next state}
=
\text{current state}
+
\text{learned increment}.
\]

The dynamical interpretation is useful, but it must come second.

If we instead write

\[
\Phi_{k,h}(z)
=
z+hF_k(z),
\]

the algebra resembles an explicit Euler step.

That resemblance becomes a numerical statement only after a reference evolution law has been declared.

The equation

\[
z_{k+1}=z_k+hF_k(z_k)
\]

does not by itself tell us that one unique continuous vector field generated the network.

This is inherited doctrine from the audited Split-Operator and numerical chapters.

## 3. Continuous depth is a different declaration

Neural ODEs make a stronger object explicit:

\[
\frac{dz}{dt}
=
f(z,t;\theta).
\]

The architecture defines a continuous-depth evolution law and obtains finite-time state changes through the associated ODE solution and numerical integration [@ChenRubanovaBettencourtDuvenaud2018].

This is a genuine continuous-time transport object.

A residual stack and a Neural ODE can be related.

They are not identical by definition.

The safe implication is:

\[
\text{explicit ODE architecture}
\Rightarrow
\text{declared continuous state evolution}.
\]

The unsafe implication is:

\[
\text{residual stack}
\Rightarrow
\text{unique exact ODE}.
\]

Haber and Ruthotto use dynamical-systems and discrete-ODE stability ideas to motivate deep architecture design [@HaberRuthotto2018]. That bridge is valuable precisely because it makes assumptions visible. It should not be turned into an identity between all deep networks and one continuous flow.

## 4. Stage index is not automatically physical time

The index

\[
k=0,1,\ldots,K
\]

orders computation.

It need not represent physical time.

Even when one speaks of “depth as time,” several meanings are possible:

- literal continuous time in an ODE;
- numerical time in a discretization;
- recurrent iteration count;
- transformer block index;
- optimization iteration;
- adaptive computational depth.

Transport language becomes useful when these are distinguished rather than blended.

A chapter that says “the representation moves through time” must say what the time variable is.

## 5. The constrained case

Suppose representation states lie on a manifold

\[
M\subseteq\mathbb R^n.
\]

Now the update has two separate questions:

1. what direction is proposed?
2. how is a legal endpoint on \(M\) produced?

At state \(z_k\), a tangent proposal satisfies

\[
\xi_k\in T_{z_k}M.
\]

A retraction maps tangent data back to the manifold:

\[
z_{k+1}
=
R_{z_k}(\xi_k).
\]

For the unit sphere,

\[
S^{n-1}
=
\{u:\|u\|_2=1\},
\]

the tangent condition is

\[
u^\top\xi=0.
\]

A standard normalized retraction is

\[
R_u(\xi)
=
\frac{u+\xi}{\|u+\xi\|_2}.
\]

This guarantees

\[
\|R_u(\xi)\|_2=1.
\]

It guarantees feasibility.

Nothing in that equation says the update is:

- geodesic;
- optimal;
- invertible;
- information preserving;
- dynamically stable;
- task improving.

The NORMREP prerequisite established exactly this geometry and the radial-information boundary [@Lee2018Riemannian; @AbsilMahonySepulchre2008].

## 6. Feasible motion is not geodesic motion

Take the unit circle.

Let

\[
u=(1,0),
\qquad
\xi=(0,1).
\]

The normalized retraction gives

\[
R_u(\xi)
=
\frac{(1,1)}{\sqrt2}.
\]

This point is on the circle.

Its angular displacement from \(u\) is

\[
\frac{\pi}{4}.
\]

Now use the sphere exponential map with the same unit tangent vector at unit time.

The endpoint is

\[
\operatorname{Exp}_u(\xi)
=
(\cos1,\sin1).
\]

Its angular displacement is

\[
1.
\]

Since

\[
\frac{\pi}{4}\neq1,
\]

the endpoints differ.

This is the smallest exact warning we need:

> **returning to the manifold is not the same thing as following the manifold geodesic.**

A retraction is often computationally convenient because it approximates the exponential map locally [@AbsilMahonySepulchre2008].

Approximation is not identity.

## 7. Moving the point and moving an arrow are different operations

The phrase “transport” is overloaded in geometry.

Suppose

\[
v_0\in T_{u_0}M.
\]

After the base point moves from \(u_0\) to \(u_1\), the same ambient coordinate vector need not belong to

\[
T_{u_1}M.
\]

This matters whenever a system carries local information such as:

- momentum;
- a tangent update;
- a local search direction;
- a basis;
- a differential perturbation;
- optimizer state defined intrinsically on a manifold.

The state update answers:

> Where did the point move?

A vector-transport or parallel-transport rule answers another question:

> How should tangent information be represented at the new point?

Those are not the same map.

## 8. Exact tangent-ownership witness

Take

\[
u_0=(1,0),
\qquad
v_0=(0,1).
\]

Initially,

\[
u_0^\top v_0=0,
\]

so

\[
v_0\in T_{u_0}S^1.
\]

Move the state by normalized retraction:

\[
u_1
=
\frac{(1,1)}{\sqrt2}.
\]

Now test the old tangent vector against the new base point:

\[
u_1^\top v_0
=
\frac1{\sqrt2}.
\]

Therefore

\[
v_0\notin T_{u_1}S^1.
\]

The same ambient coordinates are no longer legal tangent data.

The orthogonal projection onto the new tangent space is

\[
P_{u_1}v_0
=
v_0-(u_1^\top v_0)u_1
=
\left(-\frac12,\frac12\right).
\]

This projected vector is tangent because

\[
u_1^\top P_{u_1}v_0=0.
\]

Projection is one possible local operation.

It is not automatically parallel transport.

It is not automatically the best vector transport for a learning algorithm.

The durable rule is simply:

> **tangent data belongs to a base point.**

## 9. The local-compass allegory

Imagine moving across the surface of a globe while carrying a small arrow that lies flat against the surface.

Two things happen:

- your location changes;
- the meaning of “this arrow lies tangent here” changes with location.

Moving the location does not automatically tell you how to carry the arrow.

That is the geometric distinction between:

- state transport;
- tangent-data transport.

The analogy has a strict limit.

A neural representation space may not be a smooth manifold at all. Even when we constrain vectors to a sphere, the complete learned computation can include discrete routing, masking, non-smooth nonlinearities, and dimension-changing interfaces.

The allegory is useful only where the declared geometry supports it.

## 10. Path order can matter even when every endpoint is feasible

The Split-Operator prerequisite established that ordered maps need not commute.

Constrained transport adds another useful witness.

Start on

\[
S^2
\]

at

\[
u_0=(1,0,0).
\]

Choose

\[
a=(0,1,0),
\qquad
b=(0,0,1).
\]

Both are tangent at \(u_0\).

Use normalized retraction

\[
R_u(\xi)
=
\frac{u+\xi}{\|u+\xi\|}.
\]

Apply \(a\) first:

\[
u_a
=
\frac{(1,1,0)}{\sqrt2}.
\]

The vector \(b\) remains tangent there, because

\[
u_a^\top b=0.
\]

Apply the second stage:

\[
u_{ab}
=
R_{u_a}(b)
=
\left(
\frac12,
\frac12,
\frac1{\sqrt2}
\right).
\]

Reverse the order:

\[
u_b
=
\frac{(1,0,1)}{\sqrt2},
\]

then

\[
u_{ba}
=
R_{u_b}(a)
=
\left(
\frac12,
\frac1{\sqrt2},
\frac12
\right).
\]

Both endpoints are feasible:

\[
\|u_{ab}\|_2
=
\|u_{ba}\|_2
=
1.
\]

But

\[
u_{ab}\neq u_{ba}.
\]

The exact inner product is

\[
u_{ab}^\top u_{ba}
=
\frac14+\frac1{\sqrt2}.
\]

Constraint preservation therefore does not erase path ordering.

This is not a universal theorem that every pair of constrained neural updates must fail to commute.

It is a finite counterexample to the opposite claim.

## 11. The executed maps determine the path

If the network executes

\[
z_{k+1}
=
R_{z_k}\bigl(\xi_k(z_k)\bigr),
\]

then both objects matter:

- the field or proposal \(\xi_k\);
- the endpoint map \(R\).

Replacing the retraction changes the transport.

Replacing the order changes the transport.

Dropping normalization changes the transport.

Changing the base point before evaluating the next stage changes the transport.

This is the correct level at which architectural comparisons should begin.

## 12. State-dependent transport

Many neural maps are state-dependent.

Attention is the clearest example: the operator applied at one stage depends on the current state.

So a map such as

\[
z_{k+1}
=
\Phi_k(z_k)
\]

is generally not a fixed matrix multiplying every possible input.

Its differential at one point is

\[
J_{\Phi_k}(z_k).
\]

That Jacobian can describe local perturbation propagation.

It is another object again.

We must separate:

- the nonlinear state map;
- its local Jacobian;
- a tangent-space transport rule;
- a global flow, if one exists.

These objects can interact without being interchangeable.

## 13. Differential pushforward is not automatically vector transport

For a differentiable map,

\[
\Phi:M\to N,
\]

the differential maps tangent vectors by

\[
D\Phi_z:
T_zM
\to
T_{\Phi(z)}N.
\]

This is a precise geometric construction when the required smooth manifold setting exists.

In ordinary neural calculations one often works instead with an ambient Jacobian

\[
J_\Phi(z).
\]

If constraints, quotient structure, projections, or non-smooth operations are present, the relation between the ambient Jacobian and an intrinsic tangent-space map must be stated.

Calling every Jacobian multiplication “vector transport” would erase these distinctions.

The Atlas will not do that.

## 14. Transport can lose information

A constrained path can remain perfectly feasible while destroying distinctions.

The simplest example is normalization:

\[
N(x)
=
\frac{x}{\|x\|}.
\]

For every

\[
c>0,
\]

\[
N(cx)=N(x).
\]

The positive radial degree of freedom disappears.

If the original representation stored useful information in norm, the transport has erased it unless another channel carries that quantity.

Therefore:

\[
\text{feasible constrained transport}
\not\Rightarrow
\text{information-preserving transport}.
\]

This is inherited directly from the NORMREP chapter.

## 15. Transport can also relocate information

Information removed from one coordinate channel can reappear elsewhere.

A normalized architecture may retain magnitude through:

- explicit scale parameters;
- residual amplitudes;
- gates;
- temperatures;
- separate scalar channels;
- logits;
- routing variables.

The right question is not whether normalization “destroys scale” in some absolute sense.

It is:

> Which distinctions survive in the complete state carried forward?

Transport is therefore an interface-level concept.

A local geometric constraint does not describe the full system state unless the system state has actually been defined that way.

## 16. Shared and stage-dependent transport

Suppose every layer uses the same map:

\[
\Phi_k=\Phi.
\]

Then

\[
z_K=\Phi^K(z_0).
\]

This repeated-map structure supports one kind of dynamical interpretation.

Now suppose the parameters change at every layer:

\[
\Phi_0,\Phi_1,\ldots,\Phi_{K-1}.
\]

Then the system is stage-dependent.

A continuous analogy, if one is introduced, is naturally nonautonomous:

\[
\dot z=f(z,t).
\]

The chapter does not collapse these two cases.

A single autonomous generator is a stronger statement than an ordered family of learned maps.

## 17. Stability is a separate question

Transport language does not answer whether perturbations grow.

For two nearby states,

\[
z_k,\qquad z_k+\delta z_k,
\]

a local linearization gives

\[
\delta z_{k+1}
\approx
J_{\Phi_k}(z_k)\delta z_k.
\]

Across many stages,

\[
\delta z_K
\approx
J_{\Phi_{K-1}}(z_{K-1})
\cdots
J_{\Phi_0}(z_0)
\delta z_0.
\]

The product may:

- contract;
- preserve;
- amplify;
- rotate;
- shear;
- become highly non-normal.

Those are stability and sensitivity questions.

They do not follow from the fact that the base representation path remains feasible.

Haber–Ruthotto’s dynamical-systems perspective is relevant here [@HaberRuthotto2018], but no universal stability claim is inherited.

## 18. Invertibility is also separate

A map can transport a state forward while discarding information.

Normalization is one example.

ReLU is another familiar non-injective operation on part of its domain.

Pooling, clipping, quantization, token dropping, and many routing decisions can also be non-invertible.

Therefore

\[
\text{state evolution}
\not\Rightarrow
\text{reversible state evolution}.
\]

A reversible architecture requires its own construction and proof obligations.

## 19. This is not optimal transport

Optimal transport studies the movement of mass or probability measures under a specified cost and admissible coupling/map structure.

Nothing in

\[
z_{k+1}=\Phi_k(z_k)
\]

by itself defines:

- a probability measure;
- a source and target distribution;
- a coupling;
- a transport cost;
- an optimality problem.

Representation transport may eventually be connected to optimal-transport ideas in a separately specified model.

The current chapter does not make that identification.

## 20. This is not parallel transport

Parallel transport requires geometric structure specifying how tangent vectors are carried along curves, usually through a connection.

The state path

\[
z_0\to z_1\to\cdots\to z_K
\]

does not automatically define such a rule.

Even on a sphere, “project the old tangent vector onto the new tangent plane” and “parallel transport the tangent vector along the connecting geodesic” are different constructions.

The Atlas uses the terminology literally.

## 21. This is not vector transport either

Optimization on manifolds often introduces a **vector transport** to move tangent vectors from one tangent space to another in a computationally convenient way [@AbsilMahonySepulchre2008].

That is closer to the machine-learning setting than abstract parallel transport, but it remains distinct from moving the representation point itself.

The notation should therefore preserve two maps when both are present:

\[
z_{k+1}
=
R_{z_k}(\xi_k),
\]

and

\[
v_{k+1}
=
\mathcal T_{\xi_k}(v_k).
\]

The first moves state.

The second moves tangent information.

A system that carries optimizer momentum on a manifold may need both.

## 22. Transport and split operators

Suppose one representation block contains two declared state maps,

\[
\Phi_A,
\qquad
\Phi_B.
\]

Then chronological A-then-B transport is

\[
\Phi_B\circ\Phi_A.
\]

Chronological B-then-A transport is

\[
\Phi_A\circ\Phi_B.
\]

The Split-Operator chapter already established why these can differ and why execution order must be explicit.

TRANSPORT adds the constraint-aware reading:

- the first stage changes the base state seen by the second;
- tangent spaces may also change;
- a constraint-restoring map can introduce additional path dependence;
- exact-flow commutator theory must not be imported unless its assumptions hold.

This is a synthesis, not a new numerical theorem.

## 23. Transport and residual identity paths

Residual architectures are especially natural to describe as transport because the identity path makes the old state explicitly available to the next stage.

If

\[
F_k(z)=0,
\]

then

\[
\Phi_k(z)=z.
\]

That is exact identity transport at that stage.

It does not prove:

- that information remains unchanged when \(F_k\neq0\);
- that gradients propagate perfectly;
- that the full model is invertible;
- that the representation follows a geodesic;
- that the architecture is stable.

Identity transport is one structural ingredient.

## 24. Transport as an interface contract

The most useful role of this chapter is to define what a downstream method is allowed to assume.

A downstream algorithm should be able to ask:

- What is the state space?
- What is the current base state?
- What map advances it?
- Is the map linear or nonlinear?
- Is it shared or stage-dependent?
- Is there a constraint?
- Is the update tangent?
- What returns the state to the constraint set?
- Is tangent history being carried?
- If so, by what rule?
- Is there an exact continuous flow or only a finite composition?
- Which information is intentionally invariant or discarded?

Those questions turn “representation transport” from a metaphor into an interface.

## 25. Handoff to Neural Krylov Transport

The next downstream chapter is

`ATLAS-CH-NEURALKRYLOV-001`.

That chapter will explore short-horizon preconditioned solves as representation computation.

TRANSPORT supplies only the representation-side interface.

For example, if a differentiable state map is

\[
z_{k+1}=\Phi_k(z_k),
\]

one may study its local linearization

\[
J_{\Phi_k}(z_k).
\]

A Krylov construction could then be posed for a declared operator built from that local object.

But classical Krylov theory requires its own assumptions:

- a specified linear operator;
- a generated Krylov subspace;
- a projection or residual criterion;
- conditioning/preconditioning semantics;
- finite-precision limits;
- convergence hypotheses.

None of those arrive for free from the transport language.

The hard boundary is:

\[
\text{representation transport}
\not\Rightarrow
\text{Krylov convergence guarantee}.
\]

## 26. Five distinctions to keep visible

### State transport versus tangent transport

Moving \(z_k\) is not the same problem as moving \(v_k\in T_{z_k}M\).

### Feasibility versus geodesic exactness

A retraction can keep a point on the manifold without following the exponential map.

### Discrete composition versus continuous flow

A finite neural stack is exact as a composition of maps, not automatically as an ODE solution.

### Constraint preservation versus information preservation

A normalized path can remain feasible while erasing radial distinctions.

### Order versus ingredients

The same named stages applied in another order can produce another endpoint.

## 27. Failure modes

The transport language fails when it is used to smuggle in stronger mathematics than the model contains.

Common failures are:

- calling any sequence of activations an ODE trajectory;
- calling any normalized update geodesic motion;
- calling state evolution vector transport;
- calling tangent projection parallel transport;
- calling representation movement optimal transport without measures and costs;
- treating unit norm as information preservation;
- treating feasibility as stability;
- treating repeated residual form as one autonomous generator;
- treating a local Jacobian as the global nonlinear map;
- transferring Krylov convergence claims to learned nonlinear transport by analogy.

Each mistake replaces a declared object with a stronger undeclared one.

## 28. Closing view

A deep model can be read as a machine for moving representations.

That reading is useful when it remains literal.

The representation at one stage is a state.

The next stage applies a map.

Constraints may restrict where the state is allowed to live.

Retractions may restore feasibility.

Tangent data may require its own transport rule.

Order may change the path.

Continuous-depth models may provide an actual flow.

Finite residual networks may provide only a composition.

**Representation transport** is a useful mathematical description when its state, stage maps, constraints, and path semantics have been specified. These ingredients do not themselves establish a continuous flow, geodesic, or an optimal transport problem. Each stronger description requires separate hypotheses.



## References used in this chapter

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@HeZhangRenSun2016]
- [@ChenRubanovaBettencourtDuvenaud2018]
- [@HaberRuthotto2018]

Exact provenance and claim boundaries are locked in:

`sources/source-locks/ATLAS-CH-TRANSPORT-001.yaml`.
