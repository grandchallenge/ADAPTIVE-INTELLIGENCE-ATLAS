# REGRETROUTE-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-REGRETROUTE-001
- implementation issue: #259
- protected baseline: 506d2642398330a27bc9b6e6c17ec38969b6f6a0
- branch: work/regretroute-259

## Hard prerequisite

ROUTERDYN-001:
- manuscript 4c3c4b22d7f6a564b255a251ba646d11dbbc29a4
- source lock 27aca5556b902c679132780e4f74ba8822420762
- AUDIT-050 19a7e4bf2d0291380b195d2ad7cc0091922bcb8b

## New primary sources
- Auer, Cesa-Bianchi, Freund & Schapire 2002, DOI 10.1137/S0097539701398375
- Herbster & Warmuth 1998, DOI 10.1023/A:1007424614876

## Implementation artifacts
- specification fecec841c12b667d3a2dc1392897fdb968c508c4
- derivations 0426cfc1a585962d8c9914f3f9ada8813108e0e0
- witness c6f767d9d015ff5604eba5c328f0f55508627f13
- manuscript 9f0a309089ebdc04ebb87c01d0db99308819a187
- source lock a3605caab59239ffd7fb4860f4727482bc6989f0
- bibliography 52b3b3e63bf439c92a6a9f6bdec9ae03e4247a5a
- Chapter Ledger ffcf2ce60f0a34043b2ac2f2818a9e19cbaf2bf2
- Source Register 62976db0dd60dcf2af54d495d2fc95ee57e62f7c

## Exact common-frame witness
- accepted actions: {A,B}
- T=4
- feasible accepted set F_t={A,B} each round
- full-information losses: (0,1),(1,0),(0,1),(1,0)
- comparator class: action sequences with at most 3 switches
- unique zero-loss comparator: (A,B,A,B)
- comparator cumulative loss: 0

Stay policy:
- accepted actions (A,A,A,A)
- churn 0
- cumulative loss 2
- shifting regret 2

Tracking policy:
- accepted actions (A,B,A,B)
- churn 3
- cumulative loss 0
- shifting regret 0

## Static-comparator control
- fixed-A loss = 2
- fixed-B loss = 2
- best static comparator loss = 2
- stay static regret = 0
- tracking static regret = -2
- comparator choice changes the regret object

## Optionality and correction capacity
- optionality O_t=|F_t|-1=1 each round
- switch budget S=3
- remaining switch correction capacity K_t=max(0,S-N_t)
- stay preserves switch budget but has higher shifting regret
- tracking consumes switch budget but has zero shifting regret

## Durable boundaries
- preferred route and accepted dispatch are different when capacity can reroute proposals;
- comparator actions should obey the same declared feasibility/capacity constraints unless an oracle comparator is explicitly labeled;
- static, shifting, and other dynamic regret notions are not interchangeable;
- full-information and bandit feedback provide different online information;
- churn is not a regret surrogate;
- load balance is not regret;
- probability drift is not regret;
- specialization is not regret;
- optionality is not correction capacity;
- low routing regret does not automatically imply low downstream task loss;
- observed regret does not identify a causal training mechanism.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
