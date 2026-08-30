# Northbridge Worked Examples

**Disclosure:** Every example in this file is a fictional-composite teaching
fixture. The people, dialogue, values, records, and outcomes are constructed.
They are not John Briggs history, practitioner results, production observations,
or evidence that the assets work.
**Artifact state:** REVIEWED
**Test execution state:** PLANNED/UNRUN

## 1. Agent Authority Map example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AAM-NBX-CREDIT-001 / 0.2 |
| Owner | Samir Patel, partner operations |
| Case/capability | C-001 / investigate and draft partner credit |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Policy fixture `POL-NBX-12` v12; EXP-001 and EXP-005 `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Supersession | None |
| Reconsideration trigger | Credit policy, buyer delegation, amount, tenant, tool, or outcome semantics change |

| Stable action-row ID | Decision | Delegation |
| --- | --- | --- |
| `ACT-NBX-INVESTIGATE-001` | Investigate exception | Permitted for assigned buyer and partner cases using approved sources |
| `ACT-NBX-RECOMMEND-CREDIT-001` | Draft credit recommendation | Permitted up to a scenario value of $250; value is a design fixture, not a measured threshold |
| `ACT-NBX-SUBMIT-DRAFT-001` | Submit for approval | Permitted only through the durable workflow with operation identity |
| `ACT-NBX-ISSUE-CREDIT-001` | Approve or issue credit | Withheld; finance approval and ledger workflow retain authority |
| `SCOPE-NBX-PRINCIPAL-001` | Principal/subject/purpose | Northbridge partner operations / assigned buyer and partner / resolve documented shipment exception |
| `SCOPE-NBX-TIME-001` | Time and scope | One case, one policy version, until expiry or revocation |
| `CTRL-NBX-REVOCATION-001` | Revocation | Samir or Nia can revoke new submission authority; in-flight workflow becomes restricted pending owner review |
| `CTRL-NBX-AUTHORITY-PROOF-001` | Proof of authority | Signed authority record ID must appear in decision and tool attempt traces |

| Required first-class field | Constructed value and limit |
| --- | --- |
| Delegation chain and onward-delegation rule | Constructed chain: Northbridge partner-operations policy owner -> Samir Patel -> `agent-nbx-exception-01` for investigation, recommendation, and governed submission only. Onward delegation is prohibited. This does not prove the first grantor owns the business power. |
| Authority-source owner and version | Samir is the constructed business owner; `POL-NBX-12` v12 is the authority-source fixture. Validity, contractual fit, and currentness are untested scenario assumptions. |
| Protected object or resource | Buyer-scoped dispute `D-1042`, partner `PX-44`, its evidence packet, and the proposed credit draft; ledger funds remain outside agent authority. |
| Evaluated subject, object, operation, and environment attributes | Subject: agent identity, buyer principal, delegation ID; object: tenant, dispute, partner, currency; operation: investigate/recommend/submit; environment: policy v12, effective time, value, case state. Attribute truth, freshness, and assurance are assumed fixture inputs. |
| Policy decision point and policy enforcement point | Constructed PDP `PDP-NBX-CREDIT-01` evaluates policy v12; constructed PEP `PEP-NBX-CREDIT-GATEWAY-01` guards draft submission. No runtime path or complete mediation has been tested. |
| Revocation owner, propagation targets, and queued/in-flight treatment | Samir owns the business restriction and Nia owns technical propagation to agent entitlement, delegated token, PDP cache, PEP, workflow intake, and approval queue. New attempts stop; queued or ambiguous work becomes `RESTRICTED_PENDING_REVIEW`. `EXP-005` is `PLANNED/UNRUN`. |
| Stable decision or denial receipt | Constructed receipt `AUTHZ-NBX-D1042-DEC-001` represents the allow decision for draft submission; a denial would receive its own immutable `AUTHZ-NBX-D1042-DEN-<nnn>` ID. No runtime receipt has been emitted. |

**Remaining uncertainty:** The constructed delegation has not received legal,
policy, technical, or practitioner acceptance.

## 2. Governed Tool Contract example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | GTC-NBX-CREDIT-001 / 0.2 |
| Owner | Credit platform capability owner |
| Case/capability | C-001 / submit credit draft |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-NBX-CREDIT-001; `AUTHZ-NBX-D1042-DEC-001`; `USE-NBX-D1042-MEM778-001`; EXP-001/EXP-002/EXP-005 `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Caller, principal, output contract, allowed release, or provider changes |

