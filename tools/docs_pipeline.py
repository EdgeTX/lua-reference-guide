#!/usr/bin/env python3

import argparse
import datetime
import json
import html
import markdown
import os
from pathlib import Path
import re
import sys
from collections import Counter


TYPE_DEFINITIONS_PATH = Path("docs-system/type-definitions.json")
REVIEW_DECISIONS_PATH = Path("docs-system/generated/review-decisions.json")
API_GROUPS_PATH = Path("docs-system/api-groups.json")
LUALS_BUILTIN_TYPES = {
    "any",
    "boolean",
    "function",
    "integer",
    "nil",
    "number",
    "pointer",
    "string",
    "table",
    "unknown",
}


def load_model(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        model = json.load(handle)
    normalize_model(model)
    validate_model(model)
    return model


def load_type_definitions() -> dict:
    if not TYPE_DEFINITIONS_PATH.exists():
        return {}
    with TYPE_DEFINITIONS_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_review_decisions() -> dict:
    if not REVIEW_DECISIONS_PATH.exists():
        return {}
    with REVIEW_DECISIONS_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_api_groups() -> list[dict]:
    if not API_GROUPS_PATH.exists():
        return []
    with API_GROUPS_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload.get("groups", [])


def normalize_model(model: dict) -> None:
    for item in model.get("items", []):
        item.setdefault("doc_id", default_doc_id(item["module"], item["id"]))
        item.setdefault("aliases", [])
        item.setdefault("deprecated_aliases", [])
        item.setdefault("raw_luadoc", "")
        item.setdefault("source_line", None)


def validate_model(model: dict) -> None:
    required_root = ["docs_version", "upstream_ref", "generated_at", "items"]
    for key in required_root:
      if key not in model:
        raise ValueError(f"missing root key: {key}")

    seen_ids = set()
    for item in model["items"]:
        for key in [
            "id",
            "doc_id",
            "symbol",
            "module",
            "kind",
            "syntax",
            "summary",
            "parameters",
            "returns",
            "availability",
            "notes",
            "source_location",
            "raw_luadoc",
            "source_line",
        ]:
            if key not in item:
                raise ValueError(f"item missing key {key}: {item.get('id', '<unknown>')}")

        item_id = item["id"]
        if item_id in seen_ids:
            raise ValueError(f"duplicate item id: {item_id}")
        seen_ids.add(item_id)

        if "since" not in item["availability"]:
            raise ValueError(f"item missing availability.since: {item_id}")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def unique_strings(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def slugify_token(text: str) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text)
    return text.strip("-").lower()


def scoped_symbol_parts(module: str, symbol: str) -> list[str]:
    scoped_name = symbol
    if module != "runtime" and symbol.startswith(f"{module}."):
        scoped_name = symbol[len(module) + 1 :]
    elif module == "runtime" and "." in symbol:
        scoped_name = symbol.split(".", 1)[1]
    return [slugify_token(part) for part in scoped_name.split(".")]


def default_doc_id(module: str, symbol: str) -> str:
    parts = [slugify_token(module)] if module else []
    parts.extend(scoped_symbol_parts(module, symbol))
    return ".".join(part for part in parts if part)


def nested_item_slug(item: dict) -> str:
    """Item-page filename stem for the nested-by-topic-group scheme.

    Unlike doc_id, this drops the "runtime" module qualifier for bare/
    ungrouped functions -- "runtime" is an internal doc-grouping label,
    not a real Lua namespace, and the topic-group folder already
    disambiguates those. Real namespaces (model., lcd., lvgl., Bitmap.)
    are kept since the group folder doesn't imply a namespace.
    """
    module = item["module"]
    parts = scoped_symbol_parts(module, item["symbol"])
    if module != "runtime":
        parts = [slugify_token(module)] + parts
    return "-".join(part for part in parts if part)


def page_slug(text: str) -> str:
    return safe_file_stem(text).replace(".", "-")


def group_for_item(item: dict) -> dict:
    for group in load_api_groups():
        if item_matches_group(item, group):
            return group
    return {
        "name": "Uncategorized",
        "slug": "uncategorized",
        "description": "APIs not yet assigned to a user-facing group.",
    }


def page_name_for_item(item: dict) -> str:
    group = group_for_item(item)
    return str(Path(group["slug"]) / f"{nested_item_slug(item)}.md")


def review_page_name_for_item(item: dict) -> str:
    return f"review-{page_slug(item['doc_id'])}.md"


def rendered_dir(path: Path) -> Path:
    """The effective directory a page is served from under mkdocs' default
    use_directory_urls behavior: foo/bar.md serves at .../foo/bar/, so its
    own directory (for the purposes of resolving a relative link FROM it)
    is one level deeper than its file-system parent. foo/index.md serves at
    .../foo/, i.e. its own file-system parent -- no extra depth to add."""
    if path.name == "index.md":
        return path.parent
    return path.parent / path.stem


def page_href(from_page: str | Path, to_page: str | Path) -> str:
    from_dir = rendered_dir(docs_path(from_page))
    to_dir = rendered_dir(docs_path(to_page))
    href = os.path.relpath(to_dir, start=from_dir).replace(os.sep, "/")
    return f"{href}/" if href != "." else "./"


def doc_link(from_page: str | Path, to_page: str | Path) -> str:
    return os.path.relpath(docs_path(to_page), start=docs_path(from_page).parent).replace(os.sep, "/")


def docs_path(path: str | Path) -> Path:
    path = Path(path)
    if path.is_absolute():
        return path
    return Path(os.path.normpath(str(Path("/__docs__") / path)))


def group_page_name(group: dict) -> str:
    # A true folder index (group/index.md), not a flat sibling (group.md) --
    # rendered_dir() computes the same served URL either way, so every
    # link this pipeline generates (nav, cards, page_href) is unaffected,
    # but Material's navigation.indexes feature only recognizes and
    # deduplicates a section's self-referencing first nav entry (hiding it
    # from the visible list, promoting it into the clickable header
    # instead) when that entry is a genuine folder index living alongside
    # its siblings -- confirmed by comparing against the legacy
    # GitBook-imported versions (tools/import_legacy_gitbook.py), whose
    # group hub pages have always been real folder indexes and don't show
    # the "duplicate first entry" the flat scheme caused here.
    return f"{group['slug']}/index.md"


def module_page_name(module_name: str) -> str:
    return f"module-{safe_file_stem(module_name)}.md"


def item_matches_group(item: dict, group: dict) -> bool:
    if item["id"] in group.get("ids", []):
        return True
    if item["module"] in group.get("modules", []):
        return True
    for prefix in group.get("id_prefixes", []):
        if item["id"].startswith(prefix):
            return True
    return False


def items_by_group(model: dict) -> list[tuple[dict, list[dict]]]:
    groups = load_api_groups()
    ordered: list[tuple[dict, list[dict]]] = []
    matched_ids = set()
    for group in groups:
        matched = [item for item in model["items"] if item["id"] not in matched_ids and item_matches_group(item, group)]
        matched_ids.update(item["id"] for item in matched)
        ordered.append((group, matched))
    return ordered


NAV_GENERATED_BEGIN = "      # BEGIN GENERATED -- tools/docs_pipeline.py update-nav; do not hand-edit"
NAV_GENERATED_END = "      # END GENERATED"


def render_nav_yaml_block(model: dict) -> list[str]:
    """YAML lines for the API Reference nav sub-tree, adding every item
    page as a real nav entry under its group instead of only the 16 group
    hub pages. Without this, item pages aren't in the nav tree at all, so
    Material can't mark them active or show a navigation.path breadcrumb
    for them server-side -- that gap is what api-function-breadcrumb.js
    existed to paper over with JS. The legacy GitBook-imported versions
    don't have this problem since their nav is built straight from
    SUMMARY.md, which already lists every page.

    Indentation matches mkdocs.yml's existing "API Reference" block
    exactly: 6 spaces for a group's own entry (sibling of the other
    top-level API Reference children), 10 for its items, so
    update_mkdocs_nav's marker-splice drops in without reformatting
    anything around it. A group's self-referencing first child (its own
    hub page) mirrors the same pattern already used one level up for
    "API Reference" and "API Overview" -- not a new convention.

    Item label is item["symbol"] (e.g. "getFlightMode", "model.getMix"),
    the same convention render_group_page uses for its card titles,
    sorted the same way, so the sidebar and the hub page's card grid
    agree on naming and order.

    Groups are sorted alphabetically by name rather than kept in
    items_by_group's order (docs-system/api-groups.json's own file order,
    which isn't alphabetical) -- matches the previous hand-authored nav's
    order, the least surprising choice for a sidebar."""
    lines = []
    for group, items in sorted(items_by_group(model), key=lambda pair: pair[0]["name"]):
        if not items:
            continue
        group_href = f"api-reference/{group_page_name(group)}"
        lines.append(f"      - {group['name']}:")
        lines.append(f"          - {group['name']}: {group_href}")
        for item in sorted(items, key=lambda entry: entry["symbol"]):
            item_href = f"api-reference/{page_name_for_item(item)}"
            lines.append(f"          - {item['symbol']}: {item_href}")
    return lines


def update_mkdocs_nav(config_path: Path, nav_lines: list[str]) -> None:
    """Splice the generated API Reference item nav block into an mkdocs
    config file between two marker comments, leaving everything else in
    the file byte-for-byte untouched. A full yaml.safe_load + yaml.safe_dump
    round-trip would destroy this file's hand-written comments and exact
    formatting (PyYAML preserves neither), so this edits the raw text
    instead -- the same "generated content lives in a clearly marked
    region, hand-authored content stays outside it" convention already
    used for generated .md/.d.lua files in this pipeline."""
    text = config_path.read_text(encoding="utf-8")
    if NAV_GENERATED_BEGIN not in text or NAV_GENERATED_END not in text:
        raise ValueError(
            f"{config_path}: missing generated-nav markers "
            f"({NAV_GENERATED_BEGIN!r} / {NAV_GENERATED_END!r}). Add them "
            "once by hand around the API Reference group entries (empty "
            "between them is fine); this command fills them in from then on."
        )
    before, rest = text.split(NAV_GENERATED_BEGIN, 1)
    _, after = rest.split(NAV_GENERATED_END, 1)
    new_text = before + NAV_GENERATED_BEGIN + "\n" + "\n".join(nav_lines) + "\n" + NAV_GENERATED_END + after
    config_path.write_text(new_text, encoding="utf-8")


def source_label(item: dict) -> str:
    if item.get("source_line"):
        return f"{item['source_location']}:{item['source_line']}"
    return item["source_location"]


def review_action(item: dict) -> tuple[str, str]:
    unknown_params = [param["name"] for param in item["parameters"] if param["type"] == "unknown"]
    unknown_returns = [ret.get("name") or "-" for ret in item["returns"] if ret["type"] == "unknown"]
    if unknown_params or unknown_returns:
        parts = []
        if unknown_params:
            parts.append(f"unknown param types: {', '.join(unknown_params)}")
        if unknown_returns:
            parts.append(f"unknown return types: {', '.join(unknown_returns)}")
        return ("Fix C++ annotation first", "; ".join(parts))
    issues = is_suspicious_item(item)
    if issues:
        return ("Check parser behavior", ", ".join(issues))
    return ("No action needed", "Parsed output looks structurally healthy.")


def suggestion_type(type_name: str) -> str:
    return "TODO" if type_name == "unknown" else type_name


def suggested_function_signature(item: dict) -> str:
    if not item["parameters"]:
        return f"@function {item['symbol']}()"
    names = ", ".join(param["name"] for param in item["parameters"])
    return f"@function {item['symbol']}([{names}])"


def render_suggested_luadoc(item: dict) -> str:
    lines = [suggested_function_signature(item), ""]
    if item["summary"]:
        lines.append(item["summary"])
        lines.append("")
    for param in item["parameters"]:
        lines.append(
            f"@param {param['name']} ({suggestion_type(param['type'])}) {param['description']}".rstrip()
        )
        lines.append("")
    for retval in item["returns"]:
        name = retval.get("name") or ""
        prefix = f"@retval {name} " if name and name != "-" else "@retval "
        lines.append(f"{prefix}({suggestion_type(retval['type'])}) {retval['description']}".rstrip())
        lines.append("")
    if item["notes"]:
        for note in item["notes"]:
            lines.append(f"@notice {note}")
            lines.append("")
    if item["availability"].get("since"):
        lines.append(f"@status current Introduced in {item['availability']['since']}")
    return "\n".join(lines).strip()


def decision_select_options() -> list[str]:
    return [
        "TODO",
        "integer",
        "number",
        "string",
        "boolean",
        "table",
        "function",
        "pointer",
        "nil",
        "integer|string",
        "table|nil",
        "function|nil",
        "string|nil",
    ]


def render_decision_controls(item: dict) -> list[str]:
    editable_params = item["parameters"]
    editable_returns = item["returns"]
    if not editable_params and not editable_returns:
        return ["No fields to edit."]

    payload = {
        "item_id": item["id"],
        "symbol": item["symbol"],
        "summary": item["summary"],
        "parameters": item["parameters"],
        "returns": item["returns"],
        "notes": item["notes"],
        "since": item["availability"].get("since"),
    }
    options = "".join(
        f'<option value="{html.escape(option)}">{html.escape(option)}</option>'
        for option in decision_select_options()
    )
    lines = [
        f'<div class="decision-panel" data-item-id="{html.escape(item["id"])}">',
        '<div class="decision-status" data-role="status">Decision server not connected yet.</div>',
        '<table class="decision-table">',
        '<thead><tr><th>Field</th><th>Kind</th><th>Current Type</th><th>Description</th><th>Select Type</th></tr></thead>',
        '<tbody>',
    ]
    for param in editable_params:
        current_type = suggestion_type(param["type"])
        lines.append(
            "<tr>"
            f'<td><code>{html.escape(param["name"])}</code></td>'
            "<td>param</td>"
            f"<td><code>{html.escape(param['type'])}</code></td>"
            f"<td>{html.escape(param['description'])}</td>"
            "<td>"
            f'<select data-field-kind="param" data-field-name="{html.escape(param["name"])}" data-current-type="{html.escape(current_type)}">{options}</select>'
            f'<input type="text" placeholder="Custom type" data-field-kind="param" data-field-name="{html.escape(param["name"])}" data-custom-type="true" />'
            "</td>"
            "</tr>"
        )
    for retval in editable_returns:
        name = retval.get("name") or "-"
        current_type = suggestion_type(retval["type"])
        lines.append(
            "<tr>"
            f'<td><code>{html.escape(name)}</code></td>'
            "<td>return</td>"
            f"<td><code>{html.escape(retval['type'])}</code></td>"
            f"<td>{html.escape(retval['description'])}</td>"
            "<td>"
            f'<select data-field-kind="return" data-field-name="{html.escape(name)}" data-current-type="{html.escape(current_type)}">{options}</select>'
            f'<input type="text" placeholder="Custom type" data-field-kind="return" data-field-name="{html.escape(name)}" data-custom-type="true" />'
            "</td>"
            "</tr>"
        )
    lines.extend(
        [
            "</tbody>",
            "</table>",
            '<div class="decision-actions"><button type="button" data-role="save">Save Decisions</button></div>',
            f'<script type="application/json" class="decision-payload">{html.escape(json.dumps(payload))}</script>',
            "</div>",
        ]
    )
    return lines


def render_doc_text(text: str, page_path: str | Path) -> str:
    return rewrite_legacy_doc_links(text, page_path)


TABLE_FIELD_BULLET_RE = re.compile(r"^`([^`]+)`\s*\(([^)]+)\)\s*(.*)$")
TABLE_FIELD_BULLET_NO_TYPE_RE = re.compile(r"^`([^`]+)`\s+(.*)$")


def split_intro_and_bullets(text: str) -> tuple[list[str], list[str]]:
    """Split a possibly-multi-line description into leading non-bullet
    lines and `* item` bullet lines (a continuation line with no bullet
    marker is folded into the previous bullet). Shared by both the plain
    Markdown-table cell renderer and the raw-HTML table renderer below."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    intro: list[str] = []
    items: list[str] = []
    for line in lines:
        bullet_match = re.match(r"^[*-]\s+(.*)$", line)
        if bullet_match:
            items.append(bullet_match.group(1))
        elif items:
            items[-1] = f"{items[-1]} {line}"
        else:
            intro.append(line)
    return intro, items


def render_table_cell_text(intro: list[str], items: list[str]) -> str:
    """Render a description's already-split intro/bullet lines (see
    split_intro_and_bullets) for a plain Markdown table cell. Table cells
    can't contain literal newlines, and GFM only parses inline markup
    inside them (not block-level lists), so collapsing newlines to spaces
    would crush any `* item` bullet list (e.g. a `@commonparams`-expanded
    settings list) into an unreadable run-on paragraph. Bullet lines are
    rendered as a real `<ul><li>` list -- GFM tables allow raw inline HTML
    in cells, and this convention is already used elsewhere in this site's
    hand-authored pages. Any non-bullet lines are joined with `<br>`. Only
    used for rows that don't need a nested field table -- see
    render_field_html_table for those."""
    parts = []
    if intro:
        parts.append("<br>".join(intro))
    if items:
        parts.append("<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>")
    return "".join(parts)


def html_code(text: str) -> str:
    """Wrap plain text (a param/return name or type) in a literal <code>
    tag, for a cell in a hand-built raw <table> -- see render_field_html_table.
    Used instead of re-wrapping in backticks and relying on Markdown to
    convert them, since that conversion doesn't happen inside a raw HTML
    block (see render_inline_markdown)."""
    return f"<code>{html.escape(text)}</code>"


def render_inline_markdown(text: str) -> str:
    """Render a single line of description text (may contain a backtick
    code span or a Markdown link from rewrite_legacy_doc_links) to HTML, for
    embedding in a hand-built raw <table> -- see render_field_html_table.
    A full <table>...</table> is classified as an HTML block by
    Python-Markdown, and content inside an HTML block does NOT get inline
    Markdown processing by default (confirmed empirically -- even
    md_in_html's markdown="1" attribute doesn't reach into hand-authored
    <td> content), unlike a plain Markdown-table cell, which processes
    inline Markdown for free. So cell content headed into a raw table has
    to be pre-rendered here instead."""
    text = text.strip()
    if not text:
        return ""
    rendered = markdown.markdown(text)
    if rendered.startswith("<p>") and rendered.endswith("</p>") and rendered.count("<p>") == 1:
        rendered = rendered[len("<p>") : -len("</p>")]
    return rendered


def render_nested_field_table(items: list[str], type_hint: str) -> str | None:
    """A `table`-typed parameter's own sub-fields are documented in the
    firmware source as `* `name` (type) description` bullets (see e.g.
    lvgl.arc's `params`) -- occasionally missing the `(type)` part (e.g.
    model.getMix's `delayPrec`/`speedPrec`, a genuine gap in the upstream
    annotation). Rendered as a flat `<ul>`, a field list of any real size
    (some run past 15 fields) turns into a wall of text with no visible
    Type column for the sub-fields themselves, and crammed into the
    Description cell it's still squeezed into whatever width that one
    column got. When every bullet in a cell matches one of those two
    shapes, this renders a real Field/Type/Description `<table>` instead
    (blank Type cell for a bullet missing one), for the caller to place in
    a full-width row of its own (see render_field_html_table) rather than
    inside the narrow cell.

    Only attempted when type_hint is exactly "table": an integer/string
    parameter's bullets are enum/flag VALUE options (e.g. play-tone's
    `flags`), not fields of a table, and share the exact same
    `` `TOKEN` description `` surface shape as a name-only field bullet --
    the parameter's own type is what actually distinguishes them, not
    anything about the bullet text itself. Returns None (caller falls back
    to the plain `<ul>`) if the type isn't "table", or if not one single
    item matches either field shape.

    A bullet that matches neither shape (e.g. lvgl.build's trailing "any
    other key accepted by the constructor function for the chosen `type`",
    which names no field at all) is kept as a plain note appended after the
    field table rather than forcing the whole list back to a flat `<ul>` --
    once type_hint has already established this is a table's own field
    list and not an enum/flag value list, a bullet that doesn't fit the
    `name (type) description` shape is safely read as a caveat about the
    table as a whole, not a value option to preserve alongside real
    fields."""
    if type_hint != "table":
        return None
    rows = []
    notes = []
    for item in items:
        match = TABLE_FIELD_BULLET_RE.match(item)
        if match:
            name, field_type, description = match.groups()
        else:
            match = TABLE_FIELD_BULLET_NO_TYPE_RE.match(item)
            if not match:
                notes.append(item)
                continue
            name, description = match.groups()
            field_type = ""
        rows.append(
            "<tr><td>"
            + html_code(name)
            + "</td><td>"
            + (html_code(field_type) if field_type else "-")
            + "</td><td>"
            + render_inline_markdown(description)
            + "</td></tr>"
        )
    if not rows:
        return None
    header = "<thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead>"
    table_html = f'<table class="lua-nested-field-table">{header}<tbody>{"".join(rows)}</tbody></table>'
    if notes:
        notes_html = "<ul class=\"lua-nested-field-notes\">" + "".join(
            f"<li>{render_inline_markdown(note)}</li>" for note in notes
        ) + "</ul>"
        return table_html + notes_html
    return table_html


def render_table_cell_html(intro: list[str], items: list[str], type_hint: str) -> tuple[str, str | None]:
    """Render a cell's intro/bullet content for the raw-HTML table path
    (see render_field_html_table). Mirrors render_table_cell_text's
    intro/bullet handling, but pre-renders inline Markdown itself via
    render_inline_markdown instead of relying on GFM's per-cell inline
    processing, which a hand-built raw HTML table doesn't get for free.
    Returns (cell_html, nested_table_html_or_None)."""
    nested_table = render_nested_field_table(items, type_hint) if items else None
    if nested_table:
        intro_html = render_inline_markdown("<br>".join(intro)) if intro else ""
        return intro_html, nested_table
    parts = []
    if intro:
        parts.append("<br>".join(render_inline_markdown(line) for line in intro))
    if items:
        parts.append("<ul>" + "".join(f"<li>{render_inline_markdown(item)}</li>" for item in items) + "</ul>")
    return "".join(parts), None


def render_field_html_table(headers: list[str], row_specs: list[tuple[list[str], str | None]]) -> str:
    """Hand-built raw HTML <table> for a Parameters/Returns section where at
    least one row needs a genuine full-width row underneath it (a
    table-typed parameter's own field list, from render_nested_field_table).
    Plain Markdown pipe tables have no colspan support, and a pipe-syntax
    table can't have extra raw-HTML rows spliced into its <tbody> either (the
    `tables` extension owns that whole element), so once any row in a
    section needs one, the entire section's table is built here instead --
    keeps the visual result a single real <table> with one seamless
    full-width row, rather than a second table stacked underneath with a
    visible border/gap."""
    col_count = len(headers)
    head = "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    body_rows = []
    for cells, nested_html in row_specs:
        body_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>")
        if nested_html:
            body_rows.append(f'<tr class="lua-nested-field-row"><td colspan="{col_count}">{nested_html}</td></tr>')
    return f"<table><thead>{head}</thead><tbody>{''.join(body_rows)}</tbody></table>"


def render_api_page(item: dict, overlay_text: str | None, page_path: str | Path) -> str:
    lines = []
    lines.append(f"# {item['symbol']}")
    lines.append("")
    lines.append(f"`{item['syntax']}`")
    lines.append("")
    lines.append(render_doc_text(item["summary"], page_path))
    lines.append("")
    if item["aliases"]:
        lines.append("## Aliases")
        lines.append("")
        for alias in item["aliases"]:
            if alias in item["deprecated_aliases"]:
                lines.append(f"- `{alias}` (deprecated alias)")
            else:
                lines.append(f"- `{alias}`")
        lines.append("")
    lines.append("## Parameters")
    lines.append("")
    if item["parameters"]:
        parsed_params = []
        for param in item["parameters"]:
            req = "yes" if param["required"] else "no"
            intro, bullet_items = split_intro_and_bullets(render_doc_text(param["description"], page_path))
            nested_html = render_nested_field_table(bullet_items, param["type"]) if bullet_items else None
            parsed_params.append((param, req, intro, bullet_items, nested_html))
        if any(nested_html for *_, nested_html in parsed_params):
            row_specs = []
            for param, req, intro, bullet_items, nested_html in parsed_params:
                cell_html, nested_html = render_table_cell_html(intro, bullet_items, param["type"])
                row_specs.append(([html_code(param["name"]), req, html_code(param["type"]), cell_html], nested_html))
            lines.append(render_field_html_table(["Name", "Req", "Type", "Description"], row_specs))
        else:
            lines.append("| Name | Req | Type | Description |")
            lines.append("| --- | --- | --- | --- |")
            for param, req, intro, bullet_items, _ in parsed_params:
                description = render_table_cell_text(intro, bullet_items)
                lines.append(f"| `{param['name']}` | {req} | `{param['type']}` | {description} |")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Returns")
    lines.append("")
    if item["returns"]:
        parsed_returns = []
        for retval in item["returns"]:
            name = retval.get("name") or "-"
            intro, bullet_items = split_intro_and_bullets(render_doc_text(retval["description"], page_path))
            nested_html = render_nested_field_table(bullet_items, retval["type"]) if bullet_items else None
            parsed_returns.append((name, retval, intro, bullet_items, nested_html))
        if any(nested_html for *_, nested_html in parsed_returns):
            row_specs = []
            for name, retval, intro, bullet_items, nested_html in parsed_returns:
                cell_html, nested_html = render_table_cell_html(intro, bullet_items, retval["type"])
                row_specs.append(([html_code(name), html_code(retval["type"]), cell_html], nested_html))
            lines.append(render_field_html_table(["Name", "Type", "Description"], row_specs))
        else:
            lines.append("| Name | Type | Description |")
            lines.append("| --- | --- | --- |")
            for name, retval, intro, bullet_items, _ in parsed_returns:
                description = render_table_cell_text(intro, bullet_items)
                lines.append(f"| `{name}` | `{retval['type']}` | {description} |")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Availability")
    lines.append("")
    lines.append(f"- Since: `{item['availability']['since']}`")
    for radio in item["availability"].get("radios", []):
        lines.append(f"- Radio support: `{radio}`")
    lines.append("")
    if item["notes"]:
        lines.append("## Notes")
        lines.append("")
        for note in item["notes"]:
            lines.append(f"- {render_doc_text(note, page_path)}")
        lines.append("")
    lines.append("## Source")
    lines.append("")
    lines.append(f"`{item['source_location']}`")
    lines.append("")
    if overlay_text:
        lines.extend(render_overlay_sections(overlay_text))
    return "\n".join(lines)


def render_api_index(model: dict) -> str:
    current_page = Path("index.md")
    lines = []
    lines.append("# Generated API Reference")
    lines.append("")
    lines.append("This section is generated from the normalized API model and grouped with the same user-facing topic names used in the 2.11 docs.")
    lines.append("")
    for group, items in items_by_group(model):
        page = group_page_name(group)
        lines.append(f"## [{group['name']}]({doc_link(current_page, page)})")
        lines.append("")
        lines.append(f"- `{len(items)}` APIs")
        lines.append(f"- {group.get('description', 'User-facing topic grouping for this API area.')}")
        lines.append("")

    return "\n".join(lines)


def card_summary_text(summary: str) -> str:
    summary = compact_whitespace(summary)
    if not summary:
        return "Needs summary review"
    first_sentence = re.split(r"(?<=[.!?])\s+", summary, maxsplit=1)[0].strip()
    candidate = first_sentence or summary
    if len(candidate) <= 120:
        return candidate
    shortened = candidate[:117].rsplit(" ", 1)[0].strip()
    return f"{shortened}..." if shortened else f"{candidate[:117]}..."


def render_module_page(module_name: str, items: list[dict], report: dict, page_path: str | Path) -> str:
    suspicious_by_id = {}
    module_report = report["modules"].get(module_name, {})
    for suspicious in module_report.get("suspicious_items", []):
        suspicious_by_id[suspicious["id"]] = suspicious["issues"]

    lines = []
    lines.append(f"# {module_name}")
    lines.append("")
    lines.append(f"`{len(items)}` APIs in this module.")
    lines.append("")
    lines.append(f"[Back to API overview]({doc_link(page_path, 'index.md')}) | [Open review dashboard]({doc_link(page_path, 'review.md')})")
    lines.append("")
    lines.append('<div class="api-grid">')
    for item in sorted(items, key=lambda entry: entry["symbol"]):
        issues = suspicious_by_id.get(item["id"], [])
        badge = ""
        if issues:
            badge = f'<span class="api-card-badge">{" / ".join(issues)}</span>'
        summary = card_summary_text(item["summary"])
        lines.append('<a class="api-card" href="{href}">'.format(href=page_href(page_path, page_name_for_item(item))))
        lines.append(f'<span class="api-card-title">{item["symbol"]}</span>')
        lines.append(f'<span class="api-card-summary">{summary}</span>')
        if badge:
            lines.append(badge)
        lines.append("</a>")
    lines.append("</div>")
    lines.append("")
    return "\n".join(lines)


def render_group_page(group: dict, items: list[dict], page_path: str | Path) -> str:
    lines = []
    lines.append(f"# {group['name']}")
    lines.append("")
    lines.append(group.get("description", ""))
    lines.append("")
    if not items:
        lines.append("No extracted APIs are assigned to this group yet.")
        lines.append("")
        return "\n".join(lines)
    lines.append('<div class="api-grid">')
    for item in sorted(items, key=lambda entry: entry["symbol"]):
        summary = card_summary_text(item["summary"])
        lines.append('<a class="api-card" href="{href}">'.format(href=page_href(page_path, page_name_for_item(item))))
        lines.append(f'<span class="api-card-title">{item["symbol"]}</span>')
        lines.append(f'<span class="api-card-summary">{summary}</span>')
        lines.append("</a>")
    lines.append("</div>")
    lines.append("")
    return "\n".join(lines)


def render_overlay_sections(overlay_text: str) -> list[str]:
    text = overlay_text.strip()
    if not text:
        return []

    lines = []
    for raw_line in text.splitlines():
        if raw_line.startswith("## "):
            lines.append(raw_line)
        elif raw_line.startswith("# "):
            lines.append(f"### {raw_line[2:]}")
        else:
            lines.append(raw_line)
    lines.append("")
    return lines


def render_review_page(model: dict) -> str:
    current_page = Path("review.md")
    report = quality_report(model)
    decisions = load_review_decisions()
    lines = []
    lines.append("# API Review Dashboard")
    lines.append("")
    lines.append("This page is generated from the extracted API model and is meant to speed up review of the real source-derived docs.")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append(f"- Docs version: `{model['docs_version']}`")
    lines.append(f"- Upstream ref: `{model['upstream_ref']}`")
    lines.append(f"- Generated at: `{model['generated_at']}`")
    lines.append(f"- Total items: `{len(model['items'])}`")
    lines.append(f"- Review backlog entries: `{len(report['backlog'])}`")
    reviewed_backlog = sum(1 for entry in report["backlog"] if entry["id"] in decisions)
    lines.append(f"- Backlog items with saved decisions: `{reviewed_backlog}`")
    lines.append("")
    lines.append("## Module Health")
    lines.append("")
    lines.append("| Module | Items | Unknown Param Types | Unknown Return Types |")
    lines.append("| --- | ---: | ---: | ---: |")
    for module_name, data in report["modules"].items():
        lines.append(
            f"| `{module_name}` | {data['items']} | {data['unknown_param_types']} | {data['unknown_return_types']} |"
        )
    lines.append("")
    lines.append("## Review Backlog")
    lines.append("")
    if report["backlog"]:
        lines.append("| API | Status | Module | Parser Fixable | Upstream Fix Likely |")
        lines.append("| --- | --- | --- | --- | --- |")
        for entry in report["backlog"]:
            page_name = review_page_name_for_item(entry)
            parser_fixable = ", ".join(entry["parser_fixable"]) or "-"
            upstream_fix_likely = ", ".join(entry["upstream_fix_likely"]) or "-"
            decision = decisions.get(entry["id"])
            status = "`pending`"
            if decision:
                status = f"`reviewed` ({decision.get('updated_at', 'saved')})"
            lines.append(
                f"| [`{entry['id']}`]({doc_link(current_page, page_name)}) | {status} | `{entry['module']}` | `{parser_fixable}` | `{upstream_fix_likely}` |"
            )
    else:
        lines.append("No backlog items.")
    lines.append("")
    lines.append("## Suspicious Items By Module")
    lines.append("")
    item_by_id = {item["id"]: item for item in model["items"]}
    for module_name, data in report["modules"].items():
        if not data["suspicious_items"]:
            continue
        lines.append(f"### {module_name}")
        lines.append("")
        lines.append("| API | Issues | Source |")
        lines.append("| --- | --- | --- |")
        for suspicious in data["suspicious_items"]:
            item = item_by_id[suspicious["id"]]
            issues = ", ".join(suspicious["issues"])
            lines.append(
                f"| [`{item['id']}`]({doc_link(current_page, review_page_name_for_item(item))}) | `{issues}` | `{source_label(item)}` |"
            )
        lines.append("")
    lines.append("## Suggested Spot Checks")
    lines.append("")
    for item_id in [
        "getRSSI",
        "getSourceValue",
        "popupConfirmation",
        "lcd.drawText",
        "model.setModule",
    ]:
        item = item_by_id.get(item_id)
        if not item:
            continue
        lines.append(f"- [`{item_id}`]({doc_link(current_page, review_page_name_for_item(item))}) - {item['summary'] or 'Needs summary review'}")
    lines.append("")
    return "\n".join(lines)


def render_review_item_page(item: dict, page_path: str | Path) -> str:
    action_title, action_detail = review_action(item)
    unknown_params = [param["name"] for param in item["parameters"] if param["type"] == "unknown"]
    unknown_returns = [ret.get("name") or "-" for ret in item["returns"] if ret["type"] == "unknown"]
    lines = []
    lines.append(f"# Review: {item['id']}")
    lines.append("")
    lines.append(f"[Back to dashboard]({doc_link(page_path, 'review.md')}) | [Open API page]({doc_link(page_path, page_name_for_item(item))})")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append(f"- Module: `{item['module']}`")
    lines.append(f"- Current symbol: `{item['symbol']}`")
    lines.append(f"- Doc id: `{item['doc_id']}`")
    lines.append(f"- Source: `{source_label(item)}`")
    lines.append(f"- Recommended action: **{action_title}**")
    lines.append(f"- Why: {action_detail}")
    lines.append("")
    if item["aliases"]:
        lines.append("## Aliases")
        lines.append("")
        for alias in item["aliases"]:
            suffix = " (deprecated)" if alias in item["deprecated_aliases"] else ""
            lines.append(f"- `{alias}`{suffix}")
        lines.append("")
    lines.append("## Decide")
    lines.append("")
    if unknown_params or unknown_returns:
        if unknown_params:
            lines.append(f"- Unknown params to decide: `{', '.join(unknown_params)}`")
        if unknown_returns:
            lines.append(f"- Unknown returns to decide: `{', '.join(unknown_returns)}`")
        lines.append("- Use the selector table below. Your choices are saved into `docs-system/generated/review-decisions.json`, which I can read later to patch the C++ `luadoc` block.")
    else:
        lines.append("- This one looks structurally complete, but you can still change any param or return type below if you want to override it.")
    lines.append("")
    lines.append("### Decision Controls")
    lines.append("")
    lines.extend(render_decision_controls(item))
    lines.append("")
    lines.append('<div class="review-workbench">')
    lines.append('<section class="review-panel">')
    lines.append("### Source luadoc")
    lines.append("")
    lines.append("~~~~text")
    lines.append(item["raw_luadoc"].strip() or "<raw luadoc unavailable in this model>")
    lines.append("~~~~")
    lines.append("</section>")
    lines.append('<section class="review-panel">')
    lines.append("### Parsed doc")
    lines.append("")
    lines.append("#### Summary")
    lines.append("")
    lines.append(render_doc_text(item["summary"], page_path) or "None.")
    lines.append("")
    lines.append("#### Parameters")
    lines.append("")
    if item["parameters"]:
        lines.append("| Name | Req | Type | Description |")
        lines.append("| --- | --- | --- | --- |")
        for param in item["parameters"]:
            req = "yes" if param["required"] else "no"
            lines.append(
                f"| `{param['name']}` | {req} | `{param['type']}` | {render_doc_text(param['description'], page_path).replace(chr(10), ' ')} |"
            )
    else:
        lines.append("None.")
    lines.append("")
    lines.append("#### Returns")
    lines.append("")
    if item["returns"]:
        lines.append("| Name | Type | Description |")
        lines.append("| --- | --- | --- |")
        for retval in item["returns"]:
            name = retval.get("name") or "-"
            lines.append(
                f"| `{name}` | `{retval['type']}` | {render_doc_text(retval['description'], page_path).replace(chr(10), ' ')} |"
            )
    else:
        lines.append("None.")
    lines.append("")
    lines.append("#### Notes")
    lines.append("")
    if item["notes"]:
        for note in item["notes"]:
            lines.append(f"- {render_doc_text(note, page_path)}")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("</section>")
    lines.append("</div>")
    lines.append("")
    lines.append("## Suggested luadoc patch")
    lines.append("")
    lines.append("Use this as a starting point when the issue is in the C++ annotation. `TODO` means you still need to choose the real type.")
    lines.append("")
    lines.append("~~~~text")
    lines.append(render_suggested_luadoc(item))
    lines.append("~~~~")
    lines.append("")
    return "\n".join(lines)


LUADOC_BLOCK_RE = re.compile(r"/\*luadoc(.*?)\*/", re.DOTALL)
FUNCTION_RE = re.compile(r"^@function\s+(.+)$", re.MULTILINE)
PARAM_RE = re.compile(r"^[ \t]*@param\s+(.+?)(?:\n\s*\n|\Z)", re.MULTILINE | re.DOTALL)
RETVAL_RE = re.compile(r"^[ \t]*@retval\s+(.+?)(?:\n\s*\n|\Z)", re.MULTILINE | re.DOTALL)
NOTICE_RE = re.compile(r"^[ \t]*@notice\s+(.+?)(?:\n\s*\n|\Z)", re.MULTILINE | re.DOTALL)
STATUS_RE = re.compile(r"^[ \t]*@status\s+(.+)$", re.MULTILINE)
TAG_START_RE = re.compile(r"^@(param|retval|notice|status)\b")
COMMON_BLOCK_RE = re.compile(r"^@common\s+(\S+)\s*\n(.*)\Z", re.DOTALL)
COMMONPARAMS_REF_RE = re.compile(r"^[ \t]*@commonparams\s+(\S+)\s*$", re.MULTILINE)
MARKDOWN_TABLE_RE = re.compile(r"^\|.*\|$")
LIST_LINE_RE = re.compile(r"^\s*[*-]\s+")
CODE_FENCE_RE = re.compile(r"^\s*```")
KNOWN_VALUE_TYPES = {
    "string",
    "number",
    "integer",
    "boolean",
    "table",
    "function",
    "nil",
    "value",
    "multiple",
    "buffer",
}
GOLDEN_MODULES = {"runtime", "lcd", "model"}
LEGACY_DOC_LINK_REWRITES = [
    (
        "../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html#color-constants",
        "../api-overview/constants/color-constants.md#indexed-colors",
    ),
    (
        "../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html",
        "../programming/core-concepts/drawing-flags-and-colors.md",
    ),
    (
        "../../part_vii_-_appendix/fonts.md",
        "../api-overview/fonts.md",
    ),
    (
        "../../appendix/units.html",
        "../api-overview/constants/units.md",
    ),
    (
        "../appendix/units.html",
        "../api-overview/constants/units.md",
    ),
    (
        "(../appendix/units.html)",
        "(../api-overview/constants/units.md)",
    ),
    (
        "../key_events.md",
        "../api-overview/constants/key-event-constants.md",
    ),
]


def extract_blocks(text: str) -> list[dict]:
    blocks = []
    for match in LUADOC_BLOCK_RE.finditer(text):
        line_number = text.count("\n", 0, match.start()) + 1
        blocks.append(
            {
                "text": match.group(1).strip(),
                "line": line_number,
            }
        )
    return blocks


def split_signature(function_decl: str) -> tuple[str, str]:
    if "(" not in function_decl or not function_decl.endswith(")"):
        return function_decl.strip(), ""
    name, params = function_decl.split("(", 1)
    return name.strip(), params[:-1].strip()


def parse_since(status_text: str | None) -> str:
    if not status_text:
        return "unknown"
    match = re.search(r"Introduced in ([0-9.]+)", status_text)
    return match.group(1) if match else "unknown"


def version_key(version: str) -> tuple[int, ...]:
    if version == "unknown":
        return (9999,)
    parts = []
    for piece in version.split("."):
        try:
            parts.append(int(piece))
        except ValueError:
            parts.append(9999)
    return tuple(parts)


def clean_text(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    return "\n".join(lines).strip()


def compact_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def clean_inline_markup(text: str) -> str:
    text = text.replace("`", "")
    return compact_whitespace(text)


def api_overview_doc_link(from_page: str | Path, relative_target: str) -> str:
    return sibling_doc_link(from_page, "api-overview", relative_target)


def sibling_doc_link(from_page: str | Path, sibling_dir: str, relative_target: str) -> str:
    from_path = Path(from_page)
    up_levels = [".."] * (len(from_path.parent.parts) + 1)
    target = Path(*up_levels) / sibling_dir / relative_target
    return str(target).replace(os.sep, "/")


def rewrite_legacy_doc_links(text: str, from_page: str | Path) -> str:
    rewritten = text
    rewritten = rewritten.replace(
        "[Full list]((../appendix/units.html))",
        f"[Full list]({api_overview_doc_link(from_page, 'constants/units.md')})",
    )
    for old, new in LEGACY_DOC_LINK_REWRITES:
        if old == "../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html#color-constants":
            target = api_overview_doc_link(from_page, "constants/color-constants.md#indexed-colors")
        elif old == "../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html":
            target = sibling_doc_link(from_page, "programming", "core-concepts/drawing-flags-and-colors.md")
        elif old == "../../part_vii_-_appendix/fonts.md":
            target = api_overview_doc_link(from_page, "fonts.md")
        elif old in {"../appendix/units.html", "(../appendix/units.html)", "../../appendix/units.html"}:
            target = api_overview_doc_link(from_page, "constants/units.md")
            if old.startswith("("):
                target = f"({target})"
        elif old == "../key_events.md":
            target = api_overview_doc_link(from_page, "constants/key-event-constants.md")
        else:
            target = new
        rewritten = rewritten.replace(old, target)
    rewritten = rewritten.replace(
        "[Full list]((../api-overview/constants/units.md))",
        f"[Full list]({api_overview_doc_link(from_page, 'constants/units.md')})",
    )
    return rewritten


def normalize_type_annotation(raw_type: str) -> str:
    raw_type = compact_whitespace(raw_type)
    if not raw_type:
        return "unknown"
    primary = raw_type.split(",", 1)[0].strip()
    return primary or "unknown"


def normalize_item_links(item: dict) -> None:
    item["summary"] = rewrite_legacy_doc_links(item["summary"])
    item["notes"] = [rewrite_legacy_doc_links(note) for note in item["notes"]]
    for param in item["parameters"]:
        param["description"] = rewrite_legacy_doc_links(param["description"])
    for retval in item["returns"]:
        retval["description"] = rewrite_legacy_doc_links(retval["description"])


def luals_type_parts(type_name: str) -> list[str]:
    return [part.strip() for part in type_name.split("|") if part.strip()]


def collect_custom_types(model: dict) -> list[str]:
    custom = []
    seen = set()
    for item in model["items"]:
        for type_name in [param["type"] for param in item["parameters"]] + [ret["type"] for ret in item["returns"]]:
            for part in luals_type_parts(type_name):
                if part in LUALS_BUILTIN_TYPES:
                    continue
                if part not in seen:
                    custom.append(part)
                    seen.add(part)
    return custom


def render_luals_aliases(model: dict) -> list[str]:
    type_definitions = load_type_definitions()
    lines = []
    for type_name in type_definitions.keys():
        definition = type_definitions.get(type_name, {})
        description = definition.get("description")
        alias_target = definition.get("luals_alias_of", "any")
        if description:
            lines.append(f"--- {description}")
        else:
            lines.append(f"--- Custom semantic Lua API type: {type_name}")
        lines.append(f"---@alias {type_name} {alias_target}")
    if lines:
        lines.append("")
    return lines


def split_name_description(text: str) -> tuple[str, str]:
    pieces = text.split(" ", 1)
    if len(pieces) == 1:
        return pieces[0], ""
    return pieces[0], pieces[1]


def sanitize_symbol(symbol: str) -> str:
    symbol = compact_whitespace(symbol)
    if "(" in symbol and ")" in symbol:
        symbol = symbol[: symbol.rfind(")") + 1]
    symbol = re.sub(r"\s+deprecated.*$", "", symbol, flags=re.IGNORECASE)
    return symbol.strip()


def safe_file_stem(symbol: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", symbol).strip("._") or "api-item"


def parse_param_or_retval_body(body: str, *, is_retval: bool = False) -> tuple[str, str, str]:
    body = clean_text(body)
    first_line, *rest = body.splitlines()
    stripped_line = first_line.strip()

    if is_retval and stripped_line.lower().startswith("multiple "):
        raw_name = "multiple"
        raw_type = "multiple"
        description = stripped_line[len("multiple"):].strip()
    elif is_retval and stripped_line.startswith("("):
        match = re.match(r"^\(([^)]+)\)\s*(.*)$", stripped_line)
        raw_name = ""
        raw_type = match.group(1).strip() if match else "unknown"
        description = match.group(2).strip() if match else stripped_line
    else:
        colon_match = re.match(r'^([A-Za-z0-9_"\'.,/-]*)\s*:\s*([A-Za-z0-9_|/-]+)\s*,?\s*(.*)$', stripped_line)
        if colon_match:
            raw_name = colon_match.group(1).strip()
            raw_type = colon_match.group(2).strip()
            description = colon_match.group(3).strip()
        else:
            match = re.match(r'^([A-Za-z0-9_"\'.,:/-]+)\s*\(([^)]+)\)\s*(.*)$', stripped_line)
            if match:
                raw_name = match.group(1).strip()
                raw_type = match.group(2).strip()
                description = match.group(3).strip()
                if description.startswith(":"):
                    # leftover colon from a "name (type):" line -- whether or
                    # not more content follows it on the same line, it's
                    # punctuation from the type annotation, not meaningful
                    # content (e.g. a bulleted "params (table):" settings
                    # list, or "volume (integer): - (1..5) override ...").
                    description = description[1:].strip()
            else:
                pieces = stripped_line.split(" ", 1)
                raw_name = pieces[0].strip()
                raw_type = "unknown"
                description = pieces[1].strip() if len(pieces) > 1 else ""

    if is_retval and raw_type == "unknown":
        lowered = raw_name.lower()
        if lowered in KNOWN_VALUE_TYPES:
            raw_type = lowered if lowered != "value" else "unknown"
            raw_name = ""

    if is_retval and raw_type == "function" and "or `nil`" in description:
        raw_type = "function|nil"

    if is_retval and raw_type == "string" and ("if any" in description.lower() or "blank if no error occurred" in description.lower()):
        raw_type = "string|nil"

    raw_name = raw_name.rstrip(":")
    if raw_name == "":
        raw_name = "-"

    if rest:
        extra = clean_text("\n".join(rest))
        if description and re.match(r"^[*-]\s+", extra):
            # `extra` starts with a bullet list (e.g. a `table` return value's
            # own field list, see model.getMix) -- joining with a space would
            # glue the first bullet onto the intro line (e.g. "mix data: *
            # `name` ..."), silently dropping it from bullet-list parsing
            # downstream (split_intro_and_bullets, render_nested_field_table)
            # since it's no longer at the start of its own line.
            description = f"{description}\n{extra}".strip()
        else:
            description = f"{description} {extra}".strip()

    return raw_name, normalize_type_annotation(raw_type), description


def raw_type_to_practical_type(raw_type: str) -> str:
    if "|" in raw_type:
        return "|".join(raw_type_to_practical_type(part.strip()) for part in raw_type.split("|"))
    lower = raw_type.lower()
    if lower == "nil":
        return "nil"
    if lower in {"byte", "unsigned", "coord_t", "index"}:
        return "integer"
    if "string" in lower or "text" in lower:
        return "string"
    if "bool" in lower:
        return "boolean"
    if "number" in lower or "integer" in lower or "positive" in lower or "numeric" in lower:
        return "integer"
    if "function" in lower:
        return "function"
    if "table" in lower:
        return "table"
    if "pointer" in lower:
        return "pointer"
    if "optional" in lower:
        return "unknown"
    return raw_type.replace(" ", "-")


def normalize_identifier(text: str, fallback: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    return text or fallback


def normalize_param_name(raw_name: str, signature_names: list[str], parameter_index: int) -> list[str]:
    name = raw_name.strip().rstrip(":")
    if name.startswith("(") or name in {"", "-"}:
        if parameter_index < len(signature_names):
            return [signature_names[parameter_index]]
        return [f"arg{parameter_index + 1}"]
    return [part.strip() for part in name.split(",") if part.strip()]


CONCRETE_PRACTICAL_TYPES = {"nil", "integer", "string", "boolean", "function", "table", "pointer"}


def is_concrete_practical_type(practical_type: str) -> bool:
    """True if every part of a (possibly `|`-joined) practical type is
    already one raw_type_to_practical_type recognized outright, as opposed
    to a raw type string it didn't know how to map (falls through to
    `raw_type.replace(" ", "-")`, e.g. "flags") or the "unknown" sentinel.
    Used to gate infer_type_from_description's content-sniffing heuristics
    below -- they exist to guess a real type from context when the source
    only gave a vague placeholder, and must never get a chance to
    second-guess an already-unambiguous declared type. A word like "flag"
    or "path" appearing incidentally inside an otherwise-unrelated
    description (e.g. a `table` return whose own field list happens to
    mention "file attribute flags") is exactly the false-positive this
    guards against -- confirmed empirically as the actual cause of fstat's
    return being misclassified as `integer` instead of `table`."""
    return all(part in CONCRETE_PRACTICAL_TYPES for part in practical_type.split("|"))


def infer_type_from_description(name: str, description: str, fallback_type: str, module: str) -> str:
    if is_concrete_practical_type(fallback_type):
        return fallback_type
    text = f"{name} {description}".lower()
    if module in GOLDEN_MODULES:
        if "true/false" in text or "true if" in text or "false otherwise" in text:
            return "boolean"
        if "source identifier" in text and "source name" in text:
            return "integer|string"
        if "name (string)" in text or "path" in text or "file name" in text or "file path" in text:
            return "string"
        if "table of data bytes" in text or "data bytes" in text:
            return "table"
        if "drawing flags" in text or "flag" in text:
            return "integer"
        if "index" in text or "number" in text or "value of" in text or "coordinates" in text:
            return "integer"
    return fallback_type


def parse_optional_names(signature_params: str) -> set[str]:
    optional = set()
    for chunk in re.findall(r"\[([^\]]+)\]", signature_params):
        for name in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", chunk):
            optional.add(name)
    return optional


def signature_param_names(signature_params: str) -> list[str]:
    cleaned = re.sub(r"[\[\]]", "", signature_params)
    return re.findall(r"[A-Za-z_][A-Za-z0-9_]*", cleaned)


def parse_summary(block: str) -> str:
    lines = []
    started = False
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("@function"):
            started = True
            continue
        if not started:
            continue
        if TAG_START_RE.match(stripped):
            break
        if stripped.startswith("### "):
            break
        if MARKDOWN_TABLE_RE.match(stripped) or LIST_LINE_RE.match(stripped) or CODE_FENCE_RE.match(stripped):
            break
        lines.append(line)
    cleaned = [line.rstrip() for line in lines]
    summary_lines = []
    for line in cleaned:
        stripped = line.strip()
        if stripped == "" and summary_lines:
            break
        summary_lines.append(line)
    return clean_text("\n".join(summary_lines))


def infer_module(symbol: str) -> str:
    if "." in symbol:
        return symbol.split(".", 1)[0]
    return "runtime"


def parse_block(block: str, source_location: str, source_line: int | None = None) -> dict | None:
    function_match = FUNCTION_RE.search(block)
    if not function_match:
        return None

    function_decl = sanitize_symbol(function_match.group(1).strip())
    symbol, signature_params = split_signature(function_decl)
    optional_names = parse_optional_names(signature_params)
    signature_names = signature_param_names(signature_params)
    status_match = STATUS_RE.search(block)
    availability_since = parse_since(status_match.group(1) if status_match else None)

    parameters = []
    signature_index = 0
    for param_body in PARAM_RE.findall(block + "\n\n"):
        raw_name, raw_type, description = parse_param_or_retval_body(param_body)
        names = normalize_param_name(raw_name, signature_names, signature_index)
        for name in names:
            practical_type = raw_type_to_practical_type(raw_type)
            practical_type = infer_type_from_description(name, description, practical_type, infer_module(symbol))
            parameters.append(
                {
                    "name": name,
                    "type": practical_type,
                    "required": name not in optional_names,
                    "description": clean_text(description),
                }
            )
            signature_index += 1

    if signature_names and len(parameters) == len(signature_names):
        for index, name in enumerate(signature_names):
            parameters[index]["name"] = name
            parameters[index]["required"] = name not in optional_names

    returns = []
    for retval_body in RETVAL_RE.findall(block + "\n\n"):
        raw_name, raw_type, description = parse_param_or_retval_body(retval_body, is_retval=True)
        if raw_type == "multiple":
            bullet_lines = [line.strip()[1:].strip() for line in retval_body.splitlines() if line.strip().startswith("*")]
            for index, bullet in enumerate(bullet_lines, start=1):
                if bullet.startswith("("):
                    bullet_name, bullet_type, bullet_description = parse_param_or_retval_body(bullet, is_retval=True)
                    bullet_name = normalize_identifier(bullet_description.split(".")[0], f"value{index}")
                else:
                    bullet_match = re.match(r"^(.*?)\s*\(([^)]+)\)\s*(.*)$", bullet)
                    if bullet_match:
                        bullet_name = normalize_identifier(bullet_match.group(1), f"value{index}")
                        bullet_type = bullet_match.group(2).strip()
                        bullet_description = bullet_match.group(3).strip()
                    else:
                        bullet_name, bullet_type, bullet_description = parse_param_or_retval_body(bullet, is_retval=True)
                        bullet_name = normalize_identifier(bullet_name, f"value{index}")
                returns.append(
                    {
                        "name": bullet_name or f"value{index}",
                        "type": infer_type_from_description(
                            bullet_name,
                            bullet_description,
                            raw_type_to_practical_type(bullet_type),
                            infer_module(symbol),
                        ),
                        "description": clean_text(bullet_description),
                    }
                )
            continue
        practical_type = raw_type_to_practical_type(raw_type)
        practical_type = infer_type_from_description(raw_name, description, practical_type, infer_module(symbol))
        returns.append(
            {
                "name": "" if raw_name in {"", "-"} else raw_name,
                "type": practical_type,
                "description": clean_text(description),
            }
        )

    summary = parse_summary(block)
    notes = []
    for notice_body in NOTICE_RE.findall(block + "\n\n"):
        notes.append(clean_text(notice_body))

    radios = infer_radios(source_location, notes)

    return {
        "id": symbol,
        "doc_id": default_doc_id(infer_module(symbol), symbol),
        "symbol": symbol,
        "aliases": [],
        "deprecated_aliases": [],
        "module": infer_module(symbol),
        "kind": "function",
        "syntax": function_decl,
        "summary": summary,
        "parameters": parameters,
        "returns": returns,
        "availability": {
            "since": availability_since,
            "radios": radios,
        },
        "notes": notes,
        "source_location": source_location,
        "raw_luadoc": block,
        "source_line": source_line,
    }


def infer_radios(source_location: str, notes: list[str]) -> list[str]:
    source_name = Path(source_location).name
    text = " ".join(notes).lower()
    radios = []
    if "colorlcd" in source_name or "color display" in text:
        radios.append("color-lcd")
    if "stdlcd" in source_name:
        radios.append("bw-lcd")
    if not radios:
        radios.append("all")
    return radios


def merge_item(existing: dict, incoming: dict) -> dict:
    merged = dict(existing)

    if len(incoming["parameters"]) > len(existing["parameters"]):
        merged["parameters"] = incoming["parameters"]
        merged["syntax"] = incoming["syntax"]
    if len(incoming["returns"]) > len(existing["returns"]):
        merged["returns"] = incoming["returns"]
    if len(incoming["summary"]) > len(existing["summary"]):
        merged["summary"] = incoming["summary"]

    merged["doc_id"] = existing["doc_id"]
    merged["aliases"] = unique_strings(existing.get("aliases", []) + incoming.get("aliases", []))
    merged["deprecated_aliases"] = unique_strings(
        existing.get("deprecated_aliases", []) + incoming.get("deprecated_aliases", [])
    )
    merged["notes"] = list(dict.fromkeys(existing["notes"] + incoming["notes"]))
    merged["raw_luadoc"] = incoming["raw_luadoc"] if len(incoming["raw_luadoc"]) > len(existing["raw_luadoc"]) else existing["raw_luadoc"]
    merged["source_line"] = existing.get("source_line") or incoming.get("source_line")
    merged["availability"] = {
        "since": min(
            existing["availability"]["since"],
            incoming["availability"]["since"],
            key=version_key,
        ),
        "radios": sorted(
            set(existing["availability"].get("radios", []))
            | set(incoming["availability"].get("radios", []))
        ),
    }

    locations = []
    for part in (existing["source_location"], incoming["source_location"]):
        for location in part.split("; "):
            if location not in locations:
                locations.append(location)
    merged["source_location"] = "; ".join(locations)
    return merged


def is_suspicious_item(item: dict) -> list[str]:
    issues = []
    param_names = [param["name"] for param in item["parameters"]]
    duplicates = [name for name, count in Counter(param_names).items() if count > 1]
    if duplicates:
        issues.append(f"duplicate_params:{','.join(sorted(duplicates))}")
    if re.search(r"[^A-Za-z0-9._-]", item["id"]):
        issues.append("nonportable_id")
    if any(ret["type"] == "unknown" for ret in item["returns"]):
        issues.append("unknown_return_type")
    if any(param["type"] == "unknown" for param in item["parameters"]):
        issues.append("unknown_param_type")
    return issues


def quality_report(model: dict) -> dict:
    modules = {}
    for module_name in sorted({item["module"] for item in model["items"] if item["module"] in GOLDEN_MODULES}):
        items = [item for item in model["items"] if item["module"] == module_name]
        modules[module_name] = {
            "items": len(items),
            "unknown_param_types": sum(1 for item in items for param in item["parameters"] if param["type"] == "unknown"),
            "unknown_return_types": sum(1 for item in items for ret in item["returns"] if ret["type"] == "unknown"),
            "suspicious_items": [
                {"id": item["id"], "issues": is_suspicious_item(item)}
                for item in items
                if is_suspicious_item(item)
            ][:25],
        }
    backlog = []
    for item in model["items"]:
        if item["module"] not in GOLDEN_MODULES:
            continue
        issues = is_suspicious_item(item)
        if issues:
            backlog.append(
                {
                    "id": item["id"],
                    "doc_id": item["doc_id"],
                    "module": item["module"],
                    "parser_fixable": [issue for issue in issues if issue != "unknown_param_type" and issue != "unknown_return_type"],
                    "upstream_fix_likely": [issue for issue in issues if issue in {"unknown_param_type", "unknown_return_type"}],
                }
            )
    return {"modules": modules, "backlog": backlog[:40]}


def parse_common_block(block: str) -> tuple[str, str] | None:
    """Recognize a `@common <name>` block (a reusable, non-callable chunk of
    luadoc body text) and return its (name, body). Returns None for any
    block that isn't a `@common` block (e.g. a normal `@function` block)."""
    match = COMMON_BLOCK_RE.match(block.strip())
    if not match:
        return None
    return match.group(1).strip(), match.group(2)


