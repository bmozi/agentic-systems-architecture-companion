# Facilitator Guide

**Packet:** AG-RV-PILOT-001 version 1.2.3
**Status:** Facilitator-only; prepared and unrun

## Purpose

Test the materials, not the participants. Observe whether the reader-value
layer supports a practitioner delegated-action decision and an independent
decision-owner read-back.

## Recommended timing

### Stage A — 70 to 85 minutes

- consent and setup: 5 minutes;
- scenario and recognition questions: 10 minutes;
- authority map: 25 minutes;
- governed tool and action budget: 20 minutes;
- live update and revision: 10 minutes; and
- handoff and feedback: 10 minutes.

### Stage B — 35 to 50 minutes

- independent read-back: 15 minutes;
- executive brief and value ledger review: 10 minutes;
- bounded decision: 10 minutes; and
- debrief: 5 to 15 minutes.

Time is evidence, not a speed target.

## No-coaching rule

During scored work, the facilitator may repeat written text or resolve file
access. Do not grant authority, select the action, interpret `accepted`, define
the budget, identify the memory defect, supply a stop path, or confirm an
answer. Do not supply an owner, authority, date, numeric baseline, limit,
budget, order state, or evidence source. Record every question, pause, access
problem, and intervention with exact time and level.

## Sealed delivery and byte identity

Before either stage, build a sealed, flat delivery directory containing only
the exact local filenames in `participant/00-packet-route.md`. The six companion
assets must be exact immutable copies named `START-HERE.md`,
`agent-authority-map.md`, `governed-tool-contract.md`,
`action-budget-and-blast-radius.md`, `EXECUTIVE-DECISION-BRIEF.md`, and
`VALUE-AND-EVIDENCE-LEDGER.md`. Create and verify a run-specific SHA-256
manifest covering every supplied file. Do not substitute a repository path,
live link, summary, renamed file, or newer byte sequence during a run.

Every governed output contains its ID/version, exact completion
timestamp/timezone, and required `COMPLETE` state before hashing. Its governing
manifest hashes only those completed outputs and never itself or a later
record. Verify the manifest from sealed storage, capture the exact verification
timestamp/timezone, and only then create the detached freeze-verification
record. A later phase-input manifest hashes the prior outputs, manifest,
detached record, and new inputs.

Create `AG-EXECUTION-ACCESS-LOG-<ATTEMPT-ID>-v1.jsonl` from
[`05-execution-and-access-log.md`](05-execution-and-access-log.md) before the
attempt. Keep it facilitator-side. Record every phase-input gate, exact-file
release and open, output completion, manifest creation, observed verification,
detached-record completion, and phase completion with actor, one exact
filename, timestamp/timezone, and previous-entry continuity hash. Every
detached record checkpoints this log through its governing-manifest
verification. Close and bind the completed log in the run closeout manifest.

Do not admit undeclared orchestration. Human participants receive only current
phase-manifest inputs. For a synthetic rehearsal, preserve every added system,
developer, user, tool, or orchestration instruction as immutable bytes in
`ORCHESTRATION-INPUT-SHA256SUMS`; verify and log that manifest before use.
Label the result orchestration-aided. An undeclared input requires a recorded
deviation, stop, preserved partial chain, and new attempt.

The planned live update creates the first revised Stage A artifact set and is
not a post-freeze correction. After any scored freeze, preserve every prior
frozen artifact. A later correction must use a new immutable filename and
version and record exact old/new text, filenames, IDs/versions, hashes, reason,
completion and verification timestamps/timezones, replacement freeze-
verification record, and replacement manifest. The replacement is a new
immutable artifact set and provenance chain. If supplied source bytes change,
stop and record the deviation; do not silently continue the same run.

## Required detached revised-freeze record

After Stage A completes all planned live-update revisions, but before the
handoff is opened, use the run-record schema in
[`04-freeze-and-correction-record-templates.md`](04-freeze-and-correction-record-templates.md):

1. confirm that every revised artifact has an immutable literal local filename,
   artifact ID, and version;
