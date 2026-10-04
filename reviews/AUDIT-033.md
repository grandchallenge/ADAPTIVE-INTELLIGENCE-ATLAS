# AUDIT-033 — Mixture-of-Experts Systems

## Disposition

**PASS AFTER THREE ROUTING-SEMANTICS REPAIRS**

ATLAS-CH-MOE-001 remains at `draft-v0.1`.

The chapter correctly separates router probabilities, preferred top-k routes, capacity-constrained accepted dispatch, expert load, balancing proxies, specialization evidence, and distributed expert execution.

AUDIT-033 found three in-scope precision defects:

1. the source lock described top-k too close to an executed dispatch rule. It now states that top-k defines a preferred route and becomes executed dispatch only after tie-breaking, capacity, overflow, and weighting semantics are declared;
2. the derivation/manuscript used accepted-load entropy as a possible router-collapse diagnostic. Capacity handling can mask concentrated router preferences, so the repaired chapter distinguishes probability/preferred-route concentration from accepted-load concentration;
3. the phrase `capacity collapse` was too easily conflated with router/expert collapse. It is now `capacity overload`: preferred routing demand exceeds an execution limit.

No exact witness arithmetic, source identity, prerequisite identity, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `5090ed112ee086450387a8465772ec9a2358c410`;
- implementation PR:
  #127;
- audit issue:
  #128;
- chapter:
  `ATLAS-CH-MOE-001`.

## 1. Hard prerequisites

PASS.

### Conditional Computation

- manuscript blob:
  `9ddd74ac449724631fb92e0af7d6b0114ce6e3b0`;
- AUDIT-028 blob:
  `0a01aca03a3afe2a85896d3971830f3f7e9d2b40`;
- source-lock blob:
  `897bca1b91393690f810ea416663c525712630e8`.

### Transformer baseline

- manuscript blob:
  `197b74ffd40fe54b79ca15ab731b73538aada494`;
- AUDIT-011 blob:
  `e8bfa9b062b4b80bd0cccd49f168f99c40843f71`;
- source-lock blob:
  `dec885c68a9afb439aed9af5ca35b998519722bc`.

The chapter inherits only audited conditional-execution/resource semantics and Transformer feed-forward/residual-stream anatomy.

No Router Dynamics or Systems manuscript is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock identifies:

- Shazeer et al. (2017), *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*;
- Lepikhin et al. (2020), *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding*;
- Fedus, Zoph, and Shazeer (2022), *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*;
- Zoph et al. (2022), *ST-MoE: Designing Stable and Transferable Sparse Expert Models*.

They are used as representative evidence for sparse gating, capacity, balancing, expert-parallel execution, stability, and specialization analyses.

No one router, loss, capacity factor, or parallelism strategy is promoted to universal status.

## 3. Router probabilities versus dispatch

PASS AFTER REPAIR.

The chapter keeps distinct:

- logits `z_{i,e}`;
- probabilities `p_{i,e}`;
- preferred top-k set `P_i`;
- accepted dispatch `a_{i,e}`;
- gate weights `alpha_{i,e}`;
- realized expert execution.

Top-k is now explicitly a preferred route before capacity/overflow handling.

## 4. Capacity semantics

PASS.

The chapter uses the representative nominal form:

`C=ceil(c_f k N/M)`.

It explicitly scopes this as implementation-dependent in grouping/granularity.

Capacity constrains accepted assignments, not router probabilities.

## 5. Overflow semantics

PASS.

The chapter treats overflow policy as part of executed-model semantics.

The exact witness uses one declared reroute policy.

A drop-on-overflow counterfactual demonstrates that identical router probabilities can produce different accepted loads and different realized expert arithmetic.

## 6. Expert load versus router probability mass

PASS.

Accepted load:

`n_e=sum_i a_{i,e}`.

Router probability mass:

`m_e=sum_i p_{i,e}`.

The chapter correctly refuses the identity between normalized accepted load and normalized probability mass.

## 7. Exact routing witness

PASS.

Preferred top-1 assignments produce:

`(3,2,1)`.

With capacity:

`C=2`,

E1 is overloaded by one token.

Among E1-preferred tokens, t3 has the smallest E1 probability:

`1/2`.

Its best alternative is E3:

`2/5 > 1/10`.

E3 has free capacity.

The declared policy therefore reroutes:

`t3:E1->E3`.

Final accepted loads are:

`(2,2,2)`.

No token is dropped.

## 8. Router probability masses

PASS.

Independent exact arithmetic confirms:

