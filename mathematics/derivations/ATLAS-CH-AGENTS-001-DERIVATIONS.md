# ATLAS-CH-AGENTS-001 — Formal and Documentary Packet

## Purpose

This packet makes the chapter's agent object and bounded-delegation rules inspectable.

It distinguishes established representative mechanisms from Atlas-owned synthesis.

## 1. Hard prerequisite

ATLAS-CH-THESIS-001 supplies the system boundary: a learned model may be one component of an adaptive computational system containing persistent state, memory, tools, interfaces, evidence, and governance.

AUDIT-004 confirms that this boundary is Atlas Synthesis rather than a universal ontology.

AGENTS-001 specializes that boundary to repeated goal-directed interaction.

## 2. Agent object

The chapter uses

A = (M, C, X, O, Γ, U, B, σ).

M is the proposal model.

C is the controller.

X is persistent internal state.

O constructs observations.

Γ executes admissible actions against an external state.

U updates internal state.

B records budget and authority.

σ is the stop rule.

The tuple is deliberately architectural. It does not require every implementation to expose each component as a separate software module.

## 3. One transition

For external state e_t, internal state x_t, goal g, and budget/authority state B_t:

o_t = O(e_t),

p_t = M(x_t, o_t, g),

a_t = C(x_t, o_t, p_t; B_t),

(e_{t+1}, r_t) = Γ(e_t, a_t),

x_{t+1} = U(x_t, o_t, a_t, r_t).

Then B_t is updated according to the declared cost and authority rule and σ is evaluated.

The essential distinction is that later decisions can depend on consequences of earlier actions.

## 4. Model invocation as a degenerate case

Suppose M maps a fixed supplied context c to output y:

y = M(c).

If no selected operation changes an external state, no returned consequence is incorporated, and no persistent state affects a later decision, then the full loop collapses to one transition.

Thus the Atlas does not posit a metaphysical border between models and agents.

It uses a structural border:

model invocation:
supplied context -> output.

agent loop:
observation -> proposal -> admissible action -> consequence -> state update -> later decision.

## 5. Tool interfaces

For tool u with argument z, write

Γ_u(e, z) = (e', r).

Three objects must be separated:

1. the model proposal to call u;
2. the authority decision that u is admissible;
3. the actual execution and returned result.

ReAct provides a representative example of interleaving reasoning and actions with external observations.

Toolformer provides a representative example of learning when and how to invoke APIs and then consuming returned results.

Neither source implies that tool use is always beneficial or safe.

## 6. Planning as search before commitment

Planning allocates computation over candidate future states or actions before committing to one external transition.

Let H_k be a set of candidate partial histories at search depth k.

A generic search cycle can be written as:

H_{k+1} = Select(Score(Expand(H_k))).

The operators may be learned, symbolic, heuristic, or hybrid.

Tree of Thoughts is a representative language-model construction in which coherent intermediate text states can be generated, evaluated, branched, and backtracked.

The Atlas uses this as evidence that inference-time search can be separated from the base left-to-right proposal process.

It is not used to claim that tree search is necessary for agency.

## 7. Reflection as state update

Let f_t denote task feedback after an attempt.

A reflective update is

x_{t+1} = U_reflect(x_t, f_t).

The next decision then depends on x_{t+1}.

Reflexion supplies a concrete representative mechanism in which verbalized feedback is retained in episodic memory for later trials.

The structural point is narrower than the empirical result:

reflection can be modeled as changing future input state without changing model weights.

The chapter does not infer:

reflection text is correct -> later action is correct.

## 8. Decomposition as a task graph

Let G_T = (V, E) be a directed task graph.

Each node v in V has:

- goal g_v;
- admissible inputs I_v;
- required output contract Q_v;
- local budget R_v;
- stop condition σ_v.

An edge u -> v states that v may depend on an output or state transition produced by u.

A decomposition is useful only when the edges carry enough interface semantics for downstream nodes to know what they may consume.

## 9. Bounded delegation

A delegation creates a child work object

D = (g', A', R', Q', σ').

The parent supplies a bounded child goal, granted authority/tool set, resource budget, required return schema, and termination condition.

If the parent currently possesses authority A and resource budget R, the default Atlas delegation invariant is:

A' subseteq A,

R' <= R.

For vector-valued resources, the inequality is componentwise.

This is a monotonicity condition on delegated authority and resources.

An explicit external grant can enlarge authority, but that grant is then a separate transition with its own provenance.

## 10. Delegation tree resource bound

Consider a finite delegation tree T.

For every parent node v with children ch(v), suppose budgets are allocated so that the sum of child budgets is at most R_v - c_v, where c_v is the parent's own reserved execution cost.

Then the total resource consumed by the subtree rooted at v, including the parent's reserved cost c_v, cannot exceed R_v.

Proof is by induction on tree depth.

At a leaf, the statement is immediate.

At an internal node, each child subtree consumes no more than its allocated budget by the induction hypothesis. Summing child bounds and adding c_v gives at most R_v.

This is an Atlas derivation for an explicitly budgeted delegation tree.

It is not a theorem about real agent systems whose accounting can be bypassed or whose resource units are incomparable.

## 11. Authority monotonicity

If every delegation edge v -> w obeys

A_w subseteq A_v,

then authority along any descendant path is non-expanding:

A_descendant subseteq A_ancestor.

This follows by transitivity of set inclusion.

The mathematical statement is exact only for the declared authority sets.

A software system can violate the model if the enforcement boundary is porous, capabilities are misclassified, credentials leak, or an external actor grants new authority.

## 12. Hidden-bit witness

ATLAS-CW-AGENTS-001 uses environment state s in {0,1}.

Before querying, the observation is identical for both states.

A one-shot deterministic model receiving that observation must emit the same answer in both states, so it cannot be correct for both.

The agent has one authorized action QUERY with cost one.

QUERY returns s exactly.

After incorporating the return into x_t, the same answer operator emits s.

Exhaustive replay over s=0 and s=1 gives:

- one-shot fixed observation: at most 1/2 states correct;
- authorized one-query agent: 2/2 states correct;
- same loop with query authority removed: at most 1/2;
- same loop with budget zero: at most 1/2.

The witness isolates interface and state-update structure without changing model weights.

## 13. Failure modes

The formal object exposes distinct failure surfaces.

Observation failure: O hides or aliases state required for a good decision.

Proposal failure: M proposes a poor action despite sufficient state.

Controller failure: C selects or admits the wrong operation.

Tool/interface failure: Γ returns bad data, executes the wrong side effect, or violates assumed semantics.

Update failure: U discards or corrupts useful consequences.

Planning failure: search scores or prunes the useful branch incorrectly.

Reflection failure: feedback is misread and a wrong hypothesis is reinforced.

Delegation failure: task boundaries, return contracts, budgets, or authority sets are incomplete.

Termination failure: σ does not stop loops that should stop.

## 14. Downstream handoff

ATLAS-CH-COORD-001 may consume:

- A = (M,C,X,O,Γ,U,B,σ);
- tool/action interfaces;
- internal state across transitions;
- budget and authority state;
- delegation packets;
- stop rules.

Coordination must add interactions among multiple such loops, including shared state, communication, rendezvous, concurrency, and transactions.

## Claim boundary

This packet provides an Atlas formalization of agent structure and bounded delegation.

The external papers support representative mechanisms.

The tuple, delegation invariants, and hidden-bit analysis are Atlas-owned synthesis and derivation, not a universal definition or general performance theorem for autonomous systems.
