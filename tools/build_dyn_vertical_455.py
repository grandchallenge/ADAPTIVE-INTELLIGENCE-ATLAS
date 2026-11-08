#!/usr/bin/env python3
"""Source-native ATLAS-FIG-DYN-001 v0.1.1 panel compositor.

The three vector-PDF inputs were exported from versioned Wolfram Language
source. Ghostscript renders each vector PDF at 240 DPI; Pillow only places
and uniformly scales panels, never redraws mathematical curves or text.
"""
import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "figures/derivatives"
PREFIX = "ATLAS-FIG-DYN-001-v0.1.1"


def build(output: Path):
    with tempfile.TemporaryDirectory(prefix="atlas-dyn455-") as d:
        raster = []
        for i in (1, 2, 3):
            src = DER / f"{PREFIX}-panel-{i}.pdf"
            dest = Path(d) / f"panel-{i}.png"
            subprocess.run(
                ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=png16m",
                 "-r240", f"-sOutputFile={dest}", str(src)],
                check=True,
            )
            raster.append(Image.open(dest).convert("RGB"))
        # Reduce only the oscillator panel uniformly; a circular orbit remains circular.
        raster[2] = raster[2].resize(
            (850, round(raster[2].height * 850 / raster[2].width)),
            Image.Resampling.LANCZOS,
        )
        width = raster[0].width
        assert raster[1].width == width
        gap = 26
        height = sum(im.height for im in raster) + 2 * gap
        canvas = Image.new("RGB", (width, height), "white")
        y = 0
        for im in raster:
            canvas.paste(im, ((width - im.width) // 2, y))
            y += im.height + gap
        output.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(output, optimize=True, dpi=(250, 250))
        return canvas.size


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = DER / f"{PREFIX}.png"
    if args.check:
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            candidate = Path(d) / output.name
            dimensions = build(candidate)
            assert output.read_bytes() == candidate.read_bytes(), "DYN source-native print image stale"
    else:
        dimensions = build(output)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"DYN_VERTICAL_455_PASS dims={dimensions} sha256={digest} check={args.check}")


if __name__ == "__main__":
    main()
