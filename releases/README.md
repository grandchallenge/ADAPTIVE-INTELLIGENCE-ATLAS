# Releases

This directory is reserved for governed release artifacts.

Repository licensing has been selected:

- CC BY 4.0 for publication/documentation/figure material;
- MIT for software/tooling;
- file-specific and third-party rights take precedence.

License selection alone does not authorize a public release.

Release promotion requires, at minimum:

1. exact protected release commit/tag;
2. version/date citation metadata bound to that tag;
3. selected release format(s);
4. rendering-aware copy-edit and rendered-format validation;
5. exact artifact hashes and release manifest;
6. release-candidate audit;
7. explicit public-release authorization recorded in governance state.

The repository validator rejects substantive files in this directory unless `governance/RELEASE_AUTHORIZATION.yaml` exists with `public_release_authorized: true`.

The existence of a build artifact, selected license, or green repository validation run does not by itself confer publication-ready, final-copy, certified, or released status.
