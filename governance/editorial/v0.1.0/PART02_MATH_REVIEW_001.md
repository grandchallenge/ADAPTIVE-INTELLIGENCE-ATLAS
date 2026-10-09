# Part II mathematical-substrate editorial correction 001

Parent #314; chapter queue #326; candidate PR #320; immutable release baseline atlas-v0.1.0.

**Scope:** ATLAS-CH-NONNORMAL-001, section 4 (The smallest useful counterexample), with a linked section 5 notation clarification.

**Finding:** original display states A^n=a^n I + n a^(n-1) K N without quantifying n, while the chapter permits a=0. At n=0 the power law needs a separate A^0=I, and the n=1 scalar term a^0 invokes a convention in the zero-eigenvalue edge case. The previous formula could be read as an unqualified equality for all n.

**Correction proposed in the Markdown provenance and corrected-edition LaTeX only:** explicitly state the nilpotent binomial formula and corresponding B=A^n singular-value substitution for integers n>=2, separately state A^0=I and A^1=A. The nilpotent identity N^2=0 implies the displayed n>=2 formula by binomial truncation. No change to the 4/5, K=4 transient gain witness, spectrum, pseudospectrum, or claims of general stability.

**Check:** exact symbolic expansion of n=2 and n=3 against upper-triangular matrix formula gives zero matrices in Wolfram; at a=0 the square vanishes. Independent agent mathematical/editorial judgment is still requested in #326. This is a narrower theorem statement, not a stronger claim.

**Production:** 80-chapter candidate regression permits this one specifically whitelisted mathematical prose change in addition to heading normalization and the OPTBASE figure derivative. Local PDF three-pass and HTML rebuild succeeded on the changed working tree, subject to exact-head CI after commit.

**Disposition:** REVISION_CANDIDATE; not AGENT_REVIEWED, not accepted, not certified. Published atlas-v0.1.0 remains byte-identical to its audited tag.
