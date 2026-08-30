#!/usr/bin/env python3
"""Adversarial regression suite for the reader-value temporal protocol."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PACKET_RELATIVE = Path("testing/agentic-reader-value-v1")
PROTOCOL_RELATIVE = PACKET_RELATIVE / "TEMPORAL-FREEZE-PROTOCOL.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_protocol(root: Path, protocol: dict) -> None:
    (root / PROTOCOL_RELATIVE).write_text(
        json.dumps(protocol, indent=2) + "\n", encoding="utf-8"
    )


def refresh_protected_hash(root: Path, relative: str) -> None:
    protocol_path = root / PROTOCOL_RELATIVE
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    protocol["protected_documents"][relative] = digest(
        root / PACKET_RELATIVE / relative
    )
    write_protocol(root, protocol)


def refresh_packet_manifest(root: Path) -> None:
    manifest = root / PACKET_RELATIVE / "SHA256SUMS"
    refreshed = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        _, relative = line.split("  ", 1)
        refreshed.append(f"{digest(manifest.parent / relative)}  {relative}")
    manifest.write_text("\n".join(refreshed) + "\n", encoding="utf-8")


def mutate_protocol(root: Path, mutation) -> None:
    protocol_path = root / PROTOCOL_RELATIVE
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    mutation(protocol)
    write_protocol(root, protocol)


def mutate_log_schema(root: Path, mutation) -> None:
    path = root / PACKET_RELATIVE / "facilitator-only/05-execution-access-log-schema.json"
    schema = json.loads(path.read_text(encoding="utf-8"))
    mutation(schema)
    path.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")


def remove_release_binding(release_id: str):
    def mutation(protocol: dict) -> None:
        release = next(
            item for item in protocol["release_triples"] if item["id"] == release_id
        )
        release["required_prior_bundle"].remove("detached_record")
        release["exact_membership"].remove("detached_record")

    return mutation


def change_text(root: Path, relative: str, old: str, new: str) -> None:
    path = root / PACKET_RELATIVE / relative
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise AssertionError(f"mutation fixture not unique in {relative}: {old!r}")
    path.write_text(content.replace(old, new, 1), encoding="utf-8")
    refresh_protected_hash(root, relative)


def change_all_text(root: Path, relative: str, old: str, new: str) -> None:
    path = root / PACKET_RELATIVE / relative
    content = path.read_text(encoding="utf-8")
    if old not in content:
        raise AssertionError(f"mutation fixture absent in {relative}: {old!r}")
    path.write_text(content.replace(old, new), encoding="utf-8")
    refresh_protected_hash(root, relative)


def append_text(root: Path, relative: str, text: str) -> None:
    path = root / PACKET_RELATIVE / relative
    path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")
    refresh_protected_hash(root, relative)


def mutations():
    def self_hash(protocol: dict) -> None:
        protocol["freeze_chains"][0]["manifest_membership"].append(
            "governing_manifest"
        )

    def reversed_order(protocol: dict) -> None:
        protocol["freeze_chains"][0]["order"] = [
            "complete",
            "record",
            "manifest",
            "verify",
        ]

    def same_path_correction(protocol: dict) -> None:
        requirements = protocol["correction_requirements"]
        requirements["new_filename"] = False
        requirements["new_artifact_id"] = False
        requirements["new_version"] = False

    def incomplete_record_contract(protocol: dict) -> None:
        protocol["detached_record_contract"]["required_fields"].remove(
            "record_completion_timestamp"
        )

    def incomplete_log_order(protocol: dict) -> None:
        protocol["execution_access_log"]["ordered_phase_events"].remove("FILE_OPENED")

    def allow_undeclared_input(protocol: dict) -> None:
        protocol["orchestration_input_policy"]["undeclared_inputs_forbidden"] = False

    def allow_stale_revised_identity(protocol: dict) -> None:
        protocol["content_guards"][
            "revised_current_identity_must_differ_from_initial_identity_version_pair"
        ] = False

    def log_actor_without_code(schema: dict) -> None:
        schema["properties"]["actor"]["required"].remove("code")

    def omit_entry_branch(protocol: dict) -> None:
        protocol["entry_branches"]["selection_required"] = False

    def mix_entry_branches(protocol: dict) -> None:
        protocol["entry_branches"]["mutually_exclusive"] = False

    def remove_full_route_event(event: str):
        def mutation(protocol: dict) -> None:
            protocol["full_route_closure"]["required_boundary_events"].remove(event)

        return mutation

    def remove_results_identity(protocol: dict) -> None:
        protocol["full_route_closure"]["results"].pop("artifact_id")

    def close_before_results(protocol: dict) -> None:
        events = protocol["full_route_closure"]["required_boundary_events"]
        results_index = events.index("RUN_RESULTS_COMPLETED")
        close_index = events.index("LOG_CLOSED")
        events[results_index], events[close_index] = events[close_index], events[results_index]

    def debrief_before_scoring(protocol: dict) -> None:
        events = protocol["full_route_closure"]["required_boundary_events"]
        scoring_index = events.index("SCORING_ENDED")
        debrief_index = events.index("DEBRIEF_INPUT_MANIFEST_VERIFIED")
        events[scoring_index], events[debrief_index] = (
            events[debrief_index],
            events[scoring_index],
        )

    def remove_external_closeout(protocol: dict) -> None:
        protocol["full_route_closure"].pop("external_closeout")

    def allow_layout_claim_without_proof(protocol: dict) -> None:
        protocol["handoff_layout_proof"][
            "favorable_claim_requires_passing_proof"
        ] = False

    return [
        (
            "self-or-later-record hashing",
            lambda root: mutate_protocol(root, self_hash),
            "manifest_membership",
        ),
        (
            "record before manifest verification",
            lambda root: mutate_protocol(root, reversed_order),
            ".order must equal",
        ),
        *[
            (
                f"missing completed-triple binding: {release_id}",
                lambda root, release_id=release_id: mutate_protocol(
                    root, remove_release_binding(release_id)
                ),
                "must bind the completed triple",
            )
            for release_id in (
                "initial_to_live_update",
                "revised_to_handoff",
                "handoff_to_stage_b_section_1",
                "section_1_to_section_2",
                "section_2_to_sections_3_5",
            )
        ],
        (
            "same-path and unchanged-ID correction",
            lambda root: mutate_protocol(root, same_path_correction),
            "immutable correction requirements",
        ),
        (
            "detached record omits later record completion time",
            lambda root: mutate_protocol(root, incomplete_record_contract),
            "detached-record contract",
        ),
        (
            "execution log omits exact file-open event",
            lambda root: mutate_protocol(root, incomplete_log_order),
            "execution/access-log contract",
        ),
        (
            "execution log actor has no required code",
            lambda root: mutate_log_schema(root, log_actor_without_code),
            "execution-log actor code/role",
        ),
        (
            "undeclared orchestration input is allowed",
            lambda root: mutate_protocol(root, allow_undeclared_input),
            "orchestration-input policy",
        ),
        (
            "stale revised identity is allowed",
            lambda root: mutate_protocol(root, allow_stale_revised_identity),
            "content guards",
        ),
        (
            "revised workbook no longer requires new current identity",
            lambda root: change_text(
                root,
                "participant/03-practitioner-workbook.md",
                "new current ID/version and the initial ID/version it supersedes",
                "current ID/version and a related initial artifact",
            ),
            "omits required semantic guard 'current ID/version and the initial ID/version it supersedes'",
        ),
        (
            "reported fictional effects are contradicted",
            lambda root: append_text(
                root,
                "participant/02-scenario-and-task.md",
                "\nNo implementation, enforcement test, or execution occurred.\n",
            ),
            "stale no-execution wording contradicts reported effects",
        ),
        (
            "candidate scope and present authority are conflated",
            lambda root: change_text(
                root,
                "participant/05-one-screen-handoff.md",
                "| Candidate proposal scope under evaluation | This is proposed scope, not proof of authority |",
                "| Authorized proposal scope | The proposed scope is authorized |",
            ),
            "omits required semantic guard 'Candidate proposal scope under evaluation'",
        ),
        (
            "largest unacceptable outcome is optional",
            lambda root: change_text(
                root,
                "participant/05-one-screen-handoff.md",
                "| Largest unacceptable outcome (required; blank invalid) | Write the outcome, or `UNKNOWN` plus the evidence owner/trigger |",
                "| Largest risk, optional | |",
            ),
            "handoff must require a nonblank largest unacceptable outcome",
        ),
        (
            "Stage B Phase 1 deferred fields remain unresolved",
            lambda root: change_all_text(
                root,
                "participant/04-decision-owner-workbook.md",
                "NOT RELEASED — PHASE 2 CHECK",
                "UNKNOWN",
            ),
            "Stage B Phase 1 has unresolved withheld fields",
        ),
        (
            "detached record drops observed stdout",
            lambda root: change_text(
                root,
                "facilitator-only/04-freeze-and-correction-record-templates.md",
                "- Exact observed verification stdout, verbatim:\n",
                "",
            ),
            "omits required semantic guard 'Exact observed verification stdout, verbatim'",
        ),
        (
            "stale pending handoff state",
            lambda root: change_text(
                root,
                "participant/05-one-screen-handoff.md",
                "| Handoff state before hashing | `HANDOFF COMPLETE` / invalid |",
                "| Handoff state before hashing | `PENDING FREEZE` / invalid |",
            ),
            "handoff state field",
        ),
        (
            "incomplete results inventory",
            lambda root: change_text(
                root,
                "facilitator-only/03-results-and-deviation-log.md",
                "| Stage B Sections 3-5 | | | | | N/A |\n",
                "",
            ),
            "results log must contain all six freeze rows",
        ),
        (
            "cross-document artifact version mismatch",
            lambda root: change_text(
                root,
                "participant/05-one-screen-handoff.md",
                "AG-A-ONE-SCREEN-HANDOFF-v1.md",
                "AG-A-ONE-SCREEN-HANDOFF-v2.md",
            ),
            "omits AG-A-ONE-SCREEN-HANDOFF-v1.md",
        ),
        (
            "entry branch selection is omitted",
            lambda root: mutate_protocol(root, omit_entry_branch),
            "entry branches are incomplete, mixed, or stale",
        ),
        (
            "human and synthetic entry branches may be mixed",
            lambda root: mutate_protocol(root, mix_entry_branches),
            "entry branches are incomplete, mixed, or stale",
        ),
        (
            "synthetic context claims a human result",
            lambda root: append_text(
                root,
                "participant/01-synthetic-context-record.md",
                "\nHuman consent obtained.\n",
            ),
            "synthetic context claims human consent or human results",
        ),
        *[
            (
                f"full route omits {event}",
                lambda root, event=event: mutate_protocol(
                    root, remove_full_route_event(event)
                ),
                "full-route closure is incomplete or stale",
            )
            for event in (
                "STAGE_A_STARTED",
                "STAGE_A_ENDED",
                "STAGE_B_STARTED",
                "SCORING_ENDED",
                "DEBRIEF_INPUT_MANIFEST_VERIFIED",
                "DEBRIEF_COMPLETED",
                "STAGE_B_ENDED",
                "RUN_RESULTS_COMPLETED",
            )
        ],
        (
            "run-specific results identity is missing",
            lambda root: mutate_protocol(root, remove_results_identity),
            "full-route closure is incomplete or stale",
        ),
        (
            "log closes before immutable run results",
            lambda root: mutate_protocol(root, close_before_results),
            "full-route closure is incomplete or stale",
        ),
        (
            "debrief input is admitted before scoring ends",
            lambda root: mutate_protocol(root, debrief_before_scoring),
            "full-route closure is incomplete or stale",
        ),
        (
            "run results predict the future final log hash",
            lambda root: append_text(
                root,
                "facilitator-only/03-results-and-deviation-log.md",
                "\nFinal closed-log SHA-256: `PREDICTED`\n",
            ),
            "run results predict the future closed-log hash",
        ),
        (
            "external closeout is omitted",
            lambda root: mutate_protocol(root, remove_external_closeout),
            "full-route closure is incomplete or stale",
        ),
        (
            "favorable one-page claim is allowed without proof",
            lambda root: mutate_protocol(root, allow_layout_claim_without_proof),
            "one-page handoff proof contract is incomplete or stale",
        ),
    ]


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_repository.py"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    positive = run_validator(ROOT)
    if positive.returncode != 0:
        print("positive control failed", file=sys.stderr)
        print(positive.stdout, file=sys.stderr)
        print(positive.stderr, file=sys.stderr)
        return 1
    print("PASS positive control")

    failures = 0
    cases = mutations()
    with tempfile.TemporaryDirectory(prefix="ag-temporal-mutations-") as temporary:
        for index, (name, mutation, expected_error) in enumerate(cases, start=1):
            copy = Path(temporary) / f"case-{index:02d}"
            shutil.copytree(
                ROOT,
                copy,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            mutation(copy)
            refresh_packet_manifest(copy)
            result = run_validator(copy)
            evidence = result.stdout + result.stderr
            if result.returncode == 0 or expected_error not in evidence:
                failures += 1
                print(f"FAIL {name}: mutation was not rejected for {expected_error!r}")
            else:
                print(f"PASS rejected {name}")

    if failures:
        print(f"temporal mutation suite failed with {failures} error(s)", file=sys.stderr)
        return 1
    print(
        f"temporal mutation suite passed: positive control plus {len(cases)} rejected mutations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
