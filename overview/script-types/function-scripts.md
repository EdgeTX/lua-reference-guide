# Function Scripts

## Purpose

Function scripts are invoked via EdgeTX **'Lua Script'** of Special Functions configuration page.

Typical uses of Function scripts are:

* specialized handling in response to switch position changes
* customized announcements

## Execution & Lifetime

Function script is loded when model is selected.\
\
Script executes until

* it misbehaves (e.g. run-time error or low memory)
* [One-time Script](one-time-scripts.md) is running. When One-time script finishes execution, Wigdet Script resumes execution.

{% hint style="warning" %}
Function scripts **DO NOT HAVE ACCESS TO LCD DISPLAY**
{% endhint %}

## File Location

Function scripts are located on the SD card in the folder /SCRIPTS/FUNCTIONS/&#x20;

{% hint style="warning" %}
File name length (without extension) **must be 6 characters or less**
{% endhint %}

## Interface

Every Function script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

* `run` (function) obligatory\
  This function is called periodicaly when **switch** assiociated the Special Function **is ON**. \
  \
  **Parameters** \
  \
  none\
  \
  **Return values**\
  \
  none\
  \

* `background` (function) obligatory\
  This function is called periodicaly when **switch** assiociated the Special Function **is OFF**\
  \
  **Parameters**\
  \
  none\
  \
  **Return values**\
  \
  none\
  \

* `init` (function) optional\
  this function is called once when Function script is loaded and executed for the first time.\
  \
  **Parameters**\
  \
  none\
  \
  **Return values**\
  \
  none\


### Example

```lua
local function my_init()
  -- Called once when the script is loaded
end

local function my_run()
  -- Called periodically while the Special Function switch is on
end

local function my_background()
  -- Called periodically while the Special Function switch is off
end

return { run = my_run, background = my_background, init = my_init }
```
