# Governed Tool Contract

## Artifact metadata

| Field | Value |
| --- | --- |
| Artifact ID | Assign `GTC-<system>-<nnn>` |
| Version | 0.2-template |
| Owner | Unassigned |
| Case/capability | Unassigned |
| Artifact state | BLANK |
| Test execution state | PLANNED/UNRUN |
| Evidence references | None; add stable authority, policy, test, and trace IDs |
| Decision date | NOT_YET_DECIDED |
| Supersedes / superseded by | None |
| Reconsideration trigger | Capability, caller, principal, policy, provider, output, or data-release change |

## Capability promise

- Tool/capability name:
- Business outcome exposed:
- What a successful technical response means:
- What it does **not** mean:
- Accountable provider:
- Authorized agent identities:
- Caller identity and original principal propagation:
- Subjects and purposes permitted:
- Policy enforcement point outside the model:

## Request and authority

- Required inputs and authoritative sources:
- Trust level and validation rule for tool output:
- Delegation or consent evidence:
- Tenant and subject isolation:
- Allowed data release by class and field:
- Prohibited data release and egress destination:
- Secret handling and redaction rule:
- Preconditions and policy version:
- Idempotency/business-operation key:
- Expiration and replay rules:

## Required stable joins

Do not infer these joins from a trace timestamp or free-text explanation. Use
`NOT_APPLICABLE`, `UNKNOWN`, or `NOT_YET_DECIDED` explicitly rather than an
empty value. The references describe the represented path; their presence does
not prove legitimate authority, complete influence capture, or runtime
enforcement.

| Stable cross-reference | Receipt ID and resolution rule |
| --- | --- |
| Authority decision or denial receipt | NOT_YET_DECIDED — resolve to the Agent Authority Map row, authority-source version, evaluated attributes, policy decision, enforcement result, and decision/denial time |
| Memory use-event receipt or receipts | NOT_YET_DECIDED — resolve each retained item actually used to its Memory and Provenance Record, item/source version, use event, and consequential decision receipt when applicable |

## Outcomes and failure

| Outcome | Meaning | Agent response allowed | Human escalation | Evidence emitted |
| --- | --- | --- | --- | --- |
| Accepted | | | | |
| Completed | | | | |
| Rejected | | | | |
| Conflict | | | | |
| Ambiguous/unknown | | | | |
| Dependency failure | | | | |

## Consequence controls

- Per-action value/reach limit:
- Rate and cumulative budget:
- Irreversible boundary:
- Required durable workflow:
- Compensation or correction path:
- Circuit-breaker and kill authority:
- Revocation behavior:

## Verification

- Contract and policy tests:
- Duplicate and ambiguous-outcome tests:
- Cross-tenant/subject denial tests:
- Failure injection:
- Observability and provenance fields:
- Consumer/agent compatibility evidence:
- Remaining uncertainty and operational owner:

## Review record

- Editorial/technical reviewers:
- Review date:
- Artifact-state decision:
- Restrictions or required follow-up:
