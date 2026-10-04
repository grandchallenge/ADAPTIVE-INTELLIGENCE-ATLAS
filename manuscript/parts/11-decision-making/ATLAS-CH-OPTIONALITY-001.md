# Optionality and Correction Capacity
<!-- ATLAS-CH-OPTIONALITY-001 -->

**Epistemic status:** audited Regret prerequisite + established irreversibility/viability/empowerment precedents + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-OPTIONALITY-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-OPTIONALITY-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-OPTIONALITY-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-OPTIONALITY-001.yaml

A system can know exactly what went wrong and still be unable to correct it.

That is the problem this chapter isolates.

The previous Regret chapter made one boundary explicit: low reward regret does not automatically imply recoverability or preserved optionality.

Here we make those missing objects visible.

The central distinction is:

> information tells an agent what correction is needed; optionality determines whether a correction remains available.

Those two quantities can move together.

They need not.

## 1. The door that information cannot reopen

Imagine two stage-0 decisions.

One decision preserves both exits until new evidence arrives, but keeping both exits available has a cost.

The other commits to the left exit immediately and costs nothing.

Later, the world reveals whether left or right was needed.

If both policies had different expected values, ordinary value comparison might settle the choice.

The more interesting case is when the preservation cost is tuned so that the two policies have exactly the same prior expected return.

Even then, they do not leave the same future decision problem.

One leaves two corrections.

The other leaves one.

That residue is optionality.

The door metaphor is deliberately limited.

Real control systems rarely have literal doors, and "reopening" may be possible at finite cost rather than impossible.

The mathematics therefore needs to represent both hard loss of feasibility and softer increases in correction cost.

## 2. Optionality needs a contract

"Keep options open" is incomplete advice.

Options relative to what?

A usable optionality claim must name at least:

- the state abstraction;
- the future horizon;
- admissible controls;
- viability or safety constraints;
- the uncertainty that may later resolve;
- the outcomes that count as distinct;
- the post-evidence targets;
- the cost allowed for correction.

We package these as

`D_opt=(Theta,b,S,A,T,K,h,G,U,c_corr)`.

Here:

- `Theta` is the environment class;
- `b` is a belief over environments when one is used;
- `S` is the state space;
- `A` is the action correspondence;
- `T` is the transition model;
- `K` is the declared viability constraint;
- `h` is the remaining horizon;
- `G` identifies functionally distinct consequences;
- `U` describes post-evidence targets or utilities;
- `c_corr` measures correction cost.

Without these declarations, "optionality" tends to collapse into metaphor.

## 3. Viable continuations come before valuable continuations

Let

`Pi_h(s)`

be the admissible continuation policies from state `s` for the remaining horizon.

Define the viable set

`V_h(s)`

as those continuations that satisfy the declared constraints under the declared uncertainty semantics.

This is a feasibility object.

It does not say that every viable continuation is good.

That distinction matters because optionality is not simply a larger value function.

Viability theory provides a mature mathematical language for controlled evolution under state constraints [@Aubin1991Viability].

The Atlas uses that precedent conservatively.

The finite definitions here are ours, but they inherit one discipline from viability theory:

> a continuation should not be counted as available when the governing constraints make it inadmissible.

## 4. Why counting buttons fails

Suppose a console has one button.

Now duplicate the button label ten times without changing anything the system can actually do.

The raw action count increased by a factor of ten.

The real choice set did not.

To remove this trivial representation dependence, attach a consequence signature

`G_s(pi)`

to each viable continuation.

Declare:

`pi ~_s pi'`

when they have the same consequence signature.

Then define the functional option set:

`O_h(s)=V_h(s)/~_s`.

A finite count

`N_h(s)=|O_h(s)|`

now counts distinct consequence classes rather than labels.

This is still not absolute.

Change the horizon or the consequence signature and the quotient can change.

That is not a defect.

It is a reminder that optionality is always relative to what distinctions matter downstream.

## 5. Cardinality is not value

Even functional option count can mislead.

One state might offer:

- two useful recoveries.

Another might offer:

- the same two useful recoveries;
- twelve irrelevant actions;
- one catastrophic action.

A larger set is not automatically better.

If a weight function `w` has independent meaning, one may define:

`W_h(s)
=
sum_{o in O_h(s)} w(o)`.

But the weights then carry substantive assumptions.

The Atlas therefore treats option count as a descriptive coordinate, not a universal utility.

## 6. Irreversibility enters when uncertainty meets time

Arrow and Fisher's classic analysis made a structural point that remains useful far beyond its environmental application: when actions are irreversible and new information may arrive later, preserving the ability to respond can have decision value [@ArrowFisher1974].

