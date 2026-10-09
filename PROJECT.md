# Project: Vinterro One

**Role:** Dedicated product repository for UI, API, agent runtime, automation, services, database migrations and project-scoped quality assurance after a controlled extraction.

**Canonical upstream control plane:** `https://github.com/saralercan/ercan` (`master`), referencing audited immutable commits/tags, not floating branch references for reproducible CI.

**Source status:** Initial bootstrap only. No production app, worker, edge function, infrastructure secrets, account state or deployment is currently migrated into this repository.

**System boundaries:** Git holds code/configuration; Supabase holds regulated runtime/data state; Vercel/Railway provide deployment state; providers (Gmail/Ads/Shopify) retain their own authoritative transaction receipts.

**Safety:** Always verify target repo private visibility before transferring implementation or customer data.
