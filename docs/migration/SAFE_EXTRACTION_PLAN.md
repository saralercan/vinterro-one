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


## Read-only source topology audit — 2026-10-09

Repository references: current shared control-plane \`saralercan/ercan\` at the audited 2026-10-09 \`master\` revision. Pin an **immutable commit SHA** at import time and verify Git blobs for every copied path; do not follow a moving branch in release automation.

| Surface | Read-only finding | Safe next operation |
| --- | --- | --- |
| GitHub target | \`saralercan/vinterro-one\` is **PUBLIC**, \`main\` is not protected | Set Private, then require reviewed PR and passing CI |
| GitHub shared source | 405 tracked files in the central agent/control-plane repository | Select by ownership; do not fork the full central repo |
| Reklam Ajansı | Nine specialist skill source definitions and central router exist in shared repo | Identify **shared vs product** ownership, retain canonical routing and QA contracts |
| Vinterro One backend | Edge-function code and SQL migration assets exist in shared repo | Inventory dependencies, avoid blind production migration replay |
| Live edge services | 20 deployed functions are visible in the connected Supabase project; many have no directly corresponding tracked function path in the central repo | Verify service ownership and source provenance individually (do not assume all 20 belong in this product repo) |
| Vercel | The accessible Vercel account does not establish a Vinterro One application-to-Git mapping | Resolve actual web application repository, team, project and commit before product-source import |
| Railway | The connected workspace does not show a verified Vinterro Sales Worker source/deployment association | Resolve exact Railway workspace and service through read-only evidence |
| Destination tests | Bootstrap and Repository Safety Gate checks passed on \`main\` | After private switch, add product build and source-specific regression CI |
| Production state | No new repository deployment or worker cutover has been performed | Preserve the current production sources and rollback plan |

### Package ownership rules
- Move **product-owned files** only after the target is private, with file SHA, source reference, destination, dependency list and test command recorded.
- Keep reusable cross-project agent standards, shared Vinterro Digital/Drag&Drop rules and common CI in \`saralercan/ercan\`; pin a reviewed reference from the new repository.
- Avoid duplicate ownership of canonical agent and skill definitions. If a skill is shared, consume a versioned reference instead of silently diverging.
- Treat live SQL history, automation registrations, provider credentials, customer records and third-party account IDs as **runtime state**, not Git source.
- Keep email templates and campaign send approvals unchanged unless their specific owners and audit evidence have been verified.

### Pre-import verification checklist
- [ ] GitHub reports new repository Private and \`main\` protected (review + required checks)
- [ ] Identify Vinterro One frontend Git remote and deployment project from service metadata
- [ ] Identify each product-owned edge function and exact current source commit
- [ ] Identify worker/supervision deployment sources and service owner workspace
- [ ] Compare planned migration files against applied migration history
- [ ] Classify each shared agent skill as central contract or product-local implementation
- [ ] Validate secrets exclusion, license and dependency boundaries before copying
- [ ] Define regression matrix (Orchestrator, nine ad skills, approvals, emails, QA, runtime evidence)
- [ ] Maintain reversible rollback for each service; no mixed automatic cutover

**Status:** source/dependency discovery is **PARTIAL**, import and actual live-cutover verification remain **BLOCKED** while target is public.
