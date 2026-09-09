# API Schema

The normalized API schema is stored at `docs-system/schema/api-model-v1.schema.json`.

The generator currently expects one top-level object with:

- `docs_version`
- `upstream_ref`
- `generated_at`
- `items`

Each API item includes:

- `id`
- `symbol`
- `module`
- `kind`
- `syntax`
- `summary`
- `parameters`
- `returns`
- `availability`
- `notes`
- `source_location`

The schema is intentionally small for the first implementation and can grow once the upstream extractor is ready.
