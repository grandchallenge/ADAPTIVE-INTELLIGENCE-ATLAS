"""Physical PDF placement audit for the non-Wolfram NUMERICS fallback.

Usage: python3 tests/audit_atlas_numerics_459_print.py PDF
Requires pypdf and Pillow. Verifies geometry, raster identity, and resolution;
it is not a substitute for visual inspection or Wolfram-native certification.
"""
import hashlib
import re
import sys
from pathlib import Path
from PIL import Image
from pypdf import PdfReader

EXPECTED_SHA256 = "05b652b7d865f4780325c1c0c6fc2e67b1389bec28c4ac91e6105605e4193062"
PAGE = 208


def main(pdf):
    pdf = Path(pdf)
    page = PdfReader(str(pdf)).pages[PAGE - 1]
    assert len(page.images) == 1, "expected exactly one image on NUMERICS page"
    image = page.images[0]
    with Image.open(__import__("io").BytesIO(image.data)) as im:
        assert im.size == (1740, 2280), im.size
    # PDF embeds a decoded/re-encoded raster: compare source pixels, not
    # necessarily the PNG file's compressed-byte SHA.
    contents = page.get_contents().get_data().decode("latin-1")
    pat = r"([0-9.]+) 0 0 ([0-9.]+) 0 0 cm\s*/" + re.escape(image.name.split(".")[0]) + r" Do"
    m = re.search(pat, contents)
    assert m, "image transform not found"
    # The immediate image transform is nested inside a uniform scale.
    scales = re.findall(r"([0-9.]+) 0 0 \1 0 0 cm", contents)
    assert scales, "outer image scale not found"
    scale = float(scales[-1])
    width_pt, height_pt = float(m[1])*scale, float(m[2])*scale
    width_in, height_in = width_pt/72, height_pt/72
    dpi_x, dpi_y = 1740/width_in, 2280/height_in
    assert 4.5 < width_in < 5.2, width_in
    assert height_in < 7, height_in
    assert min(dpi_x, dpi_y) >= 300, (dpi_x, dpi_y)
    source = Path("figures/derivatives/ATLAS-FIG-NUMERICS-001-fallback-v0.1.2.png")
    assert hashlib.sha256(source.read_bytes()).hexdigest() == EXPECTED_SHA256
    with Image.open(source) as im:
        with Image.open(__import__("io").BytesIO(image.data)) as embedded:
            assert im.convert("RGB").tobytes() == embedded.convert("RGB").tobytes(), "PDF image pixels differ from source"
    print(f"PRINT_PLACEMENT_PASS page={PAGE} width_in={width_in:.3f} height_in={height_in:.3f} dpi={min(dpi_x,dpi_y):.1f} source_sha256={EXPECTED_SHA256}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 tests/audit_atlas_numerics_459_print.py PDF")
    main(sys.argv[1])