def expand_common_params(
    block: str,
    common_blocks: dict[str, str],
    used: set[str],
    relative_path: str,
    line: int | None,
) -> str:
    """Replace every `@commonparams <name>` reference in `block` with the
    body text of the matching `@common <name>` block, textually, before the
    normal @param/@retval/etc. parsing runs. Raises if a reference points at
    an undefined @common block."""

    def replace(match: re.Match) -> str:
        name = match.group(1).strip()
        if name not in common_blocks:
            location = f"{relative_path}:{line}" if line else relative_path
            raise ValueError(
                f"@commonparams references undefined @common block '{name}' at {location}"
            )
        used.add(name)
        return common_blocks[name].strip("\n")

    return COMMONPARAMS_REF_RE.sub(replace, block)


def extract_model(source_dir: Path, docs_version: str, upstream_ref: str) -> dict:
    all_blocks: list[tuple[str, str, int | None]] = []
    for path in sorted(source_dir.glob("*.cpp")):
        text = path.read_text(encoding="utf-8")
        relative_path = str(path.relative_to(source_dir.parent.parent.parent))
        for block in extract_blocks(text):
            all_blocks.append((block["text"], relative_path, block["line"]))

    # Pass 1: collect @common block definitions. These are reusable chunks of
    # luadoc body text (e.g. a parameter set shared by many @function blocks)
    # and are never themselves a callable API item.
    common_blocks: dict[str, str] = {}
    common_used: set[str] = set()
    for block_text, relative_path, line in all_blocks:
        parsed_common = parse_common_block(block_text)
        if parsed_common is None:
            continue
        name, body = parsed_common
        if name in common_blocks:
            location = f"{relative_path}:{line}" if line else relative_path
            raise ValueError(f"duplicate @common block '{name}' at {location}")
        common_blocks[name] = body

    # Pass 2: expand @commonparams references against the collected @common
    # blocks, then parse @function blocks as normal. @common blocks are
    # skipped here -- they have no @function tag, so parse_block already
    # returns None for them, but we skip explicitly for clarity.
    items_by_id = {}
    for block_text, relative_path, line in all_blocks:
        if parse_common_block(block_text) is not None:
            continue
        expanded_text = expand_common_params(block_text, common_blocks, common_used, relative_path, line)
        item = parse_block(expanded_text, relative_path, line)
        if item:
            existing = items_by_id.get(item["id"])
            items_by_id[item["id"]] = merge_item(existing, item) if existing else item

    unused_common = set(common_blocks) - common_used
    if unused_common:
        print(
            f"WARNING: @common block(s) defined but never referenced by any @commonparams: "
            f"{', '.join(sorted(unused_common))}",
            file=sys.stderr,
        )

    model = {
        "docs_version": docs_version,
        "upstream_ref": upstream_ref,
        "generated_at": datetime.datetime.now(datetime.UTC).isoformat().replace("+00:00", "Z"),
        "items": sorted(items_by_id.values(), key=lambda entry: entry["id"]),
    }
    validate_model(model)
    return model


