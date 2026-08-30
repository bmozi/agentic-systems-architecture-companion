# Exact Packet Route

**Packet:** AG-RV-PILOT-001 version 1.2.4
**Status:** Prepared and unrun; this route records no human result

## Before either stage

The facilitator first creates the run-specific execution/access log and records
`RUN_STARTED`. Choose exactly one entry branch for the entire attempt and
record `ENTRY_BRANCH_SELECTED`. The branches are
mutually exclusive and may not change or mix between stages:

- **Human branch:** complete every execution-owner, storage, access,
  retention, deletion, withdrawal, recording, participant, and affirmation
  field in `01-consent-and-privacy.md`. Use separate completed run records for
  Stage A and Stage B. A blank prerequisite or missing human consent means
  **do not start**. Do not create or deliver a synthetic-context record.
- **Synthetic branch:** do not complete or deliver the human consent notice.
  Complete the exact run-specific
  `AG-SYNTHETIC-CONTEXT-<ATTEMPT-ID>-v1.md` from
  `01-synthetic-context-record.md`, with artifact identity
  `AG-SYNTHETIC-CONTEXT` / `v1` and the literal
  `SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`. It must state that the
  scenario is fictional, the run is orchestration-aided, and no human consent,
  comprehension, usability, or practitioner result exists.

Before any Stage A scored file opens, create and verify
`STAGE-A-CONTEXT-SHA256SUMS` over only the selected branch record and record
`STAGE_A_CONTEXT_MANIFEST_VERIFIED`. Before Stage B starts, create and verify
`STAGE-B-CONTEXT-SHA256SUMS` over only the applicable same-branch record and
record `STAGE_B_CONTEXT_MANIFEST_VERIFIED`. Branch omission, branch mixing, or
a synthetic human-result claim is a deviation and stop.

This route is written for a sealed, flat delivery directory. Use only the exact
local filenames named below. Every named file must be an immutable copy covered
by the run-specific SHA-256 manifest. Do not navigate to a repository, follow
an embedded link unless this route names its target, omit, replace, summarize,
or add a file. Record any access problem, question, pause, or facilitator
intervention; do not silently repair the route.

The facilitator keeps a separate append-only execution/access log. It is not
participant input. Every admitted file, release, open, completion, manifest,
verification, and detached record is logged with one exact filename, actor,
timestamp/timezone, and continuity hash. Receive no prompt, file, message,
tool result, or instruction outside the current declared phase inputs. In a
synthetic rehearsal, additional orchestration must be immutable, declared,
manifest-verified, and logged before use. Any undeclared input is a deviation,
stop, and new attempt.

## Stage A — exact read and work order

1. Complete and verify the selected Stage A context gate before scored work.
2. Immediately before first reading this route, record `STAGE_A_STARTED` and
   the exact Stage A start timestamp/timezone in the practitioner workbook and
   facilitator log.
3. Read this route, then `02-scenario-and-task.md`.
4. Open `03-practitioner-workbook.md` and complete
   Section 1, **Recognition before terminology**, without companion assets.
5. Open only these local files, in order: `START-HERE.md`,
   `agent-authority-map.md`, `governed-tool-contract.md`, and
   `action-budget-and-blast-radius.md`.
6. Complete the detailed workbook and relevant portions of the supplied blank
   assets. The miniature example embedded in the Agent Authority Map is
   authorized teaching content and may be read. Do not open its linked full
   worked examples, the Failure Lab, executive files, or facilitator files.
7. Complete the initial workbook and detailed artifacts with IDs, versions,
   completion timestamps/timezones, and `INITIAL COMPLETE` state. Create and
   verify `STAGE-A-INITIAL-SHA256SUMS`, capture the verification timestamp and
   timezone, and only then create
   `STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md`.
   That record must name the attempt and phase, facilitator and participant or
   synthetic-actor codes, exact observed verification command/stdout/stderr/
   exit code/time/timezone, log checkpoint, governed artifacts and manifest,
   and a record-completion timestamp/timezone later than verification.
8. The facilitator exports the exact authorized update as
   `STAGE-A-LIVE-UPDATE-v1.md` and creates
   `STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS`, hashing the initial artifacts, their
   governing manifest and detached record, and the update file. Verify that
   phase-input manifest before opening or reading the update. Then receive the
   update and record it exactly; revise only after the initial freeze. Complete
   the four-order/correction register.
