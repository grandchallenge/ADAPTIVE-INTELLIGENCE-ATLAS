# Depth as Computational Time
<!-- ATLAS-CH-DEPTH-001 -->

**Epistemic status:** established adaptive-depth mechanisms plus Atlas synthesis and exact finite derivation.  
**Specification:** manuscript/specifications/ATLAS-CH-DEPTH-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-DEPTH-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-DEPTH-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-DEPTH-001.yaml

A network layer can be read as a transformation.

A stack of layers can also be read as a history.

That second reading changes what depth means.

Instead of asking only how many transformations the architecture contains, we can ask how much computation a representation has undergone before the system decides it is finished.

This is the computational-time view of depth.

It is useful precisely because it is weaker than a claim about physical time.

Depth need not be seconds.

It need not be the time variable of one hidden differential equation.

It is an ordered coordinate of computation.

Once that coordinate is explicit, fixed-depth networks, recurrent-depth networks, adaptive halting, equilibrium models, and conditional execution can be compared without pretending they are the same architecture.

## 1. Five notions of time

Several indices are routinely called "time" in machine learning.

They should not be merged.

Physical time measures duration in the external world.

Sequence time indexes positions or events in data.

Optimization time indexes parameter updates.

Network depth indexes transformations applied within one forward computation.

Computational time counts or weighs internal state transitions used to produce one result.

A recurrent model may have sequence time t and computational-depth index k at the same moment.

A training run adds optimization step n.

A deployed system adds wall-clock duration.

These coordinates interact, but they answer different questions.

The purpose of this chapter is to make the depth coordinate explicit enough that later chapters can reason about allocating it.

## 2. Fixed depth

Write a depth-L computation as

x_{k+1}=F_k(x_k),
k=0,...,L-1.

Then

x_L
=
F_{L-1} o ... o F_0(x_0).

The architecture commits in advance to L sequential transformations.

Different inputs may produce different activations, but the nominal transformation count is fixed.

This is the familiar layer-stack view.

The computational-time view does not reject it.

It notices that L is also a budget decision.

Every input is given the same number of depth transitions, whether it needs all of them or not.

That uniformity can be desirable.

It simplifies batching, latency prediction, and implementation.

It is also only one possible allocation rule.

## 3. Depth is not automatically physical time

The Numerics chapter gave us a disciplined way to interpret repeated updates.

A residual update can resemble a numerical step.

A tied recurrence can resemble repeated evolution under one operator.

Those analogies are useful.

But the index k does not become physical time merely because the equations resemble an integrator.

A network may change its operator with k.

Its step size may have no declared physical units.

Training may learn transformations with no claim of approximating a continuous process.

The Atlas therefore uses a careful phrase:

depth can serve as computational time.

That is an architectural interpretation.

A stronger claim that a particular network discretizes a particular differential equation requires additional evidence.

## 4. Recurrent depth

Now tie the transformation:

x_{k+1}=F(x_k).

One operator is reused across computational depth.

This separates parameter count from execution count.

Running F ten times does not require ten independently parameterized layers.

It also introduces a new question:

what happens if we keep going?

Nothing in weight tying answers that.

The sequence may converge.

It may oscillate.

It may diverge.

It may enter a cycle.

It may converge in some regions of state space and fail in others.

Recurrent depth therefore turns "more layers" into an iterative-dynamics question.

Universal Transformer is a representative example in which a transformation is applied recurrently across depth rather than assigning a wholly independent block to every depth position.

The important mechanism is repeated computation, not the product name.

## 5. A computation can stop itself

Fixed depth chooses L before inference.

Adaptive depth lets the execution decide when to stop.

Let h_k be a declared halting signal.

Let epsilon be a threshold.

Let K_max be the largest permitted depth under the current compute budget.

Define

tau
=
min(
{k in {0,...,K_max} : h_k <= epsilon}
union
{K_max}
).

The realized output is x_tau.

The termination status must also be retained:

criterion_met if h_tau <= epsilon;

budget_exhausted otherwise.

This equation separates two ideas.

The recurrence determines how state changes.

The stopping rule determines how long the recurrence is allowed to run.

That separation is essential.

A poor halting rule can stop a good recurrence too early.

A good halting rule cannot rescue a recurrence that moves in the wrong direction.

And a halting score is not automatically an error estimate merely because training learns it.

Graves's Adaptive Computation Time is a concrete mechanism for learning variable numbers of recurrent steps.

Universal Transformer adds a dynamic per-position halting mechanism to recurrent depth.

These sources show that learned variable computation is an implementable mechanism.

They do not show that learned halting always tracks task difficulty correctly.

## 6. An exact depth-as-error witness

Consider the scalar recurrence

x_{k+1}
=
(x_k+2)/2,

with

x_0=0.

The fixed point is 2.

Subtract it:

x_{k+1}-2
=
(1/2)(x_k-2).

Hence

x_k
=
2(1-2^{-k}),

and the exact error is

