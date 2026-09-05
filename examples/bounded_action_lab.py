"""Local teaching model; no model calls, remote services, or production identity."""
from dataclasses import asdict, dataclass
import hashlib
import json
import sqlite3
import time


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class Request:
    operation: str
    tenant: str
    partner: str
    dispute: str
    action: str
    purpose: str
    visibility: str
    content_digest: str

    def canonical(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"))

    def fingerprint(self) -> str:
        return digest(self.canonical().encode("utf-8"))


CONTENT = b"Draft: evidence review pending."
BASE = Request("attach-draft/D-1042/v1", "Northbridge", "PX-44", "D-1042",
               "attach_internal_draft", "internal_evidence_review",
               "assigned_team", digest(CONTENT))


class LostResponse(Exception):
    """The commit happened, but the simulated caller did not receive its reply."""


class Lab:
    def __init__(self, path, clock=time.time):
        self.path = str(path)
        self.clock = clock

    def connect(self):
        con = sqlite3.connect(self.path, timeout=5, isolation_level=None)
        con.row_factory = sqlite3.Row
        return con

    def initialize(self):
        with self.connect() as con:
            con.executescript('''
              CREATE TABLE grants (
                id TEXT PRIMARY KEY, actor TEXT, fingerprint TEXT,
                content_digest TEXT, team TEXT, active INTEGER,
                not_before REAL, expires REAL);
              CREATE TABLE cases (
                tenant TEXT, partner TEXT, dispute TEXT, team TEXT,
                is_open INTEGER, version INTEGER,
                PRIMARY KEY (tenant, partner, dispute));
              CREATE TABLE attachments (
                operation TEXT PRIMARY KEY, attachment_id TEXT UNIQUE,
                content BLOB NOT NULL);
              CREATE TABLE receipts (
                operation TEXT PRIMARY KEY, actor TEXT, grant_id TEXT,
                fingerprint TEXT, content_digest TEXT, case_version INTEGER,
                attachment_id TEXT, effect_time REAL, outcome TEXT);
            ''')
            con.execute("INSERT INTO grants VALUES (?,?,?,?,?,?,?,?)",
                        ("ATTACH-G1", "case-draft-worker", BASE.fingerprint(),
                         BASE.content_digest, "Rosa-team", 1, 0, 900))
            con.execute("INSERT INTO cases VALUES (?,?,?,?,?,?)",
                        ("Northbridge", "PX-44", "D-1042", "Rosa-team", 1, 1))

    def attach(self, actor, grant_id, request, content, lose_response=False):
        """ALLOWED is one committed effect; UNKNOWN never authorizes another key."""
        con = None
        result = None
        try:
            con = self.connect()
            con.execute("BEGIN IMMEDIATE")
            grant = con.execute("SELECT * FROM grants WHERE id=?", (grant_id,)).fetchone()
            if grant is None or actor != grant["actor"]:
                return {"decision": "DENIED", "reason": "actor_or_grant"}
            if digest(content) != request.content_digest:
                return {"decision": "DENIED", "reason": "content_bytes"}
            prior = con.execute("SELECT * FROM receipts WHERE operation=?",
                                (request.operation,)).fetchone()
            if prior:
                if (prior["fingerprint"] != request.fingerprint()
                        or prior["grant_id"] != grant_id or prior["actor"] != actor):
                    return {"decision": "DENIED", "reason": "operation_conflict"}
                # Historical outcome lookup does not grant a new effect.
                return {"decision": "EXISTING", "receipt": dict(prior)}
            if (request.fingerprint() != grant["fingerprint"]
                    or request.content_digest != grant["content_digest"]):
                return {"decision": "DENIED", "reason": "scope_or_content"}
            case = con.execute("SELECT * FROM cases WHERE tenant=? AND partner=? AND dispute=?",
                               (request.tenant, request.partner, request.dispute)).fetchone()
            if not case or not case["is_open"] or case["team"] != grant["team"]:
                return {"decision": "DENIED", "reason": "case_eligibility"}
            # This sampled instant is the lab's logical effect ordering point.
            now = self.clock()
            if not grant["active"]:
                return {"decision": "DENIED", "reason": "revoked"}
            if not (grant["not_before"] <= now < grant["expires"]):
                return {"decision": "DENIED", "reason": "time_window"}
            attachment_id = "ATT-" + digest(request.operation.encode())[:16]
            con.execute("INSERT INTO attachments VALUES (?,?,?)",
                        (request.operation, attachment_id, content))
            receipt = (request.operation, actor, grant_id, request.fingerprint(),
                       request.content_digest, case["version"], attachment_id, now, "ATTACHED")
            con.execute("INSERT INTO receipts VALUES (?,?,?,?,?,?,?,?,?)", receipt)
            result = dict(con.execute("SELECT * FROM receipts WHERE operation=?",
                                      (request.operation,)).fetchone())
            con.commit()
        except (sqlite3.Error, OSError):
            return {"decision": "UNKNOWN", "reason": "store_unavailable_or_commit_uncertain"}
        finally:
            if con is not None:
                if con.in_transaction:
                    con.rollback()
                con.close()
        if lose_response:
            raise LostResponse(request.operation)
        return {"decision": "ALLOWED", "receipt": result}

    def reconcile(self, actor, operation):
        try:
            with self.connect() as con:
                row = con.execute("SELECT * FROM receipts WHERE operation=? AND actor=?",
                                  (operation, actor)).fetchone()
                return dict(row) if row else None
        except sqlite3.Error:
            return {"outcome": "UNKNOWN"}

    def revoke(self, revoker, grant_id="ATTACH-G1"):
        if revoker not in ("Rosa", "Nia"):
            return False
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            count = con.execute("UPDATE grants SET active=0 WHERE id=?", (grant_id,)).rowcount
            con.commit()
            return count == 1

    def reassign(self, team):
        # Fixture administration, not an agent capability.
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            con.execute("UPDATE cases SET team=?, version=version+1", (team,))
            con.commit()


if __name__ == "__main__":
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as directory:
        lab = Lab(Path(directory) / "lab.sqlite", clock=lambda: 240)
        lab.initialize()
        print(json.dumps(lab.attach("case-draft-worker", "ATTACH-G1", BASE, CONTENT), indent=2))
        print(json.dumps(lab.attach("case-draft-worker", "ATTACH-G1", BASE, CONTENT), indent=2))
