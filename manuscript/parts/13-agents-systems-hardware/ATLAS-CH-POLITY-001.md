# The Computational Polity
<!-- ATLAS-CH-POLITY-001 -->

**Epistemic status:** audited prerequisites + primary scholarly sources + Atlas synthesis + exact finite witness  
**Specification:** manuscript/specifications/ATLAS-CH-POLITY-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-POLITY-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-POLITY-001.md

A capable model is not automatically a capable system.

A real adaptive system may include several models, a shared memory, tools, human participants, validators, transaction boundaries, and rules about who may change what. Once those elements matter to the result, treating the model alone as the full locus of intelligence hides the mechanism that actually produced the outcome.

This chapter calls the larger object a **computational polity**.

## 1. From agent to polity

Wooldridge and Jennings distinguish agent theory, agent architectures, and agent languages, already making clear that an intelligent agent is an architectural object rather than merely a function from prompt to answer [@WooldridgeJennings1995Agents].

The Atlas goes one level outward.

A polity is not just a collection of agents. It is a collection plus the rules by which local states, shared records, tools, validators, human roles, and authority compose.

## 2. The polity object

Write

\[
\Pi=(A,M,U,H,V,C,\Gamma,Q).
\]

Here:

- \(A\) is the set of model or agent roles;
- \(M\) is shared external memory;
- \(U\) is the set of tools or external services;
- \(H\) is the set of human roles;
- \(V\) is the set of validator or reviewer roles;
- \(C\) is the inherited coordination object;
- \(\Gamma\) is the governance relation defining admissible transitions and authority;
- \(Q\) is the task or claim contract.

These coordinates need not share one data type. The polity is a systems object, not one giant hidden vector.

## 3. Local state and shared state

The Coordination chapter already separates local actor state from shared coordination state. The External Memory chapter adds version, provenance, access, synchronization, and deletion semantics for persistent records.

POLITY therefore inherits a hard boundary:

\[
\text{shared address}\not\Rightarrow\text{shared belief}.
\]

Two participants may refer to the same named store while seeing different versions, different permissions, different caches, or different retrieval results.

Common memory is not identical internal state.

## 4. Capability is not authority

A role may be able to produce an action without being allowed to commit it.

Define

\[
\operatorname{Can}(r,a)
\]

for capability and

\[
\operatorname{May}(r,a,\Gamma)
\]

for authorization under governance \(\Gamma\).

In general,

\[
\operatorname{Can}(r,a)\not\Rightarrow\operatorname{May}(r,a,\Gamma).
\]

The reverse implication also fails as a correctness claim. Permission to act does not prove that the action is wise, true, or safe.

This distinction becomes load-bearing whenever a model proposes a change that a different role must validate or authorize.

## 5. Candidate is not conclusion

A representative polity path is

\[
q
\rightarrow
\text{route}
\rightarrow
\text{candidate}
\rightarrow
\text{evidence record}
\rightarrow
\text{validation}
\rightarrow
\text{authorized commit}.
\]

Every arrow can fail independently.

A good candidate may be routed to the wrong validator. A correct validator result may be applied to stale evidence. An authorized commit may fail at an external side effect. A message may be delivered without being accepted. A shared record may exist without being current.

The polity view makes those failure surfaces visible.

## 6. Why humans remain inside the system boundary

Human review is often drawn outside technical diagrams, as though a person enters only after the computational story is complete.

For a polity, that is a modeling error whenever the human decision changes system state.

Human roles have inputs, information limits, authority, latency, provenance, and failure modes. Klein and colleagues emphasize that automation participating in joint human-agent activity must function as a team participant rather than as an isolated device [@KleinEtAl2004TeamPlayer].

The Atlas therefore models human roles explicitly without assuming that human participation makes the system infallible.

## 7. System-level cognition is an old idea

Hutchins analyzes navigation as a cognitive and computational activity distributed across people, artifacts, procedures, and representations rather than exhausted by one person's internal cognition [@Hutchins1995CognitionWild].

The Computational Polity uses that precedent carefully.

It does not claim that every distributed system is intelligent. It claims only that, when the mechanism of successful computation spans several components, the correct explanatory boundary may also span those components.

## 8. Exact two-specialist witness

Let

\[
Q=\{\alpha,\beta\}.
\]

Define two specialists:

\[
A_\alpha(\alpha)=1,\quad A_\alpha(\beta)=0,
\]

and

\[
A_\beta(\alpha)=0,\quad A_\beta(\beta)=1.
\]

