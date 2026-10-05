# Chapter Specification — ATLAS-CH-PROGRESSSEARCH-001

## Identity

**Title:** Learning Progress as a Search Operator  
**Status:** specification-ready.

## Contract

Treat learning progress and declared generalization-state evidence as feedback for choosing the next experience and searching experience space.

Hard prerequisite: ATLAS-CH-CURRICULUM-001.

PROGRESSSEARCH inherits the Curriculum observation/action interface and oriented progress signal, then adds experience-space search, exploration, delayed credit, and horizon-sensitive choice.

For region r, inherit

[
LP_t(r)=eta_r[m_t(r)-m_{t-w}(r)],
]

with declared metric, lag, orientation, and observation scope.

## Progress-search object

Let the experience space be (mathcal E). Define

[
mathfrak S_t=(mathcal E,z_t,h_t,widehat{LP}_t,u_t,g_t,Phi_t,H,B_t),
]

where (z_t) is inherited controller observation, (h_t) search state/history, (widehat{LP}_t) progress estimates, (u_t) exploration or coverage state, (g_t) declared generalization-state evidence, (Phi_t) the declared search objective, (H) a horizon, and (B_t) remaining budget.

A search operator is

[
r_tsimmathcal S_t(cdotmidmathfrak S_t).
]

Generalization-state evidence is recorded as a vector such as

[
g_t(r)=igl(g_t^{acq},g_t^{pers},g_t^{access},g_t^{expr}igr)(r),
]

for declared evidence about acquisition, persistence, accessibility, and behavioral expression. These coordinates are evidence, not mechanism state, and are not silently summed.

## Objective and exploration

A declared search functional may depend on progress, coverage/uncertainty, generalization evidence, cost, remaining budget, and horizon. Heterogeneous terms require an explicit ordering or scalarization rule.

A pure exploit policy may choose the currently largest estimated progress among observed regions. A genuine search policy must also state how unobserved or uncertain regions can be sampled. Coverage, random exploration, optimism, posterior sampling, or another declared rule may be used; none is universal.
