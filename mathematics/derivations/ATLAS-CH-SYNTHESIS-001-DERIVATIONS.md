# ATLAS-CH-SYNTHESIS-001 — Derivation Packet

## D1. Finite task system

Let

\[
Q=\{\alpha,\beta\}.
\]

Define specialists:

\[
A_{\alpha}=(1,0),\qquad A_{\beta}=(0,1)
\]

on the ordered tasks \((\alpha,\beta)\).

The correct router is:

\[
R(\alpha)=A_{\alpha},\qquad R(\beta)=A_{\beta}.
\]

Hence routed answers are:

\[
y(\alpha)=1,\qquad y(\beta)=1.
\]

Therefore task accuracy is:

\[
\boxed{1}.
\]

## D2. Evidence and commit

Candidate:

\[
c=(q,y,s).
\]

Validator accepts iff:

\[
y=1
\]

and source \(s\) equals the declared specialist for task \(q\).

Governance commits iff validation accepts.

Thus both correct routed candidates commit as:

\[
(\alpha,1,A_{\alpha},\mathrm{validated}),
\]

\[
(\beta,1,A_{\beta},\mathrm{validated}).
\]

Validated commit coverage is:

\[
\boxed{1}.
\]

## D3. Persistent recall

Shared memory stores both records by task key.

Later recall returns:

\[
M[\alpha]=1,\qquad M[\beta]=1.
\]

Persistent recall coverage is:

\[
\boxed{1}.
\]

No rejected candidate is committed, so unauthorized commits are:

\[
\boxed{0}.
\]

## D4. Broken-router ablation

Let

\[
R'(\alpha)=A_{\alpha},\qquad R'(\beta)=A_{\alpha}.
\]

Then:

\[
y'(\alpha)=1,
\]

\[
y'(\beta)=0.
\]

The beta candidate fails validation.

Hence task accuracy and validated commit coverage are each:

\[
\boxed{\frac{1}{2}}.
\]

## D5. Remove-validator ablation

Keep correct routing and unchanged governance rule:

\[
\text{commit iff validator_accept=true}.
\]

If the validator/evidence channel is absent, no positive validation evidence exists.

Thus:

\[
\boxed{\text{authorized commit coverage}=0}
\]

even though transient answer accuracy can remain:

\[
\boxed{1}.
\]

Therefore:

\[
\boxed{
\text{answer capability}

\not\Rightarrow
\text{authorized durable state}.
}
\]

## D6. Remove-memory ablation

Keep routing, answer production, validation, and authorization.

Delete persistent shared memory.

Then immediate answer accuracy, positive validator decisions, and authorization all remain (1). No durable record is written, and later persistent recall coverage is:

\[
\boxed{0}.
\]

Therefore:

\[
\boxed{
\text{transient success}

\not\Rightarrow
\text{persistent shared recall}.
}
\]

## D7. Remove-governance ablation

Define an **externally injected forged candidate**, not the normal output of the deterministic specialist (which would produce \(A_\alpha(\beta)=0\)):

\[
c_{\mathrm{bad}}=(\beta,1,A_{\alpha}).
\]

It is correct-looking in value but wrong in source.

Validator result:

\[
V(c_{\mathrm{bad}})=0.
\]

With governance:

\[
\text{commit}=0.
\]

If governance is bypassed:

\[
\text{commit}=1.
\]

Thus unauthorized commits increase from (0) to (1).

Therefore:

\[
\boxed{
\text{content correctness alone}

\not\Rightarrow
\text{authorized transition}.
}
\]

## D8. Capability is composition-relative

The same specialist set:

\[
\{A_{\alpha},A_{\beta}\}
\]

appears in the full system and broken-router ablation.

Yet task accuracy changes from:

\[
1
\]

to:

\[
\frac{1}{2}.
\]

Hence:

\[
\boxed{
\text{component set}

\not\Rightarrow
\text{system capability}.
}
\]

The composition rule matters.

## D9. Typed metrics

The witness tracks distinct quantities:

- immediate answer accuracy;
- positive validator decisions;
- governance authorization decisions;
- durable validated records actually written;
- later validated recall;
- writes rejected by the nominal validator gate.

An authorized candidate may lack a durable record when memory is absent; an accurate transient answer may lack positive validation evidence.

They cannot be replaced by one scalar without a declared objective.

## D10. Status preservation

FRONTIER's status grammar contains seven categories. SYNTHESIS does not alter them.

An item in OPEN_PROOF_OBLIGATION remains open until separately discharged.

An item in OPEN_EXPERIMENT_OBLIGATION remains open until separately completed and adjudicated.

A CONJECTURAL_CONNECTION does not become substrate through narrative synthesis.

## D11. Cost boundary

Let:

\[
K=(c_{\mathrm{coord}},c_{\mathrm{mem}},c_{\mathrm{tool}},c_{\mathrm{human}},c_{\mathrm{val}}).
\]

The witness proves no dominance relation between architectures under this heterogeneous cost vector.

A scalar comparison requires a declared scalarization.

## Durable propositions

1. The full declared composition attains exact task, validated-commit, and persistent-recall coverage.
2. A broken router reduces task and commit coverage to one half.
3. Removing validation while preserving governance can leave answer accuracy intact while reducing authorized commits to zero.
4. Removing memory destroys persistent recall without necessarily affecting immediate answers.
5. Under the explicitly declared adversarial-injection threat model, bypassing governance can admit a validator-rejected bad-source commit.
6. Component count does not determine composition quality.
7. Capability, authority, evidence, governance, memory persistence, and cost are distinct.
8. Open FRONTIER obligations remain open.

## Claim boundary

This packet proves only the finite declared composition and ablations. It does not prove that distributed architectures are universally better, that any validator is an oracle, that shared memory is always beneficial, that governance guarantees truth, or that the Atlas has solved its open research programmes.
