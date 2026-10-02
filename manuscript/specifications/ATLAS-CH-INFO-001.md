# Chapter Specification — ATLAS-CH-INFO-001

## Identity

**Title:** Probability, Information, and Statistical Structure  
**Part:** Mathematical Substrate  
**Status:** specification-ready.

## Chapter contract

Supply the probability/information substrate required by representation learning, uncertainty, decision, and statistical-learning chapters.

## Dependency contract

Hard prerequisite:

- `ATLAS-CH-OBJECTS-001`.

Do not assume representation-learning terminology.

## Reader outcome

A reader should be able to:

- work with random variables, conditional probability, expectation, and conditional expectation;
- state concentration results with assumptions;
- define entropy, cross-entropy, KL divergence, and mutual information;
- explain why KL is not a metric and may be infinite;
- explain why mutual information is dependence, not causality;
- identify sufficient statistics relative to a statistical family;
- recognize exponential-family form.

## Formal spine

Use discrete and density-based cases carefully.

Core objects:

[
H(X),
qquad
D_{mathrm{KL}}(P|Q),
qquad
I(X;Y),
]

and exponential family

[
p_eta(x)
=
h(x)exp{eta^	op T(x)-A(eta)}.
]

Include an explicit support/absolute-continuity warning for KL.

## Principal pedagogical device

### Allegory: uncertainty budget, not semantic content

Entropy measures uncertainty under a probability model. It does not directly measure how meaningful an object is to an agent.

Limit:

The analogy breaks whenever “information” is used in the everyday semantic sense.

## Exact derivations

At minimum:

- entropy chain rule for a finite joint distribution;
- (I(X;Y)=D_{m KL}(P_{XY}|P_XP_Y));
- Bernoulli as an exponential family with sufficient statistic (T(x)=x);
- one concentration calculation with explicit assumptions.

## Computational witness

A small exact joint distribution showing:

- independence gives zero mutual information;
- deterministic dependence gives positive mutual information;
- symmetric dependence does not imply a causal arrow;
- support mismatch can make KL infinite.

## Counterexamples and failure boundaries

- KL asymmetry;
- same entropy with different distributions;
- high mutual information without identified causal direction;
- a statistic sufficient for one family but not automatically another.

## Downstream obligations

Primary consumer:

- `ATLAS-CH-REP-001`.

Also supplies later statistical-learning, uncertainty, decision, and information-geometry chapters.

## Sources

- [@CoverThomas2006]
- [@WainwrightJordan2008]
- [@Vershynin2018]

Source lock: `sources/source-locks/ATLAS-CH-INFO-001.yaml`.

## Acceptance

The chapter must keep probability-model assumptions visible and refuse semantic/causal overinterpretation of information quantities.