def luals_param_list(parameters: list[dict]) -> str:
    return ", ".join(normalize_identifier(param["name"], f"arg{index+1}") for index, param in enumerate(parameters))


def luals_return_annotations(returns: list[dict]) -> list[str]:
    lines = []
    for retval in returns:
        name = retval.get("name")
        safe_name = normalize_identifier(name, "") if name and name != "-" else ""
        suffix = f" {safe_name}" if safe_name else ""
        lines.append(f"---@return {retval['type']}{suffix}")
    return lines


GENERATED_MARKER_MD = (
    "<!--\n"
    "GENERATED FILE — do not hand-edit.\n"
    "Regenerated by `tools/docs_pipeline.py build` (see docs-system/README.md).\n"
    "To fix API facts (syntax, params, returns, availability): edit the upstream\n"
    "EdgeTX /*luadoc*/ comment, then re-extract and rebuild.\n"
    "To add narrative content (examples, long description, compat notes): add or\n"
    "edit docs-system/overlays/<doc_id>.md, then rebuild.\n"
    "-->\n\n"
)

GENERATED_MARKER_LUA = (
    "-- GENERATED FILE — do not hand-edit.\n"
    "-- Regenerated by `tools/docs_pipeline.py build` (see docs-system/README.md).\n"
    "-- To fix API facts: edit the upstream EdgeTX /*luadoc*/ comment, then\n"
    "-- re-extract and rebuild. To add narrative content: edit\n"
    "-- docs-system/overlays/<doc_id>.md, then rebuild.\n\n"
)


