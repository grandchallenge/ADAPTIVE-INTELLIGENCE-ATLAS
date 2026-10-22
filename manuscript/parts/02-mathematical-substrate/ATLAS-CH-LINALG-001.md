# Linear Maps and Decompositions
<!-- ATLAS-CH-LINALG-001 -->

**Epistemic status:** Established Theory + Atlas Derivation  
**Specification:** manuscript/specifications/ATLAS-CH-LINALG-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-LINALG-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-LINALG-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-LINALG-001.yaml

## 1. Linear algebra as transformation language

A matrix is often introduced as a rectangular table of numbers.

That description is correct and insufficient.

For the Atlas, the important object is the linear map.

Given finite-dimensional vector spaces \(V\) and \(W\), a linear transformation is a map

\[
T:V\to W
\]

satisfying

\[
T(\alpha x+\beta y)
=
\alpha T(x)+\beta T(y).
\]

Once bases are chosen, \(T\) is represented by a matrix \(A\).

The matrix is a coordinate description of the map.

Changing basis changes the coordinates used to describe the same transformation.

Changing the operator changes the transformation itself.

This distinction is the first reason linear algebra matters here.

## 2. Changing lenses versus changing the machine

Imagine observing one machine through different camera angles.

The pictures change.

The machine does not.

A change of basis plays a similar role.

The coordinates of a vector and the matrix representing an operator change together.

The underlying linear relation can remain the same.

The analogy has a limit.

A basis change is an exact algebraic transformation, not merely a visual viewpoint.

And many learned transformations are nonlinear, state-dependent, or not globally representable by one fixed matrix.

The analogy is useful only for separating coordinate description from operator identity.

## 3. Bases and coordinate representations

Let

\[
B=\{b_1,\ldots,b_n\}
\]

be a basis of \(V\).

Any vector \(x\in V\) has a unique coordinate vector

\[
[x]_B.
\]

If \(T:V\to W\) and \(C\) is a basis of \(W\), then there is a matrix

\[
[T]_{C\leftarrow B}
\]

such that

\[
[T(x)]_C
=
[T]_{C\leftarrow B}[x]_B.
\]

This equation is the bridge between abstract linear maps and matrix computation.

For a second pair of bases \(\widetilde B,\widetilde C\), let \(S_V\) and \(S_W\) convert their coordinates to the original bases:

\[
[x]_B=S_V[x]_{\widetilde B},
\qquad
[y]_C=S_W[y]_{\widetilde C}.
\]

The same linear map is represented in the new bases by

\[
\boxed{
[T]_{\widetilde C\leftarrow\widetilde B}
=
S_W^{-1}[T]_{C\leftarrow B}S_V.
}
\]

Only when domain and codomain are the same vector space and the same basis change is used on both sides does this reduce to a similarity transformation \(S^{-1}AS\). A general change of input and output bases is not necessarily a similarity and need not preserve matrix eigenvalues.

This is an exact statement about coordinates, not a claim that every learned nonlinear layer is a fixed linear map.

The Atlas will often work directly with matrices.

But the operator viewpoint remains useful because it prevents basis-dependent coordinates from being mistaken for invariant structure.

## 4. Subspaces

A subspace is a subset closed under linear combination.

Three recurring subspaces are:

\[
\operatorname{range}(A),
\]

\[
\operatorname{null}(A),
\]

and, for a matrix acting on an inner-product space, orthogonal complements of these spaces.

Subspaces matter because many later problems are really questions about which directions:

- survive a transformation;
- are erased;
- are amplified;
- are identifiable;
- are reachable.

Rank is the dimension of the image:

\[
\operatorname{rank}(A)
=
\dim \operatorname{range}(A).
\]

A low-rank operator therefore communicates through a lower-dimensional effective channel.

That can be useful compression.

It can also be information loss.

## 5. Orthogonal projection

Suppose \(Q\in\mathbb R^{n\times k}\) has orthonormal columns:

\[
Q^\top Q=I.
\]

