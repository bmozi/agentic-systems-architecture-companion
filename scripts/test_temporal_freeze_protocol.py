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
    with tempfile.TemporaryDirectory(prefix="ag-temporal-mutations-") as temporary:
        for index, (name, mutation, expected_error) in enumerate(mutations(), start=1):
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
    print("temporal mutation suite passed: positive control plus 11 rejected mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
