#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


SUMMARY_RE = re.compile(r"^(?P<indent>\s*)\* \[(?P<title>.+)\]\((?P<path>[^)]+)\)\s*$")
HINT_OPEN_RE = re.compile(r'^\{%\s*hint style="(?P<style>[^"]+)"\s*%\}\s*$')
HINT_CLOSE_RE = re.compile(r"^\{%\s*endhint\s*%\}\s*$")
TAB_OPEN_RE = re.compile(r'^\{%\s*tab title="(?P<title>[^"]+)"\s*%\}\s*$')
TABS_OPEN_RE = re.compile(r"^\{%\s*tabs\s*%\}\s*$")
TAB_CLOSE_RE = re.compile(r"^\{%\s*endtab\s*%\}\s*$")
TABS_CLOSE_RE = re.compile(r"^\{%\s*endtabs\s*%\}\s*$")
LINK_RE = re.compile(r"(!?\[[^\]]*\])\(([^)]+)\)")

LEGACY_PATH_PREFIX_ALIASES: tuple[tuple[str, str], ...] = (
    (
        "part_iii_-_opentx_lua_api_reference/bitmap-functions-less-than-greater-than-luadoc-begin-bitmap/",
        "api-reference/bitmap/",
    ),
    (
        "part_iii_-_opentx_lua_api_reference/general-functions-less-than-greater-than-luadoc-begin-general/",
        "api-reference/general/",
    ),
    (
        "part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/",
        "api-reference/lcd/",
    ),
    (
        "part_iii_-_opentx_lua_api_reference/model-functions-less-than-greater-than-luadoc-begin-model/",
        "api-reference/model/",
    ),
    ("part_i_-_script_type_overview/", "overview/"),
    ("part_ii_-_opentx_lua_api_programming_guide/", "programming/"),
    ("part_iii_-_opentx_lua_api_reference/", "api-reference/"),
    ("part_iv_-_advanced_topics/", "advanced-topics/"),
    # The real branch content (2.4-2.9, verified against the actual repo
    # trees) always uses the undotted "opentx_20_scripts" spelling -- no
    # branch anywhere uses the dotted "2.0" form below. Kept the dotted
    # entries too rather than replacing them, in case some other branch we
    # haven't checked still uses it; either way both fall through cleanly
    # to raw slugging if genuinely unmatched.
    ("part_iv_-_converting_opentx_20_scripts/", "converting-opentx-20-scripts/"),
    ("part_iv_-_converting_opentx_2.0_scripts/", "converting-opentx-2-0-scripts/"),
    ("part_v_-_converting_opentx_21_scripts/", "converting-opentx-21-scripts/"),
    ("part_vi_-_advanced_topics/", "advanced-topics/"),
    ("part_vii_-_appendix/", "appendix/"),
    ("part_i_-_script_type_overview.md", "overview/index.md"),
    ("part_ii_-_opentx_lua_api_programming_guide.md", "programming/index.md"),
    ("part_iii_-_opentx_lua_api_reference.md", "api-reference/index.md"),
    ("part_iv_-_converting_opentx_20_scripts.md", "converting-opentx-20-scripts/index.md"),
    ("part_iv_-_converting_opentx_2.0_scripts.md", "converting-opentx-2-0-scripts/index.md"),
    ("part_v_-_converting_opentx_21_scripts.md", "converting-opentx-21-scripts/index.md"),
    ("part_vi_-_advanced_topics.md", "advanced-topics/index.md"),
    ("part_vii_-_appendix.md", "appendix/index.md"),
    ("lua-api-programming/", "programming/"),
    ("lua-api-reference/", "api-reference/"),
    ("overview/", "overview/"),
)


@dataclass
class SummaryNode:
    title: str
    path: str
    children: list["SummaryNode"] = field(default_factory=list)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def infer_version_name(ref: str) -> str:
    match = re.search(r"(\d+\.\d+)", ref)
    return match.group(1) if match else "legacy"