`m=(47/20,2,33/20)`.

Normalized by six tokens:

`q=(47/120,1/3,11/40)`.

Accepted load fractions are:

`f=(1/3,1/3,1/3)`.

Therefore:

`f != q`.

## 9. Exact imbalance metrics

PASS.

Count imbalance:

`B_count=0`.

Probability-mass offsets from uniform are:

`7/120,0,-7/120`.

Thus:

`B_prob=2*(7/120)^2=49/7200>0`.

Perfect accepted-count balance therefore coexists with nonzero router-probability imbalance.

## 10. Utility counterexample

PASS.

Toy post-routing utility totals are:

`u=(8,4,2)`

while accepted token loads remain:

`(2,2,2)`.

The chapter correctly labels this as an independent illustrative diagnostic, not a router probability, specialization theorem, or recommended training objective.

## 11. Drop-policy counterfactual

PASS.

Under drop-on-overflow:

`n_drop=(2,2,1)`.

Drop rate:

`1/6`.

For identical per-token expert arithmetic cost c:

- reroute policy: `6c`;
- drop policy: `5c`.

Same router probabilities; different overflow semantics; different execution.

## 12. Preferred-router concentration versus accepted-load concentration

PASS AFTER REPAIR.

The final derivation distinguishes:

`g_e=d_e/sum_j d_j`

for preferred-route fractions and:

`f_e=n_e/sum_j n_j`

for accepted-load fractions.

It separately defines preferred-route and accepted-load entropy.

The chapter now states explicitly that capacity/rerouting/dropping can make accepted loads appear balanced while router preferences remain concentrated.

A router-collapse claim must name whether it concerns:

- logits/probability mass;
- preferred routes;
- accepted dispatch;

plus statistic, horizon, and threshold.

## 13. Capacity overload terminology

PASS AFTER REPAIR.

The final chapter distinguishes:

- preferred-router concentration;
- accepted-load concentration;
- expert underuse;
- expert functional redundancy;
- capacity overload.

These may co-occur but are not synonyms.

## 14. Specialization boundary

PASS.

The chapter requires a specialization claim to name input/domain structure, expert identity, a functional/performance statistic, a horizon, and comparison baseline.

Traffic imbalance alone is not treated as specialization.

## 15. Expert redundancy

PASS.

Functional similarity can be evaluated independently of traffic, for example through expert-output distance on a declared evaluation distribution.

Heavy use does not exclude redundancy.

## 16. Auxiliary balance objectives

PASS.

The chapter keeps:

`L_total=L_task+lambda L_balance`

as a decomposition of distinct objectives.

Optimizing a balancing proxy is not promoted into task-optimal routing, semantic specialization, equal compute, or lower communication.

## 17. Expert parallelism

PASS.

Expert placement and token dispatch are explicitly modeled.

The simple communication count:

`K_comm=sum_{i,e} a_{i,e} 1{src(i)!=dev(e)}`

is correctly labeled as a proxy.

The chapter preserves SPARSE-001's rule that arithmetic savings do not imply lower wall-clock cost.

## 18. Training versus serving

PASS.

The manuscript states that training-time routing may use different noise, balancing, capacity, and dropping semantics from inference/serving.

Routing claims must therefore bind to execution phase.

## 19. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records MOE-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-MOE-LOCK-001`.

The computational witness is bound at:

`mathematics/computational-witnesses/ATLAS-CW-MOE-001.md`.

The witness includes an explicit Claim boundary.

The manuscript contains no unresolved citation keys and includes a reference section plus the exact source-lock path.

No governed figure is required.

## 20. Downstream handoff: Router Dynamics

PASS.

ROUTERDYN-001 may inherit:

- probabilities versus preferred/accepted routes;
- capacity and overflow semantics;
- count/probability balance diagnostics;
- concentration/underuse/redundancy distinctions;
- specialization evidence requirements.

It must independently develop temporal churn and router dynamics.

## 21. Downstream handoff: Systems

PASS.

SYSTEMS-001 may inherit:

- expert placement;
- accepted dispatch;
- capacity;
- communication proxies;
- active versus total capacity;
- straggler boundaries.

It must independently develop system/hardware cost models and measured serving efficiency.

## 22. Final disposition

AUDIT-033 passes after the three routing-semantics repairs above.

The durable MoE layer is:

**router preferences -> preferred sparse routes -> capacity/overflow policy -> accepted dispatch -> expert computation + communication, with balance, specialization, collapse, and efficiency each requiring their own explicitly named evidence.**
