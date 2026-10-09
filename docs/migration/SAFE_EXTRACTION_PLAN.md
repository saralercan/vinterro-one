# Vinterro One separate-repository migration

Status on 2026-10-09: **PHASE 0 — NON-SENSITIVE BOOTSTRAP ONLY**.

## Release gates

| Phase | Work | Exit criteria |
|---|---|---|
| 0 | Repository created, initial docs prepared | Target repo name verified, owner permission verified, secure visibility reviewed |
| 1 | Make target private | GitHub API reports `visibility=private`, protect `main` and require PR checks |
| 2 | Inventory actual source, dependencies, deployment links | Provenance for UI, API, workers, edge functions, data migrations; no missing dependencies |
| 3 | Controlled import into isolated feature branch | All required files present; no tokens/PII; shared agent policy pinned; no destructive changes |
| 4 | CI, security and independent QA | Build/test/typecheck/lint; routing and supervision regression; unit/integration checks; deployment smoke |
| 5 | Cutover one service at a time | Exact source commit and rollback SHA, health checks, signed release approval |
| 6 | Finalize ownership | New runtime repo authoritative, old source retained until monitored and rollback window completed |

## Hard constraints
- Existing `saralercan/ercan` stays intact throughout stages 0–5.
- A commit or PR does not constitute proof of real agent execution or Vercel/Railway/Supabase deployment.
- No auto-deploy integrations, production secrets, migrations, ads or email writes during import.
- Never replay production SQL migrations blindly; compare schema migration history.
- Do not modify the source of existing CI callers until central/shared workflow dependencies are fully audited.

## Known blockers
1. **PUBLIC target:** user must switch repository to Private under GitHub Settings; the current GitHub connector exposes no repository-visibility change action.
2. Exact production frontend Git source and project mapping have not yet been proven.
3. Existing CI, runtime agent dispatch and real worker deployment receipts must be checked independently after staged import.
