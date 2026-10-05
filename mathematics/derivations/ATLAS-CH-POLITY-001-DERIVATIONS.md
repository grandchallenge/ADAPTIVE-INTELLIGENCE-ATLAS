# ATLAS-CH-POLITY-001 — Derivation Packet

## Scope

This packet formalizes the Atlas object used by The Computational Polity. It inherits coordination semantics and shared-memory boundaries from audited prerequisites and adds only polity-level composition.

Source boundary: `sources/source-locks/ATLAS-CH-POLITY-001.yaml`.

## 1. Polity object

Let

\[
\Pi=(A,M,U,H,V,C,\Gamma,Q).
\]

The coordinates denote machine/model roles, external memory, tools/services, human roles, validator roles, inherited coordination semantics, governance/authority rules, and the task contract.

The object is heterogeneous by design. No claim is made that all coordinates admit one common vector representation.

## 2. Local and shared state

Write a polity state schematically as

\[
X=X_A\times X_M\times X_U\times X_H\times X_V.
\]

The inherited coordination interface permits local state and shared state to coexist. The inherited memory interface requires explicit synchronization, version, provenance, and access semantics for shared records.

Thus

\[
\text{shared address}\not\Rightarrow\text{identical simultaneous view}.
\]

## 3. Capability and authority

Define two predicates:

\[
\operatorname{Can}(r,a)
\]

for ability to produce action a, and

\[
\operatorname{May}(r,a,\Gamma)
\]

for authorization to commit a under governance \(\Gamma\).

There is no logical implication

\[
\operatorname{Can}(r,a)\Rightarrow\operatorname{May}(r,a,\Gamma).
\]

Likewise, authorization is a transition rule, not a proof of correctness.

## 4. Exact two-specialist composition

Let the task set be

\[
Q=\{\alpha,\beta\}.
\]

Define

\[
A_\alpha(\alpha)=1,\quad A_\alpha(\beta)=0,
\]

and

\[
A_\beta(\alpha)=0,\quad A_\beta(\beta)=1.
\]

Under the uniform distribution on Q,

\[
\operatorname{Acc}(A_\alpha)=\operatorname{Acc}(A_\beta)=\frac12.
\]

Let routing satisfy

\[
R(\alpha)=A_\alpha,\qquad R(\beta)=A_\beta.
\]

Then

\[
\Pi(q)=R(q)(q)=1
\]

for both q, hence

\[
\operatorname{Acc}(\Pi)=1.
\]

This is an exact composition gain relative to each specialist alone.

## 5. Composition gain is conditional

If the router is replaced by

\[
R'(\alpha)=R'(\beta)=A_\alpha,
\]

then the composed system again has accuracy \(1/2\).

Therefore

\[
\text{more components}\not\Rightarrow\text{greater system capability}.
\]

The gain depends on the composition law.

## 6. Candidate, validation, commit

Represent a candidate result as

\[
e=(q,y,s,p),
\]

with task q, result y, source identity s, and provenance p.

A validator maps candidate evidence to a bounded disposition, while governance determines whether that disposition authorizes a state transition.

These are distinct maps:

\[
e\xrightarrow{V}d\xrightarrow{\Gamma}\text{commit or reject}.
\]

Neither map is assumed infallible.

## 7. Shared-memory record

An accepted record can be represented as

\[
m=(q,y,s,v,\sigma),
\]

with source s, version v, and status \(\sigma\).

The External Memory prerequisite prevents the inference that presence in M implies truth, freshness, completeness, or unrestricted visibility.

## 8. Heterogeneous cost

Polity cost should remain vector-valued unless a scalar objective is declared. A representative bookkeeping vector is

\[
c_\Pi=(c_{coord},c_{mem},c_{tool},c_{human},c_{val}).
\]

Adding unlike units without a declared scalarization is not meaningful.

## 9. System-level claim boundary

A polity-level capability claim must name:

- the task distribution or task set;
- the component roles;
- the composition/routing rule;
- the memory semantics;
- the validation rule;
- the governance/authority rule;
- the measured success criterion.

Without these, 'the system can do X' is underspecified.

## 10. Downstream handoff

ATLAS-CH-SYNTHESIS-001 may inherit the polity object, state separation, capability/authority distinction, candidate-to-commit decomposition, cost vector, and exact two-specialist witness.

It must independently justify any broader thesis about intelligence beyond the monolithic model.

## Claim boundary

This packet proves only the displayed finite witness and the stated logical separations. It does not prove that multi-agent, human-agent, tool-using, or governed systems are universally superior to monolithic models.