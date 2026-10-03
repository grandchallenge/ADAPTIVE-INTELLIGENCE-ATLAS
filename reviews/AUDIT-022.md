# AUDIT-022 — Exploration and Information Value

## Disposition

**PASS WITH TWO FORMAL/INTEGRITY REPAIRS AND ONE SOURCE-SCOPE REPAIR**

ATLAS-CH-EXPLORE-001 remains at draft-v0.1.

The chapter correctly develops exploration as purposeful information acquisition under sequential decision uncertainty. It separates immediate reward, epistemic uncertainty, observation information, decision value of information, exploration cost, continuation value, and constrained action sets.

The audit made three bounded repairs:

1. the one-step value-of-information equations now preserve the chapter's original reward signature by defining the expected one-step payoff
   `bar r(theta,a')=E_{Y'~p(.|theta,a')}[r(theta,a',Y')]`
   before forming `J_0), `J_1), and `VoI`;
2. one malformed Markdown/notation delimiter in the entropy paragraph was repaired;
3. the Moldovan–Abbeel description was narrowed from an "ergodicity/returnability structure" characterization to the source-supported ergodicity-based safety formulation and restricted guaranteed-safe policy set.

No exact witness result, Bayesian posterior update, bandit definition, information-gain boundary, UCB/Thompson/IDS distinction, downstream handoff, or Chapter Ledger state required reversal.

## Audited baseline

- implementation merge:
  `2de8b7b6fd30f47e066eb475bbd282583926b681`;
- implementation PR:
  #101;
- audit issue:
  #102;
- chapter:
  `ATLAS-CH-EXPLORE-001`.

## 1. Hard prerequisite

PASS.

The source lock binds:

- `ATLAS-CH-RLBASE-001` manuscript blob
  `a99f78b788b97bc1bb3346ca1f1b97802c0f84db`;
- `AUDIT-017` blob
  `8b7a1f9b61c15ab9c2c010ea538e25c11a7ed1cc`.

The chapter consumes the audited MDP, reward, return, value, Bellman, policy, model, uncertainty, and observability substrate.

No Regret or Optionality manuscript is used as hidden prerequisite authority.

## 2. External source identities and scope

PASS AFTER SOURCE-SCOPE REPAIR.

The source lock identifies:

- Peter Auer, Nicolò Cesa-Bianchi, and Paul Fischer, "Finite-time Analysis of the Multiarmed Bandit Problem," Machine Learning 47, 235–256 (2002), DOI `10.1023/A:1013689704352`;
- William R. Thompson, "On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples," Biometrika 25(3–4), 285–294 (1933), DOI `10.1093/biomet/25.3-4.285`;
- Daniel Russo and Benjamin Van Roy, "Learning to Optimize via Information-Directed Sampling," NeurIPS 27 (2014), arXiv `1403.5556`;
- Ronald A. Howard, "Information Value Theory," IEEE Transactions on Systems Science and Cybernetics 2(1), 22–26 (1966), DOI `10.1109/TSSC.1966.300074`;
- Teodor Mihai Moldovan and Pieter Abbeel, "Safe Exploration in Markov Decision Processes," ICML (2012), arXiv `1205.4810`.

The source roles remain bounded:

- Auer et al. supports representative finite-time stochastic-bandit/UCB analysis;
- Thompson supports posterior-probability allocation;
- Russo–Van Roy supports information-directed sampling;
- Howard supports decision-theoretic value of information;
- Moldovan–Abbeel supports one explicit ergodicity-based MDP safety formulation.

The last source is not promoted into a universal definition of safe exploration.

## 3. Bayesian exploration state

PASS.

The chapter uses:

- finite latent parameter `Theta`;
- posterior belief `b_t(theta)`;
- action set `A`;
- observation law `p(y|theta,a)`;
- immediate reward `r(theta,a,y)`;
- finite horizon `H`;
- constrained action set `C_t(b)`.

The posterior update is a standard finite Bayes update when the normalizing denominator is nonzero.

The finite-horizon recursion correctly exposes both immediate reward and belief-dependent continuation value.

## 4. Epistemic versus outcome uncertainty

PASS.

The schematic decomposition

`Y=mu_theta(a)+epsilon`

is used only to distinguish model/parameter uncertainty from conditional outcome randomness.

The chapter does not claim that all stochasticity can be learned away.

It also correctly refuses to equate variance with information value.

## 5. Information gain

PASS.

The chapter defines

`IG_b(a)=I_b(Theta;Y|a)`

and the entropy-reduction equivalent.

It states explicitly that information gain is an uncertainty-reduction quantity measured in information units, not reward units.

## 6. Value of information

