"""Offline fail-closed diagnosis for Vinterro One executor evidence.

This module NEVER connects to production, invokes a model, updates a run or
verifies a production execution. It operates only on independently gathered
read-only aggregate metrics. A positive count is not a provider receipt.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = (
    "queued_runs",
    "running_runs",
    "successful_runs",
    "provider_receipts",
    "independent_passes",
    "active_registered_workers",
    "recent_worker_heartbeats",
    "tasks_routed_last_tick",
)


def assess(metrics: dict) -> dict:
    """Return BLOCKED, NOT_VERIFIED or EVIDENCE_REVIEW_REQUIRED; never VERIFIED."""
    if not isinstance(metrics, dict):
        raise ValueError("readiness metrics must be an object")
    normalized = {}
    for name in REQUIRED:
        value = metrics.get(name)
        if type(value) is not int or value < 0:
            raise ValueError(f"missing or invalid nonnegative integer metric: {name}")
        normalized[name] = value

    m = normalized
    findings: list[str] = []
    if m["active_registered_workers"] == 0:
        findings.append("no active registered model executor")
    if m["recent_worker_heartbeats"] == 0:
        findings.append("no recent heartbeat from registered model executor")
    if m["queued_runs"] > 0 and m["tasks_routed_last_tick"] == 0:
        findings.append("queued tasks are not advancing through model executor")
    if m["successful_runs"] > m["provider_receipts"]:
        findings.append("success claims exceed provider receipts")
    if m["successful_runs"] > m["independent_passes"]:
        findings.append("success claims exceed independently reviewed completions")
    if m["recent_worker_heartbeats"] > m["active_registered_workers"]:
        findings.append("heartbeat count exceeds registered active workers")
    if m["running_runs"] > 0 and m["active_registered_workers"] == 0:
        findings.append("running tasks without a registered executor")

    if findings:
        state = "BLOCKED"
    elif m["successful_runs"] == 0:
        state = "NOT_VERIFIED"
        findings.append("no independently evidenced successful model execution")
    else:
        state = "EVIDENCE_REVIEW_REQUIRED"
        findings.append("counts are insufficient; inspect receipts, identity, reviewer independence and freshness")

    return {
        "state": state,
        "findings": findings,
        "live_execution_verified": False,
        "ad_account_writes_allowed": False,
        "first_touch_email_allowed": False,
        "production_deployment_allowed": False,
        "source": "OFFLINE_AGGREGATES_NOT_RUNTIME_EVIDENCE",
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 scripts/executor_readiness.py <read-only-aggregate-json>", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        result = assess(data)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"invalid_readonly_evidence: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result["state"] == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
