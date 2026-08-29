# Supplementary Cross-Asset Views

**Status:** Working supplementary views; not canonical assets

**Artifact state:** IN_PROGRESS

**Test execution state:** PLANNED/UNRUN

These views join fields already owned by the six canonical companion assets.
They close a narrative handoff without creating a seventh or eighth canonical
tool. Practitioner testing may later show that a separate worksheet is needed;
that outcome has not been observed.

## View 1: Workflow handoff record

Use when an agent decision enters a durable path. The agent can propose or
submit work, but the workflow owns custody, progress, and completion across
time, failure, and human judgment.

### Workflow handoff metadata

| Field | Value |
| --- | --- |
| View ID/version | Assign `WHR-<system>-<nnn>` / version |
| Owner | Unassigned |
| Case/capability | Unassigned |
| Artifact state | BLANK |
| Evidence references | Link authority map, tool contract, workflow, tests, and outcome receipts |
| Decision date | NOT_YET_DECIDED |
| Supersedes / superseded by | None |
| Reconsideration trigger | Custody, deadline, approval, compensation, or completion rule changes |

### Durable custody

| Field | Decision or evidence |
| --- | --- |
| Agent decision artifact and authority-map row | |
| Agent-side responsibility ending point | |
| Workflow identity and accountable responsibility owner | |
| Durable state/checkpoint accepted | |
| Business-operation/idempotency identity | |
| Deadline, timeout, and escalation owner | |
| Human approval and information packet | |
| Retry and ambiguous-outcome reconciliation | |
| Compensation or correction obligation | |
| Completion meaning and completion evidence | |
| In-flight revocation behavior | |
| Evidence limit and known custody gap | |

### Northbridge workflow-handoff worked view

**Provenance:** `COMPOSITE`; constructed teaching fixture, not a transcript or
observed outcome.

| Field | Constructed entry |
| --- | --- |
| View ID/version | WHR-NBX-CREDIT-001 / 0.1 |
| Agent decision artifact and authority-map row | Draft-credit recommendation `DEC-NBX-1042`; AAM-NBX-CREDIT-001 v0.2 action row `ACT-NBX-RECOMMEND-CREDIT-001` |
| Agent-side responsibility ending point | Agent submits a signed draft package; it neither approves nor completes the credit |
| Workflow identity and owner | `partner-credit-recovery`; Rosa, service operations, owns completion |
| Durable state/checkpoint | `EVIDENCE_VALIDATED`; receipt `WF-NBX-1042-CP1` required |
| Business-operation identity | `partner:PX-44/dispute:D-1042/credit:v1` |
| Deadline/escalation | Four-business-hour review target is scenario input; overdue routes to operations duty owner |
| Human approval | Finance approver sees source versions, authority, amount, policy, prior attempts, and unknown outcomes |
| Retry/reconciliation | Query by business-operation identity before repeat; unknown remains a separate state |
| Compensation/correction | Cancel uncommitted work; corrected ledger entry plus partner notice after committed error |
| Completion | Ledger shows final credit outcome and partner case records the same operation identity |
| In-flight revocation | Stop new submissions; queued approval becomes `RESTRICTED_PENDING_REVIEW` |
| Evidence limit | Constructed record; workflow engine behavior and four-hour capacity have not been tested |

## View 2: End-to-end evaluation and provenance trace

Use to connect what influenced a decision with the authority exercised, action
attempted, durable consequence observed, descendants created, and corrections
later required. A generated explanation may link to this record but cannot
replace it.

### Evaluation and provenance metadata

| Field | Value |
| --- | --- |
| View ID/version | Assign `EPT-<system>-<nnn>` / version |
| Owner | Unassigned |
| Case/capability | Unassigned |
| Artifact state | BLANK |
| Evidence references | Link source/context, authority, decision, tool, workflow, descendants, correction, and evaluation IDs |
| Decision date | NOT_YET_DECIDED |
| Supersedes / superseded by | None |
| Reconsideration trigger | Source, model, policy, tool, workflow, evaluation, or retention changes |

### Causal and evidence join

| Stage | Required identity/version | Actual record or gap | Evidence limit |
| --- | --- | --- | --- |
| Source/context | Source, version, effective time, retrieval/derivation, Memory and Provenance Record | | |
| Memory layer | Transient context, retrieved, derived, parametric, or authoritative operational state | | |
| Context assembly | Ordering/position, truncation/exclusion behavior, trust classification | | |
| Retrieval | Query or immutable query reference, index/snapshot version, relevance-score meaning | | |
| Parametric model | Provider, model, version, disclosed knowledge-cutoff metadata or explicit `UNKNOWN`/`NOT_APPLICABLE` | | |
| Omissions and descendants | Known omissions plus undiscovered-copy/descendant/effect disclaimer | | |
| Memory use | Stable use-event receipt linking each retained item actually used to its record and consequential decision | | |
| Authority source and delegation | Principal, delegation chain, onward-delegation rule, authority-source owner/version | | |
| Protected object and evaluated attributes | Protected resource plus subject, object, operation, and environment attributes actually evaluated | | |
| Decision and enforcement | Policy decision point, policy enforcement point, policy version, decision/denial, expiry | | |
| Revocation | Owner, propagation targets, queued/in-flight treatment | | |
| Authority receipt | Stable decision or denial receipt linking authority-map row, evaluated inputs, PDP, PEP, outcome, and time | | |
| Decision | Goal, observations, model/prompt/policy versions, decision artifact | | |
| Tool attempt | Governed Tool Contract, caller/principal, operation identity, request, attempt time, authority receipt, memory-use receipts | | |
| Technical result | Accepted/completed/rejected/conflict/unknown response | | |
| Durable outcome | Workflow/state record and business completion meaning | | |
| Causal descendants | Events, work, communications, later actions | | |
| Correction | Corrected source/state, invalidated descendants, compensations | | |
| Evaluation | Claim, oracle, result, test state, transfer limit | | |