Then

\[
P=QQ^\top
\]

is the orthogonal projector onto the column space of \(Q\).

Indeed,

\[
P^2
=
QQ^\top QQ^\top
=
QIQ^\top
=
P,
\]

and

\[
P^\top=P.
\]

Projection is one of the simplest examples of an operator whose geometry is visible.

It keeps components inside one subspace and removes orthogonal components.

Later chapters use this language for tangent projections, subspace methods, low-rank structure, and constrained updates.

## 6. Eigendecomposition

For a square matrix \(A\), an eigenpair satisfies

\[
Av=\lambda v.
\]

An eigenvector is a direction mapped back into its own span.

If \(A\) is diagonalizable,

\[
A=V\Lambda V^{-1}.
\]

Then powers satisfy

\[
A^k
=
V\Lambda^k V^{-1}.
\]

This is powerful.

It is also easy to overuse.

Eigenvalues directly describe asymptotic modal behavior only under assumptions that later chapters will make explicit.

If \(V\) is badly conditioned, eigenvalues can be a poor guide to finite-time amplification.

The Non-normality keystone exists largely because that distinction matters.

## 7. Normality

A real matrix is normal when

\[
A^\top A
=
AA^\top.
\]

In complex spaces the transpose is replaced by the adjoint.

Over \(\mathbb C\), normal matrices admit orthonormal eigenvector bases and unitary diagonalization. For real normal matrices the corresponding diagonalization may require complex eigenvectors. For example,

\[
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

satisfies \(R^\top R=RR^\top=I\) but has eigenvalues \(i\) and \(-i\), and no nonzero real eigenvectors.

Thus normality does not, by itself, promise an orthonormal **real** eigenbasis.

This property greatly simplifies spectral reasoning.

A non-normal matrix need not.

The Atlas will therefore use the word “normal” carefully.

It does not mean statistically normal.

It describes an operator relation.

## 8. Singular-value decomposition

For any real matrix

\[
A\in\mathbb R^{m\times n},
\]

the singular-value decomposition is

\[
\boxed{
A=U\Sigma V^\top
}
\]

where the **full SVD** uses orthogonal matrices \(U\in\mathbb R^{m\times m}\) and \(V\in\mathbb R^{n\times n}\) and rectangular diagonal \(\Sigma\in\mathbb R^{m\times n}\) with nonnegative singular values.

Equivalently, if \(r=\operatorname{rank}(A)\), its compact form is

\[
A=U_r\Sigma_rV_r^\top,
\quad
U_r\in\mathbb R^{m\times r},
\quad
\Sigma_r\in\mathbb R^{r\times r},
\quad
V_r\in\mathbb R^{n\times r},
\]

where \(U_r\) and \(V_r\) have orthonormal columns and \(\Sigma_r\) lists the positive singular values. The zero matrix has rank \(r=0\) and is covered by the full SVD.

The right singular vectors identify input directions.

The left singular vectors identify corresponding output directions.

The singular values quantify amplification:

\[
Av_i
=
\sigma_i u_i.
\]

This makes the SVD one of the Atlas's central linear tools.

It works for rectangular matrices.

It does not require diagonalizability.

And it directly answers Euclidean gain questions.

Standard treatments appear in Trefethen and Bau [@TrefethenBau1997], Horn and Johnson [@HornJohnson2012], and Golub and Van Loan [@GolubVanLoan2013].

## 9. Operator norm

The induced Euclidean norm is

\[
\|A\|_2
=
\sup_{\|x\|_2=1}\|Ax\|_2.
\]

The SVD gives

\[
\boxed{
\|A\|_2
=
\sigma_{\max}(A).
}
\]

This is not merely notation.

It says the largest singular value is the greatest one-step amplification of a unit vector under the Euclidean norm.

Later chapters on boundary sensitivity, optimization, and transient growth use exactly this interpretation.

## 10. Eigenvalues and singular values answer different questions

Consider

\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Both eigenvalues equal \(1\).

But the singular values are

\[
\sigma_1
=
\frac{1+\sqrt5}{2},
\]

and

\[
\sigma_2
=
\frac{\sqrt5-1}{2}.
\]

Therefore

\[
\|A\|_2
=
\frac{1+\sqrt5}{2}
>
1.
\]

A unit vector can be amplified in one step even though every eigenvalue has modulus \(1\).

The same matrix is a Jordan block, not diagonalizable: its only eigenvector direction is \(e_1\). For every integer \(k\ge0\),

\[
A^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}.
\]