def run_archive(ref: str, dest_dir: Path) -> None:
    archive_bytes = subprocess.check_output(["git", "archive", ref], cwd=repo_root())
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(archive_bytes)
        temp_file.flush()
        with tarfile.open(temp_file.name) as tar:
            tar.extractall(dest_dir)


def parse_summary(text: str) -> list[SummaryNode]:
    roots: list[SummaryNode] = []
    stack: list[tuple[int, SummaryNode]] = []

    for raw_line in text.splitlines():
        match = SUMMARY_RE.match(raw_line)
        if not match:
            continue

        indent = len(match.group("indent"))
        node = SummaryNode(match.group("title"), decode_gitbook_path(match.group("path")))

        while stack and stack[-1][0] >= indent:
            stack.pop()

        if stack:
            stack[-1][1].children.append(node)
        else:
            roots.append(node)

        stack.append((indent, node))

    return roots


def decode_gitbook_path(path: str) -> str:
    # Older GitBook SUMMARY files escape markdown punctuation inside paths,
    # e.g. part\_i\_-\_script\_type\_overview/mix.md. MkDocs should receive
    # the literal filename, not the markdown-escaped form.
    return re.sub(r"\\([_()[\]\\-])", r"\1", path)


def apply_legacy_path_aliases(path: str) -> str:
    lowered = decode_gitbook_path(path).strip().lower()
    for legacy_prefix, clean_prefix in LEGACY_PATH_PREFIX_ALIASES:
        if lowered == legacy_prefix.rstrip("/"):
            return clean_prefix.rstrip("/")
        if lowered.startswith(legacy_prefix):
            return f"{clean_prefix}{lowered[len(legacy_prefix):]}"
    return lowered


def normalize_component(component: str) -> str:
    cleaned = decode_gitbook_path(component).strip()
    if cleaned in {"", ".", ".."}:
        return cleaned

    if cleaned.lower() == "readme.md":
        return "README.md"

    if cleaned.lower().endswith(".md"):
        stem = cleaned[:-3]
        suffix = ".md"
    else:
        stem = cleaned
        suffix = ""

    stem = stem.lower()
    stem = re.sub(r"[&+]", " and ", stem)
    stem = re.sub(r"[^a-z0-9]+", "-", stem)
    stem = re.sub(r"-{2,}", "-", stem).strip("-")
    stem = stem or "page"
    return f"{stem}{suffix}"


def normalize_relative_path(path: str) -> str:
    decoded = apply_legacy_path_aliases(path)
    path_obj = Path(decoded)
    normalized_parts = [normalize_component(part) for part in path_obj.parts]
    return Path(*normalized_parts).as_posix()


def build_path_map(source_root: Path) -> dict[Path, Path]:
    path_map: dict[Path, Path] = {}
    used_targets: set[Path] = set()

    for source_file in sorted(source_root.rglob("*.md")):
        relative_path = source_file.relative_to(source_root)
        if relative_path.name == "SUMMARY.md":
            continue
        normalized = Path(normalize_relative_path(relative_path.as_posix()))

        candidate = normalized
        counter = 2
        while candidate in used_targets:
            if candidate.suffix:
                candidate = candidate.with_name(f"{candidate.stem}-{counter}{candidate.suffix}")
            else:
                candidate = candidate.with_name(f"{candidate.name}-{counter}")
            counter += 1

        path_map[relative_path] = candidate
        used_targets.add(candidate)

    return path_map


