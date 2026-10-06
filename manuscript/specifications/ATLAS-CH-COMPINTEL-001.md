# Chapter Specification — ATLAS-CH-COMPINTEL-001

## Identity

**Title:** Compression as Discovery and Intelligence Probe  
**Part:** Diagnostics, Robustness, and Compression  
**Status target:** draft-v0.1  
**Implementation issue:** #227  
**Protected baseline:** 21597e4f2bb7af5312dc9967417a60dc3d8dc0f5

## Hard prerequisites

- ATLAS-CH-COMPRESS-001 / AUDIT-042;
- ATLAS-CH-RESIDUAL-001 / AUDIT-006.

Exact prerequisite identities and external-source scope are frozen in sources/source-locks/ATLAS-CH-COMPINTEL-001.yaml.

The chapter may inherit from COMPRESS:

- declared-code discipline;
- separation of parameter count, storage bytes, entropy-coded length, and MDL-style codelength;
- exact-versus-lossy compression distinctions;
- requirement to pair compression ratio with retained behavior;
- mechanism separation among pruning, quantization, low rank, sharing, distillation, and coding.

The chapter may inherit from RESIDUAL:

- capability-relative sufficiency;
- admissible descriptor and post-processing classes;
- semantic versus operational recoverability;
- nonuniqueness and recoding boundaries.

The chapter may not inherit or assert

\[
\text{compressible}\Rightarrow\text{intelligent},
\]

\[
\text{short code}\Rightarrow\text{mechanistic explanation},
\]

or

\[
\text{compression progress}\Rightarrow\text{discovery}
\]

without an explicit operational test and controls.

## Governing question

When can a reduction in description length be used as evidence that a system has captured reusable predictive structure rather than merely exploited a codec, memorized examples, changed task behavior, or benefited from probe capacity?

## Core objects

Let:

- \(R\) be a representation or model state to be probed;
- \(T\) be a training partition;
- \(H\) be an untouched held-out partition;
- \(Y_T,Y_H\) be declared targets;
- \(C\) be a declared code family;
- \(\mathcal P\) be the admissible probe/decoder class;
- \(L_C(Y_H\mid R,T)\) be held-out codelength.

Define

\[
\boxed{
\Delta_C(R)
=
L_C(Y_H\mid \text{baseline},T)
-
L_C(Y_H\mid R,T).
}
\]

Positive \(\Delta_C(R)\) means the representation permits shorter transmission of held-out targets than the declared baseline under the same code semantics.

This is evidence of exploitable predictive structure relative to

\[
(C,\mathcal P,T,H,\text{baseline}).
\]

It is not by itself evidence of a unique mechanism, unique Residual, causal necessity, general intelligence, or semantic understanding.

## Compression progress

Define

\[
\Gamma_t
=
L_{C,t-1}(Y_H\mid R,T)
-
L_{C,t}(Y_H\mid R,T).
\]

Positive \(\Gamma_t\) counts as progress only if the held-out target is unchanged, held-out labels do not leak into training, code semantics are fixed or charged explicitly, and model/probe side information is accounted for.

Schmidhuber's compression-progress proposal is a source-scoped hypothesis for curiosity/discovery, not an established identity.

## Evidence ladder

### Level 0 — training compression

The system compresses or predicts its training examples.

This can be caused by memorization.

### Level 1 — held-out compression

The system achieves positive held-out codelength gain relative to a declared baseline.

### Level 2 — control-separated held-out compression

The gain exceeds matched random-label, shuffled-alignment, random-representation, and probe-capacity controls.

### Level 3 — recoding-stable compression

The result survives declared admissible invertible representation changes, or any score change is explained by the restricted decoder class.

### Level 4 — reusable cross-context structure

The compressed descriptor or learned rule supports multiple declared probes, contexts, or tasks with low additional description cost.

### Level 5 — mechanistic evidence

A compressed component is perturbed, ablated, substituted, or reconstructed and the declared capability changes as predicted.

Compression alone does not reach this level.

## Mandatory controls

### Codec control

Repeat with at least one reasonable alternative code/probe implementation, or prove the relevant comparison invariant under admissible recoding.

### Random-label control

Replace \(Y\) with matched random labels.

### Shuffle control

Break alignment between representations and target examples while preserving marginal representation statistics.

### Random-representation control

Where applicable, compare against an untrained or random representation with the same interface.

### Memorization control

Require held-out savings. Training-only compression cannot distinguish reusable structure from lookup-table memorization.

### Probe-capacity / regularization control

Sweep or match probe class and regularization.

### Task-distortion control

Report target behavior alongside codelength. A shorter code obtained by destroying the target behavior is not evidence of retained reusable computation.

### Representation-change control

If the intended claim is representation-independent, apply admissible invertible recodings.

## Exact predictive witness

Use the fixed training prefix

\[
T=(0,1,0,1)
\]

and a four-bit held-out target.

The conditional codec \(C_{\mathrm{period2}}\) is:

- codeword 1 means the held-out four bits continue the period-two motif inferred from \(T\);
- codeword 0bbbb means transmit the four held-out bits literally.

