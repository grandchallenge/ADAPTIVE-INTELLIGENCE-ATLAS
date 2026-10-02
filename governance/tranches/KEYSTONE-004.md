# KEYSTONE-004 — Boundary Contracts + Replayable Evidence Objects

## Status

**Tranche state:** implemented on branch pending merge validation.

## Objective

Produce the final style-setting keystone pair:

- \`ATLAS-CH-BCONTRACT-001\` — Boundary Contracts;
- \`ATLAS-CH-REPLAY-001\` — Replayable Evidence Objects.

## Baseline

- AUDIT-002 merge: \`25598441a2d58b8e432edbf185c971f6f30628d2\`;
- work issue: \`#11\`.

## A. Boundary Contracts

### Source lock

External sources bind:

- Baydin et al. 2018 for automatic differentiation and JVP/VJP mechanics;
- Higham 2002 for conditioning, perturbation, and numerical stability;
- Curry 2013 for local-to-global/sheaf compatibility language.

### Exact public GCL project-state boundary

The current public \`grandchallenge/MODULUS\` tree was inspected at:

\`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`.

The tree contains typed contract machinery, including:

- \`modulus/online/contracts.py\`;
- Git blob \`33b8c325203adc7a54a5b8b3ad4e0db6092af51d\`;
- public object \`RegretContract\`.

The names:

- \`BoundaryContract\`;
- \`SeparatorCompiler\`;
- \`Modula\`

were not found in the inspected public tree or searchable MODULUS commit history.

Therefore the chapter does not attribute those remembered research extensions to current public code. They remain Atlas/GCL programme context only.

### Atlas-owned mathematics

The chapter and derivation packet define the provisional explanatory object

\[
C_f=(\mathcal X,\mathcal Y,\Sigma,\mathcal I,\mathcal S,\mathcal E)
\]

with separate semantic, geometric, differential, and numerical obligations.

Exact witnesses include:

- shape-compatible but semantically incompatible normalization/magnitude composition;
- chain-rule Jacobian for two linear modules;
- exact JVP and VJP;
- exact spectral norm
  \[
  \sqrt{\frac{21+\sqrt{185}}8}
  =
  2.079707626949502\ldots;
  \]
- power-iteration convergence to the exact dominant singular value;
- separator-variable insufficiency example.

### Figure

\`ATLAS-FIG-BCONTRACT-001\`

- Wolfram source: \`figures/wolfram/ATLAS-FIG-BCONTRACT-001.wl\`;
- source Git blob: \`e064df23ccea715198fe91f9e20a817fb59302e9\`;
- rendered master: \`figures/masters/ATLAS-FIG-BCONTRACT-001.png\`;
- rendered Git blob: \`e3106af2b200823fb3b2cb699e8436a7fc89d0b8\`;
- rendered size: 48,873 bytes;
- Wolfram runtime: 15.0.1 for Linux x86 (64-bit), July 2 2026.

The right panel is literal for the exact sensitivity map; the left panel is schematic.

## B. Replayable Evidence Objects

### Source lock

External sources bind:

- National Academies 2019 for reproducibility/replicability terminology;
- Sandve et al. 2013 for computational-reproducibility practices;
- W3C PROV-DM for general provenance concepts.

Exact GCL sources bind:

- current technical-writing reference;
- current OPENMATH unattended lifecycle controller;
- a concrete replay-closure handoff;
- a current MATHCERT OPENMATH intake.

### Provisional evidence object

The chapter uses

\[
E=(C,S,M,A,O,I,R)
\]

for:

- claim identity;
- source identities;
- method;
- environment/artifacts;
- observations;
- interpretation/claim boundary;
- review/replay/adjudication/certification records.

The tuple is explicitly an Atlas explanatory model, not a universal institutional schema.

### Executable deterministic replay

Committed objects:

- \`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.py\`;
- \`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.expected\`;
- \`mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.manifest.json\`.

Program SHA-256:

\`e6e841bfe975f283ab948c4f7f9bbbf5ba488d267fda36edc1b270d5dcd062c1\`.

Expected-output SHA-256:

\`3117b181de4d46b7ff8adb4c78adec272c019160d4adf27a901e90ec114e1845\`.

Locked output:

\`1/1\\n\`.

Atlas CI is extended to:

1. verify the replay manifest;
2. verify program SHA-256;
3. verify expected-output SHA-256;
4. execute the program;
5. require byte-exact standard-output agreement.

### Documentary counterexamples

The chapter distinguishes:

- perfectly replayable wrong program;
- correct but weakly documented argument;
- mutable dependency;
- seed-only stochastic identity;
- byte-exact replay with invalid semantic bridge;
- formal proof of the wrong formalized statement;
- finite verification generalized beyond its domain;
- internal replay versus independent reproduction.

### Exact GCL authority separation

The source-locked OPENMATH controller records:

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

It separately records:

\[
\texttt{MATHFORGE\_TO\_MATHSOLVE\_TO\_MATHCERT}
\]

and explicitly prohibits controller-side MATHCERT certification.

The source-locked current MATHCERT intake records proof/search/replay evidence while still recording:

\[
\texttt{certification\_effect:false}.
\]

This is used only as a concrete GCL example of evidence/authority separation.

### Figure

\`ATLAS-FIG-REPLAY-001\`

- Wolfram source: \`figures/wolfram/ATLAS-FIG-REPLAY-001.wl\`;
- source Git blob: \`661508536ce7d9ef2a62c6fa2bd4a311223edca3\`;
- rendered master: \`figures/masters/ATLAS-FIG-REPLAY-001.png\`;
- rendered Git blob: \`5a62f3b3341b9d9ff575cbfff644d330c6125701\`;
- rendered size: 26,170 bytes;
- Wolfram runtime: 15.0.1 for Linux x86 (64-bit), July 2 2026.

All nodes and directed edges are declared by the manifest. Evidence/derivation edges and review/authority edges are visually distinct.

## Manuscript drafts

- \`manuscript/parts/07-numerical-intelligence-composition/ATLAS-CH-BCONTRACT-001.md\`;
- \`manuscript/parts/14-scientific-method-governed-adaptation/ATLAS-CH-REPLAY-001.md\`.

Both follow the Atlas style-setting pattern:

problem → bounded allegory → formal/documentary object → exact witness → figure → interpretation → failure boundary → downstream handoff.

## Promotion state

Both final keystone nodes are promoted to:

\`draft-v0.1\`.

This means the Atlas now has first complete drafts for all six keystone chapters.

It does not mean publication readiness or certification.

## Mandatory epistemic boundaries

This tranche preserves:

\[
\text{local boundary contract}
\not\Rightarrow
\text{global safety}.
\]

and

\[
\text{successful replay}
\not\Rightarrow
\text{truth}
\not\Rightarrow
\text{formal verification}
\not\Rightarrow
\text{certification}
\not\Rightarrow
\text{authority by implication}.
\]

These symbols indicate non-implication, not a universal ordering among the listed concepts.

## Next phase after merge

Run AUDIT-003 over the final pair and then perform one six-keystone synthesis pass before expanding into chapter-family drafting.

The synthesis pass should freeze:

1. the recurring chapter grammar;
2. notation and epistemic labels;
3. figure semantics;
4. source-lock requirements;
5. computational-witness requirements;
6. the boundary between established theory, Atlas synthesis, GCL research programme, and open question.
