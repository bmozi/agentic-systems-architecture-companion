# Synthetic Context Record Template

**Packet:** AG-RV-PILOT-001 version 1.2.4
**Status:** Blank source template; not a completed run record
**Artifact identity:** `AG-SYNTHETIC-CONTEXT` / `v1`
**Exact run filename:** `AG-SYNTHETIC-CONTEXT-<ATTEMPT-ID>-v1.md`

Use this template only after the run chooses the synthetic entry branch. A
synthetic rehearsal has no human participant and cannot obtain or claim human
consent. Do not complete, copy, or deliver
`01-consent-and-privacy.md` in the same attempt.

## Required immutable run context

- Packet ID/version: `AG-RV-PILOT-001` / `1.2.4`
- Attempt ID:
- Required state literal: `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`
- Scenario boundary: `FICTIONAL SCENARIO ONLY`
- Human-evidence boundary: `No human consent, comprehension, usability, or practitioner result`
- Synthetic Stage A actor code:
- Synthetic Stage B reviewer code:
- Facilitator code:
- Orchestration status: `ORCHESTRATION-AIDED`
- Exact orchestration manifest filename and SHA-256:
  `ORCHESTRATION-INPUT-SHA256SUMS` /
- Evidence root:
- Retention boundary:
- Access boundary:
- Synthetic context start timestamp/timezone:
- Pre-scored execution-log checkpoint sequence and entry SHA-256:

The checkpoint must identify an already-recorded pre-scored event. It must not
predict the context-manifest verification, a future stage event, the final log
hash, or an external closeout timestamp.

## Manifest and delivery rule

Create and verify `STAGE-A-CONTEXT-SHA256SUMS` over this completed exact run
record before any Stage A scored file opens. Before Stage B starts, create and
verify `STAGE-B-CONTEXT-SHA256SUMS` over the same immutable record. Log both
verification events. The synthetic actor receives this manifest-bound record
instead of a completed human consent form.

If either context manifest includes a human-consent record, if the selected
branch changes between stages, or if this record claims any human result,
record a deviation and stop the attempt.
