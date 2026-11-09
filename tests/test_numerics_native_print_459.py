"""Exact-source and binary-provenance guard for NUMERICS Figure #459."""
import hashlib
import struct
import subprocess
import unittest
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]
F='ATLAS-FIG-NUMERICS-001-v0.1.1'
D=R/'figures/derivatives'
M=yaml.safe_load((D/(F+'.yaml')).read_text())
S=(R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-NUMERICS-001.md').read_text()
W=(R/M['source_path']).read_text()
class NumericsNative(unittest.TestCase):
 def test_original_sources_immutable(self):
  for path,sha in [(R/'figures/wolfram/ATLAS-FIG-NUMERICS-001.wl',M['original_wolfram_sha1']),(R/'figures/masters/ATLAS-FIG-NUMERICS-001.png',M['original_master_sha1']),(R/M['source_path'],M['source_git_blob_sha1'])]:
   self.assertEqual(subprocess.check_output(['git','hash-object',str(path)],text=True).strip(),sha)
 def test_native_vectors(self):
  self.assertEqual(len(M['vector_panels']),3)
  for panel in M['vector_panels']:
   raw=(R/panel['path']).read_bytes()
   self.assertTrue(raw.startswith(b'%PDF-'))
   self.assertEqual(hashlib.sha256(raw).hexdigest(),panel['sha256'])
 def test_raster_and_active_chapter(self):
  raw=(R/M['rendered_path']).read_bytes()
  self.assertEqual(hashlib.sha256(raw).hexdigest(),M['rendered_sha256'])
  self.assertEqual(tuple(struct.unpack('>II',raw[16:24])),tuple(M['rendered_pixels']))
  self.assertEqual(S.count('../../'+M['rendered_path']),1)
  self.assertNotIn('../../figures/masters/ATLAS-FIG-NUMERICS-001.png',S)
 def test_mathematical_semantics(self):
  for literal in ('Disk[{-1,0},1]','Disk[{1,0},1]','MatrixExp[h A].MatrixExp[h B]','"Frobenius"','AspectRatio->.6'):
   self.assertIn(literal,W)
  self.assertIn('third (lower, full-width) panel',S)
  self.assertTrue((-1+1)**2+0**2<1)
  self.assertFalse((1-1)**2+0**2>1)
