# Results and Deviation Log

**Packet:** AG-RV-PILOT-001 version 1.2.5
**Status:** Blank controlled record; no result exists
**Run artifact identity:** `AG-RUN-RESULTS` / `v1`
**Exact run filename:** `AG-RUN-RESULTS-<ATTEMPT-ID>-v1.md`

Each attempt creates a new immutable run-specific result from this template.
Complete it after `STAGE_B_ENDED`, record `RUN_RESULTS_COMPLETED`, and only
then append `LOG_CLOSED`. The source template is never itself a run result.

## Run identity

- Attempt ID:
- Execution owner and authorization:
- Stage A participant or synthetic actor code:
- Stage B decision-owner or synthetic reviewer code:
- Facilitator code:
- Evaluator and independence disclosure:
- Date, mode, and timezone:
- Human or synthetic; if synthetic, exact actor code and orchestration-aided label:
- Selected entry branch: human / synthetic; exactly one:
- Exact branch record filename, artifact ID/version, and SHA-256:
- Source `SHA256SUMS` identity/hash:
- Synthetic `ORCHESTRATION-INPUT-SHA256SUMS` identity/hash, or `NOT APPLICABLE — HUMAN`:
- Run-results completion timestamp/timezone:
- Run-results completion state: `RUN RESULTS COMPLETE`

## Consent, privacy, and freeze

- Human consent records completed before either scored stage, or exact
  synthetic-context record and `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`:
- Branch omission/mixing check: none / deviation and stop
- Storage/access/retention authority:
- Run-specific SHA-256 manifest:
- Facilitator-side execution/access log exact filename:
- Final pre-close execution-log checkpoint sequence and entry SHA-256:
- Closed-log validation and external closeout: `NOT YET AVAILABLE — OCCURS AFTER LOG_CLOSED`
- Undeclared input check: none / deviation and stop
- Run-specific manifest verified before each stage:
- Prepared-source manifest match:
- Governing `STAGE-A-REVISED-FREEZE-SHA256SUMS` verification time/timezone:
- Detached `STAGE-A-REVISED-FREEZE-RECORD.md` completion time/timezone:
- `STAGE-A-HANDOFF-INPUT-SHA256SUMS` verification time/timezone:
- Later correction record and replacement-manifest verification, if any:
- Every handoff-linked literal filename received unchanged by Stage B:
- Supplied and withheld materials correct: yes / no / deviation
- Confidentiality or privacy concern:

Final closed-log SHA-256 is not available before `LOG_CLOSED` and must not be
predicted here. Do not record a future closeout timestamp. The later external
closeout record binds the actual closed-log, closeout-manifest, and this
run-results file's hashes.

## Exact starts, file route, questions, pauses, and interventions

- Exact Stage A start before first scored read of the packet route, with timezone:
- Exact `STAGE_A_STARTED` checkpoint:
- Exact Stage A material-feedback completion and `STAGE_A_FEEDBACK_COMPLETED` checkpoint:
- Exact Stage A end and `STAGE_A_ENDED` checkpoint:
- Exact Stage B start before first scored read of the packet route, with timezone:
- Exact `STAGE_B_STARTED` checkpoint:
- Exact scoring end and `SCORING_ENDED` checkpoint:
- Exact debrief-input verification checkpoint:
- Exact Section 6/debrief completion and `DEBRIEF_COMPLETED` checkpoint:
- Exact Stage B end and `STAGE_B_ENDED` checkpoint:

| Time | Stage | File opened or activity | Route position | Question/pause/access issue | Intervention and level | Interpretation effect |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

No coaching is allowed. Repeating text or resolving access is still logged.
Supplying an owner, authority, date, number, baseline, limit, budget, order
state, evidence source, or answer contaminates the affected gate.

This table summarizes the item-level JSON Lines execution/access log; it does
not replace it. Every file release or open is a separate log event naming one
exact filename. Every manifest verification records verbatim command, stdout,
stderr, exit code, timestamp/timezone, actor, and continuity hash.

## Timing and freezes

| Stage/activity | Exact start | Exact end | Elapsed | Artifact IDs/manifest or notes |
| --- | --- | --- | ---: | --- |
| A recognition before assets | | | | |
| A detailed work | | | | |
| A initial completion / manifest verification / detached record | | | | |
| A live update | | | | |
| A revised completion and four-order register | | | | |
| A revised manifest verification / detached record / handoff-input verification | | | | |
| A one-screen handoff completion / manifest verification / detached record | | | | |
| B Phase 1 input; Section 1 completion / manifest verification / detached record | | | | |
| B Phase 2 input; Section 2 completion / manifest verification / detached record | | | | |
| B Phase 3 input; Sections 3–5 completion / manifest verification / detached record | | | | |
| B Section 6 debrief after scoring | | | | |

