# AUDIT-015 — From Models to Agents

## Disposition

**PASS WITH THREE PRECISION REPAIRS**

ATLAS-CH-AGENTS-001 remains at draft-v0.1.

The chapter successfully separates a model invocation from an agent interaction loop, formalizes tool execution, planning, reflection, decomposition, bounded delegation, resource/authority state, and termination, and hands a stable single-agent object to Coordination Architectures.

The audit made three bounded precision repairs:

1. Tree of Thoughts is now bound to its NeurIPS 2023 conference DOI while retaining its arXiv identifier; ReAct also records the ICLR OpenReview identity.
2. The delegation resource inequality is explicitly componentwise when resources are vector-valued.
3. The task-graph termination sentence is restricted to a finite fixed acyclic graph whose execution does not create new nodes outside the graph.

No central formal object, computational witness, or manuscript thesis required reversal.

## Audited baseline

- AGENTS-001 merge:
  84e888476a93a1661deb109ef9a760726a69cfda;
- source-lock baseline:
  1ab13b87c02f90630dbd37be7e4a15ee83643c80;
- audit issue:
  #74;
- chapter:
  ATLAS-CH-AGENTS-001.

## 1. Hard prerequisite and system boundary

PASS.

The hard prerequisite is ATLAS-CH-THESIS-001.

The source lock binds the exact audited Thesis manuscript:

ae89cf78b1bed99dc8d0f4c64b3c1c6553548544

and AUDIT-004:

948f76b3f86d27fa4830efc30d8ef0135134256e.

The chapter preserves the Thesis distinction between a learned model and a larger adaptive computational system.

No downstream Coordination or Evidence Exchange manuscript is used as hidden prerequisite authority.

## 2. External mechanism sources

PASS AFTER SOURCE-IDENTITY REPAIR.

The source lock uses four representative primary mechanisms:

- ReAct, ICLR 2023, arXiv:2210.03629, OpenReview WE_vluYUL-X;
- Toolformer, NeurIPS 2023, DOI 10.52202/075280-2997;
- Tree of Thoughts, NeurIPS 2023, DOI 10.52202/075280-0517, arXiv:2305.10601;
- Reflexion, NeurIPS 2023, DOI 10.52202/075280-0377, arXiv:2303.11366.

The chapter uses them only for representative mechanisms: interleaved action/observation, learned API use, search over intermediate states, and feedback retained in episodic memory.

None is promoted into a universal definition or necessary architecture of agency.

## 3. Agent object

PASS.

The chapter defines

A = (M, C, X, O, Γ, U, B, σ),

with distinct roles for:

- model/proposal operator;
- controller;
- persistent internal state;
- observation constructor;
- execution interface;
- state update;
- budget-and-authority contract;
- stop rule.

The tuple is explicitly labeled Atlas synthesis rather than a universal ontology.

## 4. Model versus agent loop

PASS.

The chapter distinguishes:

model invocation:
supplied context -> output;

from:

agent loop:
observation -> proposal -> admissible action -> consequence -> state update -> later decision.

The model can remain unchanged while the surrounding interaction structure changes.

The chapter does not define agency by anthropomorphic language, prompt length, or marketing labels.

## 5. Tool proposal versus execution authority

PASS.

The chapter separates:

1. model proposal;
2. controller admissibility;
3. actual execution and returned result.

Generated text is not treated as carrying its own authority.

This is a load-bearing distinction for later coordination and governance chapters.

## 6. Planning and search

PASS.

Planning is modeled as computation over candidate continuations before external commitment.

The generic search relation

H_{k+1} = Select(Score(Expand(H_k)))

does not imply correctness.

The manuscript explicitly preserves generator, evaluator, pruning, and environment-model failure modes.

Tree of Thoughts is used as a representative mechanism, not a universal planning theory.

## 7. Reflection

PASS.

Reflection is represented as

x_{t+1} = U_reflect(x_t, f_t).

