# Source-Owned Candidate Inventory — Glasswing Packet

<!-- markdownlint-disable MD013 -->

**Inventory ID:** AGENTIC-TEST-INVENTORY-001
**Inventory version:** 1.0.1-candidate
**Source scope:** `architecting-agentic-systems/companion/testing/`
**Source-owner role:** Author-controlled Agentic Systems companion source
**Accountable acceptance owner:** `NOT_YET_DECIDED`
**Independent review state:** PENDING; not submitted or accepted in this note
**Artifact state:** IN_PROGRESS
**Test execution state:** `PLANNED/UNRUN`
**Recorded practitioner sessions:** 0

## Purpose and ownership boundary

This note identifies the exact source-owned candidate packet prepared for later
independent review. It is an inventory, not a seventh canonical companion
asset, experiment specification, run manifest, acceptance record, practitioner
result, or publication artifact.

Source authorship may propose these bytes. It cannot self-approve them. The
accountable acceptance owner remains undecided, and no participant may be
recruited until independent review accepts an exact later manifest and the
packet's consent, privacy, ownership, retention, and execution prerequisites
are completed.

## Candidate source payload

The payload below contains eight source files. Hashes were calculated from the
UTF-8/LF candidate bytes after drafting. The inventory file itself is excluded
from this payload digest to avoid a self-referential hash; an external review
or handoff manifest must hash this inventory separately.

| Source ID | Version | Relative path | Participant visibility | Words | Bytes | SHA-256 |
| --- | --- | --- | --- | ---: | ---: | --- |
| AGENTIC-TEST-COLLECTION-001 | 1.0.1-candidate | `companion/testing/README.md` | Administrative; do not substitute for participant instructions | 172 | 1,608 | `22f020f58d5fa75832232a9ab2c3a438b4ecf5f8fc149e2372aea38cf15ce207` |
| AGENTIC-TEST-GAC-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/README.md` | Administrative; establishes separation and freeze procedure | 583 | 4,748 | `95d85e5fc491915f81b9442b598378f09e77bba80cf3303f924d93a7874da97b` |
| AGENTIC-TEST-GAC-FACILITATOR-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/facilitator-only/01-facilitator-guide.md` | Withheld before and during attempt | 1,595 | 12,088 | `0d12121f3259c00712beefc78b984ee9c211a13d456f135c4d94e3f40288becd` |
| AGENTIC-TEST-GAC-RUBRIC-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/facilitator-only/02-observation-and-scoring-rubric.md` | Withheld before and during attempt | 1,645 | 10,098 | `b8fb9ea6a5a6c44a0ed2aed8ad1fa601fd505c7eec26d20fb6c7353e51ed76bf` |
| AGENTIC-TEST-GAC-RESULTS-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/facilitator-only/03-results-and-deviation-log-blank.md` | Withheld before and during attempt; copied only into an authorized run package | 1,120 | 7,894 | `50bdfd7c6e974c318263f135a667205ec33acf3b9198e2044790501b0c4ff393` |
| AGENTIC-TEST-GAC-CONSENT-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/participant/01-consent-and-privacy-notice.md` | Supplied only after prerequisites are completed | 726 | 5,174 | `df7e1e9b2fecc3a2f38f97cb19cb57aa5845d354d610cbeeb9e0cdfe1d825fa5` |
| AGENTIC-TEST-GAC-SCENARIO-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/participant/02-scenario-and-decision-task.md` | Supplied | 1,882 | 14,215 | `7118cea2cb1fe45ee662554d8c1372313fa6b544a35a5beca7306f0d4084b175` |
| AGENTIC-TEST-GAC-RESPONSE-001 | 1.0.1-candidate | `companion/testing/glasswing-studio-scheduling-v1/participant/03-response-workbook.md` | Supplied blank | 1,090 | 6,152 | `6bd7e93dc39ce02c9eaf2a4cc2fcc61460cc2edcfc019b6c7adbfacf2fce3ca0` |