9. Finish the revised workbook and every revised detailed artifact. Assign each
   an immutable literal local filename, artifact ID, and version. Its current
   ID/version pair must differ from the corresponding initial pair; the
   initial pair may appear only as a `Supersedes` or other explicit lineage
   reference, never as the revised artifact's current identity. Before any
   handoff work, remove every `DRAFT`, `PENDING FREEZE`, or equivalent pending-
   freeze marker. If an artifact contains a status or state field, it must not
   remain blank: mark it `REVISED COMPLETE` before hashing.
10. Create `STAGE-A-REVISED-FREEZE-SHA256SUMS`, hashing every completed
    governed revised artifact but not itself or any later record. Verify that
    manifest from the sealed directory and capture the exact verification
    timestamp/timezone. Only then create
    `STAGE-A-REVISED-FREEZE-RECORD.md`. It must describe that already-observed
    verification event and contain the attempt and phase, facilitator and
    actor codes, exact command/stdout/stderr/exit code/time/timezone, later
    record-completion timestamp/timezone, execution-log checkpoint, and every
    governed artifact's literal local
    filename, ID, version, completion timestamp/timezone, completion state,
    and SHA-256 hash, plus the governing manifest's exact filename and hash.
11. Create and verify `STAGE-A-HANDOFF-INPUT-SHA256SUMS`, hashing every revised
    artifact, `STAGE-A-REVISED-FREEZE-SHA256SUMS`, the completed
    `STAGE-A-REVISED-FREEZE-RECORD.md`, and the blank handoff input. Only then
    open and complete the blank
    `05-one-screen-handoff.md`; export it as the exact immutable local filename
    `AG-A-ONE-SCREEN-HANDOFF-v1.md`. List every linked detailed artifact under the
    exact literal frozen filename and record its ID/version and SHA-256. Also
    name and hash
    `STAGE-A-REVISED-FREEZE-RECORD.md` and
    `STAGE-A-REVISED-FREEZE-SHA256SUMS`. Add the handoff's ID/version,
    completion timestamp/timezone, and `HANDOFF COMPLETE` state. Create
    `STAGE-A-HANDOFF-SHA256SUMS`, hashing only the completed handoff; verify it
    and capture the exact verification timestamp/timezone; then create
    `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md`. Do not
    invent an owner, authority, date, number, budget, or evidence source: use
    `UNASSIGNED` or `UNKNOWN` where appropriate and an evidence-based trigger
    when no honest date exists.
    The handoff must contain a nonblank largest unacceptable outcome. It must
    also separate the candidate scope being evaluated from capability that is
    presently authorized by current authority evidence.
12. Complete material feedback, record `STAGE_A_FEEDBACK_COMPLETED`, and then
    record `STAGE_A_ENDED` with the exact Stage A end timestamp/timezone. A
    completed handoff freeze without these events is not a completed Stage A
    route.

The live update in Step 8 intentionally creates the first revised artifact
set. That planned revision is not a post-freeze correction. If any byte changes
after the revised freeze in Step 10, stop. Preserve the old artifact under its
old filename and hash; create a new immutable filename and version; and record
the exact old and new filenames, IDs, versions, hashes, reason, correction
completion and verification timestamps/timezones, replacement freeze-
verification record, and replacement manifest.
Never overwrite or relabel frozen bytes.

## Stage B — exact read and work order

1. Complete and verify the selected same-branch Stage B context gate before
   scored work. The synthetic branch reuses the exact immutable synthetic
   context record; the human branch uses the Stage B participant's separately
   completed consent record.
2. Immediately before first reading this route, record `STAGE_B_STARTED` and
   the exact Stage B start timestamp/timezone in the decision-owner workbook
   and facilitator log.
3. Read this route. Before the handoff is opened, verify
   `STAGE-B-PHASE-1-INPUT-SHA256SUMS`, which hashes the handoff, its governing
   manifest and detached record, this route, and the blank workbook. Then
   receive `AG-A-ONE-SCREEN-HANDOFF-v1.md` as the first scored content. Do not
   receive the scenario or detailed artifacts yet.
4. Open `04-decision-owner-workbook.md`. Complete Section 1 and export
   `STAGE-B-SECTION-1-v1.md` with ID/version, completion
   timestamp/timezone, and `SECTION 1 COMPLETE`. Create and verify
   `STAGE-B-SECTION-1-SHA256SUMS`; only then create
   `STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md`, without Stage A
   explanation or repair.
   While Section 1 is frozen, every field that depends on the still-withheld
   scenario, revised artifacts, or revised freeze evidence must say exactly
   `NOT RELEASED — PHASE 2 CHECK`; do not leave it blank, infer it from the
   handoff, or call it verified.
