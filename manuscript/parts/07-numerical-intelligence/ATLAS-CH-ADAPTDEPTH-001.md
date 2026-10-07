# Adaptive Depth as Error Control
<!-- ATLAS-CH-ADAPTDEPTH-001 -->

**Epistemic status:** audited numerical/adaptive-depth substrate + primary adaptive-computation sources + Atlas synthesis.  
**Specification:** manuscript/specifications/ATLAS-CH-ADAPTDEPTH-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-ADAPTDEPTH-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-ADAPTDEPTH-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-ADAPTDEPTH-001.yaml

Adaptive computation sounds like one idea.

It is not.

A numerical solver may adapt its step size because a local error estimate is too large.

A recurrent network may run more steps because a learned halting unit has not fired.

A residual model may spend more layers on one spatial position than another.

A system may terminate because it exhausted its budget even though its quality criterion was not met.

All of these change computation.

They do not carry the same semantics.

This chapter asks when adaptive depth deserves the stronger name **error control**.

The answer is deliberately strict:

> adaptive computation becomes error control only when the system names a target error, an estimator or certified relation to that error, a tolerance, and a controller whose stopping or step-size decision is justified by that relation.

Without those objects, the system may still be useful.

It is simply doing adaptive computation rather than certified error control.

## 1. The four control surfaces

The audited Depth chapter separated computational depth from physical time.

The audited Networks-as-Numerical-Schemes chapter separated residual updates from literal numerical discretizations.

This chapter combines those boundaries.

Four objects recur.

### Execution depth

How many transformations are actually executed?

\[
z_0\to z_1\to\cdots\to z_\tau.
\]

The stopping depth \(\tau\) may depend on the input.

### Numerical step size

For a declared reference evolution,

\[
x_{n+1}
=
\Psi_{h_n}(x_n),
\]

the parameter \(h_n\) controls the numerical mesh.

### Local error estimate

A numerical controller may construct

\[
\widehat e_n
\]

to estimate a declared local truncation/error quantity.

### Learned halting signal

A learned system may produce

\[
q_k
\]

and stop when \(q_k\) crosses a threshold.

The Atlas will not silently identify any pair of these objects.

## 2. What adaptive depth already gives us

Graves's Adaptive Computation Time provides a differentiable mechanism for learning how many recurrent computational steps to allocate before producing an output [@Graves2016ACT].

Figurnov et al. extend adaptive computation into residual vision systems where different spatial positions can receive different amounts of computation [@FigurnovEtAl2017].

These are important mechanisms.

They show that a network can learn to allocate compute nonuniformly.

They do not, by themselves, show that the learned halting signal estimates:

- truncation error;
- approximation error;
- task loss;
- probability of correctness;
- distance to a fixed point;
- distance to a target representation.

A learned stop signal can be useful without being an error estimate.

## 3. Numerical error control is more specific

Now consider a declared numerical problem.

Let

\[
x_{n+1}
=
\Psi_{h_n}(x_n).
\]

A numerical error controller needs more than a variable \(h_n\).

It needs a target quantity.

For example:

\[
e_n
=
\text{local one-step error in a declared norm}.
\]

Because the exact local error is usually unavailable, the solver constructs an estimator

\[
\widehat e_n.
\]

Then the controller compares it with a tolerance

\[
\tau_n.
\]

A basic accept/reject rule is

\[
\widehat e_n\le\tau_n.
\]

This is already much stronger than “run until a score is small.”

The score has declared semantics.

## 4. Embedded formulas

A common numerical pattern is to obtain two approximations from related stage evaluations.

Write

\[
x_{n+1}^{[p]}
\]

and

\[
x_{n+1}^{[p+1]}.
\]

Then a local estimator may use

\[
\widehat e_n
=
\left\|
x_{n+1}^{[p+1]}
-
x_{n+1}^{[p]}
\right\|.
\]

Dormand and Prince develop a family of embedded Runge-Kutta formulas with different orders [@DormandPrince1980].

