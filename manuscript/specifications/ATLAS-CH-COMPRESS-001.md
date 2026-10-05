# Chapter Specification — ATLAS-CH-COMPRESS-001

## Identity

**Title:** Compression and Description Length  
**Part:** Diagnostics and Structure  
**Status:** specification-ready.  
**Epistemic class:** audited information/representation prerequisites + classical compression sources + Atlas synthesis.

## Chapter contract

Develop compression as a family of distinct mechanisms and measurements:

- minimum description length;
- pruning;
- quantization;
- weight sharing;
- entropy coding;
- low-rank approximation;
- structured parameterizations;
- knowledge distillation.

The chapter must keep code length, parameter count, storage, task distortion, and mechanistic interpretation separate.

## Hard prerequisites

- ATLAS-CH-INFO-001
- ATLAS-CH-REP-001

## Description length

For a declared code C and data D, a two-part description objective has the form

L_C(M,D)
=
L_C(M)+L_C(D|M).

The code is part of the statement.

Raw parameter count is not automatically the same quantity as description length.

## Lossless and lossy compression

Lossless compression allows exact reconstruction of the coded object.

Lossy compression allows a declared distortion.

For a model, distortion may be measured in parameter error, output error, predictive loss, or another declared task metric.

These choices are not interchangeable.

## Exact equal-function / different-code witness

Let

W = 1_4 1_4^T,

the 4 by 4 all-ones matrix.

Then rank(W)=1 and

W = u v^T

with

u=v=(1,1,1,1)^T.

Under a declared binary payload codec with known 4 by 4 shape:

- dense representation stores 16 binary matrix entries;
- rank-1 factor representation stores 8 binary factor entries.

Thus the same exact linear map has payload lengths 16 bits and 8 bits under the declared formats.

If one-bit format tags are included, total lengths are 17 and 9 bits.

The witness demonstrates representation-dependent description length under an explicit code.

It does not claim a universal minimum code.

## Low-rank lossy control

Let

A=diag(4,3,1).

Its singular values are 4,3,1.

The best rank-1 approximation in Frobenius norm is

A_1=diag(4,0,0)

with squared error

||A-A_1||_F^2=10.

The best rank-2 approximation is

A_2=diag(4,3,0)

with squared error 1.

Low-rank compression is exact only when discarded singular values are zero.

## Pruning control

Let

w=(1,1/8)^T

and input

x=(0,8)^T.

Then

w^T x=1.

Prune the second weight by a magnitude threshold tau=1/4:

w_pruned=(1,0)^T.

Then

w_pruned^T x=0.

A small-magnitude weight can be functionally important on a declared input distribution.

Magnitude pruning is therefore an intervention with distortion risk, not a theorem of irrelevance.

## Quantization witness

Let

w=(1/4,1/2,1/2,1/4).

If the fixed quantization grid is

{0,1/4,1/2,3/4},

then all four weights are represented exactly by 2-bit indices.

Under comparison with four raw 8-bit values:

- raw payload: 32 bits;
- fixed-grid index payload: 8 bits.

Because the grid is fixed by the declared codec, no codebook overhead is charged in this witness.

A learned codebook would require its own storage accounting.

## Weight-sharing witness

For the same vector w, only two distinct values occur.

Under a declared codec storing:

- two 8-bit centroid values;
- four 1-bit centroid indices;

the payload is

16+4=20 bits,

versus 32 bits for four independent 8-bit values.

This is different from pruning: all four connections remain.

## Distillation boundary

A teacher defines target predictive behavior.

A student is trained to match that behavior under a declared distillation objective.

Distillation may yield a smaller deployable model, but it is not literal bit-level source coding of the teacher.

Teacher-student behavioral matching, parameter compression, and exact function preservation are separate claims.

## MDL toy witness

Declare two hypotheses H_A and H_B with code lengths

L(H_A)=3 bits,
L(H_B)=7 bits.

Suppose both assign the observed data the same conditional code length

L(D|H_A)=L(D|H_B)=5 bits.

Then

L(H_A,D)=8 bits,

L(H_B,D)=12 bits.

Under this declared code and equal data fit, the shorter model description wins.

The witness exists to show the two-part accounting, not to establish those code lengths universally.

## Structured transforms

Low rank and weight sharing are examples of structured parameterizations.

A structured transform reduces storage or degrees of freedom by constraining the admissible parameter family.

The structure must be declared.

Structured does not automatically mean lossless, interpretable, or computationally faster on every implementation.

## Failure boundaries

- parameter count != description length;
- storage bytes != entropy-coded length;
- lossless != lossy compression;
- pruning != quantization;
- quantization != weight sharing;
- low rank != sparsity;
- distillation != literal source coding;
- smaller model != same function;
- equal outputs on one dataset != global functional equivalence;
- compressibility != interpretability;
- compression ratio without distortion/task quality is incomplete.

## Downstream handoff

Direct consumer:

- ATLAS-CH-COMPINTEL-001.

COMPINTEL may inherit:

- declared-code discipline;
- exact-versus-lossy distinction;
- low-rank/pruning/quantization/sharing/distillation mechanism separation;
- requirement to pair compression ratio with retained behavior.

COMPINTEL must independently justify any claim that compression reveals reusable computation, mechanism, intelligence, abstraction, or discovery.

## Sources

- [@Rissanen1978MDL]
- [@EckartYoung1936]
- [@HanMaoDally2016DeepCompression]
- [@HintonVinyalsDean2015Distillation]

Source lock:

sources/source-locks/ATLAS-CH-COMPRESS-001.yaml