- **Promise:** Accept one governed draft for review; `202 Accepted` means
  durable custody, not approved or issued credit.
- **Caller/principal propagation:** Agent service identity plus buyer principal
  and Northbridge delegation ID are required and independently enforced.
- **Tool-output trust:** Status fields are authoritative only when signed by the
  workflow service; free-text messages remain untrusted diagnostic content.
- **Allowed release:** case ID, partner ID, amount, currency, reason code, and
  evidence references. Buyer contact details and secrets are prohibited.
- **Unknown outcome:** query by operation identity; do not resubmit until the
  workflow reports absent or the capability owner authorizes recovery.
- **Authority decision/denial receipt:** every attempt carries
  `AUTHZ-NBX-D1042-DEC-001`, or its immutable denial counterpart, and the
  gateway resolves it to AAM-NBX-CREDIT-001 v0.2 action row
  `ACT-NBX-SUBMIT-DRAFT-001` and the represented PDP/PEP record.
- **Memory-use receipt:** the constructed attempt carries
  `USE-NBX-D1042-MEM778-001`, resolving MPR-NBX-POLICY-001, policy v7, the
  represented use event, and decision `DEC-NBX-1042`.
- **Negative paths:** wrong tenant, missing delegation, excess amount,
  duplicate, poisoned free-text output, and timeout after acceptance must be
  tested.

**Remaining uncertainty:** No simulator or enforcement-point test has run.

## 3. Memory and Provenance Record example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | MPR-NBX-POLICY-001 / 0.2 |
| Owner | Lena Brooks, data and AI architecture |
| Case/capability | C-003 scenario / partner-credit policy influence |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Source fixture `PX-44-credit-policy` v7; EXP-002 `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Source, derivation, effective time, retention, or correction path changes |

- **Meaning/use:** A derived summary of partner-specific evidence requirements;
  it may guide investigation but cannot approve a credit.
- **Source/version:** Policy fixture v7, effective 2026-08-01; source owner is
  partner operations.
- **Derivation:** retrieval snapshot plus summary transform `SUM-3`; both must
  be recorded at use time.
- **Expiry/revalidation:** revalidate at case submission and whenever a source
  correction or newer effective version appears.
- **Correction:** v8 supersedes v7; linked memory is marked stale and open draft
  decisions are queued for revalidation.
- **Safe failure:** if source/version fitness cannot be established, the agent
  may collect facts but cannot submit the draft.

| Required first-class field | Constructed value and limit |
| --- | --- |
| Memory type or layer: transient context, retrieved, derived, parametric, or authoritative operational state | `DERIVED`; summary `MEM-778` is derived from a retrieved policy snapshot. The signed policy remains authoritative operational state; the summary does not become authoritative by proximity. |
| Context ordering, truncation, and trust classification | The fixture places the signed policy excerpt before the derived summary; partner-supplied free text follows as `UNTRUSTED`. Truncation rule: preserve source identity, version, effective date, prohibition, and correction flag or block submission. No model-use behavior has been tested. |
| Retrieval query, index version, and relevance-score meaning | Constructed query reference `RET-1042-Q1`; index snapshot `partner-policy-index@2026-08-15T00:00Z`; score `0.86` means ranker relevance within that snapshot only—not authority, truth, freshness, or permission. |
| Known omissions and undiscovered-descendant disclaimer | Known omission: later policy v8 is absent from the original snapshot. Declared descendant list covers `MEM-778`, the open draft, and its review packet; undiscovered copies, recipients, in-flight uses, or effects may remain. |
| Parametric model, provider, version, and disclosed knowledge-cutoff metadata | Provider/model/version are `NOT_YET_DECIDED` for the fixture; disclosed knowledge cutoff is `UNKNOWN`. These values must be resolved before a test run and cannot supply item-level policy lineage. |
| Stable use-event and consequential-decision receipt linking each retained item to actual use | Constructed `USE-NBX-D1042-MEM778-001` links MPR-NBX-POLICY-001 and item `MEM-778` to decision `DEC-NBX-1042`; it represents scenario influence only. No instrumented use event or consequential outcome has been observed. |

**Remaining uncertainty:** Descendant completeness and in-flight correction are
planned EXP-002 questions, not observed controls.

## 4. Action Budget and Blast-Radius Worksheet example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | ABB-NBX-CREDIT-001 / 0.1 |
| Owner | Eli Chen, platform reliability |
| Case/capability | C-005 / investigation and draft submission loop |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | Scenario graph `NBX-ACTION-GRAPH-01`; EXP-004 `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Fan-out, retry, delay, tool, workflow, or value assumptions change |

