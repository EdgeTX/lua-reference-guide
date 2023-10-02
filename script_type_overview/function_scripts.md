# Function Scripts

## Overview

Function scripts are invoked via the **'Lua Script'** option of Special Functions configuration page.

Typical uses of Function scripts are:

* specialized handling in response to switch position changes
* customized announcements

Please be aware that:

* all function scripts are stopped if a One-Time Lua script is running
* Function scripts **DO NOT HAVE ACCESS TO LCD DISPLAY**

## Lifetime

* `init` function is called once when the model is selected
* depending on the switch associated with the Special Function, either the `run` function \(switch = on\) or the `background` function \(switch = off\) is called periodically
* the script is stopped and disabled if it misbehaves \(e.g. run-time error or low memory\)

## File Location

Scripts are located on the SD card in the folder /SCRIPTS/FUNCTIONS/&lt;_name_&gt;.lua. File name length \(without extension\) **must be 6 characters or less** \(this limit was 8 characters in OpenTX 2.1\).

## Interface

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `init` function \(optional\)
* `run` function
* `background` function \(optional\)

### Example

```lua
local function init()
  -- Called once when the script is loaded
end

local function run()
  -- Called periodically while the Special Function switch is on
end

local function background()
  -- Called periodically while the Special Function switch is off
end

return { run=run, background=background, init=init }
```

