# Widget Scripts

## General description

Widgets are only available on radios with color displays. Most of the time, they show some info in a 'zone' either in the _top bar_ or in one of the model specific user defined _main views_, and they cannot receive direct input from the user via key events like e.g. Telemetry scripts.

But widgets on the _main views_ can also be shown in _full screen mode_, where they take over the entire screen area, and then they can receive user input via key events, and for radios with touch screen, also touch events.

Each model can have up to five _main views_, with up to 8 widgets per screen, depending on their size and layout. Each instance of a widget has his own custom settings.

## File Location

Widgets are located on the SD card, each in their specific folder /WIDGETS/&lt;_name_&gt;/main.lua \(_name_ must be in 8 characters or less\).

## Lifetime of widgets

All widget scripts on the SD card are loaded into memory when the radio is powered on. This has the side effect that any global functions defined in a widget script will always be available to other widget scripts. It also means that any script on the SD card will consume part of the radio's memory - even if it is not being used. Therefore, it is important to either keep widget scripts small, or to use Lua's loadScript\(\) function to load code dynamically.

They can be added to the _top bar_ or a _main view_  through the telemetry setup menu. When  a widget has been added to a screen, then the widget functions are called as follows:

* `create` function is called one time when the script is loaded
* `update` function is called upon registration and at change of settings in the telemetry setup menu.
* `background` function is periodically called when custom telemetry screen is _not visible_. **Note:** this is different from the way telemetry scripts are handled.
* `refresh` function is periodically called when custom telemetry screen is _visible_.

A widget script is stopped and disabled if it misbehaves \(e.g. too long runtime, run-time error, or low memory\), and all widgets are stopped while one-time script is running \(see One-Time scripts\).

## Script interface definition

Every widget must include a return statement at the end, that defines its interface to the rest of OpenTX code. This statement defines:

* **name** \(_name_ must be a string of 10 characters or less\)
* **options** array \(maximum five options are allowed, 10 character names max, no spaces!\)
* **create** function
* **update** function
* **background** function \(optional\)
* **refresh** function

### Example \(draws a moving counter that counts only when not visible\):

```lua
local defaultOptions = {
  { "ControlX", SOURCE, 1 },
  { "ScrollZ", BOOL, 1 }, -- BOOL is actually not a boolean, but toggles between 0 and 1
  { "StepZ", VALUE, 1, 0, 10},
  { "COLOR", COLOR, RED },
}

local function createWidget(zone, options)
  lcd.setColor( CUSTOM_COLOR, options.COLOR )
  --  the CUSTOM_COLOR is foreseen to have one color that is not radio template related, but it can be used by other widgets as well!
  local someVariable = 0
  local anotherVariable = {xWidget=0, yWidget = 0}
  return { zone=zone, options=options , someVariable = someVariable, anotherVariable=anotherVariable }
end

local function updateWidget(widgetToUpdate, newOptions)
  widgetToUpdate.options = newOptions
  lcd.setColor( CUSTOM_COLOR, widgetToUpdate.options.COLOR )
  --  the CUSTOM_COLOR is foreseen to have one color that is not radio template related, but it can be used by other widgets as well!
end

local function backgroundProcessWidget(widgetToProcessInBackground)
  local function process(...)
          return ... + 1
        end
  widgetToProcessInBackground.someVariable = process (widgetToProcessInBackground.someVariable)
end

local function refreshWidget(widgetToRefresh)
  local counterLength = 50
  local counterHeight = 30

  --backgroundProcessWidget(widgetToRefresh) 
  --background is not called automatically in display mode, so do it here if you need it.

  local function anotherProcess(parameter,step,maxParameter)
          return (parameter + step) % maxParameter
        end

  widgetToRefresh.anotherVariable.xWidget 
    = anotherProcess ( widgetToRefresh.anotherVariable.xWidget
      ,getValue(widgetToRefresh.options.ControlX)/10.24/20 
      ,widgetToRefresh.zone.w-counterLength)

  widgetToRefresh.anotherVariable.yWidget 
    = anotherProcess ( widgetToRefresh.anotherVariable.yWidget
      ,(widgetToRefresh.options.ScrollZ==1) and widgetToRefresh.options.StepZ or 0
      ,widgetToRefresh.zone.h-counterHeight)

  lcd.drawNumber(widgetToRefresh.anotherVariable.xWidget + widgetToRefresh.zone.x
    , widgetToRefresh.anotherVariable.yWidget + widgetToRefresh.zone.y
    , widgetToRefresh.someVariable
    , LEFT + DBLSIZE + CUSTOM_COLOR);
end

return { name="MovingCntr", options=defaultOptions, create=createWidget, update=updateWidget
  , refresh=refreshWidget, background=backgroundProcessWidget }
```

## Notes:

* _options_ are only passed through to OpenTX to be used on widget creation. Don't change them during operation, this has no effect.
* _create\(\)_ function is called once when widget is loaded and begins execution.
* _update\(\)_ function is called once when widget is loaded and begins execution.
* _background\(\)_ is called periodically when custom telemetry screen containing widget is not visible.
* _refresh\(\)_ function is called periodically when custom telemetry screen containing wodget is visible.
* in the example given, you can see that no global variables or functions are needed to operate the widget.
* variables that are used throughout the widget, can best be declared _inside_ the create function as local variables
* those local variablkes can then be passed through to the other functions as an element of the widget array that is returned

