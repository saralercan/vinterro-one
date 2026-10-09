# Repository boundaries

## Shared (`saralercan/ercan`)
Reusable agent standards, cross-project skills, common platform/brand policy, reusable workflows, project registry conventions and shared release principles. Preserve existing projects and migration history.

## Vinterro One (`saralercan/vinterro-one`)
Product-facing code and its direct runtime dependencies after reviewed import:
- Orchestrator and live agent execution services
- Command Center / One Copilot / application UI once its actual Git source is identified
- API and Supabase edge functions used by this product
- Railway worker and supervision mechanisms
- Product-specific plugins, adapters, models, migrations, tests and CI
- Release manifests, operational runbooks, feature-specific evaluations

## Source locations identified in the shared repository
- `plugins/vinterro-one/`
- `services/vinterro-sales-worker/`
- `services/vinterro-supervision/`
- `supabase/functions/ercan-os-api/`
- `supabase/functions/vinterro-one-chatgpt-mcp/`
- `supabase/functions/vinterro-one-supervision/`
- `docs/standards/VINTERRO_*` (review each file's shared ownership before extracting)
- `.agents/skills/reklam-ajansi*/` (review global vs product ownership)
- `.codex/agents/vinterro-*`
- `scripts/` and `tests/` (dependency-scoped selection only)

**Important:** Complete Vinterro One web frontend source has not been verified in this shared Git tree. Inspect Vercel's actual Git project mapping before relocating anything.

## Non-goals
No fork of the entire central repository. No duplication of canonical cross-project standards without ownership decisions. No direct production repository switch during bootstrap.
