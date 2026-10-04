# AUDIT-034 — Optionality and Correction Capacity

## Disposition

**PASS AFTER THREE FORMAL/SOURCE PRECISION REPAIRS**

ATLAS-CH-OPTIONALITY-001 remains at `draft-v0.1`.

The chapter successfully separates reward value, comparator-relative regret, viable future action structure, information acquisition, recoverability, and correction capacity.

AUDIT-034 found three in-scope precision defects:

1. the finite witness used a clairvoyant matching commitment `C_theta` as comparator even though only `P` and `C_L` had been declared as stage-0 actions. The repaired witness declares the stage-0 action set `{P,C_L,C_R}`, keeps the learner comparison `P` versus `C_L`, and states explicitly that the comparator is clairvoyant and selects the declared `C_theta`;
2. `CC_{h,epsilon}(s;b)` was described too close to a post-evidence quantity even though it averages over the pre-evidence belief. The repaired chapter defines conditional post-evidence feasibility `C_{h,epsilon}(s,theta)=1{k_h(s,theta)<=epsilon}`, makes `V_h(s;theta)` explicit after environment resolution, and defines `CC` as the ex-ante expectation of that conditional indicator;
3. the Aubin bibliography/source-lock entry mixed the original 1991 book with a later reprint ISBN. The repaired lock binds the original 1991 Birkhäuser Boston print identity, ISBN `9780817635718`, without attaching the later-reprint DOI.

No witness arithmetic, Chapter Ledger status, dependency edge, or downstream architecture relation required reversal.

## Audited baseline

- implementation merge: `7eb2d23b77b612ed86db7ba50df6177f58df7bdf`;
- implementation PR: #130;
- audit issue: #131;
- chapter: `ATLAS-CH-OPTIONALITY-001`.

## 1. Hard prerequisite

PASS.

The source lock binds exactly:

- REGRET manuscript blob: `56d6039348cbb13814325a4cfb3256177ab39a56`;
- AUDIT-026 blob: `6af3c12f71f0731f0e3f3d0fef2389d6a9bc0d95`;
- REGRET source-lock blob: `52d85475fd6796ce5397b3255774bed2040e5a47`.

The chapter inherits comparator-relative regret, Bayesian versus minimax distinctions, and the negative boundary that low regret does not itself imply recoverability or preserved optionality.

No downstream Governed Adaptation manuscript is used as hidden prerequisite authority.

## 2. External source scope

PASS AFTER SOURCE-IDENTITY REPAIR.

The source lock uses:

- Arrow and Fisher (1974), *Environmental Preservation, Uncertainty, and Irreversibility*, only for the structural interaction among uncertainty, irreversibility, later information, and preservation value;
- Aubin (1991), *Viability Theory*, original Birkhäuser Boston print identity, only for state-constrained viability precedent;
- Klyubin, Polani, and Nehaniv (2008), *Keep Your Options Open: An Information-Based Driving Principle for Sensorimotor Systems*, for empowerment as information-theoretic action-to-future-sensor influence and the options-open interpretation.

The Atlas does not attribute its quotient optionality, correction-cost, or correction-capacity definitions to those sources.

## 3. Decision contract

PASS.

The chapter declares:

`D_opt=(Theta,b,S,A,T,K,h,G,U,c_corr)`.

Optionality claims are therefore relative to:

- environment uncertainty and belief;
- state/action/transition model;
- viability constraints;
- horizon;
- consequence equivalence;
- post-evidence objectives;
- correction cost.

The manuscript does not present optionality as an intrinsic scalar property independent of modeling choices.

## 4. Viable continuations

PASS.

The pre-evidence viable continuation object is:

`V_h(s)`.

The derivation explicitly requires the uncertainty quantifier to be declared, with realized, robust, and chance-constrained semantics kept distinct.

For post-evidence correction, the audit repair introduces:

`V_h(s;theta)`

under the resolved environment.

