# Widget Scripts

## Purpose

Widget scripts are avaiable on radios equiped with color LCD. They are designed to run constantly in the background performinfg various task. Widget scripts are mostly used to extend EdgeTX functionality via _<mark style="color:purple;">Widgets</mark>_ that are places by user on _<mark style="color:purple;">Main Views</mark>_. They are equivalent of Telemetry Scripts on radios equiped with B\&W LCD.&#x20;

Most of the time, widget scripts show some info in a _<mark style="color:purple;">Widget's zone</mark>_ in one of the user defined _<mark style="color:purple;">Main Views.</mark>_ They cannot receive direct input from the user via key events with exeption of being displayed in so called _<mark style="color:purple;">Full Screen mode</mark>_. Full screen mode can be entered by selecting the widget, pressing ENTER and selecting **Full screen** from the widget's contextual menu, ~~or by double tapping the widget on radios with a touch screen~~. Full screen mode can be exited by long pressing the EXIT (RTN) button, or by calling the Lua function `lcd.exitFullScreen()`.

Each model can have up to nine Main Views, with up to 8 widgets per screen, depending on their size and layout. Each instance of a widget has his own _options_ table.

{% hint style="warning" %}
Widget scripts are only available on radios with color LCD screens, such as e.g. FrSky X10 or X12, Radiomaster TX16S, Jumper T16 or T18, Flysky NV14., etc.\
Read more about _<mark style="color:purple;">radios</mark>_.
{% endhint %}

## Execution & Lifetime

All widget scripts on the SD card are loaded into memory when the model is selected, even widgets that are not used. This has the side effect that any global functions defined in a widget script will always be available to other widget scripts. It also means that any Widget Script placed in proper location on the SD card will consume part of the radio's memory - even if it is not being used.&#x20;

{% hint style="warning" %}
&#x20;It is important to either keep Widget Scripts small, or to use Lua's [loadScript()](../../lua-api-reference/lua-scripts/loadscript.md) function to load code dynamically
{% endhint %}

Script executes until:

* it misbehaves (e.g. too long runtime, run-time error, or low memory)
* One-Time script is running. When One-time script finishes execution, Wigdet Script resumes execution.

## File Location

Widget scripts are located on the SD card, each one in their specific folder: \
/WIDGETS/\<folder _name_>/

{% hint style="warning" %}
Widget script folder name length **must be 8 characters or less**&#x20;
{% endhint %}

Widget script name is constant and has to be named **main.lua**

{% hint style="info" %}
Example of proper Widget script placement to be registered by EdgeTX as valid Widget script available to user in Widgets selection menu:\
/WIDGETS/MYWGT/main.lua&#x20;
{% endhint %}

{% hint style="info" %}
Try to use unique folder name as in case of naming clash previously installed widget will be overwrtitten. &#x20;
{% endhint %}

## Interface

Every Widget Script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>name</strong></td><td>string</td><td>true</td><td>This variable holds a name that is displayed to user as Widget scripts name in available Widgets list.</td></tr></tbody></table>

{% hint style="warning" %}
The `name` length must be 10 **characters or less**.
{% endhint %}





<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>options</strong></td><td>table</td><td>false</td><td>Options table is to store Widget's options available to EdgeTX user via Widget's Settings menu. <br>To see valid options read <a href="../../lua-api-reference/constants/widget-options.md">Widget Options Constants</a>.</td></tr></tbody></table>

{% hint style="info" %}
`options` table is passed to `create` function when invoked and then stored in Lua. Changing options table values while Widget script is running has no effect. This table is designed to be changed with EdgeTX system menus.
{% endhint %}

{% hint style="info" %}
If `options` is changed by the user in the Widget Settings menu, then `update` will be called with a new `options` table, unaffected by any changes made by Lua code to the old `options` table.
{% endhint %}





<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>create</strong></td><td>function</td><td>true</td><td>function is called once when the widget instance is registered (started).</td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>zone</strong><br>table</td><td>This parameter will hold visible dimensions of Widget (height &#x26; width)</td></tr><tr><td><strong>options</strong><br>table</td><td>Initial options table as described above</td></tr></tbody></table>

_Return values_

<table data-header-hidden><thead><tr><th width="140.33333333333331">Returns</th><th>Description</th></tr></thead><tbody><tr><td><strong>widget</strong><br>table</td><td>Create function will return table that has to be later passed to <code>update</code> ,  <code>background</code> &#x26; <code>refresh</code>  functions allowing to access widget's unique variables </td></tr></tbody></table>

{% hint style="info" %}
The size of the widget's zone area is as follows:

* Full screen mode: `LCD_W` by `LCD_H`
* Not full screen mode: `zone.w` by `zone.h` (updated if screen options are changed)
{% endhint %}

{% hint style="info" %}
If local variables are declared outside functions in the widget script, then they are shared between all instances of the widget. Therefore, local variables that are private for each instance should be added to the `widget` table in the `create` function before returning the `widget` table to EdgeTX.
{% endhint %}





<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>update</strong></td><td>function</td><td>false</td><td>This function is called when Widget's Settings are changed by the user. It is mostly used to modify Widget Script variables or behaviour basing on options values entered by user.</td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>widget</strong><br>table</td><td>Widget's table returned by <code>create</code> function, decribed above.</td></tr><tr><td><strong>options</strong><br>table</td><td>Initial options table as described above</td></tr></tbody></table>

_Return values_\
_none_





<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>background</strong></td><td>function</td><td>false</td><td>This function is called periodically when the widget instance is NOT VISIBLE.</td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>widget</strong><br>table</td><td>Widget's table returned by <code>create</code> function, decribed above.</td></tr></tbody></table>

_Return values_\
_none_





<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>refresh</strong></td><td>function</td><td>true</td><td>This function is called periodically when the widget instance IS VISIBLE.  </td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>widget</strong><br>table</td><td>Widget's table returned by <code>create</code> function, decribed above.</td></tr><tr><td><strong>event</strong><br>number</td><td><ul><li>When Widget Script is in full screen mode, then <code>event</code> is either 0, a <a href="../../lua-api-reference/constants/key-event-constants.md">key event value</a>, or a <a href="../../lua-api-reference/constants/touch-event-constants.md">touch event value</a>.</li><li>When the widget is not in full screen mode, then <code>event</code> is <code>nil</code></li></ul><p>See <a href="../../lua-api-reference/constants/key-event-constants.md">Key Events</a>.</p></td></tr><tr><td><strong>touchState</strong><br>table</td><td><p>This parameter is only present when radio is equiped with touch interface and <code>event</code> is a touch event.<br></p><ul><li>If <code>event</code> is a <a href="../../lua-api-reference/constants/touch-event-constants.md">touch event value</a>, then <code>touchState</code> is a table. Otherwise, it is <code>nil</code>.</li><li>When the widget is not in full screen mode then <code>touchState</code> is <code>nil</code></li></ul><p><br>See <a href="../part_iii_-_opentx_lua_api_reference/constants/touch-event-constants.md">Touch State Events</a>.</p></td></tr></tbody></table>

_Return values_\
_none_

{% hint style="info" %}
if you want `background` function to run when the widget is visible, then call it from `refresh function.`
{% endhint %}



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