The Atlas does not import their model wholesale.

We take only the structural lesson:

- uncertainty may resolve after action;
- an early commitment may remove later responses;
- the value of waiting or preserving flexibility depends on the cost of doing so.

This last clause is essential.

Irreversibility does not imply "never commit."

It makes the timing and cost of commitment part of the decision.

## 7. Recoverability is relative, not mystical

Let `B` be a declared recovery set.

Define:

`Rec_h(s;B)=1`

when some admissible viable continuation reaches `B` within horizon `h`.

An action is irreversible relative to `B,h` when the resulting state has

`Rec_h=0`.

This definition exposes four facts that ordinary language often hides.

First, irreversibility depends on the state abstraction.

Second, it depends on the recovery target.

Third, it depends on the available controls and constraints.

Fourth, it depends on the time budget.

A cracked component may be irreversible at the material level and still be operationally recoverable by replacement.

A software deployment may be reversible in principle and effectively irreversible under a five-second deadline.

## 8. A bad outcome is not the same as irreversible action

Suppose a stochastic transition causes a temporary performance drop, but the original operating region remains reachable in one step.

That is a bad outcome.

It is not irreversible.

Conversely, a commitment may have excellent immediate reward while permanently deleting one future response.

That can be irreversible without being immediately bad.

The distinction matters because tail risk and optionality are different evaluation axes.

## 9. Correction cost

After evidence arrives, the relevant question is no longer merely "what can I do?"

It is:

> can I still reach an acceptable response for the world I now believe I am in?

For environment `theta`, let `B_theta` be an acceptable target set.

After evidence resolves the environment to `theta`, let `V_h(s;theta)` be the viable continuation set under that resolved environment. Define:

`k_h(s,theta)`

as the least declared correction cost among continuations in `V_h(s;theta)` that reach `B_theta`.

If no such continuation exists:

`k_h(s,theta)=+infinity`.

This one convention cleanly separates two failure modes.

Soft degradation:

- the correction still exists;
- it simply costs more.

Hard feasibility loss:

- the target is no longer reachable under the declared contract.

The latter is the sharp form of lost correction capacity.

## 10. Conditional correction and ex-ante correction capacity

After evidence resolves the environment to `theta`, define the conditional correction indicator:

`C_{h,epsilon}(s,theta)
=
1{k_h(s,theta)<=epsilon}`.

This is the post-evidence statement: in this environment, can the declared correction still be executed within tolerance?

Before the evidence arrives, define the ex-ante belief-weighted summary:

`CC_{h,epsilon}(s;b)
=
sum_theta b(theta) C_{h,epsilon}(s,theta)`.

Interpretation:

`CC`

is the pre-evidence probability mass of environments for which a satisfactory correction will remain reachable within the declared tolerance.

The quantity lies in `[0,1]`.

It is nondecreasing in `epsilon`.

It exposes hard infeasibility because an infinite correction cost never enters at finite tolerance.

This is not the only possible optionality functional.

It is useful because its semantics are explicit and testable.

## 11. The exact equal-value witness

Now instantiate the opening story exactly.

Let:

`Theta={L,R}`

with prior:

`P(L)=P(R)=1/2`.

At stage 0 the admissible action set is `{P,C_L,C_R}`.

Preserve `P`:

- pay immediate reward `-1/2`;
- move to state `s_P`;
- retain terminal actions `{L,R}`.

Commit-left `C_L`:

- pay immediate reward `0`;
- move to state `s_L`;
- retain only terminal action `{L}`.

Commit-right `C_R` is the symmetric admissible commitment:

- pay immediate reward `0`;
- move to state `s_R`;
- retain only terminal action `{R}`.

The learner-policy comparison remains `P` versus `C_L`. Declaring `C_R` makes the environment-informed comparator below a member of the declared stage-0 action set.

At stage 1, observe `theta` perfectly.

Terminal reward is:

`u_theta(a)=1`

when the terminal action matches the environment, and zero otherwise.

The preserve policy waits for the observation and matches it.

The commit-left policy can only choose left.

## 12. Prior value does not separate the policies

For preservation:

`G(pi_P,L)=1/2`;

`G(pi_P,R)=1/2`.

Therefore:

`E[G(pi_P)]=1/2`.

For commitment:

`G(pi_L,L)=1`;

`G(pi_L,R)=0`.

Therefore:

`E[G(pi_L)]=1/2`.

The exact prior action-value gap is zero.

A scalar expected-value comparison is silent.

## 13. Bayesian regret can also tie

