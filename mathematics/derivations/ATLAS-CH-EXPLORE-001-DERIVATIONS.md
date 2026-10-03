# ATLAS-CH-EXPLORE-001 — Formal and Derivation Packet

## 1. Purpose

This packet separates four quantities that informal discussions of exploration often collapse:

1. immediate expected reward;
2. epistemic uncertainty;
3. information gained by an observation;
4. decision value created by that information.

An action can be unattractive myopically and still be optimal over a finite horizon because its observation changes later action choice.

## 2. RLBASE handoff

ATLAS-CH-RLBASE-001 supplies the controlled stochastic substrate

`M=(S,A,P,r,gamma,rho_0)`

together with policy, return, value, Bellman recursion, model-based/model-free boundaries, and partial-observability discipline.

EXPLORE-001 adds uncertainty about a latent environment or reward parameter and asks how actions may reduce that uncertainty.

It preserves the RLBASE rule that optimality is always relative to a declared model and objective.

## 3. Bayesian sequential-decision object

Let:

- `Theta` be a finite latent-parameter set;
- `b_t(theta)` be the current posterior belief;
- `A` be the action set;
- `p(y|theta,a)` be the observation law;
- `r(theta,a,y)` be the immediate reward;
- `C_t(b_t) subseteq A` be the admissible action set under the declared constraints;
- `H` be a finite horizon.

After choosing `a_t` and observing `y_{t+1}`,

`b_{t+1}(theta)
=
b_t(theta)p(y_{t+1}|theta,a_t)
/ sum_{theta'} b_t(theta')p(y_{t+1}|theta',a_t)`

when the denominator is nonzero.

Let `B(b,a,y)` denote this update.

The finite-horizon Bayes recursion is

`V_t(b)
=
max_{a in C_t(b)}
E_{theta~b,y~p(.|theta,a)}
[
r(theta,a,y)+V_{t+1}(B(b,a,y))
]`

with terminal condition `V_{H+1}=0`.

Exploration arises because action choice affects both reward and the next belief.

## 4. Epistemic uncertainty versus outcome stochasticity

Write schematically

`Y=mu_theta(a)+epsilon`.

Uncertainty in `theta` is epistemic relative to this model: observations can update the belief over `theta`.

Conditional randomness `epsilon` can remain even when `theta` is known.

Therefore an action can have:

- high outcome variance but little information about `theta`;
- low outcome variance and high information about `theta`;
- high information that is irrelevant to future action choice.

Variance, information, and decision value are distinct objects.

## 5. Information gain

For fixed belief `b` and action `a`, let the next observation be `Y`.

Define

`IG_b(a)=I_b(Theta;Y|a)`.

Equivalently,

`IG_b(a)=H_b(Theta)-E_Y[H(Theta|Y,a)]`.

Information gain is an expected reduction in uncertainty.

Its units depend on the logarithm base.

It does not have reward units.

## 6. One-step decision value of information

Suppose exactly one decision remains after the observation.

Without new information, the best expected future reward is

`J_0(b)=max_{a'} E_{theta~b}[r(theta,a')]`.

If action `a` is taken first, observation `Y` arrives, and the posterior becomes `b_Y`, the expected future reward is

`J_1(b,a)=E_Y[max_{a'}E_{theta~b_Y}[r(theta,a')]]`.

Define

`VoI_b(a)=J_1(b,a)-J_0(b)`.

Under this idealized setup, `VoI_b(a)>=0`: after receiving an observation, the future decision-maker can always ignore it and choose the same action available without the observation.

This nonnegativity statement assumes the future action set and reward model are unchanged and that observation costs are accounted for separately.

## 7. Exploration cost

Let immediate Bayesian reward be

`m_b(a)=E_{theta,Y}[r(theta,a,Y)]`.

Let `a_myopic` maximize `m_b(a)`.

The immediate exploration cost of another action `a` is

`c_exp(a)=m_b(a_myopic)-m_b(a)`.

With one future decision remaining, an informative action can be preferred when its future decision value exceeds its immediate exploration cost after other continuation differences are accounted for.

Information quantity alone does not determine that comparison.

## 8. Exact two-step witness

Let

`Theta={0,1}`

with prior

`P(theta=1)=2/5`,
`P(theta=0)=3/5`.

There are two actions.

Known action `S` gives deterministic reward

`r(S)=1/2`

and gives no information about `theta`.

Unknown action `U` gives reward

`r(U)=theta`

and therefore reveals `theta` exactly.

### Myopic values

`m(S)=1/2`.

`m(U)=E[theta]=2/5`.

So myopic exploitation selects `S`.

Immediate exploration cost:

`c_exp(U)=1/2-2/5=1/10`.

### If S is chosen first

No belief update occurs.

At the second and final decision, `S` remains myopically best.

Hence

`V(S-first)=1/2+1/2=1`.

### If U is chosen first

Immediate expected reward is

`2/5`.

