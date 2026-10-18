# Overlay Contract

Overlays are the downstream enrichment layer for a generated API page.

They are stored separately from the upstream source annotations and are merged into the final docs page after the generated API truth.

## Purpose

Use overlays for content that should stay outside C++ source comments:

- examples
- compatibility notes
- screenshots
- teaching videos
- related topics
- longer guidance and practical usage notes
- multi-paragraph descriptions
- comparison tables
- migration notes

## Source Of Truth Boundary

Generated API truth always comes from upstream source annotations:

- current symbol
- syntax
- short summary
- parameters
- returns
- availability
- short notices
- source location

Overlays must not override that generated truth.

Stable page identity comes from the docs-owned `doc_id`, so the overlay filename can stay the same even when the preferred Lua symbol changes.

## Current File Layout

Overlay files live in:

- `docs-system/overlays/<api-id>.md`
- preferably `docs-system/overlays/<doc-id>.md` for stable page identity

Examples:

- `docs-system/overlays/runtime.get-version.md`
- `docs-system/overlays/lcd.drawBitmap.md`

## Recommended Section Headings

Use plain Markdown with `##` headings.

Recommended headings:

- `## Extended Description`
- `## Examples`
- `## Compatibility Notes`
- `## Related Topics`
- `## Additional Learning`

The renderer treats these as enrichment content and places them after the generated API sections.

## Example

```md
## Extended Description

`getVersion` returns version information for the running firmware.

## Examples

```lua
local ver = getVersion()
print(ver)
```
```

## Editorial Rule

If API facts are wrong, fix upstream source annotations first.

If explanation quality is lacking, add or improve the overlay.
