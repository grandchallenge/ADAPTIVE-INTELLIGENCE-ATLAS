# Chapter Specification — ATLAS-CH-TRANSFER-001

## Identity

**Title:** Reconstruction and Transfer  
**Part:** Representation Learning  
**Status:** specification-ready.  
**Epistemic class:** established transfer-learning framework + Atlas reconstruction synthesis.

## Chapter contract

Connect transfer learning to the Residual programme by treating transfer as a reconstruction question across changes of task, domain, or representation.

The chapter must distinguish:

- source-task performance from transferability;
- parameter reuse from capability transfer;
- exact representation recoding from lossy transfer;
- task-specific sufficiency from task-family sufficiency;
- positive transfer from negative transfer;
- a sufficient reconstruction certificate from a complete theory of transfer.

## Dependency contract

Hard prerequisites:

- \`ATLAS-CH-RESIDUAL-001\`;
- \`ATLAS-CH-INFO-001\`.

Inherited:

- \`ATLAS-CH-REP-001\`;
- \`ATLAS-CH-QUOTIENT-001\`.

## Reader outcome

A reader should be able to:

1. state source/target domain and task distinctions;
2. define transfer operationally relative to a target objective/baseline;
3. distinguish feature reuse, parameter initialization, adaptation, and exact capability reconstruction;
4. state and prove the Atlas common-Residual reconstruction certificate;
5. show when a lossy bottleneck destroys transfer for a task family;
6. explain why one-task sufficiency need not imply multi-task transferability;
7. explain negative transfer without assuming transfer always helps;
8. separate semantic transferability from optimization/adaptation difficulty.

## Standard transfer framing

Following [@PanYang2010], distinguish a domain

\[
\mathcal D=(\mathcal X,P(X))
\]

from a task

\[
\mathcal T=(\mathcal Y,f).
\]

Use this only as a standard framing; later examples may work with deterministic finite capability maps.

## Atlas reconstruction certificate

Let:

- \(E_s:X\to Z_s\) be a source representation;
- \(E_t:X\to Z_t\) be a target representation;
- \(R:X\to\mathcal R\) be an admissible common Residual;
- \(C_s:Z_s\to\mathcal R\) and \(C_t:Z_t\to\mathcal R\) be compilers;
- \(\mathcal Q_t\) be target capability probes;
- \(D_q:\mathcal R\to\mathcal Y_q\) be target decoders.

If

\[
C_s(E_s(x))
=
C_t(E_t(x))
=
R(x)
\]

for every declared state \(x\), and

\[
B_t(x,q)
=
D_q(R(x))
\]

for every target probe \(q\), then both representations are sufficient for exact reconstruction of the declared target capability family through the common Residual.

This is a sufficient certificate.

It is not claimed necessary.

## Exact witness

Let latent transferable structure be

\[
r=
\begin{pmatrix}
a\\
b
\end{pmatrix}.
\]

Source representation:

\[
z_s
=
A_s r,
\qquad
A_s=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Target representation:

\[
z_t
=
A_t r,
\qquad
A_t=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

Use

\[
C_s=A_s^{-1},
\qquad
C_t=A_t^{-1}.
\]

Target tasks:

\[
D_1(r)=a+b,
\]

\[
D_2(r)=2a-b.
\]

For

\[
r=(3,1),
\]

verify both source and target representations reconstruct

\[
D_1=4,
\qquad
D_2=5.
\]

## Lossy bottleneck counterexample

Let

\[
P(r)=a.
\]

Then states

\[
r_A=(1,0),
\qquad
r_B=(1,1)
\]

have the same bottleneck value,

\[
P(r_A)=P(r_B)=1,
\]

but task \(D_2\) differs:

\[
D_2(r_A)=2,
\qquad
D_2(r_B)=1.
\]

Therefore no deterministic decoder from \(P(r)\) alone can reconstruct \(D_2\) on both states.

The bottleneck is sufficient for tasks depending only on \(a\), but not for the declared two-task family.

## Principal pedagogical device

### Allegory: shipping a machine through a narrow doorway

A transferable system may be disassembled into a portable core and reconstructed on the other side.

Correspondence:

- source representation ↔ original assembly;
- compiler ↔ disassembly map;
- Residual ↔ portable core;
- target decoder ↔ reconstruction procedure;
- bottleneck ↔ doorway width.

Limit:

Transfer learning can involve optimization, distribution shift, finite data, and adaptation dynamics. Exact deterministic reconstruction is only one clean special case.

## Figure programme

### ATLAS-FIG-TRANSFER-001

Two panels:

1. two different representations compiling to one common Residual and then branching into two target tasks;
2. a lossy one-dimensional bottleneck merging two states required to produce different target outputs.

Representation class: schematic with exact matrices/outputs.

## External evidence scope

Use:

- Pan–Yang for source/target domain-task taxonomy and negative transfer;
- Yosinski et al. for empirical layer/task dependence of feature transferability;
- Kornblith et al. for the distinction between source-task performance, architecture, and transfer quality;
- Achille–Soatto and Information Bottleneck only as supporting sufficiency/compression perspectives.

## Failure boundaries

Include:

- source accuracy does not imply transfer quality;
- a one-task sufficient representation can fail for another task;
- invertible recoding preserves information but adaptation can still fail computationally;
- a lossy bottleneck can create irrecoverable target ambiguity;
- transfer benefit must be measured against a declared target baseline;
- negative transfer can arise even when some source structure is reusable.

## Downstream obligations

Supply a precise reconstruction/transfer language to:

- minimal curricula and reasoning bases;
- model interoperability;
- compression-as-discovery;
- shared memory;
- capability recovery after adaptation.

## Acceptance

The draft must:

- state standard source/target domain-task framing;
- prove the common-Residual reconstruction certificate;
- include exact invertible source/target recoding witness;
- include a lossy-bottleneck impossibility witness;
- define negative transfer operationally;
- keep empirical transfer claims source-scoped;
- avoid claiming a universal transfer representation;
- include source lock, witness, figure provenance, and falsification tests.
