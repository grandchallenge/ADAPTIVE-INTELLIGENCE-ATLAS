# ATLAS-CH-TRANSFER-001 — Derivation Packet

## D1. Standard source/target framing

Following Pan and Yang [@PanYang2010], a domain is described by an input space and distribution,

\[
\mathcal D=(\mathcal X,P(X)),
\]

and a task by an output space and prediction object,

\[
\mathcal T=(\mathcal Y,f).
\]

A transfer problem relates a source domain/task pair to a target domain/task pair.

The Atlas does not collapse all transfer settings into one formalism. The remainder of this packet isolates one exact reconstruction setting.

## D2. Source and target representations

Let

\[
E_s:X\to Z_s
\]

be a source representation and

\[
E_t:X\to Z_t
\]

a target representation.

Let

\[
R:X\to\mathcal R
\]

be a declared admissible common Residual.

Suppose there exist compilers

\[
C_s:Z_s\to\mathcal R,
\qquad
C_t:Z_t\to\mathcal R
\]

such that

\[
\boxed{
C_s(E_s(x))
=
C_t(E_t(x))
=
R(x)
}
\]

for every declared state \(x\).

## D3. Target capability family

Let \(\mathcal Q_t\) be a family of target probes/tasks.

For every \(q\in\mathcal Q_t\), suppose there is a decoder

\[
D_q:\mathcal R\to\mathcal Y_q
\]

such that

\[
\boxed{
B_t(x,q)
=
D_q(R(x)).
}
\]

Then both source and target representations are sufficient for exact reconstruction of the target capability family through the common Residual.

Indeed,

\[
B_t(x,q)
=
D_q(C_s(E_s(x)))
\]

and

\[
B_t(x,q)
=
D_q(C_t(E_t(x))).
\]

This is the **common-Residual reconstruction certificate**.

It is sufficient.

It is not claimed necessary.

A direct source-to-target adapter can exist without an explicitly identified common Residual.

## D4. Exact linear witness

Let transferable structure be

\[
r=
\begin{pmatrix}
a\\
b
\end{pmatrix}.
\]

Define source representation

\[
z_s=A_s r,
\qquad
A_s=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Since

\[
\det(A_s)=-2,
\]

the matrix is invertible.

Define target representation

\[
z_t=A_t r,
\qquad
A_t=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

Since

\[
\det(A_t)=1,
\]

this matrix is also invertible.

Set

\[
C_s=A_s^{-1},
\qquad
C_t=A_t^{-1}.
\]

Then

\[
C_s z_s=r,
\qquad
C_t z_t=r.
\]

## D5. Exact numeric reconstruction

Take

\[
r=(3,1).
\]

Then

\[
z_s
=
A_s r
=
(4,2),
\]

and

\[
z_t
=
A_t r
=
(6,1/2).
\]

Both compilers recover

\[
r=(3,1).
\]

Define target tasks

\[
D_1(r)=a+b,
\]

and

\[
D_2(r)=2a-b.
\]

Then

\[
D_1(r)=4,
\]

and

\[
D_2(r)=5.
\]

Both source and target representations therefore reconstruct the same exact target capability outputs through the common Residual.

## D6. One-task sufficiency need not imply task-family sufficiency

Consider bottleneck

\[
P(r)=a.
\]

For any task depending only on \(a\), this bottleneck may be sufficient.

For the task

\[
D_2(r)=2a-b,
\]

it is not.

Take

\[
r_A=(1,0),
\qquad
r_B=(1,1).
\]

Then

\[
P(r_A)=P(r_B)=1,
\]

but

\[
D_2(r_A)=2,
\]

and

\[
D_2(r_B)=1.
\]

Therefore no deterministic decoder

\[
d:\mathbb R\to\mathbb R
\]

can satisfy

\[
d(P(r))=D_2(r)
\]

for both states.

This is an exact impossibility result caused by a lossy bottleneck.

## D7. Fiber criterion for exact capability reconstruction

More generally, let

\[
Z:X\to\mathcal Z
\]

be any representation and let

\[
B:X\to\mathcal Y
\]

be a deterministic capability map.

A deterministic decoder

\[
D:\mathcal Z\to\mathcal Y
\]

with

\[
B=D\circ Z
\]

exists if and only if \(B\) is constant on every fiber of \(Z\).

That is,

\[
Z(x_1)=Z(x_2)
\Rightarrow
B(x_1)=B(x_2).
\]

### Necessity

If

\[
B=D\circ Z
\]

and

\[
Z(x_1)=Z(x_2),
\]

then

\[
B(x_1)
=
D(Z(x_1))
=
D(Z(x_2))
=
B(x_2).
\]

### Sufficiency

If \(B\) is constant on fibers of \(Z\), define \(D(z)\) to be the common \(B(x)\) value for any \(x\) with \(Z(x)=z\), on the realized image of \(Z\).

This is well-defined by the fiber condition.

Thus exact transfer failure after a bottleneck can be diagnosed by finding two capability-distinct states in the same representation fiber.

## D8. Transfer and information loss

The fiber criterion is deterministic.

An information-theoretic version asks how much target-relevant information remains after compression.

The Information chapter supplies entropy, KL divergence, mutual information, and sufficiency language.

The chapter does not equate mutual information with transfer quality.

Optimization difficulty, finite data, decoder class, and distribution shift remain separate.

## D9. Source performance is not transferability

A representation can be highly specialized to its source task.

Yosinski et al. experimentally show that layer transferability changes with task distance and layer specialization, and that optimization/co-adaptation effects also matter [@YosinskiEtAl2014].

Kornblith et al. show that source benchmark quality and transfer-feature quality are not interchangeable and that training choices can affect transfer performance [@KornblithShlensLe2019].

These empirical findings support a bounded conclusion:

\[
\boxed{
\text{source performance}
\not\Rightarrow
\text{universal transfer quality}.
}
\]

## D10. Operational negative transfer

Let

\[
M_{\mathrm{transfer}}
\]

be a declared transfer procedure and

\[
M_{\mathrm{target}}
\]

a matched target-only baseline under a declared target metric \(J\).

For a higher-is-better metric, call the outcome negative transfer when

\[
J(M_{\mathrm{transfer}})
<
J(M_{\mathrm{target}}).
\]

For a lower-is-better loss, reverse the inequality.

This is an operational comparison.

It depends on the baseline, metric, data budget, and adaptation procedure.

## D11. Exact recoding does not imply easy adaptation

If source and target representations differ by an invertible map, no information is lost.

Yet a learner may still fail to discover the adapter under finite data, constrained decoder class, poor conditioning, or optimization difficulty.

Therefore:

\[
\boxed{
\text{information-preserving transfer path}
\neq
\text{guaranteed learnable transfer procedure}.
}
\]

The common-Residual certificate is semantic/reconstructive unless computational constraints are added.

## D12. Relation to the Residual formalism

The audited Residual chapter defines sufficiency and leastness relative to declared descriptor and post-processing classes.

Transfer adds a cross-system requirement:

the source and target must both be able to compile to a shared admissible object, or otherwise support an admissible adapter preserving the declared capability family.

The common Residual is one clean way to express that shared structure.

## Claim boundary

This packet proves a sufficient common-Residual reconstruction certificate, a deterministic fiber criterion for exact decoding, and one exact bottleneck impossibility witness.

It does not provide a necessary-and-sufficient theory of transfer learning under finite data, stochastic optimization, distribution shift, or restricted adaptation procedures.
