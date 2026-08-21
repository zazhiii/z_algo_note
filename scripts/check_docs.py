#!/usr/bin/env python3
"""Run deterministic, read-only quality checks over repository Markdown files."""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


DEFAULT_MAX_BYTES = 100 * 1024
DEFAULT_MAX_LINES = 1_000
DEFAULT_MAX_BARE_URLS = 10

EXCLUDED_DIRS = {
    ".git",
    ".obsidian",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}

META_DOCUMENTS = {
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "REORGANIZATION.md",
    "SECURITY.md",
}

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
H1_RE = re.compile(r"^ {0,3}#(?!#)\s+\S")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^]]+\]:\s*(<[^>]+>|\S+)")
HTML_LINK_RE = re.compile(r"\b(?:href|src)\s*=\s*([\"'])(.*?)\1", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s<>]+", re.IGNORECASE)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
SNAKE_CASE_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*\.md$")
KEBAB_CASE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
INLINE_MATH_RE = re.compile(r"(?<!\\)(\${1,2})(.+?)(?<!\\)\1")


@dataclass(frozen=True)
class Issue:
    check: str
    path: str
    message: str
    line: int | None = None


@dataclass(frozen=True)
class Link:
    target: str
    line: int


@dataclass
class Document:
    path: Path
    relative_path: str
    text: str
    byte_count: int
    visible_lines: list[tuple[int, str]]
    fence_issue: Issue | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check Markdown structure, links, size, URLs, names, and ignore rules."
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=f"maximum UTF-8 file size (default: {DEFAULT_MAX_BYTES})",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=DEFAULT_MAX_LINES,
        help=f"maximum line count (default: {DEFAULT_MAX_LINES})",
    )
    parser.add_argument(
        "--max-bare-urls",
        type=int,
        default=DEFAULT_MAX_BARE_URLS,
        help=f"maximum bare HTTP(S) URLs per file (default: {DEFAULT_MAX_BARE_URLS})",
    )
    return parser.parse_args()


def repository_root() -> Path:
    return Path(__file__).resolve().parent.parent