Use a clairvoyant environment-informed comparator that knows `theta` before stage 0 and chooses the declared matching commitment `C_theta`.

Its value is:

`V_L^*=V_R^*=1`.

Preservation regret is:

- `1/2` in L;
- `1/2` in R.

So Bayesian regret is:

`1/2`.

Commit-left regret is:

- `0` in L;
- `1` in R.

Its Bayesian regret is also:

`1/2`.

Thus the two policies tie both in prior expected return and Bayesian regret.

This does not mean every regret criterion ties.

Worst-case regret is:

- preserve: `1/2`;
- commit-left: `1`.

Optionality is a separate coordinate, not an assertion that all other coordinates are blind.

## 14. The future feasible sets do separate them

At `s_P`:

`O_1(s_P)={L,R}`.

At `s_L`:

`O_1(s_L)={L}`.

So the functional option counts are:

- preserve: `2`;
- commit-left: `1`.

This difference is not created by extra labels.

The two preserved options have distinct terminal consequences.

## 15. Correction capacity separates them more sharply

Let the post-evidence target in environment `theta` be:

choose terminal action `theta`.

Give a successful matching correction cost zero.

If the matching action is unavailable, correction cost is infinity.

Then in the preserved state:

`k(s_P,L)=0`;

`k(s_P,R)=0`.

Therefore the post-evidence indicators satisfy:

`C_{1,0}(s_P,L)=C_{1,0}(s_P,R)=1`,

and the ex-ante capacity is:

`CC_{1,0}(s_P;b)=1`.

In the committed-left state:

`k(s_L,L)=0`;

`k(s_L,R)=+infinity`.

Therefore:

`C_{1,0}(s_L,L)=1`;

`C_{1,0}(s_L,R)=0`;

and the ex-ante capacity is:

`CC_{1,0}(s_L;b)=1/2`.

The prior value tie hid a real asymmetry in the ability to act on future evidence.

## 16. Information is identical

The environment is revealed perfectly in both branches.

Thus:

`H(Theta)=1 bit`;

`H(Theta|Y)=0`;

`I(Theta;Y)=1 bit`.

The information gain is exactly the same.

Yet correction capacity differs by a factor of two.

This is the cleanest lesson in the chapter:

> learning the answer and retaining a feasible response to the answer are different resources.

## 17. Empowerment is related, but not identical

Klyubin, Polani, and Nehaniv formalize empowerment as an information-theoretic capacity of the action-to-future-sensor channel and explicitly interpret it as keeping options open [@KlyubinPolaniNehaniv2008].

That is an important neighboring idea.

It is not the same object as the Atlas correction capacity.

Empowerment asks how much potential influence an agent can exert and later perceive through its sensorimotor channel.

Correction capacity here asks whether declared target-specific responses remain feasible after evidence arrives.

A state can have high influence capacity over many irrelevant dimensions and still lack the one correction required by a particular future target.

Conversely, a binary switch can have modest channel capacity yet preserve exactly the two corrections that matter.

The two concepts can be compared.

They should not be silently identified.

## 18. Policy optionality is not environmental branching

Suppose the environment can branch into a hundred exogenous states while the controller has only one admissible response.

The world has many possible futures.

The policy has little optionality.

Now suppose the environment has only two states, but the controller retains two distinct corrective actions.

Environmental uncertainty is smaller.

Policy optionality is larger.

Keeping these axes separate prevents "many possible futures" from being mistaken for "many controllable futures."

## 19. Delay is not automatically recoverability

Waiting can preserve options.

It can also consume them.

A system that postpones maintenance may "delay commitment" while a physical degradation process steadily removes future repair paths.

A model that simply waits may cross a deadline after which rollback is impossible.

Therefore optionality is not procrastination.

The correct question is whether the viable correction set is preserved, not whether a decision was deferred.

## 20. More optionality can be too expensive

Return to the exact witness.

Replace the preservation cost `1/2` with a parameter `c`.

Then:

`Q(P)=1-c`.

Commit-left retains:

`Q(C_L)=1/2`.

At:

`c=3/4`,

preservation has expected return:

`1/4`.

Commit-left has:

`1/2`.

Preservation still has:

- two functional options;
- correction capacity `1`.

Commit-left still has:

- one functional option;
- correction capacity `1/2`.

Yet commitment now wins on expected return.

This is not a paradox.

Maintaining flexibility has a price.

Optionality becomes a rational control objective only after that price and the value of future correction are part of the contract.

## 21. More labels are not more options

A second counterexample is even simpler.

Suppose one state offers action `x`.

Another offers `x_1` and `x_2`.

