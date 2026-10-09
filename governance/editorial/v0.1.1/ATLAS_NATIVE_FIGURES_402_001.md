# Atlas figure native-source publication repair — issue #402

**Disposition:** SOURCE-RENDERED PRINT CANDIDATES — not mathematical proof certification, 80-chapter editorial acceptance, or public release.

**Exact predecessor:** corrected-edition branch `editorial/part01-corrections-20261008` at `2fd807c13d25d1665c711b82004e07c520d21e64`, after INFO native source successor [PR #403](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/403) merged. **The original source files, 18 canonical figure IDs, original masters, previous derivatives, and public v0.1.0 are unchanged.**

## Versioned Wolfram assets

| Figure | Original source Git blob | Versioned source blob | New PNG Git blob | Raw PNG SHA256 | PNG pixel size |
|---|---|---|---|---|---|
| MANIFOLD | `16cfefd6fe09a01b425dd463a75ed08dd47379f1` | `42394b53e19f3813a8b5c25d2ba9d033f497eeca` | `f71d0da791b4661a929c17403d5c04c145783787` | `8da9d6018b90bce88d2975d9eacf8fd8ff5786616fc8795f45691415f52e5667` | 1267×1320 |
| TRANSFER | `793a444e8a466b5d7d913c2e477bf9acf1314d5c` | `30dedd507fc3effdeb297ae0e378d72a19c05fe7` | `3f44726bba28c3fda7b70c177b164793821846c7` | `950622228937473d448fbc11c5057828eb9f80a331c56244377eb99cd0d6fab9` | 1167×1267 |
| OPTBASE | `61123040326f80ec73a170778ba1140ef3f8fcb9` | `49f0249f29cd503b7b6db466206d81b028862be9` | `2e4f56f0c5b666c7f21807b94d984334bc087d3d` | `90bab967825cc406015680fcc44a06c17154b09ffe948787a261f9d13e32c087` | 1167×1650 |

Images are `figures/derivatives/ATLAS-FIG-{id}-001-v0.1.2.png` for MANIFOLD and TRANSFER, and `...OPTBASE-001-v0.1.3.png` for OPTBASE. Their `figures/manifests/*` siblings declare source identities, mathematical finite-witness boundaries and binary digests. All three were evaluated with **Wolfram 15.0.1 for Linux x86-64**, the exact generator version recorded in the original masters, then exported with `ImageResolution->120`.

The PNG transfer path retains PNG signature, IHDR, pHYs, IDAT and IEND while discarding nondeterministic EXIF/text *metadata*. IDAT (compressed image pixels) is preserved exactly; no bitmap interpolation. The assembled Base64 chunks were committed as true Git binary blobs and materialized as versioned repo files. The original MANIFOLD source has a literal `\n` outside a string and fails Wolfram `SyntaxQ`; the **successor** fixes that defect without rewriting the protected original source blob.

## Independent mathematical witness check

- **MANIFOLD:** (x=(0,0,1)), (v=(4/5,0,0)), sphere exponential endpoint approximately ((0.71735609,0,0.69670671)), normalized retraction endpoint approximately ((0.62469505,0,0.78086881)). Euclidean endpoint difference approximately (0.1251771866). Label emphasis and perspective are schematic; neither endpoint is claimed to be an arbitrary learned manifold update.
- **TRANSFER:** source map sends (r=(3,1)) to ((4,2)); target map sends it to ((6,1/2)), both invertible. Task outputs are exactly (4,5). A one-dimensional bottleneck merges (r_A=(1,0)) and (r_B=(1,1)) but their second task outputs differ (2) versus (1). Layout changed from side-by-side to stacked panels for print; this is not an empirical transfer claim.
- **OPTBASE:** scalar amplification (|1-a|) contracts iff (0<a<2); clipping ((3,4)) at global norm threshold 2 yields ((6/5,8/5)); coupled and decoupled toy update values (183/100) and (181/100) differ by (1/50). Stacked panels separate annotations. None of this ranks optimizers or proves nonconvex convergence.

All exact computations were independently evaluated in the Wolfram kernel; this verifies the cited finite data only, not every graphical placement or published textbook claim.

## Admission gates

The bounded fresh [PR #404](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/404) must pass raw SHA256/pixel-size checks; canonical 80-chapter deterministic generated TeX including historical 2,971 labels and 18 stable figures; three-pass full PDF; at least 200 effective DPI per newly printed plate; HTML alt semantics, anchors and figure identities; exact-head native CI; distinct critical-role review; and candidate/merged manuscript TeX blob comparison.

**Explicitly not certified:** mathematical truth of all plotted diagrams, caption symbol fidelity in screen readers, PDF/UA tagged content, 80 final independent chapter signoffs, or public edition promotion.
