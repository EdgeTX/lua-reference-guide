---
description: >-
  This chapter will show you some ways that large script projects can be fitted
  into the limited memory of our radios.
---

# Saving Memory

Regarding memory, the situation is a bit different for the radios with black/white or grey scale screens and telemetry scripts, and the radios with color screens and widget scripts. The telemetry script radios only have 128-192 KB RAM memory - that is _very_ small! The widget script radios have 8 MB RAM memory. But the way that widgets are designed means that _all_ widget scripts present on the SD card will be loaded into memory, whether or not they are actually used. Therefore, different strategies should be applied to save memory for the two different types of radios and scripts.

## Telemetry Script Radios

Radios with black/white or grey scale screens and telemetry scripts such as e.g. FrSky Taranis, Xlite, Jumper T12 and Radiomaster TX16 have extremely small RAM memories, and therefore it may be necessary to divide up your script into smaller loadable modules.

The following simple example demonstrates how different screens can be loaded on demand, and how shared data can be stored in a table.

```lua
-- Main telemetry script

local shared = { }
shared.screens = {
  "/SCRIPTS/Test/menu1.lua",
  "/SCRIPTS/Test/menu2.lua",
  "/SCRIPTS/Test/menu3.lua"
}

function shared.changeScreen(delta)
  shared.current = shared.current + delta
  if shared.current > #shared.screens then
    shared.current = 1
  elseif shared.current < 1 then
    shared.current = #shared.screens
  end
  local chunk = loadScript(shared.screens[shared.current])
  chunk(shared)
end

local function init()
  shared.current = 1
  shared.changeScreen(0)
end

local function run(event)
  shared.run(event)
end

return { run = run, init = init }
```

```lua
-- /SCRIPTS/Test/menu1.lua

local shared = ...

function shared.run(event)
  lcd.clear()
  lcd.drawText(20, 10, "Screen 1", MIDSIZE)
  
  if event == EVT_VIRTUAL_NEXT then
    shared.changeScreen(1)
  elseif event == EVT_VIRTUAL_PREV then
    shared.changeScreen(-1)
  end
end
```

```lua
-- /SCRIPTS/Test/menu2.lua

local shared = ...

function shared.run(event)
  lcd.clear()
  lcd.drawText(20, 10, "Screen 2", MIDSIZE)
  
  if event == EVT_VIRTUAL_NEXT then
    shared.changeScreen(1)
  elseif event == EVT_VIRTUAL_PREV then
    shared.changeScreen(-1)
  end
end
```

```lua
-- /SCRIPTS/Test/menu3.lua

local shared = ...

function shared.run(event)
  lcd.clear()
  lcd.drawText(20, 10, "Screen 3", MIDSIZE)
  
  if event == EVT_VIRTUAL_NEXT then
    shared.changeScreen(1)
  elseif event == EVT_VIRTUAL_PREV then
    shared.changeScreen(-1)
  end
end
```

The table `shared` contains data that is shared between the main telemetry script and the loadable screens. Notice that the functions `shared.changeScreen` and `shared.run` are also shared this way.

Code is loaded by `shared.changeScreen` with the `loadScript` function, which returns the loadable script as a chunk of code. The code is executed with `shared` as the argument, and the loadable script adds a new `run` function to the `shared` table. `shared.run` is called by `run` in the main script.

## Widget Script Radios

Radios with color screens and widget scripts such as e.g. FrSky Horus, Jumper T16 and Radiomaster TX16 have fairly large RAM memories, but since all widget scripts present on the SD card are always loaded into memory, they could run out if a large number of big widget scripts are present on the card - even if they are not being used by the selected model. Therefore, large widget scripts should be divided into a small main script and a large loadable part.



