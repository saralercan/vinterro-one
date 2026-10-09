"""Fail closed on product code imports while this repository is public."""
from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import sys

ALLOWED_PUBLIC_FILES = frozenset({
    ".gitignore",
    "README.md",
    "AGENTS.md",
    "PROJECT.md",
    ".github/workflows/bootstrap-integrity.yml",
    ".github/workflows/repository-safety.yml",
    ".github/workflows/upstream-runtime-regression.yml",
    ".github/workflows/executor-readiness-contract.yml",
    "scripts/executor_readiness.py",
    "tests/test_executor_readiness.py",
    "docs/operations/EXECUTOR_READINESS.md",
    "docs/architecture/REPOSITORY_BOUNDARIES.md",
    "docs/migration/SAFE_EXTRACTION_PLAN.md",
    "docs/operations/RELEASE_GATE.md",
    "scripts/check_repository_safety.py",
    "tests/test_repository_safety.py",
})

SENSITIVE_NAMES = frozenset({
    "id_rsa", "id_ed25519", ".env", ".npmrc", ".pypirc",
    "credentials.json", "service-account.json", "service_account.json",
})
SENSITIVE_SUFFIXES = (".pem", ".p12", ".pfx", ".key", ".sqlite", ".sqlite3")
SECRET_PATTERNS = (
    re.compile("ghp_" + r"[A-Za-z0-9]{30,}"),
    re.compile("github_pat_" + r"[A-Za-z0-9_]{40,}"),
    re.compile("sk_live_" + r"[A-Za-z0-9]{20,}"),
    re.compile("AKIA" + r"[A-Z0-9]{16}"),
)

def inspect_file(path: str, repository_private: bool, root: Path) -> list[str]:
    issues: list[str] = []
    normalized = path.replace(chr(92), "/")
    name = Path(normalized).name.lower()
    if not repository_private and normalized not in ALLOWED_PUBLIC_FILES:
        issues.append(f"public repository must not contain: {normalized}")
    if name in SENSITIVE_NAMES or name.startswith(".env.") or name.endswith(SENSITIVE_SUFFIXES):
        issues.append(f"credential or database-like file name blocked: {normalized}")

    candidate = root / normalized
    if not candidate.is_file() or candidate.is_symlink() or candidate.stat().st_size > 2_000_000:
        return issues
    data = candidate.read_bytes()
    if b"\0" in data[:4096]:
        return issues
    decoded = data.decode("utf-8", errors="ignore")
    if any(pattern.search(decoded) for pattern in SECRET_PATTERNS):
        issues.append(f"potential hardcoded token detected: {normalized}")
    return issues


def main() -> int:
    value = os.environ.get("REPOSITORY_PRIVATE", "").strip().lower()
    if value not in {"true", "false"}:
        print("REPOSITORY_PRIVATE must be explicitly true or false", file=sys.stderr)
        return 2
    paths = subprocess.check_output(["git", "ls-files", "-z"]).decode("utf-8").split("\0")
    issues = []
    for path in filter(None, paths):
        issues.extend(inspect_file(path, value == "true", Path.cwd()))
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print(f"Repository safety policy passed ({'private' if value == 'true' else 'public'}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
