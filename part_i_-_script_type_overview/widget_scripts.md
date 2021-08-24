# Widget Scripts

## Overview

Widgets are only available on radios with color displays. Most of the time, they show some info in a 'zone' either in the _top bar_ or in one of the user defined _main views_, and they cannot receive direct input from the user via key events like e.g. Telemetry scripts.

But widgets on the _main views_ can also be shown in _full screen mode_, where they take over the entire screen area, and then they can receive user input via key events, and for radios with touch screen, also touch events.

Each model can have up to five _main views_, with up to 8 widgets per screen, depending on their size and layout. Each instance of a widget has his own custom settings.

**Please note:** Widget scripts are only available on radios with color screens, such as e.g. FrSky Horus models, Radiomaster TX16 and and Jumper T16.

## Lifetime of widgets

All widget scripts on the SD card are loaded into memory when the model is selected; even widgets that are not added to the screen anywhere. This has the side effect that any global functions defined in a widget script will always be available to other widget scripts. It also means that any script on the SD card will consume part of the radio's memory - even if it is not being used. Therefore, it is important to either keep widget scripts small, or to use Lua's loadScript\(\) function to load code dynamically.

They can be added to the _top bar_ or a _main view_  through the telemetry setup menu. When  a widget has been added to a screen, then the widget functions are called as follows:

* `create` function is called one time when the widget instance is registered on the screen.
* `update` function is called upon registration and at change of settings in the telemetry setup menu.
* `background` function is called periodically when custom telemetry screen is _not visible_. **Note:** this is different from the way telemetry scripts are handled.
* `refresh` function is periodically called when custom telemetry screen is _visible_.
* A widget script is stopped and disabled if it misbehaves \(e.g. too long runtime, run-time error, or low memory\)
* All widgets are stopped while one-time script is running \(see [One-Time scripts](one-time_scripts.md)\).

## File Location

Widgets are located on the SD card, each in their specific folder /WIDGETS/&lt;_name_&gt;/main.lua \(&lt;_name_&gt; must be in 8 characters or less\).

## Interface

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `name` string
* `options` table
* `create` function
* `update` function
* `background` function \(optional\)
* `refresh` function

### Example \(draws a moving counter that counts only when not visible\):

```lua
local name = "WidgetName"

-- Create a table with default options
-- Options can be changed from the Widget Settings menu
-- Notice that each line is a table inside { }
local options = {
  { "Source", SOURCE, 1 },
  -- BOOL is actually not a boolean, but toggles between 0 and 1
  { "Boolean", BOOL, 1 },
  { "Value", VALUE, 1, 0, 10},
  { "Color", COLOR, ORANGE },
}

local function create(zone, options)
  -- Runs one time when widget instance is registered
  -- Store zone and options in the widget table for later
  local widget = {
    zone = zone,
    options = options
  }
  -- Add local variables to the widget table,
  -- unless you want to share with other instances!
  widget.someVariable = 3
  return widget
end

local function update(widget, options)
  -- Runs if options are changed from the Widget Settings menu
  widget.options = options
end

local function background(widget)
  -- Runs periodically only when widget is not visible
end

local function refresh(widget, event, touchState)
  -- Runs periodically only when widget is visible
  -- If fullscreen, then event is 0 or event value
  -- If not fullscreen, then event is nil
end

return {
  name = name,
  options = options,
  create = create,
  update = update,
  refresh = refresh,
  background = background
}
```

## Notes:

* The `name` must be max. 10 characters long.
* `Options` is only passed to `create` to be used during widget creation. Don't change them in Lua code, as this has no effect. But the options can be changed by the user in the Widget Settings menu, and then `update` will be called.
* Maximum five `options` are allowed, with names of max. 10 characters, and no spaces.
* If local variables are declared outside functions in the widget script, then they are shared between all instances of the widget.
* Therefore, local variables that are private for each instance should be added to the `widget` table in the `create` function.
* When the widget is in fullscreen mode, then `event` is either 0, a [key event value](../part_iii_-_opentx_lua_api_reference/constants/key_events.md), or a [touch event value](../part_iii_-_opentx_lua_api_reference/constants/touch-event-constants.md).
* If `event` is a [touch event value](../part_iii_-_opentx_lua_api_reference/constants/touch-event-constants.md), then `touchState` is a table. Otherwise, it is `nil`.
* When the widget is not in fullscreen mode, then both `event` and `touchState` are `nil`.
* The size of the widget's screen area is as follows:
  * Fullscreen mode: `LCD_W` by `LCD_H`
  * Not fullscreen mode: `zone.w` by `zone.h` 



