# AUDIT-003 — Boundary Contracts + Replayable Evidence Objects

## Disposition

**PASS WITH ONE DOCUMENTARY REPAIR**

The final keystone pair is fit to remain at \`draft-v0.1\`.

This audit does not promote either chapter to publication-ready, certified, or final-copy status.

## Audited baseline

- KEYSTONE-004 merge: \`c380252b9440cfa665e1f24ce3ca0a7edf9ff8d1\`;
- audit issue: \`#13\`.

## 1. Boundary Contracts

### Provisional contract object

PASS.

The chapter defines

\[
C_f=
(\mathcal X,\mathcal Y,\Sigma,\mathcal I,\mathcal S,\mathcal E)
\]

as an Atlas explanatory object with separate:

- admissible input/output domains;
- semantic declaration;
- invariant/geometric obligations;
- sensitivity obligations;
- numerical/error obligations.

The manuscript explicitly states that this is not a universal contract standard.

### Shape-compatible semantic failure

PASS.

For

\[
f_{\rm dir}(x)=\frac{x}{\|x\|_2},
\qquad
g_{\rm mag}(y)=\|y\|_2,
\]

and

\[
x=(3,4),
\]

the input amplitude is \(5\), while

\[
g_{\rm mag}(f_{\rm dir}(x))=1.
\]

The dimensions compose; the semantics do not.

The example correctly establishes that shape compatibility is weaker than semantic compatibility.

### Chain-rule Jacobian

PASS.

For

\[
A=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix},
\]

the composed matrix is

\[
C=BA=
\begin{pmatrix}
2&1/2\\
0&1
\end{pmatrix}.
\]

The chapter's use of

\[
J_{g\circ f}=J_gJ_f
\]

is correct for the stated composition and reduces exactly to \(BA\) for the linear witness.

### JVP and VJP

PASS.

Independent Wolfram replay gives:

\[
C
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
\begin{pmatrix}
3/2\\
-1
\end{pmatrix},
\]

and

\[
C^\top
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
\begin{pmatrix}
2\\
3/2
\end{pmatrix}.
\]

The VJP convention is explicitly Euclidean.

### Exact singular values

PASS.

\[
C^\top C
=
\begin{pmatrix}
4&1\\
1&5/4
\end{pmatrix}
\]

has eigenvalues

\[
\frac{21\pm\sqrt{185}}8.
\]

Independent Wolfram replay gives singular values

\[
2.079707626949502346\ldots,
\qquad
0.961673638199607498\ldots.
\]

Thus

\[
\boxed{
\|C\|_2
=
\sqrt{\frac{21+\sqrt{185}}8}
=
2.079707626949502\ldots
}
\]

as stated.

### Power iteration

PASS.

Independent Wolfram replay from normalized \((1,1)\) gives dominant-singular-value estimates:

\[
1.9039432765,
\]

\[
2.0701070106,
\]

\[
2.0792647056,
\]

\[
2.0796873684,
\]

\[
2.0797067007,
\]

\[
2.0797075846,
\]

converging to the exact dominant singular value.

The chapter correctly states that the estimate has convergence conditions and does not become a global nonlinear bound by implication.

### Separator insufficiency

PASS.

The example

\[
s(y)=y_1
\]

with

\[
y=(0,1),
\qquad
y'=(0,2)
\]

correctly shows that a low-dimensional separator can identify states that remain operationally distinct for a downstream function depending on \(y_2\).

The manuscript asks the correct sufficiency question:

> sufficient for what?

### Local-to-global / sheaf scope

PASS.

Sheaf language is used as a compatibility/gluing lens, not as a claim that the Atlas contract object is itself a sheaf.

The manuscript explicitly blocks the inference:

\[
\text{local compatibility}
\not\Rightarrow
\text{global stability or safety}.
\]

### Public MODULUS source boundary

PASS.

The source lock pins current public MODULUS at:

\`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`.

The nearest bound public contract file is:

