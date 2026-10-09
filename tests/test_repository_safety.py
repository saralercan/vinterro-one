"""Tests for public repository import gate (no third-party dependencies)."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_repository_safety.py"
spec = importlib.util.spec_from_file_location("repository_safety", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(module)


class RepositorySafetyTests(unittest.TestCase):
    def test_allow_bootstrap_in_public(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "README.md").write_text("safe bootstrap", encoding="utf-8")
            self.assertEqual([], module.inspect_file("README.md", False, p))

    def test_block_product_files_while_public(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "src").mkdir()
            (p / "src" / "main.ts").write_text("export {}", encoding="utf-8")
            messages = module.inspect_file("src/main.ts", False, p)
            self.assertTrue(any("public repository" in x for x in messages))

    def test_allow_product_files_once_private(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "src").mkdir()
            (p / "src" / "main.ts").write_text("export {}", encoding="utf-8")
            self.assertEqual([], module.inspect_file("src/main.ts", True, p))

    def test_block_env_name_even_when_private(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / ".env.production").write_text("SAFE=0", encoding="utf-8")
            self.assertTrue(module.inspect_file(".env.production", True, p))

    def test_block_credentials_filename(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "credentials.json").write_text("{}", encoding="utf-8")
            self.assertTrue(module.inspect_file("credentials.json", True, p))

    def test_detect_token_and_only_report_filename(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            fake = "ghp_" + "A" * 36
            (p / "README.md").write_text(fake, encoding="utf-8")
            issues = module.inspect_file("README.md", False, p)
            self.assertEqual(1, len(issues))
            self.assertNotIn(fake, issues[0])


if __name__ == "__main__":
    unittest.main()
