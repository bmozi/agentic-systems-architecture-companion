# Agentic Systems Reader-Value Pilot Packet

**Packet ID:** AG-RV-PILOT-001
**Version:** 1.2.3
**Status:** Prepared and unrun; no participant recruited or consented
**Scenario:** Cedar Lane Supply, entirely fictional

## Version and evidence note

Version 1.2.3 repairs execution-chain and content defects found by the
independent replay of version 1.2.2. Every detached record now carries the
attempt, phase, facilitator/actor codes, exact observed verification
command/output/exit/time/timezone, a later record-completion time/timezone,
and an execution-log checkpoint. A facilitator-side append-only log records
each input gate, release, open, completion, manifest, verification, and record
with exact actor, filename, time, timezone, and hash-linked continuity. It is
never participant input. Undeclared orchestration inputs are forbidden; a
synthetic rehearsal must freeze and verify every orchestration instruction in
a separate declared manifest before use.

Version 1.2.3 also requires revised identities to differ from their initial
ID/version pairs, distinguishes fictional reported effects from real-world
execution evidence, separates a candidate scope from present authorization,
requires the largest unacceptable outcome in the handoff, and makes withheld
Stage B Phase 1 details say `NOT RELEASED — PHASE 2 CHECK` rather than remain
blank. The replay that found these defects remains synthetic, not human
evidence. Version 1.2.3 remains **PREPARED/UNRUN** for human testing.

Version 1.2.2 repaired a temporal self-reference defect in version 1.2.1's
freeze procedure. Governed bytes now record their completion state and time
before hashing. Their governing manifest hashes only those completed bytes and
is then verified at an exact timestamp/timezone. Only after that observed
verification event may the detached freeze-verification record be written.
The manifest never hashes itself or that later record. The next sealed phase-
input manifest hashes the completed artifacts, governing manifest, and
detached record. This sequence now governs initial and revised Stage A artifacts, the
handoff, and all three Stage B freezes. Earlier synthetic regressions were
defect-finding only, not human or practitioner sessions, and establish no
usability, safety, effectiveness, or value result.

Version 1.2.0 had repaired sealed-delivery portability, containment-state
transfer, and auditable Stage B freezes after a synthetic AI regression of
version 1.1.0.

Version 1.1.0 had already repaired route clarity, transfer density, timing
instrumentation, incident authority, order/correction tracking, and numeric-
evidence prompts found in a synthetic preflight of version 1.0.0. Those earlier
synthetic artifacts likewise establish no human result.

The miniature example embedded in the supplied Agent Authority Map was and
remains authorized teaching content. Version 1.0.0 supplied that file as-is;
this repair does not reinterpret the earlier packet as an unaided-derivation
test. Linked full worked examples remain withheld. A future test of unaided
derivation would require a separately versioned packet that removes all
teaching examples explicitly.

## What this packet tests

This packet tests whether the Agentic Systems companion helps a reader move
through the complete value chain:

`RECOGNIZE USEFUL DELEGATION -> BOUND ONE ACTION -> GOVERN THE TOOL ->`
`LIMIT CUMULATIVE CONSEQUENCE -> HANDLE FAILURE -> PROVE WHAT OCCURRED ->`
`HAND OFF A DECISION`

It does not replace the advanced Glasswing technical-transfer packet. That
packet keeps its detailed six-template scope. This packet separately tests the
accessible reader routes, first authority map, action budget, value ledger, and
executive decision language.

## Two stages

### Stage A — practitioner

Build a sealed, flat Stage A delivery directory and supply only exact immutable
copies of these files. Keep the filenames shown here; do not substitute links
back to a working repository:

1. [Consent and privacy notice](participant/01-consent-and-privacy.md)
2. [Exact packet route](participant/00-packet-route.md)
3. [Scenario and task](participant/02-scenario-and-task.md)
4. [Practitioner workbook](participant/03-practitioner-workbook.md)
5. [Start Here](../../START-HERE.md), delivered as `START-HERE.md`
6. [Agent Authority Map](../../agent-authority-map.md), delivered as
   `agent-authority-map.md`
