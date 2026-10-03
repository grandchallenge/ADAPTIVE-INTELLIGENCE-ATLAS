# From Models to Agents
<!-- ATLAS-CH-AGENTS-001 -->

**Epistemic status:** established representative mechanisms plus Atlas synthesis and derivation.  
**Specification:** manuscript/specifications/ATLAS-CH-AGENTS-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-AGENTS-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-AGENTS-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-AGENTS-001.yaml

A model can answer a question without being able to change what question comes next.

That is the threshold this chapter cares about.

A language model presented with a fixed context computes a continuation. The continuation may contain a plan, a command, a proof sketch, a search query, or a vivid description of an action. But text that describes an action is not yet an action. Nothing outside the model changes merely because the model wrote a verb.

An agent appears when selected outputs are allowed to participate in a loop.

An observation enters. A model proposes. A controller chooses among admissible operations. An interface executes one of them. The environment or tool returns a consequence. Some part of that consequence is retained. The next decision is made in light of the changed state.

The important transition is therefore not from "less intelligent" to "more intelligent."

It is from an open-loop mapping to a closed interaction architecture.

That distinction is modest enough to be useful.

It does not require us to decide whether a system has intentions, beliefs, or autonomy in a human sense. It asks a narrower systems question:

Can consequences of selected operations change the state from which later operations are chosen?

If yes, then we have acquired dynamics that cannot be understood by inspecting one model call in isolation.

## 1. The model is not the loop

The Adaptive-System Thesis established an explanatory boundary for the Atlas.

A learned model may be one component of a larger computational system that also contains memory, tools, interfaces, evidence, and governance.

Agents make that boundary concrete.

Consider a model

M(c) = y,

where c is supplied context and y is an output.

This object can be extraordinarily capable. It can summarize, prove, translate, classify, generate code, or propose a sequence of actions.

Yet the equation says nothing about whether any proposed action is executed.

It says nothing about who may execute it.

It says nothing about what the execution changes.

It says nothing about whether the result is observed.

It says nothing about whether that result changes the next model call.

Those missing arrows are where agent structure lives.

This chapter therefore uses "model" and "agent" as structural roles, not prestige labels.

A model can be a component of an agent.

The same model can also be used without an agent loop.

And a system can become more agentic in its interaction structure without changing model weights at all.

## 2. A minimal agent object

For the purposes of the Atlas, write an agent as

A = (M, C, X, O, Γ, U, B, σ).

The components are:

M — a model or proposal operator;

C — a controller that selects the next admissible operation;

X — persistent internal state;

O — an observation constructor;

Γ — an execution interface connecting actions to an external state;

U — an update operator for internal state;

B — the current budget-and-authority contract;

σ — a stopping rule.

This is not proposed as the one true definition of an agent.

It is a map legend for the mechanisms this and later chapters need to discuss.

At step t, let e_t denote external state, x_t internal state, and g the current goal.

The loop is:

o_t = O(e_t),

p_t = M(x_t, o_t, g),

a_t = C(x_t, o_t, p_t; B_t),

(e_{t+1}, r_t) = Γ(e_t, a_t),

x_{t+1} = U(x_t, o_t, a_t, r_t).

The budget and authority state are then updated, and σ decides whether another transition is permitted or required.

Every symbol matters.

The model proposal p_t need not be the executed action a_t.

The observation o_t need not expose the full environment state e_t.

The returned result r_t need not be trusted.

The update U may discard information, summarize it, corrupt it, or preserve it exactly.

The authority contract B_t may prohibit an operation even if the model strongly proposes it.

And the stop rule may terminate a competent loop or fail to terminate an incompetent one.

An agent is therefore not a model plus a longer prompt.

It is a model situated inside a transition system.

## 3. Why interaction changes the problem

The difference becomes sharp when useful information does not exist in the original context.

Suppose an environment contains one hidden bit s in {0,1}.

Before interaction, both possible worlds emit the same observation: UNKNOWN.

A deterministic one-shot model must therefore produce the same answer in both worlds.

It cannot guarantee correctness on both because the correct answers differ.

Now add one authorized tool: QUERY.

QUERY returns the hidden bit.

Nothing about the downstream answer rule has changed. The same model can simply report an observed bit if one exists.

But the system can now:

1. call QUERY;
2. receive the consequence;
3. store the returned bit;
4. invoke the answer rule on the changed state.

The exact witness in ATLAS-CW-AGENTS-001 checks both possible hidden states.

