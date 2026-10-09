# ATLAS-CW-REPLAY-001 — Replayable Evidence Object Witness

**Chapter:** \`ATLAS-CH-REPLAY-001\`  
**Figure:** \`ATLAS-FIG-REPLAY-001\`  
**Source lock:** \`sources/source-locks/ATLAS-CH-REPLAY-001.yaml\`

## Purpose

Provide one actual deterministic replay package and bind it to the chapter's documentary claim:

> replayability is a property of an evidence path, not a synonym for truth, proof, certification, or authority.

## Deterministic replay package

Program:

\`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.py\`

Expected output:

\`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.expected\`

Identity manifest:

\`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.manifest.json\`

The program uses Python standard-library exact rational arithmetic to compute

\[
\frac13+\frac16+\frac12.
\]

The locked standard output is exactly:

\[
\boxed{\texttt{1/1}}
\]

followed by one ASCII LF byte (0x0A), not an operating-system-dependent
text-mode newline.

The replay script writes the explicitly encoded bytes to stdout's binary
buffer. On Windows, text-mode print output would ordinarily yield CRLF
(0x0D 0x0A), failing the locked LF-byte comparison despite correct arithmetic.
The binary-output contract removes that environmental ambiguity without
normalizing or weakening the replay check.

## Content identities

Program SHA-256:

\`f21d6b4e38da3600e584f5dbcff0406a3f51af08b0f6d1b654fa3fff54352257\`

Expected-output SHA-256:

\`3117b181de4d46b7ff8adb4c78adec272c019160d4adf27a901e90ec114e1845\`

The hashes were independently recomputed from the exact committed text before this witness record was written.

## Execution contract

Invocation:

\`python mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.py\`

Environment class:

- Python 3.11 or later;
- standard library only;
- \`fractions.Fraction\`;
- no network access;
- no mutable external data.

Atlas CI performs four checks:

1. the replay manifest exists;
2. the committed program SHA-256 matches the manifest;
3. the committed expected-output SHA-256 matches the manifest;
4. executing the program under the CI Python runtime produces byte-exact standard output equal to the locked expected output.

This is intentionally small enough that the replay obligation itself is inspectable.

## Why this does not prove much

The computation is mathematically trivial.

That is deliberate.

The witness proves that the **evidence-path mechanism** works on one deterministic object. It is not intended to impress by mathematical difficulty.

A perfectly replayable program can still implement the wrong mathematical object.

## Mutable-dependency failure mode

A dependency named only by a mutable identifier such as

\`model/latest\`

can change while its name remains stable.

A replay record that binds only the name therefore lacks strong object identity.

A content digest or immutable revision fixes the byte identity, but still does not prove semantic relevance.

## Seed-only failure mode

For stochastic work, a random seed is useful but need not determine the result by itself.

Replay may also depend on:

- PRNG implementation;
- software versions;
- accelerator kernels;
- reduction order;
- numerical precision;
- compiler/runtime details;
- external data state.

Therefore seed plus code is not automatically a complete replay identity.

## Semantic-bridge failure mode

Suppose a byte-exact program verifies a property for every integer

\[
1\le n\le100.
\]

If the accompanying prose states that the property holds for **all** positive integers, the replay can be perfect while the claim is false or unsupported.

The failed object is the bridge between the observation and the human claim.

This is why the Atlas evidence object binds claim identity and interpretation in addition to source/code/output identities.

## Current GCL lifecycle evidence

The source lock binds the current GCL OPENMATH lifecycle controller at:

- repository: \`grandchallenge/MATH-PROGRAMME\`;
- commit: \`9c09521f0f7b1b7bbb2830b42f097f227f209d7d\`;
- path: \`governance/openmath_unattended_lifecycle_controller.json\`;
- Git blob: \`72c5b7ee3ba2e586af14d09a42c0898fe5f20f96\`.

That controller records the lifecycle

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

It separately records the authority boundary

\[
\texttt{MATHFORGE\_TO\_MATHSOLVE\_TO\_MATHCERT}
\]

and explicitly prohibits the controller from performing MATHCERT certification or claiming mathematical correctness beyond Solve adjudication.

A current MATHCERT OPENMATH intake at commit

\`8a2610215989bec15474f0a088945c0a1b6d8172\`

records source locks, proof receipts, search receipts, and a replay receipt while still recording

\[
\texttt{certification\_effect:false}.
\]

This is direct documentary evidence that GCL treats replay evidence and certification state as different objects.

## Figure provenance

Source:

\`figures/wolfram/ATLAS-FIG-REPLAY-001.wl\`

Source Git blob SHA-1:

\`661508536ce7d9ef2a62c6fa2bd4a311223edca3\`

Rendered master:

\`figures/masters/ATLAS-FIG-REPLAY-001.png\`

Rendered Git blob SHA-1:

\`5a62f3b3341b9d9ff575cbfff644d330c6125701\`

Rendered size:

\`26,170 bytes\`

Every node and directed edge is declared in the figure manifest. Layout and grayscale do not encode epistemic strength.

## Claim boundary

The witness establishes:

- one byte- and hash-bound deterministic replay;
- explicit code/output/environment identity for that replay;
- source-locked current GCL examples separating replay, adjudication, certification, and authority;
- an exact provenance/authority graph.

It does not establish:

- truth of an arbitrary claim;
- independent replication;
- formal verification;
- MATHCERT certification;
- institutional authority merely because CI is green.
