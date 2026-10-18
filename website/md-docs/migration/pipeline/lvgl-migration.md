# LVGL Migration Notes

This page tracks the migration work for the `Display LVGL` section.

## Current Status

The LVGL binding exists in EdgeTX, and the docs site now includes a checked-in `Display LVGL` section with grouped links to generated `lvgl.*` pages. However, LVGL still does not yet have the same level of extractable LuaDoc coverage as the older `runtime`, `lcd`, and `model` APIs.

## Upstream Source Of Truth

The current LVGL Lua binding surface is defined primarily in these upstream files:

- `radio/src/lua/api_colorlcd_lvgl.cpp`
- `radio/src/lua/lua_lvgl_widget.cpp`
- `radio/src/lua/lua_lvgl_widget.h`

`api_colorlcd_lvgl.cpp` exposes the public `lvgl` Lua library. The widget implementation files define the supported object types and many of the accepted parameter keys.

## Migration Goals

The target state is:

1. upstream C++ comments are the source of truth for LVGL syntax
2. the docs pipeline extracts `lvgl.*` APIs the same way it already extracts `runtime`, `lcd`, and `model`
3. the MkDocs `Display LVGL` section becomes a fully pipeline-driven user-facing reference with minimal manual maintenance

## Current Gaps

The remaining migration gaps are:

- fuller LuaDoc coverage for the supported table keys of each object type
- better documentation coverage for exported constants that matter to script authors
- smoother alignment between generated LVGL output and the checked-in `API Reference` structure

## Recommended Grouping

The current API surface suggests this eventual user-facing grouping:

1. Runtime Helpers
2. Drawing Primitives
3. Containers
4. Interactive Controls
5. Pickers And Selectors
6. Popup Helpers
7. Constants
