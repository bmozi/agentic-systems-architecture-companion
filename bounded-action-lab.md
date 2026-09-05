# A local lab: one approved internal attachment

This exercise lets you see a useful permission succeed and then change one fact to make it fail. The agent role may attach one approved draft to one assigned case. A new destination, new content, expired permission, or prior revocation prevents a new effect.

The lab uses Python's standard library and a temporary SQLite database. It calls no model, external service, finance system, or messaging system. Its invented Northbridge fixture is separate from the restricted credit gate and EXP-001 through EXP-005. Those experiments do not acquire results from this exercise.

## Run it

From the repository root:

```sh
python3 examples/bounded_action_lab.py
python3 -m unittest discover -s examples -p 'test_bounded_action_lab.py' -v
```

The demonstration prints `ALLOWED` with an `ATTACHED` receipt, then `EXISTING` with the same receipt. It removes its temporary database when finished. The tests create their own isolated temporary databases.

## Read the permission

Rosa's fictional grant `ATTACH-G1` permits `case-draft-worker` to perform `attach_internal_draft` for `internal_evidence_review`. The destination is Northbridge tenant, partner PX-44, dispute D-1042; visibility is `assigned_team`. The case must remain open and assigned to `Rosa-team`. Rosa or Nia can revoke the grant. Their names and the workload identity are fixture strings, not authenticated identities.

The exact content is UTF-8 `Draft: evidence review pending.` without a trailing newline. The operation is `attach-draft/D-1042/v1`. All eight request fields are bound: `operation`, `tenant`, `partner`, `dispute`, `action`, `purpose`, `visibility`, and `content_digest`.

`content_digest` is SHA-256 of the content bytes. The request fingerprint is SHA-256 of its UTF-8 JSON, serialized with Python `json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",", ":"))`. These fields are strings in this fixture. This local serialization convention is `ATTACH-JSON-1`; it is not a claim of cross-language canonical JSON interoperability. The grant stores both approved digests. Matching a digest establishes identity with the approved input; the fixture's stipulated human approval establishes why those bytes are allowed.

The injected clock uses seconds since the scenario's 10:00 start. New effects are eligible from `0` inclusive to `900` exclusive. The demo's clock returns `240`, representing 10:04. This makes boundary tests repeatable without waiting fifteen minutes.

## Find the transaction boundary

`BEGIN IMMEDIATE` serializes writers to the same SQLite database. Within that boundary, the code reads current grant and case state, compares actor and scope, checks the sampled clock, and writes both the attachment and receipt. The operation is unique. A failed receipt insertion rolls back the attachment too. An identical retry returns the existing receipt; a changed request with the same operation is rejected.

Revocation writes to the same database under the same writer transaction rule. When revocation orders first, attachment is denied. When attachment commits first, later revocation leaves the historical receipt intact. Returning that receipt after revocation is observation of a past effect, not permission for a new one.

The lab has deliberately placed the effect itself inside SQLite. An attachment to a remote document system would not share this transaction merely because its authorization row did. That design would require its own idempotency, revocation, reconciliation, and correction analysis.

## Try a changed fact

Before inspecting the tests, predict these outcomes:

1. The approved request arrives at 10:04 and the case remains eligible.
2. The workload changes only visibility to `public`.
3. Rosa moves the case to another team before attachment.
4. Nia revokes before the effect.
5. The database commits, but the response disappears.
6. Two workers issue the identical request concurrently.
7. The permission expires after attachment but before an identical retry.

Answers: (1) `ALLOWED`, with one durable `ATTACHED` receipt. (2–4) `DENIED`, with no new attachment. (5) The caller has an unknown outcome; it looks up the original operation rather than creating a new one. (6) One request creates the effect, and the other returns `EXISTING`. (7) Returning the historical receipt remains possible; no new effect occurs.

A missing operation in a successful lookup means no committed receipt was visible to that lookup. It is not a prediction that no concurrent or future request can commit. An unavailable lookup returns `UNKNOWN`. Responsibility remains with the operator until the outcome is established.

## What the result establishes

The retained local verification records sixteen passing tests for the named fixture and code version. They exercise permission comparisons, content binding, retries, concurrency, rollback, and reconciliation inside this small process/database model. They are executed local results; the Chapter 16 narrative's stipulated results remain a different evidence category.

The clock sample is the lab's logical effect ordering point. The program does not guarantee that disk commit or visibility occurs before a real wall-clock expiry after that sample. It assumes a suitable clock and SQLite transaction behavior; it does not test clock tampering, distributed consistency, operating-system failure, power loss, forged credentials, model behavior, malicious administrators, or external effects. Caught database failures return an unknown outcome; an unexpected cleanup failure can propagate as an exception. Neither authorizes another operation identity. This example does not implement a production audit sink, attachment removal, or identity provider.

Use the exercise to explain a bounded decision and to identify the boundary your implementation would need to preserve. These tests establish neither general safety nor practitioner effectiveness, production readiness, credit authority, or measured business benefit.
