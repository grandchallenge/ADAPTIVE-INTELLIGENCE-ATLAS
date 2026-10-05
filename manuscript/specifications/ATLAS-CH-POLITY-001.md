# Chapter Specification — ATLAS-CH-POLITY-001

## Identity

**Title:** The Computational Polity  
**Part:** Agents, Systems, and Hardware  
**Status:** specification-ready.  
**Epistemic class:** audited Coordination and External Memory prerequisites + primary agent/distributed-cognition/joint-activity sources + Atlas synthesis.

## Contract

Develop intelligence as a coordinated system of models, memory, tools, humans, validators, and governance.

The chapter must distinguish:

- one model or agent from the larger system in which it participates;
- private state from shared external memory;
- capability from authority;
- message delivery from acceptance;
- candidate result from validated result;
- tool execution from successful transaction completion;
- human participation from unlimited or implicit authority;
- governance rules from evidence that a result is correct;
- local competence from system-level competence;
- composition gain from mere component count.

## Hard prerequisites

- ATLAS-CH-COORD-001
- ATLAS-CH-EXTMEM-001

Exact prerequisite identities and source authority are locked in:

`sources/source-locks/ATLAS-CH-POLITY-001.yaml`.

## Computational polity object

Define a polity

\[
\Pi=(A,M,U,H,V,C,\Gamma,Q),
\]

where A is the set of model/agent roles; M shared external memory; U tools or external services; H human roles; V validator/reviewer roles; C the inherited coordination object; \Gamma the governance relation for admissible transitions and authority; and Q the task/claim contract.

A polity state may be a product of local and shared states rather than one vector:

\[
X=X_A\times X_M\times X_U\times X_H\times X_V.
\]

## Capability versus authority

Let \(\operatorname{Can}(r,a)\) mean role r can produce action or claim a, while \(\operatorname{May}(r,a,\Gamma)\) means r is authorized to commit it.

\[
\operatorname{Can}(r,a)\not\Rightarrow \operatorname{May}(r,a,\Gamma).
\]

Authorization likewise does not imply correctness.

## Candidate-to-commit pipeline

\[
q\rightarrow\text{route}\rightarrow\text{candidate}\rightarrow\text{evidence record}\rightarrow\text{validation}\rightarrow\text{authorized commit}.
\]

Every arrow may fail independently. Candidate production is not validation; validation is not authorization; authorization is not truth; commit is not automatically successful external effect.

## Exact specialization witness

Use task classes \(Q=\{\alpha,\beta\}\) and specialists

\[
A_\alpha(\alpha)=1,\quad A_\alpha(\beta)=0,
\]

\[
A_\beta(\alpha)=0,\quad A_\beta(\beta)=1.
\]

Under the uniform task distribution, each specialist alone has accuracy \(1/2\). Define routing

\[
R(\alpha)=A_\alpha,\qquad R(\beta)=A_\beta.
\]

Then the composed polity returns \(\Pi(q)=R(q)(q)=1\) for both tasks, so accuracy is 1. This finite result does not imply that more agents always help.

## Shared-memory extension

An accepted result may be stored as \(m=(q,y,s,v,\sigma)\), carrying task, result, source identity, version, and status. Shared storage is not automatically true, current, complete, or globally visible.

## Human and validator roles

Human and validator roles are explicit role classes inside \(\Pi\), not escape hatches from formal system description. Their actions require declared inputs, authority, provenance, bounded transition semantics, and failure handling.

## Failure boundaries

- more components != greater capability;
- shared memory != shared belief;
- route selected != route correct;
- candidate produced != candidate valid;
- validator passed != universal truth;
- human reviewed != error impossible;
- governance authorized != evidence complete;
- tool call returned != side effect durably committed;
- system-level capability != capability of any one member;
- system-level capability != unexplained emergence.

## Downstream handoff

Direct consumer: ATLAS-CH-SYNTHESIS-001.

SYNTHESIS may inherit the polity object, the capability/authority distinction, private/shared-state separation, the candidate-to-commit pipeline, and the finite specialization witness. It must independently synthesize the Atlas-wide systems view.

## Sources

- [@WooldridgeJennings1995Agents]
- [@Hutchins1995CognitionWild]
- [@KleinEtAl2004TeamPlayer]

Exact source authority and claim boundaries are locked in `sources/source-locks/ATLAS-CH-POLITY-001.yaml`.