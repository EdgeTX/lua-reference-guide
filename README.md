# EdgeTX Lua Reference Guide

This repository contains the EdgeTX Lua documentation site.

The live documentation source for the current site is in [website](website).

## Repo Layout

- `website/`: MkDocs content, theme assets, and navigation for the current docs site
- `docs-system/`: extraction contracts, overlays, generated artifacts, and pipeline notes
- `tools/`: local build and generation helpers

## Local Preview

```sh
uv run mkdocs serve -a 127.0.0.1:8014
```

This uses `mkdocs.yml`, the public/production config. It excludes the
Migration section, the API Review Dashboard, and the per-module
extraction dashboards, matching what actually ships on the published
site.

## Internal Preview (Migration docs + Review Workbench)

To see the Migration section, the per-module dashboards, and the API
review pages, serve the internal config instead:

```sh
uv run mkdocs serve -f mkdocs.dev.yml -a 127.0.0.1:8014
```

`mkdocs.dev.yml` inherits from `mkdocs.yml` and un-excludes everything
dropped from the public build. Keep only one preview server active on
`8014` at a time — switch configs by stopping one and starting the
other.

## Review Workbench

For live API review pages with saved type decisions, run the local decision server in a second terminal:

```sh
uv run python3 tools/review_decision_server.py
```

Then open the internal preview (see above) at `http://127.0.0.1:8014/` and use the API review dashboard under the site navigation.

## Contributing

- Edit the current docs under `website/`
- Keep generated or pipeline-specific notes under `docs-system/`
- Use the internal preview at `http://127.0.0.1:8014/` for review during local work
