# Execution and Access Log

**Packet:** AG-RV-PILOT-001 version 1.2.3
**Status:** Facilitator-only schema and blank run template; prepared and unrun

This log proves the order in which inputs were admitted, files were released
and opened, artifacts were completed, manifests were created and verified,
and detached records were completed. It is facilitator-side evidence. Never
place this file, its JSON Lines run instance, or its schema in a participant
delivery directory or a scored phase-input manifest.

## Exact run file and entry schema

Create one run file named
`AG-EXECUTION-ACCESS-LOG-<ATTEMPT-ID>-v1.jsonl`. Each physical line is exactly
one JSON object conforming to
[`05-execution-access-log-schema.json`](05-execution-access-log-schema.json).
Do not combine two filenames in one entry. Use `NOT_APPLICABLE` in the
artifact fields or exact-filename field when an event has no artifact or file.

Each entry records:

- packet ID/version and one immutable attempt ID;
- monotonically increasing sequence number;
- exact phase and event type;
- facilitator or actor code and role;
- one exact literal local filename;
- artifact ID, version, and state when applicable;
- an RFC 3339 timestamp with numeric offset and a separate IANA
  timezone/observed abbreviation;
- the exact observed verification command, stdout, stderr, and exit code for
  every manifest-verification event; and
- the previous entry's sequence/hash and the current entry hash.

Calculate `entry_sha256` over the RFC 8785 canonical JSON representation of
the entire entry **without** the `entry_sha256` member. Entry 1 uses
`GENESIS` for both previous-continuity values. Every later entry names the
immediately preceding sequence and entry hash. A gap, duplicate sequence,
hash mismatch, reordered entry, or attempt-ID change is a stop and deviation.

## Ordered gate pattern

Use the applicable events in this order for every phase:

1. `PHASE_INPUT_MANIFEST_CREATED`;
2. `PHASE_INPUT_MANIFEST_VERIFIED` with observed command/output/exit/time;
3. one `FILE_RELEASED` and one `FILE_OPENED` entry per exact file, in route
   order;
4. one `OUTPUT_COMPLETED` entry per governed artifact;
5. `GOVERNING_MANIFEST_CREATED`;
6. `GOVERNING_MANIFEST_VERIFIED` with observed
   command/output/exit/time;
7. `DETACHED_RECORD_COMPLETED`; and
8. `PHASE_COMPLETED`.

The detached record cites the log sequence and hash through the governing-
manifest verification it describes. The later `DETACHED_RECORD_COMPLETED`
entry cannot be cited by that earlier record; it is instead continuity-bound
by the next phase-input manifest, which hashes the completed detached record,
and by the next log entries. At run closeout, append `LOG_CLOSED`, then hash
the complete JSON Lines file in the run closeout manifest. Do not rewrite a
prior log line. A correction appends events and preserves the earlier chain.

## Orchestration boundary

Human participants receive only the exact files admitted by the current
phase-input manifest and route. Facilitator guidance remains facilitator-side
and is logged, not delivered as participant content.

For a synthetic rehearsal, every system, developer, user, tool, or
orchestration instruction beyond the packet must first be preserved as an
immutable file, declared in a run-specific
`ORCHESTRATION-INPUT-SHA256SUMS`, verified, and logged as
`ORCHESTRATION_MANIFEST_VERIFIED` before the synthetic actor receives it.
These files remain unscored orchestration inputs and must not be represented
as participant material. An undeclared prompt, message, file, tool result, or
instruction requires `DEVIATION`, `STOP`, preservation of the partial chain,
and a new attempt; it may not be silently admitted or retroactively declared.

## Closeout checks

- Attempt ID remains identical on every line.
- Sequence numbers are contiguous and each continuity hash verifies.
- Every release/open/completion event names exactly one literal filename.
- Every route gate has the required manifest-created, manifest-verified,
  detached-record-completed, and phase-completed events in order.
- Every detached record contains the same phase, actor codes, observed
  verification evidence, and log checkpoint as the corresponding log entry.
- The final closeout manifest hashes the completed JSON Lines log.

No blank template or static schema is evidence that a run occurred.