The important structural point for this chapter is not the exact Dormand-Prince coefficient table.

It is the control pattern:

- two approximations;
- one step;
- one difference;
- one local error estimate;
- one decision about accepting or shrinking the step.

This pattern gives the phrase “error-controlled adaptation” real mathematical content.

## 5. Estimator is not oracle

Even in numerical analysis, an embedded difference is not magic.

Its interpretation depends on:

- the declared differential equation;
- the method;
- smoothness;
- order conditions;
- the norm;
- the local asymptotic regime.

The safe statement is:

\[
\text{embedded difference}
\to
\text{method-specific local error estimator}.
\]

The unsafe statement is:

\[
\text{embedded difference}
=
\text{exact total error}
\]

for every problem.

The finite witness below is chosen precisely because the equality happens to be exact there.

## 6. A one-step exact witness

Consider

\[
y'(t)=t,
\qquad
y(0)=0.
\]

The exact solution is

\[
y(t)=\frac{t^2}{2}.
\]

Take one step from \(t=0\) to \(t=h\).

Euler gives

\[
y_E=0.
\]

Why?

Because

\[
f(0,0)=0.
\]

Now use the explicit trapezoid / Heun update.

Its first slope is

\[
k_1=0.
\]

The Euler predictor is still zero.

The second slope is

\[
k_2=f(h,0)=h.
\]

Therefore

\[
y_H
=
\frac h2(k_1+k_2)
=
\frac{h^2}{2}.
\]

But the exact solution at \(h\) is also

\[
y(h)=\frac{h^2}{2}.
\]

Thus, for this witness,

\[
y_H=y(h).
\]

The pair difference is

\[
|y_H-y_E|
=
\frac{h^2}{2}.
\]

And that equals the exact Euler one-step error.

This is unusually clean.

It lets us examine the controller without hiding behind asymptotic notation.

## 7. Rejecting a step

Set the tolerance to

\[
\tau=\frac18.
\]

Try

\[
h=1.
\]

The estimated error is

\[
\widehat e
=
\frac12.
\]

Therefore

\[
\widehat e>\tau.
\]

The step is rejected.

Notice what was declared:

- target: Euler one-step error in absolute value;
- estimator: Euler/Heun difference;
- tolerance: \(1/8\);
- decision: reject if estimator exceeds tolerance.

That is an error-control interface.

## 8. Shrinking the step

For a low-order method of order \(p\), local truncation error scales like

\[
C h^{p+1}
\]

in the asymptotic regime.

An idealized controller can use

\[
h_{\mathrm{new}}
=
h
\left(
\frac{\tau}{\widehat e}
\right)^{1/(p+1)}.
\]

For Euler,

\[
p=1.
\]

Using

\[
h=1,
\qquad
\tau=\frac18,
\qquad
\widehat e=\frac12,
\]

we obtain

\[
h_{\mathrm{new}}
=
\sqrt{
\frac{1/8}{1/2}
}
=
\frac12.
\]

Retry at \(h=1/2\).

Then

\[
\widehat e
=
\frac{(1/2)^2}{2}
=
\frac18.
\]

The retry lands exactly on tolerance.

Practical controllers use safety factors and clamps.

The witness omits them because the point is the semantics, not production solver tuning.

## 9. Error control is a feedback loop

The controller has the form

\[
\text{estimate}
\to
\text{compare}
\to
\text{accept/reject}
\to
\text{change future computation}.
\]

This is why adaptive numerical integration is conceptually useful for adaptive neural computation.

Both are feedback systems.

But analogy is not identity.

The crucial difference is what the feedback signal means.

## 10. A learned halting signal

A learned computation may evolve

\[
z_{k+1}
=
F_k(z_k)
\]

and emit a score

\[
q_k.
\]

Given threshold \(\delta\) and budget cap \(K_{\max}\),

\[
\tau
=
\min
\left(
\{k\le K_{\max}:q_k\le\delta\}
\cup
\{K_{\max}\}
\right).
\]

