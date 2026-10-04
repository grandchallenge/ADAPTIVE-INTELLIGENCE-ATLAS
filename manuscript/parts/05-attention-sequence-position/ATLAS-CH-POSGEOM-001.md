# The Geometry of Position
<!-- ATLAS-CH-POSGEOM-001 -->

**Epistemic status:** mathematical exposition built from audited Attention and Geometry prerequisites, primary positional-encoding sources, and Atlas-owned exact witnesses.  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-POSGEOM-001-DERIVATIONS.md\`  
**Computational witness:** \`mathematics/computational-witnesses/ATLAS-CW-POSGEOM-001.md\`

## 1. Position is not content

A Transformer sees token representations.

Without an asymmetric mask or positional signal, ordinary self-attention is permutation equivariant: permuting the token order permutes the output order.

Sequence order therefore has to enter somewhere.

The first conceptual separation is:

\[
\boxed{
\text{content geometry}
\neq
\text{position geometry}.
}
\]

Content determines what a token represents.

Position determines where that token sits in a declared coordinate system.

The two interact inside attention, but they are not the same object.

This chapter develops position as an explicit transformation acting on attention representations.

## 2. Additive sinusoidal position

The original Transformer adds a fixed sinusoidal vector to the token embedding [@VaswaniEtAl2017].

For one angular frequency \(\omega\), consider the two-dimensional component

\[
p_m(\omega)
=
\begin{pmatrix}
\sin(m\omega)\\
\cos(m\omega)
\end{pmatrix}.
\]

A fixed offset \(\delta\) acts linearly:

\[
p_{m+\delta}
=
A_\delta p_m,
\]

where \(A_\delta\) is a rotation matrix determined by \(\delta\omega\).

That fact explains the original motivation: relative displacement can be represented through a position-independent linear transform of the sinusoidal features.

But the mechanism is still additive.

The positional vector is added to the representation before later layers act.

## 3. Rotary position moves the geometry into query and key space

Rotary Position Embedding takes a different route [@SuEtAl2021RoFormer].

Instead of adding a positional vector, it rotates query and key coordinates as a function of position.

For one 2D block define

\[
R(\phi)
=
\begin{pmatrix}
\cos\phi&-\sin\phi\\
\sin\phi&\cos\phi
\end{pmatrix}.
\]

At position \(m\), use

\[
R_m(\omega)=R(m\omega).
\]

Apply that rotation to the corresponding query and key block.

The crucial algebra is

\[
R(\phi)^\top
=
R(-\phi),
\]

so

\[
R_m(\omega)^\top R_n(\omega)
=
R((n-m)\omega).
\]

Therefore

\[
(R_m q)^\top(R_n k)
=
q^\top R((n-m)\omega)k.
\]

The absolute positions \(m\) and \(n\) disappear from this pairwise expression except through their difference.

This is the core relative-position identity.

## 4. What the identity actually says

The identity is exact.

It says that the contribution of one rotary block to the query-key inner product is determined by:

- the unrotated query block;
- the unrotated key block;
- the frequency;
- the relative displacement \(n-m\).

It does not say that the whole model depends only on relative position.

Other components can break that symmetry:

- causal masks;
- finite sequence boundaries;
- content distributions;
- layerwise nonlinearities;
- caches;
- architecture-specific operations;
- any additional position-dependent mechanism.

The exact statement belongs to the transformed query-key score contribution.

## 5. An exact same-offset witness

Choose

\[
\theta=\pi/6,
\qquad
q=k=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
\]

Compare positions \((0,2)\).

The relative offset is \(2\), so

\[
(R_0q)^\top(R_2k)
=
\cos(2\theta)
=
\frac12.
\]

Now compare positions \((3,5)\).

The relative offset is still \(2\), and

\[
(R_3q)^\top(R_5k)
=
\frac12.
\]

The absolute coordinates moved.

The rotary score contribution did not.

This is a finite replay of the relative-position identity.

## 6. Why the rotation structure matters

The result is not true for arbitrary position-dependent transforms.

Define instead

\[
S_m
=
\operatorname{diag}(2^m,1).
\]

Using the same \(q=k=(1,0)^\top\),

\[
(S_m q)^\top(S_n k)
=
2^{m+n}.
\]

For the same-offset pair \((0,2)\),

\[
\text{score}=4.
\]

For the same-offset pair \((3,5)\),

\[
\text{score}=256.
\]

The relative displacement is identical.

The score is not.

What changed?

The family \(S_m\) does not satisfy the rotary group relation

\[
T_m^\top T_n=T_{n-m}.
\]

The exact relative-position identity depends on the structure of the transform family.

## 7. Multi-frequency position

Real rotary encodings use many 2D blocks.

For even dimension \(d=2h\),

\[
R_m
=
\operatorname{diag}
\left(
R(m\omega_1),
\ldots,
R(m\omega_h)
\right).
\]

Then

\[
R_m^\top R_n
=
\operatorname{diag}
\left(
R((n-m)\omega_1),
\ldots,
R((n-m)\omega_h)
\right).
\]

Each block sees the same displacement through a different phase rate.

The frequency schedule therefore determines how relative displacement is represented across coordinates.

Low frequencies rotate slowly.

High frequencies rotate quickly.

The resulting positional representation is a bank of phase measurements at multiple scales.

## 8. Position as phase

The phase viewpoint is more useful than thinking of RoPE as "just another embedding."

For one frequency,

\[
m
\longmapsto
m\omega
\longmapsto
R(m\omega).
\]

Position becomes a group parameter.

The representation at position \(m\) is related to position \(n\) by the phase difference

\[
(n-m)\omega.
\]

This makes several properties transparent:

- common translation cancels in pairwise phase difference;
- different frequencies resolve displacement differently;
- rescaling position changes phase;
- rescaling frequency also changes phase;
- those two interventions can look algebraically related while being operationally distinct.

## 9. Common translation

Shift every position by the same amount \(c\).

Then

\[
(n+c)-(m+c)=n-m.
\]

So

\[
R_{m+c}^\top R_{n+c}
=
R_{n-m}.
\]

The rotary query-key contribution is invariant under a common shift of both position indices.

Again, this is not a theorem that the full sequence model is translation invariant.

It is an exact property of the rotary score geometry.

## 10. Multidimensional position

A sequence uses one coordinate.

Images, grids, fields, and other structured domains may need several.

Let a 2D position be

\[
p=(u,v).
\]

Use two independent rotary blocks:

\[
R_p
=
\operatorname{diag}
\left(
R(u\omega_x),
R(v\omega_y)
\right).
\]

For another position

\[
q=(u',v'),
\]

we obtain

\[
R_p^\top R_q
=
\operatorname{diag}
\left(
R((u'-u)\omega_x),
R((v'-v)\omega_y)
\right).
\]

The pairwise operator depends on the coordinate-wise displacement.

This is the direct-product version of the one-dimensional construction.

The important point is not that every 2D positional method must use this formula.

It is that multidimensional position needs an explicit coordinate action.

Duplicating a scalar position label does not automatically create geometry.

## 11. Position and attention support are separate

A causal mask and positional encoding do different jobs.

The mask decides whether an attention edge is allowed.

The positional transformation affects the score attached to an allowed query-key pair.

A pair may have a well-defined relative phase and still be masked out.

This distinction keeps support geometry separate from score geometry.

## 12. Exact algebra does not guarantee long-context generalization

The identity

\[
R_m^\top R_n=R_{n-m}
\]

continues to make algebraic sense far beyond any finite training context.

That does not mean the trained model knows how to use those phases.

A model is trained under a finite distribution of:

- absolute positions;
- relative displacements;
- phase combinations;
- sequence lengths;
- attention patterns;
- optimization conditions.

Outside that regime, exact continuation of the positional formula is only one ingredient.

The model-level question is empirical.

## 13. Direct extrapolation

The simplest long-context strategy is to evaluate the same positional rule at larger indices.

For rotary position, that means evaluating phases

\[
m\omega
\]

for \(m\) beyond the range used in training.

The formula is valid.

The behavior need not be.

This is the distinction between:

\[
\boxed{
\text{formula extrapolates}
}
\]

and

\[
\boxed{
\text{trained model generalizes}.
}
\]

They are not equivalent.

## 14. Position Interpolation

Position Interpolation changes the coordinate presented to the positional mechanism [@ChenEtAl2023PositionInterpolation].

Suppose the original context scale is \(L\) and the desired scale is \(L'>L\).

A simple interpolation map is

\[
m
\longmapsto
\tilde m
=
m\frac{L}{L'}.
\]

The phase becomes

\[
\tilde m\omega
\]

instead of \(m\omega\).

The paper reports that this can extend RoPE-based pretrained models with relatively limited fine-tuning and gives a theoretical comparison between interpolation and direct extrapolation under its stated analysis.

The Atlas uses that result at its actual scope.

It is not a theorem that every model, every frequency schedule, or every target length will behave well under the same rescaling.

## 15. YaRN

YaRN belongs to the same broader problem family but is not merely "Position Interpolation again" [@PengEtAl2023YaRN].

It combines positional rescaling ideas with additional treatment intended to improve efficient long-context extension.

The reported results are empirical method evidence.

The relevant Atlas lesson is structural:

> Long-context extension is an intervention on the positional phase regime and often also on training.

The exact rotary identity remains true before and after such modifications.

What changes is which phases the model encounters and how well its learned computation handles them.

## 16. Frequency scaling and index scaling are different interventions

Consider a phase

\[
m\omega.
\]

One can change it by:

- replacing \(m\) with \(\alpha m\);
- replacing \(\omega\) with \(\alpha\omega\);
- changing both nonuniformly across frequencies;
- fine-tuning after the change.

These may coincide algebraically in a single isolated block under special choices.

They are not operationally interchangeable in a full model.

A positional extension method should therefore state exactly what it changes.

## 17. The geometry of extrapolation

Long-context behavior is often described as if context length were one scalar knob.

Geometrically, several things can move at once:

- the range of phase angles;
- the density of sampled offsets;
- aliasing relationships across frequencies;
- the distribution of query-key content seen at those phases;
- mask/boundary effects;
- the learned response to phase combinations.

This is why the positional mechanism can remain mathematically well-defined while the trained system degrades.

The geometry survives.

The learned use of the geometry may not.

## 18. Failure modes

### 18.1 Additive equals rotary

It does not.

Both use sinusoidal structure, but one adds position features while the other rotates query/key coordinates.

### 18.2 Relative identity equals long-context guarantee

It does not.

The identity is algebraic.

Generalization is model-level.

### 18.3 Any position transform works

It does not.

The non-orthogonal control shows that same-offset dependence can fail.

### 18.4 Frequency schedule equals context policy

It does not.

The schedule defines phase rates.

A context-extension policy says how positions/frequencies/training are changed when the target range changes.

### 18.5 2D means two copies of 1D

Not automatically.

The coordinate action has to be declared.

### 18.6 Interpolation equals extrapolation

They are opposite geometric choices.

Interpolation maps a larger target range back into a smaller phase regime.

Direct extrapolation evaluates outside that regime.

### 18.7 Position explains all long-context behavior

It does not.

Attention content, optimization, retrieval, memory, architecture, and training distribution all matter.

## 19. Downstream handoff

Relative-Position Operators may assume:

- the exact block-rotation identity;
- the multi-frequency decomposition;
- common-translation invariance of the rotary score contribution;
- multidimensional direct-product position;
- the distinction between exact positional algebra and empirical context extension.

It may not assume that vector RoPE already provides:

- a low-dimensional operator decomposition;
- a DC-mode theory;
- frequency-mode specialization;
- head-specific relative-position operators.

Those are the next chapter's obligations.

## References used in this chapter

- [@VaswaniEtAl2017] — fixed additive sinusoidal positional encoding.
- [@SuEtAl2021RoFormer] — rotary position embedding and relative-position score construction.
- [@ChenEtAl2023PositionInterpolation] — Position Interpolation for RoPE-based context extension.
- [@PengEtAl2023YaRN] — YaRN context-extension method.

Exact provenance and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-POSGEOM-001.yaml\`
