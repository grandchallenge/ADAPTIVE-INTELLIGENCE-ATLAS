#!/usr/bin/env python3
from pathlib import Path
import sys, re, json, hashlib, subprocess, yaml

ROOT = Path(__file__).resolve().parents[1]
ledger = yaml.safe_load((ROOT/'governance/CHAPTER_LEDGER.yaml').read_text(encoding='utf-8'))
figs = yaml.safe_load((ROOT/'governance/FIGURE_REGISTER.yaml').read_text(encoding='utf-8'))
sources = yaml.safe_load((ROOT/'governance/SOURCE_REGISTER.yaml').read_text(encoding='utf-8'))
depgraph = yaml.safe_load((ROOT/'governance/DEPENDENCY_GRAPH.yaml').read_text(encoding='utf-8'))

errors = []
chapters = ledger.get('chapters', [])
ids = [c.get('id') for c in chapters]
known = set(ids)
if len(ids) != len(known):
    errors.append('duplicate chapter IDs')

# Hard dependency validity + acyclicity.
indegree = {cid: 0 for cid in known}
outgoing = {cid: [] for cid in known}
edge_count = 0
for c in chapters:
    for dep in c.get('dependencies') or []:
        edge_count += 1
        if dep not in known:
            errors.append(f"unresolved dependency {dep} from {c.get('id')}")
            continue
        indegree[c['id']] += 1
        outgoing[dep].append(c['id'])

queue = sorted([cid for cid, degree in indegree.items() if degree == 0])
visited = []
while queue:
    cid = queue.pop(0)
    visited.append(cid)
    for target in outgoing[cid]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
            queue.sort()
if len(visited) != len(known):
    errors.append('hard dependency graph contains a cycle')

audit = depgraph.get('audit', {})
if audit.get('node_count') != len(chapters):
    errors.append('dependency graph node_count disagrees with ledger')
if audit.get('hard_edge_count') != edge_count:
    errors.append('dependency graph hard_edge_count disagrees with ledger')
if bool(audit.get('acyclic')) != (len(visited) == len(known)):
    errors.append('dependency graph acyclic flag disagrees with computed graph')

for target, roles in (depgraph.get('hard_edge_roles') or {}).items():
    if target not in known:
        errors.append(f"dependency semantic target unknown: {target}")
        continue
    declared = set(next(c for c in chapters if c['id'] == target).get('dependencies') or [])
    for role in roles:
        src = role.get('source')
        if src not in declared:
            errors.append(f"semantic hard edge {src}->{target} not present in ledger")

for link in depgraph.get('soft_cross_links') or []:
    for cid in link.get('chapters') or []:
        if cid not in known:
            errors.append(f"soft cross-link references unknown chapter {cid}")

# Keystone specifications and manuscript promotion.
for c in chapters:
    if not c.get('keystone'):
        continue
    status = c.get('status')
    spec = c.get('spec_path')
    if status in ('specification-ready', 'draft-v0.1'):
        if not spec:
            errors.append(f"keystone {c['id']} missing spec_path")
        elif not (ROOT/spec).is_file():
            errors.append(f"keystone {c['id']} spec file missing: {spec}")
    if status == 'draft-v0.1':
        for field in ('manuscript_path','derivation_path','source_lock_path','computational_witness_path'):
            path = c.get(field)
            if not path:
                errors.append(f"draft keystone {c['id']} missing {field}")
            elif not (ROOT/path).is_file():
                errors.append(f"draft keystone {c['id']} missing file for {field}: {path}")

# Figure and source registries.
fig_ids = []
classes = set(figs.get('representation_classes') or [])
for f in figs.get('figures', []):
    fig_ids.append(f.get('id'))
    if f.get('chapter_id') not in known:
        errors.append(f"figure {f.get('id')} has unknown chapter")
    if f.get('representation_class') not in classes:
        errors.append(f"figure {f.get('id')} has invalid representation class")
    for req in ('literal_semantics','nonliteral_semantics','support_role','generator'):
        if req not in f:
            errors.append(f"figure {f.get('id')} missing {req}")
    gen = f.get('generator') or {}
    if f.get('status') == 'rendered-witness':
        for field in ('source','rendered','manifest','version','parameters'):
            value = gen.get(field)
            if not value:
                errors.append(f"rendered figure {f.get('id')} missing generator.{field}")
        for field in ('source','rendered','manifest'):
            value = gen.get(field)
            if value and not (ROOT/value).is_file():
                errors.append(f"rendered figure {f.get('id')} missing file: {value}")