The code is prefix-free.

For

\[
H_{\mathrm{structured}}=(0,1,0,1),
\]

\[
L_C(H_{\mathrm{structured}}\mid T)=1.
\]

Against a fixed four-bit literal baseline,

\[
L_0(H)=4,
\]

the held-out gain is

\[
\boxed{\Delta_C=3\text{ bits}.}
\]

For the matched control

\[
H_{\mathrm{control}}=(0,0,1,1),
\]

which shares the same training prefix but breaks the learned continuation,

\[
L_C(H_{\mathrm{control}}\mid T)=5,
\]

so

\[
\boxed{\Delta_C=-1\text{ bit}.}
\]

This demonstrates that identical training exposure can produce opposite held-out compression evidence.

It does not establish intelligence.

## Exact trivial-compressibility control

Use

\[
Z=(0,0,0,0,0,0,0,0).
\]

Define a prefix-free codec:

- codeword 1 means eight zeros;
- codeword 0bbbbbbbb means literal transmission.

Then

\[
L_C(Z)=1
\]

versus an eight-bit literal baseline.

The sequence is highly compressible under this code.

Nothing about this witness establishes learning, adaptation, abstraction, agency, or intelligence.

Therefore

\[
\boxed{
\text{compressibility}\not\Rightarrow\text{intelligence}.
}
\]

## Probe versus mechanism

A low codelength can show that a property is economically recoverable from \(R\).

It does not show that the original system used that property internally:

\[
\text{recoverable from representation}
\neq
\text{causally used by system}.
\]

Mechanistic claims require interventions or comparable causal evidence.

## Probe versus Residual

Suppose \(R_1\) and \(R_2\) are invertible recodings.

A probe class containing the inverse recoding may assign them equivalent operational content.

A restricted probe class may not.

Therefore codelength depends on both representation and decoder class.

A COMPINTEL result can support a Residual hypothesis only after the descriptor and post-processing class are declared.

## Primary-source roles

### Solomonoff

Use Solomonoff (1964) for the idealized induction link between shorter generating descriptions and prior weight/prediction.

Do not treat Solomonoff induction as a practical computable compressor.

### Blier and Ollivier

Use Blier and Ollivier (2018) for empirical description-length analysis of deep models and for the warning that coding method materially changes measured bounds.

Do not infer mechanism from short description length.

### Voita and Titov

Use Voita and Titov (2020) for MDL probing of learned representations and the use of random-task/random-representation baselines.

Do not universalize linguistic-probing results into a universal intelligence measure.

### Schmidhuber

Use Schmidhuber (2009) for the compression-progress hypothesis connecting learnable regularity to curiosity/discovery.

Label it as a proposed principle/hypothesis.

## Required derivations

The derivation packet must establish:

1. the codelength gain definition;
2. the exact period-two conditional-code witness;
3. the exact all-zero trivial-compressibility witness;
4. why training-only compression is compatible with memorization;
5. why codelength is codec-relative;
6. why invertible recoding can alter a restricted probe score without altering semantic capability;
7. why codelength savings and retained behavior are separate axes;
8. an evidence-ladder proposition separating probe, reuse, mechanism, and intelligence claims.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{training compression}\not\Rightarrow\text{generalization};
\]

\[
\text{held-out compression}\not\Rightarrow\text{mechanistic use};
\]

\[
\text{short description}\not\Rightarrow\text{unique explanation};
\]

\[
\text{compressibility}\not\Rightarrow\text{intelligence};
\]

\[
\text{compression progress}\not\Rightarrow\text{scientific discovery};
\]

\[
\text{probe accessibility}\not\Rightarrow\text{causal necessity};
\]

\[
\text{same task accuracy}\not\Rightarrow\text{same codelength};
\]

and

\[
\text{same codelength}\not\Rightarrow\text{same behavior}.
\]

## Practical protocol

A COMPINTEL experiment must declare:

- model checkpoint and representation object;
- target capability/property;
- training and untouched held-out partitions;
- code/probe family;
- model-side-information accounting;
- baseline;
- random-label control;
- shuffle control;
- random/untrained representation control when meaningful;
- probe-capacity sweep;
- retained behavior/task distortion;
- admissible recoding test when representation independence is claimed.

Primary quantities are

\[
L_C(Y_H\mid R,T),
\qquad
\Delta_C(R),
\qquad
\Gamma_t.
\]

## Downstream handoff

This chapter should provide reusable diagnostic language for mechanistic diagnosis, context/token compression, research strategy, adaptive curricula, agent exploration, and scientific-discovery systems.

No downstream chapter may promote codelength or compression progress to a definition of intelligence without an independent argument.

## Sources

- [@Solomonoff1964InductiveInferenceI]
- [@BlierOllivier2018DescriptionLength]
- [@VoitaTitov2020MDLProbing]
- [@Schmidhuber2009CompressionProgress]

Source lock: sources/source-locks/ATLAS-CH-COMPINTEL-001.yaml
