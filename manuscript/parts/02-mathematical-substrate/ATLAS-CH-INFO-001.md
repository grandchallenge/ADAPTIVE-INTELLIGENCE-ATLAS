# Probability, Information, and Statistical Structure
<!-- ATLAS-CH-INFO-001 -->

**Epistemic status:** Established Theory + Atlas Derivation  
**Specification:** manuscript/specifications/ATLAS-CH-INFO-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-INFO-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-INFO-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-INFO-001.yaml

## 1. Information requires a probability model

Machine learning uses the word “information” constantly.

The word can mean:

- a random variable reduces uncertainty about another;
- a code uses fewer bits;
- a hidden state preserves a task-relevant distinction;
- a message is semantically meaningful;
- a variable causally influences another;
- a dataset contains predictive signal.

These meanings are not interchangeable.

This chapter begins with the probabilistic meaning.

A probability model states how uncertainty is represented.

Information-theoretic quantities are then functions of that model.

The chapter's first discipline is:

> never ask what entropy or mutual information means before asking what probability model it is computed under.

## 2. Uncertainty budget, not semantic content

A useful allegory is an uncertainty budget.

Entropy says how uncertain a random variable is under a declared distribution.

Conditional entropy says how much uncertainty remains after another variable is known.

Mutual information says how much uncertainty is reduced, symmetrically, by knowing the other variable.

The allegory fails if “information” is taken to mean semantic significance.

A random identifier can have high entropy and almost no meaning to a user.

A one-bit alarm can carry enormous operational importance.

Information theory measures structure in a probability model.

It does not directly measure meaning.

## 3. Random variables and distributions

A random variable

\[
X:\Omega\to\mathcal X
\]

maps outcomes in a sample space to values.

In the discrete case, a mass function satisfies

\[
p(x)\ge0,
\]

and

\[
\sum_x p(x)=1.
\]

For continuous variables, probability is described relative to a measure through a density where one exists. A density is not itself a probability mass; probabilities arise by integrating it over measurable sets.

This distinction matters. Discrete Shannon entropy and differential entropy are not interchangeable: differential entropy can be negative and changes under a rescaling of coordinates. For general measures, relative entropy requires absolute continuity and a Radon–Nikodym density, rather than a ratio of arbitrary point probabilities.

Expressions such as entropy and KL divergence behave differently in discrete and continuous settings.

The Atlas will not silently move between them.

## 4. Conditional probability

For events \(A\) and \(B\) with \(P(B)>0\),

\[
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)}.
\]

For random variables, conditional distributions express how the law of one variable changes when another is known.

This is the foundation for:

- Bayesian inference;
- predictive modeling;
- filtering;
- probabilistic memory;
- uncertainty-aware decisions.

Conditional probability is not a causal operator by itself.

It is a relation inside a probability model. For an integrable discrete random variable, conditional expectation is the conditional average

\[
\mathbb E[X\mid Y=y]
=\sum_x x\,p(x\mid y),\qquad p_Y(y)>0.
\]

For integrable \(X\), the tower identity is

\[
\mathbb E[\mathbb E[X\mid Y]]=\mathbb E[X].
\]

These formulas are statements about a joint probability model; in general they do not determine an intervention.

## 5. Expectation

For discrete integrable \(X\),

\[
\mathbb E[X]
=
\sum_x x\,p(x).
\]

Expectation is linear:

\[
\mathbb E[aX+bY]
=
a\mathbb E[X]+b\mathbb E[Y].
\]

That algebraic simplicity is one reason expectations organize so much statistical learning.

Loss functions, gradients, risk, calibration, and uncertainty estimates are often expectations under one distribution or another.

The distribution must be named.

## 6. Entropy

For a finite random variable,

\[
\boxed{
H(X)
=
-\sum_x p(x)\log_2 p(x).
}
\]

Entropy is measured in bits when the logarithm has base \(2\).

A fair bit has

\[
H(X)=1.
\]

A deterministic bit has

\[
H(X)=0.
\]

These statements are exact.

They do not say that a fair bit is “more meaningful.”

They say its value is more uncertain before observation.

Standard information-theory definitions and identities are developed in Cover and Thomas [@CoverThomas2006].

## 7. Joint and conditional entropy

For jointly distributed \(X,Y\),

\[
H(X,Y)
=
-\sum_{x,y}p(x,y)\log_2p(x,y).
\]

Conditional entropy satisfies

\[
H(X\mid Y)
=
H(X,Y)-H(Y).
\]

The entropy chain rule is

\[
\boxed{
H(X,Y)
=
H(X)+H(Y\mid X).
}
\]

This is one of the first examples of information decomposing according to conditional structure.

## 8. Cross-entropy

