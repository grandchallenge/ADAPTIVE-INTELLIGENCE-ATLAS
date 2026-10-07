# AUDIT-065 — Routing as Online Decision Making

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-REGRETROUTE-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, bibliography, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #259
- implementation PR: #260
- exact validated implementation head: 464e8cdc6e8927188c2fab1288780a0188c1b48e
- implementation GitHub Actions run: 37549285117
- implementation merge / audited protected baseline: 2b02b15e46fd9319931b96fb45ffd5dea4d6c1e4
- audit issue: #261
- audit branch: audit/a261
- chapter: ATLAS-CH-REGRETROUTE-001

Protected implementation artifact identities:

- specification: fecec841c12b667d3a2dc1392897fdb968c508c4
- derivation packet: 0426cfc1a585962d8c9914f3f9ada8813108e0e0
- computational witness: c6f767d9d015ff5604eba5c328f0f55508627f13
- reader manuscript: 9f0a309089ebdc04ebb87c01d0db99308819a187
- source lock: a3605caab59239ffd7fb4860f4727482bc6989f0
- bibliography: 52b3b3e63bf439c92a6a9f6bdec9ae03e4247a5a
- Chapter Ledger: ffcf2ce60f0a34043b2ac2f2818a9e19cbaf2bf2
- Source Register: 62976db0dd60dcf2af54d495d2fc95ee57e62f7c
- transaction receipt: c8c5978960cd3a34e651ca78e8a7a0460a5fbec2

## 1. Hard prerequisite

PASS.

ROUTERDYN-001 is bound exactly:

- manuscript 4c3c4b22d7f6a564b255a251ba646d11dbbc29a4;
- source lock 27aca5556b902c679132780e4f74ba8822420762;
- AUDIT-050 19a7e4bf2d0291380b195d2ad7cc0091922bcb8b.

The chapter preserves the prerequisite's typed separation among router probabilities, preferred routes, accepted dispatch, realized load, churn, probability drift, specialization, and local dynamics.

ROUTERDYN is not used as hidden authority for regret theory.

## 2. New source scope

PASS.

The chapter adds only:

- Auer, Cesa-Bianchi, Freund, and Schapire (2002), DOI 10.1137/S0097539701398375;
- Herbster and Warmuth (1998), DOI 10.1023/A:1007424614876.

Their use is narrow:

- adversarial/nonstochastic bandit action selection, partial feedback, and regret framing;
- comparison against expert sequences that may switch over time.

Neither source is used as authority for sparse-router capacity mechanics, optionality, correction capacity, or the exact Atlas churn/regret witness.

## 3. Bibliography integrity

PASS.

The bibliography contains the keys:

- AuerEtAl2002Nonstochastic;
- HerbsterWarmuth1998Tracking.

The manuscript and source lock reference those exact keys.

No unrelated bibliography change is introduced.

## 4. Accepted-action semantics

PASS.

The chapter distinguishes:

- preferred proposal p_t;
- feasible accepted-action set F_t;
- accepted/executed dispatch a_t;
- capacity/overflow map G_t.

The base regret object is accepted dispatch because that is the executed action that incurs the declared loss.

Counterfactual preferred-route regret is explicitly kept separate.

## 5. Loss and feedback timing

PASS.

The chapter orders each round as:

1. observe pre-action information;
2. propose/choose;
3. enforce capacity/feasibility;
4. execute accepted dispatch;
5. incur loss;
6. reveal feedback.

Full-information and bandit feedback are separately defined.

The exact witness uses full-information feedback only for deterministic replay; no claim is made that the online policy sees future losses.

## 6. Comparator definition

PASS.

For switch budget S=3 and horizon T=4, the comparator class is:

\[
\Pi_3=\{u_{1:4}: C(u)\le3\}.
\]

Shifting regret is defined by cumulative accepted-action loss minus the minimum comparator loss over that class.

The chapter explicitly blocks conflation of static, shifting, and other dynamic-regret notions.

## 7. Exact loss process

PASS.

The declared full-information losses are:

\[
(0,1),(1,0),(0,1),(1,0),
\]

with coordinates (A,B).

