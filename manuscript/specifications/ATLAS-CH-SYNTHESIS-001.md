# Chapter Specification — ATLAS-CH-SYNTHESIS-001

## Identity
**Title:** Connections, Boundaries, and Open Terrain  
**Part:** Scientific Method, Evidence, and Governed Adaptation  
**Status target:** draft-v0.1  
**Implementation issue:** #276  
**Protected baseline:** 4c038e50f91e152e8139fc0dd412587d02f620fb

## Hard prerequisites
FRONTIER-001 / AUDIT-043 supplies the programme-status grammar and the rule that open questions remain open.

POLITY-001 / AUDIT-048 supplies private/shared-state separation, capability/authority distinction, candidate-validation-commit decomposition, heterogeneous cost bookkeeping, and the exact two-specialist witness.

Exact identities are frozen in:

sources/source-locks/ATLAS-CH-SYNTHESIS-001.yaml

## Optional systems signature

For the bounded composite-systems example, introduce the descriptive signature

\[
\Sigma=(X,D,M,T,C,E,A,G,Q,K).
\]

It is not a universal ontology or an independent mathematical theorem. This chapter's primary duty is to map mathematical connections and limits across the Atlas, without claiming an architecture ranking.

- \(X\): model/representation and private state.
- \(D\): dynamics/update laws.
- \(M\): persistent/shared memory.
- \(T\): tools/external services.
- \(C\): coordination/routing/composition.
- \(E\): evidence/validation.
- \(A\): adaptation.
- \(G\): governance/authority.
- \(Q\): task/success contract.
- \(K\): heterogeneous cost/resource vector.

These are typed objects rather than one assumed vector state.

## Exact finite witness

Tasks:

\[
Q=\{\alpha,\beta\}.
\]

Specialists:

\[
A_\alpha(\alpha)=1,\quad A_\alpha(\beta)=0,
\]

\[
A_\beta(\alpha)=0,\quad A_\beta(\beta)=1.
\]

Router:

\[
R(\alpha)=A_\alpha,\qquad R(\beta)=A_\beta.
\]

Candidate \(c=(q,y,s)\).

Validator accepts iff \(y=1\) and \(s\) is the declared specialist for \(q\).

Governance commits iff validation accepts.

Shared memory persists \((q,y,s,\mathrm{validated})\).

Full composition:
- task accuracy \(2/2\);
- validated commit coverage \(2/2\);
- persistent recall coverage \(2/2\);
- unauthorized commits \(0\).

## Ablations

Broken router:

\[
R'(\alpha)=A_\alpha,\qquad R'(\beta)=A_\alpha.
\]

Task and commit coverage fall to \(1/2\).

Remove validator but keep governance: transient answer accuracy may remain \(2/2\), authorized commits become \(0/2\).

Remove shared memory: immediate success may remain \(2/2\), persistent recall becomes \(0/2\).

Remove governance: rejected bad-source candidate

\[
c_{\mathrm{bad}}=(\beta,1,A_\alpha)
\]

can be written if the commit gate is bypassed.

## Status grammar

Preserve exactly:
- AUDIT_BOUND_SUBSTRATE
- DRAFT_SUBSTRATE
- BOUNDED_EVIDENCE
- ARCHITECTURE_STAGE
- OPEN_PROOF_OBLIGATION
- OPEN_EXPERIMENT_OBLIGATION
- CONJECTURAL_CONNECTION

## Required non-implications

\[
\text{component count}\not\Rightarrow\text{composition quality},
\]

\[
\text{answer capability}\not\Rightarrow\text{authorized durable state},
\]

\[
\text{immediate success}\not\Rightarrow\text{persistent recall},
\]

\[
\text{correct-looking content}\not\Rightarrow\text{authorized transition},
\]

\[
\text{distributed}\not\Rightarrow\text{superior}.
\]

A successful finite composition does not establish a universal architecture.

## Cost boundary

Retain

\[
K=(c_{\mathrm{coord}},c_{\mathrm{mem}},c_{\mathrm{tool}},c_{\mathrm{human}},c_{\mathrm{val}}).
\]

Do not scalarize unlike costs without a declared objective.

## Required artifacts
Source lock, specification, derivation packet, exact witness, reader manuscript, Chapter Ledger promotion, Source Register entry, transaction receipt, post-draft audit.

## References used in this chapter
No new external authority is added. Programme-status authority is inherited through audited FRONTIER-001 and system-composition authority through audited POLITY-001.