def build_source_lookup(source_root: Path) -> dict[str, Path]:
    # Two passes: first register every file under its own *exact*-case path
    # (unconditional assignment -- each real file has a distinct exact path,
    # so these never collide with each other). Only then build the
    # case-insensitive fallback, deciding collisions explicitly instead of
    # via a plain setdefault ordered by rglob's sort. The naive single-pass
    # setdefault version had a real bug: when a lowercase folder (the
    # "real" one, with its own README.md) coexists with an accidental
    # differently-cased duplicate (e.g. edgetx_2.4's
    # "Bitmap-functions.../getsize.md" next to
    # "bitmap-functions.../getsize.md"), the capitalized variant sorts
    # first and its *lowercased* key registration collides with -- and
    # silently wins over -- the real lowercase file's own *exact*-case key,
    # since for an already-lowercase path those two strings are identical.
    # SUMMARY.md links use the real folder's exact original casing, so this
    # was resolving to the wrong (duplicate, README-less) source file.
    exact: dict[str, Path] = {}
    case_insensitive_candidates: dict[str, list[Path]] = {}
    for source_file in sorted(source_root.rglob("*.md")):
        relative_path = source_file.relative_to(source_root)
        if relative_path.name == "SUMMARY.md":
            continue
        decoded = decode_gitbook_path(relative_path.as_posix())
        exact[decoded] = relative_path
        case_insensitive_candidates.setdefault(decoded.lower(), []).append(relative_path)

    lookup: dict[str, Path] = dict(exact)
    for lower_key, candidates in case_insensitive_candidates.items():
        if lower_key in lookup:
            continue
        if len(candidates) == 1:
            lookup[lower_key] = candidates[0]
            continue
        # Multiple differently-cased source files collapse to the same
        # lowercased key. Prefer whichever one's directory has its own
        # README.md -- the real, "complete" section -- over a bare
        # duplicate with no index page; otherwise fall back to the first
        # in sorted order (prior behavior).
        with_readme = [c for c in candidates if (source_root / c.parent / "README.md").exists()]
        chosen = with_readme[0] if with_readme else candidates[0]
        lookup[lower_key] = chosen
        others = [c for c in candidates if c != chosen]
        print(f"  (case-duplicate sources for {lower_key!r}: using {chosen}, ignoring {others})")
    return lookup


def resolve_source_relative(path: str, source_lookup: dict[str, Path]) -> Path:
    decoded = decode_gitbook_path(path)
    return source_lookup.get(decoded) or source_lookup.get(decoded.lower()) or Path(decoded)


def map_summary_paths(
    nodes: list[SummaryNode],
    path_map: dict[Path, Path],
    source_lookup: dict[str, Path],
) -> list[SummaryNode]:
    mapped: list[SummaryNode] = []
    for node in nodes:
        source_path = resolve_source_relative(node.path, source_lookup)
        mapped_node = SummaryNode(
            title=node.title,
            path=path_map.get(source_path, source_path).as_posix(),
            children=map_summary_paths(node.children, path_map, source_lookup),
        )
        mapped.append(mapped_node)
    return mapped


def normalize_nav_path(path: str) -> str:
    path_obj = Path(path)
    if path_obj.name == "README.md":
        if path_obj.parent == Path("."):
            return "index.md"
        return (path_obj.parent / "index.md").as_posix()
    return path


def nav_entry(node: SummaryNode) -> dict[str, object]:
    path = normalize_nav_path(node.path)
    if not node.children:
        return {node.title: path}

    children: list[object] = [{node.title: path}]
    children.extend(nav_entry(child) for child in node.children)
    return {node.title: children}


def build_nav(summary_nodes: list[SummaryNode]) -> list[object]:
    nav: list[object] = []
    for node in summary_nodes:
        title = "EdgeTX Lua Reference Guide" if node.path == "README.md" else node.title
        rewritten = SummaryNode(title=title, path=node.path, children=node.children)
        nav.append(nav_entry(rewritten))
    return nav


def convert_hint_style(style: str) -> str:
    return {
        "info": "info",
        "warning": "warning",
        "danger": "danger",
        "success": "success",
    }.get(style, "note")


def indent_block(lines: Iterable[str]) -> list[str]:
    return [f"    {line}" if line else "" for line in lines]


