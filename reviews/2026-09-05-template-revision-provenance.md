# Prepared-template revision provenance

Date: September 5, 2026. Glasswing packet `AGENTIC-TEST-GAC-001` advances from
1.0.2 to 1.0.3 because three canonical dependency files changed during the
Agentic Systems Architecture editorial revision.

**Execution state: PLANNED/UNRUN. Actual practitioner sessions: 0.** This is a
local source-integrity repair. It is not an independent review, reader result,
production claim, or execution authorization. EXP-001 through EXP-005 are
unchanged. The temporal-freeze protocol and its tests are unchanged.

## Historical source

Original companion commit: `8b0ccdca61c607d825f288e6c514019889974e99`.
The [snapshot index](historical/glasswing-studio-scheduling-1.0.2-2026-09-05/snapshot-index.json)
records all sixteen preserved files: the previous manifest and every file it
pinned, including the earlier README, six templates, and participant and
facilitator files. Every preserved byte was read directly from that Git
commit, not reconstructed from the edited working tree. All fifteen old
manifest entries were verified against the preserved bytes.

Each original pathname is retained below the snapshot directory with a
`.snapshot` suffix. These are byte-for-byte historical files, not current
Markdown guidance. To reconstruct the former fixture for a historical review,
copy the indexed files to a separate directory and remove only the final
`.snapshot` suffix. The original `SHA256SUMS` then resolves against the former
layout. Do not overwrite current templates with historical copies.

## Revision scope

The root authority map, memory record, and budget worksheet were updated by
the lead editor. This integrity task did not alter their content. It refreshed
packet pins for their current versions: 0.3-template, 0.3-template, and
0.2-template respectively.

Packet README and six packet-local Markdown file/packet headers now identify
1.0.3. The participant scenario's three literal template hashes and versions
match current dependency bytes. Its case facts, decision tasks, and conditions
are unchanged. Other participant/facilitator changes are version-header-only.
The README distinguishes the new local integrity refresh from the earlier
revision's review language and states independent revision review is pending.
Consent, scoring, freeze requirements, canonical dependency membership, and
all execution conditions remain in force. The manifest was recalculated over
its original fifteen paths; no validator rule was removed or relaxed.

## Exact changed-file identities

The first hash is the preserved 1.0.2/HEAD identity; the second is the locally
revised identity. Three root-form changes originated in the parent editorial
pass; the remaining changes are this packet consistency repair.

| Path | Prior SHA-256 | Revised SHA-256 |
| --- | --- | --- |
| `action-budget-and-blast-radius.md` | `dfb70615c37c1917ff7e32c836ee45860268147aa7af2bd7bb580553eb531bf0` | `dc612f403ea663742ef57c64eb4e1330349ae49f646850d1ea2b362dc996a015` |
| `agent-authority-map.md` | `c00f3a3ad00938d30efea9792523a6c6f51a7c16d5061a9d9fdc7d8c53755f0f` | `06367a381cd5bdf37b2b8632e41936fc5e4408181ac51223e22c3fcf2cba9e5c` |
| `memory-and-provenance-record.md` | `27cbfe0c596f1d482cc9d4e74d18d55bc4bf91063db1b73498a5fed859c7a55a` | `d0d4cb0590e629c4687603688b61affdef052252cafd4a8497bcc5b4c5ead28a` |
| `testing/glasswing-studio-scheduling-v1/README.md` | `fe8dd0a1f8341f5bda45e1b73be085061c74157fb58648b132443a9f8926517e` | `a4eb830713bd3d8311e2f3aa3eea79a53b8f8f294cff7b66ac8f47d3dfc736f0` |
| `testing/glasswing-studio-scheduling-v1/SHA256SUMS` | `502f5c3c820aa96a7939304dda65cbc95e6c537cd31cbffa5f4a362e78a01a0a` | `51e90ca7ff553ce2285c0d6a054083c084656f6d47916c5992b63584be990df8` |
| `testing/glasswing-studio-scheduling-v1/facilitator-only/01-facilitator-guide.md` | `2b92ad06df3100ce8ea27acf4ceb89e619e3e79ddcc6f3208bd2ff6957a20922` | `de10ca1a40e7a19846edea2b14cf65683a8d5df457c5a07e4229784cc99cda3c` |
| `testing/glasswing-studio-scheduling-v1/facilitator-only/02-observation-and-scoring-rubric.md` | `409ff1a941daa91e74258079f01f17f09daf7d477850ae021819e082a3927144` | `bcae4ecdc312dd41e1c682bc3f82dd7fcaf112664ec90f474e1613bafb4ad5c0` |
| `testing/glasswing-studio-scheduling-v1/facilitator-only/03-results-and-deviation-log-blank.md` | `c9514e610c6019be6a044cb50eb8360db7d2d37ac66ac9eecb5c7601d11d2a44` | `f183617b266fa434c5aa89cac943616d7998d5bf132138c7e3938b4fef601f1c` |
| `testing/glasswing-studio-scheduling-v1/participant/01-consent-and-privacy-notice.md` | `3301168e03492b0fd32c08fcccdf46cb30b98dc07baad5ef486fd98f5bb46c75` | `d6a0f366117bcd85dcd63890c36a5ceaa49c4c528299e5ffa63e6fab70691867` |
| `testing/glasswing-studio-scheduling-v1/participant/02-scenario-and-decision-task.md` | `97d58fbd7e59955c047894446e05ebc332f8cfaf09483d64082c2cb3e3ab95aa` | `270b76349831933c66e495d335ddcfc88b33069f704ec4378e788db57f5f9815` |
| `testing/glasswing-studio-scheduling-v1/participant/03-response-workbook.md` | `90076766f252b9e9bf75473825db3a080a335e774d66aaab4233838dfbb070fb` | `1097bd93d6c9382efe5c2f483ea9bf573f0f6a25f070f1384435342c4c707e08` |

## Validation

`python3 scripts/validate_repository.py` is the required repository validation.
The result is recorded after execution below. A pass checks the declared
repository structure, links, checksum membership, and protocol invariants; it
does not establish comprehension, independent review, or an executed session.

Observed local result: **passed — 60 Markdown files, 152 local links, one
gateway asset, 34 checksums.** Historical snapshot verification also passed
for all fifteen old manifest dependencies. No practitioner session occurred.
