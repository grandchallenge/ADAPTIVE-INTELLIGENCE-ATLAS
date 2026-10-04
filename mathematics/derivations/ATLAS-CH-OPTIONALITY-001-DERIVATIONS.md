# ATLAS-CH-OPTIONALITY-001 — Formal and Derivation Packet

## 1. Decision object

Fix a finite or measurable environment class `Theta`, a belief `b`, state space `S`, action correspondence `A(s)`, transition law `T`, constraint set `K`, and remaining horizon `h`.

Optionality claims are incomplete unless the following are declared:

`D_opt=(Theta,b,S,A,T,K,h,G,U,c_corr)`

where:

- `G` is a consequence-signature map;
- `U={U_theta}` is the family of post-evidence objectives or targets;
- `c_corr` is the declared correction cost.

This object is intentionally richer than a scalar reward function.

## 2. Viable continuation set

Let `Pi_h(s)` be the admissible continuation policies from state `s`.

Define

`V_h(s)
=
{pi in Pi_h(s):
 trajectory(s,pi,theta) respects K for every uncertainty mode required by the declared viability semantics}`.

The uncertainty quantifier must be stated.

Examples include:

- viability for the realized environment;
- robust viability for every `theta in Theta`;
- chance-constrained viability under `b`.

The chapter witness uses deterministic post-action feasibility, so no ambiguity arises there.

## 3. Why raw action count is not enough

Suppose `A(s)={a_1,a_2}` and

`T(s,a_1,theta)=T(s,a_2,theta)`

with identical costs and all downstream consequences.

Then `|A(s)|=2`, but the two labels do not represent two functionally distinct continuations.

Therefore define a consequence signature

`G_s:V_h(s)->Z`

and equivalence

`pi ~_s pi'`
iff
`G_s(pi)=G_s(pi')`.

The functional option set is the quotient

`O_h(s)=V_h(s)/~_s`.

For finite sets, a basic count is

`N_h(s)=|O_h(s)|`.

This count still depends on the declared consequence signature and horizon.

It is not an invariant of the physical world independent of modeling choices.

## 4. Weighted optionality

A count treats all functional options as equally important.

Given a declared nonnegative weight `w:O_h(s)->R_+`, define

`W_h(s)=sum_{o in O_h(s)} w(o)`.

This is useful only when `w` has independent meaning.

A dominated, unsafe, or irrelevant option need not carry positive weight.

Therefore the chapter does not define "more options is better" by cardinality alone.

## 5. Post-evidence correction target

Let evidence `y` induce posterior `b_y` or reveal an environment label `theta`.

For each `theta`, define a target set of acceptable continuation outcomes

`B_theta`.

Let `c_corr(pi,theta)>=0` be a correction cost when `pi` reaches `B_theta`.

Define

`k_h(s,theta)
=
inf { c_corr(pi,theta):
       pi in V_h(s),
       outcome(s,pi,theta) in B_theta }`.

If the feasible set is empty:

`k_h(s,theta)=+infinity`.

This extended-real convention makes the hard/soft distinction explicit.

## 6. Tolerance-indexed correction capacity

For finite `Theta` and tolerance `epsilon>=0`:

`CC_{h,epsilon}(s;b)
=
sum_theta b(theta) 1{k_h(s,theta)<=epsilon}`.

Properties:

1. `0<=CC<=1`;
2. `CC` is nondecreasing in `epsilon`;
3. hard infeasibility contributes zero for every finite `epsilon`;
4. finite but costly correction can appear only after `epsilon` crosses the required cost;
5. `CC` depends on `b`, targets, cost semantics, and horizon.

Proof of monotonicity:

if `epsilon_1<=epsilon_2`, then

`{theta:k_h(s,theta)<=epsilon_1}
 subseteq
 {theta:k_h(s,theta)<=epsilon_2}`.

Taking nonnegative belief mass proves

`CC_{h,epsilon_1}(s;b)
<=
CC_{h,epsilon_2}(s;b)`.

## 7. Information gain is not correction capacity

Let `Y` be evidence.

Information gain can be measured by

`I(Theta;Y)`.

This quantity depends on the observation channel.

Correction capacity depends on the post-observation feasible continuation set.

Two states can therefore have the same observation channel and the same `I(Theta;Y)`, yet different `CC`.

The exact witness realizes this separation with perfect observation in both branches.

## 8. Recoverability

Let `B subseteq S` be a declared recovery set.

For state `s'`, define horizon-`h` recoverability:

`Rec_h(s';B)=1`

iff there exists an admissible viable continuation of length at most `h` that reaches `B`.

An action `a` taken at `s` is irreversible relative to `B,h` when

`Rec_h(T(s,a,theta);B)=0`

under the declared uncertainty semantics.

Thus irreversibility is not absolute.

Changing `B`, `h`, the state abstraction, or admissible controls can change the classification.

## 9. Regret remains separate

From the audited prerequisite, regret is comparator-relative.

For environment-specific comparator value `V_theta^*` and policy return `G(pi,theta)`, the witness uses

`Reg(pi,theta)=V_theta^*-G(pi,theta)`.

Bayesian regret is

`BR(pi;b)=sum_theta b(theta) Reg(pi,theta)`.

Optionality does not modify this definition.

Instead, the evaluation vector can contain both:

`E(pi)
=
(E_b[G(pi,theta)],
 BR(pi;b),
 sup_theta Reg(pi,theta),
 CC_{h,epsilon}(s_pi;b),
 N_h(s_pi))`.

Scalarization, Pareto comparison, or constraints must be declared separately.

