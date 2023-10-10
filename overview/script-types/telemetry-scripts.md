# Telemetry Scripts

## Overview

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
* one-time script is running (see [One-time scripts](one-time-scripts.md))

## File Location

Telemetry scripts are located on the SD card in the folder /SCRIPTS/TELEMETRY/.&#x20;

{% hint style="warning" %}
Telemetry script file name length (without extension) **must be 6 characters or less**&#x20;
{% endhint %}

## Interface

Every script must include a `return` statement at the end, defining its interface to EdgeTX. This statement returns a table with the following fields:

*   `run` (function) obligatory\
    this function is called periodicaly when Telemetry script is running\
    \
    **Parameters** \
    \
    `event` (number)\
    This parameter is used to indicates which radio key has been pressed (see [Key Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/key\_events.md)).

    \
    `touchState` (table)\
    This parameter is only present when radio is equiped with touch interface and `event` is a touch event (see [Touch State Events](../part\_iii\_-\_opentx\_lua\_api\_reference/constants/touch-event-constants.md)).\
    \
    **Return values**\
    \
    none\

* `init` function (optional)\
  this function is called once when Telemtry script is loaded and executed for the first time.\
  \
  **Parameters**\
  \
  none\
  \
  **Return values**\
  \
  none\

* `background` function (optional)\
  \
  **Parameters**\
  \
  none\
  \
  **Return values**\
  \
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