For discrete data distribution \(P\) and model \(Q\), we use **base-2 logarithms throughout this chapter's discrete entropy, cross-entropy, KL and mutual-information formulas**. Thus all these quantities are measured in bits:

\[
H_2(P,Q)=-\mathbb E_{x\sim P}\log_2 q(x)
       =-\sum_x p(x)\log_2 q(x).
\]

The convention is \(0\log_2(0/q)=0\) for \(q>0\); if \(p(x)>0\) and \(q(x)=0\), cross-entropy is infinite. The value in nats equals the value in bits multiplied by ln 2; conversion from nats to bits requires division by \(\ln 2\); mixing logarithm bases invalidates their numerical equality.

Cross-entropy is therefore a model-relative quantity.

It depends on both the data distribution and the proposed predictive distribution.

## 9. KL divergence

The Kullback–Leibler divergence is

\[
\boxed{
D_{\rm KL,2}(P\|Q)
=
\sum_x p(x)\log_2\frac{p(x)}{q(x)}
}
\]

with the usual \(0\log_2(0/q)=0\) convention and extended value \(+\infty\) when \(P\) is not absolutely continuous with respect to \(Q\), written \(P\not\ll Q\). In the finite-valued case we require \(q(x)>0\) whenever \(p(x)>0\).

KL divergence is nonnegative.

It is not symmetric:

\[
D_{\rm KL,2}(P\|Q)
\neq
D_{\rm KL,2}(Q\|P)
\]

in general.

Therefore KL is not a metric.

It also can be infinite.

If \(P\) places positive mass where \(Q\) assigns zero mass, then

\[
D_{\rm KL,2}(P\|Q)=\infty.
\]

The direction matters.

## 10. Cross-entropy decomposition

For discrete distributions,

\[
H_2(P,Q)
=
H_2(P)
+
D_{\rm KL,2}(P\|Q).
\]

For a fixed target \(P\), minimizing cross-entropy over distributions \(Q\) is equivalent to minimizing

\[
D_{\rm KL,2}(P\|Q).
\]

This identity is simple and widely used.

Its assumptions should remain visible.

The expression depends on the declared target distribution \(P\) and model distribution \(Q\).

## 11. Mutual information

Mutual information is

\[
\boxed{
I(X;Y)
=
D_{\rm KL,2}(P_{XY}\|P_XP_Y).
}
\]

Equivalently,

\[
I(X;Y)
=
H(X)-H(X\mid Y),
\]

and symmetrically,

\[
I(X;Y)
=
H(Y)-H(Y\mid X).
\]

If \(X\) and \(Y\) are independent,

\[
P_{XY}=P_XP_Y,
\]

so

\[
I(X;Y)=0.
\]

Mutual information therefore measures statistical dependence.

It does not specify a causal direction.

## 12. Exact correlated-bit witness

![A 2 by 2 exact joint probability table with uniform marginals and mutual information about 0.1887 bits, explicitly labeled as dependence rather than causal direction.](../../figures/derivatives/ATLAS-FIG-INFO-001-v0.1.1.png)

Consider

\[
P_{XY}
=
\begin{pmatrix}
3/8&1/8\\
1/8&3/8
\end{pmatrix}.
\]

Both marginals are fair:

\[
P_X=P_Y=(1/2,1/2).
\]

The companion Wolfram witness evaluates

\[
I(X;Y)
=
\frac{\log(27/16)}{\log16}
\approx
0.1887218755408671
\]

bits.

For deterministic equality \(Y=X\) with a fair bit,

\[
I(X;Y)=1
\]

bit.

The statistic is symmetric in \(X\) and \(Y\).

The result therefore cannot by itself tell us whether \(X\) causes \(Y\), \(Y\) causes \(X\), or both share another cause.

## 13. Same entropy, different structure

Two distributions can have the same entropy while assigning probability to different events.

Entropy therefore does not uniquely identify a distribution.

Likewise, two learned representations can have similar aggregate information measures while differing dramatically in:

- geometry;
- localization;
- robustness;
- causal role;
- downstream accessibility.

Information-theoretic summaries are powerful.

They are not complete descriptions.

## 14. Concentration

Expected behavior is not enough.

We often need to know how far a random quantity can deviate from its mean.

Concentration inequalities answer questions of the form:

\[
P(|X-\mathbb E X|\ge t)
\le
\text{tail bound}.
\]

The assumptions matter.

For example, standard Hoeffding inequalities rely on bounded independent variables.

High-dimensional probability develops many concentration tools with different assumptions and regimes [@Vershynin2018].

The Atlas will carry those assumptions forward rather than quoting a tail formula detached from its conditions.

## 15. Why concentration matters for machine learning

Concentration appears in:

- generalization arguments;
- randomized embeddings;
- sketching;
- stochastic gradients;
- random-feature approximations;
- sampling-based estimators;
- high-dimensional geometry.

