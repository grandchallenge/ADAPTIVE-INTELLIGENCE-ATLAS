# HARDWARE-001 — The Machine Under the Mathematics

## Identity

- chapter: ATLAS-CH-HARDWARE-001
- implementation issue: #176
- protected live baseline: e421edcc222922526fd4e1de853b168df1d6b847
- work branch: work/ch176
- direct consumer: ATLAS-CH-SYSTEMS-001

## Hard prerequisite

- ATLAS-CH-LINALG-001
- manuscript blob: e7fcf56322f26d232d3a3043038d9850792b4bde
- source-lock blob: f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e
- Foundation audit record: reviews/AUDIT-004.md
- audit blob: 948f76b3f86d27fa4830efc30d8ef0135134256e

## External source frame

- Williams, Waterman, and Patterson (2009), Roofline: An Insightful Visual Performance Model for Multicore Architectures, Communications of the ACM 52(4):65-76, DOI 10.1145/1498765.1498785.
- NVIDIA CUDA Programming Guide, current online documentation retrieved 2026-10-04.
- NVIDIA CUDA C++ Best Practices Guide, current online documentation retrieved 2026-10-04.

Vendor documentation is used as CUDA-scoped authority. Device-specific capacities, throughput figures, and architecture details are not generalized without a separate exact source lock.

## Exact finite witness

For

\[
A=
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
5&6\\
7&8
\end{pmatrix},
\]

the exact product is

\[
AB=
\begin{pmatrix}
19&22\\
43&50
\end{pmatrix}.
\]

Declared arithmetic count:

- 8 scalar multiplications;
- 4 scalar additions;
- total \(W=12\) FLOPs.

Declared FP32 traffic models:

A. no cross-output input reuse:
- 16 input loads + 4 output stores;
- \(Q_A=80\) bytes;
- \(I_A=0.15\) FLOP/byte.

B. perfect full-input reuse:
- 8 input loads + 4 output stores;
- \(Q_B=48\) bytes;
- \(I_B=0.25\) FLOP/byte.

Thus identical mathematics and identical declared FLOPs coexist with different declared byte movement and arithmetic intensity.

For the hypothetical one-level machine:

\[
P_{\max}=10\ \mathrm{TFLOP/s},
\qquad
B=1\ \mathrm{TB/s},
\]

the Roofline bandwidth-side bounds are \(0.15\) and \(0.25\) TFLOP/s respectively.

This is an accounting witness, not a benchmark.

## Durable boundaries

- FLOP count != runtime.
- throughput != latency.
- equal FLOPs != equal bytes moved.
- arithmetic intensity requires a declared memory boundary.
- peak throughput != attained throughput.
- occupancy != performance.
- mathematical matrix multiplication != guaranteed matrix-unit efficiency.
- smaller precision != acceptable numerical error.
- kernel fusion != semantic equivalence by default.
- CUDA terminology is not silently universalized.
- single-device kernel reasoning != distributed-systems reasoning.

## Artifact set

- sources/source-locks/ATLAS-CH-HARDWARE-001.yaml
- manuscript/specifications/ATLAS-CH-HARDWARE-001.md
- mathematics/derivations/ATLAS-CH-HARDWARE-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-HARDWARE-001.md
- manuscript/parts/13-agents-systems-hardware/ATLAS-CH-HARDWARE-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- sources/bibliography.bib
- this receipt

No governed figure is required for the draft.

## Remaining gates

Canonical exact-head validation, implementation merge, bounded post-draft audit, in-scope repair, audit exact-head validation/merge, issue closure verification, fresh frontier recomputation, handoff update, and controller reset remain mandatory.
