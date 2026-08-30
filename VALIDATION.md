# Validation

Run:

```bash
python3 scripts/validate_repository.py
```

The validator checks the manifest, required reader entry points, local Markdown
links, gateway first-pass language, comprehensive-example paths, and declared
pilot-packet SHA-256 values. A checksum pass shows that the prepared source
packet has not drifted from its manifest. It is a repository-integrity check
only. It does not establish practitioner usability, technical correctness,
security, accessibility, legal sufficiency, production fitness, or book-
edition compatibility.
