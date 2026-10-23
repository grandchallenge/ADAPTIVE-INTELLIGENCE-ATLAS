# ATLAS #405: INFO corrected-edition substantive acceptance 8/80

Decision: **ACCEPT ATLAS-CH-INFO-001 for scoped editorial use.** The
canonical complete 80-row ledger now contains 8 ACCEPTED chapters and 72
UNVERIFIED. This is not a formal mathematical theorem certification,
blanket PDF/UA accessibility signoff or authorization to publish the
corrected edition. Published v0.1.0 and protected main remain untouched.

## Independent GCL producer and critic reviews

The authenticated GCL producer, issue [#438](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/438#issuecomment-6355836948),
role run a0438e5cf0f04b2fb2c3d0e91a814e89, examined source from
the exact original mutable workbench head:
4315a87b54d85562142002ef57c2d23676816c34 and corrected candidate
4ed74fa5dc871f7645b5825cd75319eb818ddc8e.

A distinctly role-assumed GCL critic [#439](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/439#issuecomment-6355868094),
run a0439e5cf0f04b2fb2c3d0e91a814e90, independently read the exact
corrected candidate, reviewed mathematical and epistemic claims,
checked the finite witness, source-lock authority, real PDF and HTML,
and revalidated the seven previously accepted chapters. Both roles
are accountable through the actual Editorial START/END controller,
using existing authenticated GitHub transport rather than requiring
distinct human accounts. The critic result was ACCEPT_EDITORIAL_SCOPE.

## Substantive mathematical findings

- Discrete entropy, cross-entropy, mutual information, and KL divergence
  now explicitly use consistent base-2 logarithms and *bits*. Numerical
  conversion from natural-log nats is division by ln 2. The prior
  mixed-base presentation was inconsistent.
- KL divergence's zero-probability conventions, finite support /
  absolute continuity and extended +infinity value are explicit.
  The same text distinguishes density from discrete probability mass
  and differential entropy from ordinary discrete entropy.
- The conditional expectation expression now requires integrability,
  and its tower identity E[E[X|Y]]=E[X] is not misidentified with
  causal intervention.
- Hoeffding's bound now states independent almost-surely bounded
  variables. For 100 independent Bernoulli outcomes, deviation of
  the sample mean by at least 0.2 is bounded by 2exp(-8)<0.001.
  This does not assert robustness under distribution shift.
- Statistical sufficiency is family-relative, and for iid Bernoulli
  observations the count sum(X_i) is sufficient. The natural
  log-odds parameter is finite only for 0<p<1; endpoint Bernoulli
  laws are limiting cases.
- Malformed mathematical displays in the standalone chapter
  specification were corrected and tied to the same log-unit
  conventions.

The original finite correlated-bit witness was independently checked;
I(X;Y)=0.1887218755408671 bits. The unchanged computational witness
has Git blob eab21989b9901adc2c6e1633ff97f59c5b121995. Original
three bibliographic references are source-locked as literature,
not falsely claimed to be pinned historical Git objects.

Canonical INFO source Git blob
4caaa28f0e5924f94d08d6ac95f2be6a824525d1;
specification 83cd53a540e2ff0eb1681cb8a2199554a2446141;
derivation ea4934bde67017418bdb47ed35b610c007602c96.

## Actual source/render provenance and predecessor preservation

Recomposed 80-chapter TeX SHA256
2f8ba8146a69c0dc931d4630d42867f8f8d21d46328c09f4ebf9da3d59744c7c.
Three-pass actual 1428-page PDF SHA256
bc9a599dc0850b4143d8c5b0b216e088cf50cd84af449c7c8a44ea57dac293b9.
MathJax full-book HTML SHA256
bd763fbfd04a2dfd6851549e650b00c4fc7bd41b3fc5b277c771db209f35d610.
INFO source chapter occupies physical pages 149-162; text and margin
scans passed on each page, with 96 MathJax math spans and 38 displays
and one unique correct HTML chapter anchor. Original 2971 LaTeX
labels and all 18 figures with semantic HTML alt descriptions remain.

The GCL critic separately revalidated six predecessor source families
and the seventh; complete unchanged previous accepted Git chapter
blobs are THESIS, MAP, OBJECTS, EVIDENCE, LINALG, NONNORMAL, KRYLOV.
Current native PDF page ranges 69-76, 77-82, 83-93, 95-107,
109-123, 125-136, 137-148 and HTML chapter anchors were checked.
The old source-role critical evidence and original PDF/HTML
digests stay preserved; current artifact revalidation is a separate
record linked to critic #439.

Six INFO arithmetic and theory-boundary tests, nine canonical
ledger tests, six historic MAP documentary regressions and complete
RC2 source recomposition pass locally. Protected native validation
and governed merge to editable PR #320 remain mandatory for this
record to become live acceptance.

Next genuine unaccepted chapter will be determined from the current
complete 80-row chapter ledger; do not manufacture missing IDs.
