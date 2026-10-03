# Continual Learning and Forgetting
<!-- ATLAS-CH-CONTINUAL-001 -->

**Epistemic status:** established continual-learning mechanisms + audited memory/optimization prerequisites + Atlas synthesis + exact scalar witness.  
**Specification:** manuscript/specifications/ATLAS-CH-CONTINUAL-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-CONTINUAL-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-CONTINUAL-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-CONTINUAL-001.yaml

A learner can become better at what it sees now and worse at what it knew before.

That sentence contains the central difficulty of continual learning.

Ordinary optimization asks how to improve an objective.

Continual learning asks what happens when the objective, data distribution, label space, task context, or available evidence changes over time while the same learning system must preserve useful earlier capability.

The problem is not simply that parameters move.

Parameters are supposed to move.

The problem is that later updates can alter earlier behavior in ways the learner no longer has enough evidence, capacity, or structural protection to repair.

This chapter develops continual learning as a problem of **controlled interference under sequential updates**.

Its central rule is:

> forgetting is a behavioral statement under an evaluation protocol, not a synonym for parameter change.

That rule keeps the discussion grounded.

## 1. Sequential learning creates a history

Suppose contexts arrive in order

`1,2,...,T`.

After training through context `i`, evaluate the current model on every context seen so far.

Write

`R_{i,j}`

for the score on context `j` after training through context `i`.

Then the basic object is not one number.

It is a lower-triangular performance-through-time matrix.

For three contexts it has the form

`R_{1,1}`

`R_{2,1}, R_{2,2}`

`R_{3,1}, R_{3,2}, R_{3,3}`.

This matrix can reveal things a final average hides.

A later task may damage one earlier task and improve another.

A model may preserve average accuracy while destroying a rare context.

A method may learn new tasks slowly but retain old ones almost perfectly.

Another may adapt rapidly and forget sharply.

All of those behaviors can collapse to similar final averages.

So continual learning should begin from the trajectory of performance, not only its endpoint.

## 2. An Atlas forgetting summary

For a sequence with `T>=2`, and for an earlier context `j<T`, define its best prior score

`B_j=max_{k=j,...,T-1} R_{k,j}`.

Define endpoint forgetting

`F_j=max(0,B_j-R_{T,j})`.

Then define

`F_avg=(1/(T-1)) sum_{j<T} F_j`

and

`F_max=max_{j<T} F_j`.

These are Atlas summaries.

They are intentionally modest.

Cross-context aggregation is meaningful only when the context scores share a commensurate scale or a declared normalization. If different contexts use incomparable metrics or ranges, retain the per-context values instead of averaging or taking a cross-context maximum.

They do not claim to be the one canonical continual-learning metric.

Lopez-Paz and Ranzato emphasize that continual-learning evaluation should include transfer behavior, not only final task accuracy [@LopezPazRanzato2017GEM].

That matters because the nonnegative `F_j` definition deliberately clips improvement.

If later learning improves an earlier task, the signed change should remain available elsewhere in the evaluation record.

## 3. Parameter movement is not forgetting

Suppose a model moves from parameters

`theta_old`

to

`theta_new`.

The norm

`||theta_new-theta_old||`

does not tell us how much was forgotten.

A large movement may occur along directions that barely matter for an earlier task.

A small movement may cross a sensitive decision boundary and cause a large behavioral change.

Forgetting is therefore evaluated through retained performance, loss, calibration, reward, or another declared behavioral quantity.

Parameter-space movement becomes meaningful only after it is connected to that behavior.

This distinction is crucial for understanding consolidation methods.

They act in parameter space.

Their purpose is behavioral retention.

The two levels are related but not identical.

## 4. Why the word catastrophic exists

McCloskey and Cohen studied what they called catastrophic interference in connectionist networks under sequential learning [@McCloskeyCohen1989].

The important phenomenon is not merely that an old score decreases.

It is that new learning can produce severe loss of earlier capability when the same distributed parameters are reused.

Modern deep-learning literature often uses **catastrophic forgetting** for the same broad family of failures.

The Atlas uses the word carefully.

A small noisy decline is not automatically catastrophic.

A report should state:

- what was learned first;
- what was learned later;
- how old performance changed;
- over what training interval;
- under what evaluation protocol.

Severity belongs in the evidence.

It should not be smuggled in by the adjective.

## 5. Continual learning is not one benchmark regime

A major source of confusion is that different continual-learning experiments provide different information to the learner at evaluation.

Van de Ven, Tuytelaars, and Tolias distinguish task-incremental, domain-incremental, and class-incremental scenarios [@VanDeVenTuytelaarsTolias2022].

