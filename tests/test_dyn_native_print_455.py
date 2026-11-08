"""Evidence-level checks for versioned DYN native print successor."""
import hashlib
import struct
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
P = "ATLAS-FIG-DYN-001-v0.1.1"
D = ROOT / "figures/derivatives"
M = yaml.safe_load((D / (P + ".yaml")).read_text())
SOURCE = (ROOT / M["source_path"]).read_text()
CHAPTER = (ROOT / "manuscript/parts/02-mathematical-substrate/ATLAS-CH-DYN-001.md").read_text()


class NativeDYNPrint(unittest.TestCase):
    def test_originals_and_versioned_source(self):
        for path, expected in (
            ("figures/wolfram/ATLAS-FIG-DYN-001.wl", M["original_wolfram_git_blob_sha1"]),
            ("figures/masters/ATLAS-FIG-DYN-001.png", M["original_master_git_blob_sha1"]),
            (M["source_path"], M["source_git_blob_sha1"]),
        ):
            sha = subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()
            self.assertEqual(sha, expected, path)

    def test_vector_panel_provenance(self):
        self.assertEqual(len(M["vector_panels"]), 3)
        for panel in M["vector_panels"]:
            raw = (ROOT / panel["path"]).read_bytes()
            self.assertTrue(raw.startswith(b"%PDF-"))
            self.assertEqual(hashlib.sha256(raw).hexdigest(), panel["sha256"])

    def test_rendered_shape_and_active_reference(self):
        raw = (ROOT / M["rendered_path"]).read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), M["rendered_sha256"])
        self.assertEqual(tuple(struct.unpack(">II", raw[16:24])), tuple(M["rendered_pixels"]))
        self.assertEqual(CHAPTER.count("../../" + M["rendered_path"]), 1)
        self.assertNotIn("../../figures/masters/ATLAS-FIG-DYN-001.png", CHAPTER)

    def test_exact_mathematical_semantics(self):
        for token in ("Exp[-2t]", "Sqrt[m]", "-Sqrt[m]",
                      "Circle[{0,0},1]", "AspectRatio->1", 'Text["H = 1/2"'):
            self.assertIn(token, SOURCE)
        self.assertIn("clockwise unit circle", CHAPTER)
        self.assertEqual(M["figure_id"], "ATLAS-FIG-DYN-001")


if __name__ == "__main__":
    unittest.main()
