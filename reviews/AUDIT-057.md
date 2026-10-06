# AUDIT-057 — Compression as Discovery and Intelligence Probe

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-COMPINTEL-001 remains at draft-v0.1.

The audit found no mathematical, epistemic, source-scope, dependency, citation, provenance, witness, or repository defect requiring repair.

No theorem certification, intelligence metric, mechanistic certification, or publication promotion is implied.

## Audited baseline

- implementation issue: #227
- implementation PR: #228
- exact green implementation head: b7818c9eb16749aa41ac20b200293e485946e845
- implementation GitHub Actions run: 37468502141
- implementation merge / audited protected baseline: d7f83f6e51d60cdb8edbc3ad8b9a1f16a47213b4
- audit issue: #229
- audit branch: audit/a229
- chapter: ATLAS-CH-COMPINTEL-001

Merged implementation artifact blobs:

- specification: f3143c5b63537696e327f15aa1ef041f3f075482
- derivation packet: a05602c16c82587170c5b57e44cc4c5033d89bac
- computational witness: fb6f398987666794ba7520d2045982421b6f58c6
- reader manuscript: e6396abb339b8ccc14d1cb54b9c89eb982937d1e
- source lock: fbd6948afb38648697f0173aa25fbbe6a32b76ba
- Chapter Ledger: 7d6e77ecd71ed76c1141a2fe39349e5dcdef8490
- Source Register: 7b17cc17785312012761626688bac44238c67af3
- bibliography: db440c3ea184780c4eb669609887dcc9ef6fac62
- transaction receipt: 62e4a4942bac5927dafbe6ab970347b6ca4eccae

## 1. Hard prerequisite identity

PASS.

COMPRESS-001 is bound at the audited exact identities:

- manuscript: e8db79df51b64cfd4d5ef6957d4d10313886b6f4
- source lock: 156cd6afe1a06b49d2761b54d32b586fe5d23cec
- AUDIT-042: 677efa90a2d606c0400b8e471465278d19857393

RESIDUAL-001 is bound at:

- manuscript: 02b0886a87e1e17c749e15349e14f43674c3d1ff
- source lock: 6e6a25c4b4e01475e68a6c616eefb6ba7b039341
- AUDIT-006: b24ef782bedfe76a4c52d832562a0dd29d2a64a9

The implementation does not import a stronger downstream claim as hidden authority.

## 2. Solomonoff source scope

PASS.

Ray J. Solomonoff, A Formal Theory of Inductive Inference. Part I, Information and Control 7(1), 1-22 (1964), DOI 10.1016/S0019-9958(64)90223-2, is used for the idealized induction connection in which sequence priors are related to lengths of inputs/programs for a universal machine.

The chapter explicitly blocks the invalid promotion from that ideal theory to a practical computable neural-network intelligence metric.

## 3. Blier-Ollivier source scope

PASS.

Léonard Blier and Yann Ollivier, The Description Length of Deep Learning Models, NeurIPS 2018, is used for empirical deep-model description-length analysis.

The source supports that deep models can achieve strong lossless compression values under declared coding methods and that coding methodology materially changes the measured bound.

The Atlas does not use the paper to claim that short codelength identifies mechanism, understanding, or intelligence.

## 4. Voita-Titov source scope

PASS.

Elena Voita and Ivan Titov, Information-Theoretic Probing with Minimum Description Length, EMNLP 2020, pages 183-196, DOI 10.18653/v1/2020.emnlp-main.14, is used for MDL probing of learned representations.

The implementation correctly inherits:

- conditional label codelength as a probe surface;
- sensitivity to sample efficiency/model effort beyond final accuracy;
- usefulness of random-task/random-representation baselines.

It does not universalize linguistic probing into a universal intelligence score.

## 5. Schmidhuber source scope

PASS.

Jürgen Schmidhuber, Driven by Compression Progress, Dagstuhl Seminar Proceedings 09291 (2009), DOI 10.4230/DagSemProc.09291.14, is used only as a source for the proposed compression-progress principle relating learned regularity to curiosity/discovery.

The chapter labels this as a proposal/hypothesis.

It does not claim that compression progress is necessary or sufficient for curiosity, creativity, scientific discovery, or intelligence.

## 6. Core held-out codelength definition

PASS.

The chapter defines

\[
L_C(Y_H\mid R,T)
\]

relative to:

- representation \(R\);
- training partition \(T\);
- untouched held-out partition \(H\);
- declared code family \(C\);
- admissible probe/decoder class.

This prevents a training-only score from being silently called predictive evidence.

## 7. Held-out compression gain

PASS.

The chapter defines

\[
\Delta_C(R)
=
L_C(Y_H\mid B,T)
-
L_C(Y_H\mid R,T)
\]

for declared baseline \(B\).

The sign interpretation is correct:

- positive: shorter held-out code than baseline;
- zero: no gain;
- negative: worse than baseline.

The manuscript states that this is evidence relative to the measurement system, not an intrinsic scalar property of intelligence.

## 8. Compression-progress definition

PASS.

The longitudinal quantity

\[
\Gamma_t
=
L_{C,t-1}(Y_H\mid R,T)
-
L_{C,t}(Y_H\mid R,T)
\]

is algebraically correct.

The chapter requires fixed or charged target/code semantics before interpreting positive \(\Gamma_t\) as learned progress.

This blocks bookkeeping improvements from being relabeled as discovery.

## 9. Exact conditional-code witness

PASS.

Training prefix:

\[
T=(0,1,0,1).
\]

The declared conditional prefix code uses:

