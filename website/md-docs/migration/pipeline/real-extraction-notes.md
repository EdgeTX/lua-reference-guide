# Real Extraction Notes

This page summarizes the first extraction run against a real local EdgeTX checkout, so the generated API section can be reviewed as a concrete preview instead of a sample-only scaffold.

## Extraction Baseline

- EdgeTX source: local checkout at `/Users/pfeerick/repos/EdgeTX/edgetx`
- Lua source dir: `radio/src/lua`
- Source branch at extraction time: `2.12`
- Source commit at extraction time: `8718d2473a` (EdgeTX/edgetx#7771 merged: adds `/*luadoc */` annotations for the LVGL Lua API)
- Docs version tag used for the local run: `2.12`

## Current Results

- Extracted API items: `198`
- Modules discovered:
  - `runtime`: `73`
  - `lcd`: `39`
  - `model`: `37`
  - `Bitmap`: `4`
  - `lvgl`: `45`

## Quality Snapshot

- `runtime`: `19` unknown parameter types, `16` unknown return types
- `lcd`: `7` unknown parameter types, `0` unknown return types
- `model`: `5` unknown parameter types, `1` unknown return type
- backlog entries recorded: `31`

## What This Proves

- The extractor can parse the current upstream `/*luadoc */` format across the real Lua source tree.
- The normalized model is good enough to produce large-scale Markdown and LuaLS previews.
- The main remaining issues are annotation-quality gaps, especially in `runtime`, rather than missing site plumbing.

## Next Cleanup Targets

1. Improve `runtime` return typing for high-traffic APIs like `getRSSI`, `getSourceValue`, and popup helpers.
2. Improve upstream annotations for structured table parameters in functions like `model.setModule`, `model.setInfo`, and `model.setTimer`.
3. Add parser heuristics only where the upstream comments are already specific enough to support them safely.
