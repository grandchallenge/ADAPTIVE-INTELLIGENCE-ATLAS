# ATLAS-CH-PROGRESSSEARCH-001 — Derivation Packet

## 1. Inherited progress signal

For region r, metric m_t(r), lag w, and orientation eta_r in {+1,-1},

\[
LP_t(r)=\eta_r[m_t(r)-m_{t-w}(r)].
\]

This is an oriented finite difference on a declared metric. It is not a direct readout of an internal learning mechanism.

## 2. Search state

Define

\[
\mathfrak S_t=(\mathcal E,z_t,h_t,\widehat{LP}_t,u_t,g_t,\Phi_t,H,B_t).
\]

The experience space \(\mathcal E\) can be finite, partitioned, or continuously parameterized. The search state \(h_t\) is distinct from learner state and optimizer state.

The operator

\[
r_t\sim\mathcal S_t(\cdot\mid\mathfrak S_t)
\]

selects the next region or experience-generation condition.

## 3. Generalization-state evidence

Record declared evidence as

\[
g_t(r)=\bigl(g_t^{acq},g_t^{pers},g_t^{access},g_t^{expr}\bigr)(r).
\]

These coordinates may use different metrics or units. No scalar score exists until a policy declares one.

Thus

\[
g_t(r)\neq\text{mechanism state}.
\]

## 4. Pure exploitation can be search-incomplete

Let the experience regions be

\[
\mathcal E=\{A,B\}.
\]

At time zero, A is observed with estimated progress 1 and B is unobserved.

The declared toy sampling reward is

\[
R(A)=1,\qquad R(B)=3.
\]

Define exploit-only selection over the observed set \(\mathcal O_t\):

\[
r_t^{exploit}\in\arg\max_{r\in\mathcal O_t}\widehat{LP}_t(r).
\]

Initially \(\mathcal O_0=\{A\}\), so exploit-only selects A. If it never samples outside the observed set, then after two rounds its cumulative reward is

\[
1+1=2.
\]

Define coverage-first selection:

- if an unobserved region exists, sample one;
- otherwise select the region with largest observed progress.

Coverage-first samples B on the first round, observes 3, and selects B again on the second round. Its cumulative reward is

\[
3+3=6.
\]

Therefore the failure is exact:

\[
\text{greedy over observed regions}\not\Rightarrow\text{discovery of the best unobserved region}.
\]

This does not prove that coverage-first is generally optimal.

## 5. Immediate progress can be horizon-suboptimal

Consider state \(s_0\) and a two-step horizon.

At \(s_0\):

\[
R(s_0,G)=2,\qquad T(s_0,G)=s_G,
\]

and all second-step rewards from \(s_G\) equal zero.

Also

\[
R(s_0,I)=0,\qquad T(s_0,I)=s_I,
\]

with an available action X at \(s_I\) satisfying

\[
R(s_I,X)=5.
\]

One-step greedy chooses G because 2>0. Its two-step return is 2.

The path I,X has two-step return 5.

Hence

\[
\arg\max_a R(s_0,a)
\]

need not maximize finite-horizon return.

## 6. Credit horizon

For a selected experience at time t, define a declared H-step return

\[
G_t^{(H)}=\sum_{k=0}^{H-1}\gamma^k r_{t+k}.
\]

This object does not by itself identify causal credit. If several training updates, data regions, or interventions occur between t and the later metric change, an additional attribution rule is required.

## 7. Absolute learning progress

Absolute progress

\[
ALP_t(r)=|LP_t(r)|
\]

treats positive and negative signed change symmetrically in magnitude.

Therefore

\[
ALP_t(r)>0
\]

does not imply beneficial learning. It can also reflect deterioration, forgetting, metric noise, or another nonstationary change.

## 8. Search objective

A search functional may be written abstractly as

\[
\Phi_t\bigl(\widehat{LP}_t(r),u_t(r),g_t(r),c_t(r),B_t,H\bigr).
\]

No universal scalarization is assumed. If cost, evidence coordinates, progress, and uncertainty are combined, the ordering/scalarization rule is part of the algorithm.

## 9. Search changes the training intervention

Changing which regions are sampled can change:

- support;
- mixture weights;
- repeat exposure;
- controller overhead;
- effective optimization trajectory.

Thus endpoint differences cannot be attributed to 'search' alone without a controlled comparison.

## 10. Downstream handoff

ATLAS-CH-MINCURR-001 may inherit:

- the progress-search object;
- explicit exploration/coverage state;
- long-horizon return and credit-assignment requirements;
- generalization-state evidence as non-oracular evidence;
- both exact counterexamples.

It must independently define what minimality and reconstructability mean.

## Claim boundary

This packet proves the two finite witnesses and formalizes Atlas-local search bookkeeping. It does not establish a universally optimal exploration rule, a universal learning-progress objective, or mechanism identification from progress signals.