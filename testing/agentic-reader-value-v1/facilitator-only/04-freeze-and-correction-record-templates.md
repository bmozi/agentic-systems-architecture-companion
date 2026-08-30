# Detached Freeze-Verification and Correction Record Templates

**Packet:** AG-RV-PILOT-001 version 1.2.5
**Status:** Facilitator-only blank records; prepared and unrun

These schemas create run evidence. Never supply this source template during a
scored stage. Preserve blank records as blank. A detached record describes a
verification event that already occurred; it must never predict a future hash,
verification result, or timestamp.

## Output completion header

Before hashing, every governed output records its exact immutable filename,
artifact ID/version, completion timestamp/timezone, and required state:
`INITIAL COMPLETE`, `REVISED COMPLETE`, `HANDOFF COMPLETE`, `SECTION 1
COMPLETE`, `SECTION 2 COMPLETE`, or `SECTIONS 3-5 COMPLETE`.

Do not place the output's own hash, a future verification time, or a claim that
verification succeeded inside the governed output.

## Required detached record for every output phase

Use this complete schema separately for all six record filenames in the table
below. Create a record only after its governing manifest has been created and
successfully verified. Do not reuse one record across phases.

- Attempt ID:
- Phase ID: `stage_a_initial` / `stage_a_revised` /
  `stage_a_handoff` / `stage_b_section_1` / `stage_b_section_2` /
  `stage_b_sections_3_5`
- Facilitator code:
- Participant, reviewer, or synthetic actor code:
- Exact observed verification command:
- Exact observed verification stdout, verbatim:
- Exact observed verification stderr, verbatim; blank only when truly empty:
- Observed verification exit code; must be `0` for a valid freeze:
- Observed manifest verification timestamp, RFC 3339 numeric offset:
- Observed manifest verification timezone, IANA zone and abbreviation:
- Record completion timestamp, RFC 3339 numeric offset; must be later than
  manifest verification:
- Record completion timezone, IANA zone and abbreviation:
- Governing manifest exact filename:
- Governing manifest SHA-256:
- Facilitator-side execution/access log exact filename:
- Execution-log checkpoint sequence for the corresponding
  `GOVERNING_MANIFEST_VERIFIED` event:
- Execution-log checkpoint entry SHA-256:
- Required prior gate and file-open order satisfied: yes / no / deviation
- No undeclared participant or orchestration input occurred: yes / no /
  deviation and stop

| Exact immutable local filename | Artifact ID/version | Artifact completion timestamp/timezone | Artifact state before hashing | SHA-256 |
| --- | --- | --- | --- | --- |
| | | | | |

The governing manifest lists only the completed governed artifacts above. It
does not list or hash itself or this later record. After this record is
complete, the next applicable phase-input manifest hashes the governed
artifacts, governing manifest, completed record, and only the new inputs
declared in the canonical protocol.

### Additional revised Stage A assertions

Complete these fields in `STAGE-A-REVISED-FREEZE-RECORD.md` in addition to the
required schema above:

- Handoff had not been opened at the manifest-verification timestamp: yes / no / deviation
- All planned live-update revisions were complete: yes / no / deviation
- No governed artifact retained a draft or pending-freeze state: yes / no / deviation
- Every revised current ID/version pair differs from its initial pair: yes /
  no / deviation
- Initial identity appears only as explicit lineage: yes / no / deviation
- Fictional reported effects acknowledged without `no execution occurred`
  wording or real-world-evidence promotion: yes / no / deviation

After this record is complete,
`STAGE-A-HANDOFF-INPUT-SHA256SUMS` hashes those artifacts, their governing
manifest, this record, and the blank handoff input.

## Exact output chains

These are the six scored freeze chains. Completing all six does not complete
the entry branch, stage boundaries, debrief, run results, log close, or later
external closeout.

| Phase | Governed output manifest | Detached freeze-verification record |
| --- | --- | --- |
| Stage A initial | `STAGE-A-INITIAL-SHA256SUMS` | `STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md` |
| Stage A revised | `STAGE-A-REVISED-FREEZE-SHA256SUMS` | `STAGE-A-REVISED-FREEZE-RECORD.md` |
| Stage A handoff | `STAGE-A-HANDOFF-SHA256SUMS` | `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Section 1 | `STAGE-B-SECTION-1-SHA256SUMS` | `STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Section 2 | `STAGE-B-SECTION-2-SHA256SUMS` | `STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Sections 3-5 | `STAGE-B-SECTIONS-3-5-SHA256SUMS` | `STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md` |

For every row: complete the output; create the manifest; verify the manifest
and capture the exact command, stdout, stderr, exit code, timestamp/timezone,
and execution-log checkpoint; then create the detached record using every
field in the required schema, including its later completion
timestamp/timezone.

## Next phase-input manifests

| Release | Exact manifest |
| --- | --- |
| Initial artifacts to live update | `STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS` |
| Revised artifacts to blank handoff | `STAGE-A-HANDOFF-INPUT-SHA256SUMS` |
| Handoff to Stage B Section 1 | `STAGE-B-PHASE-1-INPUT-SHA256SUMS` |
| Section 1 to detailed read-back | `STAGE-B-PHASE-2-INPUT-SHA256SUMS` |
| Section 2 to executive decision | `STAGE-B-PHASE-3-INPUT-SHA256SUMS` |
| Sections 3-5 to post-scoring Section 6 | `STAGE-B-DEBRIEF-INPUT-SHA256SUMS` |

Each next phase-input manifest hashes the prior completed output, governing
manifest, detached record, and new inputs. Verify it before new material opens.
No other participant file, prompt, message, tool output, or instruction is
permitted. Synthetic orchestration uses a separate predeclared, verified
`ORCHESTRATION-INPUT-SHA256SUMS` and remains unscored facilitator evidence.

The debrief input manifest is a post-scoring release, not a seventh scored
freeze chain. It hashes `STAGE-B-SECTIONS-3-5-v1.md`, its governing manifest,
its detached record, and exact `06-section-6-debrief.md`. Verify it only after
`SCORING_ENDED` and before the debrief opens.

Run-specific results use `AG-RUN-RESULTS-<ATTEMPT-ID>-v1.md` and state
`RUN RESULTS COMPLETE` before `LOG_CLOSED`. The later external closeout uses
`AG-RUN-CLOSEOUT-SHA256SUMS` and
`AG-RUN-CLOSEOUT-<ATTEMPT-ID>-v1.md`; neither may be predicted inside a scored
artifact or pre-close result.

## Correction of already frozen bytes

The planned live-update revision is not entered here. Use this record only when
bytes change after a freeze. Stop the current route; preserve the old bytes;
and assign the new bytes a new immutable filename, artifact ID/version,
completion timestamp, manifest, observed verification event, and detached
record. Never overwrite, rename, or relabel the prior artifact.

- Correction record exact immutable filename:
- Attempt ID:
- Reason for correction:
- Exact correction timestamp and timezone:
- Replacement freeze-verification record exact immutable filename:
- Replacement manifest exact immutable filename:

| Exact old text or changed content | Exact new text or changed content | Exact old filename | Old artifact ID/version | Old SHA-256 | Exact new filename | New artifact ID/version | New SHA-256 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

- Old artifact and entire prior chain retained: yes / no / deviation
- Effect on handoff, Stage B route, scoring, and packet version:

Complete and hash the replacement governed artifacts, create and verify the
replacement manifest, and only then create its detached verification record.
Record the immutable replacement chain and exact timestamps/timezones in
`03-results-and-deviation-log.md`.