Under a uniform task distribution, each specialist alone has accuracy

\[
\frac12.
\]

Now define a router

\[
R(\alpha)=A_\alpha,\qquad R(\beta)=A_\beta.
\]

The composed polity returns

\[
\Pi(q)=R(q)(q)=1
\]

for both tasks, so

\[
\operatorname{Acc}(\Pi)=1.
\]

The system-level capability is exact and easy to inspect.

## 9. The same components can still fail

Now replace the router by one that always chooses \(A_\alpha\).

The component set is unchanged.

The system accuracy returns to

\[
\frac12.
\]

Therefore:

\[
\boxed{\text{more components}\not\Rightarrow\text{greater capability}.}
\]

The composition rule matters.

## 10. Shared memory as a polity institution

An accepted result may be stored as

\[
m=(q,y,s,v,\sigma),
\]

where \(q\) is task identity, \(y\) the result, \(s\) source identity, \(v\) version, and \(\sigma\) status.

This record can be read by later roles without requiring every model to internalize the result in weights.

But the External Memory boundary remains:

- stored does not mean true;
- present does not mean current;
- shared does not mean universally visible;
- retrieved does not mean correctly used.

## 11. Validators are roles, not oracles

A validator can reduce a declared class of error.

It cannot be promoted into an infallible truth function merely because it has the title 'validator'.

A polity therefore records:

- what the validator receives;
- which criterion it applies;
- which authority it has;
- what evidence it preserves;
- what happens when it abstains, fails, or disagrees.

The same discipline applies to human review.

## 12. Governance is transition structure

Governance answers questions such as:

- who may create a candidate;
- who may validate it;
- who may commit it;
- which transitions require distinct actors;
- which states are protected;
- which evidence is required before promotion.

These are transition constraints.

Governance does not manufacture evidence that is missing from the underlying claim.

Thus:

\[
\boxed{\text{authorized}\not\Rightarrow\text{correct}.}
\]

and

\[
\boxed{\text{correct-looking}\not\Rightarrow\text{authorized}.}
\]

## 13. Tools and external effects

A polity may call search systems, databases, compilers, laboratories, actuators, or other services.

The inherited coordination boundary matters here: an internal transaction cannot silently make an external side effect atomic.

A successful tool response and a durably committed external state change are different events unless the interface explicitly couples them.

## 14. Cost is heterogeneous

A polity consumes more than model FLOPs.

A useful bookkeeping vector is

\[
c_\Pi=(c_{coord},c_{mem},c_{tool},c_{human},c_{val}).
\]

These entries may have different units. They should not be added into one scalar unless the application declares a conversion or objective.

This prevents 'more agents' from being treated as free.

## 15. Roles are not identities

One physical or software participant may occupy several roles over time.

Conversely, one role may be filled by different participants.

The polity should therefore bind authority and provenance to role and identity explicitly rather than assuming that labels such as 'agent', 'reviewer', or 'human' carry permanent semantics.

## 16. System-level competence needs a declared contract

A polity-level claim should identify at least:

- task set or distribution;
- component roles;
- routing/composition rule;
- memory semantics;
- validation rule;
- governance/authority rule;
- success metric.

Without these, 'the system can do X' is too underspecified to audit.

## 17. What this chapter does not claim

The polity view does not imply:

- that distributed systems are always better than monolithic models;
- that human review is always superior to automation;
- that more validators always improve reliability;
- that shared memory is globally consistent;
- that governance guarantees correctness;
- that specialization always outweighs coordination cost;
- that system-level behavior is mysterious emergence.

The aim is the opposite: make system-level capability reconstructable from explicit composition.

## 18. Handoff to Beyond the Monolithic Model

ATLAS-CH-SYNTHESIS-001 may now assume:

- the polity object \(\Pi\);
- private/shared-state separation;
- the capability/authority distinction;
- candidate, validation, and commit as separate stages;
- the exact specialization witness;
- the requirement that system capability be demonstrated under declared composition.

SYNTHESIS must still connect this systems view to the rest of the Atlas: geometry, dynamics, memory, optimization, evidence, adaptation, and governance.

## 19. Durable lesson

A model can be an important component without being the whole intelligent system.

When memory, tools, humans, validators, and governance materially determine the result, the explanatory object should include them.

The computational polity is that larger object.

## References used in this chapter

- [@WooldridgeJennings1995Agents]
- [@Hutchins1995CognitionWild]
- [@KleinEtAl2004TeamPlayer]

Exact source authority, prerequisite identities, and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-POLITY-001.yaml