If both labels have identical transitions, costs, and future consequences, the second state has twice the raw action count but exactly the same functional option set.

This is why the quotient by consequence signature is load-bearing.

Without it, optionality can be manufactured by renaming buttons.

## 22. Regret and optionality answer different questions

Regret asks:

> how much reward was lost relative to this comparator?

Optionality asks:

> after this action, which materially distinct viable continuations remain, and which future corrections can still be executed?

The exact witness shows that Bayesian regret can tie while correction capacity differs.

But the objects can also align.

In the witness, worst-case regret prefers preservation.

In other problems, a comparator can explicitly reward recoverability, making regret sensitive to option destruction.

That does not make optionality redundant.

It means the comparator has been changed to include it.

The Regret chapter's discipline remains intact:

regret is always relative to the declared comparator and reward contract.

## 23. Optionality can be an objective, a constraint, or a diagnostic

There is no requirement to optimize `CC` directly.

Three common uses are structurally distinct.

Objective:

maximize a scalarization such as expected reward plus a declared optionality term.

Constraint:

maximize reward subject to:

`CC_{h,epsilon}>=alpha`.

Diagnostic:

optimize another objective, but report correction capacity to expose hidden commitment.

The third use is often valuable because it reveals opportunity destruction without pretending that all opportunity should be preserved.

## 24. Hard and soft correction failure should not be merged

Suppose two states both retain the desired correction.

From state A, correction costs 1.

From state B, correction costs 100.

Both have nonzero correction capacity at tolerance 100.

Only A has nonzero correction capacity at tolerance 1.

Now compare state C, where correction is impossible.

Its correction cost is infinity.

This is why the tolerance index is useful.

It distinguishes:

- cheap correction;
- expensive correction;
- no correction.

A single Boolean "reversible" flag often hides too much.

## 25. Optionality does not imply safety

A state can expose many future actions, including dangerous ones.

A high correction-capacity score relative to one target family says nothing automatically about:

- safety constraints omitted from `K`;
- tail risk;
- fairness;
- robustness to model error;
- calibration;
- institutional authorization.

These require separate contracts or connecting theorems.

The chapter therefore resists the phrase:

> more optionality is safer.

Sometimes it is.

Sometimes it is not.

## 26. Optionality does not imply knowledge

A system can preserve many corrections while having no idea which one is needed.

That is the mirror image of the main witness.

The witness gives perfect knowledge but limited correction in one branch.

The opposite case gives broad feasible control but weak information.

Adaptive capability needs both when the task demands both.

## 27. A useful evaluation vector

For a policy `pi`, one may report:

`E(pi)
=
(
expected return,
Bayesian regret,
worst-case regret,
functional option count,
correction capacity,
correction-cost profile
)`.

This is a vector, not a theorem that one coordinate should dominate.

Scalarization or Pareto preference must be declared.

This is often the cleanest way to preserve the semantics of optionality while still permitting ordinary decision analysis.

## 28. What the exact witness proves

The finite witness proves exactly:

- prior expected return can tie;
- Bayesian regret can tie;
- information gain can tie;
- functional option count can differ;
- correction capacity can differ;
- preservation cost can make the higher-optionality policy lower value.

It does not prove that correction capacity is unique.

It does not establish an optimal weighting between reward and flexibility.

It does not promote optionality into a universal safety principle.

Its role is to expose a missing state variable in some adaptive decisions.

## 29. Downstream handoff

**Governed Adaptation — ATLAS-CH-GOVADAPT-001** may, after this chapter's audit, assume:

- viable continuation sets `V_h(s)`;
- functional option quotients `O_h(s)`;
- horizon-relative recoverability;
- extended-real correction cost `k_h(s,theta)`;
- conditional correction indicator `C_{h,epsilon}(s,theta)`;
- ex-ante tolerance-indexed correction capacity `CC_{h,epsilon}(s;b)`;
- the distinction between information acquisition and ability to exploit information;
- the exact equal-value/equal-Bayes-regret separation witness;
- the counterexample showing that preserving options can be too costly.

The downstream chapter must keep the target family, horizon, constraints, consequence equivalence, and uncertainty semantics explicit.

## References used in this chapter

- Arrow and Fisher, *Environmental Preservation, Uncertainty, and Irreversibility* [@ArrowFisher1974].
- Aubin, *Viability Theory* [@Aubin1991Viability].
- Klyubin, Polani, and Nehaniv, *Keep Your Options Open: An Information-Based Driving Principle for Sensorimotor Systems* [@KlyubinPolaniNehaniv2008].

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-OPTIONALITY-001.yaml
