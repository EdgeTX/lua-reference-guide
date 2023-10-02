# Custom (Mixer) Scripts

{% hint style="warning" %}
## <mark style="color:red;">Do not use Lua Custom (Mixer) Scripts for controlling any aspect of your model that could cause a crash if the script stops executing!</mark>
{% endhint %}

## Overview

Each model can have several Custom Scripts associated with it, and these scripts are run periodically. They behave similarly to standard EdgeTX mixers, but at the same time they provide a much more flexible and powerful tool. Custom Scripts take one or more values as inputs, do some processing in Lua code, and output one or more values.

{% hint style="danger" %}
To enable Custom (Mixer) Scripts, firmware must be compiled with the option `LUA_MIXER=Y`.
{% endhint %}

{% hint style="info" %}
Custom Scripts should be as short as possible, to avoid delays. It is also important to keep in mind that other loaded Telemetry and Function scripts can add to the response time, or worse: hang the system!
{% endhint %}

### Typical uses

* replacement for complex mixes that are _not critical_ to model function
* complex processing of inputs and reaction to their current state and/or their history
* filtering of telemetry values

### Limitations

* cannot update LCD screen or perform user input.
* should not exceed allowed run-time/ number of instructions.
* custom scripts are run with less priority than built-in mixes. Their execution period is around 30ms and is not guaranteed!
* can be disabled/killed anytime due to logic errors in script, not enough free memory, etc...)

## Lifetime

* Custom scripts are loaded from SD card when model is selected
* `init` \_\_function is called first
* `run` function is called periodically (about 30 times per second)
* the script is killed (stopped and disabled) if it misbehaves (e.g. run-time error or low memory)
* all Custom scripts are stopped while a One-Time script is running (see Lua One-time scripts)

### Disabled script

If the script output is used as a `mixer source` , and the script is killed for whatever reason, then _the whole mixer line is disabled_ ! This can be used for example to provide a fallback in case Lua Custom script is killed.

Example where Lua mix script is used to drive ailerons in some clever way, but control falls back to the standard aileron mix if script is killed. Second mixer line replaces the first one when the script is alive:

```
CH1  [I4]Ail Weight(+100%)
  := LUA4b Weight(+100%)
```

## File Location

Place them on SD card in folder /SCRIPTS/MIXES/

{% hint style="warning" %}
File name length (without extension) **must be 6 characters or less**
{% endhint %}

## Interface

Every Custom Script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `run` function&#x20;
* `init` function _(optional)_
* `input` table _(optional)_
* `output` table _(optional)_





### Example

```lua
local input =
  {
    { "Strength", SOURCE},           -- user selects source (typically slider or knob)
    { "Interval", VALUE, 0, 100, 0 } -- interval value, default = 0.
  }

local output = { "Val1", "Val2" }

local function init()
  -- Called once when the script is loaded
end

local function run(Strength, Interval) -- Must match input table
  local v1, v2
  -- Called periodically
  return v1, v2                        -- Must match output table
end

return { input=input, output=output, run=run, init=init }
```

#### Input table

The input table defines what values are available as input(s) to custom scripts. There are two forms of input table entries.

```
{ "<name>", SOURCE }
```

SOURCE inputs provide the current value of a selected OpenTX variable. The source must be selected by the user when the script is configured. Source can be any value that EdgeTX knows about (inputs, channels, telemetry values, switches, custom functions etc.).\
**Note:** the typical input range is -1024 thru +1024. Simply divide the input value by 10.24 to convert to a percentage from -100% to +100%.

```
{ "<name>", VALUE, <min>, <max>, <default> }
```

VALUE inputs provide a constant value that is set by the user when the script is configured.

* _name_ - maximum length of 8 characters
* _min_ - minimum value of -128
* _max_ - maximum value of 127
* _default_ - must be within the valid range specified
* **Maximum of 6 inputs per script** (was 8 in 2.1)

#### Output table

The output table defines only name(s), as the actual values are returned by the script's run function.

```lua
{ "<name1>", "<name2>" }
```

**Note:** the above names are only visible as source values on the radio screen when the script is running. If the model is edited in Companion, then the values show as `LUA1a` and `LUA1b` etc.
