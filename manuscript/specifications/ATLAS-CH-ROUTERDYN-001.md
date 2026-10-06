# Chapter Specification — ATLAS-CH-ROUTERDYN-001

## Identity

**Title:** Router Dynamics and Diagnostics  
**Part:** Sparse and Conditional Computation  
**Status:** specification-ready.  
**Epistemic class:** audited MoE and Optimizer-State Dynamics prerequisites + primary router-stability/routing sources + Atlas synthesis.

## Contract

Study churn, specialization, commutators, temporal instability, and spectral router diagnostics.

The chapter must preserve the MoE distinction among:

- router logits and probabilities;
- preferred top-k routes;
- capacity-constrained accepted dispatch;
- realized expert load;
- balancing proxies;
- specialization evidence.

It must also preserve the OPTDYN distinction between instantaneous quantities and augmented-state dynamics.

## Hard prerequisites

- ATLAS-CH-MOE-001
- ATLAS-CH-OPTDYN-001

Exact prerequisite identities and external source authority are locked in:

\`sources/source-locks/ATLAS-CH-ROUTERDYN-001.yaml\`.

## Temporal router object

For N tracked tokens and E experts at checkpoint t, define:

- router probability matrix \(P_t\in[0,1]^{N\times E}\), each row summing to one;
- preferred top-1 route \(r_t(i)\in\{1,\ldots,E\}\);
- accepted dispatch matrix \(A_t\in\{0,1\}^{N\times E}\) for a declared top-1 execution policy;
- accepted load vector
  \[
  \ell_t=A_t^\top \mathbf 1.
  \]

For top-k or variable-k systems, the same diagnostics require an explicit normalization by the declared number of accepted assignments.

## Four temporal diagnostics

Probability drift:

\[
D_P(t)=
\frac{1}{2N}
\sum_{i=1}^{N}
\|P_t(i,:)-P_{t-1}(i,:)\|_1.
\]

Preferred-route churn:

\[
\chi_R(t)=
\frac{1}{N}
\sum_{i=1}^{N}
\mathbf 1\{r_t(i)\neq r_{t-1}(i)\}.
\]

Accepted-dispatch churn for top-1 routing:

\[
\chi_A(t)=
\frac{1}{2N}
\|A_t-A_{t-1}\|_{1,\mathrm{entry}}.
\]

Load drift:

\[
D_\ell(t)=
\frac{1}{2N}
\|\ell_t-\ell_{t-1}\|_1.
\]

These are distinct observables.

## Empirical expert-transition operator

For a tracked token panel, define

\[
T_t(a,b)
=
\frac{
\#\{i:r_{t-1}(i)=a,\ r_t(i)=b\}
}{
\#\{i:r_{t-1}(i)=a\}
}
\]

when the denominator is nonzero.

Each observed row is stochastic.

This is an empirical one-step transition operator on expert identities for the tracked panel. It is not automatically a stationary Markov chain model of routing.

## Exact load-versus-churn witness

Use four tokens and two experts.

At checkpoint 0:

\[
r_0=(1,1,2,2).
\]

At checkpoint 1:

\[
r_1=(2,2,1,1).
\]

Accepted loads are

\[
\ell_0=\ell_1=(2,2),
\]

so

\[
D_\ell(1)=0.
\]

But every tracked token changes expert:

\[
\chi_R(1)=\chi_A(1)=1.
\]

The empirical transition operator is

\[
T_{\mathrm{swap}}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

For the stable counterfactual \(r_1=r_0\),

\[
T_{\mathrm{stable}}=I.
\]

Both transition matrices have singular values \((1,1)\), while one has zero churn and the other total churn.

Therefore:

\[
\text{stable loads}\not\Rightarrow\text{stable routing},
\]

and

\[
\text{same singular values}\not\Rightarrow\text{same routing dynamics}.
\]

## Exact probability-drift witness

For two tokens and two experts, let

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

Preferred routes remain unchanged, so

\[
\chi_R=0.
\]

But

\[
D_P=0.3.
\]

Thus zero route churn does not imply static router probabilities.

## Specialization profile

If each tracked token has a declared category \(c_i\in\mathcal C\), define an accepted-dispatch profile for expert e:

\[
S_t(e,c)
=
\frac{
\sum_i A_t(i,e)\mathbf 1\{c_i=c\}
}{
\sum_i A_t(i,e)
}
\]

when expert e has nonzero accepted load.

A specialization diagnostic may compare \(S_t(e,\cdot)\) against the tracked-panel category distribution by total variation, Jensen-Shannon divergence, or another declared measure.

The category taxonomy is part of the measurement contract.

Load concentration alone is not semantic specialization.

## Local augmented-state commutator

Let \(J_{t-1}\) and \(J_t\) be two declared local Jacobians of an augmented router-plus-optimizer state map.

Define the commutator

\[
\mathcal C_t
=
J_tJ_{t-1}-J_{t-1}J_t.
\]

A nonzero commutator means the two local linear maps are order-sensitive.

It does not identify the cause of the order sensitivity.

## Exact commutator witness

Use

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

Then

\[
J_1J_0=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix},
\qquad
J_0J_1=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix},
\]

so

\[
\mathcal C=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\qquad
\|\mathcal C\|_F=\sqrt{2}.
\]

The two one-step maps each have eigenvalues \((1,1)\), yet their order matters.

## Spectral diagnostics boundary

Permitted diagnostic objects include:

- eigenvalues of \(T_t\), when interpretation is stated;
- singular values of \(T_t\);
- spectra/singular values of local router-state Jacobians;
- finite-horizon products \(J_{t+h-1}\cdots J_t\);
- commutator norms.

No single spectrum is a universal router-health score.

The meaning of a spectral statistic depends on which operator is being analyzed.

## Failure boundaries

- stable accepted loads != stable token routing;
- zero preferred-route churn != zero probability drift;
- balanced loads != semantic specialization;
- specialization score != causal importance;
- one empirical transition matrix != stationary Markov dynamics;
- spectral radius != complete transient behavior;
- singular spectrum != token-identity stability;
- nonzero commutator != identified mechanism;
- local Jacobian != global training trajectory;
- observed churn != necessarily harmful churn;
- low churn != necessarily useful specialization;
- capacity handling can mask preferred-route concentration.

## Downstream handoff

Direct consumer:

- ATLAS-CH-REGRETROUTE-001.

REGRETROUTE may inherit:

- probability/preferred-route/accepted-dispatch/load temporal separation;
- route-churn and probability-drift definitions;
- empirical expert-transition operators;
- declared specialization profiles;
- local commutator and spectral-diagnostic boundaries;
- the exact load-versus-churn and probability-drift witnesses.

It must independently define routing as an online decision problem, regret, optionality, correction capacity, and comparison classes.

## Sources

- [@ZophEtAl2022STMoE]
- [@ZhouEtAl2022ExpertChoice]

Exact source authority and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-ROUTERDYN-001.yaml\`.
