# ATLAS-CH-COMPINTEL-001 — Derivation Packet

## Scope

This packet formalizes when compression can serve as evidence of predictive structure and when it cannot.

It does not define intelligence by compression, does not identify codelength with mechanistic explanation, and does not convert a probing result into a causal claim.

## D1. Held-out codelength gain

Let \(R\) be a representation, \(T\) a training partition, \(H\) a held-out partition, \(C\) a declared code family, and \(\mathcal P\) the admissible decoder/probe class.

Define

\[
L_C(Y_H\mid R,T)
\]

as the held-out target codelength after fitting only on \(T\).

Let \(B\) be a baseline representation or code.

Define

\[
\Delta_C(R)
=
L_C(Y_H\mid B,T)
-
L_C(Y_H\mid R,T).
\]

Then:

- \(\Delta_C>0\): \(R\) supports shorter held-out coding than \(B\);
- \(\Delta_C=0\): no gain under this protocol;
- \(\Delta_C<0\): the declared representation/probe is worse than baseline.

This statement is relative to \(C,\mathcal P,T,H,B\).

## D2. Compression progress

At stage \(t\), define

\[
\Gamma_t
=
L_{C,t-1}(Y_H\mid R,T)
-
L_{C,t}(Y_H\mid R,T).
\]

A positive \(\Gamma_t\) can only be interpreted as learned progress if the target, held-out set, and coding semantics are fixed or any changes are explicitly charged.

Otherwise the score can improve through bookkeeping alone.

## D3. Exact conditional period-two codec

Fix

\[
T=(0,1,0,1).
\]

The decoder infers the period-two motif \((0,1)\) from \(T\).

Define a prefix-free conditional code for four held-out bits:

- word \(1\): continue the inferred motif for four bits;
- word \(0b_1b_2b_3b_4\): literal fallback.

No codeword beginning with \(0\) can have the one-bit word \(1\) as prefix, and the literal branch has fixed length.

For

\[
H_s=(0,1,0,1),
\]

the first branch applies, so

\[
L_C(H_s\mid T)=1.
\]

Against a four-bit literal baseline,

\[
L_0(H_s)=4.
\]

Thus

\[
\boxed{\Delta_C(H_s)=3.}
\]

Now choose

\[
H_c=(0,0,1,1).
\]

It does not continue the inferred motif, so the fallback uses

\[
1+4=5
\]

bits.

Hence

\[
\boxed{\Delta_C(H_c)=4-5=-1.}
\]

The training prefix is identical in both cases.

Therefore the difference is held-out structure, not different training exposure.

## D4. Training compression does not imply held-out compression

Let a memorizer store all labels in \(T\).

It can attain zero training error.

If held-out examples are unseen and no rule relating their inputs to labels has been learned, the memorizer has no basis for reducing held-out codelength relative to a literal or frequency baseline.

Thus there exist systems with perfect training fit but

\[
\Delta_C(R)\le 0
\]

on held-out data.

Therefore

\[
\boxed{
\text{training compression}
\not\Rightarrow
\text{held-out predictive compression}.
}
\]

## D5. Exact trivial-compressibility witness

Let

\[
Z=(0,0,0,0,0,0,0,0).
\]

Define a prefix-free code:

- \(1\): eight zeros;
- \(0b_1\ldots b_8\): literal sequence.

Then

\[
L_C(Z)=1.
\]

A literal baseline requires eight bits.

So the compression gain is seven bits.

But the sequence can be generated without learning, representation, adaptation, agency, or task competence.

Hence

\[
\boxed{
\text{compressibility}
\not\Rightarrow
\text{intelligence}.
}
\]

## D6. Codec relativity

Let \(D\) be any fixed data object.

Two valid prefix codes \(C_1,C_2\) may assign different lengths:

\[
L_{C_1}(D)\ne L_{C_2}(D).
\]

For the all-zero witness, a special run code gives one bit, while a fixed literal code gives eight bits.

Therefore a finite codelength claim is incomplete without the code family.

This does not make compression arbitrary.

It means comparison discipline must hold the relevant coding semantics fixed or explicitly compare reasonable alternatives.

## D7. Codelength versus behavior

Let \(f\) be a model and \(Q(f)\) a declared behavioral quality.

Let \(L(f)\) be a codelength.

The pair

\[
(L(f),Q(f))
\]

contains more information than either coordinate alone.

There may exist \(f_1,f_2\) such that

\[
L(f_1)<L(f_2)
\]

but

\[
Q(f_1)<Q(f_2).
\]

Thus shorter description does not order models by retained capability unless the distortion/behavior constraint is included.

## D8. Same accuracy, different codelength

Suppose two probes both eventually achieve perfect held-out classification.

Probe \(P_1\) learns the rule from few training examples.

Probe \(P_2\) needs many examples.

A prequential/online code charges predictive losses over the learning sequence.

