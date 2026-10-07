# ATLAS-CH-SYSTEMS-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-SYSTEMS-001
- implementation issue: #281
- protected baseline: 4e1485f3849a7284be44d81a0d5ecdec9d15783f
- branch: work/systems-281

## Hard prerequisites

HARDWARE-001:
- manuscript 2ce486d4cce53a5f5194241ce3bb1c0f40c7c895
- source lock 98d783c072fa28d784991617af49329259ba0b8e
- AUDIT-044 2c53ff24db17895ff9feba5f0f2854fdaa1e5c9b

MOE-001:
- manuscript 5281e3bc0721681c630c56057cf478311e96662d
- source lock 75d5b04a90794b7543c70414ec9e2be59c9af7ed
- AUDIT-033 261e63f7853c359460bd76302ddfaeed576892cb

## Source decision

New external authority is limited to four primary systems references needed beyond the audited prerequisites:

- Megatron-LM 2021 for composed data/tensor/pipeline training;
- GPipe 2019 for microbatch pipeline semantics;
- Orca 2022 for iteration-level serving scheduling/selective batching;
- PagedAttention/vLLM 2023 for KV-cache memory-management pressure and serving behavior.

Collective equations, byte accounting, and the topology-placement control are Atlas-owned exact finite constructions.

## Implementation artifacts

- specification b61e466116747a2a405df0cb457ea893e1147d98
- derivation packet 6689d993ba888f89cdf35cbe592e203daacad16e
- computational witness 33e06c5f988d7d9a607021d246fa4be0c8d5d501
- reader manuscript 0e2c1e948e462cc6e068e741653dac5294c2afa7
- source lock b2366df7956ead690789814b8fe06912f99c9f24
- Chapter Ledger 63fe65293efe4f39343f74fa4254473b196a3b30
- Source Register 0fc5f52912c037e5e5e0af4dbea1a3924fe015df

## Exact witness

Four ranks hold 8-element FP32 vectors and execute the same four-rank ring all-reduce.

Per placement:
- vector bytes: 32
- chunk bytes: 8
- sends per rank: 6
- bytes sent per rank: 48
- bytes received per rank: 48
- reduction additions per rank: 6
- aggregate reduction additions: 24

Grouped logical-to-physical placement:
- two cross-node ring edges
- cross-cut traffic: 96 bytes

Interleaved placement:
- four cross-node ring edges
- cross-cut traffic: 192 bytes

Equal arithmetic and equal per-rank collective bytes therefore coexist with a 2x difference in physical cross-cut traffic.

Under the declared toy shared-cut capacity of 16 bytes/time-unit:
- grouped cut-capacity lower bound: 6 time units
- interleaved cut-capacity lower bound: 12 time units

These are accounting lower bounds, not measured latency.

## Durable distinctions

- data, tensor, pipeline, and expert parallelism are separately typed;
- collective semantics do not determine collective algorithms;
- logical parallelism does not determine physical topology;
- router preference, accepted dispatch, expert placement, and network path remain distinct;
- model FLOPs, local bytes, network bytes, memory, latency, throughput, utilization, goodput, and tail behavior remain distinct;
- training efficiency does not imply serving efficiency;
- modeled performance does not become measured performance.

## Validation gate

Merge requires exact-head canonical repository validation, exact witness replay, exact-head GitHub Actions success, then a fresh post-draft audit.
