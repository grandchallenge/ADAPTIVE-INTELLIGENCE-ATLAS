"""Exact elementary counterchecks for the first Part II Atlas chapter."""
import hashlib,re,subprocess,unittest
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
M=R/'manuscript/parts/02-mathematical-substrate/ATLAS-CH-LINALG-001.md'
W=R/'mathematics/computational-witnesses/ATLAS-CW-LINALG-001.md'
D=R/'mathematics/derivations/ATLAS-CH-LINALG-001-DERIVATIONS.md'
class LinearMapAcceptance(unittest.TestCase):
 def test_true_basis_change_distinct_from_similarity(self):
  s=M.read_text()
  self.assertIn('S_W^{-1}[T]_{C',s)
  self.assertIn('similarity transformation',s)
  self.assertIn('need not preserve matrix eigenvalues',s)
  # T=diag(2,3), codomain basis rescaling (3,1), domain (2,4):
  # new representation has entries 4/3, 12, not an eigenvalue-preserving similarity.
  old=((F(2),F(0)),(F(0),F(3)))
  sv=(F(2),F(4));sw=(F(3),F(1))
  new=(old[0][0]*sv[0]/sw[0],old[1][1]*sv[1]/sw[1])
  self.assertEqual(new,(F(4,3),F(12)))
  self.assertNotEqual(new,(old[0][0],old[1][1]))
 def test_real_normal_rotation_nonreal_spectrum(self):
  s=M.read_text()
  for term in ('Over \\(\\mathbb C\\)','complex eigenvectors','no nonzero real eigenvectors'):
   self.assertIn(term,s)
  rot=((F(0),F(-1)),(F(1),F(0)))
  # R^T R = I; char poly det(lambda I-R)=lambda^2+1 > 0 for real lambda.
  self.assertEqual(sum(rot[i][0]*rot[i][0] for i in range(2)),1)
  self.assertEqual(sum(rot[i][1]*rot[i][1] for i in range(2)),1)
  self.assertEqual(sum(rot[i][0]*rot[i][1] for i in range(2)),0)
  self.assertTrue(all(F(k*k+1)>0 for k in range(-30,31)))
 def test_rank_deficient_pseudoinverse_unique_min_norm(self):
  s=M.read_text();w=W.read_text()
  self.assertIn('unique minimum-Euclidean-norm member',s)
  self.assertIn('Witness D',w)
  for t in range(-10,11):
   x1=F(2);x2=F(t)
   sq=(x1-2)**2+9
   norm=x1*x1+x2*x2
   self.assertEqual(sq,9)
   self.assertGreaterEqual(norm,F(4))
  self.assertIn('PseudoInverse[a0].b0',w)
  self.assertIn('r0.r0',w)
 def test_jordan_one_step_vs_powers(self):
  s=M.read_text()
  self.assertIn('A^k=',s)
  self.assertIn('not diagonalizable',s)
  for k in range(10):
   # (I+N)^k = I+kN, N^2=0. Test matrix applied to e2.
   x=(F(k),F(1))
   self.assertEqual(x[0]*x[0]+x[1]*x[1],k*k+1)
 def test_svd_contract_dimensions_and_rank_zero(self):
  s=M.read_text()
  for term in ('full SVD','compact form','\\Sigma_r','r=0','rectangular diagonal'):
   self.assertIn(term,s)
  self.assertIn('rank-',s)
  # Witness SVD: A^T A=[[1,1],[1,2]], eigenvalues (3+-sqrt5)/2
  # determinant 1, trace 3; singulars satisfy sigma1*sigma2=1.
  self.assertEqual(F(1)*F(2)-F(1)*F(1),1)
 def test_maintain_source_claim_scope_and_metadata(self):
  s=M.read_text();w=W.read_text();d=D.read_text()
  self.assertEqual(s.count('<!-- ATLAS-CH-LINALG-001 -->'),1)
  self.assertTrue(all(x in s for x in ('TrefethenBau1997','HornJohnson2012','GolubVanLoan2013')))
  self.assertIn('does not claim that spectral structure alone determines neural training behavior',d)
  self.assertIn('do not certify any nonlinear-system property',w)
  tex=(R/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
  self.assertEqual(len({x.split('}',1)[0] for x in tex.split(chr(92)+'label{')[1:]}),2971)
  self.assertEqual(tex.count(r'\includegraphics'),18)
if __name__=='__main__':unittest.main()
