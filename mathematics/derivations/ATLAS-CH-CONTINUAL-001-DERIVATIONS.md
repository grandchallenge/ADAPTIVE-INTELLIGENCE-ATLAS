# ATLAS-CH-CONTINUAL-001 — Formal and Derivation Packet

## 1. Purpose

This packet formalizes sequential interference and separates four anti-forgetting mechanisms:

- replay through remembered data;
- consolidation through parameter-space penalties;
- gradient constraints induced by episodic memory;
- parameter isolation through capacity partitioning.

The exact witness uses two conflicting quadratic tasks in one shared scalar parameter.

## 2. Sequential performance matrix

Let contexts arrive in order

`1,2,...,T`.

After training through context `i`, the mandatory retention evaluation covers each encountered context `j<=i`.

Let

`R_{i,j}`

be the declared score. These encountered-context entries form the lower triangle used for forgetting. If the protocol also evaluates not-yet-trained contexts `j>i`, those entries may complete a full performance matrix for forward-transfer analysis. Such a forward-transfer claim also requires a declared untrained/reference baseline for the future context.

The performance record contains more information than a single final average.

For a sequence with `T>=2`, and for earlier context `j<T`, define

`B_j=max_{k=j,...,T-1} R_{k,j}`.

Define nonnegative endpoint forgetting

`F_j=max(0,B_j-R_{T,j})`.

Then

`F_avg=(1/(T-1)) sum_{j=1}^{T-1} F_j`

and

`F_max=max_{j<T} F_j`.

These are Atlas summaries over a declared score matrix. Cross-context aggregation is meaningful only when scores share a commensurate scale or a declared normalization; otherwise the per-context values should remain separate.

They intentionally do not erase the signed history when positive backward transfer matters. Forward transfer is a separate quantity and cannot be reconstructed from the lower-triangular retention entries alone.

## 3. Performance change is not parameter change

Let a model have parameters `theta`.

A sequential update may produce large parameter motion with negligible old-task performance change if the old task is insensitive along that direction.

Conversely, a small parameter move can cause large old-task performance loss along a sensitive direction.

Therefore:

`||theta_new-theta_old||`

is not a forgetting metric by itself.

Forgetting is defined through retained behavior under an evaluation contract.

## 4. Catastrophic interference boundary

McCloskey and Cohen document severe sequential interference in connectionist networks.

The Atlas uses **forgetting** as the broad performance-loss term.

It uses **catastrophic forgetting/interference** only when the degradation is severe under the declared protocol or when reporting a source's own terminology.

This avoids turning every small negative transfer event into a catastrophic claim.

## 5. Task, domain, and class incremental settings

The van de Ven–Tuytelaars–Tolias distinction matters because the evaluator exposes different information.

Task-incremental:

- context/task identity is available at evaluation;
- task-specific components can be selected.

Domain-incremental:

- the input distribution/context changes;
- the required output semantics remain shared;
- explicit context identity need not be available.

Class-incremental:

- the learner must discriminate over an expanding global class set;
- examples from different learning episodes must ultimately coexist in one prediction problem.

Performance numbers from these settings should not be compared as if the test-time information contract were identical.

## 6. Replay as objective reconstruction

Let current-context empirical loss be

`L_cur(theta)`.

Let a memory buffer contain remembered samples `M` from earlier contexts.

A simple replay objective is

`L_replay(theta)
=
L_cur(theta)
+
alpha L_M(theta)`.

The key mechanism is direct:

earlier evidence re-enters the training objective.

The memory may contain exact examples, transitions, exemplars, or generated substitutes.

Replay is a **use of memory**.

Its storage locus, lifetime, provenance, and addressability remain separate MEMTAX coordinates.

## 7. Replay is not exact retention

Even if earlier examples are replayed, exact retention need not follow.

Reasons include:

- memory is only a subset of earlier data;
- optimization is approximate;
- weighting may favor the new context;
- representation changes can affect unremembered examples;
- the model may lack capacity to fit all contexts simultaneously.

