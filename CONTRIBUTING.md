# Contributing

This repo has three kinds of content. Mixing them up is the #1 way to lose
work — a regenerate silently overwrites a hand-edit. Check which class a
file belongs to before you edit it. For the full architecture rationale, see
[`MIGRATION-PLAN.md`](MIGRATION-PLAN.md); this file is just the practical
"where do I make this edit" guide.

## The three content classes

### 1. Generated API reference — do not hand-edit

- `website/md-docs/api-reference/**` — every per-function page, plus
  `module-*.md`, `review-*.md`, and `review.md`
- `docs-system/generated/luals/*.d.lua` and `website/md-docs/assets/luals/*.d.lua`
  (both written by the same `build` run — see [Pipeline commands](#pipeline-commands))

These are produced by `tools/docs_pipeline.py build` from Lua API facts
(syntax, params, returns, availability) parsed out of `/*luadoc */` comments
in the upstream EdgeTX firmware source, plus any matching overlay content
merged on top. Every file in this class starts with a comment like:

```
<!--
GENERATED FILE — do not hand-edit.
...
-->
```

If you see that comment, don't edit the file directly — the next `build` run
overwrites it silently with no warning. Fix the actual source instead (see
below).

### 2. Overlays — edit directly

- `docs-system/overlays/<doc_id>.md` (legacy fallback: `<id>.md`)

Narrative content that doesn't belong in a terse C++ comment: long
descriptions, worked examples, compatibility notes, related topics. Merged
onto the end of the matching generated API reference page by `build`.
Missing overlays are fine — not every function needs one.

### 3. Hand-authored guides — edit directly

- `website/md-docs/programming/**`
- `website/md-docs/api-overview/**`
- `website/md-docs/radios/**`

Plain markdown, no generation involved. Normal PR flow.

## "I want to fix X" — which class am I in?

- **Wrong or missing API fact** (syntax, params, returns, availability) on a
  generated page → don't touch the `.md`/`.d.lua`. Fix the upstream
  `/*luadoc */` comment in the EdgeTX firmware repo, then re-extract and
  rebuild here.
- **Missing example or explanation** on a generated page → add or edit the
  matching `docs-system/overlays/<doc_id>.md`, then rebuild. No upstream PR
  needed.
- **Typo or content issue** on a hand-authored guide or an overlay → edit it
  directly, normal PR.
- **A bug affecting many generated pages at once** (a broken link pattern, a
  formatting mistake) → the bug is in `tools/docs_pipeline.py`'s renderer,
  not in the individual pages. Fix the renderer, then rebuild. Do not hand-
  patch every affected page one at a time — that's exactly what happened in
  commits `0988101a` and `67ba1431`, and it's the mistake the generated-file
  marker above exists to make visible.

## Pipeline commands

```sh
uv run python3 tools/docs_pipeline.py extract \
  --source-dir /path/to/edgetx/radio/src/lua \
  --docs-version 2.12 \
  --upstream-ref edgetx-2.12 \
  --output /tmp/api-model.2.12.json

uv run python3 tools/docs_pipeline.py validate /tmp/api-model.2.12.json

uv run python3 tools/docs_pipeline.py report /tmp/api-model.2.12.json \
  --output docs-system/generated/golden-module-quality.json

uv run python3 tools/docs_pipeline.py build \
  --input /tmp/api-model.2.12.json \
  --overlay-dir docs-system/overlays \
  --docs-output website/md-docs/api-reference \
  --luals-output docs-system/generated/luals website/md-docs/assets/luals
```

`uv` is the required toolchain (`pyproject.toml` / `uv.lock` in the repo
root) — always run pipeline and MkDocs commands through `uv run`. See
[`docs-system/README.md`](docs-system/README.md) for the full pipeline
reference.

## Local preview

```sh
mkdocs serve -f mkdocs.dev.yml -a 127.0.0.1:8014
```

`mkdocs.yml` is the public/production config. `mkdocs.dev.yml` inherits from
it and adds back the `Migration` nav section, per-module review dashboards,
and the API Review Dashboard (`exclude_docs: ""`) — that's why
`review-*.md`/`module-*.md` exist in `api-reference/` but never appear in
the public site nav. Keep only one preview server running at a time on
`8014`.

## Before submitting a PR

Verify with:

```sh
uv run mkdocs build -f mkdocs.dev.yml --strict
```

A clean strict build (zero warnings) is expected before a PR is ready for
review.
