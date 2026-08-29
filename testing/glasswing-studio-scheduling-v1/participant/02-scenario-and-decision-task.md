# Glasswing Studio-Scheduling Scenario and Decision Task

<!-- markdownlint-disable MD013 -->

**File ID:** AGENTIC-TEST-GAC-SCENARIO-001
**File version:** 1.0.1-candidate
**Packet:** AGENTIC-TEST-GAC-001 version 1.0.1-candidate
**Artifact state:** IN_PROGRESS; fictional participant fixture
**Test execution state:** `PLANNED/UNRUN`
**Recommended participant role:** Enterprise, solution, security, platform, or
AI architect; AI product or governance practitioner; or equivalent
**Timebox:** `NOT_YET_DECIDED`; the authorized execution owner must declare it
before use

## Disclosure

Glasswing Arts Cooperative, every role, system, policy, record, identifier,
quantity, message, action, outcome, and recovery proposal below are
constructed. Nothing is observed history, a practitioner result, an experiment
result, a real incident, a safety or legal conclusion, or John Briggs's
experience.

## Your task

Glasswing is considering one bounded autonomy change for its fictional studio-
scheduling assistant. Decide whether the proposed change should be approved,
restricted, or rejected on the supplied scenario facts. Choose the **smallest
useful subset** of the six canonical companion templates. Do not fill a
template merely because it is available.

For each selected asset, state the distinct decision it records, the scenario
evidence it uses, what remains unknown or unrun, and the stop, escalation, or
reconsideration trigger. Account for every fixture group even when it is
excluded from a selected template or preserved as a separate disposition.

The proposed change is:

> Permit `GAC-AGENT-STUDIO-01` to place one short-lived tentative studio hold
> for a current internal program request after preparing a schedule. A hold is
> not a confirmed booking, fee decision, room-access grant, equipment approval,
> external communication, or authorization for onward delegation.

The participant may make only a `SCENARIO DECISION` about the constructed
proposal. This task cannot grant authority, change a policy, execute a tool,
approve a release, clear an incident, or transition an experiment.

## Canonical working assets supplied

Use exact unchanged copies of these files. The hashes pin the candidate packet
to the current source bytes; they do not prove that a template works.

| Canonical asset | Template version | SHA-256 |
| --- | --- | --- |
| [Agent Authority Map](../../../agent-authority-map.md) | 0.2-template | `9948d63664ff56f598cd0842b636e581cb83cc3d301a5dd017d77c2629a2f15a` |
| [Governed Tool Contract](../../../governed-tool-contract.md) | 0.2-template | `52d574fdc56434e6bc32e83c8b5403d80536e7b1b3a077dbfaf848414ed02eb4` |
| [Memory and Provenance Record](../../../memory-and-provenance-record.md) | 0.2-template | `27cbfe0c596f1d482cc9d4e74d18d55bc4bf91063db1b73498a5fed859c7a55a` |
| [Action Budget and Blast-Radius Worksheet](../../../action-budget-and-blast-radius.md) | 0.1-template | `dfb70615c37c1917ff7e32c836ee45860268147aa7af2bd7bb580553eb531bf0` |
| [Autonomy Evidence Gate](../../../autonomy-evidence-gate.md) | 0.1-template | `67cf1d908e6aa7d98745d84913b79c228cfbee04103d3218973cab9932960b43` |
| [Agentic Incident Readiness Plan](../../../agentic-incident-readiness-plan.md) | 0.1-template | `26d2dea9ee8a92ab1df0d8ec066386730b80ec1e4da263b8f98638ea85d86f56` |

Record selection and decisions in the [response workbook](03-response-workbook.md).

## Scenario context

Glasswing is a fictional community-arts cooperative. Internal program teams
request studios for workshops. A human scheduling lead currently reviews each
request, checks room and equipment constraints, places or confirms any hold,
and decides whether a message may leave the cooperative.

`GAC-AGENT-STUDIO-01` currently reads a frozen copy of a request and public
availability, then drafts a non-authoritative schedule for the lead. It has a
technical service identity that can reach the scheduling gateway, but the
scenario provides no accepted delegation record allowing it to place a hold.
The proposal would add that one action for case `GAC-CASE-204` and equivalent
eligible internal requests.

The review package contains five fixture groups.

### A. Operating proposal

- Accountable business role for studio scheduling: `GAC-ROLE-SCHEDULING`.
- Technical service identity: `svc:gac-studio-assistant`.
- Protected object: the exact program request, candidate slot, studio, and
  tentative-hold record.
