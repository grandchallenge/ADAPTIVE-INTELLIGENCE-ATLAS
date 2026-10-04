from gsd.checkpoints import normalize_refs, parse_checkpoint_revision


def test_parse_revision():
    ref = parse_checkpoint_revision("stage1-step20000-tokens42B")
    assert ref is not None
    assert ref.step == 20000
    assert ref.tokens_b == 42.0


def test_normalize_and_sort_refs():
    refs = normalize_refs([
        "main",
        "stage1-step20000-tokens42B",
        "stage1-step0-tokens0B",
        "stage1-step10000-tokens21B",
    ])
    assert [r.step for r in refs] == [0, 10000, 20000]
