# From Readability to Functional Evidence
<!-- ATLAS-CH-MECHDIAG-001 -->

**Epistemic status:** audited Evidence and Transformer prerequisites + Atlas-owned finite counterexamples + source-scoped interpretation.  
**Specification:** manuscript/specifications/ATLAS-CH-MECHDIAG-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-MECHDIAG-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MECHDIAG-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MECHDIAG-001.yaml

A representation can contain a perfectly readable feature that the system's output does not use.

This is a problem for a tempting inference: if a probe predicts a concept from an internal activation, it is easy to say that the model uses that concept to make its decision. The first statement is about **recovering information** from a representation; the second concerns **functional dependence** of the declared output on an internal variable.

They require different evidence. The chapter's central question is:

> Which intervention changes the behavior, according to which metric and reference comparison?

A successful local test is still not, by itself, proof of a unique global explanation.

## Exact finite separation

Let an input \(x\) produce an internal representation \(h(x)\in\mathcal H\). A declared downstream map

\[
F:\mathcal H\to\mathcal Y
\]

produces the output \(F(h(x))\).

A probe \(p:\mathcal H\to\mathcal Z\) instead predicts some target quantity \(z(x)\). Its observed predictive success depends on the probe class, evaluated inputs, target definition and evaluation distribution.

A probe's accuracy asks whether \(z\) is **accessible** to that probe. It does not establish that \(F\) reads the same coordinates. In particular,

\[
p(h(x))=z(x)
\quad\not\Rightarrow\quad
F\text{ functionally depends on the probed coordinates}.
\]

The right-hand statement needs a specified dependence or intervention test. Neither question can be answered by an attractive visualization of an activation alone.

**Two-coordinate separation**

Take the finite input domain

\[
x\in\{-1,+1\},\qquad h(x)=(x,x),\qquad F(h_1,h_2)=h_1.
\]

Both coordinate readers

\[
p_1(h)=h_1,\qquad p_2(h)=h_2
\]

recover \(x\) exactly on this domain. Their probe accuracies are identical and perfect. But \(F\) ignores \(h_2\) by definition.

To see the distinction, compare the unmodified state with two zero-setting interventions:

| Input \(x\) | Original \(F(x,x)\) | Set \(h_1=0\): \(F(0,x)\) | Set \(h_2=0\): \(F(x,0)\) |
|---|---:|---:|---:|
| \(-1\) | \(-1\) | \(0\) | \(-1\) |
| \(+1\) | \(+1\) | \(0\) | \(+1\) |

Thus the difference from the original output is nonzero when coordinate 1 is zeroed, but exactly zero when coordinate 2 is zeroed. The conclusion is exact **for this specified map, domain and intervention**. It does not assert that every high-performing probe of a trained model is functionally unused.

**Reference-state substitution control**

Zero is one possible intervention value, not a neutral universal default. A complementary test replaces a coordinate with its value in a declared **clean/reference state**.

Begin at the opposite-input state

\[
h(-x)=(-x,-x).
\]

Patch coordinate 1 from \(h(x)\), obtaining \((x,-x)\). The output becomes

\[
F(x,-x)=x.
\]

Patch coordinate 2 instead, obtaining \((-x,x)\). The output remains

\[
F(-x,x)=-x.
\]

This clean/reference substitution supports the same local separation as the zero-setting test. Crucially, the states \((x,-x)\) and \((-x,x)\) are not among the naturally observed states \(h(\{-1,+1\})\). The algebra is valid because this toy \(F\) is defined on both, but a real network's off-distribution patched activations may require additional controls. A restoration effect does not automatically make the patched state natural or identify a unique circuit.

## Diagnostic record

A component-level assertion should be transported with its actual test, not reduced to “feature \(j\) matters.”

Use the Atlas diagnostic record

\[
D=(B,S,T,M,R),
\]

where:

- \(B\) is the declared target behavior, such as the original output \(F(h(x))\);
- \(S\) is the component or component set under examination;
- \(T\) is the intervention family, including the value being inserted or removed;
- \(M\) is the measured quantity, such as a score difference, error rate or exact output change;
- \(R\) specifies reference inputs, replacement states, baselines and comparison rules.

For the two-coordinate example, one measurable quantity is

\[
M_T(x)=|F(h(x))-F(T(h(x)))|.
\]

At either input \(x\in\{-1,+1\}\), setting \(h_1=0\) gives \(M_T(x)=1\); setting \(h_2=0\) gives \(M_T(x)=0\).

The notation does not create an empirical guarantee. It forces the investigator to declare what was actually varied and what counts as an effect.

## Redundancy boundary

Functional tests have their own false-negative modes. Consider another finite map,

\[
G(h_1,h_2)=\max(h_1,h_2),
\qquad (h_1,h_2)\in\{0,1\}^2.
\]