Thus repeated application can amplify particular vectors by a factor growing with \(k\), despite a spectral radius of one. This is an exact finite-dimensional counterexample; it does not license an analogous claim about a trained network without identifying its actual update operator.

This is the smallest important lesson:

\[
\boxed{
\text{spectral radius}
\neq
\text{operator norm}
}
\]

in general.

The Non-normality chapter develops the consequences.

## 11. Pseudoinverse and least squares

For a linear system \(Ax=b\), least squares minimizes \(\|Ax-b\|_2\), including when no exact solution exists. For rank-deficient matrices, the set of minimizers need not contain only one point.

Using

\[
A=U\Sigma V^\top,
\]

define the Moore–Penrose pseudoinverse

\[
A^+
=
V\Sigma^+U^\top,
\]

where each nonzero singular value is inverted.

Then

\[
x_\star=A^+b
\]

selects the **unique minimum-Euclidean-norm member** of the set of least-squares minimizers; it does not assert that every least-squares minimizer is unique.

For example, \(A=\operatorname{diag}(1,0)\) and \(b=(2,3)^\top\) give

\[
\arg\min_x\|Ax-b\|_2
=
\{(2,t)^\top:t\in\mathbb R\},
\qquad
A^+b=(2,0)^\top,
\qquad
\|AA^+b-b\|_2=3.
\]

The surviving residual is unavoidable; choosing the pseudoinverse also sets the undetermined second component to zero. A new exact witness below replays this distinction.

This object recurs in inverse problems, linear probes, regression, and local approximations.

## 12. Low-rank approximation

Suppose

\[
A=U\Sigma V^\top
\]

with singular values

\[
\sigma_1\ge\sigma_2\ge\cdots.
\]

Truncating after \(k\) singular components gives

\[
A_k
=
U_k\Sigma_kV_k^\top.
\]

The Eckart–Young theorem identifies \(A_k\) as a best rank-\(k\) approximation in the spectral and Frobenius norms.

In the spectral norm,

\[
\|A-A_k\|_2
=
\sigma_{k+1}.
\]

For the witness matrix above, the best rank-one error is

\[
\frac{\sqrt5-1}{2}.
\]

Low rank is therefore a precise approximation concept.

It is not automatically semantic compression.

A small matrix approximation error can still erase a downstream feature that matters.

## 13. Conditioning

Some problems are intrinsically sensitive.

Suppose

\[
D=
\begin{pmatrix}
1&0\\
0&1/100
\end{pmatrix}.
\]

Then

\[
\sigma_{\max}(D)=1,
\qquad
\sigma_{\min}(D)=1/100.
\]

The \(2\)-norm condition number is

\[
\boxed{
\kappa_2(D)=100.
}
\]

The weak singular direction is much more sensitive to inversion.

This is a property of the problem.

It must be distinguished from the stability of a particular algorithm used to solve it.

That distinction becomes central in Numerical Intelligence.

## 14. Condition number is not optimization difficulty

A large matrix condition number can matter greatly.

But it does not by itself prove that a nonlinear training problem will be difficult.

Training dynamics also depend on:

- parameterization;
- optimizer state;
- curvature variation;
- stochastic gradients;
- non-normality;
- constraints;
- numerical precision;
- data ordering.

The Atlas therefore treats conditioning as one diagnostic quantity, not a universal explanation.

## 15. Block structure

Large transformations often have meaningful block structure.

For example,

