# Function Scripts

## Overview

Function scripts are invoked via the **'Lua Script'** option of Special Functions configuration page.

## Typical uses

* specialized handling in response to switch position changes
* customized announcements

## Limitations

* all function scripts are stopped if a One-Time Lua script is running
* Function scripts **DO NOT HAVE ACCESS TO LCD DISPLAY**

## Location

Place them on SD card in folder /SCRIPTS/FUNCTIONS/

## Lifetime

* `init` function is called once when model is selected
* depending on the switch associated with the Special Function, either the `run` function \(switch = on\) or the `background` function \(switch = off\) is called periodically
* the script is stopped and disabled if it misbehaves \(e.g. run-time error or low memory\)

## Script interface definition

Every script must include a _return_ statement at the end, that defines its interface to the rest of OpenTX code. This statement defines:

* `init` function \(optional\)
* `run` function
* `background` function \(optional\)

## Example \(interface only\):

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

