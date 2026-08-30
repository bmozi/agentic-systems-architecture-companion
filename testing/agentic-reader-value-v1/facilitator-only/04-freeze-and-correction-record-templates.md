# Detached Freeze-Verification and Correction Record Templates

**Packet:** AG-RV-PILOT-001 version 1.2.2
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

## Revised Stage A freeze-verification record

Save the completed record as exactly
`STAGE-A-REVISED-FREEZE-RECORD.md`. Create it only after the governing manifest
has been created and successfully verified.

- Attempt ID:
- Record completion timestamp and timezone:
- Manifest verification timestamp and timezone:
- Verification method and result:
- Governing manifest exact filename: `STAGE-A-REVISED-FREEZE-SHA256SUMS`
- Governing manifest SHA-256:
- Handoff had not been opened at the manifest-verification timestamp: yes / no / deviation
- All planned live-update revisions were complete: yes / no / deviation
- No governed artifact retained a draft or pending-freeze state: yes / no / deviation

| Exact immutable local filename | Artifact ID/version | Artifact completion timestamp/timezone | Artifact state before hashing | SHA-256 |
| --- | --- | --- | --- | --- |
| | | | | |

The governing manifest lists only the completed governed artifacts above. It
does not list or hash itself or this later record. After this record is
complete, `STAGE-A-HANDOFF-INPUT-SHA256SUMS` hashes those artifacts, their
governing manifest, this record, and the blank handoff input.

- Facilitator code:

## Exact output chains

| Phase | Governed output manifest | Detached freeze-verification record |
| --- | --- | --- |
| Stage A initial | `STAGE-A-INITIAL-SHA256SUMS` | `STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md` |
| Stage A revised | `STAGE-A-REVISED-FREEZE-SHA256SUMS` | `STAGE-A-REVISED-FREEZE-RECORD.md` |
| Stage A handoff | `STAGE-A-HANDOFF-SHA256SUMS` | `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Section 1 | `STAGE-B-SECTION-1-SHA256SUMS` | `STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Section 2 | `STAGE-B-SECTION-2-SHA256SUMS` | `STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md` |
| Stage B Sections 3-5 | `STAGE-B-SECTIONS-3-5-SHA256SUMS` | `STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md` |

For every row: complete the output; create the manifest; verify the manifest
and capture the exact timestamp/timezone; then create the detached record with
all literal filenames, IDs/versions, completion states/times, artifact hashes,
and the manifest filename/hash.

## Next phase-input manifests

| Release | Exact manifest |
| --- | --- |
| Initial artifacts to live update | `STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS` |
| Revised artifacts to blank handoff | `STAGE-A-HANDOFF-INPUT-SHA256SUMS` |
| Handoff to Stage B Section 1 | `STAGE-B-PHASE-1-INPUT-SHA256SUMS` |
| Section 1 to detailed read-back | `STAGE-B-PHASE-2-INPUT-SHA256SUMS` |
| Section 2 to executive decision | `STAGE-B-PHASE-3-INPUT-SHA256SUMS` |

Each next phase-input manifest hashes the prior completed output, governing
manifest, detached record, and new inputs. Verify it before new material opens.

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