This removes an ambiguity between pre-evidence robust/uncertain viability and conditional post-evidence feasibility.

## 5. Functional option quotient

PASS.

The chapter defines consequence equivalence:

`pi ~_s pi'`

iff

`G_s(pi)=G_s(pi')`.

The functional option set is:

`O_h(s)=V_h(s)/~_s`.

Thus duplicated action labels do not automatically create distinct functional options.

The chapter states that the quotient still depends on the declared horizon and consequence signature.

## 6. Weighted optionality boundary

PASS.

The optional weighted quantity:

`W_h(s)=sum_{o in O_h(s)}w(o)`

is used only when the weight function has independent semantics.

The chapter does not treat raw cardinality as a universal utility.

Dominated, dangerous, redundant, or irrelevant options need not receive positive value.

## 7. Correction cost

PASS AFTER REPAIR.

For resolved environment `theta`, the chapter now defines:

`k_h(s,theta)`

over `V_h(s;theta)`.

If no viable continuation reaches the declared target:

`k_h(s,theta)=+infinity`.

This keeps separate:

- finite but increased correction cost;
- hard infeasibility.

## 8. Conditional correction versus ex-ante capacity

PASS AFTER REPAIR.

The post-evidence conditional indicator is:

`C_{h,epsilon}(s,theta)
=
1{k_h(s,theta)<=epsilon}`.

The pre-evidence belief-weighted summary is:

`CC_{h,epsilon}(s;b)
=
sum_theta b(theta) C_{h,epsilon}(s,theta)
=
E_{theta~b}[C_{h,epsilon}(s,theta)]`.

Thus `C` answers the conditional question after the environment is resolved, while `CC` measures ex-ante correction coverage under the declared belief.

The chapter no longer conflates these temporal viewpoints.

## 9. Monotonicity

PASS.

If:

`epsilon_1<=epsilon_2`,

then:

`{theta:k_h(s,theta)<=epsilon_1}
subseteq
{theta:k_h(s,theta)<=epsilon_2}`.

Nonnegative belief mass therefore gives:

`CC_{h,epsilon_1}(s;b)
<=
CC_{h,epsilon_2}(s;b)`.

No stronger regularity claim is made.

## 10. Recoverability and irreversibility

PASS.

Recoverability is defined relative to a recovery set `B` and horizon `h`.

Irreversibility therefore depends on:

- state abstraction;
- target/recovery equivalence;
- admissible controls;
- constraints;
- horizon.

A stochastic bad outcome is not automatically called irreversible.

## 11. Exact witness action class

PASS AFTER REPAIR.

The stage-0 action set is now explicitly:

`{P,C_L,C_R}`.

The two learner policies compared are:

- preserve `P`;
- commit-left `C_L`.

The symmetric `C_R` action is declared because the comparator is explicitly clairvoyant and chooses `C_theta`.

The comparator therefore no longer invokes an undeclared action.

## 12. Exact prior-value witness

PASS.

For preservation:

- `G(pi_P,L)=1/2`;
- `G(pi_P,R)=1/2`.

Hence:

`E_b G(pi_P)=1/2`.

For commit-left:

- `G(pi_L,L)=1`;
- `G(pi_L,R)=0`.

Hence:

`E_b G(pi_L)=1/2`.

The prior action-value gap is exactly zero.

## 13. Exact comparator regret

PASS.

The comparator observes `theta` before stage 0 and chooses the matching declared commitment.

Its environment-specific value is:

`V_L^*=V_R^*=1`.

Preservation regret is `1/2` in both environments, so Bayes regret is `1/2`.

Commit-left regret is `0` in L and `1` in R, so Bayes regret is also `1/2`.

Worst-case regret remains:

- preserve: `1/2`;
- commit-left: `1`.

The chapter correctly states that optionality is not invisible to every risk criterion.

## 14. Functional-option witness

PASS.

Using terminal consequence identity:

