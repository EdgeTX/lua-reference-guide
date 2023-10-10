# Telemetry Scripts

## Purpose

Although they are named "Telemetry scripts" in fact they can be used to perform constant task while running in background. Telemetry scripts are mostly used for building customized screens that are avalilable to user directly from main screen using key shortcut. Each model can have up to three active scripts as configured on the model's Telemetry configuration page. The same script can be assigned to multiple models.

{% hint style="warning" %}
Telemetry scripts are only available on radios with B\&W LCD screens, such as e.g. FrSky Taranis models (including Xlite), Radiomaster TX12, Zorro, Boxer or Jumper T12.\
Read more about <mark style="color:red;">\<radios></mark>.
{% endhint %}

## Execution & Lifetime

Telemetry script is loaded and executed when model is selected.\
\
Script executes until:

* it misbehaves (e.g. run-time error or low memory)
* [One-time Script](one-time-scripts.md) is running. When One-time script finishes execution, Wigdet Script resumes execution.

## File Location

Telemetry scripts are located on the SD card in the folder /SCRIPTS/TELEMETRY/.&#x20;

{% hint style="warning" %}
Telemetry script file name length (without extension) **must be 6 characters or less**&#x20;
{% endhint %}

## Interface

Every Telemetry script must include a `return` statement at the end, defining its interface to EdgeTX. \
This statement returns a table with the following fields:

<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>run</strong></td><td>function</td><td>true</td><td>Function is called periodicaly when when telemetry screen is visible. </td></tr></tbody></table>

_Parameters_

<table data-header-hidden><thead><tr><th width="145">Parameter</th><th>Decription</th></tr></thead><tbody><tr><td><strong>event</strong><br>number</td><td>Used to indicates which radio key has been pressed (see <a href="../part_iii_-_opentx_lua_api_reference/constants/key_events.md">Key Events</a>)</td></tr></tbody></table>

_Return values_\
_none_



<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>init</strong></td><td>function</td><td>false</td><td>This function is called once when script is executed</td></tr></tbody></table>

_Parameters_\
none

_Return Values_\
none



<table><thead><tr><th width="142.33333333333331">Field</th><th width="108">Type</th><th width="105" data-type="checkbox">Required</th><th>Desctiption</th></tr></thead><tbody><tr><td><strong>background</strong></td><td>function</td><td>false</td><td>This function is called periodically, both when the telemetry screen is visible and when it is not</td></tr></tbody></table>

_Parameters_\
none

_Return Values_\
none

### Examples

```lua
local function my_init()
  -- init is called once when model is loaded
end

local function my_background()
  -- background is called periodically
end

local function my_run(event)
  -- run is called periodically only when screen is visible
end

return { run = my_run, background = my_background, init = my_init }
```

