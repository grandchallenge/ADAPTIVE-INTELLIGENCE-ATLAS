# Chapter Specification — ATLAS-CH-PROGRESSSEARCH-001

## Identity

**Title:** Learning Progress as a Search Operator  
**Status:** specification-ready.

## Contract

Treat learning progress and declared generalization-state evidence as feedback for choosing the next experience and searching experience space.

Hard prerequisite: ATLAS-CH-CURRICULUM-001.

PROGRESSSEARCH inherits the Curriculum observation/action interface and oriented progress signal, then adds experience-space search, exploration, delayed credit, and horizon-sensitive choice.

For region r, inherit

\[
LP_t(r)=\eta_r[m_t(r)-m_{t-w}(r)].
\]

This remains a controller-visible measurement, not a direct mechanism observation.

## Progress-search object

Let the experience space be \(\mathcal E\). Define

\[
\mathfrak S_t=(\mathcal E,z_t,h_t,\widehat{LP}_t,u_t,g_t,\Phi_t,H,B_t),
\]

where \(z_t\) is inherited controller observation, \(h_t\) search state/history, \(\widehat{LP}_t\) progress estimates, \(u_t\) exploration or coverage state, \(g_t\) declared generalization-state evidence, \(\Phi_t\) the declared search objective, \(H\) a horizon, and \(B_t\) remaining budget.

A search operator is

\[
r_t\sim\mathcal S_t(\cdot\mid\mathfrak S_t).
\]

## Generalization-state evidence

Record the evidence interface as

[
g_t(r)=left(g_t^{acq}(r),g_t^{pers}(r),g_t^{access}(r),g_t^{expr}(r)ight).
]

These coordinates stand for declared evidence about acquisition, persistence, accessibility, and behavioral expression. They need not share units and must not be silently summed.

## Objective and exploration

A declared search functional may depend on progress, coverage or uncertainty, generalization evidence, cost, remaining budget, and horizon. Heterogeneous terms require an explicit ordering or scalarization rule.

A pure exploit policy may choose the currently largest estimated progress among observed regions. A search policy must also state how unobserved or uncertain regions can be sampled. Coverage, random exploration, optimism, posterior sampling, or another declared rule may be used; none is universal.

## Exact exploration witness

Use two regions A and B.

Initially A has been observed with progress 1. B is unobserved. The declared toy reward on sampling is

[
R(A)=1,qquad R(B)=3.
]

A pure exploit-only policy restricted to observed regions selects A for two rounds and obtains total reward 2.

A coverage-first policy selects unobserved B first, observes reward 3, then selects B again and obtains total reward 6.

The witness proves only that exploitation over already observed regions can fail to discover a higher-progress unobserved region.