if len(fig_ids) != len(set(fig_ids)):
    errors.append('duplicate figure IDs')

src_ids = [s.get('id') for s in sources.get('sources', [])]
if len(src_ids) != len(set(src_ids)):
    errors.append('duplicate source IDs')

# Reject hidden control characters in prose/math Markdown. Tabs are forbidden in
# Atlas-authored Markdown so an accidental JavaScript escape such as \\times -> TAB
# cannot silently corrupt TeX.
for root_name in ('manuscript','mathematics'):
    for md in (ROOT/root_name).rglob('*.md'):
        raw = md.read_text(encoding='utf-8')
        for i, ch in enumerate(raw):
            code = ord(ch)
            if ch == '\t' or (code < 32 and ch != '\n'):
                errors.append(f"control character U+{code:04X} in {md.relative_to(ROOT)} at offset {i}")
                break

# Executable deterministic replay witness.
replay_manifest_path = ROOT/'mathematics/computational-witnesses/replay_examples/deterministic_fraction_sum.manifest.json'
if replay_manifest_path.is_file():
    replay_manifest = json.loads(replay_manifest_path.read_text(encoding='utf-8'))
    replay_script = ROOT/replay_manifest['script_path']
    replay_expected = ROOT/replay_manifest['expected_output_path']
    if not replay_script.is_file():
        errors.append(f"replay script missing: {replay_script.relative_to(ROOT)}")
    if not replay_expected.is_file():
        errors.append(f"replay expected output missing: {replay_expected.relative_to(ROOT)}")
    if replay_script.is_file():
        script_digest = hashlib.sha256(replay_script.read_bytes()).hexdigest()
        if script_digest != replay_manifest.get('script_sha256'):
            errors.append('deterministic replay script SHA-256 mismatch')
    if replay_expected.is_file():
        expected_bytes = replay_expected.read_bytes()
        expected_digest = hashlib.sha256(expected_bytes).hexdigest()
        if expected_digest != replay_manifest.get('expected_output_sha256'):
            errors.append('deterministic replay expected-output SHA-256 mismatch')
        manifest_stdout = replay_manifest.get('expected_stdout')
        if manifest_stdout is not None and manifest_stdout.encode('utf-8') != expected_bytes:
            errors.append('deterministic replay expected_stdout disagrees with locked expected-output bytes')
    if replay_script.is_file() and replay_expected.is_file():
        proc = subprocess.run(
            [sys.executable, str(replay_script)],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode != 0:
            errors.append(f"deterministic replay exited {proc.returncode}: {proc.stderr.decode('utf-8', errors='replace')}")
        elif proc.stdout != replay_expected.read_bytes():
            errors.append('deterministic replay stdout differs from locked expected output')
else:
    errors.append('deterministic replay manifest missing')

# Manuscript citation closure against the canonical bibliography.
bib_text = (ROOT/'sources/bibliography.bib').read_text(encoding='utf-8')
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_text))
for md in (ROOT/'manuscript/parts').rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    # Citation keys may appear as [@Key] or after punctuation/whitespace, but
    # repository revisions such as repo@<commit> and email-like strings are not citations.
    for key in set(re.findall(r'(?<![A-Za-z0-9._/-])@([A-Za-z0-9:_-]+)', text)):
        if key not in bib_keys:
            errors.append(f"unresolved citation key {key} in {md.relative_to(ROOT)}")

if not (60 <= len(chapters) <= 80):
    errors.append(f"chapter count {len(chapters)} outside architecture target")

if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)

roots = [c['id'] for c in chapters if not c.get('dependencies')]
specified = sum(1 for c in chapters if c.get('status') == 'specification-ready')
drafts = sum(1 for c in chapters if c.get('status') == 'draft-v0.1')
rendered = sum(1 for f in figs.get('figures', []) if f.get('status') == 'rendered-witness')
print(
    f"OK: {len(chapters)} chapters, {edge_count} hard edges, "
    f"{len(roots)} root(s), {specified} specification-ready keystones, "
    f"{drafts} draft keystones, {rendered} rendered witnesses, "
    f"{len(fig_ids)} registered figures, {len(src_ids)} sources, {len(bib_keys)} bibliography keys"
)