## 10. Exact witness setup

Let

`Theta={L,R}`,
`b(L)=b(R)=1/2`.

At stage 0 the learner chooses between `P` and `C_L`.

Action `P`:

- immediate reward `-1/2`;
- next state `s_P`;
- terminal feasible actions `A(s_P)={L,R}`.

Action `C_L`:

- immediate reward `0`;
- next state `s_L`;
- terminal feasible actions `A(s_L)={L}`.

At stage 1, `theta` is observed perfectly in either state.

Terminal reward:

`u_theta(a)=1{a=theta}`.

Policy `pi_P` chooses `P`, then terminal action `theta`.

Policy `pi_L` chooses `C_L`, then the only feasible terminal action L.

## 11. Exact return calculation

For `pi_P`:

`G(pi_P,L)=-1/2+1=1/2`.

`G(pi_P,R)=-1/2+1=1/2`.

Therefore:

`E_b G(pi_P)=1/2`.

For `pi_L`:

`G(pi_L,L)=0+1=1`.

`G(pi_L,R)=0+0=0`.

Therefore:

`E_b G(pi_L)=1/2(1)+1/2(0)=1/2`.

Hence the prior action-value gap is exactly zero.

## 12. Exact regret calculation

Let an environment-informed comparator choose the matching commitment `C_theta` at stage 0 and obtain value

`V_theta^*=1`

for both environments.

Then:

`Reg(pi_P,L)=1-1/2=1/2`;

`Reg(pi_P,R)=1-1/2=1/2`.

So:

`BR(pi_P;b)=1/2`.

For `pi_L`:

`Reg(pi_L,L)=0`;

`Reg(pi_L,R)=1`.

So:

`BR(pi_L;b)=1/2`.

Thus prior value and Bayesian regret both tie.

Worst-case regret does not tie:

`W(pi_P)=1/2`;

`W(pi_L)=1`.

This is allowed: optionality is not claimed to be invisible to every other risk criterion.

## 13. Exact functional option sets

Use terminal consequence identity as the consequence signature.

At `s_P`:

`O_1(s_P)={L,R}`,
so
`N_1(s_P)=2`.

At `s_L`:

`O_1(s_L)={L}`,
so
`N_1(s_L)=1`.

The two states are therefore distinct in functional optionality despite equal prior action value.

## 14. Exact correction capacity

Define target:

`B_theta={terminal action theta}`.

Set correction cost:

`c_corr(a,theta)=0`
when `a=theta`.

If no matching action is feasible, correction is infeasible and cost is `+infinity`.

Then:

`k_1(s_P,L)=0`;
`k_1(s_P,R)=0`.

Hence:

`CC_{1,0}(s_P;b)=1`.

For the committed state:

`k_1(s_L,L)=0`;
`k_1(s_L,R)=+infinity`.

Hence:

`CC_{1,0}(s_L;b)=1/2`.

## 15. Exact information separation

Because stage 1 reveals `theta` perfectly in either branch:

`H(Theta)=1 bit`;

`H(Theta|Y)=0`;

therefore

`I(Theta;Y)=1 bit`

for both branches.

Yet:

`CC_{1,0}(s_P;b)=1`;

`CC_{1,0}(s_L;b)=1/2`.

So equal information acquisition does not imply equal correction capacity.

## 16. Preservation-cost family

Replace preservation cost `1/2` with `c in [0,1]`.

Then:

`Q(P)=1-c`;

`Q(C_L)=1/2`.

Therefore:

- if `c<1/2`, preservation has higher expected return;
- if `c=1/2`, they tie;
- if `c>1/2`, commitment has higher expected return.

Functional option counts and zero-tolerance correction capacities remain:

- preserve: `N=2`, `CC=1`;
- commit-left: `N=1`, `CC=1/2`.

At `c=3/4`:

`Q(P)=1/4 < 1/2 = Q(C_L)`.

This is the exact counterexample to a universal "preserve more options" rule.

## 17. Alias counterexample

State `s_A` exposes one terminal action `x`.

State `s_B` exposes two labels `x_1,x_2`.

Suppose both labels have exactly the same transition, cost, and consequence signature as `x`.

Then raw counts are:

`|A(s_A)|=1`;

`|A(s_B)|=2`.

But the quotient option sets satisfy:

`|O(s_A)|=|O(s_B)|=1`.

Therefore raw action count is not representation invariant.

## 18. Relation to empowerment

Empowerment is an information-theoretic channel-capacity construction over action-to-future-sensor influence.

The Atlas correction capacity here is target- and feasibility-based.

They can correlate, but neither definition implies equality.

A high-capacity actuation channel can include consequences irrelevant to the current correction targets.

Conversely, a small discrete action set can retain exactly the two corrections required by a binary future uncertainty.

## 19. Relation to viability theory

Viability theory supplies a mature language for controlled dynamics under state constraints.

This chapter uses that precedent only to insist that a continuation must be feasible under declared constraints before it is counted as a viable option.

The quotient, correction-cost, and correction-capacity definitions above are Atlas-owned finite constructions.

## 20. Downstream interface

After audit, downstream governed-adaptation work may consume:

- `V_h(s)`: viable continuations;
- `O_h(s)`: functional option classes;
- `k_h(s,theta)`: extended-real correction cost;
- `CC_{h,epsilon}(s;b)`: tolerance-indexed correction capacity;
- `Rec_h(s;B)`: horizon-relative recoverability;
- the exact equal-value/equal-Bayes-regret separation witness.

It must retain the declared target, horizon, constraints, uncertainty semantics, and consequence equivalence.
