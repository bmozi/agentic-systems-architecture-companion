# Stage A Practitioner Workbook

**Packet:** AG-RV-PILOT-001 version 1.2.4
**Status:** Blank participant record

- Participant code:
- Entry branch: human / synthetic; exactly one
- Exact selected context-record filename and artifact ID/version:
- `STAGE-A-CONTEXT-SHA256SUMS` verification timestamp/timezone and log checkpoint:
- Broad role and experience band, optional:
- Exact Stage A start before first scored read of the packet route, with timezone:
- `STAGE_A_STARTED` log checkpoint sequence/hash:
- Exact Stage A end, with timezone:
- `STAGE_A_ENDED` log checkpoint sequence/hash:
- Frozen supplied-file manifest and route record:

## 1. Recognition before terminology

Complete this section before opening companion assets.

- Who needs what outcome?
- What useful work could be delegated?
- What becomes possible if the action is governable and reconstructable?
- What can go wrong if technical access, model confidence, old memory, and
  current business authority are treated as the same thing?

## 2. Explain it to someone outside the team

In no more than five sentences, explain what the agent may do, what it may not
do, who grants the authority, how much consequence it may accumulate, and how
Cedar Lane can prove what occurred.

## 3. Delegated-action record

- Beneficiary and bounded outcome:
- Candidate proposal scope under evaluation:
- Present authorization and current authority evidence, or `NOT AUTHORIZED`:
- Principal, agent identity, subject, purpose, and protected object:
- Delegated action and withheld actions:
- Authority source, version, validity, expiry, and revocation:
- Memory permitted to influence the action:
- Governed tool request, enforcement point, and receipt:
- Business identity that survives retries and tool calls:
- Accepted, committed, completed, rejected, and unknown meanings:
- Query-before-repeat and correction rule:
- Shared consequence scope across workers, depots, retries, and time:
- Kill authority and queued/in-flight treatment:
- Expansion evidence and reconsideration trigger:

## 4. Budget and consequence evidence

Do not invent a number. `UNKNOWN` is valid. Before supplying a numeric limit,
record the baseline, authority/evidence source, scope, time window, and owner.
Keep these four evidence classes visibly separate.

| Dimension or boundary | Authorized limit and authority evidence, or `UNKNOWN` | Unproved hypothesis and test | Reported exposure, source, and time, or `UNKNOWN` | Observed terminal consequence and evidence, or `UNKNOWN` | Baseline/evidence still required and owner/trigger |
| --- | --- | --- | --- | --- | --- |
| Monetary value | | | | | |
| Orders and suppliers | | | | | |
| Quantity and depots | | | | | |
| Attempts, retries, and workers | | | | | |
| Time/open exposure | | | | | |

## 5. Practitioner incident-authority matrix

Do not infer authority from identity, system access, job title, or availability.
Use `UNASSIGNED` for no assigned owner and `UNKNOWN` for an absent authority
source, expiry, or permission.

| Incident responsibility | Assigned owner or `UNASSIGNED` | Authority source or `UNKNOWN` | Expiry/reconsideration trigger | Explicitly prohibited actions |
| --- | --- | --- | --- | --- |
| Technical containment across identities, tools, queues, and in-flight work | | | | |
| Provider status query and provider contact | | | | |
| Per-order accept, cancel, or correct decision | | | | |
| Finance, fee, reservation, and payment residue | | | | |
| Event correction and consumer acknowledgement | | | | |
| Receiving and inventory reconciliation | | | | |
| Manual supply continuity while automation is held | | | | |
| Incident closure and bounded re-entry | | | | |

## 6. Monday-morning decision

- Smallest useful design or policy change:
- First authority, duplicate, budget, memory, or stop-path failure to test:
- Assigned test owner or `UNASSIGNED`:
- Assigning authority or evidence-based assignment trigger, or `UNKNOWN`:
- Result that would block or reverse the design:

## 7. Live update, four-order register, and revised-artifact completion

Record the update exactly as supplied. The initial artifacts must already be
frozen before revising them. This planned revision after the live update is
not a post-freeze correction.

- Initial artifact IDs/versions:
- Initial governing manifest exact filename: `STAGE-A-INITIAL-SHA256SUMS`
- Initial detached freeze-verification record exact filename:
  `STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md`
- Live-update input manifest exact filename:
  `STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS`
- Exact live update:
- Initial answer now challenged:
- Actions to stop, reconcile, or correct:
- Current authority and memory problem:
- Artifact fields revised:
- Evidence still missing:

