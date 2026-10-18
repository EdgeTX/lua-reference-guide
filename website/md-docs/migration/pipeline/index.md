# Pipeline Overview

The migration introduces a deterministic docs pipeline with four layers:

1. Upstream EdgeTX source annotations
2. Normalized API model
3. Generated outputs
4. Optional overlay content

## Outputs

- Markdown API reference pages for the docs site
- LuaLS `*.d.lua` declaration files

## Overlay Layer

The generated pages can be extended by downstream overlay files for examples, compatibility notes, screenshots, videos, and related topics.

See the [Overlay Contract](overlay-contract.md) for the intended split between source-owned API truth and docs-owned learning material.

## Source Boundary

In the current pipeline, upstream C++ annotations are intentionally kept compact:

- syntax and signature
- one short summary
- parameter and return metadata
- availability and source facts

Richer authored material belongs in overlay markdown files, not in `/*luadoc */` prose blocks.

## Current implementation

The current repo implementation uses sample JSON input to validate the renderer and directory conventions before wiring in the upstream extractor.
