#!/usr/bin/env python3
"""Validate the Casey Skills Control Plane as a closed, fail-safe registry."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

CASEY_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = CASEY_ROOT / "registry" / "skills.yaml"
SKILLS_ROOT = CASEY_ROOT / "skills"
SCHEMAS_ROOT = CASEY_ROOT / "schemas"
SKILL_SCHEMA_PATH = SCHEMAS_ROOT / "skill-manifest.schema.json"

FIXTURE_BINDINGS = (
    (
        CASEY_ROOT / "tests" / "fixtures" / "adversarial-cases.json",
        SCHEMAS_ROOT / "adversarial-cases.schema.json",
    ),
    (
        CASEY_ROOT / "examples" / "private-overlay.sanitized.json",
        SCHEMAS_ROOT / "private-overlay.schema.json",
    ),
)

REQUIRED_CONTRACTS = (
    "case-context-package.schema.json",
    "evidence-reference.schema.json",
    "connector-capability.schema.json",
    "authorized-write-policy.schema.json",
    "private-overlay.schema.json",
)

FORBIDDEN_STRUCTURED_KEYS = re.compile(
    r"^(?:secret|token|password|api[_-]?key|private[_-]?key|client[_-]?secret)$",
    re.IGNORECASE,
)
SECRET_VALUE_PREFIXES = ("sk-", "ghp_", "github_pat_", "xoxb-", "xoxp-")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def format_schema_errors(validator: Draft202012Validator, value: Any) -> list[str]:
    messages: list[str] = []
    for error in sorted(validator.iter_errors(value), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{location}: {error.message}")
    return messages


def find_sensitive_values(value: Any, location: str = "<root>") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if FORBIDDEN_STRUCTURED_KEYS.match(str(key)):
                findings.append(f"forbidden structured key at {child_location}")
            findings.extend(find_sensitive_values(child, child_location))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(find_sensitive_values(child, f"{location}[{index}]"))
    elif isinstance(value, str) and value.startswith(SECRET_VALUE_PREFIXES):
        findings.append(f"secret-like value at {location}")
    return findings


def detect_dependency_cycles(graph: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in visiting:
            cycle_start = trail.index(node)
            errors.append("dependency cycle: " + " -> ".join(trail[cycle_start:] + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        trail.append(node)
        for dependency in graph.get(node, []):
            visit(dependency, trail)
        trail.pop()
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node, [])
    return errors


def main() -> int:
    errors: list[str] = []

    for required in REQUIRED_CONTRACTS:
        path = SCHEMAS_ROOT / required
        if not path.is_file():
            errors.append(f"missing private-overlay contract: {path.relative_to(CASEY_ROOT)}")

    try:
        registry = load_yaml(REGISTRY_PATH)
    except Exception as exc:  # pragma: no cover - fatal parse path
        print(f"ERROR: cannot load registry: {exc}", file=sys.stderr)
        return 1

    try:
        skill_schema = load_json(SKILL_SCHEMA_PATH)
        Draft202012Validator.check_schema(skill_schema)
    except Exception as exc:  # pragma: no cover - fatal schema path
        print(f"ERROR: invalid skill manifest schema: {exc}", file=sys.stderr)
        return 1

    manifest_validator = Draft202012Validator(skill_schema)
    entries = registry.get("skills", []) if isinstance(registry, dict) else []
    registry_ids: list[str] = [entry.get("id", "") for entry in entries]

    if len(registry_ids) != len(set(registry_ids)):
        errors.append("registry contains duplicate skill IDs")

    registry_by_id = {entry.get("id"): entry for entry in entries if entry.get("id")}
    dependency_graph: dict[str, list[str]] = {}
    registered_directories: set[str] = set()

    for entry in entries:
        skill_id = entry.get("id", "<missing-id>")
        raw_path = entry.get("path")
        if not raw_path:
            errors.append(f"{skill_id}: registry path is missing")
            continue

        skill_path = (REGISTRY_PATH.parent / raw_path).resolve()
        try:
            skill_path.relative_to(SKILLS_ROOT.resolve())
        except ValueError:
            errors.append(f"{skill_id}: registry path escapes skills root: {raw_path}")
            continue

        registered_directories.add(skill_path.name)
        if not skill_path.is_dir():
            errors.append(f"{skill_id}: skill directory does not exist: {raw_path}")
            continue

        for required_name in ("SKILL.md", "manifest.json"):
            required_path = skill_path / required_name
            if not required_path.is_file():
                errors.append(f"{skill_id}: missing {required_name}")

        manifest_path = skill_path / "manifest.json"
        if not manifest_path.is_file():
            continue

        try:
            manifest = load_json(manifest_path)
        except Exception as exc:
            errors.append(f"{skill_id}: invalid manifest JSON: {exc}")
            continue

        for message in format_schema_errors(manifest_validator, manifest):
            errors.append(f"{skill_id}: manifest schema violation: {message}")

        consistency_fields = {
            "id": entry.get("id"),
            "version": entry.get("version"),
            "domain": entry.get("domain"),
            "lifecycle": entry.get("lifecycle"),
        }
        for field, expected in consistency_fields.items():
            if manifest.get(field) != expected:
                errors.append(
                    f"{skill_id}: manifest {field}={manifest.get(field)!r} "
                    f"does not match registry {expected!r}"
                )

        if manifest.get("trust", {}).get("minimum") != entry.get("trust_required"):
            errors.append(f"{skill_id}: manifest trust minimum does not match registry")

        dependencies = manifest.get("dependencies", [])
        dependency_graph[skill_id] = dependencies
        for dependency in dependencies:
            if dependency not in registry_by_id:
                errors.append(f"{skill_id}: unknown dependency {dependency}")
            if dependency == skill_id:
                errors.append(f"{skill_id}: skill cannot depend on itself")

        for finding in find_sensitive_values(manifest):
            errors.append(f"{skill_id}: {finding}")

    actual_directories = {
        child.name for child in SKILLS_ROOT.iterdir() if child.is_dir() and not child.name.startswith(".")
    }
    unregistered = sorted(actual_directories - registered_directories)
    stale_entries = sorted(registered_directories - actual_directories)
    if unregistered:
        errors.append("unregistered skill directories: " + ", ".join(unregistered))
    if stale_entries:
        errors.append("registry entries without directories: " + ", ".join(stale_entries))

    errors.extend(detect_dependency_cycles(dependency_graph))

    for schema_path in sorted(SCHEMAS_ROOT.glob("*.schema.json")):
        try:
            Draft202012Validator.check_schema(load_json(schema_path))
        except Exception as exc:
            errors.append(f"invalid JSON schema {schema_path.name}: {exc}")

    for fixture_path, fixture_schema_path in FIXTURE_BINDINGS:
        if not fixture_path.is_file():
            errors.append(f"missing fixture: {fixture_path.relative_to(CASEY_ROOT)}")
            continue
        if not fixture_schema_path.is_file():
            errors.append(f"missing fixture schema: {fixture_schema_path.relative_to(CASEY_ROOT)}")
            continue
        try:
            fixture = load_json(fixture_path)
            fixture_schema = load_json(fixture_schema_path)
            fixture_validator = Draft202012Validator(fixture_schema)
            for message in format_schema_errors(fixture_validator, fixture):
                errors.append(f"{fixture_path.name}: {message}")
            for finding in find_sensitive_values(fixture):
                errors.append(f"{fixture_path.name}: {finding}")
        except Exception as exc:
            errors.append(f"cannot validate fixture {fixture_path.name}: {exc}")

    if errors:
        print("Casey Skills Control Plane validation failed:", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(entries)} skills, "
        f"{len(list(SCHEMAS_ROOT.glob('*.schema.json')))} schemas, "
        f"and {len(FIXTURE_BINDINGS)} fixture sets."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
