# AUDIT-044 — The Machine Under the Mathematics

## Disposition

**PASS AFTER ONE SOURCE-METADATA REPAIR**

ATLAS-CH-HARDWARE-001 remains at draft-v0.1.

The implementation correctly separates mathematical work from physical execution cost; treats Roofline as an upper-bound diagnostic rather than a timing oracle; declares arithmetic intensity relative to a memory boundary; keeps CUDA execution/memory terminology vendor-scoped; distinguishes matrix algebra from specialized matrix-unit mapping; separates precision format from numerical accuracy; and keeps distributed/serving claims downstream in SYSTEMS-001.

The audit found one documentary precision issue: the living CUDA documents were identified by title, URL, and retrieval date but not pinned tightly enough to their current document metadata. The source lock now records:
- CUDA Programming Guide: last updated 2026-09-10;
- CUDA C++ Best Practices Guide: documentation version 13.4.

No mathematical, witness, reader-prose, dependency, or downstream-boundary reversal was required.

## Audited implementation

- implementation issue: #176
- implementation PR: #177
- implementation merge: 2960157b277b32b0f4a4b25df7009bc6db238136
- audit issue: #178
- audit branch: audit/hardware-178

## 1. Hard prerequisite

PASS.

The source lock binds the exact audited Linear Algebra substrate:
- manuscript blob: e7fcf56322f26d232d3a3043038d9850792b4bde
- source-lock blob: f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e
- Foundation audit blob: 948f76b3f86d27fa4830efc30d8ef0135134256e

AUDIT-004 explicitly includes ATLAS-CH-LINALG-001 among the audited Foundation reader-spine chapters.

## 2. Roofline source and algebra

PASS.

The chapter uses Williams, Waterman, and Patterson (2009), Communications of the ACM 52(4):65-76, DOI 10.1145/1498765.1498785.

The one-level bound is stated as

[
P le min(P_{max}, BI).
]

Arithmetic intensity is defined from declared work and bytes:

[
I_M=W/Q_M.
]

The memory-bound/compute-bound interpretation is explicitly model- and boundary-relative.

## 3. Exact traffic witness

PASS.

For a (2	imes2) product, the declared scalar convention counts:
- 8 multiplications;
- 4 additions;
- 12 FLOPs.

No-reuse traffic:
- 20 FP32 scalar transfers;
- 80 bytes;
- (I_A=12/80=0.15) FLOP/byte.

Perfect full-input-reuse traffic:
- 12 FP32 scalar transfers;
- 48 bytes;
- (I_B=12/48=0.25) FLOP/byte.

The intensity ratio is (5/3).

For the hypothetical machine (P_{max}=10) TFLOP/s and (B=1) TB/s, the bandwidth-side Roofline bounds are 0.15 and 0.25 TFLOP/s.

The witness is correctly labeled as accounting, not benchmarking.

## 4. CUDA source scope

PASS AFTER METADATA REPAIR.

The CUDA Programming Guide is used only for CUDA-scoped programming-model, memory-space, SIMT/warp, and matrix-operation claims.

The CUDA C++ Best Practices Guide is used only for CUDA-scoped bandwidth, memory-reuse, occupancy/resource, and floating-point precision guidance.

The chapter does not universalize CUDA's exact hierarchy or execution model to all accelerators.

## 5. Matrix/tensor hardware boundary

PASS.

The chapter blocks the inference that arbitrary mathematical matrix multiplication automatically reaches specialized matrix-unit peak throughput.

Supported shapes, types, layouts, synchronization, data movement, and surrounding work remain relevant.

## 6. Precision boundary

PASS.

The chapter separates storage width, arithmetic format, accumulator format, rounding, overflow/underflow, and task-level error.

Lower precision is not promoted into a universal accuracy or performance guarantee.

## 7. Occupancy and fusion boundaries

PASS.

Occupancy is treated as a resource-residency diagnostic, not as performance itself.

Fusion is treated as a way to alter launches/materialization/data movement only when the required semantics and numerical tolerance are preserved.

## 8. Benchmark discipline

PASS.

The chapter requires device, software stack, precision, shape, warmup/synchronization, repetitions/statistics, FLOP/byte convention, transfer inclusion, and timing-region disclosure.

Peak specification, measured kernel rate, and end-to-end application rate remain separate objects.

## 9. Downstream systems boundary

PASS.

Data/tensor/pipeline/expert parallelism, collectives, distributed KV caches, serving, batching, and multi-device throughput/latency remain deferred to ATLAS-CH-SYSTEMS-001.

## 10. Repository integrity

Implementation head a8e1fe2e5474a61019614c4500d2cf92c2336335 passed canonical validation before merge.

The audit metadata repair requires fresh exact-head validation before audit merge.

## Final disposition

AUDIT-044 passes after one source-metadata repair, subject to fresh exact-head green CI.
