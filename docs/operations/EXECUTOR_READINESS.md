# Executor readiness — evidence contract

This is a **read-only, offline safety assessment**. Never treat a CI pass, configured agent, periodic control-plane heartbeat, or passed evaluation as proof that an actual independent model executor has completed a task.

### Signals required for a real execution
1. A registered active model worker with a fresh heartbeat and a proven queue-consumer path.
2. A task-specific worker transition (queued → running), with an immutable provider receipt carrying nonzero token usage and provider request identity.
3. Independent reviewer and applicable supervisor/release gate with task-specific and fresh evidence.
4. Completion state reconciled to the exact task and provider receipt; zero unsupported claims.

A single count of successful evaluations, a control heartbeat, or a worker's configuration alone does **not** establish these conditions. `scripts/executor_readiness.py` evaluates non-sensitive read-only aggregate JSON and can only return `BLOCKED`, `NOT_VERIFIED` or `EVIDENCE_REVIEW_REQUIRED`. It never returns `VERIFIED`.

Only a full manual/provider audit may determine VERIFIED. Do not place project credentials, production run payloads, prompt content, worker tokens or user records in Git or CI.

### Diagnostic categories
- **BLOCKED:** no registered worker or heartbeat, queued tasks with no routing, or successful-run claims unsupported by receipt/independent QA.
- **NOT_VERIFIED:** no detected contradiction, but no end-to-end verified completion.
- **EVIDENCE_REVIEW_REQUIRED:** aggregate counts appear plausible but require authenticated per-run receipts, provider corroboration, reviewer identity and freshness checks.

### Cutover
Until the dedicated GitHub repository is **Private** and protected, no product source or deployment migration. CI is for static/contract regression only. Live agent execution, ads publication/budget updates, production deploys and outbound email require independent approvals and verified release gates.