This is a perfectly valid stopping rule.

It says nothing yet about whether

\[
q_k
\]

is:

- a probability;
- a task-loss estimate;
- a residual;
- a confidence score;
- a distance to convergence;
- a numerical local-error estimate.

The semantics must come from somewhere else.

## 11. Learned stopping is not numerical stopping

Graves ACT uses learned halting to allocate recurrent computation [@Graves2016ACT].

Its mechanism is not “estimate a Runge-Kutta truncation error and reduce the step.”

Figurnov et al. allocate computation spatially in residual networks [@FigurnovEtAl2017].

Their mechanism is not “refine a finite-element mesh where a PDE residual is large.”

These systems can inspire numerical analogies.

The Atlas preserves the direction of implication:

\[
\text{adaptive computation}
\Rightarrow
\text{variable compute allocation}.
\]

It does not infer:

\[
\text{adaptive computation}
\Rightarrow
\text{numerical error control}.
\]

## 12. Perfect ranking is still not calibration

A common temptation is weaker.

Suppose the learned halting score tracks difficulty very well.

Perhaps smaller score always means smaller true error.

Is that enough?

No.

Consider the audited contraction from the Depth chapter:

\[
x_{k+1}
=
\frac{x_k+2}{2},
\qquad
x_0=0.
\]

The fixed point is 2.

Its exact error is

\[
E_k
=
|x_k-2|
=
2^{1-k}.
\]

Now define

\[
q_k=4^{-k}.
\]

Then

\[
q_k=\frac{E_k^2}{4}.
\]

The score is a strictly monotone function of the true error.

It ranks every depth perfectly.

But it is not on the same scale.

## 13. An exact premature-halting witness

At depth

\[
k=2,
\]

the score is

\[
q_2=\frac1{16}.
\]

The true error is

\[
E_2=\frac12.
\]

Suppose we want true error at most

\[
\frac1{16}.
\]

If we mistakenly use the same numerical threshold on the learned score,

\[
q_k\le\frac1{16},
\]

the system stops at \(k=2\).

But

\[
E_2=\frac12
\]

is eight times the requested tolerance.

This failure is not due to poor ranking.

The ranking is perfect.

The failure is magnitude calibration.

## 14. The missing map

In the witness, the relation is exactly

\[
E_k
=
2\sqrt{q_k}.
\]

Once that map is known, the halting score can support correct thresholding.

For target error

\[
\varepsilon,
\]

we require

\[
2\sqrt{q_k}
\le
\varepsilon.
\]

So the correct score threshold is

\[
q_k
\le
\left(
\frac{\varepsilon}{2}
\right)^2.
\]

For

\[
\varepsilon=\frac1{16},
\]

this becomes

\[
q_k\le\frac1{1024}.
\]

The first matching depth is

\[
k=5,
\]

where

\[
E_5=\frac1{16}.
\]

The score has become an error-control signal only because the relation to target error is declared.

## 15. Rank quality versus magnitude semantics

This distinction appears throughout machine learning.

A score can be excellent at:

- ranking examples by difficulty;
- ranking candidate states by quality;
- separating easy from hard inputs;
- predicting which examples deserve more compute.

Those are useful capabilities.

They do not automatically answer:

> What threshold guarantees error below epsilon?

That question requires magnitude semantics.

The Atlas therefore distinguishes:

\[
\text{ranking}
\]

from

\[
\text{calibration}
\]

from

\[
\text{certified upper bound}.
\]

## 16. Expected calibration may still be too weak

Suppose a learned halting score satisfies

\[
E[E_k\mid q_k=s]
=
g(s).
\]

That is a meaningful probabilistic calibration statement.

It does not imply

\[
E_k\le g(s)
\]

for every individual example.

If the controller requires a hard error guarantee, an expectation is not enough.

The appropriate object might instead be:

- a high-probability bound;
- a conformal upper bound;
- a deterministic residual bound;
- a certified interval;
- a worst-case estimate.