### Task-incremental learning

The system knows, or can unambiguously determine, which task is being evaluated.

Task-specific heads, masks, or modules can therefore be selected.

### Domain-incremental learning

The input distribution or context changes, but the output semantics remain shared.

Explicit task identity need not be supplied at test time.

### Class-incremental learning

The output problem grows.

The model must discriminate across a global set of classes accumulated over time.

These regimes differ materially.

A method that relies on a task selector has an easier inference contract than one that must infer among all accumulated classes.

So a continual-learning result should always say what context information is available.

## 6. Memory enters continual learning in different roles

The Memory Taxonomy chapter established that memory should be described by locus, write path, read path, lifetime, addressability, mutability, provenance, and sharing.

That discipline prevents an immediate mistake.

**Replay is not a memory type.**

Replay is a use of remembered information during learning.

The remembered material might live in:

- a local buffer;
- an external store;
- a generated model;
- a compressed exemplar set;
- another durable or ephemeral locus.

The continual-learning mechanism is the reintroduction of earlier evidence.

The memory architecture is a separate design decision.

## 7. Replay: put old evidence back into the objective

Let

`L_cur(theta)`

be the current-context loss.

Let a memory `M` support an earlier-data loss

`L_M(theta)`.

A simple replay objective is

`L_replay(theta)
=
L_cur(theta)
+
alpha L_M(theta)`.

The logic is direct.

If later optimization sees only the new context, it may move into a region that is excellent for the new objective and poor for the old one.

Replay makes earlier evidence visible again.

Rebuffi et al.'s iCaRL uses a bounded exemplar set in a class-incremental learning system [@RebuffiEtAl2017iCaRL].

Gradient Episodic Memory also retains episodic examples, although it uses them differently [@LopezPazRanzato2017GEM].

Replay is powerful because it attacks one root cause of forgetting:

the optimizer otherwise cannot optimize against evidence it no longer sees.

## 8. Replay does not guarantee retention

Reintroducing old evidence is not the same as freezing old capability.

A replay buffer may be incomplete.

Its sampling distribution may be distorted.

Its weight in the loss may be too small.

Optimization may stop early.

The model may lack enough capacity to satisfy old and new objectives simultaneously.

The remembered examples may not represent the full earlier distribution.

Therefore replay changes the optimization problem in a retention-friendly direction.

It does not create an automatic theorem of zero forgetting.

## 9. Consolidation: preserve important parameter directions

A different strategy is to remember not the old examples themselves but information about which parameters were important for the old task.

Elastic Weight Consolidation is a canonical example.

After learning task A, let

`theta_A^*`

be the selected parameter point.

When learning B, EWC uses

`L_EWC(theta)
=
L_B(theta)
+
(lambda/2)
sum_i
F_i
(theta_i-theta_{A,i}^*)^2`.

Kirkpatrick et al. motivate the weights `F_i` through a diagonal Fisher-information approximation to parameter importance [@KirkpatrickEtAl2017EWC].

The geometry is intuitive.

Moving a parameter with large `F_i` is expensive.

Moving one with small `F_i` is cheaper.

The old solution behaves like an anisotropic spring anchor.

## 10. EWC is an approximation, not an oracle

The EWC penalty is useful precisely because storing and replaying all old data may be impossible or undesirable.

But compression has a price.

The old task is represented through:

- an anchor point;
- a local quadratic approximation;
- diagonal importance estimates.

That is far less information than the full old data distribution and full old loss surface.

The original EWC paper explicitly frames the diagonal Fisher construction as a tractable approximation [@KirkpatrickEtAl2017EWC].

So the correct claim is not:

> important parameters can never move.

It is:

> estimated important directions are penalized more strongly.

That can reduce interference.

It does not guarantee exact behavioral preservation.

## 11. The stability-plasticity tension

If every old parameter were frozen forever, old behavior could be protected locally.

But new learning would eventually run out of freedom.

If every parameter remained fully plastic, adaptation would be easy but interference could be severe.

Continual learning therefore repeatedly faces a stability-plasticity tension.

How much should the system preserve?

How much should it change?

The answer depends on:

- capacity;
- task compatibility;
- available memory;
- context information;
- horizon;
- evaluation priorities.

The exact witness makes this tension visible with no stochastic noise.

## 12. Exact witness: two tasks, one scalar

Use one parameter

`w`.

Task A has loss

`L_A(w)=(1/2)(w+1)^2`.

Task B has loss

`L_B(w)=(1/2)(w-1)^2`.