Payload total: **8 files / 8,813 whitespace-delimited words / 61,977 bytes**.

SHA-256 of the ordered `sha256sum`-format payload manifest in the table's
lexicographic path order:

`7a3529301e8f51c2d821299ed84e1c13f2d15a404619e340b555b160f5f74a82`

## Pinned canonical dependencies

These six files remain the canonical assets. This packet creates no new
canonical asset and does not edit the dependency bytes.

| Canonical asset | Template version | Repository-relative path | SHA-256 |
| --- | --- | --- | --- |
| Agent Authority Map | 0.2-template | `companion/agent-authority-map.md` | `9948d63664ff56f598cd0842b636e581cb83cc3d301a5dd017d77c2629a2f15a` |
| Governed Tool Contract | 0.2-template | `companion/governed-tool-contract.md` | `52d574fdc56434e6bc32e83c8b5403d80536e7b1b3a077dbfaf848414ed02eb4` |
| Memory and Provenance Record | 0.2-template | `companion/memory-and-provenance-record.md` | `27cbfe0c596f1d482cc9d4e74d18d55bc4bf91063db1b73498a5fed859c7a55a` |
| Action Budget and Blast-Radius Worksheet | 0.1-template | `companion/action-budget-and-blast-radius.md` | `dfb70615c37c1917ff7e32c836ee45860268147aa7af2bd7bb580553eb531bf0` |
| Autonomy Evidence Gate | 0.1-template | `companion/autonomy-evidence-gate.md` | `67cf1d908e6aa7d98745d84913b79c228cfbee04103d3218973cab9932960b43` |
| Agentic Incident Readiness Plan | 0.1-template | `companion/agentic-incident-readiness-plan.md` | `26d2dea9ee8a92ab1df0d8ec066386730b80ec1e4da263b8f98638ea85d86f56` |

Supporting source dependencies:

| Source | Version/state | SHA-256 | Boundary |
| --- | --- | --- | --- |
| `companion/PRACTITIONER-TEST-LOGS.md` | Six blank logs; `PLANNED/UNRUN`; 0 sessions | `36416a68a5e2097f85664bc00ae78a9803f7176f18a449b3dafb990366fd2605` | Freeze a controlled copy; never populate the source file |
| `companion/TERMS.md` | Internal working terms; legal review incomplete | `1ba1b3d165ef611df9cc22e89c0d43adbbb51a51c55f3ce8acd6c5439c1ca8b0` | No external distribution or safety/certification use |

## Candidate claims and state limits

- The Glasswing scenario is fictional, unrelated to Northbridge, and not John
  Briggs's experience.
- Participant and facilitator materials are separate. The participant side
  contains no reference route, answer key, expected asset count, or scoring
  criteria.
- The facilitator route uses five assets but explicitly permits a smaller
  defensible route. Six-asset completion is not an oracle.
- The packet is intended to expose decisions about delegated and withheld
  authority, the governed tool/action path, memory and provenance, cumulative
  consequence, evidence-gated autonomy, and incident/re-entry limits.
- Every tool behavior, correction, budget mechanism, incident action,
  containment step, and evidence result remains constructed or
  `PLANNED/UNRUN`.
- No practitioner has been recruited or consented. No usability, runtime,
  control, effectiveness, correctness, safety, privacy, legal, production, or
  business result exists.
- The packet has no authority to execute or transition EXP-001, EXP-002,
  EXP-003, EXP-004, or EXP-005. All remain `PLANNED/UNRUN` in their authoritative
  register.

## Change and review rule

Any change to a source payload file, canonical dependency, terms file, log
source, task, participant role, blinding rule, rubric, state limit, or evidence
boundary invalidates the corresponding hash. Create a new candidate version,
recompute an external full manifest including this inventory, rerun mechanical
and semantic checks, and obtain independent review before recruitment or use.

**Current disposition:** `CANDIDATE — PENDING INDEPENDENT REVIEW`. This note
does not self-approve the packet.