- Declared purpose: prepare one internal studio schedule and, if separately
  authorized, place one short-lived tentative hold for that same request.
- Current allowed behavior: read scoped availability and draft a schedule for
  human review.
- Proposed additional behavior: place one 20-minute tentative hold.
- Actions outside the proposal: confirm or cancel a booking; set or waive a
  fee; override capacity, equipment, accessibility, or supervision rules;
  unlock a room; send an external message; modify the program request; or
  delegate the action to another agent.
- The scheduling gateway can authenticate the service identity. The scenario
  does not identify an accepted authority-source version, completed delegation
  chain, or immutable decision receipt for the proposed hold.
- Candidate policy decision point: `GAC-PDP-SCHED-02`.
- Candidate enforcement point outside the model:
  `GAC-PEP-SCHED-GATEWAY-02`.
- Proposed authority receipt shape:
  `AUTHZ-GAC-<case>-<operation>-<sequence>`.
- Candidate authority owner, effective interval, revocation service-level
  expectation, and treatment of queued work are `NOT_YET_DECIDED`.

### B. Capability interface

Scenario record `GTC-GAC-HOLD-004` version 1.3.0 has artifact state `REVIEWED`
and test execution state `PLANNED/UNRUN`. It describes
`studio_schedule.place_tentative_hold` for the proposed agent caller.

The scenario record states:

- original principal, agent identity, case, purpose, slot, policy version,
  authority receipt, and memory-use receipts must reach the external policy
  enforcement point;
- allowed request fields are case code, slot ID, studio code, hold duration,
  and business-operation ID;
- organizer notes, contact details, payment data, access codes, and free-text
  retrieved content are prohibited tool arguments and prohibited egress;
- business-operation identity is
  `gac:case:<case>:slot:<slot>:tentative-hold:v1`;
- `Accepted` means only that the request entered processing;
- `Completed` plus a resolvable hold receipt means one tentative hold exists;
- `Rejected` and `Conflict` do not permit an automatic alternate action;
- `Ambiguous/unknown` requires a status query by business-operation identity;
  it is neither success nor failure and forbids a repeat until reconciled;
- a notice may be drafted only after a reconciled `Completed` result, and this
  scenario gives the agent no authority to send it;
- revocation is intended to reach the delegated token, policy cache,
  enforcement point, scheduling queue, and unresolved operations; and
- no policy, duplicate, timeout, reconciliation, egress, revocation, or runtime
  enforcement test has run.

Treat the record as a supplied scenario fact. Decide whether it is sufficient
for the proposed change, requires a revision, or can be referenced without a
new Governed Tool Contract.

### C. Reference material

The current fictional studio policy is `GAC-POL-STUDIO-09` version 5,
effective 2026-08-15. For mobile-sculpture workshops it permits only studio S3
as a scheduling candidate and requires a human equipment review before any
booking confirmation.

Derived item `MEM-GAC-118` was built from policy version 4. It says S2 and S3
are candidates. Retrieval snapshot `GAC-INDEX-SCHED-07` was built on
2026-08-10 and still returns `MEM-GAC-118` for case `GAC-CASE-204`, whose
request declares mobile-sculpture equipment. Correction record
`GAC-CORR-POL-09-V5` names version 5, but its declared descendant list omits
`MEM-GAC-118` and the retrieval snapshot.

The candidate context order places the derived summary before the signed
policy excerpt. The request description follows as `UNTRUSTED` data. The
scenario provides no stable use-event receipt, no executed revalidation, and
no evidence that in-flight drafts or holds are found after a correction.
Provider/model/version is `NOT_YET_DECIDED`; disclosed knowledge-cutoff
metadata is `UNKNOWN`.

### D. Message and timing sequence

The proposed action graph uses causal fact `GAC-FACT-204`. For the exercise,
the authored delivery fixture contains:

- two deliveries of the same `studio.request.updated` fact;
- two proposed workers, `slot-planner` and `accessibility-planner`, each able
  to receive both deliveries;
- up to three candidate-slot attempts by each worker before it sees a
  reconciled outcome; and
- one possible review-notice draft after each locally interpreted successful
  result.

Those inputs create twelve candidate tool-attempt opportunities before shared
case controls are applied: two deliveries multiplied by two workers multiplied
by three slots. This is scenario arithmetic, not an observed system count,
prediction, accepted threshold, or experiment result.

The scheduling role supplies these hard scenario boundaries:

- no more than one active tentative hold per case;
- no more than two tentative-hold attempts for the case in one hour, including
  retries and every worker;
