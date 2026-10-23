# ATLAS-CH-INFO-001 — Derivation Packet

## D1. Entropy

For a finite random variable \(X\) with mass function \(p(x)\),

\[
H(X)
=
-\sum_x p(x)\log_2 p(x).
\]

Entropy is defined relative to a probability model. It is not semantic meaning.

## D2. KL divergence

For discrete distributions \(P,Q\),

\[
D_{\mathrm{KL},2}(P\|Q)
=
\sum_x p(x)\log_2\frac{p(x)}{q(x)}
\]

when \(P\) is absolutely continuous with respect to \(Q\) on the relevant support.

The discrete logarithm is base 2, matching the chapter's bits convention and cross-entropy decomposition. The zero-mass contribution is zero; support failure gives positive infinity. KL is generally asymmetric and can be infinite.

## D3. Mutual information

\[
I(X;Y)
=
D_{\mathrm{KL},2}(P_{XY}\|P_X P_Y).
\]

For the exact witness

\[
P_{XY}
=
\begin{pmatrix}
3/8&1/8\\
1/8&3/8
\end{pmatrix},
\]

both marginals are uniform and

\[
I(X;Y)
=
\frac{\log(27/16)}{\log 16}
\approx
0.1887218755408671
\]

bits.

For \(Y=X\) with a fair Bernoulli variable,

\[
I(X;Y)=1
\]

bit.

Neither result supplies a causal arrow.

## D4. Exponential family

A regular exponential-family form is

\[
p_\eta(x)
=
h(x)\exp\{\eta^\top T(x)-A(\eta)\}.
\]

For Bernoulli \(x\in\{0,1\}\) with \(0<p<1\),

\[
p(x)
=
\exp\{x\eta-A(\eta)\}
\]

with

\[
\eta=\log\frac{p}{1-p},
\qquad
A(\eta)=\log(1+e^\eta).
\]

For one Bernoulli observation \(T(x)=x\) is sufficient. For iid Bernoulli observations the statistic \(T(X_1,\dots,X_n)=\sum_i X_i\) is sufficient for the common parameter \(p\); the endpoint distributions \(p=0,1\) are limits of finite natural parameters.

## D5. Concentration scope

A concentration inequality is meaningful only with its assumptions.

For example, Hoeffding-style concentration requires bounded independent variables in its standard form. The Atlas will not quote an exponential tail bound while hiding the independence/boundedness hypotheses. For independent \(Z_i\in[a_i,b_i]\), the two-sided Hoeffding bound is

\[
\Pr\!\left(\left|\sum_{i=1}^n(Z_i-\mathbb EZ_i)\right|\ge t\right)
\le 2\exp\!\left(-\frac{2t^2}{\sum_i(b_i-a_i)^2}\right).
\]

For 100 independent Bernoulli trials and deviation \(0.2\) of the sample mean, this gives \(2e^{-8}<0.001\).

## Claim boundary

This packet establishes standard discrete information quantities, one exact mutual-information witness, and one exponential-family example. It does not identify information with semantics or causality.
