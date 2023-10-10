# One-Time Scripts

## Overview

One-Time scripts start when called upon by a specific radio function or when the user selects them from a contextual menu. They do their task and are then terminated (by user or function) and unloaded.&#x20;

{% hint style="danger" %}
<mark style="color:red;">**Running a One-Time script will suspend execution of all other currently loaded Lua scripts (Custom, Telemetry, and Functions). They are automatically restarted once the One-Time script is finished. This is done to provide enough system resources to execute the One-Time script.**</mark>
{% endhint %}

## Execution & Lifetime

Script is executed when user selects Execute on a script file from SD card browser screen, or opens a Lua Tool, or creates a new model with a Wizard script.

The script executes until:

* it returns value different from 0 (except returning string that contains new script name to be executed)
* is forcefully closed by user by long press of EXIT key
*   is forcefully closed by system if it misbehaves (e.g. run-time error or low

    memory)

## File Location

One-Time Scripts can be placed anywhere on SD card, however, the folder /SCRIPTS/ is recommended.

{% hint style="info" %}
If One-Time Script is placed in special folder /SCRIPTS/TOOLS it will be visible in EdgeTX RADIO>TOOLS tab\
\
To give this One-Time Script unique name place at the beginning of lua script line: \
`-- toolName = "TNS|ScriptName|TNE`

Otherwise script's filename will be used to display in RADIO>TOOLS list.
{% endhint %}

{% hint style="info" %}
Wizard scripts must be stored in the same subfolder of /TEMPLATES/ with the same "first name" as the template file using it. Some Wizard scripts are just small scripts that load one of the common scripts located in /SCRIPTS/WIZARD/.
{% endhint %}

## **Interface**

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

*   `run` (function) obilgatory\
    this function is called periodicaly when sccript is running\
    \
    **Parameter**

    \
    `event` (number)\
    This parameter is used to indicates which radio key has been pressed (see [Key Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/key\_events.md)).

    \
    `touchState` (table) \
    This parameter is only present when radio is equiped with touch interface and `event` is a touch event (see [Touch State Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/touch-event-constants.md)).\


    **Return value**

    \
    `exit` (multi type)&#x20;

    1. if `exit` value is 0 (zero) script will continue to run&#x20;
    2. if `exit` value is non-zero script will be halted.&#x20;
    3. If `exit` value is a text string with the file path to a new Lua script, then the new script will be loaded and run.\

*   `init` (function) _optional_ \
    this function is called once when script is executed.\
    \
    **Parameters**

    none\
    \
    **Return Value**\
    none

## Examples

Simplest one-time LUA script

```lua
local function run(event, touchState)
  print("Script run executed")
  return 0
end

return { run=run }
```

{% hint style="info" %}
Because 0 is returned all the time this script will continue running until user long press EXIT (RTN) key.&#x20;
{% endhint %}

One-Time LUA script with initialization and exit feature if user short press and release EXIT (RTN) key&#x20;

```lua
local exit = 0

local function run(event, touchState)
  print("Script run function executed")
  -- code to execute
  if event == EVT_VIRTUAL_EXIT then 
    exit = 1
  end 
  return exit
end

local function init()
  print("Script init function executed")
  -- code to execute
end

return { run=run, init=init }
```