Replay therefore changes the evidence available to optimization.

It does not by itself prove zero forgetting.

## 8. EWC as local parameter consolidation

After learning task A, let

`theta_A^*`

be the chosen parameter point.

Kirkpatrick et al. approximate the earlier-task posterior locally and use diagonal Fisher information to weight parameter importance.

The EWC objective for new task B has the form

`L_EWC(theta)
=
L_B(theta)
+
(lambda/2)
sum_i
F_i
(theta_i-theta^*_{A,i})^2`.

The quadratic term resists movement in coordinates estimated to matter for the earlier task.

This is a soft constraint.

It is not an exact projection onto the set of parameters preserving old-task behavior.

## 9. Why Fisher weighting matters

A uniform penalty

`||theta-theta_A^*||^2`

treats every parameter direction equally.

EWC instead uses coordinate weights `F_i`.

The intended logic is:

- high estimated importance -> high cost for motion;
- low estimated importance -> more plasticity.

The source itself describes the diagonal Fisher as a tractable approximation.

The Atlas therefore treats EWC as an approximate consolidation mechanism, not as a theorem that Fisher-diagonal importance exactly equals behavioral necessity.

## 10. Exact conflicting-task witness

Use one scalar parameter `w`.

Task A loss:

`L_A(w)=(1/2)(w+1)^2`.

Task B loss:

`L_B(w)=(1/2)(w-1)^2`.

The unique optima are

`w_A^*=-1`

and

`w_B^*=1`.

No single scalar value makes both losses zero.

Thus the one-parameter model has an exact capacity conflict.

## 11. Sequential learning without protection

After Task A:

`w=-1`.

Then

`L_A(-1)=0`.

Train Task B to its optimum:

`w=1`.

Then

`L_B(1)=0`

but

`L_A(1)
=
(1/2)(2)^2
=
2`.

The exact old-task loss increase is therefore

`2`.

This is a deterministic interference witness.

It is not a claim about the typical magnitude of forgetting in deep networks.

## 12. EWC-like penalty in the witness

Set scalar importance

`F=1`.

Use

`J_lambda(w)
=
L_B(w)
+
(lambda/2)(w+1)^2`.

Since

`L_A(w)=(1/2)(w+1)^2`,

the toy objective is also

`J_lambda=L_B+lambda L_A`.

Differentiate:

`dJ_lambda/dw
=
(w-1)+lambda(w+1)`.

Set to zero:

`(1+lambda)w+(lambda-1)=0`.

Hence

`w_lambda=(1-lambda)/(1+lambda)`

for `lambda>=0`.

## 13. Exact retained and current losses

Compute

`w_lambda+1
=
2/(1+lambda)`.

Therefore

`L_A(w_lambda)
=
(1/2)[2/(1+lambda)]^2
=
2/(1+lambda)^2`.

Also

`w_lambda-1
=
-2lambda/(1+lambda)`.

Therefore

`L_B(w_lambda)
=
(1/2)[2lambda/(1+lambda)]^2
=
2lambda^2/(1+lambda)^2`.

At `lambda=0`:

- `w=1`;
- `L_A=2`;
- `L_B=0`.

At `lambda=1`:

- `w=0`;
- `L_A=1/2`;
- `L_B=1/2`.

As `lambda -> infinity`:

- `w_lambda -> -1`;
- `L_A -> 0`;
- `L_B -> 2`.

The witness makes the retention/adaptation tradeoff exact.

## 14. Replay coincidence in the quadratic toy

Suppose exact replay gives equal weight to the full Task A and Task B objectives:

`L_joint(w)=L_A(w)+L_B(w)`.

Then

`L_joint(w)
=
(1/2)(w+1)^2+(1/2)(w-1)^2
=
w^2+1`.

Its unique minimizer is

`w=0`.

