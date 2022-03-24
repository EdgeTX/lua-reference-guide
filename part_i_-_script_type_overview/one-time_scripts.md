# One-Time Scripts

_**WARNING -**_ **Running a One-Time script will suspend execution of all other currently loaded Lua scripts (Custom, Telemetry, and Functions)**

## Overview

One-Time scripts start when called upon by a specific radio function or when the user selects them from a contextual menu. They do their task and are then terminated and unloaded. Please note that all persistent scripts are halted during the execution of One-Time scripts. They are automatically restarted once the One-Time script is finished. This is done to provide enough system resources to execute the One-Time script.

## Lifetime

Script is executed when user selects Execute on a script file from SD card browser screen, or opens a Lua Tool, or creates a new model with a Wizard script.

The script executes until:

* it returns value different from 0
* is forcefully closed by user by long press of EXIT key
*   is forcefully closed by system if it misbehaves (e.g. run-time error or low

    memory)

## File Location

General One-Time scripts can be placed anywhere on SD card, however, the folder /SCRIPTS/ is recommended.&#x20;

Tool scripts must be stored in /SCRIPTS/TOOLS.

Wizard scripts must be stored in the same subfolder of /TEMPLATES/ with the same "first name" as the template file using it. Some Wizard scripts are just small scripts that load one of the common scripts located in /SCRIPTS/WIZARD/.

## **Interface**

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `init` function (optional)
* `run` function

### Example

```lua
local function init()
  -- init is called once when model is loaded
end

local function run(event, touchState)
  -- run is called periodically only when screen is visible
  -- A non-zero return value will halt the script
  return x
end

return { run=run, init=init }
```

### Notes:

* The `event` parameter indicates which transmitter key has been pressed (see [Key Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/key\_events.md)).
* The `touchState` value is only present when `event` is a touch event (see [Touch State Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/touch-event-constants.md)).
* A non-zero return value from `run` will halt the script. If the return value is a text string with the file path to a new Lua script, then the new script will be loaded and run.