|x_k-2|
=
2^{1-k}.

Depth now has a literal approximation meaning for this one system.

At depth 1, the error is 1.

At depth 2, it is 1/2.

At depth 3, it is 1/4.

At depth 5, it is 1/16.

For tolerance epsilon in (0,2), the minimum depth satisfying the tolerance is

tau(epsilon)
=
ceil(log_2(2/epsilon)).

The transformation did not change.

The requested accuracy changed how long we computed.

This is the simplest useful model of adaptive computational time.

It is also deliberately narrow.

Most learned networks do not hand us an exact error formula.

The later Adaptive Depth as Error Control chapter exists precisely because learned stopping becomes much more interesting when h_k must stand in for unknown task error.

## 7. Compute is more than step count

Suppose two systems both take four depth transitions.

They need not cost the same amount.

One may use a small operator at every step.

Another may invoke attention over a long sequence.

One may reuse cached state.

Another may move large tensors through memory.

One may parallelize internal work.

Another may be sequential.

So define realized computational cost more carefully.

For one declared resource unit,

C(x_0)
=
sum_{k=0}^{tau-1} c_k(x_k),

where c_k records the cost of the executed transition in that unit.

If several heterogeneous resources are tracked, use a vector such as

C_vec
=
(C_FLOPs, C_memory, C_energy, C_latency-proxy)

rather than adding unlike units without a declared scalarization.

The integer tau tells us sequential depth.

It does not by itself tell us wall-clock latency.

This becomes especially important for conditional computation.

Skipping half the mathematical blocks is not useful as a speed claim unless the implementation actually avoids the relevant work and the hardware can exploit the irregular execution.

## 8. Equilibrium depth

Recurrent depth suggests taking more and more iterations.

Equilibrium models make a different move.

Instead of declaring an explicit number of layers, define the representation by a fixed-point equation:

x*=F(x*).

The computational problem becomes:

find x*.

Deep Equilibrium Models are a representative neural architecture built around this idea.

The phrase "infinite depth" is evocative but must be handled carefully.

The model does not need to store an actually infinite sequence of layer activations.

It solves a fixed-point/root-finding problem.

And the equilibrium equation does not prescribe one solver.

Naive fixed-point iteration

x_{k+1}=F(x_k)

is one possibility.

Other root-finding methods can reach the same equation through different computational trajectories.

This distinction matters because an equilibrium can exist while naive iteration fails to converge.

Definition of a fixed point and convergence of a solver are different claims.

## 9. Convergence is an architectural question only after assumptions

For the exact witness, F is a contraction.

Every step halves the distance to the fixed point.

That gives a clean convergence story.

A learned recurrent transformation need not have that property.

The local Jacobian may expand in some directions.

The operator may have multiple fixed points.

A solver may depend on initialization.

A stopping test may declare convergence while task-relevant quantities remain wrong.

Equilibrium depth therefore does not abolish numerical analysis.

It makes numerical analysis part of the architecture.

The solver, tolerance, maximum iterations, residual test, initialization, and failure handling are all computational choices.

## 10. Conditional depth

Adaptive halting asks when to stop a sequential computation.

Conditional execution asks which blocks to run at all.

For a residual-style block, write

x_{k+1}
=
x_k
+
g_k(x_k) Delta_k(x_k).

With a hard gate

g_k in {0,1},

the block is either applied or skipped.

If g_k=0 and the implementation respects that decision before evaluating Delta_k, the block's expensive transform can be avoided.

SkipNet is a representative architecture of this kind: an input-dependent routing policy skips residual blocks.

This creates input-dependent effective depth.

Two examples entering the same nominal network can traverse different numbers of transformations.

## 11. Soft gates are not free skips

During training, it is often convenient to relax a binary gate:

g_k in [0,1].

Then the update can interpolate continuously between carry and transform.

But the computational claim changes.

If the system must compute Delta_k(x_k) before multiplying it by a small g_k, then the expensive operation was not skipped.

A soft coefficient near zero is mathematical sparsity of influence.

It is not necessarily computational sparsity of execution.

This distinction is easy to lose when a paper reports sparse weights, sparse gates, or small activation coefficients.

The hardware question is concrete:

which operations were never executed?

That boundary is handed directly to the later Conditional Computation chapter.

## 12. Effective depth is input-dependent execution history

For hard gating, define the active block set

A(x_0)
=
{k : g_k(x_k)=1}.

A simple realized block cost is

C_block(x_0)
=
sum_{k in A(x_0)} c_k,

plus the overhead required to make the routing decisions.

The path is a function of the evolving state.

This means conditional depth can create system effects absent from a static layer count.

Different examples may have different latency.

A batch may wait for its slowest member.

Branch divergence may reduce hardware utilization.

Routing decisions themselves cost compute.

The mean number of active blocks is therefore not the same quantity as end-to-end throughput.

## 13. Parameter depth and execution depth

A weight-tied recurrent system may have few unique parameters and many execution steps.