Every loss is nonnegative and each round has exactly one zero-loss action.

Therefore the unique zero-loss sequence is:

\[
(A,B,A,B).
\]

Its switch count is three and its cumulative loss is zero.

Independent audit replay agrees.

## 8. Zero-churn / positive-regret witness

PASS.

For:

\[
(A,A,A,A),
\]

accepted-dispatch churn is zero and cumulative loss is two.

Because the shifting comparator loss is zero:

\[
\boxed{R_4^{(3)}=2}.
\]

Thus zero churn can coexist with positive shifting regret.

## 9. High-churn / zero-regret witness

PASS.

For:

\[
(A,B,A,B),
\]

accepted-dispatch churn is three and cumulative loss is zero.

Therefore:

\[
\boxed{R_4^{(3)}=0}.
\]

Thus maximal round-to-round churn in this witness can coexist with zero shifting regret.

The two policies are evaluated under the same horizon, losses, feasibility, feedback, and comparator class.

## 10. Static-comparator control

PASS.

Fixed A and fixed B each incur cumulative loss two.

Therefore best static comparator loss is two.

The stay policy has static regret zero; the alternating policy has realized static regret -2.

The chapter correctly interprets this as a comparator-class change, not a contradiction.

## 11. Optionality

PASS.

Operational optionality is defined as:

\[
O_t=|F_t|-1.
\]

Because both A and B are feasible each round, O_t=1 throughout the exact witness.

Both policies therefore have identical optionality despite different churn and shifting regret.

The chapter does not treat optionality as a performance metric.

## 12. Correction capacity

PASS.

The chapter declares one operational correction-capacity measure as remaining switch budget:

\[
K_t=\max(0,S-N_t),
\]

where N_t counts switches already used before round t.

For the stay policy the values are (3,3,3,3); for the tracking policy they are (3,3,2,1).

The manuscript correctly treats this as one resource notion rather than a universal definition of recoverability.

## 13. Capacity and comparator fairness

PASS.

The chapter requires ordinary comparator actions to obey the same feasible accepted-action sets as the online policy.

An unconstrained oracle comparator may be introduced only as a separately labeled counterfactual.

This prevents capacity impossibility from being silently charged to online routing quality.

## 14. Metric firewalls

PASS.

The manuscript preserves the separations among:

- router probability drift;
- preferred-route churn;
- accepted-dispatch churn;
- load balance;
- specialization;
- regret;
- downstream task loss.

It explicitly rejects churn as a regret surrogate and does not infer downstream task performance from low routing regret without an interface relation.

## 15. Switching-cost boundary

PASS.

The chapter states that if switching itself is costly, the objective must include a declared switching penalty.

This makes churn part of the loss rather than smuggling churn preference into the interpretation of regret.

No switching cost is present in the exact base witness.

## 16. Nonstationarity boundary

PASS.

The exact loss process is deterministic/nonstationary in that the minimizing action alternates.

The chapter separately names comparator switching, loss variation, context drift, expert availability drift, capacity drift, and optimizer/model drift as different forms of nonstationarity.

No universal nonstationary-regret theorem is claimed.

## 17. Transaction-receipt provenance

PASS.

Every implementation artifact identity recorded in governance/tranches/REGRETROUTE-001.md matches the protected implementation merge.

The protected receipt itself is blob c8c5978960cd3a34e651ca78e8a7a0460a5fbec2.

No post-receipt implementation repair occurred.

## 18. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- REGRETROUTE status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- hard dependency remains ROUTERDYN-001;
- the REGRETROUTE source lock is registered;
- both new bibliography keys resolve;
- no governed figure is introduced;
- exact implementation head passed GitHub Actions run 37549285117;
- protected implementation merge passed canonical repository validation;
- independent audit replay returned REGRETROUTE_AUDIT_WITNESS_OK.

## Final disposition

AUDIT-065 passes with no repair.

The durable REGRETROUTE rule is:

**routing churn, load balance, probability drift, specialization, optionality, correction capacity, regret, and downstream task loss are distinct objects. Regret is meaningful only after accepted-action semantics, feasibility/capacity, feedback timing, and comparator class are declared.**
