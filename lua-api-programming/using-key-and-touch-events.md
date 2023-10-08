---
description: >-
  This section will discuss how interactive scripts receiving user inputs via
  key and touch events can be created.
---

# Using Key and Touch Events

The two Lua widgets **EventDemo** and **LibGUI** are provided on the SD card content for color screen radios. EventDemo is just a small widget showing off how key, and especially touch events, can be used. LibGUI contains a globally available library, and a widget showing how the library can be used by other widgets. This section will discuss these two widgets for color screen radios, but generally, what is stated about key events here also applies to the `run` function in Telemetry and One-Time scripts.

## EventDemo Widget

This widget uses the design pattern for saving memory by loadable files discussed in the [previous section,](saving-memory.md#widget-script-radios) so all of the action takes place in the file **loadable.lua**. The following code listing is an outline of the `refresh` function with comments explaining what is going on.

```lua
-- This code chunk is loaded on demand by the widget's main script 
-- when the create(...) function is run. Hence, the body of this 
-- file is executed by the widget's create(...) function.

-- zone and options were passed as arguments to chunk(...)
local zone, options = ...
-- The widget table will be returned to the main script
local widget = { }

function widget.refresh(event, touchState)
  if event == nil then -- Widget mode
    -- Draw in widget mode. The size equals zone.w by zone.h
  else -- Full screen mode
    -- Draw in full screen mode. The size equals LCD_W by LCD_H
    if event ~= 0 then -- Do we have an event?
      if touchState then -- Only touch events come with a touchState
        if event == EVT_TOUCH_FIRST then
          -- When the finger first hits the screen
        elseif event == EVT_TOUCH_BREAK then
          -- When the finger leaves the screen and did not slide on it
        elseif event == EVT_TOUCH_TAP then
          -- A short tap gives TAP instead of BREAK
          -- touchState.tapCount shows number of taps
        elseif event == EVT_TOUCH_SLIDE then
          -- Sliding the finger gives a SLIDE instead of BREAK or TAP
          if touchState.swipeRight then
            -- Is true if user swiped right
          elseif touchState.swipeLeft then
          elseif touchState.swipeUp then
          elseif touchState.swipeDown then
            -- etc.
          else
            -- Sliding but not swiping
          end
        end
      else -- event ~= 0 and touchState == nil: key event
        if event == EVT_VIRTUAL_ENTER then
          -- User hit ENTER
        elseif event == EVT_VIRTUAL_EXIT then
          -- etc.
        end
      end
    end    
  end
end
```

## LibGUI

LibGUI was created to support the SoarETX widgets, but it was made separate so everyone can use it, if they so desire. Since it is all Lua, the code is visible for everyone to study and use as is, or modify for their own use (as long as they comply with the terms of the Gnu Public license, of course).

It is a widget that comes with a global library. Since all widgets are loaded, whether or not they are being used, global functions declared in the body of a widget script will always be available in any widget script in the `create` and `refresh` functions. It is not necessary to setup the widget to use the library, and the only purpose of the widget is to show how `LibGUI` can be used to create widget apps.

The library is implemented in the [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/libgui.lua.** The widget that demonstrates how to use the library is implemented in the [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/loadable.lua**. The file **/WIDGETS/LibGUI/main.lua** contains the standard functions needed for a widget and handles the loading of the two other files.

The global function `loadGUI()` returns a new `libGUI` object. This object can be used to create new `GUI`objects, which are used to create screens with elements like buttons, menus, labels, numbers etc.

### libGUI Properties

`libGUI` has the following properties controlling general settings for the library.

#### libGUI.flags

These are default drawing flags to be applied if no flags are given at creation of screen elements.

**Note:** these flags should not contain color values, as colors are added by the following.

#### libGUI.colors

This is a table of the colors used for drawing the GUI elements. These are all theme colors by default, but they can be changed for the `libGUI` instance without changing the theme colors anywhere else.

| Color    | Default value          | Used for                                                                     |
| -------- | ---------------------- | ---------------------------------------------------------------------------- |
| primary1 | COLOR\_THEME\_PRIMARY1 | Text on dropDown menu                                                        |
| primary2 | COLOR\_THEME\_PRIMARY2 | Text on buttons and numbers/timers being edited                              |
| primary3 | COLOR\_THEME\_PRIMARY3 | Text on labels, menus, and numbers/timers                                    |
| focus    | COLOR\_THEME\_FOCUS    | Background on buttons and numbers/timers being edited.                       |
| edit     | COLOR\_THEME\_EDIT     | Background when a value is being edited.                                     |
| active   | COLOR\_THEME\_ACTIVE   | Background on active toggle buttons and the border around selected elements. |

#### libGUI.widgetRefresh

A function `f()` to draw the zone of the screen in widget mode. It takes no arguments.

### libGUI Functions

#### libGUI.match(x, ...)

This is a small utility function that returns `true` if the first argument `x` matches any of the following arguments. It is useful for comparing values of `event`, e.g. if we want to test if the user pressed either of the following buttons, we can use:`libGUI.match(event, EVT_VIRTUAL_ENTER, EVT_VIRTUAL_EXIT, EVT_VIRTUAL_MENU)`

#### libGUI.newGUI()

This is the main function that creates a new `GUI` object. If an application has different screens, then a `GUI` object is created for each screen.

### GUI Object Properties

#### GUI.fullScreenRefresh

A function `f()` to draw the screen background in full screen mode. The GUI elements are drawn afterwards on top.

### GUI Object Functions

#### GUI.run(event, touchState)

Redraws the screen and processes key and touch events. It can directly replace a widget's `refresh` function, or it can be called by `refresh`.

#### GUI.setEventHandler(event, f)

Sets a function `f(event, touchState)` to handle an event. If no GUI element is being edited, then this can trap events before they are passed to the GUI, e.g. to press EXIT to go back to the previous screen. If `f` is `nil`, then the event handler is removed.

If the function returns another event value, then it is passed to the active screen element (i.e. the handler can modify certain events).

It cannot trap the events `EVT_VIRTUAL_PREV`, `EVT_VIRTUAL_NEXT` as these events are used for navigation. If elements are being edited, then this also takes precedence over the event handler.

#### GUI.showPrompt(guiPrompt)

This function can be used to show a modal prompt window, or trap events (alternative to `setEventHandler`). `guiPrompt` is a `GUI` or another Lua table with a function `run(event, touchState`).

When it is set, the main GUI will first be drawn, and then it will call `guiPrompt.run(event, touchState)` instead of its own `onEvent` function.&#x20;

#### GUI.dismissPrompt()

Dismisses the prompt.

### GUI Screen Elements

The screen elements are drawn in the order that they are added to the GUI, and touch events are sent to the first element that covers the touched point of the screen. GUI elements therefore should never overlap.

There are some common properties that can be set for all or most of the GUI elements.

* `element.disabled = true` prevents the element from taking focus and receiving events, and disabled buttons are greyed out.
* `element.hidden = true` in addition to the above, the element is not drawn.
* `element.title` can be changed for elements with a title.
* `element.value` can be changed for elements with a value.
* `element.flags` drawing flags for the element's text. If no flags were given at element creation, it defaults to `GUI.flags`.

The various screen elements are added to the GUI with the functions described below. The functions all add the element to the GUI and returns a reference so the element subsequently can be accessed by the client.

#### GUI.button (x, y, w, h, title, callBack \[, flags])

Add a button to the GUI.

When tapped, it calls `callBack(self)` so a call back function can tell which button activated it.

#### GUI.toggleButton(x, y, w, h, title, value, callBack \[, flags])

Add a toggle button to the GUI.

The `value` is either `true` or `false`.

When tapped, it calls `callBack(self)` so a call back function can tell which toggle button activated it, and what `self.value` is.

#### GUI.number(x, y, w, h, value, changeValue \[, flags])

Add an editable number to the GUI.

The `value` can be either a number or text. By setting the value to a text, it can be shown that the number is not present e.g. by "- -" or similar.

When tapped, the number will go to edit mode. In edit mode, and `changeValue(d, self)` is called if the increase/decrease buttons are pressed, or a finger is slided up or down from the number. The parameter `d` is the number of "ticks" by which the number is being changed, and `changeValue` must return the new value for the number. In a simple case, the new value would just be `self.value + d`, but it could also select new values from a table etc.

#### GUI.timer(x, y, w, h, tmr, changeValue \[, flags])

Add a timer to the GUI.

If no `value` is present, then the model timer `tmr` will be shown. If `value` is a number, then it indicates the time in seconds, and it will be shown as **MM:SS**. The `value` can also be text, e.g. "- - : - -" to show that the timer is disabled.

When tapped, the timer will go to edit mode, as described above for number.

#### GUI.label(x, y, w, h, title\[, flags])

Add a text label to the GUI.

The label does not respond to any events, but its `title` and `flags` can be changed.

#### GUI.menu(x, y, w, h, items, callBack \[, flags])

Add a scrollable menu to the GUI.&#x20;

`items` is a table with the menu item texts.

When a menu item is tapped, it calls `callBack(self)` and `self.selected` gets the index of the selected item.

#### GUI.dropDown(x, y, w, h, items, selected, callBack, flags)

Add a field with values that can be selected on a drop down menu.

`items` is a table with the items that can be selected from.

`selected` is the index of the initially selected item.

When an item has been selected, it calls `callBack(self)`. The index of the selected item is given by `self.selected`.

#### GUI.gui.horizontalSlider(x, y, w, value, min, max, delta, callBack)

Adds a horizontal slider that starts at `(x, y)` and has the width `w`.

`value` is the initial value, and `min - max` is the interval of values that can be selected with step size `delta`.

When the value is changed, `callBack(self)` is called, and the value is given by `self.value`.

#### GUI.gui.verticalSlider(x, y, w, value, min, max, delta, callBack)

The same as the above, just vertical.

#### gui.custom(self, x, y, w, h)

This can be used to create your own custom GUI elements. `self` is a table containing the element. You must define the functions `self.draw(focused)` and `self.onEvent(event, touchState)`. There is a function `self.drawFocus(color)` defined that can draw a border around the element (use if focused == true).&#x20;

#### gui.gui(x, y, w, h)

Create a nested sub-GUI. This can be used to group GUI elements which will be offset by `(x, y)` relative to the parent `GUI`.
