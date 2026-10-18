---
description: How to enable and use the LVGL UI layer in EdgeTX Lua scripts.
---

# Using LVGL Library

LVGL gives EdgeTX Lua scripts access to the same style of UI controls used by the firmware on color-screen radios. Instead of redrawing every element manually with the `lcd` API, a script can build a UI from objects such as labels, boxes, pages, buttons, toggles, sliders, and dialogs.

The practical result is:

- less manual redraw logic
- better support for state-driven UI updates
- a closer match to native EdgeTX screens

For the detailed constructor pages, see [Display LVGL](../../api-reference/display-lvgl/index.md). For LVGL-specific constants, see [LVGL Constants](../../api-overview/constants/lvgl-constants.md).

## Limitations

- Direct drawing through the `lcd` API is not available inside scripts that use LVGL to create the UI.
- LVGL is only available on radios and builds that support the LVGL UI layer.

## Activating the LVGL API

A script must return `useLvgl = true` in the table it exports:

```lua
return { init = init, run = run, useLvgl = true }
```

When LVGL is available, EdgeTX exposes a global `lvgl` object. This is the main entry point for building and updating the UI.

Scripts should still check that `lvgl` is not `nil` before using it. If it is `nil`, the script is usually:

- running on an earlier EdgeTX version
- running on a target without LVGL support
- missing `useLvgl = true`

In that case, the script should show a clear error or fall back to a non-LVGL implementation.

## Usage Patterns

### One-Time scripts

For One-Time scripts, `init()` should still prepare the initial script state, but it should also create the LVGL UI tree. The `run()` function can still handle events, but most interaction should be delegated to the LVGL objects themselves.

When used this way, the UI updates automatically as state changes instead of being redrawn by hand every cycle.

### Widget scripts

Widget scripts should usually create or rebuild their LVGL UI in `update()`, using the widget zone size to decide layout. The `background()` and `refresh()` functions should focus on state updates that are not already managed by the LVGL objects.

### Controls and focus

Interactive controls such as buttons, toggles, and text editors show a focus outline when selected. Leave enough space between nearby controls so that outline remains visible and does not collide with surrounding content.

## Common Call Pattern

Most LVGL constructors follow this shape:

```lua
lvgl.function([parent], { settings })
```

The optional `parent` object determines where the new object is attached. If no parent is passed, the object is created in the top-level script window.

Most functions return an LVGL object, so you can keep a reference and update it later or call object methods on it.

LVGL functions can also be used with Lua OO syntax:

```lua
lvgl.show(parent)
parent:show()
```

## Shared Settings

Many LVGL objects share a few common settings:

| Name | Type | Purpose |
| --- | --- | --- |
| `x`, `y` | `number` | Position relative to the top-left of the parent |
| `w`, `h` | `number` | Width and height |
| `color` | color or function | Primary color for the object |
| `pos` | function | Dynamic position callback returning `x, y` |
| `size` | function | Dynamic size callback returning `w, h` |
| `visible` | function | Dynamic visibility callback |
| `floating` | `boolean` | Keep an object fixed inside a scrollable container |

Functions used for settings are called repeatedly by the firmware. When the function returns a new value, the object updates automatically.

## Adapting To Different Screens

EdgeTX supports several color-screen sizes and orientations, so fixed coordinates do not always scale cleanly. A few LVGL helpers make this easier:

- flex layouts can reduce manual positioning
- `lvgl.PAGE_BODY_HEIGHT` gives the body height of a page container
- `lvgl.UI_ELEMENT_HEIGHT` gives the default control height
- `lvgl.LCD_SCALE` helps scale fixed values for the current screen
- `lvgl.PERCENT_SIZE + N` can be used for percentage-based sizes and positions

Use percentage sizing carefully: the parent container must already have a defined size, and not every object type supports percentage-based values equally well.

## Examples

### One-Time script

```lua
local exitTool = false

local function close()
  lvgl.confirm({
    title = "Exit",
    message = "Really exit?",
    confirm = function()
      exitTool = true
    end,
  })
end

local function init()
  if lvgl == nil then
    return
  end

  lvgl.clear()

  local pg = lvgl.page({
    title = "Test Tool",
    subtitle = "Page 1",
    back = close,
  })

  pg:label({ x = 70, y = 16, color = BLACK, font = DBLSIZE, text = "Test Page" })
  pg:button({ x = 200, y = 150, text = "CLOSE", press = close })
end

local function run()
  if lvgl == nil then
    lcd.drawText(0, 0, "LVGL support required", COLOR_THEME_WARNING)
  end

  if exitTool then
    return 2
  end

  return 0
end

return { init = init, run = run, useLvgl = true }
```

### Widget script

```lua
local options = {
  { "Color", COLOR, COLOR_THEME_SECONDARY1 },
  { "Shadow", BOOL, 0 },
}

local function create(zone, options)
  return { zone = zone, options = options, counter = 0 }
end

local function update(wgt, options)
  wgt.options = options

  lvgl.clear()

  if wgt.options.Shadow ~= 0 then
    lvgl.label({
      x = wgt.zone.x + 1,
      y = wgt.zone.y + 1,
      color = BLACK,
      font = DBLSIZE,
      text = function()
        return wgt.counter
      end,
    })
  end

  lvgl.label({
    x = wgt.zone.x,
    y = wgt.zone.y,
    color = wgt.options.Color,
    font = DBLSIZE,
    text = function()
      return wgt.counter
    end,
  })
end

local function background(wgt)
  wgt.counter = wgt.counter + 1
end

local function refresh(wgt)
  wgt.counter = wgt.counter + 1
end

return {
  name = "CounterLVGL",
  options = options,
  create = create,
  update = update,
  refresh = refresh,
  background = background,
  useLvgl = true,
}
```