### Northbridge evaluation-and-provenance worked view

**Provenance:** `COMPOSITE`; constructed teaching fixture, not empirical
evidence.

| Stage | Constructed record | Evidence limit |
| --- | --- | --- |
| Source/context | Partner rule `PX-44-credit-policy` v7, effective time recorded; retrieval `RET-1042`; derived summary `MEM-778`; MPR-NBX-POLICY-001 v0.2 | Source authenticity and retrieval behavior are assumed fixture inputs |
| Memory layer | `MEM-778` is `DERIVED`; the signed partner policy is represented as authoritative operational state for this fixture | The five-layer vocabulary is proposed, not a universal standard |
| Context assembly | Signed policy excerpt precedes the summary; partner free text follows as `UNTRUSTED`; required identity/version/prohibition/correction fields cannot be truncated | Recording order does not prove correct model use or resistance to untrusted influence |
| Retrieval | Query `RET-1042-Q1`; index `partner-policy-index@2026-08-15T00:00Z`; score `0.86` means ranker relevance only | Relevance is not authority, truth, freshness, or permission |
| Parametric model | Provider/model/version `NOT_YET_DECIDED`; disclosed cutoff `UNKNOWN` | No item-level parametric lineage or currentness is implied |
| Omissions and descendants | Known omission: later policy v8 absent from original snapshot; declared descendants are memory, open draft, and review packet; undiscovered copies, recipients, uses, or effects may remain | The fixture cannot prove correction completeness |
| Memory use | Constructed receipt `USE-NBX-D1042-MEM778-001` links MPR-NBX-POLICY-001/item `MEM-778` to `DEC-NBX-1042` | No instrumented use event or complete causal influence has been observed |
| Authority source and delegation | `POL-NBX-12` v12; constructed chain policy owner -> Samir -> agent for investigation/recommendation/submission; onward delegation prohibited | Does not establish real legal or contractual authority or grantor legitimacy |
| Protected object and evaluated attributes | Dispute `D-1042`, partner `PX-44`, buyer tenant, evidence packet, and draft; subject/object/operation/environment attributes are named in AAM-NBX-CREDIT-001 v0.2 | Attribute truth, freshness, assurance, and fitness are assumed |
| Decision and enforcement | Constructed PDP `PDP-NBX-CREDIT-01`; PEP `PEP-NBX-CREDIT-GATEWAY-01`; approval withheld | No test proves complete mediation or runtime enforcement |
| Revocation | Samir/Nia; entitlement, token, PDP cache, PEP, workflow intake, approval queue; queued/ambiguous work becomes `RESTRICTED_PENDING_REVIEW` | `EXP-005` is `PLANNED/UNRUN`; propagation behavior is not observed |
| Authority receipt | Constructed `AUTHZ-NBX-D1042-DEC-001` represents the allow decision; denial receipts use their own immutable IDs | Receipt shape does not prove legitimate authority or outcome |
| Decision | `DEC-NBX-1042`; model/provider/prompt and policy versions named; rationale links sources | Rationale is not proof of causal completeness |
| Tool attempt | `TRY-NBX-1042-01`; GTC-NBX-CREDIT-001 v0.2; caller agent and original buyer principal; operation identity; `AUTHZ-NBX-D1042-DEC-001`; `USE-NBX-D1042-MEM778-001` | Receipt resolution, simulator behavior, and enforcement have not been executed |
| Technical result | Scenario injects timeout after acceptance; result remains `UNKNOWN` | Unknown cannot be restated as failure or success |
| Durable outcome | Workflow query later returns one accepted operation, then approval rejection | Constructed outcome, not production reliability evidence |
| Causal descendants | Draft notice and approval task share parent action ID; no ledger credit emitted | Declared graph may omit unknown downstream participants |
| Correction | Memory v7 superseded by v8; related open decisions queued for revalidation | Correction propagation is planned for EXP-002, not observed |
| Evaluation | Claims link to EXP-001 and EXP-002, both `PLANNED/UNRUN` | No test result supports the fixture yet |

## Review rule

A cross-asset view is useful only if every joined identity resolves to the
canonical artifact or retained evidence it names. A complete-looking row with
an unresolved reference is an evidence gap, not a successful trace.
