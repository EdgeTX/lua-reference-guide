# Telemetry Scripts

## Telemetry Scripts

## General description

Telemetry scripts are used for building customized screens. Each model can have up to three active scripts as configured on the model's telemetry configuration page. The same script can be assigned to multiple models.

## File Location

Scripts are located on the SD card in the folder /SCRIPTS/TELEMETRY/&lt;_name_&gt;.lua. File name length \(without extension\) **must be 6 characters or less** \(this limit was 8 characters in OpenTX 2.1\).

## Lifetime of telemetry script

* Telemetry scripts are loaded when the model is selected.
* `init` function is called one time when the script is loaded
* `background` function is periodically; both when the telemetry screen is visible and when it is not. 
* `run` function is called periodically only when the telemetry screen is visible
* script is stopped and disabled if it misbehaves \(e.g. run-time error or low memory\)
* all telemetry scripts are stopped if a one-time script is running \(see One-time scripts\)

## Script interface definition

Every script must include a return statement at the end, that defines its interface to the rest of OpenTX code. This statement defines:

* `init` function \(optional\)
* `background` function \(optional\)
* `run` function

### Example:

```lua
local function init()
  -- init is called once when model is loaded
end

local function background()
  -- background is called periodically
end

local function run(event)
  -- run is called periodically only when screen is visible
end

return { run=run, background=background, init=init }
```

### Notes:

* The `event` parameter indicates which transmitter key has been pressed \(see [Key Events](../part_iii_-_opentx_lua_api_reference/constants/key_events.md)\). 