This is the same point as the `lambda=1,F=1` EWC-like objective.

That equality is deliberately constructed.

It occurs because the old task loss itself is exactly the same quadratic used as the retention penalty.

In general:

- replay evaluates remembered data under the current model;
- EWC replaces old-task influence with a local parameter-space quadratic approximation.

They are not the same algorithm.

## 15. Parameter isolation in the toy

Now allow two task-selected scalar parameters:

`w_A`

and

`w_B`.

Let Task A use only `w_A` and Task B only `w_B`.

Choose

`w_A=-1`,
`w_B=1`.

Then both losses are zero.

This removes direct overwrite because the tasks no longer compete for the same scalar.

But the mechanism has changed the resource budget.

It requires:

- two parameters rather than one;
- a rule selecting the correct parameter at evaluation.

The witness therefore models a task-incremental style routing advantage.

It does not solve class-incremental prediction when task identity is unavailable.

## 16. GEM-style gradient constraints

Let `g` be the current-task gradient.

Let `g_j` be the gradient of remembered loss for earlier context `j`.

For a proposed update

`theta' = theta - eta * g_tilde`,

the first-order change in remembered loss is

`L_j(theta')-L_j(theta)
approximately
-eta g_j^T g_tilde`.

A sufficient first-order condition for non-increase is therefore

`g_j^T g_tilde >= 0`.

GEM projects the current gradient into a region satisfying constraints induced by episodic memory.

This is different from unconstrained replay and different from EWC's parameter-space spring.

The guarantee is local/first-order with respect to the remembered losses used to construct the constraints; finite-step and out-of-memory behavior require additional analysis.

## 17. Mechanism comparison

Replay changes the data/evidence in the current objective.

EWC changes the parameter geometry of the current objective through an importance-weighted penalty.

GEM changes the allowable update direction using remembered-task gradients.

Parameter isolation changes which parameters later tasks are permitted to overwrite.

These mechanisms can be combined.

They should not be collapsed into one category merely because all aim to reduce interference.

## 18. Capacity is part of the accounting

A method can reduce forgetting by consuming more resources.

Examples include:

- storing exemplars;
- storing generators;
- storing Fisher/importance values;
- keeping task-specific masks;
- reserving new parameters;
- retaining separate heads.

A fair continual-learning comparison should therefore report the relevant memory and capacity budget together with predictive performance.

## 19. Average retention can hide a failed task

Suppose two earlier contexts have forgetting values

`F_1=0`

and

`F_2=1`.

Then

`F_avg=1/2`

while

`F_max=1`.

A method with the same average can distribute damage differently.

Therefore average forgetting and worst-context forgetting answer different questions.

The performance matrix should remain recoverable behind scalar summaries.

## 20. Forward and backward transfer

Sequential learning can improve earlier or later learning.

A signed change in an earlier-task score after later training may be positive.

Clipping forgetting to a nonnegative quantity deliberately hides that improvement.

Therefore a transfer analysis should retain signed score changes or use a dedicated transfer metric in addition to nonnegative forgetting summaries.

Lopez-Paz and Ranzato explicitly emphasize transfer metrics alongside final accuracy.

## 21. Consolidation is not semantic memory by definition

MEMTAX allows a semantic-consolidation role.

EWC is called a consolidation method because it protects parameterized knowledge through weighted resistance to change.

That does not imply that the resulting parameters are a clean semantic database.

Likewise, replaying episodic records can support semantic generalization without changing the records' memory role.

Mechanism and memory role remain distinct.

## 22. Downstream interface

EXTMEM-001 may consume:

- replay as a use of stored records;
- the distinction between storing evidence and protecting parameters;
- capacity/memory overhead as part of the comparison;
- the exact failure of one shared scalar to satisfy conflicting tasks;
- the fact that task-specific parameter isolation can eliminate direct overwrite only by changing capacity/routing assumptions.

It must independently argue when external persistent/shared memory is preferable to parametric retention.