\[
A=
\begin{pmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{pmatrix}
\]

can represent coupling among subsystems.

Block Jacobians later make optimizer-state dynamics explicit.

Boundary composition can also be analyzed through block sensitivity.

The point is structural:

a matrix need not be an undifferentiated table.

Its partition can encode a model of interactions.

## 16. Kronecker structure

For matrices \(A\) and \(B\), the Kronecker product

\[
A\otimes B
\]

constructs a larger structured linear map.

Kronecker products appear in:

- separable transformations;
- tensor-product bases;
- covariance approximations;
- structured preconditioners.

This chapter does not develop the full theory.

It establishes the notation and the idea that large operators may be described compositionally.

## 17. What linearization does and does not buy us

Even nonlinear systems have local linear structure.

If

\[
F:\mathbb R^n\to\mathbb R^m
\]

is differentiable, then near \(x\),

\[
F(x+\delta)
\approx
F(x)+J_F(x)\delta.
\]

The Jacobian is a linear operator.

This lets the Atlas reuse:

- singular values;
- operator norms;
- projections;
- condition estimates.

But local linearization is local.

A Jacobian at one point does not automatically describe a global nonlinear system.

The Boundary Contracts and optimizer-dynamics chapters both rely on this limitation.

## 18. Computational witness {#computational-witness-1}

![The unit circle mapped by a non-normal matrix into an ellipse beside an exact conditioning example with condition number 100.](../../figures/masters/ATLAS-FIG-LINALG-001.png)

The companion witness replays three exact facts.

For

\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\]

Wolfram returns eigenvalues

\[
1,1
\]

and singular values

\[
\frac{1+\sqrt5}{2},
\qquad
\frac{\sqrt5-1}{2}.
\]

For the projection

\[
P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]

it verifies

\[
P^2=P.
\]

For

\[
D=
\begin{pmatrix}
1&0\\
0&1/100
\end{pmatrix},
\]

it verifies

\[
\kappa_2(D)=100.
\]

The expanded witness also replays the rank-deficient pseudoinverse case and the real-normal rotation counterexample. It keeps algebraic identities distinct from any downstream machine-learning interpretation.

The witness is exact finite-dimensional mathematics.

It does not imply a neural-network mechanism.

## 19. Five failure modes

### Coordinates mistaken for invariants

A matrix entry can change under basis change while the operator remains the same.

### Eigenvalues mistaken for all amplification

Non-normal operators can have large singular gain despite benign-looking eigenvalues.

### Low rank mistaken for semantic sufficiency

A good norm approximation can still lose task-critical information.

### Conditioning mistaken for algorithm failure

An ill-conditioned problem and an unstable algorithm are different objects.

### Local linearization mistaken for global behavior

A Jacobian is a local differential object.

## 20. Atlas connections

**Geometry.**  
Tangent spaces are linear spaces attached to nonlinear manifolds.

**Attention.**  
Attention matrices act as state-dependent linear mixing operators on value fields when the mixing weights are fixed.

**Optimization.**  
Hessians, preconditioners, and update operators are linear-algebraic objects embedded in nonlinear dynamics.

**Numerical intelligence.**  
Conditioning, projections, factorizations, and Krylov methods are core tools.

**Memory and representation.**  
Low-rank and subspace structure can describe compressed state, but semantic adequacy is a separate question.

## 21. Closing view

Linear algebra is not here because neural networks contain matrices.

It is here because adaptive systems repeatedly ask linear questions inside larger nonlinear ones.

Which directions survive?

Which directions are amplified?

Which subspace matters?

Which information is lost?

Which coordinate change is merely descriptive?

Which operator is ill-conditioned?

The SVD, projections, pseudoinverses, norms, and decompositions give precise answers to those questions.

They become useful when we remember what kind of object they describe.

## References used in this chapter

- [@TrefethenBau1997]
- [@HornJohnson2012]
- [@GolubVanLoan2013]

See sources/source-locks/ATLAS-CH-LINALG-001.yaml for exact source roles and claim scope.