A large feed-forward system may have many unique parameters and one pass through each.

An equilibrium model may have a compact parameterization but a variable number of solver iterations.

A conditional network may contain many blocks but execute only some of them for one input.

This suggests at least three separate depth coordinates:

architectural depth:
how many transformation slots are represented in the nominal graph;

parameter depth:
how many distinct parameterized transformations occur along the path;

execution depth:
how many sequential transformations are actually evaluated for this input.

They coincide in a plain feed-forward stack.

They separate in recurrent, equilibrium, and conditional systems.

## 14. Halting is a decision under uncertainty

An adaptive system rarely knows the true remaining task error.

It sees proxies.

A confidence score.

A residual norm.

A change in representation.

A learned halting logit.

A budget counter.

A task-specific certificate.

The stop decision therefore has two possible errors.

Stop too early and computation is insufficient.

Continue too long and resources are wasted.

This is the computational analogue of a sequential decision problem.

But this chapter does not yet equate adaptive halting with numerical error control.

A learned halting logit may correlate with difficulty without estimating a rigorous truncation error.

The next numerical chapter will ask what additional structure is needed before a stopping signal can be interpreted as an error-control mechanism.

## 15. More depth can make things worse

The computational-time picture can tempt us into a monotone story:

more time, better answer.

That is false in general.

An unstable recurrence can amplify error.

Repeated application can oversmooth or collapse distinctions.

A learned iterative process can move away from a useful intermediate state.

A conditional controller can route difficult inputs into pathological loops.

An equilibrium solver can fail its tolerance or reach an unintended root.

More computation is only useful when the dynamics and stopping semantics support it.

Depth is a resource coordinate.

It is not a quality score.

## 16. Budget exhaustion is a first-class outcome

Suppose execution terminates at the finite budget cap K_max before the declared criterion h_k <= epsilon is met.

The termination status is then budget_exhausted rather than criterion_met.

If the budget limit is reached first, the system has not necessarily converged.

It has terminated because resources ended.

That outcome should be distinguishable from successful halting.

A production system may still return its best current state.

A scientific report should not label that return "converged" unless the declared criterion was met.

This sounds obvious.

It becomes less obvious when adaptive computation is buried inside a large model and the maximum-step cap is treated as an implementation detail.

The cap is part of the semantics.

## 17. Training and inference can disagree

Dynamic-depth mechanisms often use relaxations, penalties, or stochastic estimators during training.

Deployment may use hard thresholds.

A training objective may reward expected compute.

Hardware may care about tail latency.

A controller may learn under one maximum depth and be deployed under another.

Thus there are two distinct questions:

did the learning procedure optimize the intended depth policy?

does the deployed execution realize the intended compute behavior?

The first is an optimization question.

The second is a systems question.

A complete conditional-compute story requires both.

## 18. What recurrent, adaptive, equilibrium, and conditional depth share

These mechanisms look different.

Their common object is a computational path whose length or structure is no longer just the static count of named layers.

Recurrent depth asks how many times to reuse an operator.

Adaptive depth asks when to stop.

Equilibrium depth asks what state satisfies a terminal fixed-point condition and how to solve for it.

Conditional depth asks which transformations to execute.

All four make computation allocation explicit.

That is why they belong in one chapter.

## 19. What the next chapters may assume

ATLAS-CH-ADAPTDEPTH-001 — Adaptive Depth as Error Control may assume:

- depth as computational time;
- fixed versus adaptive stopping;
- the stopping variable tau;
- exact distinction between a stopping signal and true error;
- fixed-point/equilibrium semantics;
- resource-aware compute accounting.

Its task is to add numerical error estimation and adaptive-step logic.

ATLAS-CH-SPARSE-001 — Conditional Computation may assume:

- hard and relaxed gates;
- active execution sets;
- realized path cost;
- input-dependent effective depth;
- the distinction between small soft weights and actually skipped operations.

Its task is to extend this into sparse activation, token selection, routing, and hardware-aware conditional execution.

## 20. The boundary to remember

Depth is often drawn vertically.

The Atlas needs a second picture.

Imagine depth horizontally as a computational trajectory.

A representation enters at k=0.

Each transition changes it.

A fixed-depth system stops because the architecture says L.

An adaptive system stops because a rule says enough.

An equilibrium system stops because a solver says the fixed-point criterion is met.

A conditional system changes which transitions exist on the realized path.

This picture does not prove that neural computation is continuous time.

It does something more practical.

It turns depth from a static architectural count into a resource that can be allocated, reused, skipped, or terminated under explicit rules.

Once depth is treated that way, adaptive computation becomes a question of dynamics, numerics, and systems design rather than a synonym for "deeper network."

## References used in this chapter

The exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-DEPTH-001.yaml

The external mechanism basis includes Graves's Adaptive Computation Time, Universal Transformers, Deep Equilibrium Models, and SkipNet. The numerical and architectural interpretation is grounded in the audited Atlas Numerics and Architecture History prerequisites.