## Declared counts and full-route closure

- Declared input-file count:
- Actual release count:
- Actual open/read count:
- Governed scored artifact count:
- Governing-manifest verification count:
- Detached-record count; expected six:
- Stage-boundary event count/result:
- Debrief input/output count/result:
- Run-results identity/completion result:

| Closure layer | State | Evidence and negative boundary |
| --- | --- | --- |
| Six scored freeze chains | complete / partial / deviated / not interpretable | |
| Selected entry branch and both context gates | complete / partial / deviated | |
| Stage A start/feedback/end | complete / partial / deviated | |
| Stage B start/scoring end/debrief/end | complete / partial / deviated | |
| Immutable run-specific results before log close | complete / partial / deviated | |
| Later external closeout | pending until after log close / complete / deviated | |

Do not call the full route complete while the later external closeout row is
pending or deviated. Six freeze chains complete is not full-route completion.

## Post-freeze corrections

The planned live-update revision is not a correction. Preserve each prior
frozen artifact. Leave blank if no later correction occurred.

| Section | Exact old text | Exact new text | Reason | Correction timestamp/timezone | Exact old filename, ID/version, SHA-256 | Exact new filename, ID/version, SHA-256 | Replacement manifest, verification event, detached record, and next-phase manifest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Temporal freeze chain

| Output phase | Completed artifact filename + ID/version + completion time/state | Governing manifest filename/hash | Observed command/stdout/stderr/exit + exact verification timestamp/timezone | Detached record filename/hash + attempt/phase/actor + completion timestamp/timezone + log checkpoint | Next phase-input manifest filename/hash + verification time |
| --- | --- | --- | --- | --- | --- |
| Initial Stage A | | | | | |
| Revised Stage A | | | | | |
| Handoff | | | | | |
| Stage B Section 1 | | | | | |
| Stage B Section 2 | | | | | |
| Stage B Sections 3-5 | | | | | N/A |

A detached record is valid only when created after the manifest verification
it describes. No governing manifest may list itself or that later record. No
governed output may embed its own hash or a future verification timestamp.
Each detached record includes the same attempt ID; matching phase; nonblank
facilitator and actor codes; exact observed command, stdout, stderr, exit code,
timestamp and timezone; a later record-completion timestamp/timezone; the
manifest/artifact bindings; and the execution-log filename, checkpoint
sequence, and entry hash.

## Content-integrity findings

- Revised current ID/version pairs differ from initial pairs; initial pairs
  appear only as lineage:
- Candidate proposal scope is separate from present authorization and current
  authority evidence:
- Handoff largest unacceptable outcome is nonblank:
- Stage B Section 1 uses `NOT RELEASED — PHASE 2 CHECK` for every withheld
  detail and was not edited after freeze:
- Fictional reported effects are acknowledged without claiming real-world
  execution evidence or saying `no execution occurred`:

## Handoff layout proof

- Handoff Markdown exact filename/hash:
- PDF exact filename/hash:
- Layout-proof record exact filename/hash:
- US Letter portrait, one page, margins at least 0.5 inch, text at least 9pt,
  reader-facing words no more than 450 excluding provenance, no clipping,
  overlap, hidden overflow, or unreadable shrinking: pass / hold / unrun
- Layout finding and retained failure, if any:
- Human scanability/comprehension evidence: `UNRUN` unless separately consented

## Gate results

| Gate | Score/state | Exact evidence | Negative or boundary finding |
| --- | --- | --- | --- |
| RV-1 | | | |
| RV-2 | | | |
| RV-3 | | | |
| RV-4 | | | |
| RV-5 | | | |
| RV-6 | | | |
| RV-7 | | | |

## Deviations and stops

| ID | Condition | What occurred | Action | Evidence retained | Effect |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Findings and disposition

| ID | Finding | Source | Severity | Revise / retest / hold / remove | Owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Truthful state statement

- What this exact pair establishes:
- What it does not establish:
- Protocol integrity state:
- Synthetic behavior state:
- Local layout state:
- Human evidence state: `PREPARED/UNRUN` unless a consented human run occurred
- Real-world evidence state: `UNRUN`
- Packet state after authorized review:
- Files changed only after raw evidence was preserved:
- Next attempt and version:

## Pre-close completion

- Every required field complete: yes / no / deviation
- `RUN_RESULTS_COMPLETED` sequence/hash:
- Run-results completion timestamp/timezone:
- Run-results state: `RUN RESULTS COMPLETE` / invalid
- Authorized next event: `LOG_CLOSED` only after this record is immutable
