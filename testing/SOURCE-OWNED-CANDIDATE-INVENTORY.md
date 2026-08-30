# Source-Owned Packet Inventory — Glasswing

<!-- markdownlint-disable MD013 -->

**Inventory ID:** AGENTIC-TEST-INVENTORY-001
**Inventory version:** 1.0.2
**Source scope:** `testing/glasswing-studio-scheduling-v1/`
**Artifact state:** PREPARED; source integrity and routing reviewed
**Test execution state:** `PLANNED/UNRUN`
**Recorded practitioner sessions:** 0

## Purpose and ownership boundary

This note identifies the exact prepared source packet and its dependencies. It
is not a canonical companion template, experiment specification, run manifest,
participant result, or publication artifact.

Source review establishes that the packet is internally routed, its current
dependencies are pinned, and mechanical drift is detectable. It does not
authorize recruitment. Before any attempt, an accountable execution owner must
verify the checked-in manifest and complete the consent, privacy, retention,
access, timebox, evaluator, and evidence-storage conditions in the packet.

## Source payload

The checksum manifest covers:

- the packet README;
- three participant-facing files;
- three facilitator-only files;
- six canonical companion templates;
- the blank practitioner-log source; and
- the working distribution terms.

Use [`glasswing-studio-scheduling-v1/SHA256SUMS`](glasswing-studio-scheduling-v1/SHA256SUMS)
as the sole mechanical hash authority. This inventory deliberately does not
duplicate hashes, byte counts, or word counts that can become stale while
appearing authoritative.

## Pinned canonical dependencies

| Canonical asset | Version | Purpose in the packet |
| --- | --- | --- |
| [Agent Authority Map](../agent-authority-map.md) | 0.2-template | Separate technical reach from delegated and withheld action |
| [Governed Tool Contract](../governed-tool-contract.md) | 0.2-template | Review the supplied action path and unknown outcome |
| [Memory and Provenance Record](../memory-and-provenance-record.md) | 0.2-template | Expose stale derived policy and missing influence evidence |
| [Action Budget and Blast-Radius Worksheet](../action-budget-and-blast-radius.md) | 0.1-template | Bound attempts and effects across workers and deliveries |
| [Autonomy Evidence Gate](../autonomy-evidence-gate.md) | 0.1-template | Keep proposed autonomy restricted until evidence exists |
| [Agentic Incident Readiness Plan](../agentic-incident-readiness-plan.md) | 0.1-template | Govern containment, reconstruction, correction, and re-entry |

Supporting dependencies are [Practitioner Test
Logs](../PRACTITIONER-TEST-LOGS.md) and the working [Terms](../TERMS.md).

## Claims and state limits

- Glasswing is fictional and is not John Briggs's experience.
- Participant and facilitator materials remain separated.
- The five-asset facilitator route is a reference, not an answer key or a
  requirement to maximize form completion.
- All tool behavior, correction, budget, incident, containment, and evidence
  results remain constructed or `PLANNED/UNRUN`.
- No usability, runtime, control, effectiveness, correctness, safety, privacy,
  legal, production, or business result exists.
- This packet cannot execute or transition EXP-001 through EXP-005.

## Change rule

Any changed packet or dependency byte causes repository validation to fail
until the packet version, embedded dependency hash when present, and
`SHA256SUMS` are deliberately updated together. Preserve the old commit as the
historical version; do not silently rewrite a packet used in a completed run.

**Current disposition:** `PREPARED/UNRUN`. Source integrity is reviewable. No
participant or system evidence exists.