7. [Governed Tool Contract](../../governed-tool-contract.md), delivered as
   `governed-tool-contract.md`
8. [Action Budget and Blast-Radius Worksheet](../../action-budget-and-blast-radius.md),
   delivered as `action-budget-and-blast-radius.md`
9. [One-Screen Decision Handoff](participant/05-one-screen-handoff.md)

Follow the route exactly: recognition comes before companion assets; the
initial detailed artifact is frozen before the live update; the revised
detailed artifacts are sealed under immutable, literal local filenames after
the update; and only then may the one-screen handoff be opened, completed, and
frozen. After every revised artifact is `REVISED COMPLETE`, the governing
`STAGE-A-REVISED-FREEZE-SHA256SUMS` hashes only those completed artifacts.
Verify that manifest, capture the exact timestamp/timezone, and only then
create `STAGE-A-REVISED-FREEZE-RECORD.md` with the observed verification event,
artifact IDs, versions, filenames, hashes, and manifest filename/hash. Then
create `STAGE-A-HANDOFF-INPUT-SHA256SUMS`, which hashes the revised artifacts,
their manifest, the detached record, and the blank handoff. The miniature
example embedded in the Agent Authority Map is authorized and may be read. Do
not follow its links to full worked examples, or supply the repository Failure
Lab, facilitator materials, executive brief, value ledger, or any omitted file
during Stage A.

### Stage B — independent decision owner

Build a sealed, flat Stage B delivery directory and supply exact immutable
copies with the filenames shown below. Supply them in the route's phases:

1. [Consent and privacy notice](participant/01-consent-and-privacy.md);
2. [Exact packet route](participant/00-packet-route.md);
3. the completed [One-Screen Decision Handoff](participant/05-one-screen-handoff.md),
   delivered as `AG-A-ONE-SCREEN-HANDOFF-v1.md`, as the first scored content;
4. `STAGE-A-HANDOFF-SHA256SUMS`,
   `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md`, and the
   [Decision-owner workbook](participant/04-decision-owner-workbook.md);
5. the frozen scenario; every detailed artifact named and linked in the
   handoff under that exact literal local filename; the detached
   `STAGE-A-REVISED-FREEZE-RECORD.md`; and its governing
   `STAGE-A-REVISED-FREEZE-SHA256SUMS` manifest;
6. [Executive Decision Brief](../../EXECUTIVE-DECISION-BRIEF.md), delivered as
   `EXECUTIVE-DECISION-BRIEF.md`; and
7. [Value and Evidence Ledger](../../VALUE-AND-EVIDENCE-LEDGER.md), delivered as
   `VALUE-AND-EVIDENCE-LEDGER.md`.

Use a different person for Stage B during the first calibration round. Do not
let the Stage A participant explain or repair the artifact during the initial
read-back. Complete, manifest, verify, and document Section 1 with a later
detached record before supplying detailed artifacts. Apply the same sequence
to Section 2 before supplying the executive brief or value ledger, and to
Sections 3-5 before debrief. Every next phase-input manifest hashes the prior
completed output, its manifest, its detached record, and newly released
inputs. Supply no other files or omitted links.

Do not rename, summarize, regenerate, substitute, or omit a handoff-linked
detail. A route or manifest mismatch is a recorded deviation and stop, not a
file-access problem to repair silently.

For each stage, create a run-specific SHA-256 manifest that covers every exact
file supplied, including each of the six companion assets assigned to that
stage above. Verify the manifest before the participant starts and retain it
with the run. Treat the delivered bytes as immutable. If any supplied byte
changes, stop, preserve the earlier evidence, record the exact change, and
issue a new timestamp and hash; a meaning change also requires a new packet
version.

The planned revision after the facilitator's live update is part of the Stage
A procedure: it produces the first revised freeze and is not a post-freeze
correction. A later change to any already frozen byte is a correction. It must
use a new immutable filename and artifact version and record the exact old and
new filenames, versions, hashes, reason, completion and verification
timestamps/timezones, replacement freeze-verification record, and replacement
manifest. Never overwrite the earlier artifact or reuse its filename.
Operational correction in the four-order register means reconciling an order,
event, budget, receiving, or inventory consequence; it does not authorize a
change to frozen evidence bytes.