The right guarantee depends on the application.

## 17. Local error is not global error

Numerical error control has its own version of this warning.

Suppose every accepted step satisfies

\[
\widehat e_n\le\tau_n.
\]

Does that immediately prove the final trajectory is within a desired global error?

No.

Global error depends on:

- accumulation;
- stability;
- amplification;
- the mesh sequence;
- the problem dynamics;
- method order;
- regularity.

The NETNUM prerequisite already separated local and global error.

ADAPTDEPTH inherits that boundary intact.

## 18. More depth is not always refinement

Suppose a network runs twice as many layers.

That does not automatically mean the numerical step size was halved.

For a numerical refinement statement, we need a fixed reference problem.

For example, if a horizon

\[
T
\]

is represented by steps

\[
h_0,\ldots,h_{N-1},
\]

then a fixed-horizon mesh satisfies

\[
\sum_{n=0}^{N-1}h_n=T.
\]

Increasing \(N\) can represent a finer mesh only if the \(h_n\) values are changed accordingly.

If the network simply appends more transformations, it may be extending computational time rather than refining the same interval.

This is exactly why Depth and NETNUM are both hard prerequisites.

## 19. Adaptive depth versus adaptive step size

The distinction can be written compactly.

### Adaptive execution depth

\[
z_{k+1}=F_k(z_k),
\qquad
k<\tau(x).
\]

The input chooses how many stages execute.

### Adaptive time stepping

\[
x_{n+1}=\Psi_{h_n}(x_n),
\]

where an error controller changes

\[
h_n
\]

for a declared reference evolution.

The first changes stage count.

The second changes a numerical mesh.

A system can combine them.

It must declare that combination explicitly.

## 20. A learned error estimator

There is a legitimate bridge between the two worlds.

Suppose a learned module predicts

\[
\widehat e_\theta(z_k)
\]

and training data provides a target numerical or task error.

Now the learned score is intended to estimate an error.

But intention is still not guarantee.

We should ask:

- what is the training target?
- what norm?
- what distribution?
- what calibration?
- what tail behavior?
- what happens out of distribution?
- is the estimate biased?
- is an upper bound needed?
- what does rejection do?

The bridge becomes mathematically meaningful only after these questions are answered.

## 21. Error control as an interface contract

A complete adaptive error-control interface should declare:

### State

What state is being advanced?

\[
x_n
\quad\text{or}\quad
z_k.
\]

### Target error

What quantity should be small?

\[
E_n.
\]

### Estimator

What is actually observed?

\[
\widehat e_n.
\]

### Relation

Why does the estimator say anything about the target error?

Examples:

\[
E_n
\le
B(\widehat e_n),
\]

or

\[
P(E_n\le B(\widehat e_n))
\ge
1-\alpha.
\]

### Tolerance

What target is requested?

\[
\varepsilon.
\]

### Controller

What action follows?

- stop;
- continue;
- shrink step;
- grow step;
- route elsewhere;
- spend more compute.

### Budget

What happens if the criterion never passes?

This interface is the central durable object of the chapter.

## 22. Budget exhaustion remains a separate state

Suppose a system has maximum depth

\[
K_{\max}.
\]

If the error or halting criterion is not met before that cap, the output may still be returned.

But the termination reason is

\[
\text{budget\_exhausted}.
\]

It is not

\[
\text{criterion\_met}.
\]

This distinction was repaired explicitly in AUDIT-018.

ADAPTDEPTH preserves it.

The same rule applies to numerical solvers.

A solver that runs out of permitted work has not thereby satisfied tolerance.

## 23. Error control is not compute optimality

A step-size controller may meet an accuracy target while using more function evaluations than another method.

A halting policy may reduce FLOPs while increasing error.

A routing scheme may lower average cost while worsening tail latency.

Therefore two objectives remain separate:

\[
\text{error control}
\]

and

\[
\text{resource optimization}.
\]

They can be combined through a joint objective.