def write_generated_markdown(path: Path, content: str) -> None:
    path.write_text(GENERATED_MARKER_MD + content, encoding="utf-8")


def render_luals_module(module_name: str, items: list[dict], alias_lines: list[str]) -> str:
    lines = ["---@meta", ""]
    lines.extend(GENERATED_MARKER_LUA.rstrip("\n").split("\n"))
    lines.append("")
    lines.extend(alias_lines)
    if module_name != "runtime":
        lines.append(f"---@class {module_name}")
        lines.append(f"{module_name} = {{}}")
        lines.append("")

    for item in items:
        lines.append(f"--- {item['summary']}")
        lines.append(f"--- @since {item['availability']['since']}")
        for index, param in enumerate(item["parameters"]):
            optional = "?" if not param["required"] else ""
            param_name = normalize_identifier(param["name"], f"arg{index+1}")
            description = clean_inline_markup(param["description"])
            lines.append(f"---@param {param_name}{optional} {param['type']} {description}")
        lines.extend(luals_return_annotations(item["returns"]))
        target = item["symbol"] if module_name != "runtime" else item["symbol"]
        lines.append(f"function {target}({luals_param_list(item['parameters'])}) end")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_outputs(
    model: dict,
    overlay_dir: Path,
    docs_output: Path,
    luals_outputs: list[Path],
    report_unowned: bool = False,
) -> None:
    ensure_dir(docs_output)
    for luals_output in luals_outputs:
        ensure_dir(luals_output)
    report = quality_report(model)

    # A zero-item group's page is normally just the empty-group stub, safe to
    # regenerate freely. But if a group has zero *currently extracted* items
    # and its page already holds real, hand-authored content (e.g. LVGL,
    # whose firmware has no luadoc annotations at all to extract from), never
    # overwrite or delete it -- both here and in the stale-page cleanup below,
    # which would otherwise unlink it before the per-group write loop ever
    # gets a chance to check what's currently on disk.
    preserved_group_pages: dict[str, str] = {}
    for group, group_items in items_by_group(model):
        if group_items:
            continue
        group_page = group_page_name(group)
        group_path = docs_output / group_page
        if not group_path.exists():
            continue
        existing = group_path.read_text(encoding="utf-8")
        rendered = render_group_page(group, group_items, group_page)
        if existing.strip() != rendered.strip():
            preserved_group_pages[group_page] = (
                f"group '{group['slug']}' has zero extracted items, but the page "
                "already has real (non-stub) content"
            )

    generated_pages = {
        "index.md",
        "review.md",
    }
    generated_pages.update(module_page_name(module_name) for module_name in {item["module"] for item in model["items"]})
    generated_pages.update(group_page_name(group) for group, _ in items_by_group(model))
    generated_pages.update(page_name_for_item(item) for item in model["items"])
    generated_pages.update(review_page_name_for_item(item) for item in model["items"])
    generated_pages -= preserved_group_pages.keys()
    for page_name in generated_pages:
        stale_page = docs_output / page_name
        if stale_page.exists():
            stale_page.unlink()

    index_path = docs_output / "index.md"
    write_generated_markdown(index_path, render_api_index(model))
    review_path = docs_output / "review.md"
    write_generated_markdown(review_path, render_review_page(model))

    modules: dict[str, list[dict]] = {}
    for item in model["items"]:
        modules.setdefault(item["module"], []).append(item)

    for module_name, module_items in sorted(modules.items()):
        module_path = docs_output / module_page_name(module_name)
        ensure_dir(module_path.parent)
        write_generated_markdown(module_path, render_module_page(module_name, module_items, report, module_page_name(module_name)))

    for group, group_items in items_by_group(model):
        group_page = group_page_name(group)
        if group_page in preserved_group_pages:
            print(f"Skipping {docs_output / group_page}: {preserved_group_pages[group_page]}. Not overwriting.")
            continue
        group_path = docs_output / group_page
        rendered = render_group_page(group, group_items, group_page)
        ensure_dir(group_path.parent)
        write_generated_markdown(group_path, rendered)

    for item in model["items"]:
        overlay_text = None
        for overlay_path in [overlay_dir / f"{item['doc_id']}.md", overlay_dir / f"{item['id']}.md"]:
            if overlay_path.exists():
                overlay_text = overlay_path.read_text(encoding="utf-8")
                break
        page_path = docs_output / page_name_for_item(item)
        ensure_dir(page_path.parent)
        write_generated_markdown(page_path, render_api_page(item, overlay_text, page_name_for_item(item)))
        review_item_path = docs_output / review_page_name_for_item(item)
        ensure_dir(review_item_path.parent)
        write_generated_markdown(review_item_path, render_review_item_page(item, review_page_name_for_item(item)))

    for module_name, module_items in sorted(modules.items()):
        alias_lines = render_luals_aliases(model)
        content = render_luals_module(module_name, sorted(module_items, key=lambda entry: entry["symbol"]), alias_lines)
        for luals_output in luals_outputs:
            target_path = luals_output / f"{module_name}.d.lua"
            target_path.write_text(content, encoding="utf-8")

    if report_unowned:
        owned = set(generated_pages) | set(preserved_group_pages.keys())
        unowned = []
        for path in sorted(docs_output.rglob("*.md")):
            rel = str(path.relative_to(docs_output))
            if rel not in owned:
                unowned.append(rel)
        if unowned:
            print(
                f"\n{len(unowned)} .md file(s) under {docs_output} are not accounted "
                "for by the current model (not an index/review/module/group page, "
                "not an item page, not a preserved zero-item group page). This does "
                "NOT delete anything -- some of these may be legitimate hand-authored "
                "content with no model backing (e.g. LVGL pages); some may be genuine "
                "orphans left over from a prior run under a different page-naming "
                "scheme or group assignment. Review each one manually:"
            )
            for rel in unowned:
                print(f"  {rel}")
        else:
            print(f"\nNo unowned .md files found under {docs_output}.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Markdown and LuaLS output from a normalized API model.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract_parser = subparsers.add_parser("extract", help="Extract a normalized API model from EdgeTX luadoc comments.")
    extract_parser.add_argument("--source-dir", required=True, type=Path)
    extract_parser.add_argument("--docs-version", required=True)
    extract_parser.add_argument("--upstream-ref", required=True)
    extract_parser.add_argument("--output", required=True, type=Path)

    validate_parser = subparsers.add_parser("validate", help="Validate a normalized API model.")
    validate_parser.add_argument("input", type=Path)

    report_parser = subparsers.add_parser("report", help="Generate a quality report for golden modules.")
    report_parser.add_argument("input", type=Path)
    report_parser.add_argument("--output", type=Path)

    build_parser = subparsers.add_parser("build", help="Build Markdown and LuaLS outputs.")
    build_parser.add_argument("--input", required=True, type=Path)
    build_parser.add_argument("--overlay-dir", required=True, type=Path)
    build_parser.add_argument("--docs-output", required=True, type=Path)
    build_parser.add_argument("--luals-output", required=True, type=Path, nargs="+")
    build_parser.add_argument(
        "--report-unowned",
        action="store_true",
        help=(
            "After building, list every .md file under --docs-output that the "
            "current model doesn't account for (not an index/review/module/group "
            "page, not an item page, not a preserved zero-item group page). "
            "Report-only -- never deletes anything. Some listed files may be "
            "legitimate hand-authored content the pipeline has no model data "
            "for (e.g. LVGL pages); some may be genuine orphans left over from "
            "a prior run under a different page-naming scheme or group "
            "assignment. Review each one manually before deleting."
        ),
    )

    nav_parser = subparsers.add_parser(
        "update-nav", help="Regenerate the API Reference item nav sub-tree in one or more mkdocs config files."
    )
    nav_parser.add_argument("--input", required=True, type=Path)
    nav_parser.add_argument("--mkdocs-config", required=True, type=Path, nargs="+")

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        if args.command == "extract":
            model = extract_model(args.source_dir, args.docs_version, args.upstream_ref)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")
            print(f"Extracted {len(model['items'])} items into {args.output}")
            return 0

        if args.command == "validate":
            load_model(args.input)
            print(f"Validated {args.input}")
            return 0

        if args.command == "report":
            model = load_model(args.input)
            report = quality_report(model)
            text = json.dumps(report, indent=2) + "\n"
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(text, encoding="utf-8")
                print(f"Wrote quality report to {args.output}")
            else:
                print(text, end="")
            return 0

        if args.command == "build":
            model = load_model(args.input)
            build_outputs(model, args.overlay_dir, args.docs_output, args.luals_output, args.report_unowned)
            print(f"Built Markdown into {args.docs_output}")
            for luals_output in args.luals_output:
                print(f"Built LuaLS into {luals_output}")
            return 0

        if args.command == "update-nav":
            model = load_model(args.input)
            nav_lines = render_nav_yaml_block(model)
            for config_path in args.mkdocs_config:
                update_mkdocs_nav(config_path, nav_lines)
                print(f"Updated nav in {config_path}")
            return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
