# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 01a4c2c7d526df385bb8b2ab58046c3c476e3629

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-SHIFT-001 — **Distribution Shift and Robustness**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Develop covariate shift, concept drift, adversarial robustness, robust optimization, and structural sensitivity while explicitly separating guarantees under the source law from guarantees under a changed deployment law.

## Hard prerequisite on exact current main

### ATLAS-CH-UNCERTAINTY-001

- manuscript: e6714d0505a96e2bfdc431b4ec60d50b0044efa6
- source lock: b9f38d496efe2d704b759510cf171d5a3e83a2c8
- AUDIT-054: 132a0df9a603ec88811312d193971100549648a4

Inherited boundary:

- uncertainty objects remain distinct rather than collapsed into one scalar;
- population calibration definitions may be inherited;
- calibration-versus-sharpness and exact finite uncertainty witnesses may be inherited;
- exchangeability and risk/coverage guarantees remain tied to the law and assumptions under which they were established;
- calibration, risk, and coverage under source law P do not automatically transfer to changed law Q;
- P-exchangeability does not imply Q-exchangeability;
- uncertainty diagnostics established under P are not changed-law robustness guarantees.

## Before drafting SHIFT

1. bind the exact audited UNCERTAINTY triple above;
2. source-lock only primary references genuinely needed for covariate shift, label/concept shift, adversarial robustness, robust optimization, or structural sensitivity;
3. declare source law P and deployment law Q explicitly before making any shifted-risk or shifted-calibration claim;
4. distinguish covariate shift, label/prior shift, concept/conditional shift, adversarial perturbation, and structural/mechanism shift rather than using “distribution shift” as one undifferentiated object;
5. define at least one exact finite witness where a guarantee/diagnostic valid under P fails under Q while the predictor itself is unchanged;
6. include a control where a changed marginal does not change the relevant conditional/task risk, so “shift detected” is not automatically “performance failure”;
7. keep calibration, coverage, selective risk, ordinary predictive risk, adversarial risk, and structural sensitivity as separate metrics;
8. state support/absolute-continuity assumptions for any importance-weighting or covariate-shift correction;
9. keep average-case distribution shift distinct from worst-case/adversarial perturbation unless a bridge is proved;
10. do not infer causal or mechanistic shift solely from changed predictive statistics.

## Immediately completed transaction — REGRETROUTE-001

- implementation issue: #259 — closed completed
- implementation PR: #260
- exact green implementation head: 464e8cdc6e8927188c2fab1288780a0188c1b48e
- implementation GitHub Actions run: 37549285117 — success
- implementation merge: 2b02b15e46fd9319931b96fb45ffd5dea4d6c1e4
- post-draft audit: AUDIT-065
- audit issue: #261 — closed completed
- audit PR: #262
- exact green audit head: 1903dc4e1afeb045ee0aeb1119ee63eeaa0b00eb
- audit GitHub Actions run: 37549565211 — success
- audit merge/current main: 01a4c2c7d526df385bb8b2ab58046c3c476e3629
- audit record blob: 54185fc68c34f093aafcd43135867fe2a7be7e83
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final REGRETROUTE artifacts:

- specification: fecec841c12b667d3a2dc1392897fdb968c508c4
- derivation packet: 0426cfc1a585962d8c9914f3f9ada8813108e0e0
- computational witness: c6f767d9d015ff5604eba5c328f0f55508627f13
- reader manuscript: 9f0a309089ebdc04ebb87c01d0db99308819a187
- source lock: a3605caab59239ffd7fb4860f4727482bc6989f0
- bibliography: 52b3b3e63bf439c92a6a9f6bdec9ae03e4247a5a
- Chapter Ledger: ffcf2ce60f0a34043b2ac2f2818a9e19cbaf2bf2
- Source Register: 62976db0dd60dcf2af54d495d2fc95ee57e62f7c
- transaction receipt: c8c5978960cd3a34e651ca78e8a7a0460a5fbec2

Durable REGRETROUTE substrate:

- preferred proposal, feasible accepted-action set, accepted dispatch, capacity map, loss timing, and feedback are separately typed;
- regret is defined only relative to a declared comparator class;
- exact common-frame witness uses losses (0,1),(1,0),(0,1),(1,0) over actions A,B and comparator sequences with at most three switches;
- unique zero-loss shifting comparator is (A,B,A,B);
- stay route (A,A,A,A) has accepted-route churn 0 and shifting regret 2;
- tracking route (A,B,A,B) has churn 3 and shifting regret 0;
- therefore route churn is not a regret surrogate;
- against the static comparator class both fixed actions lose 2, so comparator choice materially changes the regret object;
- optionality O_t=|F_t|-1 equals 1 throughout the witness but does not determine regret;
- remaining switch budget is an operational correction-capacity resource, not a performance metric;
- ordinary comparators should obey the same capacity/feasibility constraints as the online policy unless an oracle comparator is explicitly labeled;
- probability drift, preferred-route churn, accepted churn, load balance, specialization, regret, and downstream task loss remain distinct;
- if switching itself is costly, that cost must be placed explicitly in the loss/objective;
- full-information and bandit feedback expose different information to the online router.

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering selects:

- ATLAS-CH-SHIFT-001

Other dependency-legal count-0 chapters remain:

- ATLAS-CH-SPECTRALDIAG-001
- ATLAS-CH-SPECTRALSHAPE-001
- ATLAS-CH-SYNTHESIS-001
- ATLAS-CH-SYSTEMS-001
- ATLAS-CH-TOKENCOMP-001
- ATLAS-CH-VARIOPT-001

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