def rewrite_link_target_with_map(
    target: str,
    source_file: Path,
    source_root: Path,
    path_map: dict[Path, Path],
    source_lookup: dict[str, Path],
    legacy_assets_dir: str,
) -> str:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target

    if ".gitbook/assets/" in target:
        return target.replace(".gitbook/assets/", f"assets/{legacy_assets_dir}/")

    if target.startswith("/"):
        return target

    bare_target, hash_part = (target.split("#", 1) + [""])[:2]
    suffix = f"#{hash_part}" if hash_part else ""
    if not bare_target:
        return target

    bare_target = decode_gitbook_path(bare_target)

    if bare_target.endswith("/"):
        candidate = (source_file.parent / bare_target / "README.md").resolve()
        if candidate.exists():
            bare_target = f"{bare_target}README.md"

    relative_path = (source_file.parent / bare_target).resolve()
    if relative_path.is_dir() and (relative_path / "README.md").exists():
        stripped = bare_target.rstrip("/")
        bare_target = f"{stripped}/README.md"
        relative_path = (source_file.parent / bare_target).resolve()

    if not Path(bare_target).suffix and relative_path.with_suffix(".md").exists():
        bare_target = f"{bare_target}.md"
        relative_path = (source_file.parent / bare_target).resolve()

    try:
        relative_path.relative_to(source_root.resolve())
    except ValueError:
        return target

    try:
        source_relative = relative_path.relative_to(source_root.resolve())
    except ValueError:
        source_relative = resolve_source_relative(
            Path(bare_target).as_posix(),
            source_lookup,
        )
        if source_relative == Path(decode_gitbook_path(Path(bare_target).as_posix())):
            return target

    mapped_target = path_map.get(source_relative)
    if mapped_target is None:
        return target

    current_output = path_map[source_file.relative_to(source_root)]
    relative_to_output = Path(
        os.path.relpath(mapped_target, start=current_output.parent if current_output.parent != Path("") else Path("."))
    )
    return f"{relative_to_output.as_posix()}{suffix}"

def transform_markdown(
    content: str,
    source_file: Path,
    source_root: Path,
    path_map: dict[Path, Path],
    source_lookup: dict[str, Path],
    legacy_assets_dir: str,
) -> str:
    lines = content.splitlines()
    output: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        hint_open = HINT_OPEN_RE.match(line)
        if hint_open:
            style = convert_hint_style(hint_open.group("style"))
            block: list[str] = []
            i += 1
            while i < len(lines) and not HINT_CLOSE_RE.match(lines[i]):
                block.append(lines[i])
                i += 1
            output.append(f"!!! {style}")
            output.extend(indent_block(block))
            if block:
                output.append("")
            i += 1
            continue

        if TABS_OPEN_RE.match(line) or TABS_CLOSE_RE.match(line):
            i += 1
            continue

        tab_open = TAB_OPEN_RE.match(line)
        if tab_open:
            output.append(f"#### {tab_open.group('title')}")
            output.append("")
            i += 1
            continue

        if TAB_CLOSE_RE.match(line):
            output.append("")
            i += 1
            continue

        output.append(line)
        i += 1

    rewritten = "\n".join(output)

    def replace_link(match: re.Match[str]) -> str:
        label, target = match.groups()
        return f"{label}({rewrite_link_target_with_map(target, source_file, source_root, path_map, source_lookup, legacy_assets_dir)})"

    rewritten = LINK_RE.sub(replace_link, rewritten)
    return f"{rewritten.rstrip()}\n"


def copy_current_theme_assets(output_docs_dir: Path) -> None:
    current_docs_root = repo_root() / "website" / "md-docs"
    for folder_name in ("assets", "javascripts", "stylesheets"):
        src = current_docs_root / folder_name
        dst = output_docs_dir / folder_name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def copy_legacy_assets(source_root: Path, output_docs_dir: Path, legacy_assets_dir: str) -> None:
    legacy_assets = source_root / ".gitbook" / "assets"
    if not legacy_assets.exists():
        return
    dst = output_docs_dir / "assets" / legacy_assets_dir
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(legacy_assets, dst)


