# Widget Scripts

## Purpose

Widget scripts are available on radios equipped with color LCD. They are designed to run constantly in the background performing various tasks. Widget scripts are mostly used to extend EdgeTX functionality via _Widgets_ that are placed by the user on _Main Views_. They are the equivalent of Telemetry Scripts on radios equipped with B&W LCD.

Most of the time, widget scripts show some info in a _Widget's zone_ in one of the user defined _Main Views_. They cannot receive direct input from the user via key events with exception of being displayed in so called _Full Screen mode_. Full screen mode can be entered by selecting the widget, pressing ENTER and selecting **Full screen** from the widget's contextual menu, ~~or by double tapping the widget on radios with a touch screen~~. Full screen mode can be exited by long pressing the EXIT (RTN) button, or by calling the Lua function `lcd.exitFullScreen()`.

Each model can have up to nine Main Views, with up to 8 widgets per screen, depending on their size and layout. Each instance of a widget has its own _options_ table.

!!! warning
    Widget scripts are only available on radios with color LCD screens, such as e.g. FrSky X10 or X12, Radiomaster TX16S, Jumper T16 or T18, Flysky NV14, etc.<br>
    Read more about [supported radios](../../radios/README.md).

## Execution & Lifetime

All widget scripts on the SD card are loaded into memory when the model is selected, even widgets that are not used. This has the side effect that any global functions defined in a widget script will always be available to other widget scripts. It also means that any Widget Script placed in the proper location on the SD card will consume part of the radio's memory - even if it is not being used.

!!! warning
    It is important to either keep Widget Scripts small, or to use Lua's [loadScript()](../../api-reference/lua-scripts/load-script.md) function to load code dynamically

Script executes until:

* it misbehaves (e.g. too long runtime, run-time error, or low memory)
* a One-Time script is running. When the One-Time script finishes execution, the Widget Script resumes execution.

## File Location

Widget scripts are located on the SD card, each one in their specific folder:<br>
`/WIDGETS/<folder name>/`

!!! warning
    Widget script folder name length **must be 8 characters or less**

Widget script name is constant and has to be named **main.lua**

!!! info
    Example of proper Widget script placement to be registered by EdgeTX as a valid Widget script available to the user in the Widgets selection menu:<br>
    `/WIDGETS/MYWGT/main.lua`

!!! info
    Try to use a unique folder name. In case of a naming clash, the previously installed widget will be overwritten.

## Interface

Every Widget Script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **name** | string | true | This variable holds a name that is displayed to the user as the Widget script's name in the available Widgets list. |

!!! warning
    The `name` length must be 10 **characters or less**.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **options** | table | false | Options table is used to store the Widget's options available to the EdgeTX user via the Widget's Settings menu.<br>To see valid options read [Widget Options Constants](../constants/widget-options.md). |

!!! info
    `options` table is passed to `create` function when invoked and then stored in Lua. Changing options table values while the Widget script is running has no effect. This table is designed to be changed via EdgeTX system menus.

!!! info
    If `options` is changed by the user in the Widget Settings menu, then `update` will be called with a new `options` table, unaffected by any changes made by Lua code to the old `options` table.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **create** | function | true | Function is called once when the widget instance is registered (started). |

_Parameters_

| Parameter | Description |
| --- | --- |
| **zone**<br>table | This parameter will hold visible dimensions of Widget (height & width) |
| **options**<br>table | Initial options table as described above |

_Return values_

| Returns | Description |
| --- | --- |
| **widget**<br>table | Create function will return a table that has to be later passed to `update`, `background`, and `refresh` functions, allowing access to the widget's unique variables. |

!!! info
    The size of the widget's zone area is as follows:

    * Full screen mode: `LCD_W` by `LCD_H`
    * Not full screen mode: `zone.w` by `zone.h` (updated if screen options are changed)

!!! info
    If local variables are declared outside functions in the widget script, then they are shared between all instances of the widget. Therefore, local variables that are private for each instance should be added to the `widget` table in the `create` function before returning the `widget` table to EdgeTX.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **update** | function | false | This function is called when the Widget's Settings are changed by the user. It is mostly used to modify Widget Script variables or behaviour based on the options values entered by the user. |

_Parameters_

| Parameter | Description |
| --- | --- |
| **widget**<br>table | Widget's table returned by the `create` function, described above. |
| **options**<br>table | Initial options table as described above |

_Return values_<br>
_none_

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **background** | function | false | This function is called periodically when the widget instance is NOT VISIBLE. |

_Parameters_

| Parameter | Description |
| --- | --- |
| **widget**<br>table | Widget's table returned by the `create` function, described above. |

_Return values_<br>
_none_

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| **refresh** | function | true | This function is called periodically when the widget instance IS VISIBLE. |

_Parameters_

| Parameter | Description |
| --- | --- |
| **widget**<br>table | Widget's table returned by the `create` function, described above. |
| **event**<br>number | <ul><li>When the Widget Script is in full screen mode, then `event` is either 0, a [key event value](../constants/key-event-constants.md), or a [touch event value](../constants/touch-event-constants.md).</li><li>When the widget is not in full screen mode, then `event` is `nil`</li></ul>See [Key Events](../constants/key-event-constants.md). |
| **touchState**<br>table | This parameter is only present when the radio is equipped with a touch interface and `event` is a touch event.<br><ul><li>If `event` is a [touch event value](../constants/touch-event-constants.md), then `touchState` is a table. Otherwise, it is `nil`.</li><li>When the widget is not in full screen mode then `touchState` is `nil`</li></ul>See [Touch State Events](../constants/touch-event-constants.md). |

_Return values_<br>
_none_

!!! info
    if you want the `background` function to run when the widget is visible, then call it from the `refresh` function.

### Examples

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
