# Detached Freeze and Correction Record Templates

**Packet:** AG-RV-PILOT-001 version 1.2.1
**Status:** Facilitator-only blank records; prepared and unrun

These schemas create run evidence. Never supply this source template during a
scored stage. Create each run record under the exact output filename named
below. Preserve blank records as blank; do not imply that a freeze or
correction occurred until the required bytes exist and verify.

## Revised Stage A freeze record

Save the completed record as exactly
`STAGE-A-REVISED-FREEZE-RECORD.md`. Complete and verify it before Stage A opens
the handoff.

- Attempt ID:
- Exact freeze timestamp and timezone:
- Governing manifest exact filename: `STAGE-A-REVISED-FREEZE-SHA256SUMS`
- Handoff had not been opened at the freeze timestamp: yes / no / deviation
- All planned live-update revisions were complete: yes / no / deviation
- No governed artifact retained a draft or pending-freeze state: yes / no / deviation

| Exact immutable local filename | Artifact ID | Artifact version | Artifact state at freeze | SHA-256 |
| --- | --- | --- | --- | --- |
| | | | | |

The governing manifest lists this completed freeze record and every governed
artifact above. It does not list or hash itself.

- Facilitator code:

After hashing this completed record, create and verify the governing manifest.
Record the verification method, result, and timestamp/timezone in
`03-results-and-deviation-log.md`, outside this manifest-governed record. Do not
append the later verification result here; that would change this record's
already listed hash.

## Correction of already frozen bytes

The planned live-update revision is not entered here. Use this record only when
bytes change after a freeze. Stop the current route; preserve the old bytes;
and assign the new bytes a new immutable filename, artifact ID/version, freeze
record, and manifest. Never overwrite, rename, or relabel the prior artifact.

- Correction record exact immutable filename:
- Attempt ID:
- Reason for correction:
- Exact correction timestamp and timezone:
- Replacement freeze record exact immutable filename:
- Replacement manifest exact immutable filename:

| Exact old text or changed content | Exact new text or changed content | Exact old filename | Old artifact ID/version | Old SHA-256 | Exact new filename | New artifact ID/version | New SHA-256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

- Old artifact and prior freeze retained: yes / no / deviation
- Effect on handoff, Stage B route, scoring, and packet version:

After hashing this completed correction record and creating the replacement
manifest, record both verification results and their timestamp/timezone in
`03-results-and-deviation-log.md`. Do not add later verification results to
this already frozen record.
