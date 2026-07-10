from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CASEY_ROOT = Path(__file__).resolve().parents[1]


def test_control_plane_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(CASEY_ROOT / "scripts" / "validate_control_plane.py")],
        cwd=CASEY_ROOT.parent,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
