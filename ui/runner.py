import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORD_LINE = re.compile(r"^([a-z0-9]+): (\d+)$")


def _parse_block(output: str, header: str, unique_label: str) -> tuple[dict[str, int], int | None]:
    counts: dict[str, int] = {}
    unique = None
    capturing = False

    for line in output.splitlines():
        stripped = line.strip()
        if stripped == header:
            capturing = True
            continue
        if not capturing:
            continue
        if stripped.startswith(unique_label):
            unique = int(stripped.split(":")[-1].strip())
            break
        match = WORD_LINE.match(stripped)
        if match:
            counts[match.group(1)] = int(match.group(2))
        elif stripped:
            capturing = False

    return counts, unique


def run_test(url: str) -> dict:
    env = os.environ.copy()
    env["BASE_URL"] = url

    completed = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_unique_word_count.py", "--tb=short"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    ui_counts, ui_unique = _parse_block(output, "UI word occurrences:", "UI unique words:")
    api_counts, api_unique = _parse_block(output, "API word occurrences:", "API unique words:")

    return {
        "passed": completed.returncode == 0,
        "output": output,
        "ui_counts": ui_counts,
        "api_counts": api_counts,
        "ui_unique": ui_unique,
        "api_unique": api_unique,
    }
