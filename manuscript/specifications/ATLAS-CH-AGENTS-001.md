# Chapter Specification — ATLAS-CH-AGENTS-001

## Identity

**Title:** From Models to Agents  
**Part:** Agents, Systems, and Hardware  
**Status:** specification-ready.  
**Epistemic class:** established mechanisms plus Atlas synthesis.

## Chapter contract

Explain the transition from a model that maps a supplied context to an output into a system that repeatedly observes, decides, acts through interfaces, receives consequences, updates state, and decides whether to continue.

The chapter must make agent structure mathematically inspectable without treating anthropomorphic vocabulary as explanation.

## Dependency contract

Hard prerequisite:

- ATLAS-CH-THESIS-001 — The Adaptive-System Thesis.

The Thesis supplies the Atlas system boundary in which a learned model is one component of a larger adaptive computational system.

No Coordination, Evidence Exchange, memory-infrastructure, or governance chapter may be used as a hidden prerequisite.

## Reader outcome

A reader should be able to:

1. distinguish a model invocation from an agent transition;
2. identify internal state, environment state, observation, proposal, action, execution result, update, and stop rule;
3. explain how tool use changes the transition relation available to the system;
4. interpret planning as controlled search over candidate continuations rather than as a synonym for intelligence;
5. interpret reflection as a state update whose effect must be tested downstream;
6. represent decomposition as a task graph rather than a rhetorical list;
7. define delegation with explicit task, authority, resource, return, and termination boundaries;
8. explain why a delegated child must not silently acquire authority absent from the parent contract;
9. identify failure modes caused by stale state, bad observations, invalid tools, evaluator error, loops, and budget exhaustion;
10. state what Coordination Architectures may assume after this chapter.

## Formal spine

Use the Atlas agent object

A = (M, C, X, O, Γ, U, B, σ),

where:

- M is the model or proposal operator;
- C is the controller that selects the next admissible operation;
- X is persistent internal state;
- O constructs observations from the environment or tool return;
- Γ is the execution interface acting on an external state;
- U updates internal state;
- B is the current budget-and-authority contract;
- σ is the stopping rule.

At step t:

o_t = O(e_t),

p_t = M(x_t, o_t, g),

a_t = C(x_t, o_t, p_t; B_t),

(e_{t+1}, r_t) = Γ(e_t, a_t),

x_{t+1} = U(x_t, o_t, a_t, r_t),

followed by budget update and evaluation of σ.

This is an Atlas explanatory model, not a universal definition of agency.

## Model-agent boundary

A one-shot model call may be represented as a degenerate one-transition case.

Agent structure becomes materially distinct when later computation depends on consequences of earlier selected actions through persistent state or environmental feedback.

Do not define agency merely by:
- number of tokens;
- use of a system prompt;
- anthropomorphic self-reference;
- marketing labels;
- the presence of hidden chain-of-thought.

## Tool use

Tools are typed transition channels.

For an admissible tool u with argument z,

Γ_u : (e, z) -> (e', r).

The controller may propose a tool call, but admissibility belongs to the interface/authority contract rather than to free-form model text.

Use ReAct and Toolformer only as representative mechanism sources.

## Planning and search

Represent planning as allocating compute across candidate future states or action sequences before commitment.

Search may include branching, scoring, pruning, lookahead, and backtracking.

Tree of Thoughts is a representative language-model search mechanism, not a universal planning theory.

## Reflection

Represent reflection as an update

x_{t+1} = U_reflect(x_t, feedback_t).

The key scientific question is whether the changed state causally improves later decisions under controlled comparison.

Reflexion is a representative mechanism in which verbal feedback enters episodic memory.

Do not equate fluent self-critique with verified correction.

## Decomposition

A decomposed task is a directed task graph G_T = (V, E), where nodes are bounded subgoals and edges encode declared prerequisite or information-flow relations.

A list of subtasks is not yet a useful decomposition unless the interface among subtasks is specified.

## Bounded delegation

A delegation packet is

D = (g', A', R', Q', σ'),

where:

- g' is the child goal;
- A' is the granted authority/tool set;
- R' is the resource budget;
- Q' is the required return contract;
- σ' is the child stop rule.

For a child spawned by a parent with authority A and resource budget R, the default safety invariant is:

A' subseteq A

and

R' <= R,

unless an explicit external authority grants an enlargement.

The child return is candidate evidence or state input to the parent, not automatic truth.

## Computational witness

Create mathematics/computational-witnesses/ATLAS-CW-AGENTS-001.md.

Use a two-state hidden-bit environment to demonstrate exactly that:

- a one-shot model receiving no informative observation cannot guarantee the correct answer for both possible hidden states;
- the same proposal component inside an agent with one authorized QUERY action can observe the bit, update state, and succeed on both states;
- removing query authority or exhausting the budget removes that capability without changing model weights.

This is an architectural witness, not a claim about frontier-model performance.

## Figure decision

No governed figure is required for v0.1.

The transition equations, delegation contract, and exact witness state table carry the chapter's essential semantics. A later state-machine plate may be added when Coordination Architectures supplies a richer multi-agent topology.

## Failure boundaries

Include:

- stale or lossy state;
- observation aliasing;
- invalid or adversarial tool returns;
- planner/evaluator error;
- reflection that reinforces a wrong hypothesis;
- decomposition with incompatible subtask interfaces;
- cyclic delegation;
- resource exhaustion;
- authority leakage;
- termination failure;
- confusing a successful trace with a general capability theorem.

## Downstream handoff

ATLAS-CH-COORD-001 may assume:

- the agent transition object;
- typed action/tool interfaces;
- persistent agent state;
- explicit budget and authority state;
- bounded delegation packets;
- stop conditions.

Coordination must then add communication, shared state, concurrency, transactions, and multi-agent consistency rather than rebuilding the single-agent loop.

## Acceptance

The draft must:

- preserve the audited model-versus-system boundary;
- define the agent loop exactly;
- make tool effects explicit as transitions;
- distinguish planning/search from guaranteed correctness;
- treat reflection as state update with an empirical burden;
- formalize decomposition and bounded delegation;
- include the exact hidden-bit witness;
- state authority monotonicity under delegation;
- expose termination and resource boundaries;
- avoid anthropomorphic definitions;
- remain mathematical systems prose rather than framework documentation.