Therefore their final accuracies can match while their cumulative codelengths differ.

This is the operational distinction emphasized by MDL probing.

Thus

\[
\text{same final accuracy}
\not\Rightarrow
\text{same codelength}.
\]

## D9. Same codelength, different behavior

Codelength is a scalar summary.

Distinct models can receive equal total codelength while making different individual predictions or exhibiting different calibration.

Therefore

\[
\text{same codelength}
\not\Rightarrow
\text{same behavior}.
\]

Task-level diagnostics remain separately necessary.

## D10. Invertible recoding and probe-class dependence

Let

\[
R_2=g(R_1)
\]

for invertible \(g\).

Semantically, \(R_1\) and \(R_2\) contain the same information.

If the admissible decoder class \(\mathcal P\) contains composition with \(g^{-1}\), then every decoder \(p\) for \(R_1\) corresponds to

\[
p\circ g^{-1}
\]

for \(R_2\).

Under a recoding-invariant accounting scheme, the optimal operational content can therefore match.

But if \(\mathcal P\) excludes \(g^{-1}\), the measured codelength can change.

Hence a probe score is a property of

\[
(R,\mathcal P,C),
\]

not of \(R\) alone.

## D11. Probe accessibility is not causal use

Suppose a probe \(p\) decodes target \(Y\) from representation \(R\).

This establishes an existence statement:

\[
Y\approx p(R).
\]

It does not establish that the original system's downstream computation uses \(p\), uses the decoded property, or depends causally on the relevant coordinates.

To establish causal use, one needs intervention evidence such as:

- ablation;
- activation patching;
- substitution;
- controlled reconstruction;
- causal mediation or equivalent tests.

Therefore

\[
\boxed{
\text{probe accessibility}
\not\Rightarrow
\text{causal use}.
}
\]

## D12. Reuse criterion

A stronger reuse test uses multiple contexts \(q\in\mathcal Q\).

Let a descriptor \(Z=R(X)\) be transmitted once.

For tasks \(Y^{(1)},\ldots,Y^{(m)}\), define incremental task-specific description costs

\[
\ell_j
=
L_C(Y_H^{(j)}\mid Z,T_j).
\]

A reusable descriptor should support low total incremental cost

\[
\sum_{j=1}^m \ell_j
\]

relative to task-specific baselines, while preserving declared behavior.

This is evidence of shared predictive structure.

It is still relative to the task family and code.

## D13. Relation to the Residual

The Residual chapter asks for a least admissible descriptor sufficient for a declared capability under a declared factorization preorder.

COMPINTEL can generate evidence that one descriptor is economical.

It does not prove leastness.

In particular,

\[
L_C(R_1)<L_C(R_2)
\]

under one code does not imply

\[
R_1\preceq R_2
\]

in the Residual factorization preorder.

Codelength and factorization order are different structures.

## D14. Compression progress as discovery hypothesis

The Schmidhuber proposal treats improvement in an observer's ability to predict/compress data as a signal of newly learned regularity.

An Atlas-compatible operationalization is:

\[
\Gamma_t>0
\]

on a fixed held-out target, accompanied by control separation.

A stronger discovery claim requires at least:

1. the new codelength gain occurs on held-out data;
2. it exceeds random-label and shuffle controls;
3. it persists under reasonable codec/probe variations;
4. it transfers to a second declared context or reduces future learning cost;
5. task behavior is preserved;
6. no leakage or side-information omission explains the gain.

This defines an experimental criterion.

It does not prove that all discovery is compression progress.

## D15. Evidence ladder proposition

The following implications are intentionally one-way:

\[
\text{training fit}
\;\not\Rightarrow\;
\text{held-out compression},
\]

\[
\text{held-out compression}
\;\not\Rightarrow\;
\text{control-separated structure},
\]

\[
\text{control-separated structure}
\;\not\Rightarrow\;
\text{representation-invariant structure},
\]

\[
\text{representation-invariant structure}
\;\not\Rightarrow\;
\text{cross-task reuse},
\]

\[
\text{cross-task reuse}
\;\not\Rightarrow\;
\text{causal mechanism},
\]

\[
\text{causal mechanism}
\;\not\Rightarrow\;
\text{general intelligence}.
\]

Each level requires additional evidence.

## D16. Durable propositions

1. Finite codelength is code-relative.
2. Held-out codelength is a stronger predictive-structure test than training codelength.
3. Random-label and shuffle controls distinguish target structure from generic fitting ability.
4. Probe capacity is part of the measurement apparatus.
5. Codelength and task behavior are separate axes.
6. Invertible recoding can change a restricted probe score without changing semantic information.
7. MDL probing measures economical recoverability, not causal use.
8. Compression progress can operationalize a discovery hypothesis when evaluated on fixed held-out data with controls.
9. Cross-task low incremental codelength is evidence of reuse relative to a declared task family.
10. No result in this packet establishes compression as a definition of intelligence.