def git_markdown_files(root: Path) -> list[Path] | None:
    """Return tracked and non-ignored untracked Markdown paths, or None without Git."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError:
        return None
    if result.returncode != 0:
        return None

    paths: list[Path] = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        relative = raw_path.decode("utf-8", errors="surrogateescape")
        path = root / relative
        if path.suffix.lower() in {".md", ".markdown"} and path.is_file():
            paths.append(path)
    return sorted(set(paths), key=lambda item: item.as_posix().casefold())


def walk_markdown_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for current, directories, filenames in os.walk(root):
        directories[:] = sorted(
            directory for directory in directories if directory not in EXCLUDED_DIRS
        )
        for filename in filenames:
            path = Path(current, filename)
            if path.suffix.lower() in {".md", ".markdown"}:
                paths.append(path)
    return sorted(paths, key=lambda item: item.as_posix().casefold())


def relative_display(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def parse_document(path: Path, root: Path) -> tuple[Document | None, Issue | None]:
    relative = relative_display(path, root)
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        return None, Issue("encoding", relative, f"not valid UTF-8: {error}")
    except OSError as error:
        return None, Issue("read", relative, f"cannot read file: {error}")

    visible_lines: list[tuple[int, str]] = []
    open_fence: tuple[str, int, int] | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(line)
        if open_fence is None:
            if match:
                marker = match.group(1)
                open_fence = (marker[0], len(marker), line_number)
            else:
                visible_lines.append((line_number, line))
            continue

        marker_character, marker_length, _ = open_fence
        if match:
            marker = match.group(1)
            remainder = match.group(2)
            if (
                marker[0] == marker_character
                and len(marker) >= marker_length
                and not remainder.strip()
            ):
                open_fence = None

    fence_issue = None
    if open_fence is not None:
        marker_character, marker_length, opening_line = open_fence
        fence_issue = Issue(
            "code-fence",
            relative,
            f"unclosed {marker_character * marker_length} code fence",
            opening_line,
        )

    return (
        Document(path, relative, text, len(raw), visible_lines, fence_issue),
        None,
    )


def mask_inline_code(line: str) -> str:
    line = INLINE_CODE_RE.sub(lambda match: " " * len(match.group(0)), line)
    return INLINE_MATH_RE.sub(lambda match: " " * len(match.group(0)), line)


def inline_link_targets(line: str) -> list[str]:
    """Extract destinations from inline Markdown links without a Markdown dependency."""
    targets: list[str] = []
    index = 0
    while True:
        close_label = line.find("](", index)
        if close_label < 0:
            break
        if close_label > 0 and line[close_label - 1] == "\\":
            index = close_label + 2
            continue

        cursor = close_label + 2
        while cursor < len(line) and line[cursor].isspace():
            cursor += 1
        content_start = cursor
        depth = 1
        escaped = False
        while cursor < len(line):
            character = line[cursor]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    break
            cursor += 1
        if depth != 0:
            index = close_label + 2
            continue

        content = line[content_start:cursor].strip()
        if content.startswith("<") and ">" in content:
            target = content[1 : content.find(">")]
        else:
            target = content.split(maxsplit=1)[0] if content else ""
        if target:
            targets.append(target)
        index = cursor + 1
    return targets


def document_links(document: Document) -> list[Link]:
    links: list[Link] = []
    for line_number, original_line in document.visible_lines:
        line = mask_inline_code(original_line)
        links.extend(Link(target, line_number) for target in inline_link_targets(line))

        reference = REFERENCE_LINK_RE.match(line)
        if reference:
            target = reference.group(1)
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            links.append(Link(target, line_number))

        for html_link in HTML_LINK_RE.finditer(line):
            links.append(Link(html_link.group(2), line_number))
    return links


def relative_target(target: str) -> str | None:
    target = target.strip().replace("\\(", "(").replace("\\)", ")")
    if not target or target.startswith(("#", "/", "\\", "//")):
        return None
    if SCHEME_RE.match(target):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    return target or None


def check_target_case(base: Path, target: str) -> tuple[bool, str | None]:
    """Check existence and exact path casing, including on case-insensitive systems."""
    normalized = posixpath.normpath(target.replace("\\", "/"))
    current = base.resolve()
    for component in normalized.split("/"):
        if component in {"", "."}:
            continue
        if component == "..":
            current = current.parent
            continue
        try:
            names = {child.name for child in current.iterdir()}
        except OSError:
            return False, None
        if component not in names:
            case_match = next(
                (name for name in names if name.casefold() == component.casefold()), None
            )
            if case_match is not None:
                return False, case_match
            return False, None
        current = current / component
    return current.exists(), None


def count_bare_urls(document: Document) -> tuple[int, list[int]]:
    count = 0
    lines: list[int] = []
    for line_number, original_line in document.visible_lines:
        line = mask_inline_code(original_line)
        reference = REFERENCE_LINK_RE.match(line)
        reference_span = reference.span(1) if reference else None
        html_spans = [match.span(2) for match in HTML_LINK_RE.finditer(line)]
        line_count = 0
        for match in URL_RE.finditer(line):
            start = match.start()
            if start > 0 and line[start - 1] in "(<\"'":
                continue
            if reference_span and reference_span[0] <= start < reference_span[1]:
                continue
            if any(span[0] <= start < span[1] for span in html_spans):
                continue
            line_count += 1
        if line_count:
            count += line_count
            lines.append(line_number)
    return count, lines


def valid_document_name(document: Document) -> bool:
    name = document.path.name
    if name == "README.md" or name in META_DOCUMENTS:
        return True
    if not document.relative_path.startswith("contest/"):
        return bool(SNAKE_CASE_RE.fullmatch(name))
    return bool(SNAKE_CASE_RE.fullmatch(name) or KEBAB_CASE_RE.fullmatch(name))


def ignored_markdown_issues(root: Path, source_files: list[Path]) -> list[Issue]:
    """Find actual Markdown and representative Markdown names ignored by Git rules."""
    actual_files = walk_markdown_files(root)
    source_directories = {path.parent for path in source_files}
    probe_paths = {
        directory / "doc_quality_probe.md" for directory in source_directories
    }
    candidates = sorted(
        set(actual_files) | probe_paths, key=lambda path: path.as_posix().casefold()
    )
    if not candidates:
        return []

    candidate_input = b"\0".join(
        relative_display(path, root).encode("utf-8", errors="surrogateescape")
        for path in candidates
    ) + b"\0"
    try:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-v", "-z", "--stdin"],
            cwd=root,
            input=candidate_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError:
        return [Issue("gitignore", ".gitignore", "Git is required for this check")]
    if result.returncode not in {0, 1}:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        detail = detail or f"git check-ignore exited {result.returncode}"
        return [Issue("gitignore", ".gitignore", detail)]

    actual_relative = {relative_display(path, root) for path in actual_files}
    issues: list[Issue] = []
    fields = result.stdout.rstrip(b"\0").split(b"\0") if result.stdout else []
    for index in range(0, len(fields) - 3, 4):
        source, line_number, pattern, path_field = (
            field.decode("utf-8", errors="surrogateescape")
            for field in fields[index : index + 4]
        )
        rule = f"{source}:{line_number}:{pattern}"
        ignored_path = path_field
        ignored_path = ignored_path.replace("\\", "/")
        if ignored_path in actual_relative:
            message = f"Markdown file is ignored by {rule}"
            issue_path = ignored_path
        else:
            message = f"Markdown files in this directory would be ignored by {rule}"
            issue_path = str(Path(ignored_path).parent).replace("\\", "/") or "."
        issues.append(Issue("gitignore", issue_path, message))
    return issues


def check_document(
    document: Document,
    max_bytes: int,
    max_lines: int,
    max_bare_urls: int,
) -> list[Issue]:
    issues: list[Issue] = []
    if not document.text.strip():
        issues.append(Issue("empty", document.relative_path, "document is empty"))

    if not any(H1_RE.match(line) for _, line in document.visible_lines):
        issues.append(Issue("heading", document.relative_path, "missing level-one heading"))

    if document.fence_issue:
        issues.append(document.fence_issue)

    line_count = len(document.text.splitlines())
    limits: list[str] = []
    if document.byte_count > max_bytes:
        limits.append(f"{document.byte_count} bytes > {max_bytes}")
    if line_count > max_lines:
        limits.append(f"{line_count} lines > {max_lines}")
    if limits:
        issues.append(
            Issue("large-document", document.relative_path, "; ".join(limits))
        )

    bare_url_count, bare_url_lines = count_bare_urls(document)
    if bare_url_count > max_bare_urls:
        sample = ", ".join(str(line) for line in bare_url_lines[:5])
        issues.append(
            Issue(
                "bare-url",
                document.relative_path,
                f"{bare_url_count} bare URLs > {max_bare_urls}; first seen on lines {sample}",
            )
        )

    if not valid_document_name(document):
        issues.append(
            Issue(
                "filename",
                document.relative_path,
                "use lowercase snake_case (contest records may use lowercase kebab-case)",
            )
        )

    seen_links: set[tuple[str, int]] = set()
    for link in document_links(document):
        target = relative_target(link.target)
        if target is None or (target, link.line) in seen_links:
            continue
        seen_links.add((target, link.line))
        exists, case_match = check_target_case(document.path.parent, target)
        if not exists:
            if case_match:
                message = f"path casing does not match: {target!r} (found {case_match!r})"
            else:
                message = f"relative link target does not exist: {target!r}"
            issues.append(Issue("relative-link", document.relative_path, message, link.line))
    return issues


def main() -> int:
    args = parse_args()
    if args.max_bytes < 1 or args.max_lines < 1 or args.max_bare_urls < 0:
        print("error: limits must be positive (bare URL limit may be zero)", file=sys.stderr)
        return 2

    root = repository_root()
    source_files = git_markdown_files(root)
    if source_files is None:
        source_files = walk_markdown_files(root)

    issues: list[Issue] = []
    documents: list[Document] = []
    for path in source_files:
        document, read_issue = parse_document(path, root)
        if read_issue:
            issues.append(read_issue)
        elif document:
            documents.append(document)
            issues.extend(
                check_document(
                    document,
                    args.max_bytes,
                    args.max_lines,
                    args.max_bare_urls,
                )
            )
    issues.extend(ignored_markdown_issues(root, source_files))

    issues.sort(key=lambda issue: (issue.path.casefold(), issue.line or 0, issue.check))
    if issues:
        print(f"Documentation quality check failed: {len(issues)} issue(s) in {len(documents)} file(s).")
        for issue in issues:
            location = f"{issue.path}:{issue.line}" if issue.line else issue.path
            print(f"[{issue.check}] {location}: {issue.message}")
        return 1

    print(f"Documentation quality check passed: {len(documents)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