If `theta=1`, which has probability `2/5`, the posterior becomes degenerate at 1 and the second action is `U`, giving reward 1.

If `theta=0`, which has probability `3/5`, the posterior becomes degenerate at 0 and the second action is `S`, giving reward `1/2`.

Expected second-step reward is

`J_1
=
(2/5)(1)+(3/5)(1/2)
=
7/10`.

Without information, the best second-step reward would be `1/2`.

Therefore

`VoI(U)=7/10-1/2=1/5`.

Total value of exploring first is

`V(U-first)=2/5+7/10=11/10`.

Net advantage over choosing the known arm first is

`11/10-1=1/10`.

The decomposition is exact:

`VoI(U)-c_exp(U)=1/5-1/10=1/10`.

## 9. Information gain in the witness

Before choosing `U`,

`H(Theta)=h_2(2/5)`

under base-2 entropy.

After observing `U), posterior entropy is zero.

Thus

`IG(U)=h_2(2/5)>0`.

Action `S` gives no information:

`IG(S)=0`.

The witness separates:

- information gain: `h_2(2/5)` bits;
- value of information: `1/5` reward units;
- immediate exploration cost: `1/10` reward units;
- net two-step advantage: `1/10` reward units.

## 10. Stochastic bandits

A stochastic K-armed bandit contains unknown reward laws

`nu_1,...,nu_K`.

At each time `t`, the learner chooses arm `A_t` and observes only

`Y_t~nu_{A_t}`.

The unchosen arm outcomes are not observed.

This partial feedback makes the bandit a minimal exploration–exploitation problem.

It is not a full MDP because action does not, in the basic bandit model, introduce a nontrivial controlled state-transition process.

## 11. Optimism and upper confidence bounds

An optimism principle chooses an action using an estimate plus an uncertainty allowance, schematically

`a_t in argmax_i [mu_hat_i(t)+beta_i(t)]`.

Uncertain arms can therefore be selected even when their point estimates are not maximal.

Auer, Cesa-Bianchi, and Fischer give finite-time analysis for representative upper-confidence-bound policies in stochastic bandits.

A confidence bound is not a posterior probability.

The two objects can encourage exploration for different mathematical reasons.

## 12. Posterior sampling

Thompson's probability-matching idea can be written in modern Bayesian language as:

1. sample a latent arm/model parameter from the posterior;
2. choose the action optimal for that sampled parameter;
3. observe feedback;
4. update the posterior.

Exploration emerges because posterior uncertainty changes which sampled model is temporarily treated as true.

This is distinct from adding a deterministic confidence bonus.

## 13. Information-directed sampling

Russo and Van Roy define information-directed sampling through a tradeoff between expected single-period regret and mutual information about the optimal action.

The Atlas uses the source for one conceptual lesson:

an action's exploration value depends on **which uncertainty it resolves**, not merely how large its uncertainty is.

An observation can contain substantial information that has little effect on the best future action.

Conversely, a modest amount of information about the identity of the best action can have large decision value.

## 14. Information gain is not value of information

Two observations can carry equal mutual information about `Theta` and have different decision value if only one changes the optimal action.

Two experiments can also have different information gain and the same decision value if both lead to the same future action.

Howard's information-value perspective makes the dependence on consequences explicit.

Therefore

`IG(a)`

and

`VoI(a)`

belong to different semantic layers.

One measures uncertainty reduction.

The other measures improvement in attainable decision value under a declared objective.

## 15. Constrained exploration

Let `C_t(b)` denote the currently admissible actions or policies under a declared constraint.

Different constraint semantics include:

- state or action admissibility;
- probability-of-violation limits;
- cumulative cost budgets;
- returnability or reachability requirements;
- conservative performance floors.

These are not interchangeable.

Moldovan and Abbeel provide one concrete safe-exploration formulation for MDPs based on ergodicity/returnability structure and a restricted set of guaranteed-safe policies.

The Atlas extracts only the general rule:

**a safety constraint changes the feasible exploration problem.**

It is not merely another exploration bonus.

## 16. Constraint–information–reward tradeoff

If the most informative action is inadmissible, the constrained optimum may learn more slowly.

If a guarantee is probabilistic, the probability level and model assumptions are part of the claim.

If the constraint is only in expectation, it does not imply pathwise satisfaction.

If the constraint concerns returnability, one-step admissibility may not be sufficient.

A mature constrained-exploration claim therefore exposes:

- constrained quantity;
- threshold or admissible set;
- horizon;
- guarantee type;
- probability/confidence level when applicable;
- model assumptions;
- resulting feasible action/policy set.

## 17. Downstream interface

ATLAS-CH-REGRET-001 may consume:

- stochastic bandit object;
- immediate versus continuation value;
- exploration cost;
- representative optimism, posterior-sampling, and information-directed mechanisms;
- distinction between Bayesian information value and confidence-based exploration.

It must independently develop regret definitions, Bayesian/minimax criteria, lower bounds, and the scope of regret guarantees.
