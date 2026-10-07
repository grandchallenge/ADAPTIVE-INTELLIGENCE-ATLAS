#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, yaml

ROOT=Path(__file__).resolve().parents[1]
VERSION='0.1.0'
TAG='atlas-v0.1.0'
RC_VERSION='0.1.0-rc.1'
RELEASE=ROOT/'releases'/f'v{VERSION}'
AUTH=ROOT/'governance/RELEASE_AUTHORIZATION.yaml'
MANIFEST=RELEASE/'release-manifest.json'
errors=[]

EXPECTED={
  'latex':'0d636871e6875bbadbd244e54bf272fdefe2dbd5179515d9d22d3a25e49c384a',
  'pdf':'efd0f21088ced19e5cc706069cc57cd4d0fa57ffc402c63767d8ad4939d96b96',
  'html':'795700db6ac8cd689d8dcfad7d116734015f7a196e3fd3fce2608eb5cac7daa4',
}

def sha256(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

if not AUTH.is_file():
    errors.append('governance/RELEASE_AUTHORIZATION.yaml missing')
    auth={}
else:
    auth=yaml.safe_load(AUTH.read_text(encoding='utf-8')) or {}
    if auth.get('public_release_authorized') is not True: errors.append('public_release_authorized must be true')
    if auth.get('final_version')!=VERSION: errors.append('authorized final_version mismatch')
    if auth.get('final_tag')!=TAG: errors.append('authorized final_tag mismatch')
    src=auth.get('source_candidate') or {}
    if src.get('tag')!='atlas-v0.1.0-rc.1': errors.append('authorized source candidate tag mismatch')
    if src.get('implementation_merge')!='e6a97fe9cf2ef4577f046c95f74f5eb690ba2e0e': errors.append('authorized candidate implementation mismatch')
    if src.get('audit_merge')!='498e4c2f517255883f83bf8e23afba8841e5c9dc': errors.append('authorized candidate audit mismatch')
    if auth.get('required_sha256')!=EXPECTED: errors.append('authorization SHA-256 set mismatch')

paths={
 'canonical':ROOT/'manuscript/latex'/f'atlas-v{VERSION}.tex',
 'latex':RELEASE/f'atlas-v{VERSION}.tex',
 'pdf':RELEASE/f'atlas-v{VERSION}.pdf',
 'html':RELEASE/f'atlas-v{VERSION}.html',
}
rc_paths={
 'latex':ROOT/'manuscript/latex'/f'atlas-v{RC_VERSION}.tex',
 'pdf':ROOT/'build/release-candidate'/f'v{RC_VERSION}'/f'atlas-v{RC_VERSION}.pdf',
 'html':ROOT/'build/release-candidate'/f'v{RC_VERSION}'/f'atlas-v{RC_VERSION}.html',
}
for k,p in paths.items():
    if not p.is_file(): errors.append(f'missing {k} release artifact: {p}')
for k,p in rc_paths.items():
    if not p.is_file(): errors.append(f'missing audited candidate {k}: {p}')

for k in ('latex','pdf','html'):
    p=paths[k]
    rp=rc_paths[k]
    if p.is_file():
        actual=sha256(p)
        if actual!=EXPECTED[k]: errors.append(f'{k} final SHA-256 mismatch: {actual}')
    if rp.is_file():
        actual=sha256(rp)
        if actual!=EXPECTED[k]: errors.append(f'{k} candidate SHA-256 drift: {actual}')
    if p.is_file() and rp.is_file() and p.read_bytes()!=rp.read_bytes():
        errors.append(f'{k} final artifact is not byte-identical to audited candidate')
if paths['canonical'].is_file():
    if sha256(paths['canonical'])!=EXPECTED['latex']: errors.append('final canonical LaTeX SHA-256 mismatch')
    if paths['latex'].is_file() and paths['canonical'].read_bytes()!=paths['latex'].read_bytes(): errors.append('release LaTeX differs from final canonical LaTeX')

if not MANIFEST.is_file():
    errors.append('final release manifest missing')
else:
    m=json.loads(MANIFEST.read_text(encoding='utf-8'))
    if m.get('artifact_class')!='public-release': errors.append('final manifest artifact_class mismatch')
    if m.get('public_release_authorized') is not True: errors.append('final manifest must record authorization')
    if m.get('version')!=VERSION: errors.append('final manifest version mismatch')
    if m.get('release_date')!='2026-10-07': errors.append('final manifest date mismatch')
    if m.get('release_tag')!=TAG: errors.append('final manifest tag mismatch')
    if m.get('promotion')!='byte-preserving': errors.append('final manifest promotion must be byte-preserving')
    if m.get('sha256')!=EXPECTED: errors.append('final manifest SHA-256 set mismatch')
    if m.get('chapter_count')!=80: errors.append('final manifest chapter_count mismatch')
    if m.get('figure_count')!=18: errors.append('final manifest figure_count mismatch')
    if m.get('html_alt_attributes')!=18: errors.append('final manifest HTML alt count mismatch')
    if len(m.get('assembly_chapters',[]))!=80: errors.append('final manifest must preserve all 80 input chapter identities')

if paths['canonical'].is_file():
    tex=paths['canonical'].read_text(encoding='utf-8')
    if sum(1 for x in tex.splitlines() if x.startswith(r'\chapter'))!=80: errors.append('final LaTeX must contain exactly 80 chapters')
    if tex.count(r'\includegraphics')!=18: errors.append('final LaTeX must contain exactly 18 figures')
    if 'Interlude: From Readability to Functional' not in tex: errors.append('MECHDIAG interlude title missing')
if paths['html'].is_file():
    h=paths['html'].read_text(encoding='utf-8',errors='replace')
    imgs=re.findall(r'<img\b[^>]*>',h)
    if len(imgs)!=18: errors.append(f'final HTML image count {len(imgs)} != 18')
    if sum(1 for x in imgs if re.search(r'\balt=',x))!=18: errors.append('final HTML must provide alt text for all 18 figures')
if paths['pdf'].is_file() and not paths['pdf'].read_bytes().startswith(b'%PDF-'): errors.append('final PDF signature missing')

citation=yaml.safe_load((ROOT/'CITATION.cff').read_text(encoding='utf-8'))
if citation.get('version')!=VERSION: errors.append('CITATION.cff version not final')
if str(citation.get('date-released'))!='2026-10-07': errors.append('CITATION.cff final date mismatch')

checks=RELEASE/'SHA256SUMS.txt'
if not checks.is_file(): errors.append('SHA256SUMS.txt missing')
else:
    expected_text=''.join(EXPECTED[k]+'  '+paths[k].name+'\n' for k in ('latex','pdf','html'))
    if checks.read_text(encoding='utf-8')!=expected_text: errors.append('SHA256SUMS.txt mismatch')
if not (RELEASE/'RELEASE_NOTES.md').is_file(): errors.append('RELEASE_NOTES.md missing')

allowed={
 'releases/.gitkeep','releases/README.md',
 f'releases/v{VERSION}/atlas-v{VERSION}.tex',
 f'releases/v{VERSION}/atlas-v{VERSION}.pdf',
 f'releases/v{VERSION}/atlas-v{VERSION}.html',
 f'releases/v{VERSION}/release-manifest.json',
 f'releases/v{VERSION}/SHA256SUMS.txt',
 f'releases/v{VERSION}/RELEASE_NOTES.md',
}
actual={str(p.relative_to(ROOT)).replace('\\','/') for p in (ROOT/'releases').rglob('*') if p.is_file()}
unexpected=sorted(actual-allowed)
missing=sorted(allowed-actual)
if unexpected: errors.append('unexpected release files: '+', '.join(unexpected))
if missing: errors.append('missing governed release files: '+', '.join(missing))

if errors:
    for e in errors: print('ERROR:',e)
    raise SystemExit(1)
print('OK: authorized public release v0.1.0 staged; exact audited bytes preserved; 80 chapters; 18 figures; 18 HTML alt attributes; hashes/citation/authorization verified')