2. reject any revised artifact that still says `DRAFT`, `PENDING FREEZE`, or
   otherwise claims its freeze is pending; if it contains a status/state
   field, reject a blank field and require `REVISED COMPLETE` before hashing;
3. calculate the SHA-256 hash of each exact revised artifact and create
   `STAGE-A-REVISED-FREEZE-SHA256SUMS`, listing only those completed artifacts;
4. verify that manifest from the sealed directory and capture the exact
   verification timestamp/timezone;
5. only after successful verification, create
   `STAGE-A-REVISED-FREEZE-RECORD.md` containing one row per governed artifact
   with its exact filename, ID/version, completion time/state, and hash, plus
   the already-observed verification timestamp/timezone and the governing
   manifest's literal filename and SHA-256. Also record the attempt, phase,
   facilitator and actor codes, exact verification command/stdout/stderr/exit
   code/timestamp/timezone, execution-log filename/checkpoint sequence/hash,
   and a record-completion timestamp/timezone later than verification; and
6. create and verify `STAGE-A-HANDOFF-INPUT-SHA256SUMS`, listing the revised
   artifacts, their governing manifest, the completed detached record, and the
   blank handoff input.

Only then may Stage A open and complete `05-one-screen-handoff.md`. Its detail
links must enumerate every governed detail under the exact literal filename in
the freeze record. A link to a directory, repository, alias, summary, or
artifact ID without the literal filename is not sufficient.

## Stage A sequence

1. Complete the consent prerequisites and obtain human consent. A blank field
   means do not start.
2. Record exact Stage A start, timezone, and supplied-file route immediately
   before the participant's first packet read.
3. Follow `participant/00-packet-route.md` exactly. Let the participant
   complete recognition before opening companion assets. The miniature example
   embedded in the Agent Authority Map is authorized teaching content; do not
   follow its links to full worked examples or supply omitted files.
4. Complete the initial workbook and detailed artifacts before the update with
   IDs/versions, completion timestamps/timezones, and `INITIAL COMPLETE` state.
   Create and verify `STAGE-A-INITIAL-SHA256SUMS`; only then create
   `STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md`. Export the exact quote in
   Step 5 as `STAGE-A-LIVE-UPDATE-v1.md`. Create and verify
   `STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS`, covering the initial artifacts,
   their manifest and detached record, and that update file. Do not read the
   update until this phase-input manifest passes.
   The initial detached record uses the same complete record contract as the
   revised record: attempt, phase, facilitator/actor codes, exact observed
   command/output/exit/time/timezone, log checkpoint, manifest/artifact
   bindings, and later record-completion timestamp/timezone.
5. Read the live update:

> One duplicated low-stock record reached three depot workers. The old memory
> was treated as current purchase authority. The first order call timed out
> after the supplier committed it, so one worker retried with a new tool-call
> and business ID. Other workers selected a second supplier to improve
> availability. A provider report says four orders totaling $18,400 are now
> accepted or committed; treat that amount as reported exposure, not an
> observed terminal consequence. Two budget reservations are reported, and
> the agent published a restock-planned event. No shared budget stopped the
> workers, no one knows which orders can be cancelled without residue, and the
> dashboard shows only a high-confidence
> plan.

6. Ask only: “What can each party safely say or do now, and what changes in
   your artifacts?”
7. Finish revised detailed artifacts, including the four-order register, and
   apply the required detached revised-freeze procedure above. Do not open the
   handoff until `STAGE-A-HANDOFF-INPUT-SHA256SUMS` verifies. Then have Stage A
   complete the one-screen handoff with ID/version, completion
   timestamp/timezone, and `HANDOFF COMPLETE` state. Create and verify
   `STAGE-A-HANDOFF-SHA256SUMS`; only afterward create
   `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md`. Record initial, revised,
   and one-screen completion and verification timestamps, manifests, and
   detached records; do not let the handoff erase earlier evidence.
   The handoff must distinguish
   a recommended stop or containment from evidence that containment was
   actually executed. When execution is not evidenced, the actual status must
   be `UNKNOWN`.
   Reject a revised output whose current ID/version pair still equals its
   initial pair; the initial pair may appear only in explicit lineage. Require
   the handoff's candidate proposal scope and presently authorized scope to be
   separate, and require a nonblank largest unacceptable outcome.
   Because the update reports fictional actions and effects, reject `no
   execution occurred`; require `FICTIONAL REPORTED EFFECTS EXIST; REAL-WORLD
   EXECUTION EVIDENCE DOES NOT` plus the unreconciled scenario effects.
