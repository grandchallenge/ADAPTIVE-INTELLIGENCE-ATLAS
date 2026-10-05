# Compression and Description Length
<!-- ATLAS-CH-COMPRESS-001 -->

**Epistemic status:** mathematical and engineering exposition built from audited Information and Representation prerequisites, classical compression sources, and Atlas-owned exact witnesses.  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-COMPRESS-001-DERIVATIONS.md\`  
**Computational witness:** \`mathematics/computational-witnesses/ATLAS-CW-COMPRESS-001.md\`  
**Source lock:** \`sources/source-locks/ATLAS-CH-COMPRESS-001.yaml\`

## 1. Compression begins with a code

"Smaller" can mean several different things.

A model can use:

- fewer scalar parameters;
- fewer nonzero parameters;
- fewer distinct parameter values;
- fewer bits per value;
- a lower-rank factorization;
- a shorter entropy-coded file;
- a smaller student network;
- a shorter formal description under a declared code.

These are not identical quantities.

The chapter therefore begins with a rule:

\[
\boxed{
\text{compression claim}
\Rightarrow
\text{declare the object, code, and tolerated distortion}.
}
\]

Without those declarations, a compression ratio can be numerically correct and scientifically ambiguous.

## 2. Description length is not parameter count

Minimum-description-length thinking treats model selection as a coding problem [@Rissanen1978MDL].

For a declared code \(C\), model \(M\), and data \(D\), a two-part objective has the form

\[
L_C(M,D)
=
L_C(M)
+
L_C(D\mid M).
\]

The first term describes the model.

The second describes the data given that model.

A shorter model can be worse if it leaves a much longer residual/data description.

A larger model can be justified if it dramatically shortens the unexplained data.

This is richer than "count the parameters."

## 3. A finite MDL witness

Suppose two hypotheses have declared model-code lengths

\[
L(H_A)=3,
\qquad
L(H_B)=7.
\]

Suppose they encode the observed data equally well:

\[
L(D\mid H_A)
=
L(D\mid H_B)
=
5.
\]

Then

\[
L(H_A,D)=8,
\]

while

\[
L(H_B,D)=12.
\]

Under this declared code, \(H_A\) wins.

Nothing in the arithmetic says that 3 bits and 7 bits are universally correct descriptions.

The point is that the code belongs inside the claim.

## 4. Lossless and lossy are different questions

Lossless compression preserves the coded object exactly.

Lossy compression preserves it only up to a declared distortion.

For learned systems, several distortions are possible:

- parameter error;
- operator error;
- output error;
- predictive loss;
- calibration change;
- retrieval degradation;
- latency or energy change.

Two compression methods can have the same storage ratio and very different task distortion.

So the meaningful object is not just

\[
\frac{\text{original size}}{\text{compressed size}}.
\]

It is the size–distortion pair.

## 5. Exact low-rank compression

Consider the \(4\times4\) all-ones matrix

\[
W
=
\mathbf 1_4\mathbf 1_4^\top.
\]

Its rank is one.

Let

\[
u=v=(1,1,1,1)^\top.
\]

Then

\[
W=uv^\top.
\]

The dense matrix and the factors implement exactly the same linear map:

\[
Wx=u(v^\top x)
\]

for every \(x\in\mathbb R^4\).

This is exact structural compression, not approximation.

## 6. Exact code-length comparison

Use a deliberately simple codec:

- the \(4\times4\) shape is known;
- entries are binary;
- one format bit distinguishes dense and rank-one representations.

Dense form:

- one format bit;
- sixteen matrix-entry bits.

Total:

\[
17\text{ bits}.
\]

Rank-one form:

- one format bit;
- four bits for \(u\);
- four bits for \(v\).

Total:

\[
9\text{ bits}.
\]

The same exact function has two different description lengths under the declared code.

That is the chapter's simplest exact compression witness.

## 7. Low rank can also be lossy

Now take

\[
A=\operatorname{diag}(4,3,1).
\]

Its singular values are

\[
4,\;3,\;1.
\]

By the classical low-rank approximation result [@EckartYoung1936], the best rank-one Frobenius approximation keeps only the largest singular value:

\[
A_1
=
\operatorname{diag}(4,0,0).
\]

The squared error is

\[
\|A-A_1\|_F^2
=
3^2+1^2
=
10.
\]

The best rank-two approximation is

\[
A_2
=
\operatorname{diag}(4,3,0),
\]

with squared error

\[
1.
\]

Low-rank representation is therefore not synonymous with exact compression.

It is exact only when discarded singular values are zero.

## 8. Pruning removes parameters

Pruning changes the support of the parameterization.

A simple magnitude-pruning rule removes weights whose absolute values fall below a threshold.

The appeal is obvious:

- fewer nonzero connections;
- potentially less storage;
- potentially less compute.

But magnitude is not the same thing as functional importance.

## 9. A small weight can still matter

Let

\[
w=
\begin{pmatrix}
1\\
1/8
\end{pmatrix}
\]

and

\[
x=
\begin{pmatrix}
0\\
8
\end{pmatrix}.
\]

Then

\[
w^\top x=1.
\]

Apply a pruning threshold

\[
\tau=1/4.
\]

The second weight disappears:

\[
w_{\rm pruned}
=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
\]

Now

\[
w_{\rm pruned}^\top x=0.
\]

The small parameter was decisive on this input.

So:

\[
\boxed{
\text{small magnitude}
\not\Rightarrow
\text{functional irrelevance}.
}
\]

Neural pruning methods can work well in practice, including as part of the Deep Compression pipeline [@HanMaoDally2016DeepCompression].

Their success is empirical and distribution-dependent.

## 10. Quantization changes precision

Quantization answers a different question.

The connections can remain present while each stored value uses fewer bits or is mapped to a smaller set of representable levels.

Take

\[
w=
(1/4,1/2,1/2,1/4).
\]

Use the fixed grid

\[
Q=
\{0,1/4,1/2,3/4\}.
\]

Every value of \(w\) lies exactly on the grid.

If raw values use 8 bits each, the payload is

\[
4\times8=32\text{ bits}.
\]

If fixed-grid indices use 2 bits each, the payload is

\[
4\times2=8\text{ bits}.
\]

Parameter distortion is zero in this witness.

The parameter count did not change.

The number of bits per parameter did.

## 11. Codebook overhead matters

The previous witness used a fixed grid known by the codec.

If the quantization levels are learned, the levels themselves must be stored.

That overhead belongs in the accounting.

This is one reason "4-bit model" and "4 bits per raw weight" are not necessarily the same storage claim.

Metadata, scales, zero points, codebooks, indices, alignment, and container formats can matter.

## 12. Weight sharing is different again

The same vector contains only two distinct values:

\[
1/4
\quad\text{and}\quad
1/2.
\]

Suppose a codec stores:

- two 8-bit centroids;
- four one-bit centroid indices.

The payload is

\[
16+4=20\text{ bits}.
\]

That is shorter than four independent 8-bit values:

\[
32\text{ bits}.
\]

All four connections remain.

Pruning removed a connection.

Weight sharing did not.

## 13. Deep Compression combines mechanisms

Han, Mao, and Dally combine pruning, trained quantization/weight sharing, and Huffman coding in one pipeline [@HanMaoDally2016DeepCompression].

Those stages attack different redundancies:

- pruning removes selected connections;
- quantization reduces the set of distinct values;
- weight sharing reuses centroids;
- entropy coding exploits frequency structure in the resulting symbols.

Calling the whole pipeline "compression" is correct.

Treating all its stages as the same mathematical operation is not.

## 14. Entropy coding acts on symbol statistics

After a representation has been chosen, symbols may occur with unequal frequencies.

A variable-length code can assign shorter codewords to more common symbols.

This connects compression back to the Information chapter.

Entropy coding does not decide which neural connections are important.

It compresses a symbol stream under a declared statistical model.

## 15. Low rank and sparsity are different structures

A matrix can be sparse and full rank.

A matrix can be dense and rank one.

These are different kinds of compressible structure.

Sparsity says many coordinates are zero.

Low rank says many rows or columns are dependent through a lower-dimensional factorization.

The hardware consequences, approximation errors, and implementation costs can differ.

## 16. Structured parameterizations

Low rank and weight sharing are examples of replacing an unconstrained parameter array with a smaller structured family.

For

\[
W\in\mathbb R^{m\times n},
\]

a dense matrix has

\[
mn
\]

scalar slots.

A rank-\(r\) factorization

\[
W=UV^\top
\]

with

\[
U\in\mathbb R^{m\times r},
\qquad
V\in\mathbb R^{n\times r}
\]

stores

\[
r(m+n)
\]

scalar slots before metadata.

When

\[
r(m+n)<mn,
\]

the factorized form uses fewer scalar slots.

That arithmetic alone does not prove lower wall-clock latency.

Kernel efficiency and memory traffic still matter.

## 17. Distillation compresses behavior, not bits

Knowledge distillation takes a different route [@HintonVinyalsDean2015Distillation].

A teacher or ensemble produces predictive targets.

A smaller student is trained to match those targets.

At temperature \(T\), one can form softened teacher probabilities

\[
p_T(i)
=
\frac{\exp(z_{T,i}/T)}
{\sum_j \exp(z_{T,j}/T)}
\]

and analogous student probabilities.

The student is optimized to reproduce teacher behavior under a declared loss.

Nothing requires the student parameters to be a bit-level encoding of the teacher parameters.

This is behavioral compression or transfer.

## 18. Exact equality on a finite dataset is not global equality

Suppose a student matches a teacher exactly on every example in a finite training set.

That proves equality on that set.

It does not prove

\[
f_{\rm student}(x)
=
f_{\rm teacher}(x)
\]

for every possible input.

The relevant domain must be declared.

This is the Representation chapter's equivalence discipline applied to compression.

## 19. Compression ratio is incomplete without retained behavior

A 100x smaller artifact can be excellent or useless.

The ratio alone does not say.

A serious report pairs size with something like:

- output error;
- predictive loss;
- accuracy;
- calibration;
- robustness;
- retrieval quality;
- task-specific utility.

Compression is a tradeoff surface, not a one-number race.

## 20. Parameter distortion can disagree with task distortion

A tiny parameter perturbation can have a large functional effect in one system.

A large parameter change can preserve function through reparameterization in another.

Therefore

\[
\|\theta-\hat\theta\|
\]

and task degradation are different measurements.

The right distortion depends on the object being preserved.

## 21. Compression and representation equivalence

Two encodings can represent the same function differently.

The rank-one witness makes this exact:

\[
W
\]

and

\[
uv^\top
\]

are different stored representations of the same linear operator.

This is why compression is naturally connected to representation theory.

We are looking for shorter encodings inside an equivalence class of acceptable behavior.

The equivalence relation must be stated.

## 22. MDL is not "smallest network wins"

MDL balances model description and residual/data description.

A model that is too small can fit poorly and require a longer data description.

A larger model can be justified if it compresses the data sufficiently.

The principle is not:

> always pick fewer parameters.

It is:

> under a declared coding framework, minimize the relevant total description.

## 23. Compression can reveal redundancy

If a model can be compressed with little change in declared behavior, then some part of its original description was redundant relative to that behavior and codec.

That is a useful scientific observation.

But redundancy can come from many sources:

- duplicate parameters;
- low-rank structure;
- unused features;
- overprecise numerical representation;
- repeated values;
- symmetries;
- overparameterization;
- training artifacts.

Compression alone does not tell us which mechanism caused the redundancy.

## 24. Compressibility is not interpretability

A highly compressible model can still be opaque.

A concise program can implement a difficult-to-understand computation.

A sparse network can still have distributed causal structure.

A low-rank map can still be semantically uninterpretable.

Therefore:

\[
\boxed{
\text{short description}
\not\Rightarrow
\text{human-understandable mechanism}.
}
\]

That stronger inference belongs downstream, where compression will be considered as a possible probe rather than a proof.

## 25. Compressibility is not intelligence

The same caution applies to intelligence.

Many simple objects compress extremely well.

Some useful computations require large descriptions under a given code.

A system's compressibility may provide evidence about reusable structure.

It is not a scalar definition of intelligence.

## 26. Failure modes

### 26.1 Parameter count equals description length

False.

Precision, codebook structure, sparsity, entropy coding, and metadata all matter.

### 26.2 Pruning equals quantization

False.

One changes support; the other changes value representation.

### 26.3 Quantization equals weight sharing

Not necessarily.

A fixed quantization grid and a learned shared codebook have different storage accounting.

### 26.4 Low rank equals sparsity

False.

These are different structural constraints.

### 26.5 Distillation equals source coding

False.

Distillation transfers predictive behavior under a training objective.

### 26.6 High compression ratio means good compression

Incomplete.

Retained behavior or distortion must also be reported.

### 26.7 Same outputs on one dataset means same function

False outside the declared dataset.

### 26.8 Compressible means interpretable

False without additional evidence.

### 26.9 Compressible means intelligent

False.

That claim requires an independent theory.

## 27. Downstream handoff

Compression as Discovery and Intelligence Probe may inherit:

- declared-code discipline;
- exact-versus-lossy distinction;
- mechanism separation among pruning, quantization, sharing, low rank, entropy coding, and distillation;
- the requirement to report compression jointly with retained behavior;
- the warning that compressibility is evidence of shorter representation under a declared equivalence, not proof of mechanism or intelligence.

The downstream chapter must independently justify any stronger claim about:

- reusable computation;
- mechanistic discovery;
- abstraction;
- intelligence;
- reconstruction from a compressed residual.

## References used in this chapter

- [@Rissanen1978MDL] — shortest-description model selection.
- [@EckartYoung1936] — optimal lower-rank matrix approximation.
- [@HanMaoDally2016DeepCompression] — pruning, trained quantization/weight sharing, and Huffman coding.
- [@HintonVinyalsDean2015Distillation] — teacher-student knowledge distillation.

Exact provenance and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-COMPRESS-001.yaml\`