def build_output_tree(
    source_root: Path,
    output_docs_dir: Path,
    path_map: dict[Path, Path],
    source_lookup: dict[str, Path],
    legacy_assets_dir: str,
) -> None:
    if output_docs_dir.exists():
        shutil.rmtree(output_docs_dir)
    output_docs_dir.mkdir(parents=True, exist_ok=True)

    copy_current_theme_assets(output_docs_dir)
    copy_legacy_assets(source_root, output_docs_dir, legacy_assets_dir)

    # Every book has both a real section folder (.../part_i_-_..._overview/
    # README.md) and a same-titled top-level stub file
    # (part_i_-_..._overview.md) that LEGACY_PATH_PREFIX_ALIASES maps
    # straight to the same "overview/index.md" target the folder's
    # README.md also auto-mirrors to below. Verified empirically against
    # edgetx_2.4: the folder's README.md is consistently the more complete
    # of the two (has frontmatter, more current wording -- "EdgeTX" vs the
    # stub's "OpenTX" -- more lines), so it should win. build_path_map's own
    # collision handling doesn't cover this (it only dedupes when two
    # *different source files* map to the *same explicit target*, which
    # isn't this case: the stub's target IS index.md, the folder's target
    # is its own README.md; the mirror write below is untracked by it
    # entirely). Rather than special-case the mirror, track every path
    # actually written to output_docs_dir and make ANY write -- primary or
    # mirror -- back off once something else already claimed that exact
    # path, first-processed wins. rglob's sort naturally processes each
    # folder's README.md (and its mirror) before that section's top-level
    # stub (Path comparison is by parts-tuple, and "section" as a bare
    # first part sorts before "section.md" as a longer first part), so this
    # gives the README priority without needing to special-case which side
    # is the "real" one.
    written_targets: set[Path] = set()

    for source_file in sorted(source_root.rglob("*.md")):
        relative_path = source_file.relative_to(source_root)
        if relative_path.name == "SUMMARY.md":
            continue
        target = path_map[relative_path]
        destination = output_docs_dir / target
        transformed = transform_markdown(
            source_file.read_text(encoding="utf-8"),
            source_file,
            source_root,
            path_map,
            source_lookup,
            legacy_assets_dir,
        )

        if target in written_targets:
            print(f"  (skipping {relative_path}: {target} was already written by an earlier source file)")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(transformed, encoding="utf-8")
            written_targets.add(target)

        if destination.name == "README.md":
            index_target = (destination.parent / "index.md").relative_to(output_docs_dir)
            if index_target in written_targets:
                print(f"  (skipping index.md mirror for {relative_path}: {index_target} already written)")
            else:
                (destination.parent / "index.md").write_text(transformed, encoding="utf-8")
                written_targets.add(index_target)