Task A wants

`w=-1`.

Task B wants

`w=1`.

There is no single scalar that makes both losses zero.

This is not an optimization failure.

It is a representational conflict.

The model has one degree of freedom and two incompatible optima.

## 13. Unprotected sequential learning

Train Task A first.

The optimum is

`w=-1`.

Then

`L_A=0`.

Now train Task B to its own optimum.

The parameter moves to

`w=1`.

Then

`L_B=0`

but

`L_A=2`.

The old-task loss increased exactly by

`2`.

That is forgetting in the declared loss metric.

No randomness is involved.

No optimizer pathology is required.

Sequential interference follows from incompatible objectives sharing one parameter.

## 14. Exact quadratic consolidation

Set the scalar importance estimate to

`F=1`.

Use the retention objective

`J_lambda(w)
=
L_B(w)
+
(lambda/2)(w+1)^2`.

The exact minimizer is

`w_lambda=(1-lambda)/(1+lambda)`.

At that point,

`L_A(w_lambda)=2/(1+lambda)^2`

and

`L_B(w_lambda)=2lambda^2/(1+lambda)^2`.

For

`lambda=0`,

we recover full adaptation to B:

`w=1`,
`L_A=2`,
`L_B=0`.

For

`lambda=1`,

the compromise is

`w=0`,
`L_A=1/2`,
`L_B=1/2`.

For very large `lambda`,

`w`

approaches the old optimum and Task B becomes poorly fit.

The penalty therefore does exactly what a consolidation penalty should do in this toy:

it trades plasticity for retention.

## 15. Replay and EWC coincide here for a special reason

Now imagine exact replay with equal weight on both complete task objectives:

`L_joint=L_A+L_B`.

In this witness,

`L_joint(w)=w^2+1`.

The minimizer is again

`w=0`.

So equal replay and the `lambda=1,F=1` quadratic retention penalty produce the same solution.

This is not a general equivalence.

It happens because Task A's loss is itself exactly the quadratic used as the retention penalty.

In a real network:

- replay reevaluates remembered data under the current model;
- EWC uses a local parameter-space approximation around an earlier solution.

The exact coincidence is useful precisely because it shows both the connection and the boundary.

## 16. Gradient constraints: protect old losses at update time

Gradient Episodic Memory takes another route [@LopezPazRanzato2017GEM].

Let

`g`

be the current gradient.

Let

`g_j`

be a gradient computed from episodic memory for old context `j`.

Suppose the update uses

`theta' = theta - eta g_tilde`.

To first order,

`L_j(theta')-L_j(theta)
approximately
-eta g_j^T g_tilde`.

If

`g_j^T g_tilde >= 0`,

the linearized old-context loss does not increase.

GEM therefore turns remembered examples into constraints on the update direction.

This is neither ordinary replay nor EWC.

Replay changes the objective.

EWC adds a parameter penalty.

GEM changes the feasible gradient direction.

## 17. First-order protection has a scope

A gradient constraint is local.

It reasons about the immediate linearized change around the current parameters.

Finite learning rates introduce higher-order effects.

A bounded episodic memory may not represent the full old distribution.

So even a constrained update must retain its claim boundary.

This is a recurring Atlas theme:

> a local protective condition is not automatically a global retention guarantee.

The correct object and scale matter.

## 18. Parameter isolation: stop sharing the contested parameters

There is a more structural response to interference.

Do not let later tasks overwrite the same parameters.

PackNet uses iterative pruning and parameter allocation to add tasks while preserving previously assigned weights [@MallyaLazebnik2018PackNet].

In the scalar witness, parameter isolation means replacing the one shared variable with two task-selected variables:

`w_A=-1`

and

`w_B=1`.

Task A uses `w_A`.

Task B uses `w_B`.

Both losses are zero.

Interference disappears because the conflict has been removed from the shared parameter.

## 19. Isolation pays with capacity and routing

The previous result sounds perfect until we count resources.

The original model had one scalar.

The isolated model has two.

It also needs a selector telling it which scalar to use.

This distinction matters in the continual-learning scenarios.

If task identity is supplied at test time, task-specific masks or heads are natural.

If the model must classify across all accumulated classes without task identity, routing is part of the problem.

Parameter isolation therefore trades one form of difficulty for another:

- less overwrite;
- more capacity accounting;
- more routing structure.

## 20. Replay, consolidation, constraints, and isolation are different levers

The four mechanism families act at different places.

### Replay

Change what data or evidence is present during optimization.

### Consolidation

Change the cost of moving through parameter space.

### Gradient constraints