PASS AFTER FORMAL REPAIR.

The draft originally reused the full reward symbol `r(theta,a,y)` and then wrote `r(theta,a')` inside the one-step value-of-information equations.

That silently changed the function signature.

The repaired formulation defines

`bar r(theta,a')=E_{Y'~p(.|theta,a')}[r(theta,a',Y')]`

and then uses

`J_0(b)=max_{a'}E_b[bar r(theta,a')]`

and

`J_1(b,a)=E_Y[max_{a'}E[bar r(theta,a')|Y,a]]`.

Thus

`VoI_b(a)=J_1(b,a)-J_0(b)`

is notation-consistent.

The stated nonnegativity boundary remains correct under the declared idealization: unchanged future action set and reward model, with acquisition cost accounted for separately.

## 7. Exploration cost

PASS.

Immediate Bayesian reward and the myopic comparator are distinct from future information value.

The chapter does not claim that positive information gain is sufficient to justify exploration.

## 8. Exact two-step witness

PASS.

Independent exact rational replay confirms:

- `safe_total=1`;
- expected future reward after the informative action = `7/10`;
- `unknown_total=11/10`;
- immediate exploration cost = `1/10`;
- value of information = `1/5`;
- net advantage = `1/10`.

The witness's Claim boundary is correct.

It proves only the declared two-step Bayesian decision result.

## 9. Information gain in the witness

PASS AFTER INTEGRITY REPAIR.

The informative action reveals `theta` exactly, reducing posterior entropy from `h_2(2/5)` to zero.

The known action leaves the posterior unchanged.

A malformed Markdown delimiter in the derivation was repaired.

No mathematical value changed.

## 10. Stochastic bandit boundary

PASS.

A bandit is defined through unknown arm reward laws and chosen-arm-only feedback.

The chapter explicitly distinguishes this from a full MDP with controlled state transitions.

It does not import the downstream Regret chapter to define the exploration object.

## 11. Optimism/UCB

PASS.

The schematic upper-confidence rule

`argmax_i [mu_hat_i(t)+beta_i(t)]`

is presented as a representative optimism mechanism.

Confidence bounds are explicitly distinguished from posterior probabilities.

## 12. Posterior sampling

PASS.

The chapter accurately presents Thompson's allocation idea as posterior-probability-based and clearly labels the sample-model/choose-optimal-action description as a modern Bayesian rendering.

It is not collapsed into UCB.

## 13. Information-directed sampling

PASS.

The chapter uses Russo–Van Roy only for the representative idea of trading expected short-term regret against information about the optimal action.

It does not import the full regret theory into EXPLORE-001.

## 14. Information gain versus decision value

PASS.

The chapter explicitly permits:

- equal information gain with different decision values;
- different information gain with equal decision values.

Howard's information-value perspective is used at the correct level: consequences and future decisions matter, not probability structure alone.

## 15. Safe/constrained exploration

PASS AFTER SOURCE-SCOPE REPAIR.

The chapter correctly requires the safety notion to be explicit.

Representative constraint forms are kept distinct:

- admissible state/action sets;
- probability-of-violation limits;
- cumulative cost budgets;
- reachability/returnability conditions;
- conservative performance floors.

The Moldovan–Abbeel sentence now stays within the source-supported ergodicity-based formulation.

The broader taxonomy is Atlas synthesis, not attributed wholesale to that paper.

## 16. Horizon discipline

PASS.

The exact witness is finite-horizon.

The manuscript states that exploration value is horizon-dependent and does not transfer a long-horizon or asymptotic criterion into the two-step witness.

## 17. Downstream handoff

PASS.

ATLAS-CH-REGRET-001 may inherit:

- stochastic-bandit notation;
- exploration–exploitation distinction;
- exploration cost;
- immediate-versus-continuation decomposition;
- representative optimism, posterior-sampling, and information-directed mechanisms.

It must independently develop Bayesian and minimax regret and the limits of regret guarantees.

## 18. Integrity

PASS subject to merge validation.

The Chapter Ledger records ATLAS-CH-EXPLORE-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-EXPLORE-LOCK-001`.

The bibliography closes all manuscript citation keys.

The witness contains an explicit `## Claim boundary`.

No governed figure is required; the exact rational witness is clearer as equations and a replay block.

Repository validation is the final audit merge gate.

## 19. Final disposition

AUDIT-022 passes with the bounded repairs above.

The chapter now supplies a dependency-safe exploration layer:

**uncertainty -> informative action -> observation -> belief update -> changed future decision -> information value, subject to cost, horizon, state change, and constraints.**

This is sufficient for the downstream Regret chapter to analyze the price of learning without treating exploration itself as regret.