def build_config(
    output_docs_dir: Path,
    nav: list[object],
    config_path: Path,
    site_dir: Path,
    version_name: str,
) -> None:
    # theme/plugins/markdown_extensions mirror the current root mkdocs.yml
    # feature-for-feature (dark mode palette, the dotted-symbol search
    # separator fix, minify, pymdownx set) so a legacy
    # version doesn't look or search noticeably worse than the current
    # site just because it was generated once and never regenerated.
    # There's no shared-config loader between the two -- this is a plain
    # copy -- so if mkdocs.yml's theme config changes again, update this
    # to match.
    config = {
        "site_name": "EdgeTX Lua Reference Guide",
        "site_description": f"Legacy EdgeTX {version_name} Lua documentation imported from the GitBook branch",
        "site_url": "https://luadoc.edgetx.org/",
        "repo_url": "https://github.com/EdgeTX/lua-reference-guide",
        "repo_name": "EdgeTX/lua-reference-guide",
        # No edit_uri: docs_dir is a temp workspace, not real repo content
        # (this converted GitBook page isn't something you can "edit" back
        # into the branch the same way), so leave it empty to suppress
        # Material's edit-this-page pencil rather than let it infer a
        # broken link from repo_url. repo_url/repo_name alone are enough to
        # show the GitHub header widget, which is all that's wanted here.
        "edit_uri": "",
        "docs_dir": str(output_docs_dir),
        "site_dir": str(site_dir),
        "theme": {
            "name": "material",
            "logo": "assets/edgetx-logo.svg",
            "favicon": "assets/edgetx-logo.svg",
            "font": False,
            "palette": [
                {
                    "media": "(prefers-color-scheme: light)",
                    "scheme": "default",
                    "primary": "custom",
                    "accent": "custom",
                    "toggle": {"icon": "material/brightness-7", "name": "Switch to dark mode"},
                },
                {
                    "media": "(prefers-color-scheme: dark)",
                    "scheme": "slate",
                    "primary": "custom",
                    "accent": "custom",
                    "toggle": {"icon": "material/brightness-4", "name": "Switch to light mode"},
                },
            ],
            "features": [
                "navigation.indexes",
                "navigation.path",
                "navigation.top",
                "toc.follow",
                "search.suggest",
                "search.highlight",
                "content.code.copy",
            ],
        },
        "plugins": [
            {
                "search": {
                    "separator": "[\\s\\-\\.]+",
                },
            },
            {"minify": {"minify_html": True}},
        ],
        "extra_css": ["stylesheets/extra-live-v2.css"],
        "extra_javascript": [
            "javascripts/mobile-nav-inline.js",
            "javascripts/legacy-version-banner.js",
        ],
        "extra": {
            "version": {"provider": "mike", "default": "latest", "alias": True},
            "legacy_version": {
                "enabled": True,
                "label": "Legacy version",
                "message": f"This documentation version preserves the original {version_name} GitBook content and structure for reference.",
            },
        },
        "markdown_extensions": [
            "tables",
            "admonition",
            "pymdownx.details",
            "pymdownx.superfences",
            {"pymdownx.highlight": {"anchor_linenums": True}},
            "pymdownx.inlinehilite",
            "pymdownx.snippets",
            {"pymdownx.tabbed": {"alternate_style": True}},
            "pymdownx.tilde",
            "attr_list",
            "md_in_html",
            {"toc": {"permalink": True}},
        ],
        "nav": nav,
    }
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Import a GitBook-era branch into a MkDocs-ready legacy docs tree.")
    parser.add_argument("--ref", default="upstream/edgetx_2.11")
    parser.add_argument("--output-docs-dir")
    parser.add_argument("--output-config")
    parser.add_argument("--site-dir")
    args = parser.parse_args()

    root = repo_root()
    version_name = infer_version_name(args.ref)
    output_docs_dir = (root / (args.output_docs_dir or f".site-legacy-generated/{version_name}/docs")).resolve()
    output_config = (root / (args.output_config or f".site-legacy-generated/{version_name}/mkdocs.yml")).resolve()
    site_dir = (root / (args.site_dir or f"site-legacy/{version_name}")).resolve()
    legacy_assets_dir = f"legacy-{version_name}"
    temp_root = root / ".tmp"
    temp_root.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(dir=temp_root, prefix="legacy-gitbook-") as temp_dir:
        source_root = Path(temp_dir)
        run_archive(args.ref, source_root)
        summary_text = (source_root / "SUMMARY.md").read_text(encoding="utf-8")
        path_map = build_path_map(source_root)
        source_lookup = build_source_lookup(source_root)
        summary_nodes = map_summary_paths(parse_summary(summary_text), path_map, source_lookup)
        build_output_tree(source_root, output_docs_dir, path_map, source_lookup, legacy_assets_dir)
        build_config(output_docs_dir, build_nav(summary_nodes), output_config, site_dir, version_name)

    print(f"Generated legacy docs in {output_docs_dir}")
    print(f"Generated MkDocs config at {output_config}")


if __name__ == "__main__":
    main()