- one-bit word 1 for exact continuation of the inferred period-two motif;
- five-bit word beginning with 0 for literal four-bit fallback.

The code is prefix-free.

For

\[
H_s=(0,1,0,1),
\]

the codelength is one bit.

Against a four-bit literal baseline,

\[
\Delta_C(H_s)=4-1=3.
\]

Independent exact replay confirms the arithmetic.

## 10. Matched held-out failure control

PASS.

With the same training prefix and

\[
H_c=(0,0,1,1),
\]

the motif continuation fails.

The fallback code uses five bits.

Therefore

\[
\Delta_C(H_c)=4-5=-1.
\]

This is a clean finite demonstration that identical training exposure can yield opposite held-out compression evidence.

## 11. Trivial-compressibility witness

PASS.

For

\[
Z=(0,0,0,0,0,0,0,0),
\]

the declared special run code uses one bit versus an eight-bit literal baseline.

Thus

\[
\Delta_C(Z)=7.
\]

The chapter uses this as an exact counterexample to the implication

\[
\text{compressibility}
\Rightarrow
\text{intelligence}.
\]

The inference is correctly blocked.

## 12. Memorization boundary

PASS.

The chapter correctly states that a lookup-table or sufficiently flexible system can fit training labels without reducing held-out codelength.

Therefore training fit/compression is not promoted to generalization or reusable structure.

## 13. Codec relativity

PASS.

Finite codelength is explicitly treated as \(L_C(D)\), not as an intrinsic code-free quantity.

The all-zero witness itself demonstrates that the same object can receive one bit under a special run code and eight bits under a literal code.

The chapter responds by requiring fixed code semantics or sensitivity analysis, not by claiming that compression is arbitrary.

## 14. Probe-capacity and regularization controls

PASS.

The probe is treated as part of the measuring apparatus.

The implementation requires matched or swept probe capacity/regularization and/or charged model complexity.

This is consistent with the MDL-probing source boundary.

## 15. Random-label, shuffle, and random-representation controls

PASS.

The chapter requires:

- matched random labels;
- broken representation-target alignment while preserving marginals;
- random/untrained representation baselines where meaningful.

These are correctly presented as empirical controls rather than mathematical guarantees.

## 16. Task-distortion boundary

PASS.

The chapter reports codelength and retained behavior as separate axes.

It explicitly rejects a compression result obtained by destroying the target behavior as evidence of retained reusable computation.

## 17. Invertible recoding boundary

PASS.

For invertible \(g\) with

\[
R_2=g(R_1),
\]

the chapter correctly notes that semantic information can be preserved while operational probe difficulty changes if the decoder class cannot express \(g^{-1}\).

Therefore the measurement is a property of representation, probe class, and code.

This is consistent with the audited RESIDUAL semantic-versus-operational factorization boundary.

## 18. Residual boundary

PASS.

The implementation does not infer the Residual factorization preorder from codelength ranking.

It explicitly blocks

\[
L_C(R_1)<L_C(R_2)
\Rightarrow
R_1\preceq R_2.
\]

A short descriptor under one code does not prove leastness under the declared admissible factorization class.

## 19. Accessibility versus causal use

PASS.

The chapter correctly distinguishes:

\[
\text{economically recoverable from }R
\]

from

\[
\text{causally used by the original system}.
\]

Mechanism claims are delegated to interventions such as ablation, substitution, patching, or controlled reconstruction.

No probe result is promoted to causal necessity.

## 20. Evidence ladder

PASS.

The staged ladder is logically disciplined:

1. training compression;
2. held-out compression;
3. control-separated held-out compression;
4. recoding-stable compression;
5. cross-context reuse;
6. mechanistic intervention.

The chapter states that each level requires additional evidence.

No level is equated with general intelligence.

## 21. Cross-context reuse

PASS.

Low incremental codelength across multiple declared tasks is used as evidence of reuse relative to the task family and code.

The chapter does not promote this to a universal abstraction theorem or least Residual.

## 22. Same-accuracy/different-codelength boundary

PASS.

The chapter correctly notes that prequential/MDL coding can distinguish probes that reach the same final accuracy at different learning rates/sample efficiencies.

Thus

\[
\text{same final accuracy}
\not\Rightarrow
\text{same codelength}.
\]

## 23. Same-codelength/different-behavior boundary

PASS.

Codelength is a scalar summary.

Equal total codelength does not imply equal pointwise predictions, calibration, robustness, or mechanism.

The non-implication is correct.

## 24. Citation and bibliography integrity

PASS.

Reader citation keys resolve for:

- Solomonoff1964InductiveInferenceI;
- BlierOllivier2018DescriptionLength;
- VoitaTitov2020MDLProbing;
- Schmidhuber2009CompressionProgress.

The Source Register points to the exact COMPINTEL source lock.

The source lock records both source role and claim boundary.

## 25. Repository integrity

PASS subject to audit-PR validation.

At protected implementation merge d7f83f6e51d60cdb8edbc3ad8b9a1f16a47213b4:

- chapter status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated in the Chapter Ledger;
- hard dependencies remain COMPRESS-001 and RESIDUAL-001;
- no governed figure is introduced;
- canonical protected-merge validation is green;
- implementation exact head b7818c9eb16749aa41ac20b200293e485946e845 passed GitHub Actions run 37468502141.

## Final disposition

AUDIT-057 passes with no repair.

The durable COMPINTEL layer is:

**declared code + untouched held-out target + conditional codelength + explicit baseline + matched controls + retained behavior + recoding discipline + intervention boundary, with compression treated as a probe of predictive structure rather than a definition of intelligence.**
