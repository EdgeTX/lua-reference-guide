# Mixes Scripts

{% hint style="warning" %}
### <mark style="color:red;">Don't use Lua Mixes Scripts for controlling any aspect of your model that could cause a crash if the script stops executing!</mark>
{% endhint %}

## Purpose

Mixes Scripts take one or more values as inputs, do some processing in Lua code, and output one or more values. Each model can have several Mixes Scripts associated with it, and these scripts are run periodically. They behave similarly to standard EdgeTX mixers, but at the same time they provide a much more flexible and powerful tool.&#x20;

Typical use cases:

* replacement for complex mixes that are _not critical_ to model function
* complex processing of inputs and reaction to their current state and/or their history
* filtering of telemetry values

## Execution & Lifetime

Mixes script is loded when model is selected.\
\
Script executes until

* it misbehaves (e.g. run-time error or low memory)
* [One-time Script](one-time-scripts.md) is running. When One-time script finishes execution, Wigdet Script resumes execution.

{% hint style="warning" %}
### Limitations

* cannot update LCD screen or perform user input.
* should not exceed allowed run-time/ number of instructions.
* custom scripts are run with less priority than built-in mixes. Their execution period is around 30ms and is not guaranteed!
{% endhint %}

{% hint style="warning" %}
If the script output is used as a `mixer source` , and the <mark style="color:red;">**script is killed**</mark> for whatever reason, then _the_ <mark style="color:red;">**whole mixer line is disabled**</mark>!&#x20;
{% endhint %}

{% hint style="info" %}
Mixes Scripts should be as short as possible, to avoid delays. It is also important to keep in mind that other loaded Telemetry and Function scripts can add to the response time, or worse: hang the system!
{% endhint %}

{% hint style="info" %}
By default, the necessary compile time option `LUA_MIXER` to use Mixes Scripts is enabled for all radio targets from EdgeTX v2.11 onwards.
{% endhint %}



## File Location

Mixes scripts are located on SD card in folder /SCRIPTS/MIXES/

{% hint style="warning" %}
File name length (without extension) **must be 6 characters or less**
{% endhint %}



## Interface

Every Mixes Script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

| table item | type     | required |
| ---------- | -------- | -------- |
| **run**    | function | yes      |

This function is called periodicaly when script is running. \
\
**Parameters** \
Variables matching those used in `input` table\
\
**Return values**\
Variables matching those used in `output` table\


| table item | type     | required |
| ---------- | -------- | -------- |
| **init**   | function | no       |

This function is called once when Mixes Script is loaded and executed for the first time

**Parameters**\
none\
\
**Return values**\
none\


| table item | type  | required |
| ---------- | ----- | -------- |
| **input**  | table | yes      |

The input table defines what values are available as input(s) to custom scripts.&#x20;

There are two forms of input table entries

**SOURCE**

```
{ "<name>", SOURCE }
```

SOURCE inputs provide the current value of a selected OpenTX variable. The source must be selected by the user when the script is configured. Source can be any value that EdgeTX knows about (inputs, channels, telemetry values, switches, custom functions etc.).\
**Note:** the typical input range is -1024 thru +1024. Simply divide the input value by 10.24 to convert to a percentage from -100% to +100%.

**VALUE**

```
{ "<name>", VALUE, <min>, <max>, <default> }
```

VALUE inputs provide a constant value that is set by the user when the script is configured.

* _name_ - maximum length of 8 characters
* _min_ - minimum value of -128
* _max_ - maximum value of 127
* _default_ - must be within the valid range specified
* **Maximum of 6 inputs per script**



| table item | type  | required |
| ---------- | ----- | -------- |
| **output** | table | yes      |

The output table defines only name(s), as the actual values are returned by the script's run function.

```lua
{ "<name1>", "<name2>" }
```

{% hint style="info" %}
Above names are only visible as source values on the radio screen when the script is running. If the model is edited in Companion, then the values show as `LUA1a` and `LUA1b` etc.
{% endhint %}



### Examples

Example of <mark style="color:purple;">\<decribe what it does>.</mark>

```lua
local my_input =
  {
    { "Strength", SOURCE},           -- user selects source (typically slider or knob)
    { "Interval", VALUE, 0, 100, 0 } -- interval value, default = 0.
  }

local my_output = { "Val1", "Val2" }

local function my_init()
  -- Called once when the script is loaded
end

local function my_run(Strength, Interval) -- Must match input table
  local v1, v2
  -- Called periodically
  return v1, v2                        -- Must match output table
end

return { input = my_input, output = my_output, run = my_run, init = my_init }
```

Example where Lua mix script is used to drive ailerons in some clever way, but control falls back to the standard aileron mix if script is killed. Second mixer line replaces the first one when the script is alive:

```
CH1  [I4]Ail Weight(+100%)
  := LUA4b Weight(+100%)
```
