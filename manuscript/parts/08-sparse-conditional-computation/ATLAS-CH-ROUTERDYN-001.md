# Router Dynamics and Diagnostics
<!-- ATLAS-CH-ROUTERDYN-001 -->

**Epistemic status:** audited MoE/Optimizer-Dynamics prerequisites + primary router-stability/routing sources + Atlas synthesis + exact finite witnesses  
**Specification:** manuscript/specifications/ATLAS-CH-ROUTERDYN-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-ROUTERDYN-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-ROUTERDYN-001.md

A routing system can look balanced while changing its mind about every token.

That is the central diagnostic problem.

Mixture-of-Experts systems expose several routing layers at once: probabilities, preferred routes, capacity-constrained dispatch, realized expert load, and expert behavior. Looking at only one can hide motion in the others.

## 1. Four moving objects

For N tracked tokens and E experts, let

\[
P_t
\]

be the router probability matrix at checkpoint t.

Let

\[
r_t(i)
\]

be the declared preferred top-1 expert for token i.

Let

\[
A_t
\]

be the accepted dispatch matrix after capacity, overflow, and execution policy.

Finally, let

\[
\ell_t=A_t^\top\mathbf 1
\]

be accepted expert load.

The audited MoE chapter already established that these are not interchangeable.

ROUTERDYN adds time.

## 2. Probability drift

Define average rowwise probability drift by

\[
D_P(t)
=
\frac{1}{2N}
\sum_i
\|P_t(i,:)-P_{t-1}(i,:)\|_1.
\]

The factor one-half turns rowwise L1 distance between probability vectors into total variation.

This diagnostic can move even when the preferred expert does not.

That matters because routing margins can become sharper or flatter before a top-1 assignment flips.

## 3. Preferred-route churn

For top-1 routing, define

\[
\chi_R(t)
=
\frac1N
\sum_i
\mathbf1\{r_t(i)\ne r_{t-1}(i)\}.
\]

This is token-identity sensitive.

A value of zero says every tracked token kept the same preferred expert.

A value of one says every tracked token changed preferred expert.

It says nothing by itself about whether those changes helped the task.

## 4. Accepted-dispatch churn

Capacity and overflow can change what is actually executed.

For one accepted expert per token,

\[
\chi_A(t)
=
\frac{1}{2N}
\|A_t-A_{t-1}\|_{1,\mathrm{entry}}.
\]

Preferred-route churn and accepted-dispatch churn can differ when capacity handling intervenes.

That is why a router-dynamics dashboard should not report one as a synonym for the other.

## 5. Load drift

Accepted load is much coarser:

\[
D_\ell(t)
=
\frac{1}{2N}
\|\ell_t-\ell_{t-1}\|_1.
\]

Load answers a systems question: how much accepted work moved among experts?

It does not preserve token identity.

That information loss creates the first exact counterexample.

## 6. Exact counterexample: perfect balance, total churn

Take four tracked tokens.

At one checkpoint,

\[
r_0=(1,1,2,2).
\]

At the next,

\[
r_1=(2,2,1,1).
\]

The load vector is unchanged:

\[
\ell_0=\ell_1=(2,2).
\]

So

\[
D_\ell=0.
\]

But every token changed expert:

\[
\chi_R=\chi_A=1.
\]

Thus:

\[
\boxed{
\text{stable load}
\not\Rightarrow
\text{stable routing}
}
\]

in the exact finite witness.

This is why load balancing is not a temporal-stability metric.

## 7. Transition operators on expert identity

For a fixed tracked token panel, define the empirical expert-transition matrix

\[
T_t(a,b)
=
\frac{
\#\{i:r_{t-1}(i)=a,\ r_t(i)=b\}
}{
\#\{i:r_{t-1}(i)=a\}
}.
\]

Each observed row is stochastic.

The swap witness produces

