# ATLAS #405: Probability, Information and Statistical Structure

Status: PRODUCED / DISTINCT CRITIC PENDING.
Original mutable corrected-edition workbench source head:
4315a87b54d85562142002ef57c2d23676816c34.
GCL producer issue #438, authenticated active editorial START run
a0438e5cf0f04b2fb2c3d0e91a814e89.

Actual complete chapter source, its formal chapter specification, the
supporting documentary derivation, the original finite joint-distribution
witness, and the three external bibliographic source locks were reviewed.

Substantive repairs:
- All finite discrete entropy, cross-entropy, KL and MI formulas
  explicitly use base-2 logarithms (bits); the conversion between bits
  and natural-log nats is explicit. The original mixed-base KL/cross-
  entropy notation was genuinely inconsistent.
- KL extended value at support mismatch and conditional zero-mass
  conventions are explicit; finite KL requires absolute continuity.
  Density versus probability mass and differential entropy are not
  silently conflated.
- Conditional expectation for discrete integrable X, and the tower
  identity E[E[X|Y]]=E[X], are provided with relevant integrability
  assumptions. They are not presented as interventions.
- Hoeffding's bound now states independence and almost-sure bounds;
  a concrete 100-Bernoulli, t=.2 sample-average example gives
  2 exp(-8)<.001 without claiming generalization or robustness.
- Sufficiency is family-relative via the conditional distribution
  independent of the parameter; iid Bernoulli sum is sufficient.
  The exponential family uses finite natural parameter only for
  0<p<1; endpoint Bernoulli distributions are limiting cases.
- Existing source specification's malformed display math was restored
  to typed base-2 KL, MI and exponential-family equations.

The preexisting exact correlated-bit joint distribution still yields
mutual information 0.1887218755408671 bits. The finite joint witness
source and three classical reference lock records remain unchanged.
These references are bibliographic source locks, not fabricated
commit-pinned source objects.

Exact Git source blobs:
Chapter 4caaa28f0e5924f94d08d6ac95f2be6a824525d1;
specification 83cd53a540e2ff0eb1681cb8a2199554a2446141;
documentary derivation ea4934bde67017418bdb47ed35b610c007602c96;
unchanged finite witness eab21989b9901adc2c6e1633ff97f59c5b121995.

Six stdlib-only independent tests cover correlated-bit mutual information;
cross-entropy/KL units and nats conversions; KL support mismatch and
conditional expectation tower; bounded independent Hoeffding;
iid Bernoulli likelihood/sufficiency; full TeX label/figure invariants,
math pairings and all three external bibliographic authorities.

Exact 80-chapter RC2 TeX SHA256
2f8ba8146a69c0dc931d4630d42867f8f8d21d46328c09f4ebf9da3d59744c7c.
Actual 1428-page three-pass PDF SHA256
bc9a599dc0850b4143d8c5b0b216e088cf50cd84af449c7c8a44ea57dac293b9.
Actual full-book MathJax HTML SHA256
bd763fbfd04a2dfd6851549e650b00c4fc7bd41b3fc5b277c771db209f35d610.
INFO physical pages 149–162; no marginal glyph collisions and selectable
text. Original 2971 LaTeX label targets and 18 source figures with
matching HTML alt descriptions remain intact.

Seven previous accepted sources are exactly unchanged; the native PDF and
HTML were rechecked at THESIS 69–76, MAP 77–82, OBJECTS 83–93,
EVIDENCE 95–107, LINALG 109–123, NONNORMAL 125–136, KRYLOV 137–148.
The new renderer signatures do not replace prior producer/critic
source and rendered evidence; separate current-render revalidation
must be recorded.

No admission, formal mathematical certification, PDF/UA signoff or public
corrected-edition release follows from a producer-only verdict.
