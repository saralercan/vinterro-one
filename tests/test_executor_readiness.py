"""Fail-closed executor/worker evidence tests; no external network or tokens."""
import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "executor_readiness.py"
spec = importlib.util.spec_from_file_location("executor_readiness", MODULE)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

BASE = dict(
    queued_runs=0,
    running_runs=0,
    successful_runs=0,
    provider_receipts=0,
    independent_passes=0,
    active_registered_workers=1,
    recent_worker_heartbeats=1,
    tasks_routed_last_tick=0,
)


class ExecutorEvidenceTests(unittest.TestCase):
    def assess(self, **updates):
        return engine.assess({**BASE, **updates})

    def test_idle_worker_does_not_prove_execution(self):
        self.assertEqual(self.assess()["state"], "NOT_VERIFIED")

    def test_queue_without_executor_is_blocked(self):
        self.assertEqual(self.assess(queued_runs=8, active_registered_workers=0,
                                     recent_worker_heartbeats=0)["state"], "BLOCKED")

    def test_heartbeat_without_model_routing_is_blocked(self):
        result = self.assess(queued_runs=3)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertFalse(result["live_execution_verified"])

    def test_recorded_success_without_receipt_blocked(self):
        self.assertEqual(self.assess(successful_runs=1)["state"], "BLOCKED")

    def test_recorded_success_without_review_blocked(self):
        self.assertEqual(self.assess(successful_runs=1, provider_receipts=1)["state"], "BLOCKED")

    def test_counts_look_good_still_not_verified(self):
        result = self.assess(successful_runs=2, provider_receipts=2,
                             independent_passes=2, tasks_routed_last_tick=2)
        self.assertEqual(result["state"], "EVIDENCE_REVIEW_REQUIRED")
        self.assertFalse(result["live_execution_verified"])

    def test_routed_task_and_no_completion_not_verified(self):
        self.assertEqual(self.assess(queued_runs=1,tasks_routed_last_tick=1)["state"],"NOT_VERIFIED")

    def test_heartbeats_cannot_exceed_active_workers(self):
        self.assertEqual(self.assess(active_registered_workers=1,
                                     recent_worker_heartbeats=2)["state"], "BLOCKED")

    def test_missing_or_boolean_metrics_rejected(self):
        for bad in ({}, {**BASE, "queued_runs": True}, {**BASE, "queued_runs": -1}):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    engine.assess(bad)

    def test_no_external_actions_can_be_authorized_by_aggregate_assessment(self):
        for candidate in (
            self.assess(),
            self.assess(queued_runs=1),
            self.assess(successful_runs=1,provider_receipts=1,independent_passes=1),
        ):
            self.assertFalse(candidate["ad_account_writes_allowed"])
            self.assertFalse(candidate["first_touch_email_allowed"])
            self.assertFalse(candidate["production_deployment_allowed"])


if __name__ == "__main__":
    unittest.main()