- `O_1(s_P)={L,R}`, count 2;
- `O_1(s_L)={L}`, count 1.

The option-count difference is therefore functional, not a label-count artifact.

## 15. Correction-capacity witness

PASS AFTER REPAIR.

For preservation:

- `k(s_P,L)=k(s_P,R)=0`;
- conditional indicators are `1,1`;
- ex-ante zero-tolerance capacity is `1`.

For commit-left:

- `k(s_L,L)=0`;
- `k(s_L,R)=+infinity`;
- conditional indicators are `1,0`;
- ex-ante zero-tolerance capacity is `1/2`.

Thus equal prior value and equal Bayes regret coexist with unequal ex-ante correction capacity.

## 16. Information separation

PASS.

The environment is equiprobable binary and is revealed perfectly in both branches.

Therefore:

- `H(Theta)=1 bit`;
- `H(Theta|Y)=0`;
- `I(Theta;Y)=1 bit`.

Information gain is identical while conditional correction feasibility and ex-ante correction capacity differ.

The chapter therefore correctly separates knowing the needed correction from retaining the ability to perform it.

## 17. Preservation-cost counterexample

PASS.

With preservation cost `c`:

`Q(P)=1-c`;

`Q(C_L)=1/2`.

At `c=3/4`:

`Q(P)=1/4 < 1/2=Q(C_L)`.

The higher-optionality policy can therefore have lower expected return.

No universal anti-commitment rule is inferred.

## 18. Alias counterexample

PASS.

Two labels with identical transitions, costs, and consequence signatures form one equivalence class.

Raw action count can increase while functional option count remains fixed.

This blocks a representation-dependent action-count interpretation of optionality.

## 19. Empowerment boundary

PASS.

Empowerment is treated as an information-theoretic channel-capacity notion of possible sensorimotor influence.

The Atlas correction-capacity object is target- and feasibility-specific.

The chapter says the two may correlate but does not identify them.

## 20. Policy versus environment optionality

PASS.

Exogenous environmental branching is not counted as controllable policy optionality.

The chapter correctly distinguishes many possible worlds from many feasible responses.

## 21. Delay boundary

PASS.

Delaying a decision is not treated as synonymous with recoverability.

A delay may itself consume future repair paths or cross a deadline.

The relevant object is the retained viable correction set.

## 22. Regret boundary

PASS.

Optionality does not redefine regret.

The chapter permits a multi-coordinate evaluation vector containing expected return, Bayes regret, worst-case regret, functional option count, correction capacity, and correction-cost profile.

Any scalarization or Pareto ordering must be declared separately.

## 23. Safety boundary

PASS.

The chapter does not infer safety, robustness, fairness, calibration, or low tail risk from high optionality/correction capacity.

Such claims require their own contracts or connecting theorems.

## 24. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records OPTIONALITY-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-OPTIONALITY-LOCK-001`.

The canonical bibliography closes:

- `ArrowFisher1974`;
- `Aubin1991Viability`;
- `KlyubinPolaniNehaniv2008`.

The computational witness includes an explicit Claim boundary.

No governed figure is required.

## 25. Downstream handoff

PASS.

After audit, ATLAS-CH-GOVADAPT-001 may inherit:

- viable continuation sets;
- consequence-quotiented functional options;
- conditional post-evidence correction feasibility;
- ex-ante tolerance-indexed correction capacity;
- horizon-relative recoverability;
- the exact equal-value/equal-Bayes-regret separation witness;
- the preservation-cost and action-alias counterexamples.

It must retain explicit targets, horizon, constraints, consequence equivalence, uncertainty semantics, and cost tolerance.

## 26. Final disposition

AUDIT-034 passes after the three formal/source precision repairs.

The durable layer is:

**future uncertainty + viable continuation structure + consequence equivalence + conditional correction cost -> explicit post-evidence correction feasibility and ex-ante correction capacity, kept separate from information gain, regret, and raw action count.**
