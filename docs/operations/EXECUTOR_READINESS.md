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

### Non-local GPT and Codex Cloud activation gates (2026-10-30)

**Separate three distinct capabilities.** ChatGPT is the operator command surface, not proof of a deployed dispatcher. OpenAI Responses API / Agents API is a metered model/backend runtime requiring a currently authorized, funded and budget-constrained OpenAI API project. Codex Cloud is a separate OpenAI-managed coding environment; an existing API connector does not publish or activate a Codex Cloud environment. A registry of logical agents does not mean the same number of running cloud workers.

1. **Repository first:** Make this dedicated repository PRIVATE through an authenticated repository administrator and verify returned GitHub metadata, then enable branch protections and reviews. Until then, do not move product source, customer data, worker tokens or deployment configuration into this repository. Do not point any live service at this public bootstrap checkout.
2. **Codex Cloud:** In ChatGPT/Codex, create a cloud environment using the reviewed private repository, verify installation/tests and security scope, then explicitly publish the environment. Run one operator-requested, read-only coding task; capture its task ID and tested pull request before claiming the Codex coding path active. Local Codex/CLI is not a substitute.
3. **GPT runtime:** Validate actual OpenAI API project status and credits, a Vault-backed credential and restricted model/cost budget, and authorized owner MFA (aal2) before attempting any billable invocation. Credential presence or a stale connector status is not provider access proof. Only an authenticated synthetic one-shot with provider request ID, nonzero token usage, independent review and reconciliation can demonstrate readiness.
4. **Cloud executor:** Provision a dedicated, isolated cloud service only after release/deployment approval, and connect it to approved private application source. Prove live heartbeat, narrow worker identity/capabilities, idempotent single-run claim, visibility timeout, receipt, independent QA and bounded failure behavior. Never equate a Supabase Edge Function marked ACTIVE, a missing last_seen_at, or a scheduler tick with real model execution.
5. **Legacy tasks are quarantined:** Registration, verification, connectivity tests or deploying a worker must NOT automatically replay previously queued jobs. Require a fresh explicit operator-scoped run ID, risk classification, authorization and review. Do not send external mail, publish ads, mutate production commerce data or deploy production as part of a smoke test.
6. **Evidence and release:** Verify provider status and reviewer independence end-to-end, confirm exact run linkage and fresh timestamps, enforce spending caps and rollback, then obtain separate approvals for production deploy and each high-risk external action. Record VERIFIED only with observed end-to-end evidence; otherwise report PARTIAL / BLOCKED / NOT_VERIFIED.

Public reference documentation: [Codex Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments), [OpenAI Agents runtime selection](https://developers.openai.com/api/docs/guides/agents).
