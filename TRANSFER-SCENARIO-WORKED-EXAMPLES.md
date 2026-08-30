# Unrelated Transfer-Scenario Worked Examples

**Scenario disclosure:** Clearwater Facilities is a wholly constructed example
unrelated to Northbridge. Its agent reviews building-sensor anomalies, drafts
maintenance work, and may request dispatch. Names, limits, data, and outcomes
are hypothetical. This packet tests conceptual transfer only after practitioner
sessions occur; none have occurred.
**Artifact state:** REVIEWED
**Test execution state:** PLANNED/UNRUN

## 1. Agent Authority Map example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AAM-CWF-HVAC-001 / 0.2 |
| Owner | Facilities operations manager |
| Case/capability | Investigate HVAC anomaly and draft work order |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Constructed policy `CWF-MAINT-4`; no test evidence |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Building, vendor, safety class, cost, occupancy, or dispatch scope changes |

The agent may read approved sensor and maintenance history for the assigned
building, classify a non-safety anomaly, and draft a work order. It may not
disable equipment, enter an occupied restricted area, approve spending, or
dispatch a vendor. Facilities operations delegates the draft capability; the
on-call engineer can revoke it. Fire, gas, water, and life-safety signals are
explicitly excluded and escalate through existing controls.

| Stable action-row ID | Decision | Delegation |
| --- | --- | --- |
| `ACT-CWF-READ-HVAC-001` | Read approved HVAC evidence | Permitted for the assigned building and equipment only |
| `ACT-CWF-CLASSIFY-NONSAFETY-001` | Classify a non-safety anomaly | Permitted only when safety exclusion and source-fitness checks pass |
| `ACT-CWF-DRAFT-WO-001` | Create a draft work order | Permitted through the governed tool; spending and dispatch remain withheld |
| `ACT-CWF-DISPATCH-001` | Dispatch a vendor or control equipment | Withheld; human facilities authority and existing safety controls retain the decision |

| Required first-class field | Constructed value and limit |
| --- | --- |
| Delegation chain and onward-delegation rule | Constructed chain: Clearwater facilities policy owner -> facilities operations manager -> `agent-cwf-hvac-01` for investigation/classification/draft only. Onward delegation is prohibited. The chain does not establish real business or safety authority. |
| Authority-source owner and version | Facilities operations manager; constructed policy `CWF-MAINT-4` v4. Ownership, validity, and currentness are scenario assumptions. |
| Protected object or resource | Assigned building, HVAC equipment/anomaly record, sensor history, and draft work order; equipment control, occupied restricted areas, spending, and dispatch remain protected and prohibited. |
| Evaluated subject, object, operation, and environment attributes | Subject: agent and facilities principal; object: building, equipment, anomaly, safety class; operation: read/classify/draft; environment: occupancy, policy v4, cost class, sensor freshness. Attribute truth and assurance are untested. |
| Policy decision point and policy enforcement point | Constructed PDP `PDP-CWF-MAINT-01`; constructed PEP `PEP-CWF-WO-GATEWAY-01`. No test proves that every path is mediated. |
| Revocation owner, propagation targets, and queued/in-flight treatment | On-call engineer revokes; propagation targets agent entitlement, delegated credential, PDP cache, gateway PEP, and draft-work queue. New work stops; queued/unknown drafts become `RESTRICTED_PENDING_REVIEW`. Propagation time is `UNKNOWN`; `EXP-005` remains `PLANNED/UNRUN`. |
| Stable decision or denial receipt | Constructed allow receipt `AUTHZ-CWF-HVAC-DEC-001`; exclusions use immutable `AUTHZ-CWF-HVAC-DEN-<nnn>` receipts. No runtime receipt has been emitted. |

**Evidence limit:** This is a design fixture, not a safety analysis or authority
approval.

## 2. Governed Tool Contract example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | GTC-CWF-WO-001 / 0.2 |
| Owner | Maintenance platform owner |
| Case/capability | Create draft work order |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-CWF-HVAC-001 v0.2; `AUTHZ-CWF-HVAC-DEC-001`; `USE-CWF-HVAC-MANUAL001-001`; `USE-CWF-HVAC-REG001-001`; no test evidence |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Work-order API, vendor, identity, allowed fields, or result semantics change |

`Accepted` means a draft has durable custody, not vendor dispatch. The request
must carry agent identity, facilities principal, building, anomaly, purpose,
and operation identity. The external enforcement point denies excluded safety
classes and buildings. Allowed release excludes occupant identity, access
codes, and credentials. Tool free text is untrusted; status and draft ID must
pass schema and tenant validation. An unknown result is queried before repeat.

The request carries authority receipt `AUTHZ-CWF-HVAC-DEC-001`, resolving
AAM-CWF-HVAC-001 v0.2 action row `ACT-CWF-DRAFT-WO-001` and the represented
PDP/PEP outcome, plus memory-use receipt
`USE-CWF-HVAC-MANUAL001-001`, resolving retained item
`MEM-CWF-MANUAL-INT-001` v1 and source `SRC-CWF-MANUAL-HVAC-004` v4, and
receipt `USE-CWF-HVAC-REG001-001`, resolving retained item
`MEM-CWF-REGISTRY-CAL-001` v1 and source
`SRC-CWF-EQUIPREG-20260829T000000Z` v1. Both resolve MPR-CWF-HVAC-001 v0.2,
their represented use events, and decision `DEC-CWF-HVAC-001`. A denied request
receives its own stable denial receipt. These are constructed join shapes; no
receipt resolution or enforcement behavior has been executed.

**Evidence limit:** No API, denial, egress, duplicate, or timeout test has run.

