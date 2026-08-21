#!/usr/bin/env python3
"""Check external links separately from deterministic documentation checks."""

from __future__ import annotations

import argparse
import concurrent.futures
import sys
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from check_docs import (
    URL_RE,
    document_links,
    git_markdown_files,
    mask_inline_code,
    parse_document,
    repository_root,
    walk_markdown_files,
)


@dataclass(frozen=True)
class Result:
    url: str
    ok: bool
    detail: str


def trim_surrounding_punctuation(url: str) -> str:
    url = url.rstrip(".,;:!?")
    for opening, closing in (("(", ")"), ("[", "]"), ("{", "}")):
        while url.endswith(closing) and url.count(closing) > url.count(opening):
            url = url[:-1]
    return url


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check HTTP(S) links. This network-dependent check is never run by check_docs.py."
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="seconds per request")
    parser.add_argument("--workers", type=int, default=8, help="parallel request count")
    return parser.parse_args()


def check_url(url: str, timeout: float) -> Result:
    headers = {"User-Agent": "docs-quality-check/1.0"}
    for method in ("HEAD", "GET"):
        request = Request(url, headers=headers, method=method)
        try:
            with urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", 200)
                return Result(url, 200 <= status < 400, f"HTTP {status}")
        except HTTPError as error:
            if method == "HEAD" and error.code in {400, 403, 405, 501}:
                continue
            return Result(url, False, f"HTTP {error.code}")
        except (URLError, TimeoutError, OSError) as error:
            if method == "HEAD":
                continue
            reason = getattr(error, "reason", error)
            return Result(url, False, str(reason))
    return Result(url, False, "request failed")


def external_urls() -> tuple[set[str], list[str]]:
    root = repository_root()
    paths = git_markdown_files(root)
    if paths is None:
        paths = walk_markdown_files(root)

    urls: set[str] = set()
    read_errors: list[str] = []
    for path in paths:
        document, issue = parse_document(path, root)
        if issue:
            read_errors.append(f"{issue.path}: {issue.message}")
            continue
        assert document is not None
        for link in document_links(document):
            if link.target.lower().startswith(("http://", "https://")):
                urls.add(link.target)
        for _, line in document.visible_lines:
            urls.update(
                trim_surrounding_punctuation(url)
                for url in URL_RE.findall(mask_inline_code(line))
            )
    return urls, read_errors


def main() -> int:
    args = parse_args()
    if args.timeout <= 0 or args.workers < 1:
        print("error: --timeout and --workers must be positive", file=sys.stderr)
        return 2

    urls, read_errors = external_urls()
    if read_errors:
        for error in read_errors:
            print(f"[read] {error}")
        return 1
    if not urls:
        print("External link check passed: no HTTP(S) links found.")
        return 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(lambda url: check_url(url, args.timeout), sorted(urls)))

    failures = [result for result in results if not result.ok]
    for result in failures:
        print(f"[external-link] {result.url}: {result.detail}")
    if failures:
        print(f"External link check failed: {len(failures)} of {len(results)} URL(s).")
        return 1
    print(f"External link check passed: {len(results)} URL(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