\`modulus/online/contracts.py\`

with Git blob:

\`33b8c325203adc7a54a5b8b3ad4e0db6092af51d\`.

Audit refetch confirms that file contains typed online-control contract machinery.

The source lock does **not** claim that this object is the Atlas BoundaryContract concept.

The remembered names:

- \`BoundaryContract\`;
- \`SeparatorCompiler\`;
- \`Modula\`

remain explicitly marked as absent from the inspected current public tree/searchable history and are not attributed as current public implementations.

### Figure provenance and semantics

PASS.

\`ATLAS-FIG-BCONTRACT-001\`:

- source Git blob: \`e064df23ccea715198fe91f9e20a817fb59302e9\`;
- rendered Git blob: \`e3106af2b200823fb3b2cb699e8436a7fc89d0b8\`;
- rendered size: 48,873 bytes.

The right panel is literal for the exact map \(C\); the left panel is explicitly schematic.

The alt text names both roles, so the figure does not rely on styling alone.

### Epistemic boundary

PASS.

No inspected text promotes:

\[
\text{local contract}
\]

to

\[
\text{global safety guarantee}.
\]

## 2. Replayable Evidence Objects

### Evidence-object semantics

PASS.

The chapter defines

\[
E=(C,S,M,A,O,I,R)
\]

with distinct fields for:

- exact claim;
- sources;
- method;
- environment/artifacts;
- observations;
- interpretation;
- review/replay/adjudication/certification state.

The manuscript repeatedly states that this is an Atlas explanatory model, not a universal institutional schema.

### Reproducibility and replicability terminology

PASS.

The National Academies terminology is used with the intended distinction between computational reproducibility and replication with new data.

The Atlas term **replay** is explicitly narrower and local to the Atlas/GCL context.

### Deterministic replay

PASS AFTER ONE MANIFEST REPAIR.

The committed replay program computes exactly:

\[
\frac13+\frac16+\frac12=1.
\]

The locked standard output is:

\`1/1\`

followed by one newline.

KEYSTONE-004 CI already verified:

- program SHA-256;
- expected-output SHA-256;
- successful execution;
- byte-exact output agreement.

The program SHA-256 remains:

\`e6e841bfe975f283ab948c4f7f9bbbf5ba488d267fda36edc1b270d5dcd062c1\`.

The expected-output SHA-256 remains:

\`3117b181de4d46b7ff8adb4c78adec272c019160d4adf27a901e90ec114e1845\`.

#### Repair made by this audit

The manifest's \`expected_stdout\` field encoded the literal characters backslash + \`n\` rather than the actual newline byte represented by the locked expected-output file.

Execution integrity was unaffected because CI compared against the expected-output file itself.

AUDIT-003 repaired the manifest field and strengthened \`tools/validate_atlas.py\` so that:

\[
\text{manifest expected\_stdout bytes}
=
\text{locked expected-output bytes}
\]

is now a required invariant.

This closes the documentary inconsistency rather than merely noting it.

### Mutable-dependency caveat

PASS.

The chapter correctly distinguishes a stable name from a stable object identity.

It also correctly states that immutable byte identity does not establish semantic relevance.

### Seed-only caveat

PASS.

The chapter correctly notes that stochastic replay can depend on PRNG implementation, software versions, accelerator nondeterminism, reduction order, precision, runtime/compiler behavior, and mutable external data.

No claim is made that a seed alone guarantees reproducibility.

### Byte identity versus semantic identity

PASS.

The finite-domain example correctly shows that a byte-exact replay can support a bounded observation while failing to support an improperly generalized universal claim.

The chapter therefore keeps:

\[
O
\]

and

\[
I
\]

separate in the evidence object.

### Formal verification boundary

PASS.

The chapter correctly states that a machine-checked proof establishes its formal statement under a trust base; it does not automatically prove a different intended human statement if the semantic bridge is wrong.

### Internal replay versus independent reproduction

PASS.

The manuscript states that re-execution by the originating implementation is useful replay/regression evidence but does not become independent reproduction merely because it succeeded twice.

### Exact GCL lifecycle state

PASS.

Audit refetch of

\`grandchallenge/MATH-PROGRAMME@9c09521f0f7b1b7bbb2830b42f097f227f209d7d\`

at

\`governance/openmath_unattended_lifecycle_controller.json\`

reconfirms Git blob:

\`72c5b7ee3ba2e586af14d09a42c0898fe5f20f96\`

and lifecycle:

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

The same controller explicitly prohibits:

- claiming mathematical correctness not established by Solve adjudication;
- MATHCERT certification.

This supports the chapter's authority-separation example.

### MATHCERT certification state

PASS.

Audit refetch of

\`grandchallenge/MATHCERT@8a2610215989bec15474f0a088945c0a1b6d8172\`

at

\`evidence/openmath_2026/OM26-H1/INTAKE.json\`

reconfirms Git blob:

\`dbd2098d3891c9a0c5050993d8a82b736330c5f4\`

and:

\[
\boxed{\texttt{certification\_effect:false}}.
\]

The chapter therefore has a concrete documentary example in which evidence/replay records exist while certification remains false.

### Provenance figure

PASS.

\`ATLAS-FIG-REPLAY-001\`:

- source Git blob: \`661508536ce7d9ef2a62c6fa2bd4a311223edca3\`;
- rendered Git blob: \`5a62f3b3341b9d9ff575cbfff644d330c6125701\`;
- rendered size: 26,170 bytes.

The figure manifest declares:

- six evidence-path nodes;
- three review/authority nodes;
- five evidence edges;
- three authority edges.

The generator renders those exact node/edge classes.

Layout, grayscale, and spacing are explicitly non-semantic.

### Epistemic boundary

PASS.

The chapter maintains:

\[
\text{replay}
\neq
\text{truth}
\]

and does not collapse replay into formal verification, replication, adjudication, certification, or authority.

## 3. Cross-keystone integrity

PASS.

After KEYSTONE-004, the Chapter Ledger records:

- 80 chapters;
- 126 hard edges;
- 1 root;
- all 6 keystones at \`draft-v0.1\`;
- all 6 keystone figures at \`rendered-witness\`.

No keystone remains \`specification-ready\`.

The whole-tree Markdown control-character guard remains active.

Citation closure remains checked against the canonical bibliography.

The deterministic replay witness is now a live CI obligation.

## 4. Final disposition

**AUDIT-003 passes with one repaired documentary defect.**

No mathematical defect, public-source overclaim, figure-provenance mismatch, or epistemic promotion requiring further manuscript repair was found.

The final keystone pair remains:

\`draft-v0.1\`.

The six-keystone drafting programme is therefore complete at first-pass level.

## 5. Next substantive phase

Before expanding into chapter-family drafting, perform one **six-keystone synthesis pass**.

That pass should extract and freeze the common Atlas grammar established empirically by the six drafts:

1. chapter opening problem;
2. bounded allegory plus explicit limit;
3. formal/documentary object;
4. exact derivation or reconstruction;
5. computational witness;
6. figure with literal/nonliteral semantics;
7. counterexamples and failure boundaries;
8. downstream handoff;
9. source-lock and provenance obligations;
10. epistemic status and promotion rules.

The synthesis should also freeze notation and evidence labels shared across chapter families so later drafting inherits a tested grammar rather than six independent local conventions.