At \((1,1)\), its output is \(1\). Zeroing either coordinate individually leaves the output unchanged:

\[
G(0,1)=G(1,0)=1.
\]

Zeroing both changes it:

\[
G(0,0)=0.
\]

This is an exact redundancy counterexample. A one-coordinate ablation is null even though the pair jointly sustains the output under the declared intervention. The result licenses

\[
\text{null one-component effect}
\not\Rightarrow
\text{absence of a functionally relevant representation}.
\]

It does **not** prove that every null result hides redundancy. The correct next step is to test justified groups or alternative interventions, with the expanded search space and limitations explicitly reported.

**Three diagnostic outcomes, not two**

A tested property can be:

1. **Accessible:** a specified readout class recovers the property on the evaluated distribution.
2. **Not recovered by this test:** a specified readout fails, or a specified intervention produces no measured change.
3. **Absent under a stronger declared criterion:** a separate, adequately justified search or impossibility argument rules out the property in a specified representation class.

The second category is not automatically the third. Failure to find a linear probe, for example, does not rule out a nonlinear readout. Nor does probe success guarantee downstream functional use.

This distinction prevents a test result from being promoted into a universal information or mechanism claim.

**Localization, restoration and uniqueness**

Locating an activation with a substantial intervention effect is one question. Showing that a chosen small component set is a **complete** explanation is another.

A local restoration can demonstrate sufficiency under the chosen patch and reference comparison. It need not demonstrate:

- necessity against all alternative routes;
- uniqueness among competing component sets;
- completeness over every relevant input;
- minimality under a declared size or cost criterion;
- invariance to a change of representation basis.

For example, if an invertible linear recoding replaces \(h\) by \(Ah\) while the downstream function is correspondingly changed to \(F\circ A^{-1}\), the overall input-output map remains identical, yet the identities of individual coordinates generally change. A coordinate label is therefore not automatically a basis-independent feature.

An evidence report should separate the *tested* component set and representation from claims of globally unique mechanism.

**Activation interventions are not parameter edits**

Changing a hidden activation during one forward pass and editing a model's stored parameters are different operations.

An activation patch compares a behavior under a controlled internal-state substitution. A parameter edit changes the function used by subsequent inputs and can have effects outside the test case. Success on one example does not establish preservation of unrelated behavior, and it does not make the edited parameter location a uniquely identified causal component.

The external interpretability literature recorded in the source lock motivates mechanistic probing, intervention and editing questions. The bibliography keys in that source-lock file are retained as documentary identifiers, not inserted as citations until the manuscript bibliography defines them. This chapter uses those sources as context, not as an authority for a general causal theorem. Its exact proof obligation is confined to the finite constructions above.

**Reading an intervention report**

A reader should be able to ask, in order:

1. Which behavior \(B\) was selected, and on which input distribution?
2. Which internal representation and component set \(S\) were used?
3. Is the result an observational probe, a zero-setting ablation, a clean/reference patch, or a parameter change?
4. What precisely is measured by \(M\), and what comparison is specified by \(R\)?
5. Does the intervention take the system outside its observed or training-supported states?
6. Were related components, groups or alternative paths checked for redundancy?
7. Was the conclusion local to the selected inputs, or was a larger claim independently supported?

The finite examples show why changing only one of these fields can change what follows from the evidence.

**What this chapter does not prove**

Neither exact example is an empirical finding about a deployed neural network. The first proves that a perfectly readable coordinate may be unused by a particular output map. The second proves that null one-coordinate masking can coexist with joint support of a behavior.

The chapter does not prove that a probe identifies a causal mechanism; that successful patching establishes a unique explanation; that a given head, neuron or coordinate has basis-independent semantics; that single-feature masking is generally reliable; or that activation editing and parameter editing are interchangeable.

A spectral correlate is likewise not automatically an interventionally validated explanation.

## Downstream handoff

ATLAS-CH-SPECTRALDIAG-001 may inherit four bounded objects:

- readability versus functional dependence;
- the explicit diagnostic tuple \(D=(B,S,T,M,R)\);
- the two-coordinate readout/patching witness;
- the redundancy control and its null-test warning.

It must independently test any claim that a spectral signature identifies a functional mechanism. The presence of a readable or statistically distinctive spectral feature does not, on its own, satisfy that requirement.

The durable rule is:

> An internal measurement becomes functional evidence only relative to a declared behavior, intervention, metric, reference rule and tested scope.

## References used in this chapter

- Elazar et al. (2021), identifier `ElazarEtAl2021Amnesic`.
- Meng et al. (2022), identifier `MengEtAl2022FactualAssociations`.
- Wang et al. (2023), identifier `WangEtAl2023Interpretability`.

These source-lock identifiers still need bibliographic reconciliation before chapter-level citation signoff.

Exact source identities, prerequisite locks and finite claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-MECHDIAG-001.yaml
