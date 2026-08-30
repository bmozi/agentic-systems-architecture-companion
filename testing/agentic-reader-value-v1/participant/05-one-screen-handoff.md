# One-Screen Decision Handoff

**Packet:** AG-RV-PILOT-001 version 1.2.2
**Status:** Blank Stage A transfer; complete only after the live update

Keep this to one screen or one printed page. Do not open or complete it until
`STAGE-A-HANDOFF-INPUT-SHA256SUMS` verifies the revised artifacts, their
governing manifest, their detached verification record, and this blank input.
Export the completed handoff as `AG-A-ONE-SCREEN-HANDOFF-v1.md`. Link detailed artifacts instead of copying
them. Use each exact literal immutable local filename; Stage B must receive
that same filename and byte sequence. `UNASSIGNED` and `UNKNOWN` are valid and
preferable to invention.

| Decision field | Stage A entry |
| --- | --- |
| Handoff artifact ID/version | |
| Handoff completion timestamp/timezone | |
| Handoff state before hashing | `HANDOFF COMPLETE` / invalid |
| Evidence class and current state | |
| Beneficiary and useful delegated outcome | |
| Recommended decision | `EXPLORE` / `PROCEED BOUNDED` / `INVEST` / `HOLD` / `STOP` |
| Allowed now | |
| Withheld | |
| Assigned owner | Name role or write `UNASSIGNED` |
| Assigning/acting authority | Name source/trigger or write `UNKNOWN` |
| Known evidence | |
| Material unknowns | |
| Largest unacceptable outcome | |
| Recommended stop or containment | What should be stopped, held, isolated, or reconciled now |
| Actual containment execution status | Evidence of what was actually executed; write `UNKNOWN` when execution is not evidenced |
| Immediate next action | |
| Reconsideration | Date **or** evidence-based trigger |
| Detailed artifact exact literal local filenames, IDs/versions, SHA-256 values, and links | List every file Stage B must receive; no directory path, alias, or renamed substitute |
| Revised freeze-verification record exact filename/hash | `STAGE-A-REVISED-FREEZE-RECORD.md` / |
| Governing revised manifest exact filename/hash | `STAGE-A-REVISED-FREEZE-SHA256SUMS` / |
| Verified handoff-input manifest | `STAGE-A-HANDOFF-INPUT-SHA256SUMS` |

Evidence guard: keep an authorized limit, unproved hypothesis, reported
exposure, and observed terminal consequence separate. Do not invent a numeric
budget. Link the four-order/correction register when any order remains open or
`UNKNOWN`.

- Revised Stage A manifest-verification timestamp/timezone from the detached record:
- Revised freeze record verified: yes / no
- Governing revised manifest verified: yes / no

Do not put this handoff's own hash, future verification timestamp, or claim of
successful freeze inside this file. After its `HANDOFF COMPLETE` bytes exist,
the facilitator creates `STAGE-A-HANDOFF-SHA256SUMS`, verifies it, and only
then creates `STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md`. Stage B Phase 1
hashes and verifies that completed triple.
