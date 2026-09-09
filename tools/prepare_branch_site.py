#!/usr/bin/env python3

from __future__ import annotations

import argparse
import io
import re
import shutil
import subprocess
import tarfile
from dataclasses import dataclass, field
from pathlib import Path
from shutil import copy2


SUMMARY_ITEM_RE = re.compile(r"^(?P<indent>\s*)\*\s+\[(?P<title>.+?)\]\((?P<path>.+?)\)\s*$")
MARKDOWN_HTML_LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)#]+)\.html(#[^)]+)?(\))")
HTML_HREF_RE = re.compile(r'(<a[^>]+href=")([^"#]+)\.html(#[^"]+)?(")')
SHARED_SHELL_DIRS = ("assets", "stylesheets", "javascripts")


@dataclass
class NavItem:
    title: str
    path: str
    children: list["NavItem"] = field(default_factory=list)


def unescape_summary_path(path: str) -> str:
    return (
        path.strip()
        .replace(r"\_", "_")
        .replace(r"\(", "(")
        .replace(r"\)", ")")
        .replace(r"\[", "[")
        .replace(r"\]", "]")
        .replace(r"\ ", " ")
    )


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def resolve_existing_path(docs_dir: Path, raw_path: str) -> str:
    candidate = docs_dir / raw_path
    if candidate.exists():
        return raw_path

    current = docs_dir
    resolved_parts: list[str] = []
    for part in Path(raw_path).parts:
        children = {child.name.lower(): child.name for child in current.iterdir()} if current.is_dir() else {}
        matched = children.get(part.lower())
        if matched is None:
            return raw_path
        resolved_parts.append(matched)
        current = current / matched

    return str(Path(*resolved_parts))


def parse_summary(summary_path: Path) -> list[NavItem]:
    items: list[NavItem] = []
    stack: list[tuple[int, list[NavItem]]] = [(-1, items)]

    for raw_line in summary_path.read_text(encoding="utf-8").splitlines():
        match = SUMMARY_ITEM_RE.match(raw_line)
        if not match:
            continue

        depth = len(match.group("indent")) // 2
        title = match.group("title").strip()
        path = unescape_summary_path(match.group("path"))
        item = NavItem(title=title, path=path)

        while stack and depth <= stack[-1][0]:
            stack.pop()

        parent_items = stack[-1][1]
        parent_items.append(item)
        stack.append((depth, item.children))

    return items


def normalize_nav_paths(items: list[NavItem], docs_dir: Path) -> None:
    for item in items:
        item.path = resolve_existing_path(docs_dir, item.path)
        normalize_nav_paths(item.children, docs_dir)


def render_nav(items: list[NavItem], indent: int = 2) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent

    for item in items:
        if item.children:
            lines.append(f"{prefix}- {yaml_quote(item.title)}:")
            lines.append(f"{prefix}    - {item.path}")
            lines.extend(render_nav(item.children, indent + 4))
        else:
            lines.append(f"{prefix}- {yaml_quote(item.title)}: {item.path}")

    return lines


def export_git_ref(repo_root: Path, ref: str, docs_dir: Path) -> None:
    archive = subprocess.run(
        ["git", "archive", "--format=tar", ref],
        cwd=repo_root,
        check=True,
        stdout=subprocess.PIPE,
    )
    docs_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tar:
        tar.extractall(docs_dir)


def mirror_legacy_assets(docs_dir: Path) -> None:
    asset_source = docs_dir / ".gitbook" / "assets"
    if not asset_source.exists():
        return

    asset_target = docs_dir / "gitbook-assets"
    shutil.copytree(asset_source, asset_target, dirs_exist_ok=True)

    for asset in asset_target.rglob("*"):
        if not asset.is_file():
            continue
        root_alias = docs_dir / asset.name
        if not root_alias.exists():
            copy2(asset, root_alias)


def rewrite_legacy_links(docs_dir: Path) -> None:
    for markdown_file in docs_dir.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        updated = text.replace(".gitbook/assets/", "gitbook-assets/")
        updated = MARKDOWN_HTML_LINK_RE.sub(r"\1\2.md\3\4", updated)
        updated = HTML_HREF_RE.sub(r"\1\2.md\3\4", updated)
        if updated != text:
            markdown_file.write_text(updated, encoding="utf-8")


def copy_shared_site_shell(repo_root: Path, docs_dir: Path) -> None:
    shared_root = repo_root / "website"
    if not shared_root.exists():
        return

    for dirname in SHARED_SHELL_DIRS:
        source_dir = shared_root / dirname
        if not source_dir.exists():
            continue
        shutil.copytree(source_dir, docs_dir / dirname, dirs_exist_ok=True)


def build_config_text(site_name: str, docs_dir: Path, site_dir: Path, nav: list[NavItem]) -> str:
    lines = [
        f"site_name: {yaml_quote(site_name)}",
        f"docs_dir: {yaml_quote(str(docs_dir))}",
        f"site_dir: {yaml_quote(str(site_dir))}",
        "theme:",
        "  name: material",
        "  logo: assets/edgetx-logo.svg",
        "  favicon: assets/edgetx-logo.svg",
        "  palette:",
        "    primary: custom",
        "    accent: custom",
        "  features:",
        "    - navigation.indexes",
        "    - navigation.path",
        "extra_css:",
        "  - stylesheets/extra.css",
        "extra_javascript:",
        "  - javascripts/review-workbench.js",
        "  - javascripts/legacy-version-banner.js",
        "extra:",
        "  version:",
        "    provider: mike",
        "    default: latest",
        "    alias: true",
        "  legacy_version:",
        "    enabled: false",
        "    label: Legacy version",
        "    message: This documentation version is preserved for reference and may not include later corrections or the newest docs structure.",
        "markdown_extensions:",
        "  - tables",
        "  - admonition",
        "  - fenced_code",
        "nav:",
    ]
    lines.extend(render_nav(nav))
    lines.append("")
    return "\n".join(lines)


def prepare_workspace(repo_root: Path, ref: str, output_dir: Path) -> tuple[Path, Path]:
    if output_dir.exists():
        shutil.rmtree(output_dir)

    docs_dir = output_dir / "docs"
    site_dir = output_dir / "site"
    export_git_ref(repo_root, ref, docs_dir)
    mirror_legacy_assets(docs_dir)
    rewrite_legacy_links(docs_dir)
    copy_shared_site_shell(repo_root, docs_dir)

    summary_path = docs_dir / "SUMMARY.md"
    if not summary_path.exists():
        raise FileNotFoundError(f"{ref} does not contain SUMMARY.md")

    nav = parse_summary(summary_path)
    if not nav:
        raise RuntimeError(f"Could not parse any nav items from {summary_path}")
    normalize_nav_paths(nav, docs_dir)

    site_name = nav[0].title
    config_path = output_dir / "mkdocs.branch.yml"
    config_path.write_text(
        build_config_text(site_name=site_name, docs_dir=docs_dir, site_dir=site_dir, nav=nav),
        encoding="utf-8",
    )
    return config_path, docs_dir


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export a git branch into a standalone MkDocs workspace using that branch's SUMMARY.md nav."
    )
    parser.add_argument("--ref", required=True, help="Git ref to export, for example origin/edgetx_2.10")
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for the generated workspace",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    output_dir = Path(args.output).resolve()
    config_path, docs_dir = prepare_workspace(repo_root=repo_root, ref=args.ref, output_dir=output_dir)

    print(f"Prepared branch workspace for {args.ref}")
    print(f"Docs dir: {docs_dir}")
    print(f"MkDocs config: {config_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
