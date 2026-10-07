# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-07
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 4e1485f3849a7284be44d81a0d5ecdec9d15783f

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-SYSTEMS-001 — **Scaling, Parallelism, and Serving**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

## Hard prerequisites on exact current main

### ATLAS-CH-HARDWARE-001
- manuscript: 2ce486d4cce53a5f5194241ce3bb1c0f40c7c895
- source lock: 98d783c072fa28d784991617af49329259ba0b8e
- AUDIT-044: 2c53ff24db17895ff9feba5f0f2854fdaa1e5c9b

Inherited boundary:
- bandwidth, locality, arithmetic intensity, precision, resource constraints, and benchmark discipline may be inherited;
- FLOPs are not time and throughput is not latency;
- peak throughput is not attained throughput;
- kernel optimization is not distributed-system optimization;
- distributed communication, serving, KV-cache behavior, and multi-device scaling remain SYSTEMS responsibilities.

### ATLAS-CH-MOE-001
- manuscript: 5281e3bc0721681c630c56057cf478311e96662d
- source lock: 75d5b04a90794b7543c70414ec9e2be59c9af7ed
- AUDIT-033: 261e63f7853c359460bd76302ddfaeed576892cb

Inherited boundary:
- expert placement, accepted dispatch, capacity, communication proxies, active versus total capacity, and straggler boundaries may be inherited;
- router preference, accepted dispatch, balance, specialization, collapse, and efficiency remain distinct objects;
- sparse experts create conditional capacity, not free capacity;
- SYSTEMS must independently develop system/hardware cost models and measured serving efficiency.

## Before drafting SYSTEMS

1. bind the exact audited HARDWARE and MOE triples above;
2. source-lock only primary distributed-training/serving references genuinely needed beyond those prerequisites;
3. type data, tensor, pipeline, and expert parallelism separately;
4. declare communication topology and collective semantics;
5. separate model FLOPs, bytes moved, collective cost, memory footprint, latency, throughput, utilization, and tail behavior;
6. define at least one exact finite placement/communication witness;
7. include a control where equal arithmetic work produces different communication or latency cost;
8. keep training-system efficiency distinct from serving efficiency;
9. keep preferred MoE routing distinct from accepted expert dispatch and physical placement;
10. preserve measured-versus-modeled performance boundaries.

## Immediately completed transaction — SYNTHESIS-001

- implementation issue: #276 — closed completed
- implementation PR: #277
- exact green implementation head: 14ba13a9ea0fd9bf7bc965fdb0b505bc83e16a57
- implementation Actions run: 37593846381 — success
- implementation merge: 0925dd1a0108f99a230bb0dabf4cc423f1839867
- post-draft audit: AUDIT-069 — PASS — NO REPAIR
- audit issue: #278 — closed completed
- audit PR: #279
- exact green audit head: 6079d71dcf4ccb2320185bb9de028a57f6c27c5c
- audit Actions run: 37594641803 — success
- audit merge/current main: 4e1485f3849a7284be44d81a0d5ecdec9d15783f
- audit record blob: 77e7168bb57b8c79fdda11537b1c6fa08d210c4a
- final protected merge tree has zero file differences from the exact validated audit head

Final SYNTHESIS artifacts:
- specification: b654fade91567c1a2d940c766bf75e0729b7a504
- derivation packet: f2b0fed22d025ba33c3e10e61cd61887da7d9452
- computational witness: e9ffd717f2568259aca8fdc3bd3913d11fb814ec
- reader manuscript: 1196cd0495bda0cc63515dbc46c127577c937f2e
- source lock: 32f4c6b53797bbbd9ae3b9694b5f68d246ef0f3a
- Chapter Ledger: 112d7e3ecc4ce9e1e6ba1c033c05ad98f8d8b65a
- Source Register: 36b5c66c314f7f792e9053dfd6d9016573b70acd
- transaction receipt: 4bd44862c5b942d50aa5509b29f24a03f3ec6d4c

Durable SYNTHESIS substrate:
- typed system object Sigma=(X,D,M,T,C,E,A,G,Q,K);
- full composition achieves task, validated-commit, and persistent-recall coverage 2/2 with zero unauthorized commits;
- broken routing reduces task/commit coverage to 1/2;
- removing validation while preserving governance can leave transient answers correct but authorized commits at 0/2;
- removing memory destroys persistent recall without necessarily changing immediate answers;
- removing the authorization gate can admit a validator-rejected bad-source record;
- capability, authority, evidence, governance, memory, adaptation, and heterogeneous cost remain distinct;
- FRONTIER status grammar is preserved and open obligations remain open;
- no universal distributed-versus-monolithic architecture theorem is claimed.

## Recomputed dependency-legal frontier

Remaining architecture chapters: 3.

Stable-ID ordering selects:
- ATLAS-CH-SYSTEMS-001

Other dependency-legal count-0 chapters:
- ATLAS-CH-TOKENCOMP-001
- ATLAS-CH-VARIOPT-001

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