5. Receive `02-scenario-and-task.md`; every handoff-linked detailed artifact
   under the exact literal filename in the handoff; the detached
   `STAGE-A-REVISED-FREEZE-RECORD.md`; and the governing
   `STAGE-A-REVISED-FREEZE-SHA256SUMS`. Verify the record and manifest before
   reading detail. Do not accept a renamed, regenerated, summarized,
   substituted, or omitted artifact. Record every exact local filename, ID,
   version, hash, record, manifest, and route. A mismatch is a deviation and
   stop.
6. Verify `STAGE-B-PHASE-2-INPUT-SHA256SUMS`, which hashes the Section 1
   artifact, governing manifest, detached record, scenario, every revised
   detail, revised governing manifest, and revised detached record. Complete
   and export `STAGE-B-SECTION-2-v1.md` with ID/version, completion
   timestamp/timezone, and `SECTION 2 COMPLETE`. Create and verify
   `STAGE-B-SECTION-2-SHA256SUMS`; only then create
   `STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md` before opening either
   executive file.
7. Receive `EXECUTIVE-DECISION-BRIEF.md` and
   `VALUE-AND-EVIDENCE-LEDGER.md`. Verify
   `STAGE-B-PHASE-3-INPUT-SHA256SUMS`, which hashes the Section
   2 artifact, governing manifest, detached record, and both executive files.
   Only then open the two executive files in that order and complete Sections
   3 through 5. Export `STAGE-B-SECTIONS-3-5-v1.md` with ID/version, completion
   timestamp/timezone, and `SECTIONS 3-5 COMPLETE`. Create and verify
   `STAGE-B-SECTIONS-3-5-SHA256SUMS`; only then create
   `STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md`.
8. After the Sections 3–5 detached record is complete, record `SCORING_ENDED`.
   Only then create and verify `STAGE-B-DEBRIEF-INPUT-SHA256SUMS` over the
   frozen Sections 3–5 artifact, its governing manifest, its detached record,
   and the exact blank `06-section-6-debrief.md`. Release and open that debrief
   input only after the manifest verifies. Complete Section 6 as
   `STAGE-B-SECTION-6-DEBRIEF-v1.md` with artifact ID/version,
   completion timestamp/timezone, and `DEBRIEF COMPLETE`. Only during this
   post-scoring debrief may Stage A explain anything. The explanation must not
   rewrite or upgrade frozen scored bytes or scores. Record `DEBRIEF_COMPLETED`
   and then `STAGE_B_ENDED` with the exact Stage B end time.

Every governed output records completion before hashing. Its manifest hashes
only completed governed files, never itself or the later detached record.
Verification captures the exact timestamp/timezone before that record is
written. The next phase-input manifest hashes the completed output, governing
manifest, detached record, and new inputs. Any correction must preserve the
prior chain and create an immutable replacement set, manifest, observed
verification event, detached record, and next-phase manifest when applicable.
Every detached record uses the required attempt/phase/actor, observed-command,
observed-output, exit, verification-time, later record-completion-time, and
execution-log checkpoint fields. Each event is recorded in the facilitator
log; that log remains outside participant input.

Synthetic route preflight may identify wording or routing defects, but it is
not human consent, practitioner validation, or evidence that the packet is
usable, safe, effective, or valuable.

## Results, log close, and later external closeout

The six scored freeze chains and the full route are separate results. Six
valid detached records establish only **six freeze chains complete**.

After Stage B ends, complete a new immutable run-specific result from the
facilitator template as `AG-RUN-RESULTS-<ATTEMPT-ID>-v1.md`, artifact identity
`AG-RUN-RESULTS` / `v1`, state `RUN RESULTS COMPLETE`. It must include both
stage boundaries, scoring end, debrief, all counts, scores, critical gates,
deviations, layout evidence, and separate protocol/synthetic/layout/human/
real-world states. Record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`. The
results record must not predict the final closed-log hash or a future closeout
timestamp.

Only after results completion may the facilitator append `LOG_CLOSED`,
validate the closed log, and copy it without byte change to `closeout/input`.
Create `AG-RUN-CLOSEOUT-SHA256SUMS` over the closed-log copy and run-results
file. Then create the later external
`AG-RUN-CLOSEOUT-<ATTEMPT-ID>-v1.md` record binding the closed-log hash,
closeout-manifest hash, and run-results hash. Only after this later binding may
the result say **full synthetic route complete**. The external closeout is not
an event retroactively inserted into the already closed log.