| Dimension | Constructed envelope | Stop behavior |
| --- | --- | --- |
| Draft value | $250 per case; $1,000 per buyer/day | Prevent new submission and alert owner |
| Cases | One active draft per dispute | Reconcile operation identity |
| External messages | One draft notice; no customer send | Route additional communication to review |
| Tool calls | 20 investigation calls per case | Stop planning and preserve trace |
| Workflow starts | One per operation identity | Reject duplicate and query current state |
| Time | 15 minutes of agent planning | Hand off or abstain |

Tenant, buyer, partner, and causal-action IDs scope every counter. Eli holds the
technical kill path; Samir holds the business restriction decision. Issuing a
credit remains outside the envelope.

**Remaining uncertainty:** All quantities are scenario assumptions. EXP-004
has not tested multiplication or containment.

## 5. Autonomy Evidence Gate example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AEG-NBX-CREDIT-001 / 0.1 |
| Owner | Maya Torres, architecture decision owner |
| Case/capability | C-001 / move from investigation to draft submission |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-NBX-CREDIT-001 v0.2; GTC-NBX-CREDIT-001 v0.2; MPR-NBX-POLICY-001 v0.2; ABB-NBX-CREDIT-001 v0.1; EXP-001, EXP-002, EXP-003, EXP-004, and EXP-005 all `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Any material failure, control/version change, or proposed capability expansion |

| Evidence class | Constructed required result | Current result | Status |
| --- | --- | --- | --- |
| Meaning/authority | Recommendation and approval remain distinct | Briefs only | NOT_READY |
| Tool/policy | Deny wrong tenant and ambiguous repeat | Unrun | PLANNED/UNRUN |
| Memory fitness | Corrected policy revalidates open drafts | Unrun | PLANNED/UNRUN |
| Loop/budget | Declared loops stop within bounds | Unrun | PLANNED/UNRUN |
| Outcome/recovery | Workflow outcome reconstructable and correctable | Unrun | PLANNED/UNRUN |
| Human capacity | Review packet usable within declared demand | No practitioner evidence | NOT_READY |
| Incident readiness | Revocation/tabletop covers queued paths | Unrun | PLANNED/UNRUN |

**Constructed decision:** `RESTRICTED`; investigation and draft generation may
be studied, but no autonomous submission or approval is authorized by this
fixture.

## 6. Agentic Incident Readiness Plan example

| Metadata field | Constructed value |
| --- | --- |
| Artifact ID/version | AIR-NBX-CREDIT-001 / 0.1 |
| Owner | Eli Chen, technical incident commander; Samir, business owner |
| Case/capability | C-007 scenario / repeated credit-draft loop |
| Artifact state | REVIEWED |
| Test execution state | PLANNED/UNRUN |
| Evidence references | AAM-NBX-CREDIT-001 v0.2; GTC-NBX-CREDIT-001 v0.2; MPR-NBX-POLICY-001 v0.2; ABB-NBX-CREDIT-001 v0.1; AEG-NBX-CREDIT-001 v0.1; EXP-005 `PLANNED/UNRUN` |
| Decision date | 2026-08-29 source review |
| Reconsideration trigger | Owner, path, revocation, correction, communication, or evidence changes |

- **Detect:** causal repetition, budget breach, duplicate operation identity,
  review backlog, or mismatch between tool response and workflow state.
- **Contain:** stop new agent decisions, revoke tool delegation, pause affected
  workflows and event reactions, preserve unaffected tenant paths, and classify
  ambiguous in-flight operations.
- **Reconstruct:** join source/memory versions, authority, decision, attempts,
  workflow outcomes, notices, and descendants.
- **Correct:** reconcile each operation, compensate erroneous state, invalidate
  stale memory, notify accountable owners, and verify downstream completion.
- **Re-enter:** only the separately gated capability may resume; lack of a new
  incident is not sufficient evidence.

**Remaining uncertainty:** No tabletop or technical revocation exercise has
run, and the constructed roles/times do not establish Northbridge readiness.
