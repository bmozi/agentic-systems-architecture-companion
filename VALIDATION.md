# Validation

Run:

```bash
python3 scripts/validate_repository.py
python3 scripts/test_temporal_freeze_protocol.py
```

The validator checks the manifest, required reader entry points, local Markdown
links, gateway first-pass language, comprehensive-example paths, and declared
pilot-packet SHA-256 values. It also validates the version 1.2.2 canonical
temporal inventory: six output freezes, five next-release triples, exact
complete-manifest-verify-record ordering, manifest membership and exclusions,
completion states, correction requirements, artifact identity/version/filename
bindings, protected protocol documents, and the six-row results inventory.
The mutation suite refreshes ordinary packet checksums and confirms that a
positive control passes while eleven structural regressions are rejected. A
checksum pass shows that the prepared source
packet has not drifted from its manifest. It is a repository-integrity check
only. It does not establish practitioner usability, technical correctness,
security, accessibility, legal sufficiency, production fitness, or book-
edition compatibility.