Without the query transition, the fixed answer rule succeeds on one of two states.

With one authorized query and budget one, it succeeds on two of two.

Remove the authority or remove the budget, and performance returns to one of two.

The point is not that querying is sophisticated.

The point is that capability can depend on the transition structure around a fixed model.

A system can know more at step t+1 because it did something at step t.

That sentence is the seed from which tool use, search, planning, memory, and coordination grow.

## 4. Tools are transition channels

A tool is often described by its name: calculator, browser, compiler, database, theorem prover, shell, simulator, calendar.

For systems analysis, the name is less important than the interface.

For a tool u with argument z, write

Γ_u(e, z) = (e', r).

The call may leave the external state unchanged and merely return information.

Or it may change the world.

A search query and a bank transfer are both "tool calls" in loose language. Their transition semantics and authority consequences are radically different.

This is why the Atlas separates three events:

the model proposes a call;

the controller determines whether the call is admissible;

the execution interface performs the call and returns a result.

Collapsing these steps creates a dangerous fiction in which generated text appears to carry its own authority.

It does not.

Authority comes from the execution boundary.

The ReAct architecture provides a clear representative mechanism for interleaving reasoning traces, task actions, and returned observations.

Toolformer provides another representative mechanism: a model can learn when to call particular APIs, what arguments to supply, and how to incorporate returned information into later prediction.

These are important constructions.

They should not be inflated into the claim that giving a model more tools necessarily makes the resulting system better.

A larger action set creates opportunities and failure modes at the same time.

## 5. Planning is computation before commitment

Not every proposed action should be executed immediately.

Planning inserts additional computation between the current state and external commitment.

Instead of following one candidate continuation, the system may construct several.

It may estimate consequences.

It may score alternatives.

It may prune some branches.

It may backtrack.

A generic search layer can be written as

H_{k+1} = Select(Score(Expand(H_k))),

where H_k is a set of candidate partial histories at search depth k.

Nothing in this notation requires the candidates to be natural language.

They could be symbolic states, trajectories, programs, proof states, schedules, or mixed representations.

For language models, Tree of Thoughts is a useful representative example because it makes the branching structure explicit. Intermediate text states are generated, evaluated, explored, and sometimes abandoned.

The important abstraction is not the word "thought."

It is the separation between proposing one continuation and allocating computation over several possible continuations before acting.

Planning can improve a decision while still being wrong.

The generator can miss the useful branch.

The evaluator can rank candidates badly.

The search can prune the correct path.

The lookahead model can mispredict the environment.

More search is therefore not identical to more truth.

Planning changes how inference is allocated.

It does not repeal the need for evidence about the quality of the generator, evaluator, model of consequences, and stopping rule.

## 6. Reflection is state update, not self-transcendence

Agent systems are often said to "reflect."

The word invites more mystery than necessary.

Suppose an attempt produces feedback f_t.

A reflective mechanism computes an update

x_{t+1} = U_reflect(x_t, f_t).

The next attempt is conditioned on x_{t+1} rather than x_t.

That is enough structure to study.

Reflexion is a representative mechanism of this type. Feedback is converted into verbal material retained in episodic memory and used in subsequent trials.

The empirical question is whether the update improves later decisions.

The system may reflect accurately.

It may also construct a persuasive explanation of the wrong failure, preserve it, and become more consistently wrong.

Fluency does not settle that question.

A reflection should therefore be treated as a candidate state update whose downstream effect can be measured, ablated, substituted, or contradicted.

This returns us to one of the Atlas's recurring themes:

description is weaker than intervention.

If reflection is claimed to matter, compare the system with and without the reflective state, or with controlled alternatives, while preserving the rest of the loop as closely as possible.

## 7. Decomposition requires interfaces

Large goals are often decomposed into smaller tasks.

That sounds simple until two subtasks disagree about what passes between them.

Let a task decomposition be a directed graph

G_T = (V, E).

Each node v has at least:

- a local goal g_v;
- admissible inputs I_v;
- a required return contract Q_v;
- a local resource budget R_v;
- a stop condition σ_v.

An edge u -> v means that v may consume some declared output or state produced by u.

A list is not yet a robust decomposition.

A decomposition becomes operational when the interfaces between pieces are explicit enough that a downstream node knows what it may assume.

This is the same compositional pressure seen elsewhere in the Atlas.

Tensor shapes do not guarantee semantic compatibility.

Subtask completion labels do not guarantee that a returned object means what the next task needs.

The more independent the subtasks become, the more important their boundaries become.

## 8. Delegation is decomposition plus authority

Delegation adds another ingredient.

A child process is not merely asked to compute something.

It is given some capacity to act.

Represent a delegation packet as

D = (g', A', R', Q', σ').

Here g' is the bounded child goal, A' the authority or tool set granted to the child, R' the resource budget, Q' the required return object, and σ' the child stop rule.

Suppose the parent currently has authority set A and resource budget R.

The default Atlas rule is:

A' subseteq A

and

R' <= R,

unless a distinct external authority explicitly grants an enlargement.

This is not a complete security theorem.

It is a clean invariant.

Spawning a child does not create permission out of nothing.

If every delegation edge respects authority inclusion, then authority cannot expand merely by descending the delegation tree. Set inclusion is transitive.

If every parent allocates child budgets from its own finite budget, the total resource assigned to descendants can likewise be bounded by the root allocation, provided the accounting boundary is actually enforced.

This is what "bounded delegation" means in this chapter.

Not timid delegation.

Not necessarily shallow delegation.

Delegation whose authority, resources, return contract, and stopping condition remain explicit.

## 9. The return is not the truth

A delegated child returns something.

Perhaps it is an answer, a proof, a file, a tool result, a plan, a test report, a witness, or a failure record.

The parent now faces an epistemic problem as well as a control problem.

What is this object allowed to establish?

AGENTS-001 does not solve that question fully. Later chapters on coordination and evidence exchange will.

But one rule belongs here:

child completion is not automatic parent belief.

The return Q' is an input to the parent's next state transition.

It may be checked, replayed, challenged, combined with other evidence, rejected, or escalated.

This matters even when the child and parent use the same underlying model.

A second invocation is not independent verification merely because it happened later.

## 10. Authority and capability are different coordinates

An agent may be capable of proposing an operation it is not authorized to perform.

It may be authorized to perform an operation it cannot use competently.

These are different axes.

Let Cap(x) denote the set of operations the system can successfully formulate or execute from state x under ideal access.

Let Auth(x) denote the operations the current contract permits.

The executable set is constrained by their intersection, together with the actual interfaces available.

A safe system design cannot infer authority from apparent competence.

Nor should it infer competence from possession of credentials.

This distinction becomes increasingly important as agent systems acquire access to software environments, communication channels, financial operations, scientific instruments, or other consequential interfaces.

The model says what it proposes.

The authority boundary says what may happen.

## 11. Budgets turn "keep trying" into mathematics

An unbounded instruction such as "continue until solved" hides several decisions.

How many model calls?

How many tool calls?

How much wall-clock time?

How many child tasks?

How deep may recursion go?

How much money, energy, memory, or external rate limit may be consumed?

Budgets make these questions explicit.

Let R_t be a vector rather than a scalar if resources are heterogeneous.

For example,

R_t = (tokens, tool_calls, wall_time, money, child_slots).

Each transition incurs a nonnegative cost vector c_t.

The update is

R_{t+1} = R_t - c_t,

subject to component-wise nonnegativity.

A stop rule can then require termination before a forbidden negative resource state is reached.

This does not guarantee useful behavior.

It converts one vague control surface into an inspectable one.

## 12. Termination is part of the agent

A loop without a meaningful stop condition is not merely inefficient.

It is incompletely specified.

Stopping may depend on goal satisfaction, proof of impossibility, resource exhaustion, repeated state, lack of progress, external cancellation, confidence or risk threshold, authority boundary, or human review.

A good stop rule can be difficult to design because the system may not know whether one more step would succeed.

But omitting the problem does not remove it.

It merely replaces an explicit stopping policy with whatever accidental limit the runtime, user, or infrastructure imposes.

For recursive delegation, termination becomes structural.

Acyclic task graphs terminate when every finite node terminates.

Cyclic delegation requires an additional argument: decreasing resource, decreasing measure, explicit depth bound, or some other well-founded condition.

"Try again" is not a termination proof.

## 13. Where agent loops fail

The formal decomposition lets us locate failures more precisely.

### Observation failure

The useful distinction in the environment never reaches the agent.

Two states that require different actions may look identical through O.

### Proposal failure

The necessary information is present, but M proposes a poor continuation.

### Controller failure

A sound proposal exists, but C selects a worse operation or admits an operation that should be blocked.

### Interface failure

The tool or environment does not behave according to the semantics the agent assumes.

A returned result may be stale, malformed, adversarial, or simply wrong.

### State-update failure

Useful evidence arrives and is then summarized away, overwritten, misindexed, or attached to the wrong object.

### Planning failure

Search explores the wrong branches, scores them badly, or spends its budget before reaching a useful continuation.

### Reflection failure

The system explains its failure incorrectly and makes the mistaken explanation persistent.

### Delegation failure

The child goal is underspecified, authority is too broad, the return contract is ambiguous, or recursion is allowed to expand without a decreasing resource.

### Termination failure

The system stops before the necessary evidence arrives or continues after further actions have become wasteful or unsafe.

Calling all of these "model errors" would erase the architecture we need in order to repair them.

## 14. Autonomy is not one number

People often ask whether a system is autonomous as though autonomy were a scalar property.

For engineering purposes, several coordinates matter separately.

How long can the loop continue without external intervention?

Which actions may it execute?

How much state persists?

Which environments can it observe?

Can it create child tasks?

Can it alter its own plan?

Can it spend resources?

Can it change the authority of descendants?

What events force review or termination?

Two systems using the same model may therefore have radically different autonomy surfaces.

One may be allowed to search a read-only corpus for three steps.

Another may execute code, modify files, communicate externally, spawn children, and continue for hours.

Calling both "agents" does not make those differences disappear.

The useful question is not merely whether an agent exists.

It is what transition system has actually been authorized.

## 15. What the representative mechanisms establish

The sources used in this chapter demonstrate several concrete mechanisms.

ReAct demonstrates that reasoning traces and environment-facing actions can be interleaved, with observations feeding later steps.

Toolformer demonstrates a learned mechanism for deciding when and how to call external APIs and incorporate their returns.

Tree of Thoughts demonstrates explicit branching, evaluation, lookahead, and backtracking over intermediate language-model states.

Reflexion demonstrates a feedback pathway in which verbalized reflections are retained and influence later episodes.

These results justify discussing such mechanisms as concrete engineering objects.

They do not prove that every capable agent must use them, every task benefits from them, self-evaluation is reliable, tool use is safe, search always improves performance, reflection always corrects errors, or more autonomy is better.

The Atlas needs mechanisms without mythology.

## 16. From one loop to many

A single agent already contains several interacting states: model context, persistent memory, external environment, tool state, resource state, and authority state.

The next chapter introduces a different difficulty.

What happens when several such loops share information or act on common resources?

Then we acquire communication, shared state, concurrency, race conditions, rendezvous, transactions, provenance across actors, partial failure, disagreement, and coordination costs.

Those are not decorations on the single-agent loop.

They form a new systems layer.

ATLAS-CH-COORD-001 may therefore assume the agent object

A = (M, C, X, O, Γ, U, B, σ),

together with typed actions, persistent state, bounded delegation, budget state, authority state, and stop rules.

It must add the mathematics and systems semantics of coordination rather than pretending that a collection of agents is just one larger prompt.

## 17. The boundary to remember

The chapter began with a small distinction.

A model can produce text that describes an action.

An agent loop can allow a selected action to change the state from which later computation proceeds.

Everything else in this chapter elaborates that closure.

Tools enlarge the transition relation.

Planning spends computation before commitment.

Reflection changes persistent state.

Decomposition creates explicit subproblems.

Delegation grants bounded capacity to act on them.

Budgets limit continuation.

Authority limits which transitions may occur.

Stopping rules close the process.

None of these mechanisms guarantees intelligence.

None guarantees truth.

None guarantees safety.

But once they are explicit, they become objects that can be analyzed rather than properties vaguely attributed to "the model."

That is the move from models to agents that the Atlas needs.

## References used in this chapter

External mechanism sources are pinned in:

sources/source-locks/ATLAS-CH-AGENTS-001.yaml

They include:

- ReAct: Synergizing Reasoning and Acting in Language Models, ICLR 2023, arXiv:2210.03629;
- Toolformer: Language Models Can Teach Themselves to Use Tools, NeurIPS 2023, DOI 10.52202/075280-2997;
- Tree of Thoughts: Deliberate Problem Solving with Large Language Models, NeurIPS 2023, arXiv:2305.10601;
- Reflexion: Language Agents with Verbal Reinforcement Learning, NeurIPS 2023, DOI 10.52202/075280-0377.

The Atlas formal loop, budget-and-authority contract, and delegation invariants are chapter-owned synthesis and derivation.
