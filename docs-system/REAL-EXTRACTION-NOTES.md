# Real Extraction Notes

This note captures the first extraction run against a real local EdgeTX checkout, so the migration work can continue from a concrete baseline instead of sample data only.

## Extraction Baseline

- EdgeTX source: `/Users/pfeerick/repos/EdgeTX/edgetx`
- Lua source dir: `radio/src/lua`
- Extracted from branch `2.12`
- Extracted from commit `8718d2473a` (EdgeTX/edgetx#7771 merged: adds `/*luadoc */` annotations for the LVGL Lua API)
- Docs version used for the local run: `2.12`

## Current Results

- Extracted API items: `198`
- Modules discovered:
  - `runtime`: `73`
  - `lcd`: `39`
  - `model`: `37`
  - `Bitmap`: `4`
  - `lvgl`: `45`

Generated artifacts:

- API model: `docs-system/generated/api-model.local.json`
- Quality report: `docs-system/generated/golden-module-quality.json`
- Markdown preview: `docs-system/generated/site-preview/`
- LuaLS preview: `docs-system/generated/luals-preview/`

## Quality Snapshot

From the current quality report:

- `runtime`: `19` unknown parameter types, `16` unknown return types
- `lcd`: `7` unknown parameter types, `0` unknown return types
- `model`: `5` unknown parameter types, `1` unknown return type
- backlog entries recorded: `31`

## What The Prototype Already Proves

- The extractor can parse the current upstream `/*luadoc */` format across the real Lua source tree.
- The normalized model is good enough to produce large-scale Markdown and LuaLS previews.
- The remaining quality issues are now mostly annotation-quality gaps rather than a missing pipeline.

## First High-Value Cleanup Targets

These look like the best next targets because they affect common APIs and surface directly in generated docs and LuaLS output.

### Runtime return typing

Examples:

- `getRSSI()` returns three values, but all currently resolve to `unknown`
- `getSourceValue()` still emits unknown return types for freshness/current-state values
- `popupConfirmation`, `popupInput`, and `popupWarning` have weak return typing

### Structured table parameters

Examples:

- `model.setModule(value)`
- `model.setInfo(value)`
- `model.setTimer(value)`

These are likely better solved by improving upstream annotation detail rather than only parser heuristics.

### LCD optional color/flag parameters

Examples:

- `lcd.drawText(..., inversColor)`
- `lcd.drawTimer(...)`
- `lcd.drawNumber(...)`

Some of these may be parser-fixable if we add better heuristics for color and flag-related parameter descriptions.

## Recommendation For The Next Pass

1. Focus on `runtime`, especially frequently used functions with `unknown` returns.
2. Improve upstream `/*luadoc */` comments first where the comments are underspecified.
3. Add parser heuristics only where the source comments are already clear and structured enough to support them.
4. Re-run `extract`, `report`, and `build` after each focused annotation batch to measure improvement.
