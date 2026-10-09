# ATLAS-CH-ROUTERDYN-001 — Derivation Packet

## 1. Scope

This packet studies temporal routing observables without collapsing them.

It inherits:

- router probabilities, preferred routes, accepted dispatch, load, capacity, and overflow semantics from ATLAS-CH-MOE-001;
- augmented-state, local-Jacobian, transient-growth, and time-varying-product boundaries from ATLAS-CH-OPTDYN-001.

Source boundary:

\`sources/source-locks/ATLAS-CH-ROUTERDYN-001.yaml\`.

## 2. Probability, route, dispatch, and load

Let

\[
P_t\in[0,1]^{N\times E},
\qquad
\sum_{e=1}^{E}P_t(i,e)=1.
\]

For declared top-1 preferred routing,

\[
r_t(i)\in\arg\max_e P_t(i,e).
\]

Tie-breaking is part of the routing contract.

Accepted dispatch is

\[
A_t(i,e)\in\{0,1\},
\]

after capacity, overflow, and other execution rules.

Accepted load is

\[
\ell_t(e)=\sum_i A_t(i,e).
\]

Thus the map

\[
P_t\to r_t\to A_t\to \ell_t
\]

contains several noninvertible stages.

## 3. Probability drift

Define

\[
D_P(t)=
\frac{1}{2N}
\sum_i
\|P_t(i,:)-P_{t-1}(i,:)\|_1.
\]

Because each row is a probability vector, the rowwise total variation lies in \([0,1]\), so

\[
0\le D_P(t)\le1.
\]

Zero preferred-route churn can coexist with positive \(D_P\).

For

\[
P_0=
\begin{pmatrix}
0.6&0.4\\
0.4&0.6
\end{pmatrix},
\quad
P_1=
\begin{pmatrix}
0.9&0.1\\
0.1&0.9
\end{pmatrix},
\]

the preferred routes are unchanged.

Each row changes by L1 distance \(0.6\), so average total variation is

\[
D_P=\frac{1}{2}\cdot0.6=0.3.
\]

## 4. Route churn

For tracked top-1 preferred routes,

\[
\chi_R(t)
=
\frac{1}{N}
\sum_i
\mathbf 1\{r_t(i)\ne r_{t-1}(i)\}.
\]

For top-1 accepted dispatch,

\[
\chi_A(t)
=
\frac{1}{2N}
\|A_t-A_{t-1}\|_{1,\mathrm{entry}}.
\]

If each token has exactly one accepted expert, then every changed expert contributes two differing binary entries, so \(\chi_A\) equals the fraction of tokens whose accepted expert changes.

## 5. Load drift

Define

\[
D_\ell(t)
=
\frac{1}{2N}
\|\ell_t-\ell_{t-1}\|_1.
\]

Load drift is blind to token identity.

Consider

\[
r_0=(1,1,2,2),
\qquad
r_1=(2,2,1,1).
\]

Both checkpoints have

\[
\ell=(2,2),
\]

so

\[
D_\ell=0.
\]

Yet every token changes route, hence

\[
\chi_R=\chi_A=1.
\]

This proves:

\[
D_\ell=0
\not\Rightarrow
\chi_R=0.
\]

## 6. Empirical expert-transition matrix

For each expert a with at least one tracked token at time \(t-1\), define

\[
T_t(a,b)
=
\frac{
\#\{i:r_{t-1}(i)=a,\ r_t(i)=b\}
}{
\#\{i:r_{t-1}(i)=a\}
}.
\]

The quotient is defined only for prior expert classes with positive tracked occupancy; such observed rows sum to one. Empty prior classes have undefined empirical transition rows and must be marked unobserved, not silently imputed as stochastic rows. The total-swap witness has positive occupancy for both experts.

For the total-swap witness,

\[
T_{\mathrm{swap}}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

For the stable counterfactual,

\[
T_{\mathrm{stable}}
=
I.
\]

Both have singular values

\[
(1,1).
\]

But their eigenvalues are respectively

\[
(1,-1)
\]

and

\[
(1,1).
\]

Therefore equal singular spectra do not imply equal token-level temporal behavior.

A one-step empirical \(T_t\) is not automatically a stationary Markov transition law.

## 7. Churn from transition diagonals

Let

\[
w_a
=
\frac{
\#\{i:r_{t-1}(i)=a\}
}{N}.
\]

Then

\[
\chi_R(t)
=
1-\sum_a w_a T_t(a,a).
\]

This identity holds for the tracked top-1 panel.

It makes explicit that churn depends on token-retention probability along the diagonal, weighted by previous expert occupancy.

## 8. Specialization profile

Let each tracked token carry a declared category

\[
c_i\in\mathcal C.
\]

For expert e with nonzero accepted load, define

\[
S_t(e,c)
=
\frac{
\sum_i A_t(i,e)\mathbf 1\{c_i=c\}
}{
\ell_t(e)
}.
\]

Let the tracked-panel baseline category distribution be

\[
q_t(c)
=
\frac{1}{N}
\sum_i
\mathbf 1\{c_i=c\}.
\]

One bounded specialization score is total variation:

\[
\sigma_t(e)
=
\frac12
\sum_c
|S_t(e,c)-q_t(c)|.
\]

Then

\[
0\le\sigma_t(e)\le1.
\]

The score depends on the declared category taxonomy.

A different taxonomy can change the measured specialization.

This is not a universal semantic specialization measure.

## 9. Temporal specialization drift

For experts with nonzero loads at both checkpoints, define

\[
D_S(t,e)
=
\frac12
\sum_c
|S_t(e,c)-S_{t-1}(e,c)|.
\]

An expert can keep the same load while its category profile changes substantially.

Hence stable load is also insufficient to establish stable specialization.

## 10. Local augmented-state dynamics

Let

\[
\xi_t
\]

collect declared router parameters and optimizer memory needed for the next update.

For differentiable update \(\xi_{t+1}=H_t(\xi_t)\) with \(J_t=DH_t(\xi_t)\) along its declared reference trajectory, the tangent first variation obeys

\[
\delta\xi_{t+1}
=
J_t\delta\xi_t.
\]

This equality defines the **linearized/tangent** recurrence; a finite displacement \(v\) between nonlinear executions obeys \(H_t(\xi_t+v)-H_t(\xi_t)=J_tv+o(\|v\|)\), not the exact tangent equality.

For a time-varying trajectory,

\[
\delta\xi_{t+h}
=
J_{t+h-1}\cdots J_t\delta\xi_t.
\]

The matrix product is an exact propagation law for the tangent recurrence, not for finite differences between nonlinear runs. No one \(J_t\) is assumed to globally describe training.

## 11. Commutator diagnostic

For successive local maps, define

\[
\mathcal C_t
=
J_tJ_{t-1}-J_{t-1}J_t.
\]

If

\[
\mathcal C_t\ne0,
\]

the local linear maps do not commute.

This diagnoses order sensitivity of the two local maps.

It does not identify why the maps differ or whether the observed order sensitivity is harmful.

## 12. Exact commutator witness

Let

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
\]

while

\[
J_0J_1=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
\]

Therefore

\[
\mathcal C
=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

Its Frobenius norm is

\[
\|\mathcal C\|_F=\sqrt2.
\]

Both \(J_0\) and \(J_1\) have eigenvalues \((1,1)\).

One-step eigenvalues therefore do not encode the order sensitivity exhibited by this pair.

## 13. Spectral diagnostics

Potential diagnostic objects include:

- eigenvalues of empirical \(T_t\);
- singular values of \(T_t\);
- eigenvalues/singular values of local \(J_t\);
- finite-horizon singular values of products \(J_{t+h-1}\cdots J_t\);
- commutator norms.

The operator identity must always accompany the spectral statistic.

A singular value of \(T_t\) and a singular value of an augmented-state Jacobian are not interchangeable quantities.

## 14. Churn is not automatically failure

High churn can arise because:

- the router is unstable;
- the data distribution changed;
- specialization is still developing;
- experts are functionally interchangeable;
- capacity/overflow rules changed accepted dispatch;
- optimizer-state motion changed routing margins.

Low churn can coexist with poor routing if assignments are consistently bad.

Therefore a churn statistic requires a task or performance context before being promoted to a quality claim.

## 15. Downstream handoff

ATLAS-CH-REGRETROUTE-001 may inherit:

- probability, preferred-route, accepted-dispatch, and load temporal separation;
- \(D_P,\chi_R,\chi_A,D_\ell\);
- empirical expert-transition matrices;
- declared-taxonomy specialization profiles;
- augmented-state commutator diagnostics;
- exact counterexamples showing load and singular-spectrum blindness.

It must independently define online-decision comparison classes, regret, optionality, correction capacity, and action/reward timing.

## Claim boundary

This packet proves only the displayed finite identities/counterexamples and defines Atlas-local diagnostics.

It does not establish a universal scalar router-health metric, causal harm from churn, or globally valid linear router dynamics.
