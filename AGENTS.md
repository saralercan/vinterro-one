# Vinterro One — Repository Agent Contract

This repository is for the Vinterro One product runtime, NOT a replacement for the cross-project control-plane repository `saralercan/ercan`.

## Resolution and precedence
1. Verified current production registry and live application deployment for runtime truth.
2. This project's explicit instructions and owned source for implementation details.
3. Reviewed and version-pinned central control-plane `saralercan/ercan` standards for common security, agent dispatch, QA and release rules.
4. No unsupported claims: distinguish `VERIFIED`, `PARTIAL`, `BLOCKED`, `NOT_VERIFIED`.

## Global Vinterro One trigger semantics
When the user says "tüm ajanları çalıştır", "Vinterro One çalıştır" or equivalent, include canonical Reklam Ajansı and all nine advertising subskills in the coverage plan. Task-relevant skills receive work; unrelated skills complete explicit scope checks. Do not claim independent parallel model execution unless actual execution receipts prove it.

## Canonical advertising specialization
One Reklam Ajansı. Nine skills: Google Ads, Meta Ads, paid social video (Pinterest/TikTok), creative studio, analytics/attribution, growth/budget, compliance/privacy, global market research, retail/marketplace advertising.

## Engineering and release safety
- Producer -> independent reviewer -> correction/retest -> applicable release gate.
- Deployment, advertising publishing/budget, external messages and destructive operations have separate approval gates.
- Never store API keys, access tokens, production data exports or recipient lists in Git.
- No production deployment is connected to this repo during bootstrap.
- Do not delete source from `saralercan/ercan` until verified rollback and cutover.
- This repo is currently public as of 2026-10-09: do not add product source or confidential architecture until visibility has been changed to PRIVATE and checked via GitHub metadata.
