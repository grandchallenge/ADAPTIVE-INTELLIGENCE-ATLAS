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
