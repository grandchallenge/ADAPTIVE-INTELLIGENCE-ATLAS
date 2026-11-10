"""Reproducible non-Wolfram fallback render of ATLAS NUMERICS #459.

This is explicitly NOT a Wolfram-native master. Keep the .wl source and
its native-rendering acceptance obligation open. Run on CHAD with:
  python3 figures/scripts/render_atlas_numerics_459.py OUTPUT.png
"""
import hashlib
import json
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm


def main(output):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    A = np.array([[0., 1.], [0., 0.]])
    B = np.array([[0., 0.], [1., 0.]])
    assert np.array_equal(A @ B - B @ A, np.diag([1., -1.]))
    hs = 10. ** np.arange(-3., -.25 + 1e-10, .2)
    assert len(hs) == 14 and abs(np.log10(hs[-1]) + .4) < 1e-10
    lie, strang = [], []
    for h in hs:
        exact = expm(h * (A + B))
        lie.append(np.linalg.norm(expm(h*A) @ expm(h*B) - exact, "fro"))
        strang.append(np.linalg.norm(expm(h*A/2) @ expm(h*B) @ expm(h*A/2) - exact, "fro"))
    assert abs(np.polyfit(np.log(hs[:5]), np.log(lie[:5]), 1)[0] - 2) < .02
    assert abs(np.polyfit(np.log(hs[:5]), np.log(strang[:5]), 1)[0] - 3) < .02

    plt.rcParams.update({"font.size": 13, "axes.titlesize": 16, "axes.labelsize": 14})
    fig, axes = plt.subplots(3, 1, figsize=(11.6, 15.2), constrained_layout=True)
    xx, yy = np.meshgrid(np.linspace(-4, 2, 700), np.linspace(-3, 3, 700))
    for ax in axes[:2]:
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(-4, 2)
        ax.set_ylim(-3, 3)
        ax.axhline(0, color=".35", linewidth=.8)
        ax.axvline(0, color=".35", linewidth=.8)
        ax.set_xlabel("Re(z)")
        ax.set_ylabel("Im(z)")
        ax.grid(alpha=.15)
    axes[0].contourf(xx, yy, (xx+1)**2+yy**2, levels=[0, 1], colors=[".83"])
    axes[0].contour(xx, yy, (xx+1)**2+yy**2, levels=[1], colors="black")
    axes[0].set_title("Explicit Euler: strict decay |1+z| < 1")
    axes[0].text(-1, .4, "strict decay", ha="center")
    axes[1].contourf(xx, yy, (xx-1)**2+yy**2, levels=[1, 1e4], colors=[".83"])
    axes[1].contour(xx, yy, (xx-1)**2+yy**2, levels=[1], colors="black")
    axes[1].set_title("Implicit Euler: strict decay |1-z| > 1")
    axes[1].text(-2.1, 2.25, "left half-plane included", ha="center", fontsize=11)
    axes[2].loglog(hs, lie, "ko-", label="Lie-Trotter", linewidth=2, markersize=4)
    axes[2].loglog(hs, strang, "k--s", label="Strang", linewidth=2, markersize=4, alpha=.65)
    axes[2].set_xlabel("h")
    axes[2].set_ylabel("Frobenius local defect")
    axes[2].set_title("Split one-step local defect (small-h slopes 2 and 3)")
    axes[2].grid(alpha=.2, which="both")
    axes[2].legend(loc="lower right")
    axes[2].text(.25, .50, "slope ~ 2", transform=axes[2].transAxes)
    axes[2].text(.5, .22, "slope ~ 3", transform=axes[2].transAxes)
    fig.savefig(output, dpi=150, facecolor="white")
    plt.close(fig)
    from PIL import Image
    with Image.open(output) as im:
        width, height = im.size
        assert width >= 1600 and height >= 2000
    manifest = {
        "record_type": "ATLAS_NUMERICS_FALLBACK_RENDER/1",
        "status": "NON_WOLFRAM_FALLBACK_NOT_NATIVE_CERTIFICATION",
        "source": "figures/scripts/render_atlas_numerics_459.py",
        "output": output.name,
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "width": width, "height": height,
        "hs_count": len(hs),
        "lie_small_h_slope": float(np.polyfit(np.log(hs[:5]), np.log(lie[:5]), 1)[0]),
        "strang_small_h_slope": float(np.polyfit(np.log(hs[:5]), np.log(strang[:5]), 1)[0]),
    }
    output.with_suffix(".json").write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n")
    print(json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 render_atlas_numerics_459.py OUTPUT.png")
    main(sys.argv[1])