8. Record exact Stage A end.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact. Complete consent
   before beginning.
2. Record exact Stage B start, timezone, and route immediately before first
   packet read.
3. Create and verify `STAGE-B-PHASE-1-INPUT-SHA256SUMS`, covering the completed
   handoff, its governing manifest and detached record, the route, and the
   blank workbook. Only then supply and open the handoff as the first scored
   content; its provenance files are unscored inputs. Complete and export
   `STAGE-B-SECTION-1-v1.md` with ID/version, completion timestamp/timezone,
   and `SECTION 1 COMPLETE`. Create and verify
   `STAGE-B-SECTION-1-SHA256SUMS`; only then create
   `STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md`, before supplying the
   scenario or detailed artifacts.
   Section 1 must use the exact literal `NOT RELEASED — PHASE 2 CHECK` for the
   revised record, revised manifest, detailed files, and detailed execution
   evidence. Blank, `UNKNOWN`, or claimed verification is a deviation at this
   gate. Do not edit frozen Section 1 after Phase 2 supplies those files.
4. Supply the scenario; every handoff-linked detail under the exact literal
   local filename; `STAGE-A-REVISED-FREEZE-RECORD.md`; and
   `STAGE-A-REVISED-FREEZE-SHA256SUMS`. Supply the governing manifest as a file,
   not merely its name or a facilitator assertion. Verify exact filenames and
   hashes. Do not rename, substitute, regenerate, summarize, or omit a linked
   detail. Any mismatch is a recorded deviation and stop. Create and verify
   `STAGE-B-PHASE-2-INPUT-SHA256SUMS`, which includes Section 1 and its
   manifest/record plus every new detailed input. Complete and export
   `STAGE-B-SECTION-2-v1.md` with ID/version, completion timestamp/timezone,
   and `SECTION 2 COMPLETE`. Create and verify
   `STAGE-B-SECTION-2-SHA256SUMS`; only then create
   `STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md`, before supplying either
   executive file.
5. Supply `EXECUTIVE-DECISION-BRIEF.md` and
   `VALUE-AND-EVIDENCE-LEDGER.md`, in that order. Create and verify
   `STAGE-B-PHASE-3-INPUT-SHA256SUMS`, including Section 2 and its
   manifest/record plus both executive inputs. Complete and export
   `STAGE-B-SECTIONS-3-5-v1.md` with ID/version, completion timestamp/timezone,
   and `SECTIONS 3-5 COMPLETE`. Create and verify
   `STAGE-B-SECTIONS-3-5-SHA256SUMS`; only then create
   `STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md`.
6. Keep the Stage A participant unavailable through the Sections 3–5 freeze.
   End scoring before allowing explanation or repair, then complete Section 6.
7. Record exact Stage B end. Record every open time, pause, question, access
   problem, intervention, completion timestamp, manifest verification event,
   detached record, artifact version, and hash.

Every one of the six detached records—not only the revised Stage A record—uses
the complete record contract and cites the corresponding execution-log
checkpoint. The results log is a summary; it does not replace the item-level
JSON Lines evidence.

## Intervention levels

- **L0:** silence or think-aloud reminder;
- **L1:** repeat written text;
- **L2:** neutral probe such as “Who authorized this exact consequence?”;
- **L3:** define a term without applying it; and
- **L4:** recommend or supply the decision.

L3 is aided. L4 contaminates the affected gate. Preserve the result.

## Stop conditions

Stop and retain partial evidence on consent withdrawal, confidential-data
disclosure, material unblinding, changed frozen bytes, distress, material tool
failure, or coaching that makes the central result uninterpretable.
