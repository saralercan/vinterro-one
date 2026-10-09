# Production release checklist

Before any new `vinterro-one` repository commit can be considered production-ready:

- [ ] GitHub target visibility is Private, `main` protected.
- [ ] Source of truth for each Vercel/Railway/Supabase component is explicitly inventoried.
- [ ] Secrets and client records remain outside source control.
- [ ] Product build, lint, types and tests pass on known commit.
- [ ] Global "tüm ajanları çalıştır" / "Vinterro One çalıştır" routes cover canonical Reklam Ajansı and all nine scopes.
- [ ] Independent reviewer QA and applicable policy/approval checks pass.
- [ ] Canary/smoke tests verify real endpoints and account permissions with evidence.
- [ ] Backups, rollback and one-component-at-a-time deploy order reviewed.
- [ ] No advertising campaign publication, spend, or outbound Gmail first-touch is performed without its separate explicit authorization.

Decision states: VERIFIED | PARTIAL | BLOCKED | NOT_VERIFIED.
