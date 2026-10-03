# Chapter Specification — ATLAS-CH-EXPLORE-001

## Identity

- Stable ID: `ATLAS-CH-EXPLORE-001`
- Title: **Exploration and Information Value**
- Part: `ATLAS-PART-DECISION`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-RLBASE-001`
- Implementation issue: #101
- Drafting baseline: `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`

## Contract

Develop bandits, exploration–exploitation, information gain, value of information, and safe exploration.

## Opening obstruction

An action can have lower immediate expected reward and higher finite-horizon value because its observation changes what the decision-maker knows before later choices.

A run that looks locally suboptimal can therefore be globally optimal under epistemic uncertainty.

## Formal objects

Let `theta in Theta` be a finite latent parameter with belief `b_t(theta)`.

Let `A` be the action set, `p(y|theta,a)` the observation law, `r(theta,a,y)` the reward, `H` a finite horizon, and `C_t(b_t)` the admissible action set under the declared constraints.

Posterior update:

`b_{t+1}(theta) proportional to b_t(theta) p(y_{t+1}|theta,a_t)`.

Finite-horizon Bayes value:

`V_t(b)=max_{a in C_t(b)} E[r(theta,a,Y)+V_{t+1}(B(b,a,Y))]`.

For action `a`, define information gain

`IG_t(a)=I_b(theta;Y_{t+1}|a)`.

For one remaining decision after the observation, define decision value of information

`VoI_b(a)=E_Y[max_{a'}E[r(theta,a')|Y,a]]-max_{a'}E[r(theta,a')]`.

The two quantities must remain distinct: information gain is an uncertainty-reduction quantity; value of information is expressed in the declared decision objective.

## Required distinctions

1. exploration versus random action;
2. immediate reward versus continuation value;
3. epistemic uncertainty versus outcome stochasticity;
4. information gain versus value of information;
5. stochastic bandits versus full MDP exploration;
6. optimism/UCB versus posterior sampling;
7. posterior sampling versus information-directed sampling;
8. finite-horizon Bayes value versus asymptotic criteria;
9. unconstrained versus constrained exploration;
10. constraint guarantees versus ordinary expected reward.

## Bandit substrate

A stochastic K-armed bandit has unknown arm reward laws `nu_1,...,nu_K`.

At time `t`, choose one arm `A_t` and observe only `Y_t ~ nu_{A_t}`.

Use this partial-feedback object to explain exploration–exploitation without importing the downstream Regret chapter.

Source roles:

- Auer et al.: upper-confidence-bound allocation;
- Thompson: posterior-probability allocation;
- Russo–Van Roy: information-directed sampling;
- Howard: value of information;
- Moldovan–Abbeel: one explicit MDP safe-exploration formulation.

## Exact computational witness

Two-step Bayesian bandit.

Latent parameter:

`theta in {0,1}`,
`P(theta=1)=2/5`,
`P(theta=0)=3/5`.

Known arm `S`:

- deterministic reward `1/2`;
- no information about `theta`.

Unknown arm `U`:

- reward `theta`;
- one pull reveals `theta`.

Immediate values:

`E[r(U)]=2/5 < 1/2=E[r(S)]`.

If `S` is chosen first, the best second action is again `S`:

`V(S-first)=1`.

If `U` is chosen first:

`V(U-first)=2/5+(2/5)(1)+(3/5)(1/2)=11/10`.

Immediate exploration cost:

`1/2-2/5=1/10`.

Future value of information:

`[(2/5)(1)+(3/5)(1/2)]-1/2=1/5`.

Net two-step advantage:

`1/10`.

With base-2 logs, `IG(U)=h_2(2/5)>0`; `IG(S)=0`.

## Safe-exploration discipline

The phrase "safe exploration" is incomplete unless the constraint is named.

The manuscript must distinguish representative constraint forms such as:

- state/action admissibility;
- probability-of-violation limits;
- cumulative cost budgets;
- returnability/reachability conditions;
- conservative performance floors.

Any guarantee must retain its horizon, probability or deterministic semantics, and model assumptions.

## Downstream handoff

`ATLAS-CH-REGRET-001` may inherit:

- stochastic-bandit notation;
- the exploration–exploitation distinction;
- immediate reward versus information value;
- representative optimism, posterior-sampling, and information-directed mechanisms;
- exploration cost relative to a declared comparator and horizon.

It must develop Bayesian and minimax regret itself.

No downstream Regret or Optionality manuscript is prerequisite authority here.

## Completion criteria

- exact source lock;
- audited RLBASE bind;
- formal/derivation packet;
- exact two-step witness with explicit Claim boundary;
- complete manuscript with epistemic status and references;
- Chapter Ledger promotion;
- Source Register and bibliography closure;
- tranche receipt;
- repository validation green;
- bounded post-draft audit with all in-scope repairs.