- no more than one internal review-notice draft per case;
- zero external messages, booking confirmations, fee actions, access grants,
  or onward delegations by the agent;
- a hold must expire after 20 minutes unless a human takes responsibility;
- a shared causal identity and shared case counter must cover every worker and
  delivery; and
- exhaustion, counter ambiguity, or an unavailable breaker stops new attempts
  and routes the case to the scheduling lead.

Counter reservation, simultaneous workers, crash recovery, timeout after
acceptance, breaker behavior, revocation propagation, and correction of an
erroneous hold are all `PLANNED/UNRUN` scenario requirements.

### E. Release and recovery records

Candidate release record `GAC-REL-HOLD-006` has state `RESTRICTED`. Its
supporting list records:

| Evidence area | Supplied state |
| --- | --- |
| Meaning and authority review | `NOT_YET_DECIDED`; no accountable delegation record |
| Tool contract review | Scenario record present; all tests `PLANNED/UNRUN` |
| Context and memory fitness | Version conflict and omitted descendants present; correction test `PLANNED/UNRUN` |
| Duplicate, retry, and loop behavior | Fixture specified; no execution |
| Misuse and data-release behavior | Tests `PLANNED/UNRUN` |
| Outcome evaluation | `PLANNED/UNRUN` |
| Human-review capacity | `UNKNOWN`; accountable owner not assigned |
| Incident exercise | `PLANNED/UNRUN` |

The record proposes initial exposure to internal case `GAC-CASE-204`, but the
scenario contains no accepted exposure decision, rollback owner, monitoring
window, or retained result.

A separate constructed recovery proposal, `GAC-RESET-017` version 0.1, says:

> If a derived policy summary directs a hold attempt and the gateway returns
> `Accepted` before a timeout, stop model inference, revoke the model service
> credential, clear the worker queue, reset all counters to zero, and restart
> draft-only operation.

No tabletop or technical check has run. The proposal does not state how to
reconcile the accepted operation, reach the delegated token or policy cache,
identify queued and downstream work, preserve the action and memory-use trace,
invalidate derived descendants, find affected and unaffected cases, correct a
hold, assign communication, or decide a bounded re-entry gate.

## Separate unresolved decisions

- `GAC-AUTH-HOLD-007` — delegation for the proposed tentative hold;
  accountable decision owner `NOT_YET_DECIDED`.
- `GAC-REL-HOLD-006` — system release for the proposed hold path; current state
  `RESTRICTED`.
- `GAC-OPS-STUDIO-004` — room, equipment, accessibility, supervision, and
  physical-use decision; outside this agentic review.
- `GAC-PRIV-COMMS-002` — external communication and personal-data decision;
  outside this proposal and unresolved.

This exercise cannot change any of those decisions. It cannot create a real
authority grant or convert an asset review into runtime, release, safety,
privacy, legal, or outcome evidence.

## Constraints

- Do not treat authentication or a callable interface as delegated business
  authority.
- Do not infer that a record marked `REVIEWED` is accepted for release or
  enforced at runtime.
- Keep technical response, reconciled business outcome, authority decision,
  and release decision separate.
- Preserve source/version conflict, omissions, unknowns, unrun checks,
  ambiguous outcomes, and separate gates rather than silently repairing them.
- Apply value, rate, reach, time, and cumulative limits across the complete
  case, not only one agent or worker.
- Do not reset counters or re-enter merely because model inference stopped.
- Use `NOT_APPLICABLE`, `UNKNOWN`, or `NOT_YET_DECIDED` with reasons and owners
  instead of leaving required fields empty.
- Do not invent policy, consent, delegation, execution, test, safety, legal,
  privacy, capacity, or business facts.

## No-coaching rule

Once the timed attempt begins, the facilitator may clarify file location,
restore access to exact frozen bytes, or restate written instructions verbatim.
The facilitator may not recommend an asset, interpret a field, identify a
fixture problem, name an expected disposition, disclose the withheld route or
scoring categories, or confirm correctness. Record all questions and supplied
help. Stop on unblinding, fixture drift, missing consent, confidentiality risk,
loss of independence, or material tool failure.

## Deliverable

Submit one response workbook plus completed copies of only the templates you
selected. Do not overwrite the blank canonical templates or source fixtures.
Give every output a participant-assigned artifact ID and version. Label every
conclusion `SCENARIO DECISION`, every absent test or observation
`PLANNED/UNRUN`, and every unresolved value `UNKNOWN` or `NOT_YET_DECIDED` as
appropriate.
