#!/usr/bin/env python3
"""Validate the companion repository's reader routes and local links."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "companion.json"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{7,40}$")
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")
FREEZE_ORDER = ["complete", "manifest", "verify", "record"]
PRIOR_TRIPLE = ["governed_outputs", "governing_manifest", "detached_record"]
PACKET_VERSION = "1.2.3"
REQUIRED_RECORD_FIELDS = [
    "attempt_id",
    "phase_id",
    "facilitator_code",
    "actor_code",
    "verification_command",
    "verification_stdout",
    "verification_stderr",
    "verification_exit_code",
    "verification_timestamp",
    "verification_timezone",
    "record_completion_timestamp",
    "record_completion_timezone",
    "governing_manifest_filename",
    "governing_manifest_sha256",
    "execution_log_filename",
    "execution_log_checkpoint_sequence",
    "execution_log_checkpoint_entry_sha256",
    "governed_artifacts",
]
ORDERED_LOG_EVENTS = [
    "PHASE_INPUT_MANIFEST_CREATED",
    "PHASE_INPUT_MANIFEST_VERIFIED",
    "FILE_RELEASED",
    "FILE_OPENED",
    "OUTPUT_COMPLETED",
    "GOVERNING_MANIFEST_CREATED",
    "GOVERNING_MANIFEST_VERIFIED",
    "DETACHED_RECORD_COMPLETED",
    "PHASE_COMPLETED",
]
ALL_LOG_EVENTS = [
    "ATTEMPT_STARTED",
    "ORCHESTRATION_MANIFEST_VERIFIED",
    *ORDERED_LOG_EVENTS,
    "DEVIATION",
    "STOP",
    "LOG_CLOSED",
]
LOG_PHASES = [
    "attempt",
    "stage_a_initial",
    "stage_a_revised",
    "stage_a_handoff",
    "stage_b_section_1",
    "stage_b_section_2",
    "stage_b_sections_3_5",
    "closeout",
]
PHASE_PROTOCOL = {
    "stage_a_initial": {
        "results_label": "Initial Stage A",
        "state": "INITIAL COMPLETE",
        "manifest": "STAGE-A-INITIAL-SHA256SUMS",
        "record": "STAGE-A-INITIAL-FREEZE-VERIFICATION-RECORD.md",
        "next_release": "initial_to_live_update",
        "output": None,
    },
    "stage_a_revised": {
        "results_label": "Revised Stage A",
        "state": "REVISED COMPLETE",
        "manifest": "STAGE-A-REVISED-FREEZE-SHA256SUMS",
        "record": "STAGE-A-REVISED-FREEZE-RECORD.md",
        "next_release": "revised_to_handoff",
        "output": None,
    },
    "stage_a_handoff": {
        "results_label": "Handoff",
        "state": "HANDOFF COMPLETE",
        "manifest": "STAGE-A-HANDOFF-SHA256SUMS",
        "record": "STAGE-A-HANDOFF-FREEZE-VERIFICATION-RECORD.md",
        "next_release": "handoff_to_stage_b_section_1",
        "output": ("AG-A-ONE-SCREEN-HANDOFF", "1", "AG-A-ONE-SCREEN-HANDOFF-v1.md"),
    },
    "stage_b_section_1": {
        "results_label": "Stage B Section 1",
        "state": "SECTION 1 COMPLETE",
        "manifest": "STAGE-B-SECTION-1-SHA256SUMS",
        "record": "STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md",
        "next_release": "section_1_to_section_2",
        "output": ("STAGE-B-SECTION-1", "1", "STAGE-B-SECTION-1-v1.md"),
    },
    "stage_b_section_2": {
        "results_label": "Stage B Section 2",
        "state": "SECTION 2 COMPLETE",
        "manifest": "STAGE-B-SECTION-2-SHA256SUMS",
        "record": "STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md",
        "next_release": "section_2_to_sections_3_5",
        "output": ("STAGE-B-SECTION-2", "1", "STAGE-B-SECTION-2-v1.md"),
    },
    "stage_b_sections_3_5": {
        "results_label": "Stage B Sections 3-5",
        "state": "SECTIONS 3-5 COMPLETE",
        "manifest": "STAGE-B-SECTIONS-3-5-SHA256SUMS",
        "record": "STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md",
        "next_release": None,
        "output": ("STAGE-B-SECTIONS-3-5", "1", "STAGE-B-SECTIONS-3-5-v1.md"),
    },
}
RELEASE_PROTOCOL = {
    "initial_to_live_update": {
        "from_phase": "stage_a_initial",
        "manifest": "STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS",
        "new_inputs": ["live_update"],
    },
    "revised_to_handoff": {
        "from_phase": "stage_a_revised",
        "manifest": "STAGE-A-HANDOFF-INPUT-SHA256SUMS",
        "new_inputs": ["blank_handoff"],
    },
    "handoff_to_stage_b_section_1": {
        "from_phase": "stage_a_handoff",
        "manifest": "STAGE-B-PHASE-1-INPUT-SHA256SUMS",
        "new_inputs": ["packet_route", "blank_decision_owner_workbook"],
    },
    "section_1_to_section_2": {
        "from_phase": "stage_b_section_1",
        "manifest": "STAGE-B-PHASE-2-INPUT-SHA256SUMS",
        "new_inputs": [
            "scenario",
            "revised_governed_outputs",
            "revised_governing_manifest",
            "revised_detached_record",
        ],
    },
    "section_2_to_sections_3_5": {
        "from_phase": "stage_b_section_2",
        "manifest": "STAGE-B-PHASE-3-INPUT-SHA256SUMS",
        "new_inputs": ["executive_decision_brief", "value_and_evidence_ledger"],
    },
}
CORRECTION_REQUIREMENTS = {
    "preserve_prior_chain": True,
    "new_filename": True,
    "new_artifact_id": True,
    "new_version": True,
    "new_completion_timestamp": True,
    "new_governing_manifest": True,
    "new_verification_event": True,
    "new_detached_record": True,
    "new_next_release_manifest_when_applicable": True,
    "stop_current_attempt": True,
}
BINDING_DOCUMENTS = {
    "AG-A-ONE-SCREEN-HANDOFF": {
        "README.md",
        "participant/00-packet-route.md",
        "participant/05-one-screen-handoff.md",
    },
    "STAGE-B-SECTION-1": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
    "STAGE-B-SECTION-2": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
    "STAGE-B-SECTIONS-3-5": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
}
DETACHED_RECORD_CONTRACT = {
    "required_fields": REQUIRED_RECORD_FIELDS,
    "verification_output_must_be_verbatim": True,
    "successful_exit_code": 0,
    "record_completion_must_follow_verification": True,
    "phase_id_must_match_freeze_chain": True,
    "actor_codes_must_be_nonempty": True,
    "record_is_excluded_from_governing_manifest": True,
}
EXECUTION_LOG_PROTOCOL = {
    "template": "facilitator-only/05-execution-and-access-log.md",
    "entry_schema": "facilitator-only/05-execution-access-log-schema.json",
    "run_filename_pattern": "AG-EXECUTION-ACCESS-LOG-<ATTEMPT-ID>-v1.jsonl",
    "participant_input": False,
    "phase_input_member": False,
    "append_only": True,
    "one_exact_filename_per_entry": True,
    "continuity_fields": [
        "sequence",
        "previous_sequence",
        "previous_entry_sha256",
        "entry_sha256",
    ],
    "ordered_phase_events": ORDERED_LOG_EVENTS,
    "verification_event_required_fields": [
        "command",
        "stdout",
        "stderr",
        "exit_code",
        "timestamp",
        "timezone",
    ],
    "detached_record_checkpoint_event": "GOVERNING_MANIFEST_VERIFIED",
    "final_log_bound_by_closeout_manifest": True,
}
ORCHESTRATION_POLICY = {
    "human_participant_inputs_are_exact_phase_manifest_only": True,
    "facilitator_materials_are_not_participant_inputs": True,
    "synthetic_orchestration_requires_prior_immutable_files": True,
    "synthetic_orchestration_manifest": "ORCHESTRATION-INPUT-SHA256SUMS",
    "synthetic_orchestration_must_be_verified_before_delivery": True,
    "synthetic_results_must_be_labeled_orchestration_aided": True,
    "undeclared_inputs_forbidden": True,
    "undeclared_input_action": [
        "record_deviation",
        "stop_attempt",
        "preserve_partial_chain",
        "start_new_attempt",
    ],
}
CONTENT_GUARDS = {
    "revised_current_identity_must_differ_from_initial_identity_version_pair": True,
    "initial_identity_allowed_only_as_lineage_reference_in_revised_output": True,
    "fictional_reported_effects_must_not_be_described_as_no_execution_occurred": True,
    "fictional_reported_effects_are_not_real_world_execution_evidence": True,
    "candidate_proposal_scope_must_be_separate_from_present_authorization": True,
    "present_authorization_requires_current_authority_evidence": True,
    "handoff_required_field": "Largest unacceptable outcome (required; blank invalid)",
    "phase_1_not_released_literal": "NOT RELEASED — PHASE 2 CHECK",
    "phase_1_deferred_fields": [
        "revised_freeze_record_received_and_verified",
        "revised_governing_manifest_received_and_verified",
        "every_handoff_linked_filename_received_unchanged",
        "detailed_execution_evidence_verified",
    ],
}


def markdown_links(path: Path):
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_PATTERN.finditer(line):
            yield number, match.group(1).strip()


def local_target(source: Path, raw: str) -> Path | None:
    target = raw
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(" ", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None
    if decoded.startswith("/"):
        raise ValueError("absolute local path")
    resolved = (source.parent / decoded).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("link escapes repository") from exc
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_temporal_freeze_protocol(errors: list[str]) -> None:
    """Validate the canonical v1.2.3 freeze, release, and execution graph."""
    packet = ROOT / "testing" / "agentic-reader-value-v1"
    protocol_path = packet / "TEMPORAL-FREEZE-PROTOCOL.json"
    try:
        protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"temporal protocol inventory is unreadable: {exc}")
        return

    if protocol.get("schema_version") != 2:
        errors.append("temporal protocol: schema_version must be 2")
    if protocol.get("packet_id") != "AG-RV-PILOT-001":
        errors.append("temporal protocol: packet_id mismatch")
    if protocol.get("packet_version") != PACKET_VERSION:
        errors.append(f"temporal protocol: packet_version must be {PACKET_VERSION}")

    expected_states = [entry["state"] for entry in PHASE_PROTOCOL.values()]
    if protocol.get("allowed_completion_states") != expected_states:
        errors.append("temporal protocol: allowed completion states are incomplete or stale")

    chains = protocol.get("freeze_chains")
    if not isinstance(chains, list):
        errors.append("temporal protocol: freeze_chains must be a list")
        chains = []
    chain_by_id = {
        entry.get("id"): entry for entry in chains if isinstance(entry, dict)
    }
    if len(chain_by_id) != len(chains) or set(chain_by_id) != set(PHASE_PROTOCOL):
        errors.append("temporal protocol: freeze inventory must contain each of six phases exactly once")
    for phase, expected in PHASE_PROTOCOL.items():
        chain = chain_by_id.get(phase)
        if chain is None:
            continue
        checks = {
            "results_label": expected["results_label"],
            "output_role": "governed_outputs",
            "completion_state": expected["state"],
            "governing_manifest": expected["manifest"],
            "detached_record": expected["record"],
            "order": FREEZE_ORDER,
            "manifest_membership": ["governed_outputs"],
            "manifest_exclusions": ["governing_manifest", "detached_record"],
            "next_release": expected["next_release"],
        }
        for field, wanted in checks.items():
            if chain.get(field) != wanted:
                errors.append(f"temporal protocol: {phase}.{field} must equal {wanted!r}")
        output = expected["output"]
        actual_output = (
            chain.get("output_artifact_id"),
            chain.get("output_version"),
            chain.get("output_filename"),
        )
        if output is None:
            if actual_output != (None, None, None):
                errors.append(f"temporal protocol: {phase} must use the governed-output set")
        elif actual_output != output:
            errors.append(f"temporal protocol: {phase} artifact ID/version/filename mismatch")

    releases = protocol.get("release_triples")
    if not isinstance(releases, list):
        errors.append("temporal protocol: release_triples must be a list")
        releases = []
    release_by_id = {
        entry.get("id"): entry for entry in releases if isinstance(entry, dict)
    }
    if len(release_by_id) != len(releases) or set(release_by_id) != set(RELEASE_PROTOCOL):
        errors.append("temporal protocol: release inventory must contain each of five releases exactly once")
    for release_id, expected in RELEASE_PROTOCOL.items():
        release = release_by_id.get(release_id)
        if release is None:
            continue
        if release.get("from_phase") != expected["from_phase"]:
            errors.append(f"temporal protocol: {release_id} has the wrong predecessor")
        if release.get("manifest") != expected["manifest"]:
            errors.append(f"temporal protocol: {release_id} manifest filename mismatch")
        if release.get("required_prior_bundle") != PRIOR_TRIPLE:
            errors.append(f"temporal protocol: {release_id} must bind the completed triple")
        if release.get("new_inputs") != expected["new_inputs"]:
            errors.append(f"temporal protocol: {release_id} new-input inventory mismatch")
        exact_membership = PRIOR_TRIPLE + expected["new_inputs"]
        if release.get("exact_membership") != exact_membership:
            errors.append(f"temporal protocol: {release_id} exact membership mismatch")

    if protocol.get("detached_record_contract") != DETACHED_RECORD_CONTRACT:
        errors.append("temporal protocol: detached-record contract is incomplete or stale")
    if protocol.get("execution_access_log") != EXECUTION_LOG_PROTOCOL:
        errors.append("temporal protocol: execution/access-log contract is incomplete or stale")
    if protocol.get("orchestration_input_policy") != ORCHESTRATION_POLICY:
        errors.append("temporal protocol: orchestration-input policy is incomplete or stale")
    if protocol.get("content_guards") != CONTENT_GUARDS:
        errors.append("temporal protocol: content guards are incomplete or stale")

    if protocol.get("correction_requirements") != CORRECTION_REQUIREMENTS:
        errors.append("temporal protocol: immutable correction requirements are incomplete")
    if protocol.get("results_inventory") != list(PHASE_PROTOCOL):
        errors.append("temporal protocol: results inventory must list all six phases in order")

    bindings = protocol.get("artifact_bindings")
    if not isinstance(bindings, list):
        errors.append("temporal protocol: artifact_bindings must be a list")
        bindings = []
    binding_by_id = {
        entry.get("artifact_id"): entry for entry in bindings if isinstance(entry, dict)
    }
    expected_outputs = {
        value["output"][0]: value["output"]
        for value in PHASE_PROTOCOL.values()
        if value["output"] is not None
    }
    if len(binding_by_id) != len(bindings) or set(binding_by_id) != set(expected_outputs):
        errors.append("temporal protocol: artifact binding inventory mismatch")
    for artifact_id, expected in expected_outputs.items():
        binding = binding_by_id.get(artifact_id)
        if binding is None:
            continue
        wanted_documents = BINDING_DOCUMENTS[artifact_id]
        if (
            binding.get("version"),
            binding.get("filename"),
        ) != (expected[1], expected[2]):
            errors.append(f"temporal protocol: {artifact_id} version/filename mismatch")
        documents = binding.get("documents")
        if not isinstance(documents, list) or set(documents) != wanted_documents:
            errors.append(f"temporal protocol: {artifact_id} document binding mismatch")
            continue
        variant = re.compile(rf"{re.escape(artifact_id)}-v([0-9]+)\.md")
        for relative in documents:
            path = packet / relative
            if not path.is_file():
                errors.append(f"temporal protocol: missing binding document {relative}")
                continue
            content = path.read_text(encoding="utf-8")
            if expected[2] not in content:
                errors.append(f"temporal protocol: {relative} omits {expected[2]}")
            wrong_versions = {match.group(1) for match in variant.finditer(content)} - {expected[1]}
            if wrong_versions:
                errors.append(f"temporal protocol: {relative} has stale {artifact_id} versions")

    results_path = packet / "facilitator-only" / "03-results-and-deviation-log.md"
    try:
        results_text = results_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"temporal protocol: results inventory is unreadable: {exc}")
    else:
        section = results_text.split("## Temporal freeze chain", 1)
        section = section[1].split("\n## ", 1)[0] if len(section) == 2 else ""
        rows = []
        for line in section.splitlines():
            if not line.startswith("|") or line.startswith("| ---"):
                continue
            label = line.split("|", 2)[1].strip()
            if label and label != "Output phase":
                rows.append(label)
        expected_rows = [entry["results_label"] for entry in PHASE_PROTOCOL.values()]
        if rows != expected_rows or len(rows) != 6:
            errors.append("temporal protocol: results log must contain all six freeze rows in order")

    handoff_path = packet / "participant" / "05-one-screen-handoff.md"
    handoff_text = handoff_path.read_text(encoding="utf-8") if handoff_path.is_file() else ""
    state_rows = [
        line for line in handoff_text.splitlines()
        if line.startswith("| Handoff state before hashing |")
    ]
    if state_rows != ["| Handoff state before hashing | `HANDOFF COMPLETE` / invalid |"]:
        errors.append("temporal protocol: handoff state field must require HANDOFF COMPLETE")
    required_handoff_row = (
        "| Largest unacceptable outcome (required; blank invalid) | "
        "Write the outcome, or `UNKNOWN` plus the evidence owner/trigger |"
    )
    if required_handoff_row not in handoff_text:
        errors.append("temporal protocol: handoff must require a nonblank largest unacceptable outcome")

    schema_path = packet / EXECUTION_LOG_PROTOCOL["entry_schema"]
    try:
        log_schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"temporal protocol: execution-log entry schema is unreadable: {exc}")
    else:
        required_entry_fields = {
            "packet_id",
            "packet_version",
            "attempt_id",
            "sequence",
            "phase",
            "event_type",
            "actor",
            "exact_filename",
            "artifact",
            "timestamp",
            "timezone",
            "observation",
            "continuity",
        }
        if set(log_schema.get("required", [])) != required_entry_fields:
            errors.append("temporal protocol: execution-log schema required fields are incomplete")
        properties = log_schema.get("properties", {})
        if properties.get("packet_id", {}).get("const") != "AG-RV-PILOT-001":
            errors.append("temporal protocol: execution-log schema packet ID mismatch")
        if properties.get("packet_version", {}).get("const") != PACKET_VERSION:
            errors.append("temporal protocol: execution-log schema packet version mismatch")
        if properties.get("phase", {}).get("enum") != LOG_PHASES:
            errors.append("temporal protocol: execution-log phase inventory is incomplete")
        if properties.get("event_type", {}).get("enum") != ALL_LOG_EVENTS:
            errors.append("temporal protocol: execution-log event inventory is incomplete")
        actor = properties.get("actor", {})
        if set(actor.get("required", [])) != {"code", "role"}:
            errors.append("temporal protocol: execution-log actor code/role are not required")
        continuity = properties.get("continuity", {})
        if set(continuity.get("required", [])) != {
            "previous_sequence",
            "previous_entry_sha256",
            "entry_sha256",
        }:
            errors.append("temporal protocol: execution-log continuity fields are incomplete")
        verification_events = {
            "ORCHESTRATION_MANIFEST_VERIFIED",
            "PHASE_INPUT_MANIFEST_VERIFIED",
            "GOVERNING_MANIFEST_VERIFIED",
        }
        all_of = log_schema.get("allOf", [])
        guarded = set()
        for rule in all_of if isinstance(all_of, list) else []:
            guarded.update(
                rule.get("if", {})
                .get("properties", {})
                .get("event_type", {})
                .get("enum", [])
            )
        if guarded != verification_events:
            errors.append("temporal protocol: verification log events must require observations")

    required_snippets = {
        "participant/00-packet-route.md": [
            "Any undeclared input is a deviation,",
            "current ID/version pair must differ",
            "NOT RELEASED — PHASE 2 CHECK",
        ],
        "participant/02-scenario-and-task.md": [
            "candidate scope for evaluation",
            "present authorization is `NOT",
            "fictional reported effects exist; real-world execution evidence does not",
        ],
        "participant/03-practitioner-workbook.md": [
            "Present authorization and current authority evidence, or `NOT AUTHORIZED`",
            "current ID/version and the initial ID/version it supersedes",
            "FICTIONAL REPORTED EFFECTS EXIST;",
        ],
        "participant/04-decision-owner-workbook.md": [
            "Present authorization evidenced by the handoff",
            "Do not edit the frozen Section 1",
            "Presently authorized scope and current authority evidence, or `NOT AUTHORIZED`",
        ],
        "participant/05-one-screen-handoff.md": [
            "Candidate proposal scope under evaluation",
            "Presently authorized scope and current authority evidence",
            "FICTIONAL REPORTED EFFECTS EXIST; REAL-WORLD EXECUTION EVIDENCE DOES",
        ],
        "facilitator-only/01-facilitator-guide.md": [
            "ORCHESTRATION-INPUT-SHA256SUMS",
            "exact verification command/stdout/stderr/exit",
            "NOT RELEASED — PHASE 2 CHECK",
        ],
        "facilitator-only/04-freeze-and-correction-record-templates.md": [
            "Exact observed verification command",
            "Exact observed verification stdout, verbatim",
            "Record completion timestamp, RFC 3339 numeric offset",
            "Execution-log checkpoint entry SHA-256",
        ],
        "facilitator-only/05-execution-and-access-log.md": [
            "one JSON object conforming",
            "previous entry's sequence/hash",
            "undeclared prompt, message, file, tool result, or",
        ],
    }
    for relative, snippets in required_snippets.items():
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol: missing semantic source {relative}")
            continue
        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for snippet in snippets:
            if snippet not in content and " ".join(snippet.split()) not in normalized:
                errors.append(f"temporal protocol: {relative} omits required semantic guard {snippet!r}")

    decision_owner = packet / "participant" / "04-decision-owner-workbook.md"
    if decision_owner.is_file():
        marker_count = decision_owner.read_text(encoding="utf-8").count(
            CONTENT_GUARDS["phase_1_not_released_literal"]
        )
        if marker_count < 8:
            errors.append("temporal protocol: Stage B Phase 1 has unresolved withheld fields")
    scenario = packet / "participant" / "02-scenario-and-task.md"
    if scenario.is_file() and "No implementation, enforcement test" in scenario.read_text(encoding="utf-8"):
        errors.append("temporal protocol: stale no-execution wording contradicts reported effects")

    protected = protocol.get("protected_documents")
    expected_protected = {
        str(path.relative_to(packet))
        for path in packet.rglob("*.md")
    }
    if not isinstance(protected, dict) or set(protected) != expected_protected:
        errors.append("temporal protocol: protected-document inventory is incomplete")
    else:
        for relative, expected_hash in protected.items():
            path = packet / relative
            if not re.fullmatch(r"[0-9a-f]{64}", str(expected_hash)):
                errors.append(f"temporal protocol: invalid protected hash for {relative}")
            elif sha256(path) != expected_hash:
                errors.append(f"temporal protocol: protected document drift: {relative}")

    for path in sorted(packet.rglob("*.md")):
        header = "\n".join(path.read_text(encoding="utf-8").splitlines()[:6])
        if ("**Packet:**" in header or "**Version:**" in header) and PACKET_VERSION not in header:
            errors.append(f"{path.relative_to(ROOT)}: packet header is not version {PACKET_VERSION}")


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print("missing companion.json", file=sys.stderr)
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid companion.json: {exc}", file=sys.stderr)
        return 1

    if manifest.get("schema_version") != 1:
        errors.append("companion.json: schema_version must be 1")
    if not COMMIT_PATTERN.fullmatch(str(manifest.get("source_commit", ""))):
        errors.append("companion.json: source_commit must be a 7-40 character Git hash")

    required = manifest.get("required_files")
    if not isinstance(required, list) or not required:
        errors.append("companion.json: required_files must be a non-empty list")
        required = []
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    checksum_manifests = manifest.get("checksum_manifests", [])
    if not isinstance(checksum_manifests, list):
        errors.append("companion.json: checksum_manifests must be a list")
        checksum_manifests = []
    checked_checksums = 0
    for relative in checksum_manifests:
        checksum_path = ROOT / relative
        if not checksum_path.is_file():
            errors.append(f"missing checksum manifest: {relative}")
            continue
        listed_targets: set[Path] = set()
        for number, line in enumerate(
            checksum_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = CHECKSUM_PATTERN.fullmatch(line)
            if not match:
                errors.append(f"{relative}:{number}: invalid SHA256SUMS line")
                continue
            expected, raw_target = match.groups()
            target = (checksum_path.parent / raw_target).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}:{number}: checksum target escapes repository")
                continue
            if not target.is_file():
                errors.append(f"{relative}:{number}: missing checksum target: {raw_target}")
                continue
            listed_targets.add(target)
            checked_checksums += 1
            if sha256(target) != expected:
                errors.append(f"{relative}:{number}: checksum mismatch: {raw_target}")
        packet_files = {
            path.resolve()
            for path in checksum_path.parent.rglob("*")
            if path.is_file()
            and path != checksum_path
            and "__pycache__" not in path.parts
        }
        for unlisted in sorted(packet_files - listed_targets):
            errors.append(
                f"{relative}: packet file missing from checksum manifest: "
                f"{unlisted.relative_to(checksum_path.parent)}"
            )

    validate_temporal_freeze_protocol(errors)

    gateways = manifest.get("gateway_assets")
    if not isinstance(gateways, list) or not gateways:
        errors.append("companion.json: gateway_assets must be a non-empty list")
        gateways = []
    for gateway in gateways:
        relative = gateway.get("path", "")
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing gateway asset: {relative}")
            continue
        content = path.read_text(encoding="utf-8").casefold()
        phrases = [gateway.get("first_pass", ""), *gateway.get("required_language", [])]
        for phrase in phrases:
            if not phrase or phrase.casefold() not in content:
                errors.append(f"{relative}: missing required gateway language: {phrase!r}")
        for example in gateway.get("examples", []):
            if not (ROOT / example).is_file():
                errors.append(f"{relative}: missing comprehensive example: {example}")

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    checked_links = 0
    for source in markdown_files:
        for line, raw in markdown_links(source):
            try:
                target = local_target(source, raw)
            except ValueError as exc:
                errors.append(f"{source.relative_to(ROOT)}:{line}: {exc}: {raw}")
                continue
            if target is None:
                continue
            checked_links += 1
            if not target.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}:{line}: missing local link target: {raw}"
                )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"companion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(
        f"companion validation passed: {len(markdown_files)} Markdown files, "
        f"{checked_links} local links, {len(gateways)} gateway asset(s), "
        f"{checked_checksums} checksum(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
