# Widget Scripts

## Overview

Most of the time, widget scripts show some info in a _zone_ either in the _top bar_ or in one of the user defined _main views_, and they cannot receive direct input from the user via key events like e.g. Telemetry scripts.

But widgets on the main views can also be shown in _full screen mode_, where they take over the entire screen area. And here they receive user input via key events, and for radios with touch screen, also touch events. Full screen mode can be entered by selecting the widget, pressing ENTER and selecting **Full screen** on the widget menu, or by double tapping the widget on radios with a touch screen. Full screen mode can be exited by long pressing the RETURN button, or by calling the Lua function `lcd.exitFullScreen()`.

Each model can have up to five main views, with up to 8 widgets per screen, depending on their size and layout. Each instance of a widget has his own _options_ table.

**Please note:** Widget scripts are only available on radios with color screens, e.g. FrSky Horus models, Radiomaster TX16 and Jumper T16.

## Lifetime

All widget scripts on the SD card are loaded into memory when the model is selected; even widgets that are not used. This has the side effect that any global functions defined in a widget script will always be available to other widget scripts. It also means that any script on the SD card will consume part of the radio's memory - even if it is not being used. Therefore, it is important to either keep widget scripts small, or to use Lua's loadScript() function to load code dynamically.

They can be added to the top bar or a main view through the telemetry setup menu. When a widget has been added to a screen, then the widget functions are called as follows:

* `create` is called once when the widget instance is registered (started).
* `update` is called when widget settings are changed by the user.
* `background` is called periodically when the widget instance _is_ _not_ visible. **Note:** this is different from the way that telemetry scripts are handled.
* `refresh` is called periodically when the widget instance _is_ visible. **Note:** if you want `background` to run when the widget is visible, then call it from `refresh`.
* A widget script is stopped and disabled if it misbehaves (e.g. too long runtime, run-time error, or low memory)
* All widgets are stopped while a One-Time script is running (see [One-Time scripts](one-time\_scripts.md)).

## File Location

Widgets are located on the SD card, each in their specific folder /WIDGETS/<_name_>/main.lua (<_name_> must be in 8 characters or less).

## Interface

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `name` string
* `options` table
* `create` function
* `update` function
* `background` function (optional)
* `refresh` function

### Example

```lua
local name = "WidgetName"

-- Create a table with default options
-- Options can be changed by the user from the Widget Settings menu
-- Notice that each line is a table inside { }
local options = {
  { "Source", SOURCE, 1 },
  -- BOOL is actually not a boolean, but toggles between 0 and 1
  { "Boolean", BOOL, 1 },
  { "Value", VALUE, 1, 0, 10},
  { "Color", COLOR, ORANGE },
  { "Text", STRING, "Max8chrs" }
}

local function create(zone, options)
  -- Runs one time when the widget instance is registered
  -- Store zone and options in the widget table for later use
  local widget = {
    zone = zone,
    options = options
  }
  -- Add local variables to the widget table,
  -- unless you want to share with other instances!
  widget.someVariable = 3
  -- Return widget table to EdgeTX
  return widget
end

local function update(widget, options)
  -- Runs if options are changed from the Widget Settings menu
  widget.options = options
end

local function background(widget)
  -- Runs periodically only when widget instance is not visible
end

local function refresh(widget, event, touchState)
  -- Runs periodically only when widget instance is visible
  -- If full screen, then event is 0 or event value, otherwise nil
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

### Notes

* The `name` must be max. 10 characters long.
* `options` is passed to `create` and then stored in Lua. Changing it has no effect on EdgeTX.
* If `options` is changed by the user in the Widget Settings menu, then `update` will be called with a new `options` table, unaffected by any changes made by Lua code to the old `options` table.
* Maximum five `options` are allowed, with names of max. 10 characters, and no spaces. cf. [widget options constants](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/widget-options.md) for valid option types.&#x20;
* If local variables are declared outside functions in the widget script, then they are shared between all instances of the widget.
* Therefore, local variables that are private for each instance should be added to the `widget` table in the `create` function before returning the `widget` table to EdgeTX.
* When the widget is in full screen mode, then `event` is either 0, a [key event value](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/key\_events.md), or a [touch event value](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/touch-event-constants.md).
* If `event` is a [touch event value](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/touch-event-constants.md), then `touchState` is a table. Otherwise, it is `nil`.
* When the widget is not in full screen mode, then both `event` and `touchState` are `nil`.
* The size of the widget's screen area is as follows:
  * Full screen mode: `LCD_W` by `LCD_H`
  * Not full screen mode: `zone.w` by `zone.h` (updated if screen options are changed)
