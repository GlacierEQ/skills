#!/usr/bin/env python3
"""Deterministic guardrail evaluator used by sanitized adversarial fixtures.

This module does not execute tools. It evaluates whether a proposed operation is
eligible to proceed, requires review, or must be blocked under the public Casey
Skills Control Plane contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Decision:
    outcome: str
    reason_codes: tuple[str, ...]


UNVERIFIED_EVIDENCE = {
    "party_allegation",
    "inference",
    "verification_target",
    "generated_summary",
    "strategic_recommendation",
}

HIGH_RISK_ACTIONS = {"create", "update", "delete", "execute", "admin"}


def evaluate_case(case: dict[str, Any]) -> Decision:
    """Evaluate one normalized operation request.

    Outcomes:
      - ``allow``: all declared controls are satisfied;
      - ``review``: operation may proceed only after explicit human approval;
      - ``block``: a hard safety, provenance, privacy, or isolation rule failed.
    """

    reasons: list[str] = []
    action = case.get("action", "read")
    purpose = case.get("purpose", "analysis")
    evidence_status = set(case.get("evidence_status", []))

    if case.get("public_destination") and case.get("contains_private_data"):
        reasons.append("PRIVATE_DATA_PUBLIC_DESTINATION")

    if not case.get("domain_match", True):
        reasons.append("DOMAIN_ISOLATION_FAILURE")

    if case.get("fallback_used") and not case.get("fallback_approved"):
        reasons.append("UNAPPROVED_FALLBACK")

    if case.get("provenance_required") and not case.get("provenance_complete"):
        reasons.append("INCOMPLETE_PROVENANCE")

    if purpose == "court_facing" and evidence_status.intersection(UNVERIFIED_EVIDENCE):
        reasons.append("UNVERIFIED_COURT_FACING_PROPOSITION")

    if case.get("destructive") and not case.get("explicit_authorization"):
        reasons.append("DESTRUCTIVE_WRITE_WITHOUT_AUTHORIZATION")

    if action in HIGH_RISK_ACTIONS and not case.get("write_policy_match", False):
        reasons.append("WRITE_OUTSIDE_POLICY")

    if action in HIGH_RISK_ACTIONS and not case.get("audit_enabled", False):
        reasons.append("MISSING_WRITE_AUDIT")

    if case.get("connector_trust") == "untrusted" and action in HIGH_RISK_ACTIONS:
        reasons.append("UNTRUSTED_CONNECTOR_WRITE")

    if reasons:
        return Decision("block", tuple(sorted(set(reasons))))

    if action in HIGH_RISK_ACTIONS and case.get("approval_required"):
        if not case.get("explicit_authorization"):
            return Decision("review", ("HUMAN_APPROVAL_REQUIRED",))

    return Decision("allow", ())
