# One-Time Scripts

_**WARNING -**_ **Running a One-Time script will suspend execution of all other currently loaded Lua scripts \(Custom, Telemetry, and Functions\)**

## Overview

One-Time scripts start when called upon by a specific radio function or when the user selects them from a contextual menu. They do their task and are then terminated and unloaded. Please note that all persistent scripts are halted during the execution of One-Time scripts. They are automatically restarted once the One-Time script is finished. This is done to provide enough system resources to execute the one time script.

## Lifetime

Script is executed when user selects Execute on a script file from SD card browser screen.

Script executes until:

* it returns value different from 0
* is forcefully closed by user by long press of EXIT key
* is forcefully closed by system if if it misbehaves \(e.g. run-time error or low

  memory\)

## File Location

Place them anywhere on SD card, the folder /SCRIPTS/ is recommended. The only exception is official model wizard script, that should be put into /SCRIPTS/WIZARD/ folder that way it will start automatically when new model is created.

## **Interface**

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `init` function \(optional\)
* `run` function

### Example

```lua
local function init()
  -- init is called once when model is loaded
end

local function run(event)
  -- run is called periodically only when screen is visible
  -- A non-zero return value will halt the script
  return x
end

return { run=run, init=init }
```

### Notes:

* The `event` parameter indicates which transmitter key has been pressed \(see [Key Events](../part_iii_-_opentx_lua_api_reference/constants/key_events.md)\). 
* A non-zero return value from `run` will halt the script.

