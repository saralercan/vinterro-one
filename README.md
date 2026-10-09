# Vinterro One

Vinterro One is the product-specific repository for the Vinterro Digital multi-agent control plane.

> **Bootstrap status (2026-10-09):** This repository is currently **PUBLIC**, though the planned production layout is **PRIVATE**. Only non-sensitive scaffolding belongs here until GitHub Settings → General → Danger Zone → Change repository visibility → **Private** has been completed and verified. **The application source and live service deployment have not been migrated.**

## Repository roles

- **This repository** (`saralercan/vinterro-one`): product runtime, UI, integrations, service workers, migrations, tests and product-specific agents after a reviewed migration.
- **Shared standards repository** (`saralercan/ercan`): cross-project governance, reusable agent standards, reusable CI, portable skills and canonical routing policies. Do not duplicate central policies without version pinning.

## Deployment and safety

1. No live Vercel, Railway or Supabase project points to this repository as part of this bootstrap.
2. Existing `saralercan/ercan` sources remain untouched until a tested migration and reversible cutover.
3. Never commit secrets, tokens, user records, confidential CRM/outreach data or production database exports.
4. Code changes require CI, independent QA, evidence and an explicit production release gate.
5. Marketing spend, live advertising changes and first-contact mail actions require their separate approvals.

See the staged migration PR for proposed layout, testing and source mapping.
