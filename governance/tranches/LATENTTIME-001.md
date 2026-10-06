# LATENTTIME-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-LATENTTIME-001
- implementation issue: #247
- protected baseline: c550463eb448e41c2493747a6ed6ad83e34b24dc
- branch: work/latenttime-247

## Hard prerequisites

RPO-001:
- manuscript 0483a358aa486aab5ae213e05b5bbd23161e021d
- source lock 9ad49c8e7950fa4e534c3083500fbdac288127a9
- AUDIT-051 773b34624a7224c87cf908688e3a981c0ec8c618

DYN-001:
- manuscript f4aa89075f221529401e56a152a6cdfca3dcc47d
- source lock 217d1e4e74c00c1d83a3e769d6437786197d4383
- AUDIT-008 c6af8bae5e875b32b3955eb0f2232c0edfa76d7b
- AUDIT-008A 525254a67510636cf39b0758c300c77a479de9a5

## New primary sources
- Sakoe & Chiba 1978, DOI 10.1109/TASSP.1978.1163055
- Zhou & De la Torre 2012, DOI 10.1109/CVPR.2012.6247812

## Implementation artifacts
- specification 1fa3ecba7df0de0ba828ed7e2d2383f8c895dd2d
- derivations 82b9e9fd771003b3b0dbe7c1c88b8315028cc84c
- witness cb5983be9863b2d8898a255d38623638fae0d900
- manuscript feba2a0c9b2e1a96f0149bb2889d0e1ca8aa6afd
- source lock 9981093df848bee6d38191f67fc0d5180d7f5a67
- bibliography ac6eb5e72b3ef35daeb9b5e897c1d1e355253393
- Chapter Ledger 06b183fa8b5b55019cdd88604830ec5008097066
- Source Register 41d5419ea4783d521e14c5b2478048255a2548a3

## Exact warped witness
- X=(0,1,2)
- Y=(0,0,1,2)
- local cost c(i,j)=(x_i-y_j)^2
- admissible steps {(1,0),(0,1),(1,1)}
- exact admissible path count: 25
- unique zero-cost path: ((1,1),(1,2),(2,3),(3,4))
- optimal cost: 0

## Identity control
- X0=Y0=(0,1,2)
- exact admissible path count: 13
- unique zero-cost path: ((1,1),(2,2),(3,3))
- optimal cost: 0

## Durable boundaries
- observed sequence position is not automatically latent time;
- an optimal warping path is relative to observations, cost, endpoints, and admissible path constraints;
- unique alignment optimum does not prove uniquely true physical or causal time;
- positional Fourier/RoPE structure does not by itself identify latent time;
- discrete warping paths are combinatorial alignment objects, not automatically continuous-time flows;
- multimodal alignment requires an explicit comparison representation/metric;
- low alignment cost does not prove semantic identity or causal direction.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