## 3. Memory and Provenance Record example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | MPR-CWF-HVAC-001 / 0.2 |
| Owner | Facilities data owner |
| Case/capability | Maintenance interval and known-sensor condition |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Manual fixture `SRC-CWF-MANUAL-HVAC-004` v4; equipment-registry snapshot fixture `SRC-CWF-EQUIPREG-20260829T000000Z` v1; no test evidence |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Manual, sensor calibration, building use, retention, or source ownership changes |

Retained item `MEM-CWF-MANUAL-INT-001` v1 summarizes a manufacturer interval
from `SRC-CWF-MANUAL-HVAC-004` v4. Retained item
`MEM-CWF-REGISTRY-CAL-001` v1 summarizes the installed unit and calibration
state from `SRC-CWF-EQUIPREG-20260829T000000Z` v1. The signed equipment
registry is authoritative for installed unit and calibration date; both
summaries are advisory. They expire after 24 hours or when a calibration event
appears. A correction invalidates the affected summary and rechecks open
drafts. Missing current registry data permits evidence collection but blocks a
maintenance classification.

| Required first-class field | Constructed value and limit |
| --- | --- |
| Memory type or layer: transient context, retrieved, derived, parametric, or authoritative operational state | `DERIVED`; `MEM-CWF-MANUAL-INT-001` v1 and `MEM-CWF-REGISTRY-CAL-001` v1 are derived from the exact manual and registry sources named above. The signed equipment registry is authoritative operational state for installed unit and calibration date. |
| Context ordering, truncation, and trust classification | Registry evidence precedes the advisory manual summary; sensor free text is `UNTRUSTED`. The constructed truncation rule preserves equipment identity, calibration time, safety exclusion, and correction flag or blocks classification. Model behavior is untested. |
| Retrieval query, index version, and relevance-score meaning | Constructed query reference `RET-CWF-HVAC-Q1`; index `facilities-manuals@v4`; relevance score is `NOT_APPLICABLE` for the exact registry lookup and, for manual search, means rank only—not authority, truth, freshness, or safety fitness. |
| Known omissions and undiscovered-descendant disclaimer | Known omissions: vendor service bulletin status and any unregistered field repair are `UNKNOWN`. Declared descendants include the summary and open draft; undiscovered copies, downstream recipients, and effects may remain. |
| Parametric model, provider, version, and disclosed knowledge-cutoff metadata | Model/provider/version are `NOT_YET_DECIDED`; disclosed knowledge cutoff is `UNKNOWN`. These cannot substitute for registry or manual lineage. |
| Stable use-event and consequential-decision receipt linking each retained item to actual use | Constructed `USE-CWF-HVAC-MANUAL001-001` links MPR-CWF-HVAC-001 v0.2, `MEM-CWF-MANUAL-INT-001` v1, and `SRC-CWF-MANUAL-HVAC-004` v4 to decision `DEC-CWF-HVAC-001`; constructed `USE-CWF-HVAC-REG001-001` links the same MPR version, `MEM-CWF-REGISTRY-CAL-001` v1, and `SRC-CWF-EQUIPREG-20260829T000000Z` v1 to that decision. Each represents a scenario use event only; no retained item has been instrumented or used in a real consequential decision. |

**Evidence limit:** Correction propagation and descendant completeness are
unrun assumptions.

## 4. Action Budget and Blast-Radius Worksheet example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | ABB-CWF-HVAC-001 / 0.1 |
| Owner | Facilities reliability lead |
| Case/capability | HVAC draft work orders |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Building-topology fixture `TOPO-CWF-BLDG-001` v0.1; no test evidence |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Sensor count, building scope, vendor path, or dispatch authority changes |

The scenario permits one open draft per equipment/anomaly identity, ten sensor
reads per investigation, five new drafts per building/hour, and no external
dispatch. Duplicated telemetry shares a causal identity. Repeated drafts trip a
breaker and route to operations. The maximum irreversible consequence is zero
because device control and dispatch remain prohibited.

**Evidence limit:** Limits are hypothetical and have not been calibrated to a
real queue or workload.

## 5. Autonomy Evidence Gate example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AEG-CWF-HVAC-001 / 0.1 |
| Owner | Facilities architecture review |
| Case/capability | Add autonomous vendor dispatch for low-cost HVAC work |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-CWF-HVAC-001 v0.2; GTC-CWF-WO-001 v0.2; MPR-CWF-HVAC-001 v0.2; ABB-CWF-HVAC-001 v0.1; EXP-001, EXP-002, EXP-003, EXP-004, and EXP-005 all `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Safety classification, cost, occupancy, provider, or incident changes |

The proposed change introduces spending, physical access, scheduling, and
external communication. Required authority, exclusion, duplicate, stale-
sensor, provider, capacity, cancellation, and incident evidence is absent.
The fixture's decision is `RESTRICTED`: keep draft generation; withhold dispatch.

**Evidence limit:** The restriction teaches gate use; it is not a decision for
any real facility.

## 6. Agentic Incident Readiness Plan example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AIR-CWF-HVAC-001 / 0.1 |
| Owner | Facilities incident commander |
| Case/capability | Duplicate maintenance drafts after sensor replay |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-CWF-HVAC-001 v0.2; GTC-CWF-WO-001 v0.2; MPR-CWF-HVAC-001 v0.2; ABB-CWF-HVAC-001 v0.1; AEG-CWF-HVAC-001 v0.1; no tabletop evidence |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Path, owner, vendor, sensor, revocation, or correction changes |

The plan detects repeated causal identities and backlog growth; stops new agent
drafts; revokes work-order delegation; preserves sensor, memory, decision, and
tool records; reconciles drafts by equipment/anomaly identity; closes duplicates;
and rechecks maintenance state before re-entry. Existing life-safety response
paths must remain unaffected.

**Evidence limit:** No tabletop has shown that the owners, kill path,
reconstruction, correction, or unaffected-path protection work.
