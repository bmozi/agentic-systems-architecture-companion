# Facilitator Guide

**Packet:** AG-RV-PILOT-001 version 1.2.1
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

The manifest is detached and must not list or hash itself. A later-stage
delivery manifest may hash the earlier manifest as one supplied file.

The planned live update creates the first revised Stage A artifact set and is
not a post-freeze correction. After any scored freeze, preserve every prior
frozen artifact. A later correction must use a new immutable filename and
version and record exact old/new text, filenames, IDs/versions, hashes, reason,
correction timestamp/timezone, replacement freeze record, and replacement
manifest. If supplied source bytes change, stop and record the deviation; do
not silently continue the same run.

## Required detached revised-freeze record

After Stage A completes all planned live-update revisions, but before the
handoff is opened, use the run-record schema in
[`04-freeze-and-correction-record-templates.md`](04-freeze-and-correction-record-templates.md):

1. confirm that every revised artifact has an immutable literal local filename,
   artifact ID, and version;
2. reject any revised artifact that still says `DRAFT`, `PENDING FREEZE`, or
   otherwise claims its freeze is pending; if it contains a status/state
   field, reject a blank field and require `REVISED COMPLETE` before hashing;
3. calculate the SHA-256 hash of each exact revised artifact;
4. create `STAGE-A-REVISED-FREEZE-RECORD.md` containing one row per governed
   artifact with its exact filename, ID, version, and hash, plus one exact
   freeze timestamp/timezone and the literal governing manifest name
   `STAGE-A-REVISED-FREEZE-SHA256SUMS`;
5. hash the completed freeze record and create
   `STAGE-A-REVISED-FREEZE-SHA256SUMS` listing the freeze record and every
   governed revised artifact, but not the manifest itself; and
6. verify every listed hash from the sealed directory and record verification
   time/timezone in the facilitator log.

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
4. Freeze the initial workbook and detailed artifacts before the update;
   record IDs, versions, timestamp, and manifest.
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
   handoff until the record and manifest verify. Then have Stage A complete and
   freeze the one-screen handoff. Record initial, revised, and one-screen
   timestamps and manifests; do not let the handoff erase earlier evidence.
   The handoff must distinguish
   a recommended stop or containment from evidence that containment was
   actually executed. When execution is not evidenced, the actual status must
   be `UNKNOWN`.
8. Record exact Stage A end.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact. Complete consent
   before beginning.
2. Record exact Stage B start, timezone, and route immediately before first
   packet read.
3. Supply the frozen one-screen handoff first. Complete and checksum-freeze
   Section 1 before supplying the scenario or detailed artifacts.
4. Supply the scenario; every handoff-linked detail under the exact literal
   local filename; `STAGE-A-REVISED-FREEZE-RECORD.md`; and
   `STAGE-A-REVISED-FREEZE-SHA256SUMS`. Supply the governing manifest as a file,
   not merely its name or a facilitator assertion. Verify exact filenames and
   hashes. Do not rename, substitute, regenerate, summarize, or omit a linked
   detail. Any mismatch is a recorded deviation and stop. Complete and
   checksum-freeze Section 2 before supplying either executive file.
5. Supply `EXECUTIVE-DECISION-BRIEF.md` and
   `VALUE-AND-EVIDENCE-LEDGER.md`, in that order. Complete and checksum-freeze
   Sections 3–5.
6. Keep the Stage A participant unavailable through the Sections 3–5 freeze.
   End scoring before allowing explanation or repair, then complete Section 6.
7. Record exact Stage B end. Record every open time, pause, question, access
   problem, intervention, freeze timestamp, artifact version, and hash.

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
