# External Run Closeout Record Template

**Packet:** AG-RV-PILOT-001 version 1.2.5
**Status:** Facilitator-only blank post-log record; prepared and unrun
**Artifact identity:** `AG-RUN-CLOSEOUT` / `v1`
**Exact run filename:** `AG-RUN-CLOSEOUT-<ATTEMPT-ID>-v1.md`

Create this record only after `RUN_RESULTS_COMPLETED`, `LOG_CLOSED`, successful
closed-log validation, and byte-identical copy of the log into
`closeout/input`. The closed log cannot describe its own future external hash.

## Required later closeout binding

- Packet ID/version:
- Attempt ID:
- Closed execution-log exact filename:
- Closed execution-log validation command/stdout/stderr/exit code:
- Closed execution-log SHA-256:
- Byte-identical closeout-copy check command/result:
- Run-results exact filename:
- Run-results artifact ID/version/state: `AG-RUN-RESULTS` / `v1` / `RUN RESULTS COMPLETE`
- Run-results SHA-256:
- External manifest exact filename: `AG-RUN-CLOSEOUT-SHA256SUMS`
- External manifest exact members: closed execution log and run-results file
- External manifest verification command/stdout/stderr/exit code:
- External closeout-manifest SHA-256:
- Closeout completion timestamp/timezone:
- Completion state: `CLOSEOUT COMPLETE`

This record binds the Closed execution-log SHA-256, the external
closeout-manifest SHA-256, and the Run-results SHA-256. It remains outside the
already closed log. The binding proves local byte identity and ordering, not a
third-party timestamp, human result, or real-world outcome.
