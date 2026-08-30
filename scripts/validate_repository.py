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
    """Protect the v1.2.2 complete-hash-verify-record ordering."""
    packet = ROOT / "testing" / "agentic-reader-value-v1"
    required: dict[str, list[str]] = {
        "participant/00-packet-route.md": [
            "STAGE-A-HANDOFF-INPUT-SHA256SUMS",
            "STAGE-A-LIVE-UPDATE-INPUT-SHA256SUMS",
            "STAGE-B-PHASE-1-INPUT-SHA256SUMS",
            "STAGE-B-PHASE-2-INPUT-SHA256SUMS",
            "STAGE-B-PHASE-3-INPUT-SHA256SUMS",
            "never itself or the later detached record",
        ],
        "participant/03-practitioner-workbook.md": [
            "Do not put this workbook's own hash",
            "STAGE-A-REVISED-FREEZE-RECORD.md",
        ],
        "participant/04-decision-owner-workbook.md": [
            "STAGE-B-SECTION-1-FREEZE-VERIFICATION-RECORD.md",
            "STAGE-B-SECTION-2-FREEZE-VERIFICATION-RECORD.md",
            "STAGE-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD.md",
        ],
        "participant/05-one-screen-handoff.md": [
            "Do not put this handoff's own hash",
            "HANDOFF COMPLETE",
        ],
        "facilitator-only/04-freeze-and-correction-record-templates.md": [
            "Create it only after the governing manifest",
            "does not list or hash itself or this later record",
        ],
        "TEMPORAL-FREEZE-PROTOCOL-VALIDATION.md": [
            "complete governed bytes",
            "create a detached freeze-verification record",
        ],
    }
    for relative, phrases in required.items():
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol missing file: {path.relative_to(ROOT)}")
            continue
        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for phrase in phrases:
            if " ".join(phrase.split()) not in normalized:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing temporal protocol language: {phrase!r}"
                )

    forbidden = {
        "manifest hashes the record and every governed artifact",
        "manifest must hash every governed revised artifact and the freeze record",
        "hash the completed freeze record and create",
        "Section 1 freeze timestamp",
        "Section 2 freeze timestamp",
        "Handoff freeze timestamp",
    }
    for path in sorted(packet.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        header = "\n".join(content.splitlines()[:6])
        if ("**Packet:**" in header or "**Version:**" in header) and "1.2.2" not in header:
            errors.append(f"{path.relative_to(ROOT)}: packet header is not version 1.2.2")
        for phrase in forbidden:
            if phrase.casefold() in content.casefold():
                errors.append(
                    f"{path.relative_to(ROOT)}: forbidden temporal self-reference: {phrase!r}"
                )


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
