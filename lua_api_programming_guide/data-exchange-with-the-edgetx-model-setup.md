---
description: >-
  An EdgeTX model has several data components that can be exchanged with Lua
  scripts. This section gives an overview.
---

# Data Exchange with the EdgeTX Model Setup

In general terms, there are two different types of data that can be exchanged with EdgeTX:

* Values, which generally fall on a scale between -1024 and 1024, also sometimes reported as -100% to 100%, e.g. for mixer values and channel outputs.
* Switches, which are either `true` or `false.`

A specific data source type, e.g. Global Variables, can be indexed directly with an index that starts with 0 for the first one. This can be a little confusing, as e.g. GV1 for FM0 is read with [`model.getGlobalVariable(0, 0)`](../part\_iii\_-\_opentx\_lua\_api\_reference/model-functions-less-than-greater-than-luadoc-begin-model/getglobalvariable.md), because GV1 is the first global variable, and FM0 is the first flight mode. But as long as you remember that all direct indices start with 0 for the first one, you should be fine!

Global Variables is a _value_ data source that can return a value between -1024 and 1024. Examples of value sources are:

* Global Variables
* Sticks, sliders and knobs
* Trim values
* Input lines
* Channel outputs
* Trainer channel inputs
* Telemetry sensors

There is a way to access a value of _any_ such type with a _meta-index_. You use the function [`getFieldInfo(name)`](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getfieldinfo.md) where `name` can be any of the valid source names listed [here](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getfieldinfo.md). It returns a table with a description of the value source, including the field `id,` which is the meta-index.

You can use `id` with the function [`getValue(id)`](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getvalue.md) to read the current value. You can also use `name` directly, but this is less efficient, as EdgeTX does a linear search for the name every time it is called. Therefore, the procedure of first extracting the meta-index from `getFieldInfo(name).id`, and then using that, is recommended.

For switches, [`getLogicalSwitchValue(index)`](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getlogicalswitchvalue-id.md) uses a direct index to read this specific type of switch sources, again using the `index` 0 for LS1 etc. But there are also several types of switch sources, such as:

* Logical switches
* Switch positions, testing if a physical switch is in a particular position, e.g. `SA↑`.&#x20;
* Trim buttons
* Transmitter and telemetry activity

You can find the meta-index of a particular switch source with [`getSwitchIndex(name)`](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getswitchindex-positionname.md), where `name` is exactly the name that you see in the radio menus where you can select a switch source.

You can read the current value of a switch source with [`getSwitchValue(index)`](../part\_iii\_-\_opentx\_lua\_api\_reference/general-functions-less-than-greater-than-luadoc-begin-general/getswitchvalue-switchindex.md) as a `true`/`false` value.

It can be very confusing that some source can be read both as a value and as a switch. As an example, elevator trim can be read as the current value of the _trim_:&#x20;

```lua
local id = getFieldInfo("trim-ele")
local eleTrim = getValue(id)
```

Or it can be read as the current value of the _trim button position_:

```lua
local idUp = getSwitchIndex(CHAR_TRIM .. "Eu")
local idDown = getSwitchIndex(CHAR_TRIM .. "Ed")
local eleUp = getSwitchValue(idUp)
local eleDown = getSwitchValue(idDown)
```

These are really two different things, as the elevator _trim_ is an internal value stored by the radio, which is changed with the trim button, and the button is a physical button.

But it can also be a more direct comparison, e.g. the 3-position switch B, which can be read as a _value_ source with:

```lua
local idB = getFieldInfo("sb")
local swBvalue = getValue(idB) -- a value of -1024, 0 or 1024
```

Or the current position of switch B can be read with:

```lua
local idBup = getSwitchIndex("SB" .. CHAR_UP)
local idBdown = getSwitchIndex("SB" .. CHAR_DOWN)
local swBup = getSwitchValue(idBup)
local swBdown = getSwitchValue(idBdown)
```

Hopefully, these examples illustrated the differences between _values_ and _switches_, and showed how these can be retrieved in a Lua script.

You can also send data the other way: from Lua to the EdgeTX model setup.

To send a _value_, use a global variable: `model.setGlobalVariable(index, fm, value)`. If you use the default GV setting, where all other flight modes use the value of FM0, then you can use 0 for `fm`.

To send a _switch_, setup a `STICKY` type logical switch, and then use `setStickySwitch(index, true/false)`.&#x20;

The following table gives an overview of the Lua API functions that can be used to exchange data with the EdgeTX model setup.

| Function                                             | Description                                                                                                                                                                           |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `getFieldInfo(name)`                                 | Gets the meta-index of a _value_ source with `name`.                                                                                                                                  |
| `getValue(index)`                                    | Gets the current value of a source, where `index` is from the above.                                                                                                                  |
| `getFlightMode()`                                    | Returns the current flight mode number and name.  **Do not** confuse with `model.getFlightMode`, which is a completely different function!                                            |
| `model.getGlobalVariable( index, fm)`                | Read the value of a global variable between -1024 and 1024. You can use the above to get the current flioght mode for `fm`, or you can setup the GV to always use the value from FM0. |
| `model.setGlobalVariable( index, fm, value)`         | Sets the value of a global variable.                                                                                                                                                  |
| `setTelemetryValue(id, subID, instance, value, ...)` | This function can send data from Lua to a telemetry sensor. If it is running, then the sensor will show up with Discover Sensors. This can be used to log values generated by Lua.    |
| `getLogicalSwitchValue( index)`                      | Get the value of a logical switch.                                                                                                                                                    |
| `setStickySwitch(id, value)`                         | Set the value of a `STICKY` type logical switch.                                                                                                                                      |
| `getSwitchIndex(name)`                               | Get the meta-index of a switch source with `name`.                                                                                                                                    |
| `getSwitchName(index)`                               | Get the name of a switch source.                                                                                                                                                      |
| `getSwitchValue(index)`                              | Get the value of a switch source.                                                                                                                                                     |
| `getPhysicalSwitches()`                              | Get a list of physical switches on the radio. Can be used to make a selection list.                                                                                                   |
| `getShmVar(index)`                                   | Get the value of a shared memory variable. These are little "mail boxes" provided as a way to send data between Lua widgets and other Lua scripts like Mixer and Function scripts.    |
| `setShmVar(index, value)`                            | Set the value of a shared memory variable.                                                                                                                                            |
| `model.setTimer(timer, value)`                       | Set the timer to `value`.                                                                                                                                                             |
| `model.getTimer(timer)`                              | Read the timer.                                                                                                                                                                       |

