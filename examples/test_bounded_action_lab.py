"""Executable examples for the declared local boundary, not field evidence."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest

from bounded_action_lab import BASE, CONTENT, Lab, LostResponse, digest


class BoundedActionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.lab = Lab(Path(self.temp.name) / "lab.sqlite", clock=lambda: 240)
        self.lab.initialize()

    def attach(self, **kwargs):
        return self.lab.attach(kwargs.pop("actor", "case-draft-worker"),
                               kwargs.pop("grant_id", "ATTACH-G1"),
                               kwargs.pop("request", BASE), kwargs.pop("content", CONTENT), **kwargs)

    def count(self, table):
        with self.lab.connect() as con:
            return con.execute("SELECT COUNT(*) FROM " + table).fetchone()[0]

    def test_exact_request_commits_bytes_and_receipt(self):
        result = self.attach()
        self.assertEqual("ALLOWED", result["decision"])
        self.assertEqual("ATTACHED", result["receipt"]["outcome"])
        with self.lab.connect() as con:
            self.assertEqual(CONTENT, con.execute("SELECT content FROM attachments").fetchone()[0])
        self.assertEqual(1, self.count("receipts"))

    def test_identical_retry_returns_same_outcome(self):
        first = self.attach()
        retry = self.attach()
        self.assertEqual("EXISTING", retry["decision"])
        self.assertEqual(first["receipt"], retry["receipt"])
        self.assertEqual(1, self.count("attachments"))

    def test_wrong_actor_or_missing_grant_denied(self):
        self.assertEqual("DENIED", self.attach(actor="other-worker")["decision"])
        self.assertEqual("DENIED", self.attach(grant_id="missing")["decision"])
        self.assertEqual(0, self.count("attachments"))

    def test_every_bound_field_substitution_denied(self):
        for field in ("operation", "tenant", "partner", "dispute", "action", "purpose", "visibility"):
            with self.subTest(field=field):
                self.assertEqual("DENIED", self.attach(request=replace(BASE, **{field: "substituted"}))["decision"])
        self.assertEqual(0, self.count("attachments"))

    def test_changed_bytes_and_changed_digest_denied(self):
        changed = b"Credit approved."
        self.assertEqual("content_bytes", self.attach(content=changed)["reason"])
        self.assertEqual("DENIED", self.attach(content=changed,
                         request=replace(BASE, content_digest=digest(changed)))["decision"])
        self.assertEqual(0, self.count("attachments"))

    def test_same_key_different_payload_conflicts_after_commit(self):
        self.attach()
        result = self.attach(request=replace(BASE, visibility="public"))
        self.assertEqual("operation_conflict", result["reason"])
        self.assertEqual(1, self.count("attachments"))

    def test_revocation_before_prevents_effect(self):
        self.assertFalse(self.lab.revoke("agent"))
        self.assertTrue(self.lab.revoke("Nia"))
        self.assertEqual("revoked", self.attach()["reason"])
        self.assertEqual(0, self.count("attachments"))

    def test_revocation_after_preserves_history(self):
        first = self.attach()
        self.lab.revoke("Rosa")
        self.assertEqual(first["receipt"], self.lab.reconcile("case-draft-worker", BASE.operation))
        self.assertEqual("EXISTING", self.attach()["decision"])
        self.assertEqual(1, self.count("attachments"))

    def test_expiry_and_not_before_exclude_new_effect(self):
        for instant in (-1, 900, 901):
            self.lab.clock = lambda value=instant: value
            self.assertEqual("time_window", self.attach()["reason"])
        self.lab.clock = lambda: 0
        self.assertEqual("ALLOWED", self.attach()["decision"])

    def test_reassignment_reverses_permission(self):
        self.lab.reassign("another-team")
        self.assertEqual("case_eligibility", self.attach()["reason"])
        self.assertEqual(0, self.count("attachments"))

    def test_lost_response_reconciles_without_duplicate(self):
        with self.assertRaises(LostResponse):
            self.attach(lose_response=True)
        self.assertEqual("ATTACHED", self.lab.reconcile("case-draft-worker", BASE.operation)["outcome"])
        self.assertIsNone(self.lab.reconcile("other-worker", BASE.operation))
        self.assertEqual("EXISTING", self.attach()["decision"])
        self.assertEqual(1, self.count("attachments"))

    def test_concurrent_identical_requests_one_effect(self):
        barrier = threading.Barrier(2)
        def run():
            barrier.wait()
            return self.attach()["decision"]
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(lambda _: run(), range(2)))
        self.assertCountEqual(["ALLOWED", "EXISTING"], results)
        self.assertEqual(1, self.count("attachments"))

    def test_concurrent_different_operations_cannot_expand_grant(self):
        barrier = threading.Barrier(2)
        def run(request):
            barrier.wait()
            return self.attach(request=request)["decision"]
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(run, [BASE, replace(BASE, operation="attach-draft/D-1042/v2")]))
        self.assertCountEqual(["ALLOWED", "DENIED"], results)
        self.assertEqual(1, self.count("attachments"))

    def test_concurrent_same_key_changed_payload_cannot_win(self):
        barrier = threading.Barrier(2)
        def run(request):
            barrier.wait()
            return self.attach(request=request)["decision"]
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(run, [BASE, replace(BASE, visibility="public")]))
        self.assertCountEqual(["ALLOWED", "DENIED"], results)
        self.assertEqual(1, self.count("attachments"))

    def test_receipt_write_failure_rolls_back_attachment(self):
        with self.lab.connect() as con:
            con.execute("CREATE TRIGGER reject_receipt BEFORE INSERT ON receipts BEGIN SELECT RAISE(ABORT, 'injected'); END")
        self.assertEqual("UNKNOWN", self.attach()["decision"])
        self.assertEqual(0, self.count("attachments"))
        self.assertEqual(0, self.count("receipts"))

    def test_unavailable_store_cannot_authorize_effect(self):
        unavailable = Lab(Path(self.temp.name) / "missing" / "lab.sqlite", clock=lambda: 240)
        self.assertEqual("UNKNOWN", unavailable.attach("case-draft-worker", "ATTACH-G1", BASE, CONTENT)["decision"])
        self.assertEqual(0, self.count("attachments"))


if __name__ == "__main__":
    unittest.main()
