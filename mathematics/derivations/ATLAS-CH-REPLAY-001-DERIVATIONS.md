# ATLAS-CH-REPLAY-001 — Documentary Model and Replay Packet

**Status:** first-pass documentary derivation  
**Source lock:** \`sources/source-locks/ATLAS-CH-REPLAY-001.yaml\`

## D1. Provisional evidence object

The Atlas uses

\[
\boxed{
E=(C,S,M,A,O,I,R)
}
\]

as a bounded explanatory model.

- \(C\): exact claim identity and wording;
- \(S\): source identities;
- \(M\): method, derivation, code, or proof object;
- \(A\): execution environment and artifact identities;
- \(O\): observations or outputs;
- \(I\): interpretation and claim boundary;
- \(R\): review, replay, adjudication, or certification records.

This tuple is not asserted as a universal institutional schema.

Its purpose is to prevent the sentence “we reproduced it” from hiding which object was reproduced, under what conditions, and with what epistemic consequence.

## D2. Replayability is not truth

Let \(P\) be a deterministic program and let

\[
o=P(i)
\]

for locked input \(i\).

If another actor reconstructs the same program, input, environment, and execution and obtains the same output \(o\), then the computation is replayable under those conditions.

That does not imply that:

- the program implements the intended mathematics;
- the input corresponds to the intended source;
- the interpretation of \(o\) is correct;
- a finite computation proves a universal claim;
- an institution has certified the result.

Replay establishes reconstructability of a support path.

## D3. Tiny deterministic replay

The repository contains the program at

\[
\texttt{mathematics/computational-witnesses/replay\_examples/deterministic\_fraction\_sum.py}.
\]

Its complete content is SHA-256 bound in the companion manifest.

The program computes, using exact rational arithmetic,

\[
\frac13+\frac16+\frac12.
\]

The expected output is

\[
\boxed{1/1}.
\]

The code SHA-256 is

\[
\texttt{e6e841bfe975f283ab948c4f7f9bbbf5ba488d267fda36edc1b270d5dcd062c1},
\]

and the expected-output SHA-256 is

\[
\texttt{3117b181de4d46b7ff8adb4c78adec272c019160d4adf27a901e90ec114e1845}.
\]

Atlas CI executes the program, compares the bytes of standard output, and verifies these hashes.

This is a genuine replay object, but a deliberately trivial mathematical one.

## D4. A mutable dependency breaks identity

Suppose a replay instruction names a mutable object such as “model/latest”.

Even if the name remains unchanged, the bytes behind it may change.

A stable name is not a stable object identity.

A stronger replay record binds the relevant source or artifact by immutable revision or content digest.

This does not mean that hashes prove semantic correctness. A hash answers:

> Are these bytes the bytes we named?

It does not answer:

> Are these the right bytes for the mathematical claim?

## D5. A random seed is not a complete environment

For a stochastic computation, recording the seed is valuable but can be insufficient.

Results may also depend on:

- pseudorandom-number-generator implementation;
- library versions;
- nondeterministic accelerator kernels;
- parallel reduction order;
- precision;
- compiler/runtime behavior;
- external data state.

Hence

\[
\text{seed}+\text{code}
\]

is not automatically equal to

\[
\text{complete replay identity}.
\]

The necessary environment record depends on the sensitivity of the claim.

## D6. Byte identity and semantic identity differ

Assume a program exhaustively verifies a property for

\[
n\le100.
\]

The program, environment, output, and hashes may replay perfectly.

If the manuscript then states

> the property holds for all positive integers,

the semantic bridge is invalid.

The bytes can be exact while the claim is too strong.

Thus the evidence object must bind not only artifacts but also the exact claim \(C\) and interpretation \(I\).

## D7. Formal verification is another support route

A proof assistant can verify that a term inhabits a formal statement under a specific kernel and axiom environment.

This is stronger than ordinary computational replay for that formal statement.

But a formal proof of the wrong formalization does not establish the intended human claim.

The semantic bridge remains an explicit object of review.

## D8. Reproducibility and replication

The National Academies uses **reproducibility** for obtaining consistent computational results using the same data, computational steps, methods, code, and analysis conditions, and **replicability** for obtaining consistent results in a new study with new data [@NASEM2019Reproducibility].

The Atlas uses **replay** more narrowly for an identity-bound reconstruction of a specified evidence path.

The term is local to this monograph/GCL context and is not proposed as a replacement for broader scientific terminology.

## D9. Provenance graph

W3C PROV distinguishes entities, activities, agents, and derivation relations [@W3CPROVDM2013].

The Atlas figure specializes that general idea to a scientific support path:

\[
\text{source}
\to
\text{method}
\to
\text{execution}
\to
\text{observation}
\to
\text{interpretation}
\to
\text{claim}.
\]

Review and certification form separate edges/states rather than being inferred from the existence of the path.

## D10. GCL lifecycle example

The current GCL OPENMATH controller records the lifecycle

\[
\texttt{READY}
\to
\texttt{LAUNCHED}
\to
\texttt{RETURNED}
\to
\texttt{CAPTURED}
\to
\texttt{REPLAYED}
\to
\texttt{ADJUDICATED}
\to
\texttt{ADVANCED}.
\]

Its authority boundary is explicitly

\[
\texttt{MATHFORGE\_TO\_MATHSOLVE\_TO\_MATHCERT}.
\]

The controller explicitly prohibits itself from claiming mathematical correctness not established by Solve adjudication and from performing MATHCERT certification.

A current MATHCERT OPENMATH intake separately records

\[
\texttt{certification\_effect:false}
\]

even while source locks, proof receipts, search receipts, and replay receipts are present.

These exact records demonstrate the Atlas distinction:

\[
\boxed{
\text{evidence present}
\not\Rightarrow
\text{certification already granted}.
}
\]

## Claim boundary

This packet defines the Atlas evidence-object model, supplies one executable deterministic replay, and source-locks exact GCL examples of lifecycle and authority separation. It does not claim that GCL governance is universally optimal or that successful replay establishes truth, proof, independent reproduction, or certification.