Change which local update directions are allowed.

### Parameter isolation

Change which parameters can be written by later contexts.

These can be combined.

They can also fail for different reasons.

A replay method may fail because the memory is unrepresentative.

A consolidation method may fail because its importance approximation is poor.

A gradient constraint may fail outside its local approximation or memory support.

An isolation method may exhaust capacity.

Calling all four "memory methods" hides the mechanism.

## 21. Capacity must be reported

Continual learning is easy if we permit unlimited duplication.

For every new task, create a fresh model.

Old performance remains untouched.

But the system grows without bound and may require explicit task routing.

That is why memory and capacity accounting are part of the scientific claim.

Relevant resources can include:

- stored examples;
- stored activations or transitions;
- generated replay models;
- Fisher or importance statistics;
- task-specific heads;
- masks;
- reserved parameter blocks;
- additional networks.

A method that retains better by spending more memory may still be the right engineering choice.

The cost must simply remain visible.

## 22. Average forgetting can hide a damaged context

Suppose two earlier contexts have

`F_1=0`

and

`F_2=1`.

Then

`F_avg=1/2`.

But

`F_max=1`.

Another learner might have

`F_1=1/2`

and

`F_2=1/2`.

The average is identical.

The risk profile is not.

This is why the Atlas keeps both average and worst-context summaries.

A safety-critical application may care about the worst retained capability.

A broad benchmark may care more about average retained performance.

Neither scalar subsumes the other.

## 23. Positive transfer should not be clipped out of existence

Forgetting metrics often focus on decline.

But later learning can improve earlier tasks.

If context B teaches a reusable representation, then

`R_{T,A}>R_{A,A}`

may occur.

A nonnegative forgetting metric reports zero in that case.

That is correct for the narrow question "how much was lost?"

It is incomplete for the broader question "what effect did later learning have?"

So continual-learning reports should preserve signed transfer information where it matters.

Lopez-Paz and Ranzato make transfer an explicit part of continual-learning evaluation [@LopezPazRanzato2017GEM].

## 24. Final accuracy alone is also insufficient

Suppose one learner forgets A badly while learning B, then relearns A later.

Its final score may look good.

Another learner preserves A continuously.

If the application requires always-available capability, those histories are different.

Similarly, a learner may retain old tasks perfectly but fail to learn new ones.

That is not good continual learning merely because forgetting is zero.

The performance-through-time matrix makes both failures visible:

- instability of old capability;
- failure of new acquisition.

## 25. Forgetting and transfer can be asymmetric

Task A may help Task B.

Task B may harm Task A.

Task C may improve both.

Sequential order therefore matters.

A continual-learning benchmark is not fully described by its set of tasks.

It also has an ordering, data schedule, context-transition structure, and evaluation schedule.

Changing the order can change the interference pattern.

That makes continual learning a dynamical training process, not merely multi-task learning with a shuffled dataset.

## 26. Multi-task learning is the useful counterfactual

If all tasks and all data are jointly available from the start, we can optimize a joint objective.

That is not the continual-learning information pattern.

It is still a valuable reference.

The gap between:

- joint training;
- sequential training;
- sequential training with replay;
- sequential training with consolidation;

helps separate capacity conflict from information loss.

If joint training cannot fit all tasks, the model has a compatibility or capacity problem.

If joint training succeeds but sequential training forgets, the schedule and information constraints are implicated more directly.

## 27. Replay versus joint training

Replay approximates some aspects of joint access.

But unless the replay store contains all old data with the same weighting and sampling, it is not identical to joint training.

A bounded exemplar buffer changes the old-data distribution.

Generated replay adds modeling error.

Reservoir sampling, class balancing, and prioritization change which old evidence remains visible.

So "replay" should always be accompanied by a memory contract:

what is stored, how much, how selected, and how sampled.

## 28. EWC versus ordinary L2 regularization

An ordinary quadratic penalty might constrain

`||theta||^2`

or distance from a generic reference.

EWC instead anchors parameters to an earlier task solution with coordinate-specific importance weights.

The source emphasizes this selective plasticity [@KirkpatrickEtAl2017EWC].

The distinction matters.

Uniform resistance can protect unimportant coordinates too strongly and important coordinates too weakly.

EWC attempts to allocate plasticity where the previous task is estimated to tolerate it.

Again, the quality of that estimate is part of the method's empirical burden.

## 29. Consolidation and semantic memory are not synonyms

The Memory Taxonomy chapter uses **semantic** as a role describing generalized knowledge rather than event-specific records.

EWC is called a consolidation method because it stabilizes parameters.

