# Reinforcement Learning and Control
<!-- ATLAS-CH-RLBASE-001 -->

**Epistemic status:** established reinforcement-learning/control foundations plus Atlas synthesis and exact finite derivation.  
**Specification:** manuscript/specifications/ATLAS-CH-RLBASE-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-RLBASE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-RLBASE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-RLBASE-001.yaml

A dynamical system tells us how state changes.

A control problem adds a question:

which change should we choose?

Reinforcement learning enters when the consequences of those choices are uncertain, delayed, only partly modeled, or learned from interaction.

The central object is therefore not "reward" by itself.

It is a coupled system containing state, action, dynamics, reward, policy, and future consequences.

The discipline of reinforcement learning begins by keeping those objects separate.

## 1. A controlled stochastic dynamical system

For this chapter, write a discounted Markov decision process as

M = (S, A, P, r, gamma, rho_0).

Here S is the state space.

A(s) is the set of admissible actions at state s.

P(s'|s,a) is the transition kernel.

r(s,a,s') is the one-step reward associated with the transition.

gamma in [0,1) is the discount factor.

rho_0 is the initial-state distribution.

A policy is another object:

pi(a|s).

The policy says how actions are selected.

The transition kernel says what the environment does after an action.

These should not be fused.

A poor policy can act in a perfectly specified environment.

A good policy can fail in a misspecified environment.

And a learned policy may change while the environment dynamics remain fixed.

## 2. The Markov boundary

The word Markov does real work.

The MDP state is assumed to contain enough information that, conditional on the current state and action, the next-state distribution does not depend on the earlier history.

Informally:

the present state is sufficient for predicting the controlled future.

This is a modeling claim.

It can fail.

If two histories are mapped to the same state representation but require different predictions or decisions, the chosen state is not Markov for the purpose at hand.

That failure cannot be repaired merely by applying a more sophisticated Bellman update.

Sometimes the right repair is a richer state.

Sometimes it is memory.

Sometimes the problem is genuinely partially observable.

## 3. Reward is not value

Reward is local.

Value is prospective.

Assume throughout the finite-MDP discussion that one-step rewards are finite; because S and A are finite, the reward table is then bounded.

Let

G_t
=
sum_{k=0}^\infty gamma^k R_{t+k+1}

be the discounted return. With gamma<1 and bounded one-step reward, this series is absolutely bounded.

For a fixed policy pi, define the state value

V^pi(s)
=
E_pi[G_t | S_t=s].

Define the action value

Q^pi(s,a)
=
E_pi[G_t | S_t=s,A_t=a].

These quantities summarize expected future reward under declared conditions.

They are not the same thing as uncertainty.

A value estimate of 10 does not tell us how uncertain that estimate is.

Nor does reward automatically mean "good" in a broader human sense.

Reward is part of the formal problem specification.

If the reward function encodes the wrong objective, an optimizer can solve the mathematical problem and still produce an outcome the designer did not want.

## 4. Bellman's recursion

Sequential decision problems become tractable when the future can be folded back into the present.

Condition on the first transition.

Under policy pi,

V^pi(s)
=
sum_a pi(a|s)
sum_{s'} P(s'|s,a)
[
r(s,a,s') + gamma V^pi(s')
].

This is the Bellman expectation equation.

It says that value equals expected immediate reward plus discounted expected continuation value.

The equation is exact for the declared MDP and policy.

The approximation begins later, when we estimate the quantities with samples, restricted representations, learned models, or finite computation.

That distinction matters.

An approximate neural critic does not make the Bellman identity approximate.

It makes our representation or solution of the identity approximate.

## 5. A two-state control problem

Consider the exact witness used by this chapter.

There are two states.

At s1, the only action gives reward 2 and returns to s1.

At s0, action a gives reward 0 and moves to s1.

Action b gives reward 2 and returns to s0.

Let

gamma = 1/2.

Start with a policy that chooses a at s0.

Then

V^pi(s1)
=
2 + (1/2)V^pi(s1),

so

V^pi(s1)=4.

At s0,

V^pi(s0)
=
0 + (1/2)4
=
2.

Now ask what would happen if, only at s0, we took action b once and then followed the old policy.

Its action value is

Q^pi(s0,b)
=
2 + (1/2)V^pi(s0)
=
3.

Three is greater than two.

So the old policy contains a locally improvable decision.

Switch s0 to action b.

The environment has not changed.

The reward function has not changed.

The transition law has not changed.

Only the policy has changed.

Under the new policy,

V(s0)
=
2 + (1/2)V(s0)
=
4.

The witness therefore gives the cleanest possible policy-improvement story:

same world, different controller, larger value.

## 6. Policy evaluation and policy improvement

This pattern generalizes.

Policy evaluation asks:

What is V^pi for the current policy?

Policy improvement asks:

Can we choose actions greedily with respect to Q^pi and obtain a policy no worse than pi?

In the exact finite discounted setting, the policy-improvement theorem answers yes.

Alternating exact evaluation and greedy improvement gives policy iteration.

Applying the optimal Bellman operator directly gives value iteration.

The important point is structural.

Evaluation and improvement are different operations.

One estimates the consequences of a controller.

The other changes the controller.

Blurring them makes it harder to identify where an error entered.

## 7. Optimality is relative

Define the Bellman optimality operator

(TV)(s)
=
max_a
sum_{s'} P(s'|s,a)
[
r(s,a,s') + gamma V(s')
].

The optimal value V* satisfies

V* = T V*.

An optimal policy chooses maximizing actions.

But the star has a scope.

Optimal with respect to which state representation?

Which admissible actions?

Which transition model?

Which reward?

Which discount?

Which horizon?

Which observation model?

An optimal policy for the wrong MDP is still optimal for the wrong MDP.

This is why later chapters will add uncertainty, optionality, correction capacity, and information value rather than treating a single scalar Bellman optimum as the entire decision problem.

## 8. When the model is known

If P and r are known, we can reason with the model directly.

Dynamic programming applies Bellman operators using expected transitions.

Policy evaluation repeatedly applies the policy Bellman operator.

Value iteration repeatedly applies the optimal Bellman operator.

Policy iteration alternates evaluation and improvement.

This is planning in a known controlled stochastic system.

No interaction sample is needed to define the recursion.

The computational burden may still be large.

But the uncertainty about transition law is conceptually separate.

## 9. Learning from sampled transitions

Reinforcement learning often begins when the model is not used directly.

Instead we observe transitions:

(S_t,A_t,R_{t+1},S_{t+1}).

A temporal-difference update for a state-value estimate has the form

V(S_t)
<-
V(S_t)
+
alpha
[
R_{t+1}
+
gamma V(S_{t+1})
-
V(S_t)
].

The bracketed term compares the old estimate with a one-step bootstrapped target.

This is where dynamics, information, and stochastic approximation meet.

The Bellman equation supplies the fixed-point structure.

The sampled transition supplies local evidence.

The learning rule decides how quickly to move.

These are three distinct objects.

## 10. Q-learning and off-policy control

Q-learning replaces the next-state policy average with a maximum:

Q(S_t,A_t)
<-
Q(S_t,A_t)
+
alpha_t
[
R_{t+1}
+
gamma max_a Q(S_{t+1},a)
-
Q(S_t,A_t)
].

This lets the behavior that generated data differ from the greedy policy defined by the current Q values.

That separation is powerful.

It also creates a distribution question.

Which state-action pairs are actually sampled?

The classical Watkins-Dayan convergence result retains strong conditions.

It does not say that arbitrary nonlinear approximation, replay, bootstrapping, nonstationarity, and off-policy data will converge merely because the update still resembles Q-learning.

The equation can survive while the theorem does not.

## 11. Policy gradients

Bellman-style control is not the only route.

Suppose a stochastic policy pi_theta is differentiable in parameters theta.

Define an expected-return objective J(theta).

Policy-gradient methods estimate

grad_theta J(theta)

and update the policy parameters directly.

For a sampled trajectory, REINFORCE uses the score-function term grad_theta log pi_theta(A_t|S_t) multiplied by an appropriate sampled return. Under the stated sampling assumptions, its expectation recovers the policy-objective gradient.

Williams's REINFORCE family is a foundational example.

This viewpoint is useful because the object being optimized is the policy distribution itself.

Modern actor-critic methods combine policy-gradient and value-estimation roles.

Again, the distinction matters.

The actor changes the policy.

The critic estimates a value-related quantity.

Neither label guarantees that the learned approximation is correct.

## 12. Model-based reinforcement learning

A model can itself be learned.

Then the system may use real experience to improve an estimated transition/reward model and use that model to generate planning updates.

Dyna is a representative architecture for this integration.

The same experience can support at least three activities:

direct value or policy learning;

model learning;

planning through the learned model.

This can improve data efficiency because one real transition can influence many simulated updates.

It also creates model bias.

Planning is only as faithful as the learned model in the states and actions where planning relies on it.

A planner can be internally exact and externally wrong because the model is wrong.

## 13. Partial observability

The MDP assumes the controller has access to the state used by the transition model.

Many real systems do not.

In a partially observable Markov decision process, hidden state S_t generates observations rather than being directly exposed.

The controller acts on history or on an information state derived from history.

A standard choice is the belief state

b_t(s)
=
P(S_t=s | history_t).

The belief is a probability distribution over hidden states.

Under the standard POMDP formulation, with the transition/observation model fixed and the posterior updated from the complete available history, the exact belief state can recover a Markov control problem in information space.

That is an elegant transformation.

It is not free.

Exact beliefs may be expensive.

The observation model may be wrong.

Approximate memory may discard information.

And two histories that induce the same approximate representation may still require different decisions.

## 14. What value leaves out

Value is useful precisely because it compresses a future distribution into an expectation.

Compression loses distinctions.

Two actions can have the same expected return and very different downside tails.

Two policies can have similar value and different information gain.

One policy can preserve many future corrective actions while another reaches the same expected return through an irreversible commitment.

A value function does not automatically record these differences.

That is not a defect in the definition.

It is a boundary.

The later decision chapters exist because the Atlas does not want one scalar expectation to silently absorb every notion of good decision making.

## 15. Model-free is not assumption-free

The phrase model-free can sound stronger than it is.

A model-free algorithm may avoid explicitly representing P.

It still relies on assumptions about the data-generating process, reward signal, state representation, stationarity, coverage, function class, optimizer, or learning-rate schedule.

The environment model can be absent from the learned representation while remaining present in the mathematics of why an estimator should work.

This is another recurring Atlas lesson:

not representing an object explicitly does not make the object irrelevant.

## 16. Control and uncertainty are different layers

A value estimate can be wrong.

A transition model can be wrong.

A reward model can be wrong.

An observation model can be wrong.

Future value estimates can be wrong.

These uncertainties interact.

RLBASE-001 does not solve that joint propagation problem.

It establishes the controlled stochastic substrate on which the later uncertainty chapter can operate.

This is why ATLAS-CH-JOINTUNC-001 depends on both this chapter and the Information substrate.

The goal there will not be to add several independent error bars mechanically.

It will be to reason about uncertainty that propagates through one coupled decision system.

## 17. What exploration adds

The Bellman optimality equation tells us what would be optimal if the relevant model or values were known.

Learning has another problem.

Which actions should be tried in order to learn what is not yet known?

An action can have two kinds of consequence:

it can produce reward;

it can produce information.

Those are not the same object.

A low-reward action now may improve future decisions by revealing structure.

A high-reward familiar action may teach us almost nothing.

ATLAS-CH-EXPLORE-001 begins from that gap.

It may assume everything established here:

states, actions, transitions, rewards, policies, returns, values, Bellman operators, and model-based/model-free distinctions.

Its job is to add the value of information and the exploration-exploitation problem.

## 18. The boundary to remember

Reinforcement learning is often summarized as learning to maximize reward.

That slogan is too compressed for the Atlas.

A more useful statement is:

reinforcement learning studies how a controller can improve sequential decisions from interaction when consequences are distributed through time and the relevant dynamics or values are not simply handed to it.

The objects remain distinct.

Dynamics describe what follows an action.

Reward scores a local transition according to the model.

Return accumulates those scores through time.

Value takes an expectation under a policy.

Bellman recursion connects present and future.

Learning estimates or improves the relevant objects from data.

Planning uses a model to reason ahead.

Partial observability moves control into information state.

And optimality remains relative to the problem we chose to write down.

Once those boundaries are explicit, later chapters can ask harder questions without overloading the word value.

## References used in this chapter

The exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-RLBASE-001.yaml

The external basis includes Bellman's Markovian decision-process work, Sutton and Barto's standard reinforcement-learning treatment, Watkins and Dayan on Q-learning, Williams on REINFORCE, Sutton on Dyna, and Kaelbling, Littman, and Cassandra on POMDPs.