Use one row per possible order. `UNKNOWN` is valid. For cancellation state, use
`CANCEL_REQUESTED`, `CANCEL_ACCEPTED`, `CANCELLED`, another evidenced state, or
`UNKNOWN`; one state must not be treated as another.

- `CANCEL_REQUESTED` means a cancellation request was sent.
- `CANCEL_ACCEPTED` means the provider accepted the cancellation request; it is
  not yet evidence that cancellation completed.
- `CANCELLED` requires authoritative evidence that the order reached the
  provider's cancelled state. It does not erase fee, reservation, shipment,
  return, event, receiving, budget, or inventory residue.

| Order / business identity | Acceptance, commitment, and evidence | Cancellation state and evidence | Fee/reservation residue | Shipment/return | Event correction/consumer acknowledgement | Receiving | Budget | Inventory | Closure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Order 1 | | | | | | | | | |
| Order 2 | | | | | | | | | |
| Order 3 | | | | | | | | | |
| Order 4 | | | | | | | | | |

- Revised artifact literal local filenames and IDs/versions:
- Initial-to-revised identity lineage: for each revised artifact, state its
  new current ID/version and the initial ID/version it supersedes. The current
  revised pair must not equal the initial pair:
- Revised artifact state: write `REVISED COMPLETE` only after every intended
  revision is present; do not write `FROZEN` here:
- Scenario-effect statement: write `FICTIONAL REPORTED EFFECTS EXIST;
  REAL-WORLD EXECUTION EVIDENCE DOES NOT` after the live update. Do not write
  `no execution occurred`:

The facilitator creates the detached freeze evidence after the revised bytes
are complete. Before the handoff opens, no revised artifact may contain
`DRAFT`, `PENDING FREEZE`, or an equivalent pending-freeze marker. If an
artifact contains a status/state field, it must say `REVISED COMPLETE`, not
remain blank. The governing manifest
`STAGE-A-REVISED-FREEZE-SHA256SUMS` and the later
`STAGE-A-REVISED-FREEZE-RECORD.md`—not a self-referential field inside this
artifact—govern and document the freeze. The manifest hashes only completed
revised artifacts. After it verifies, the detached record describes that
observed event. Do not put this workbook's own hash or a future verification
timestamp inside the workbook.

## 8. One-screen transfer preparation

Complete and freeze the separate
[One-Screen Decision Handoff](05-one-screen-handoff.md) after the live update.
Do not open it until `STAGE-A-HANDOFF-INPUT-SHA256SUMS` has verified the revised
artifacts, their governing manifest, their detached record, and the blank
handoff. Link each detailed artifact using its exact literal
frozen local filename and ID/version rather than copying every implementation
detail. Name the detached record and governing manifest exactly. Use a date
**or** an evidence-based reconsideration trigger. Never invent an owner,
assigning authority, date, budget, or evidence to make the handoff look full.

- Handoff artifact ID/version:
- Handoff artifact completion timestamp/timezone and `HANDOFF COMPLETE` state:
- Handoff governing manifest filename: `STAGE-A-HANDOFF-SHA256SUMS`
- Handoff detached freeze-verification record filename:
  `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md`
- Revised freeze record filename: `STAGE-A-REVISED-FREEZE-RECORD.md`
- Governing revised manifest filename: `STAGE-A-REVISED-FREEZE-SHA256SUMS`
- Handoff-input manifest filename: `STAGE-A-HANDOFF-INPUT-SHA256SUMS`
- Recommended stop/containment:
- Actual containment execution status and evidence, or `UNKNOWN`:
- Largest unacceptable outcome (required; blank is invalid):
- Candidate scope proposed for evaluation:
- Presently authorized scope and current authority evidence, or `NOT AUTHORIZED`:

If a frozen revised byte later changes, do not call it the planned live-update
revision and do not overwrite it. Stop and preserve both versions. Record the
exact old/new filenames, IDs/versions, hashes, reason, correction timestamp and
timezone, replacement freeze-verification record, and replacement manifest
before any new handoff or attempt. A replacement is a new immutable artifact
set and provenance chain; do not mutate the earlier one.

## 9. Material feedback

- Prompt that changed your thinking:
- Term or field that was unclear:
- Important decision the materials missed:
- Any prompt that pushed you toward an unsupported answer:
- Question, pause, or access problem and exact time:
- What this exercise cannot establish:
- Material-feedback completion timestamp/timezone:
- `STAGE_A_FEEDBACK_COMPLETED` log checkpoint sequence/hash:

The facilitator records `STAGE_A_ENDED` only after these fields are complete.
Completing the handoff freeze does not by itself complete the Stage A route.
