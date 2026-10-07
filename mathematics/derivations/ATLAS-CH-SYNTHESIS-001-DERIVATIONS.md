# ATLAS-CH-SYNTHESIS-001 — Derivation Packet

## D1. Finite task system

Let

[
Q={alpha, eta}.
]

Define specialists:

[
A_alpha=(1,0),qquad A_ eta=(0,1)
]

on ordered tasks ((alpha, eta)).

The correct router is:

[
R(alpha)=A_alpha,qquad R( eta)=A_ eta.
]

Hence routed answers are:

[
y(alpha)=1,qquad y( eta)=1.
]

Therefore task accuracy is:

[
 oxed{1}.
]

## D2. Evidence and commit

Candidate:

[
c=(q,y,s).
]

Validator accepts iff:

[
y=1
]

and source (s) equals the declared specialist for (q).

Governance commits iff validation accepts.

Thus both correct routed candidates commit as:

[
(alpha,1,A_alpha,mathrm{validated}),
]

[
( eta,1,A_ eta,mathrm{validated}).
]

Validated commit coverage is:

[
 oxed{1}.
]

## D3. Persistent recall

Shared memory stores both records by task key.

Later recall returns:

[
M[alpha]=1,qquad M[ eta]=1.
]

Persistent recall coverage is:

[
 oxed{1}.
]

No rejected candidate is committed, so unauthorized commits are:

[
 oxed{0}.
]

## D4. Broken-router ablation

Let

[
R'(alpha)=A_alpha,qquad R'( eta)=A_alpha.
]

Then:

[
y'(alpha)=1,
]

[
y'( eta)=0.
]

The beta candidate fails validation.

Hence task accuracy and validated commit coverage are each:

[
 oxed{ rac12}.
]

## D5. Remove-validator ablation

Keep correct routing and unchanged governance rule:

[
 ext{commit iff validator_accept=true}.
]

If the validator/evidence channel is absent, no positive validation evidence exists.

Thus:

[
 oxed{ ext{authorized commit coverage}=0}
]

even though transient answer accuracy can remain:

[
 oxed{1}.
]

Therefore:

[
 oxed{
 ext{answer capability}

otRightarrow
 ext{authorized durable state}.
}
]

## D6. Remove-memory ablation

Keep routing, answer production, validation, and authorization.

Delete persistent shared memory.

Then immediate answer accuracy remains (1), but later persistent recall coverage is:

[
 oxed{0}.
]

Therefore:

[
 oxed{
 ext{transient success}

otRightarrow
 ext{persistent shared recall}.
}
]

## D7. Remove-governance ablation

Define bad candidate:

[
c_{mathrm{bad}}=( eta,1,A_alpha).
]

It is correct-looking in value but wrong in source.

Validator result:

[
V(c_{mathrm{bad}})=0.
]

With governance:

[
 ext{commit}=0.
]

If governance is bypassed:

[
 ext{commit}=1.
]

Thus unauthorized commits increase from (0) to (1).

Therefore:

[
 oxed{
 ext{content correctness alone}

otRightarrow
 ext{authorized transition}.
}
]

## D8. Capability is composition-relative

The same specialist set:

[
{A_alpha,A_ eta}
]

appears in the full system and broken-router ablation.

Yet task accuracy changes from:

[
1
]

to:

[
 rac12.
]

Hence:

[
 oxed{
 ext{component set}

otRightarrow
 ext{system capability}.
}
]

The composition rule matters.

## D9. Typed metrics

The witness tracks distinct quantities:

- answer accuracy;
- validated commit coverage;
- persistent recall coverage;
- unauthorized commit count.

They cannot be replaced by one scalar without a declared objective.

## D10. Status preservation

FRONTIER's status grammar contains seven categories. SYNTHESIS does not alter them.

An item in OPEN_PROOF_OBLIGATION remains open until separately discharged.

An item in OPEN_EXPERIMENT_OBLIGATION remains open until separately completed and adjudicated.

A CONJECTURAL_CONNECTION does not become substrate through narrative synthesis.

## D11. Cost boundary

Let:

[
K=(c_{mathrm{coord}},c_{mathrm{mem}},c_{mathrm{tool}},c_{mathrm{human}},c_{mathrm{val}}).
]

The witness proves no dominance relation between architectures under this heterogeneous cost vector.

A scalar comparison requires a declared scalarization.

## Durable propositions

1. The full declared composition attains exact task, validated-commit, and persistent-recall coverage.
2. A broken router reduces task and commit coverage to one half.
3. Removing validation while preserving governance can leave answer accuracy intact while reducing authorized commits to zero.
4. Removing memory destroys persistent recall without necessarily affecting immediate answers.
5. Removing governance can admit a validator-rejected bad-source commit.
6. Component count does not determine composition quality.
7. Capability, authority, evidence, governance, memory persistence, and cost are distinct.
8. Open FRONTIER obligations remain open.

## Claim boundary

This packet proves only the finite declared composition and ablations. It does not prove that distributed architectures are universally better, that any validator is an oracle, that shared memory is always beneficial, that governance guarantees truth, or that the Atlas has solved its open research programmes.