\[
T_{\rm swap}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

A stable routing panel produces

\[
T_{\rm stable}=I.
\]

The matrices describe very different temporal behavior.

Yet both have singular values

\[
(1,1).
\]

So:

\[
\boxed{
\text{same singular spectrum}
\not\Rightarrow
\text{same routing dynamics}
}
\]

for this pair.

Spectral diagnostics are useful only when the operator being diagnosed and the information discarded by the summary are explicit.

## 8. One-step transition is not automatically a Markov model

The matrix \(T_t\) is an empirical transition object.

Calling it a stationary Markov chain requires additional assumptions.

The data distribution may change.

The router parameters may change.

The experts themselves may change.

Capacity policy may change.

The token panel may not be representative.

ROUTERDYN therefore uses Markov-style algebra only as a diagnostic lens unless stationarity and sampling assumptions are separately justified.

## 9. Route churn can be zero while probabilities move

Now take two tokens and two experts:

\[
P_0=
\begin{pmatrix}
0.6&0.4\\
0.4&0.6
\end{pmatrix},
\qquad
P_1=
\begin{pmatrix}
0.9&0.1\\
0.1&0.9
\end{pmatrix}.
\]

The preferred experts do not change.

Therefore

\[
\chi_R=0.
\]

But the average probability drift is

\[
D_P=0.3.
\]

A routing system can therefore become much more confident without changing its top-1 token assignment.

The converse is also possible: a small probability change near a decision boundary can cause route churn.

## 10. Routing stability and training stability are different claims

ST-MoE studies training instabilities in large sparse models and introduces router z-loss as one stabilization technique in that setting [@ZophEtAl2022STMoE].

That is valuable evidence about sparse-model training.

But “training became more stable” is not identical to “token assignments became temporally stable.”

A loss spike, router-logit magnitude, assignment churn, load imbalance, and expert specialization are different observables.

The chapter keeps them separate.

## 11. Routing rules alter what can specialize

Expert Choice reverses a common routing perspective: instead of each token choosing a fixed number of experts, experts choose tokens subject to capacity [@ZhouEtAl2022ExpertChoice].

This reinforces a broader point.

Specialization is not produced by experts in isolation.

It depends on the routing rule that determines what experience reaches them.

A temporal specialization study must therefore record the routing policy alongside the expert profile.

## 12. Specialization needs a declared taxonomy

Suppose each tracked token has a declared category

\[
c_i\in\mathcal C.
\]

For expert e with nonzero accepted load, define

\[
S_t(e,c)
=
\frac{
\sum_i A_t(i,e)\mathbf1\{c_i=c\}
}{
\ell_t(e)
}.
\]

This gives the expert's accepted-token category profile.

A simple specialization score can compare that profile with the tracked-panel category distribution.

But the category system is part of the measurement.

If the categories are language, syntax, topic, token identity, task family, or another feature, the meaning of “specialized” changes.

Therefore:

\[
\boxed{
\text{load concentration}
\ne
\text{semantic specialization}
}
\]

and

\[
\boxed{
\text{specialization score}
\ne
\text{causal importance}.
}
\]

## 13. Temporal specialization drift

An expert can keep the same load while the composition of that load changes.

A total-variation profile drift can be written

\[
D_S(t,e)
=
\frac12
\sum_c
|S_t(e,c)-S_{t-1}(e,c)|.
\]

This lets the Atlas ask whether an expert's observed role is stable even when its utilization is stable.

Again, the answer is relative to the declared taxonomy.

## 14. Router dynamics include optimizer memory

Routing parameters are trained parameters.

If their next update depends on momentum, adaptive moments, schedules, or other optimizer state, then the dynamical state is larger than the router weights alone.

Let

\[
\xi_t
\]

collect the declared router-plus-optimizer state.

A local linearization is

\[
\delta\xi_{t+1}=J_t\delta\xi_t.
\]

Along a changing trajectory,

\[
\delta\xi_{t+h}
=
J_{t+h-1}\cdots J_t\delta\xi_t.
\]

This is inherited directly from the audited Optimizer-State Dynamics viewpoint.

## 15. Commutators detect order sensitivity

Successive local maps need not commute.

Define

\[
\mathcal C_t
=
J_tJ_{t-1}-J_{t-1}J_t.
\]

If

\[
\mathcal C_t\ne0,
\]

the order of the two local linear maps matters.

This is a diagnostic fact.

It is not a causal explanation of why the maps changed.

## 16. Exact commutator witness

Take

\[
J_0=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\qquad
J_1=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}.
\]

Each has eigenvalues

\[
(1,1).
\]

But

\[
J_1J_0
\ne
J_0J_1.
\]

The commutator is

\[
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\]

with Frobenius norm

\[
\sqrt2.
\]

Identical one-step eigenvalue multisets therefore do not determine the two-step order-sensitive behavior.

## 17. Spectral router diagnostics are typed

Several spectra may be interesting:

- the spectrum of an empirical expert-transition matrix;
- singular values of that transition matrix;
- eigenvalues of a local augmented router-state Jacobian;
- singular values of that Jacobian;
- finite-horizon gains of Jacobian products.

These are spectra of different operators.

They cannot be compared as though “the router spectrum” were one universal object.

## 18. Churn is not automatically bad

High churn can indicate instability.

It can also indicate:

- adaptation to a changing data distribution;
- a router still discovering useful specialization;
- exchange among functionally similar experts;
- movement caused by changing capacity semantics;
- benign margin crossing near equivalent experts.

Low churn can be bad too.

A router can be stably wrong.

ROUTERDYN therefore reports churn before interpreting churn.

## 19. Capacity can hide preference dynamics

The MoE audit established an important warning: accepted load can look balanced even when preferred routing is concentrated because capacity handling modifies execution.

The temporal version is stronger.

Accepted-load stability can arise from a capacity mechanism even while preferred token assignments or router probabilities move substantially.

A longitudinal study should therefore preserve both pre-capacity and post-capacity observables.

## 20. A practical diagnostic record

A router-dynamics measurement should declare at least:

- checkpoint/time index;
- tracked token panel or sampling distribution;
- router logits/probabilities;
- preferred-route rule and tie-breaking;
- capacity and overflow policy;
- accepted dispatch;
- load vector;
- route-churn metric;
- probability-drift metric;
- any token taxonomy used for specialization;
- any transition operator;
- any augmented-state Jacobian approximation;
- spectral statistic and operator identity.

Without these fields, two “router stability” claims may be measuring different phenomena.

## 21. Handoff to Routing as Online Decision Making

ATLAS-CH-REGRETROUTE-001 may now assume:

- probability, preferred-route, accepted-dispatch, and load temporal separation;
- exact route-churn and probability-drift definitions;
- empirical expert-transition operators;
- taxonomy-relative specialization profiles;
- local augmented-state commutator diagnostics;
- the finite examples showing that loads and singular spectra can hide token-level motion.

REGRETROUTE must add the online-decision layer.

It must define:

- the routing action;
- comparison policy/class;
- reward or loss timing;
- regret;
- optionality;
- correction capacity;
- nonstationarity assumptions.

Temporal diagnostics are not regret theory by themselves.

## 22. Durable lesson

A router does not have one dynamics.

It has several coupled temporal surfaces:

\[
\text{probability}
\to
\text{preference}
\to
\text{dispatch}
\to
\text{load},
\]

plus expert behavior and optimizer memory.

The chapter's main discipline is to diagnose each surface before interpreting the system.

## References used in this chapter

- [@ZophEtAl2022STMoE]
- [@ZhouEtAl2022ExpertChoice]

Exact source authority, prerequisite identities, and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-ROUTERDYN-001.yaml