That does not mean the resulting parameters form a clean semantic store.

Likewise, episodic replay examples can contribute to generalized semantic behavior during training.

Memory role and anti-forgetting mechanism answer different questions.

This distinction becomes important in the next chapter family.

## 30. Catastrophic forgetting is partly an access problem

Why does replay help?

Because the learner regains access to evidence that the current stream no longer supplies.

Why does external memory become relevant downstream?

Because parameters are a lossy, interference-prone place to preserve some kinds of information.

But this chapter stops short of the stronger claim.

It does not conclude that knowledge should generally leave the weights.

It establishes the ingredients needed to ask that question:

- what was retained;
- what was forgotten;
- what evidence had to be stored;
- what capacity was consumed;
- what mechanism prevented interference.

The External-Memory chapter will make the architectural argument.

## 31. Failure modes

### Forgetting-equals-parameter-drift

Measure only parameter distance.

Failure: behavior is not evaluated.

### Zero-forgetting-by-zero-learning

Freeze everything.

Failure: old capability is retained because new capability is never acquired.

### Replay-equals-memory-architecture

Call every replay buffer an external persistent memory system.

Failure: training use is confused with storage locus and lifetime.

### EWC-equals-guarantee

Treat a Fisher-weighted local quadratic penalty as exact preservation.

Failure: approximation becomes certification.

### Isolation-equals-free retention

Allocate fresh parameters indefinitely.

Failure: capacity and routing costs disappear from the comparison.

### Average-only reporting

Report one mean retention score.

Failure: severe failure on one context can be hidden.

### Regime mixing

Compare task-incremental and class-incremental results as if task identity were equally available.

Failure: the inference contracts differ.

## 32. A practical continual-learning ledger

Before interpreting a continual-learning result, record:

| Field | Question |
|---|---|
| stream | What changes over time? |
| context | Is task/context identity available during training and evaluation? |
| write target | Which parameters or memory objects are updated? |
| old evidence | What earlier information remains accessible? |
| protection | Replay, consolidation, gradient constraint, isolation, or combination? |
| capacity | What grows with the number of contexts? |
| evaluation | What is the full performance-through-time matrix? |
| forgetting | Average, worst-context, or another declared summary? |
| transfer | Are signed forward/backward effects retained? |
| baseline | Joint training, separate models, naive sequential training, or another comparator? |

This ledger prevents an anti-forgetting mechanism from being evaluated without its information and capacity contract.

## 33. What the exact witness establishes

The scalar witness establishes a narrow but useful result.

Two tasks with incompatible optima share one parameter.

Sequentially optimizing the second task exactly raises the first task's loss from

`0`

to

`2`.

A unit quadratic retention penalty changes the exact compromise to

`w=0`

with losses

`1/2`

and

`1/2`.

Equal-weight replay happens to produce the same point because the old task loss is exactly the same quadratic as the chosen penalty.

Two isolated task-selected parameters achieve zero loss on both tasks by spending extra capacity and routing.

Nothing stronger is implied.

The witness is not a benchmark result.

It is a controlled model of interference.

## 34. Atlas handoff

**The External-Memory Thesis — ATLAS-CH-EXTMEM-001.**

The downstream chapter may now assume:

- forgetting is behavioral, not parameter-distance alone;
- replay restores earlier evidence to training;
- consolidation protects selected parameter directions without replaying the full old distribution;
- gradient constraints and parameter isolation are distinct mechanisms;
- memory and capacity costs belong in the comparison;
- task identity materially changes the difficulty of retention.

That chapter must independently answer the architectural question:

> which knowledge should remain in parameters, and which knowledge should move into persistent shared memory?

The dependency direction matters.

Continual-learning difficulty motivates that question.

It does not answer it in advance.

## References used in this chapter

- McCloskey and Cohen, *Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem* [@McCloskeyCohen1989].
- Kirkpatrick et al., *Overcoming catastrophic forgetting in neural networks* [@KirkpatrickEtAl2017EWC].
- Rebuffi et al., *iCaRL: Incremental Classifier and Representation Learning* [@RebuffiEtAl2017iCaRL].
- Lopez-Paz and Ranzato, *Gradient Episodic Memory for Continual Learning* [@LopezPazRanzato2017GEM].
- Mallya and Lazebnik, *PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning* [@MallyaLazebnik2018PackNet].
- van de Ven, Tuytelaars, and Tolias, *Three types of incremental learning* [@VanDeVenTuytelaarsTolias2022].

Exact prerequisite identities and source-authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-CONTINUAL-001.yaml
