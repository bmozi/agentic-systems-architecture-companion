# Observation and Scoring Rubric

**Packet:** AG-RV-PILOT-001 version 1.2.4
**Status:** Predetermined, blank, and unrun

Score retained behavior, not agreement with preferred vocabulary.

## Scale

- **2 — unaided and defensible:** explicit, coherent, and reached with L0–L1.
- **1 — partial or prompted:** material issue appears but is incomplete or
  requires L2–L3.
- **0 — absent, contradicted, unsafe, or coached:** missed, invented, unsafe,
  or supplied by L4.
- **NA — not interpretable:** missing or materially contaminated evidence.

Do not use the total as a validated psychometric score.

## Seven reader-value gates

| Gate | Observable evidence | Stage | Score | Evidence location |
| --- | --- | --- | ---: | --- |
| RV-1 Recognition | Names useful delegation and human consequence before mechanisms | A | | |
| RV-2 Plain understanding | Explains delegated and withheld action, authority, limits, and proof without agent jargon | A and B | | |
| RV-3 First useful artifact | Produces a bounded authority record with explicit unknowns | A | | |
| RV-4 Outside read-back | From separately completed, manifested, verified, and recorded Sections 1 and 2, Stage B reconstructs value, authority, limits, failure, recommended containment, actual containment status, and proof without repair | B | | |
| RV-5 Failure discovery | Detects stale memory, absent delegation, unknown outcome, duplication, and budget escape | A | | |
| RV-6 Team transfer | One-screen handoff separates candidate and presently authorized scope and yields decision, allowed/withheld scope, assigned owner or `UNASSIGNED`, assigning authority/trigger or `UNKNOWN`, evidence, unknowns, required largest unacceptable outcome, recommended stop/containment, actual containment execution status or `UNKNOWN`, next action, and date or evidence-based trigger without invention | B | | |
| RV-7 Decision-owner legibility | Selects a bounded state without inventing ROI, approval, or safety | B | | |

## Critical Agentic Systems gates

Mark `clear`, `unclear`, `unsafe`, or `contaminated`:

| Gate | Clear behavior | Result | Evidence |
| --- | --- | --- | --- |
| Delegated authority | Separates service identity, model ability, memory, and current institutional permission | | |
| Action boundary | Names one permitted action and explicitly withheld actions and substitutions | | |
| Governed tool | External enforcement, business identity, outcome meanings, and receipts survive tool calls | | |
| Cumulative consequence | Shared scope covers workers, depots, retries, ambiguity, orders, and spend while authorized limits, hypotheses, reported exposure, and observed terminal consequence stay separate; unsupported numbers remain `UNKNOWN` | | |
| Stop and correction | Separates recommended stop/containment from evidenced execution; unevidenced execution remains `UNKNOWN`; kill authority reaches queued and in-flight work; committed effects are reconciled and corrected | | |
| Evidence | Source, memory, authority, decision, tool, order, event, cancellation, shipment, and inventory can be joined | | |
| Incident authority | Names owner, authority source, expiry/trigger, and prohibited actions for containment, provider contact, per-order decisions, finance, event correction, receiving/inventory, manual continuity, and closure; honest `UNASSIGNED`/`UNKNOWN` remains acceptable | | |
| Four-order correction | Keeps all four possible orders distinct through `CANCEL_REQUESTED`, `CANCEL_ACCEPTED`, `CANCELLED`, residue, shipment/return, event acknowledgement, receiving, budget, inventory, and closure; `UNKNOWN` is not closure | | |
| Handoff scanability | Stage B can locate value, decision, allowed/withheld scope, ownership/authority gaps, evidence, unknowns, recommended containment, actual containment status, next action, and reconsideration on one screen; any favorable local one-page claim is separately supported by the completed layout proof | | |

## Stage B sequence integrity

Mark each condition `clear`, `deviated`, or `not interpretable`:

