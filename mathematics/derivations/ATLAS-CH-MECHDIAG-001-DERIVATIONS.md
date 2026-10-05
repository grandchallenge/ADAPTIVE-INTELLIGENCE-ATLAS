# ATLAS-CH-MECHDIAG-001 — Derivation Packet

## 1. Readability is not functional dependence

Let an input x produce an internal vector h(x), and let the system output be y=F(h). A probe p(h) can predict a target from h. High probe accuracy establishes readability relative to the chosen probe class and data distribution. It does not imply that F depends on the coordinates used by p.

For a declared transformation T, define the measured difference

\[
E_T(x)=s(F(h(x)))-s(F(T(h(x)))),
\]

where s is the declared task score. The transformation, replacement value, metric, and input set are part of the result.

## 2. Exact counterexample

Take

\[
x\in\{-1,+1\},\qquad h(x)=(x,x),\qquad F(h)=h_1.
\]

Both coordinate probes recover x exactly. Yet

\[
F(0,h_2)=0,\qquad F(h_1,0)=x.
\]

Thus perfect prediction by the second coordinate coexists with zero dependence of F on that coordinate.

## 3. Reference substitution

Start from the reference state h(-x)=(-x,-x). Replacing coordinate 1 by its value from h(x) gives (x,-x) and output x. Replacing coordinate 2 gives (-x,x) and output -x. The substitution therefore separates the used coordinate from the equally predictive spectator coordinate.

## 4. Redundancy warning

A null single-coordinate result is not an absence proof. For example, with binary coordinates and

\[
F(h_1,h_2)=\max(h_1,h_2),
\]

at state (1,1), setting either coordinate alone to zero leaves the output unchanged. Either coordinate can still support the result.

Therefore

\[
\text{null one-coordinate effect}\not\Rightarrow\text{no relevant representation}.
\]

## 5. Test-relative claims

A result is always relative to a declared component set, transformation family, metric, and reference rule. A replacement can also create an unusual state, so multiple controls may be required before a local result is promoted to a broader explanation.

A useful Atlas record is

\[
D=(B,S,T,M,R),
\]

where B is the target behavior, S the selected components, T the tested transformations, M the metric, and R the reference rule.

## 6. Operational diagnostic states

A property is accessible when a declared readout class recovers it from the tested representation. Failure of one readout class establishes only inaccessibility relative to that class. A stronger statement that information is absent requires a broader declared search and cannot be inferred from one failed probe.

## 7. Downstream boundary

ATLAS-CH-SPECTRALDIAG-001 may inherit the distinction between readability and functional dependence, the redundancy warning, the reference-substitution test, and the diagnostic record D. It must independently justify any proposed spectral signature. A spectral correlate is not automatically a functional explanation.

## Claim boundary

This packet proves the displayed finite examples and defines Atlas-local bookkeeping. External empirical results remain scoped to their reported systems and tasks.