They should not be conflated.

## 24. Spatially adaptive computation

Figurnov et al. show a system in which different image regions receive different computation [@FigurnovEtAl2017].

This is a useful reminder that adaptive depth need not be scalar.

We might write a local depth field

\[
\tau(i,j).
\]

That looks superficially like adaptive mesh refinement.

The resemblance is interesting.

It is not yet a PDE statement.

Adaptive mesh refinement requires:

- a spatial discretization;
- a reference PDE or operator;
- an error indicator/estimator;
- refinement/coarsening semantics;
- consistency across interfaces.

A spatial halting mask supplies none of these automatically.

## 25. Neural error indicators

A useful research direction is to learn an error indicator rather than merely a halting probability.

For example, a model might predict:

\[
\widehat e_k
=
g_\theta(z_k,z_{k+1},r_k).
\]

The controller could then continue while

\[
\widehat e_k>\varepsilon.
\]

But the Atlas would still ask what supports the implication:

\[
\widehat e_k\le\varepsilon
\Rightarrow
E_k\le\varepsilon.
\]

Possible answers include:

- exact residual theory;
- calibration on a declared distribution;
- conformal upper bounds;
- interval propagation;
- theorem-backed a posteriori estimates.

The learned component does not erase the proof obligation.

## 26. Residuals are promising but not universal

Numerical methods often use residuals or embedded differences because they have a known mathematical relation to error.

Neural systems also expose residual-like objects:

- state increments;
- reconstruction residuals;
- fixed-point residuals;
- gradient norms;
- disagreement scores.

These can be useful stopping signals.

But the relation

\[
\text{small residual}
\Rightarrow
\text{small target error}
\]

is problem dependent.

For an ill-conditioned or non-normal system, a small residual may coexist with a larger solution error.

The error-control interface therefore requires the relation, not just the residual.

## 27. Fixed-point stopping

Suppose an equilibrium computation seeks

\[
z^*=F(z^*).
\]

A natural residual is

\[
r_k
=
\|F(z_k)-z_k\|.
\]

Stopping when

\[
r_k\le\varepsilon
\]

is a residual criterion.

To convert it into a state-error guarantee

\[
\|z_k-z^*\|\le C\varepsilon,
\]

we need additional structure.

For a contraction with factor \(L<1\), such relations can be derived.

Without them, the residual is not the state error.

This is another instance of the same principle.

## 28. Halting as decision making

A learned halting rule can also be viewed as a decision problem.

At depth \(k\), the system chooses between:

- stop now;
- spend another unit of compute.

The decision trades expected improvement against compute cost.

That is a valid formulation.

It is not numerical error control unless the objective or constraint explicitly references an error quantity with justified semantics.

The Atlas therefore allows adaptive depth to be interpreted in several ways without collapsing them.

## 29. A hierarchy of stopping semantics

From weakest to strongest:

### Heuristic stop score

A learned or handcrafted number triggers stopping.

### Empirically predictive score

The score correlates with future improvement or error on held-out data.

### Calibrated expected error

The score predicts average error under a declared distribution.

### High-probability error control

The score yields a probabilistic upper bound with stated coverage.

### Deterministic certified error bound

The score or residual implies a mathematical upper bound under declared assumptions.

These levels should not be described with the same language.

## 30. Why embedded pairs matter conceptually

Embedded numerical formulas are useful beyond ODE software.

They illustrate a design pattern for adaptive intelligence:

> create two computations whose discrepancy carries information about whether more computation is warranted.

The pattern might reappear as:

- shallow versus deep prediction disagreement;
- coarse versus refined representation;
- low-rank versus expanded solve;
- cheap versus expensive model;
- one-step versus multi-step estimate.

But the discrepancy becomes error control only when its relation to target error is justified.

The numerical example teaches the grammar.

It does not certify every neural analogue.

## 31. Error estimators can fail outside their regime

Numerical estimators themselves have domains of validity.

A step controller can struggle when:

