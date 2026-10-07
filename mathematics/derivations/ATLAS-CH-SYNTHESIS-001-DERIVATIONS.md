# ATLAS-CH-SYNTHESIS-001 — Derivation Packet

## Scope

This packet proves the finite composition and ablation witness used by SYNTHESIS-001. It does not establish a universal architecture of intelligence.

## D1. Specialists and routing

Let

\[
Q=\{\alpha,\beta\}.
\]

Define

\[
A_\alpha(\alpha)=1,\qquad A_\alpha(\beta)=0,
\]

\[
A_\beta(\alpha)=0,\qquad A_\beta(\beta)=1.
\]

With

\[
R(\alpha)=A_\alpha,\qquad R(\beta)=A_\beta,
\]

both routed answers equal \(1\). Therefore task accuracy is

\[
\boxed{1}.
\]

## D2. Validation, authorization, and memory

A candidate is

\[
c=(q,y,s).
\]

The validator accepts iff \(y=1\) and \(s\) is the declared specialist for \(q\).

Governance authorizes commit iff validation accepts.

Committed records are stored as

\[
m=(q,y,s,\mathrm{validated}).
\]

For the full composition:

\[
\boxed{
\text{task accuracy}
=
\text{validated commit coverage}
=
\text{persistent recall coverage}
=
1
}
\]

and unauthorized commits equal \(0\).

## D3. Broken-router ablation

Use

\[
R'(\alpha)=A_\alpha,\qquad R'(\beta)=A_\alpha.
\]

Then

\[
y'(\alpha)=1,\qquad y'(\beta)=0.
\]

The beta candidate fails validation, so task accuracy and validated commit coverage are

\[
\boxed{\frac12}.
\]

Thus

\[
\boxed{
\text{component set}\not\Rightarrow\text{system capability}.
}
\]

## D4. Validator ablation

Keep correct routing and the same governance rule, but remove the validator/evidence channel.

Correct transient answers can still be produced, so answer accuracy can remain \(1\).

However, governance has no positive validation evidence and therefore authorizes no durable commit:

\[
\boxed{
\text{authorized commit coverage}=0.
}
\]

Hence

\[
\boxed{
\text{answer capability}\not\Rightarrow\text{authorized durable state}.
}
\]

## D5. Memory ablation

Keep routing, validation, and authorization, but remove persistent shared memory.

Immediate answer accuracy can remain \(1\), while later recall coverage is

\[
\boxed{0}.
\]

Therefore

\[
\boxed{
\text{transient success}\not\Rightarrow\text{persistent shared recall}.
}
\]

## D6. Governance ablation

Consider

\[
c_{\mathrm{bad}}=(\beta,1,A_\alpha).
\]

The answer value is correct-looking but the source is wrong, so the validator rejects it.

With the authorization gate present, the candidate cannot commit.

If that gate is removed, the rejected candidate can be written.

Therefore

\[
\boxed{
\text{correct-looking content}\not\Rightarrow\text{authorized transition}.
}
\]

## D7. Typed metrics and costs

The witness tracks distinct objects:

- answer accuracy;
- validated commit coverage;
- persistent recall coverage;
- unauthorized commit count.

The cost vector remains

\[
K=(c_{\mathrm{coord}},c_{\mathrm{mem}},c_{\mathrm{tool}},c_{\mathrm{human}},c_{\mathrm{val}}).
\]

No scalar comparison follows without a declared scalarization.

## D8. Status preservation

SYNTHESIS preserves FRONTIER's categories:

- AUDIT_BOUND_SUBSTRATE;
- DRAFT_SUBSTRATE;
- BOUNDED_EVIDENCE;
- ARCHITECTURE_STAGE;
- OPEN_PROOF_OBLIGATION;
- OPEN_EXPERIMENT_OBLIGATION;
- CONJECTURAL_CONNECTION.

Open proof and experiment obligations remain open until separately discharged.

## Durable propositions

1. The full composition attains exact task, validated-commit, and persistent-recall coverage.
2. Broken routing reduces task and commit coverage to one half.
3. Validation can be necessary for governed durable state even when transient answers are correct.
4. Persistent memory is necessary for persistent recall in the declared system.
5. Removing the authorization gate can admit a validator-rejected record.
6. Component count does not determine composition quality.
7. Capability, authority, evidence, governance, memory, and cost are distinct.
8. Open FRONTIER obligations remain open.

## Claim boundary

This packet proves only the declared finite composition and ablations. It does not prove that distributed architectures are universally better, that validators are infallible, that shared memory is always beneficial, that governance guarantees truth, or that the Atlas has solved its open research programmes.
