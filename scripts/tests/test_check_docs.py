from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

import check_docs  # noqa: E402


class DocumentationChecksTest(unittest.TestCase):
    def parse(self, root: Path, name: str, content: str) -> check_docs.Document:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        document, issue = check_docs.parse_document(path, root)
        self.assertIsNone(issue)
        assert document is not None
        return document

    def test_valid_document_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            document = self.parse(
                root,
                "guide.md",
                "# Guide\n\n[Target](target.md)\n\n```python\nprint('ok')\n```\n",
            )
            self.assertEqual([], check_docs.check_document(document, 10_000, 100, 10))

    def test_independent_failures_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self.parse(
                root,
                "Bad-Name.md",
                "## No H1\n\n[Missing](missing.md)\n\nhttps://one.example\n```\n",
            )
            issues = check_docs.check_document(document, 10, 2, 0)
            self.assertEqual(
                {
                    "bare-url",
                    "code-fence",
                    "filename",
                    "heading",
                    "large-document",
                    "relative-link",
                },
                {issue.check for issue in issues},
            )

    def test_math_is_not_treated_as_a_link(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self.parse(
                root,
                "math_note.md",
                "# Math\n\n$pre[j]\\oplus pre[i-1](j\\ge i)$\n",
            )
            issues = check_docs.check_document(document, 10_000, 100, 10)
            self.assertNotIn("relative-link", {issue.check for issue in issues})

    def test_tilde_fence_must_close_with_same_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self.parse(root, "note.md", "# Note\n\n~~~text\ncontent\n```\n")
            self.assertIsNotNone(document.fence_issue)

    def test_empty_document_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self.parse(root, "empty.md", "")
            issues = check_docs.check_document(document, 10_000, 100, 10)
            self.assertIn("empty", {issue.check for issue in issues})

    def test_gitignore_rule_for_markdown_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            (root / ".gitignore").write_text("*.md\n!README.md\n", encoding="utf-8")
            readme = root / "README.md"
            readme.write_text("# Readme\n", encoding="utf-8")
            (root / "notes.md").write_text("# Ignored\n", encoding="utf-8")

            issues = check_docs.ignored_markdown_issues(root, [readme])
            self.assertTrue(any(issue.path == "notes.md" for issue in issues))


if __name__ == "__main__":
    unittest.main()