## Facilitator only

- [Facilitator guide](facilitator-only/01-facilitator-guide.md)
- [Observation and scoring rubric](facilitator-only/02-observation-and-scoring-rubric.md)
- [Results and deviation log](facilitator-only/03-results-and-deviation-log.md)
- [Freeze and correction record templates](facilitator-only/04-freeze-and-correction-record-templates.md)
- [Execution and access log](facilitator-only/05-execution-and-access-log.md)
- [Execution-log entry schema](facilitator-only/05-execution-access-log-schema.json)

Never supply these files before either scored stage ends.

## Execution prerequisites

Before recruitment:

1. assign an accountable execution owner;
2. approve storage, access, retention, redaction, and deletion;
3. decide whether further ethics, legal, privacy, or organizational review is
   required;
4. copy the exact files into sealed, flat stage-delivery directories and freeze
   every supplied byte;
5. record SHA-256 values in a run-specific evidence manifest;
6. keep scheduling identity separate from participant codes; and
7. assign a facilitator and evaluator with disclosed relationships.

Before any run, also create the facilitator-side execution/access log. It is
not supplied to participants and is not a member of a scored phase-input
manifest. It records the exact order of every admitted input, release, open,
completion, manifest, verification, and detached-record event. Each detached
record checkpoints the log through the governing-manifest verification it
describes; the next release and later log entries continue the chain.

For a synthetic rehearsal, preserve every additional system, developer, user,
tool, or orchestration instruction as immutable bytes, list it in
`ORCHESTRATION-INPUT-SHA256SUMS`, verify that manifest before delivery, and
record the event in the facilitator log. An undeclared input is a stop and new
attempt, not an omission to repair after the fact.

The checked-in `SHA256SUMS` records the prepared source packet. It does not
cover companion assets stored outside this packet. Each run-specific manifest
must hash every exact delivered file, including those companion assets, under
its delivery filename. Any byte change requires a new timestamp and hash and,
when meaning changes, a new packet version.

A manifest cannot truthfully hash itself or a record created after its
verification. Every governing manifest hashes only already-completed governed
artifacts. A detached freeze-verification record is created after manifest
verification. The next-stage delivery manifest hashes the prior artifacts,
their governing manifest, and that completed detached record as supplied
files.

## Temporal sealing rule

[`TEMPORAL-FREEZE-PROTOCOL.json`](TEMPORAL-FREEZE-PROTOCOL.json) is the
machine-readable canonical inventory for the six output freezes, five
next-release triples, completion states, correction rules, artifact bindings,
and results rows. Reader-facing instructions must agree with that inventory;
the repository validator also checks reviewed protocol-document hashes so a
prose change cannot silently bypass structural review.

For initial and revised Stage A, the handoff, and each Stage B output:

1. complete the governed artifact with ID, version, exact completion
   timestamp/timezone, and required `COMPLETE` state;
2. create a manifest hashing only those completed governed artifacts;
3. verify the manifest from sealed storage and capture the exact verification
   timestamp/timezone; and
4. write the detached freeze-verification record describing that observed
   event. It must include attempt ID, phase, facilitator and actor codes,
   literal filenames, IDs, versions, artifact hashes, the manifest filename
   and hash, the exact verification command/stdout/stderr/exit code/time/
   timezone, the execution-log checkpoint, and an explicit later record-
   completion timestamp/timezone.

The next phase-input manifest hashes the completed artifact, governing
manifest, detached record, and newly released inputs. See
[`TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md`](TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md)
and the facilitator-only freeze templates. This static repair changes no
human-testing state.

## Evidence boundary

A completed pair can reveal wording defects, unsafe interpretations, transfer
failures, and useful behavior for the exact participants and materials. It
cannot prove agent safety, runtime enforcement, business value, broad
usability, or publication readiness.