- the problem is stiff;
- smoothness assumptions fail;
- the step is outside the asymptotic regime;
- the estimator suffers cancellation;
- the chosen norm misses a relevant component.

This matters for neural analogies.

Even a mathematically motivated error signal has to be checked against the regime where its guarantee was derived.

## 32. Adaptive computation and distribution shift

A learned halting model may be calibrated on one input distribution.

Deployment may shift.

Then the relation between score and error can change.

This parallels the Uncertainty chapter's warning:

\[
P\text{-calibration}
\not\Rightarrow
Q\text{-calibration}.
\]

ADAPTDEPTH therefore treats learned error control as distribution-relative unless a stronger robust guarantee is established.

## 33. Acceptance and rejection should be explicit

A controller is incomplete if it only says “adapt.”

For each proposed computation, one should know:

- what was measured;
- whether the criterion passed;
- whether the state was accepted;
- what changed after rejection;
- whether computation was retried;
- whether the budget was consumed;
- whether the final output met tolerance.

This transaction-like view aligns numerical adaptation with the Atlas's broader emphasis on explicit state and evidence.

## 34. A minimal controller grammar

A generic adaptive controller can be written:

1. propose an update;
2. compute an indicator;
3. map indicator to target error semantics;
4. compare against tolerance;
5. accept or reject;
6. change compute allocation;
7. stop on criterion or budget;
8. record the termination reason.

This grammar covers:

- numerical step-size control;
- recurrent halting;
- iterative solver stopping;
- conditional depth;
- learned refinement.

The semantics differ at step 3.

That is where the important mathematics lives.

## 35. Failure modes

The recurring category errors are now concrete.

### Halting score as error

A learned number is thresholded and then described as tolerance satisfaction without calibration.

### Rank as magnitude

A score orders easy and hard cases correctly, so its numerical value is treated as an error bound.

### Local as global

A local estimator is small, so final accumulated error is claimed small without stability analysis.

### Depth as mesh

More layers are described as finer time discretization without a fixed horizon and step-scale relation.

### Budget as convergence

The system stops at \(K_{\max}\) and the output is labeled converged.

### Spatial depth as adaptive mesh refinement

A learned spatial computation mask is described with PDE refinement language without a declared discretized PDE.

### Error control as optimal compute

Meeting tolerance is confused with using the minimum possible resources.

## 36. Research programme

The synthesis suggests several precise research targets.

### Learned a posteriori estimators

Train a model to estimate a mathematically defined error and then test calibration and bounds.

### Two-resolution neural computation

Construct cheap/high-resolution pairs whose discrepancy predicts the value of more computation.

### Conformal stopping

Use distribution-free calibration machinery to turn empirical error predictors into high-probability stopping rules under exchangeability assumptions.

### Robust halting under shift

Test whether error/halting calibration survives changed data laws.

### Resource-aware error control

Optimize compute subject to a declared error constraint instead of mixing accuracy and cost in one opaque score.

Each target requires its own proof or evidence layer.

## 37. Closing view

Adaptive depth is most mathematically useful when it is treated as a control problem rather than a slogan.

The system evolves a state.

It observes an indicator.

The indicator has declared semantics.

A controller compares that indicator with a target.

The system spends more or less computation accordingly.

The durable synthesis is:

\[
\boxed{
\text{adaptive error control}
=
\text{adaptive computation}
+
\text{target error}
+
\text{estimator/error relation}
+
\text{tolerance}
+
\text{controller}
+
\text{budget state}.
}
\]

Remove the estimator/error relation and we still have adaptive computation.

We no longer have justified error control.

## References used in this chapter

- Graves, Adaptive Computation Time for Recurrent Neural Networks [@Graves2016ACT].
- Figurnov et al., Spatially Adaptive Computation Time for Residual Networks [@FigurnovEtAl2017].
- Dormand and Prince, A family of embedded Runge-Kutta formulae [@DormandPrince1980].

Exact provenance and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-ADAPTDEPTH-001.yaml
