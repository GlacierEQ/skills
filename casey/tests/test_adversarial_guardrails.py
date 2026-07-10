from __future__ import annotations

import json
import sys
from pathlib import Path

CASEY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CASEY_ROOT / "scripts"))

from policy_guardrails import evaluate_case  # noqa: E402


def test_adversarial_cases_match_expected_decisions() -> None:
    fixture_path = CASEY_ROOT / "tests" / "fixtures" / "adversarial-cases.json"
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))

    failures: list[str] = []
    for case in payload["cases"]:
        decision = evaluate_case(case)
        expected_codes = tuple(sorted(case["expected_reason_codes"]))
        if decision.outcome != case["expected_outcome"]:
            failures.append(
                f"{case['id']}: outcome {decision.outcome!r} != {case['expected_outcome']!r}"
            )
        if decision.reason_codes != expected_codes:
            failures.append(
                f"{case['id']}: reason codes {decision.reason_codes!r} != {expected_codes!r}"
            )

    assert not failures, "\n".join(failures)
