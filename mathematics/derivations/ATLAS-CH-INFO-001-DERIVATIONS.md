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
D_{\mathrm{KL}}(P\|Q)
=
\sum_x p(x)\log\frac{p(x)}{q(x)}
\]

when \(P\) is absolutely continuous with respect to \(Q\) on the relevant support.

KL is generally asymmetric and can be infinite.

## D3. Mutual information

\[
I(X;Y)
=
D_{\mathrm{KL}}(P_{XY}\|P_X P_Y).
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

For Bernoulli \(x\in\{0,1\}\),

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

The statistic \(T(x)=x\) is sufficient for the Bernoulli family in the standard iid setting.

## D5. Concentration scope

A concentration inequality is meaningful only with its assumptions.

For example, Hoeffding-style concentration requires bounded independent variables in its standard form. The Atlas will not quote an exponential tail bound while hiding the independence/boundedness hypotheses.

## Claim boundary

This packet establishes standard discrete information quantities, one exact mutual-information witness, and one exponential-family example. It does not identify information with semantics or causality.