For example, if \(Z_1,\ldots,Z_n\) are **independent** random variables with \(a_i\le Z_i\le b_i\) almost surely, Hoeffding's inequality implies for \(t>0\)

\[
\Pr\!\left(\left|\sum_{i=1}^n (Z_i-\mathbb E Z_i)\right|\ge t\right)
\le 2\exp\!\left(-\frac{2t^2}{\sum_{i=1}^n(b_i-a_i)^2}\right).
\]

As an explicit example, for \(100\) independent Bernoulli trials, irrespective of their individual success probabilities, the chance that their sample average differs from its expectation by at least \(0.2\) is at most \(2e^{-8}<0.001\). Independence and boundedness are essential here; the inequality is not a distribution-shift guarantee.

A concentration bound is an uncertainty statement about a random object.

It is not a guarantee that a learned system behaves well under distribution shift.

That requires a different argument.

## 16. Sufficient statistics

A statistic

\[
T(X)
\]

compresses observed data.

It is sufficient for a parameter \(\theta\) in a statistical family when the conditional distribution of the full sample given the statistic does **not depend on \(\theta\)** (with suitable regular conditional distributions). Equivalently, in a dominated family, the factorization criterion characterizes sufficiency under its usual hypotheses.

For an iid Bernoulli sample \(X_1,\ldots,X_n\), the count \(T=\sum_i X_i\) is sufficient for the common success probability \(p\), since its likelihood factors as \(p^T(1-p)^{n-T}\). A statistic sufficient for that family need not be sufficient for a different dependence or heterogeneity model.

Sufficiency is therefore relative to a model.

A statistic can be sufficient for one family and inadequate for another.

This is a useful early example of a theme that later reappears in boundary compression:

> sufficient for what?

## 17. Exponential families

An exponential family has form

\[
p_\eta(x)
=
h(x)
\exp\{
\eta^\top T(x)-A(\eta)
\}.
\]

Here:

- \(\eta\) is a natural parameter;
- \(T(x)\) is a sufficient-statistic vector in the standard regular setting;
- \(A(\eta)\) is the log-partition function.

Exponential-family structure connects:

- statistics;
- convexity;
- entropy;
- duality.

Wainwright and Jordan develop this framework systematically [@WainwrightJordan2008].

## 18. Bernoulli as an exponential family

For \(x\in\{0,1\}\) and **\(0<p<1\)**,

\[
p(x)
=
p^x(1-p)^{1-x}.
\]

Define

\[
\eta
=
\log\frac{p}{1-p}.
\]

Then

\[
p(x)
=
\exp\{
x\eta-A(\eta)
\},
\]

where

\[
A(\eta)
=
\log(1+e^\eta).
\]

Thus

\[
T(x)=x
\]

is the natural sufficient statistic for one observation. For an iid sample the sufficient statistic is \(\sum_i X_i\), as above. The endpoints \(p=0\) and \(p=1\) arise only as limits of the finite natural parameter \(\eta\); they do not have finite values of \(\log(p/(1-p))\).

This small example is useful because it connects probability, sufficient statistics, and convex log-partition structure in one line.

## 19. Information geometry waits for later

Exponential families also support a geometric viewpoint.

The Hessian of the log-partition function is related to covariance and Fisher information under standard regularity conditions.

That leads toward information geometry.

This chapter does not develop that theory.

It establishes the probabilistic and statistical objects the later chapter will require.

## 20. Three overinterpretations to avoid

### Entropy equals meaning

False.

Entropy quantifies uncertainty under a probability model.

### Mutual information equals causality

False.

Mutual information is symmetric dependence information.

### KL equals distance

False.

KL is asymmetric and can be infinite.

These are not pedantic distinctions.

They determine which downstream arguments are legal.

## 21. Atlas connections

**Representation.**  
Information measures can characterize statistical dependence or compression, but representation geometry and identifiability remain separate questions.

**Attention.**  
Softmax creates normalized weights, but probabilistic-looking normalization does not automatically make every attention object a probability model with the semantics assumed here.

**Decision theory.**  
Expected utility and uncertainty require explicit distributions or uncertainty sets.

**Memory.**  
Retrieval and compression can be studied in terms of sufficient statistics and information preservation, but semantic adequacy is task-relative.

**Optimization.**  
KL and related divergences can induce optimization geometry.

## 22. Closing view

Probability gives the Atlas a language for uncertainty.

Information theory gives it a language for statistical dependence and coding structure.

Exponential families give it a language for structured statistical models.

Concentration gives it a language for deviations.

These tools are powerful precisely because their meanings are narrow.

The Atlas will use them most effectively by refusing to ask them to mean more than they do.

## References used in this chapter

- [@CoverThomas2006]
- [@WainwrightJordan2008]
- [@Vershynin2018]