| Condition | Result | Evidence |
| --- | --- | --- |
| The facilitator-side JSON Lines log used one attempt ID, contiguous sequence and continuity hashes, one exact filename per event, and ordered input gates, releases, opens, completions, manifests, verifications, records, and phase completions | | |
| No participant received an undeclared input; any synthetic orchestration was frozen, declared, verified, and logged before use and the result was labeled orchestration-aided | | |
| Every detached record included attempt, phase, facilitator/actor codes, verbatim observed command/stdout/stderr/exit/time/timezone, later record-completion time/timezone, manifest/artifact bindings, and execution-log checkpoint | | |
| Section 1 was completed, manifested, verified, and documented by a later detached record before scenario or detail access | | |
| Section 1 recorded `NOT RELEASED — PHASE 2 CHECK` for revised freeze evidence, detailed files, and detailed execution evidence, and the frozen artifact was not retroactively edited | | |
| Revised Stage A details were complete before hashing; their manifest was verified before the detached verification record was written; and the handoff-input manifest then carried artifacts, manifest, record, and blank handoff | | |
| Detached record describes the observed manifest-verification timestamp/timezone and includes every governed artifact's literal filename, ID/version, completion time/state, and SHA-256 plus the manifest filename/hash | | |
| No governing manifest hashes itself or its later detached record; no governed output embeds its own hash or a future verification time | | |
| No revised artifact retained `DRAFT`, `PENDING FREEZE`, or an equivalent pending-freeze claim after the detached freeze; any existing status/state field was nonblank and `REVISED COMPLETE` before hashing | | |
| Every revised output's current ID/version pair differed from its initial pair; initial identity appeared only as explicit lineage | | |
| Candidate scope remained separate from presently authorized scope; no proposal, technical access, model confidence, or recommendation was treated as current authority | | |
| The handoff's largest unacceptable outcome was nonblank, and fictional reported effects were not contradicted by “no execution occurred” wording or promoted into real-world evidence | | |
| Stage B received every handoff-linked detail under its exact literal filename plus `STAGE-A-REVISED-FREEZE-RECORD.md` and `STAGE-A-REVISED-FREEZE-SHA256SUMS`, with no rename, substitution, regeneration, summary, or omission | | |
| Section 2 was completed, manifested, verified, and documented by a later detached record before executive brief or value ledger access | | |
| Sections 3–5 were completed, manifested, verified, and documented by a later detached record before Section 6 or Stage A explanation | | |
| Each next phase-input manifest hashes the prior completed output, its governing manifest, its detached record, and newly released inputs | | |
| Planned live-update revision was distinguished from any later correction of already frozen bytes | | |
| Every post-freeze correction preserved the prior chain and created an immutable replacement artifact set, manifest, observed verification event, detached record, and next-phase manifest when applicable | | |

## Full-route protocol integrity

These closure checks are not additional scored freeze chains. Mark each
`clear`, `deviated`, or `not interpretable`:

| Condition | Result | Evidence |
| --- | --- | --- |
| Exactly one run-specific entry branch was selected: human consent or synthetic context, never both and never neither | | |
| A synthetic attempt used `AG-SYNTHETIC-CONTEXT-<ATTEMPT-ID>-v1.md`, made no fictional consent claim, and was not entered as a human result | | |
| `STAGE_A_STARTED` followed the verified Stage A context manifest, and `STAGE_A_FEEDBACK_COMPLETED` and `STAGE_A_ENDED` followed the three Stage A scored freezes | | |
| `STAGE_B_STARTED` followed the verified Stage B context manifest, and the three Stage B scored freezes ended before `SCORING_ENDED` | | |
| Section 6 was admitted by a verified debrief-input manifest only after scoring ended; `DEBRIEF_COMPLETED` and `STAGE_B_ENDED` were then logged | | |
| Immutable run-specific results were completed and hashed before `RUN_RESULTS_COMPLETED`, and `LOG_CLOSED` occurred later | | |
| Neither results nor log predicted or embedded the future final log hash; a later external closeout record binds the observed closed-log hash to the immutable results hash and timestamps | | |
| The six scored freeze chains and the full-route boundaries are reported separately | | |

## One-page layout proof boundary

A favorable local `LAYOUT PASSED` statement requires the run-specific layout
proof to show one US Letter page, margins of at least 0.5 inch, reader-facing
type of at least 9 point, no more than 450 reader-facing words excluding
provenance, and no clipping or overlap. A layout pass is not evidence of
comprehension, scanability behavior, usefulness, safety, business value, or a
human result. Score those claims only from the separately admitted behavioral
evidence.

Any unsafe critical gate blocks a favorable interpretation regardless of total.

For RV-6 and every critical gate, never reward invented data. An explicit
`UNASSIGNED`, `UNKNOWN`, or evidence-based reconsideration trigger can be
unaided and defensible. A plausible but unsupported owner, authority, date,
budget, limit, order state, or evidence source scores 0 for the affected
behavior.

## Findings to record

- exact prompt and participant words;
- initial and revised interpretation;
- intervention level;
- wording or route that caused friction;
- useful behavior to preserve;
- likely source: material, scenario, participant, facilitator, or unresolved;
- severity and proposed disposition; and
- regression condition for any change.

## Interpretation

Use only bounded language: complete, partial, materially unclear, unsafe, or
inconclusive for this participant, version, scenario, and stage. Do not claim
broad usability, correctness, safety, or benefit.
