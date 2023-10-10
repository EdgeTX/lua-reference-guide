# One-Time Scripts

## Purpose

One-Time scripts start when called upon by a specific radio function or when the user selects script browsing SD Card and then selects "Execute" from a contextual menu. They do their task and are then terminated (by user or function) and unloaded.

## Execution & Lifetime

Script is executed when user selects "Execute" on a script file from SD card browser screen, or opens a Lua Tool, or creates a new model with a Wizard script.

The script executes until:

* it returns value different from 0 (except returning string that contains new script name to be executed)
* is forcefully closed by user by long press of EXIT key
*   is forcefully closed by system if it misbehaves (e.g. run-time error or low

    memory)

{% hint style="danger" %}
<mark style="color:red;">**Running a One-Time script will suspend execution of all other currently loaded Lua scripts (Custom, Telemetry, and Functions). They are automatically restarted once the One-Time script is finished. This is done to provide enough system resources to execute the One-Time script.**</mark>
{% endhint %}

## File Location

One-Time Scripts can be placed anywhere on SD card, however, the folder /SCRIPTS/ is recommended.

{% hint style="info" %}
If One-Time Script is placed in special folder /SCRIPTS/TOOLS it will be visible in EdgeTX RADIO>TOOLS tab\
\
To give this One-Time Script unique name place at the beginning of lua script line:\
`-- toolName = "TNS|ScriptName|TNE`

Otherwise script's filename will be used to display in RADIO>TOOLS list.
{% endhint %}

{% hint style="info" %}
Wizard scripts must be stored in the same subfolder of /TEMPLATES/ with the same "first name" as the template file using it. Some Wizard scripts are just small scripts that load one of the common scripts located in /SCRIPTS/WIZARD/.
{% endhint %}

## **Interface**

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>run</strong></td><td>function</td><td>true</td><td>Function is called periodicaly when script is running. </td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>event</strong><br>number</td><td>Used to indicates which radio key has been pressed (see <a href="../part_iii_-_opentx_lua_api_reference/constants/key_events.md">Key Events</a>)</td></tr><tr><td><strong>touchState</strong><br>table</td><td>This parameter is only present when radio is equiped with touch interface and <code>event</code> is a touch event (see <a href="../part_iii_-_opentx_lua_api_reference/constants/touch-event-constants.md">Touch State Events</a>).</td></tr></tbody></table>

_Return values_

<table data-header-hidden><thead><tr><th width="140.33333333333331">Returns</th><th>Description</th></tr></thead><tbody><tr><td><strong>exit</strong><br>multi type</td><td><ul><li>if <code>exit</code> value is 0 (zero) script will continue to run</li></ul><ul><li>if <code>exit</code> value is non-zero script will be halted.</li></ul><ul><li>If <code>exit</code> value is a text string with the file path to a new Lua script, then the new script will be loaded and run.</li></ul></td></tr></tbody></table>



<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>init</strong></td><td>function</td><td>false</td><td>This function is called once when script is executed</td></tr></tbody></table>

_Parameters_\
none

_Return Values_\
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
Because 0 is returned all the time this script will continue running until user long press EXIT (RTN) key.
{% endhint %}

***

One-Time LUA script with initialization and exit feature if user short press and release EXIT (RTN) key

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