Reflexion supports the concrete mechanism of verbal feedback retained for later episodes.

The manuscript explicitly rejects:

fluent self-critique -> verified correction.

It places an empirical burden on claims that reflective state improves later decisions.

## 8. Decomposition

PASS.

The chapter uses a task graph

G_T = (V, E)

whose nodes carry goals, admissible inputs, return contracts, budgets, and stop conditions.

A rhetorical subtask list is not treated as a complete decomposition.

Interface semantics remain necessary.

## 9. Bounded delegation

PASS AFTER PRECISION REPAIR.

The delegation packet is

D = (g', A', R', Q', σ').

Default invariants are:

A' subseteq A,

R' <= R.

For vector-valued resources, the resource relation is now explicitly componentwise.

An authority enlargement requires a distinct external grant rather than arising automatically from child creation.

## 10. Authority monotonicity

PASS.

If every delegation edge obeys

A_child subseteq A_parent,

then authority is non-expanding along a descendant path by transitivity of set inclusion.

The derivation correctly limits this theorem to the declared authority-set model and notes enforcement failures such as porous boundaries, misclassification, credential leakage, or external grants.

## 11. Resource-tree bound

PASS AFTER WORDING REPAIR.

For the explicitly budgeted finite delegation tree, child allocations plus parent reserved cost are bounded by the parent budget.

The induction statement now says that total resource consumed by the subtree rooted at v, including the parent reserved cost, is at most R_v.

The manuscript does not generalize this to unmetered systems or incomparable resource units.

## 12. Termination

PASS AFTER SCOPE REPAIR.

The reader-facing statement is now restricted to a finite fixed acyclic task graph whose activated nodes terminate and whose execution does not create new nodes outside the graph.

Cyclic or dynamically expanding delegation is explicitly said to require an additional well-founded argument, resource decrease, or depth bound.

"Try again" is not treated as a termination proof.

## 13. Computational witness

PASS.

ATLAS-CW-AGENTS-001 exhaustively evaluates the hidden state s in {0,1}.

The same answer rule scores:

- 1/2 with no informative interaction;
- 2/2 with QUERY authorized and budget one;
- 1/2 with QUERY authority removed;
- 1/2 with zero budget.

The witness correctly isolates action availability, returned observation, persistent state, and budget without changing model weights.

Its claim boundary explicitly rejects general conclusions about language-agent reliability, arbitrary tool usefulness, autonomy desirability, or framework superiority.

## 14. Failure surfaces

PASS.

The manuscript distinguishes:

- observation failure;
- proposal failure;
- controller failure;
- interface failure;
- state-update failure;
- planning failure;
- reflection failure;
- delegation failure;
- termination failure.

This prevents all agent-system defects from being collapsed into "model error."

## 15. Autonomy and authority

PASS.

Autonomy is treated as a multidimensional systems surface rather than a scalar prestige label.

Capability and authority are separate coordinates.

The executable set is constrained by both available capability and granted authority.

## 16. Downstream handoff

PASS.

ATLAS-CH-COORD-001 may inherit:

- the agent tuple;
- typed action interfaces;
- persistent state;
- budget and authority state;
- delegation packets;
- stop rules.

Coordination must add shared state, communication, concurrency, rendezvous, transactions, and multi-agent consistency.

## 17. Integrity

PASS.

The manuscript, formal packet, and witness contain no hidden C0 control characters or tabs.

The Chapter Ledger records ATLAS-CH-AGENTS-001 at draft-v0.1.

The Source Register contains ATLAS-SRC-AGENTS-LOCK-001.

The witness contains an explicit Claim boundary.

No governed figure is registered, consistent with the tranche decision to defer a state-machine plate until the coordination topology is available.

## 18. Final disposition

AUDIT-015 passes with the three precision repairs above.

The Atlas now has a stable bridge from:

model as proposal operator

to

agent as bounded interaction loop.

The next coordination chapter may start from that object rather than rebuilding the model/tool/state/authority boundary.
