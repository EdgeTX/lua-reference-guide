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

This is a widget that comes with a global library. Since all widgets are loaded whether or not they are being used, global functions declared in the body of a widget script will always be available. It is not necessary to setup the widget to use the library, and the only purpose of the widget is to show how `LibGUI` can be used to create apps.

The library is implemented in the [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/libgui.lua.** The widget that demonstrates how to use the library is implemented in the [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/loadable.lua**. The file **/WIDGETS/LibGUI/main.lua** contains a global function that loads the library and the standard functions needed for a widget.

The global function `loadGUI()` returns a new `libGUI` object. This object can be used to create new `GUI`objects, which are used to create screens with elements like buttons, menus, labels, numbers that can be edited, and timers.

### libGUI Properties

`libGUI` has the following properties controlling general settings for the library.

#### libGUI.flags

These are default drawing flags to be applied if no flags are given at creation of screen elements.

**Note:** these flags should not contain color values, as colors are added by the following.

#### libGUI.colors

This is a table of colors used for drawing the GUI elements. The following colors are available:

| Color | Default value | Used for |
| :--- | :--- | :--- |
| text | COLOR\_THEME\_PRIMARY3 | Text on labels, menus etc. |
| focusText | COLOR\_THEME\_PRIMARY2 | Text on buttons and numbers/timers being edited. |
| buttonBackground | COLOR\_THEME\_FOCUS | Background on buttons and numbers/timers being edited. |
| editBackground | COLOR\_THEME\_EDIT | Background when a value is being edited. |
| screenBackground | `nil` | The color of the screen background. Set to `nil` to show theme background image. |
| active | COLOR\_THEME\_ACTIVE | Background on active toggle buttons and the border around selected elements. |

Notice that all of the default colors are theme colors. This will make the GUI screens use the contemporary color theme.

### libGUI Functions

#### libGUI.match\(x, ...\)

This is a small utility function that returns `true` if the first argument `x` matches any of the following arguments. It is useful for comparing values of `event`, e.g. if we want to test if the user pressed either of the following buttons, we can use:`libGUI.match(event, EVT_VIRTUAL_ENTER, EVT_VIRTUAL_EXIT, EVT_VIRTUAL_MENU)`

#### libGUI.newGUI\(\)

This is the main function that creates a new `GUI` object. If an application has different screens, then a `GUI` object is created for each screen.

### GUI Object Properties

#### GUI.widgetRefresh

A function `f()` to draw the zone of the screen in widget mode. It takes no arguments.

#### GUI.fullScreenRefresh

A function `f(event, touchState)` to draw the screen background in full screen mode. The GUI elements are drawn afterwards on top.

#### GUI.prompt

A GUI \(or another table with a function `run(event, touchState`\). When this is set, the GUI will first be drawn, and then it will call `prompt.run(event, touchState)` instead of running itself. That way, the `prompt` can implement a modal prompt window.

### GUI Object Functions

#### GUI.run\(event, touchState\)

Redraws the screen and processes key and touch events. It can directly replace a widget's `refresh` function, or it can be called by `refresh`.

#### GUI.SetEventHandler\(event, f\)

Sets a function `f(event, touchState)` to handle an event. If no GUI element is being edited, then this can trap events before they are passed to the GUI, e.g. to press EXIT to go back to the previous screen. If `f` is `nil`, then the event handler is removed.

### GUI Screen Elements

The screen elements are drawn in the order that they are added to the GUI, and touch events are sent to the first element that covers the touched point of the screen. GUI elements therefore should never overlap.

There are some common properties that can be set for all or most of the GUI elements.

* `element.disabled = true` prevents the element from taking focus and receiving events, and disabled buttons are greyed out.
* `element.hidden = true`  in addition to the above, the element is not drawn.
* `element.title` can be changed for elements with a title.
* `element.value` can be changed for elements with a value.
* `element.flags` drawing flags for the element's text. If no flags were given at element creation, it defaults to `GUI.flags`.
* `elements.blink` will make non-button elements blink
* `elements.invers` will make non-button elements draw in inversed colors.

The various screen elements are added to the GUI with the functions described below. The functions all add the element to the GUI and returns a reference so the element subsequently can be accessed by the client.

#### GUI.button \(x, y, w, h, title\[, callBack\] \[, flags\]\)

Add a button to the GUI. 

When tapped, it calls `callBack(self)` so a call back function can tell which button activated it.

#### GUI.toggleButton\(x, y, w, h, title, value\[, callBack\] \[, flags\]\)

Add a toggle button to the GUI. 

The `value` is either `true` or `false`. 

When tapped, it calls `callBack(self)` so a call back function can tell which toggle button activated it, and what `self.value` is.

#### GUI.number\(x, y, w, h, value\[, callBack\] \[, flags\]\)

Add an editable number to the GUI.

The `value` can be either a number or text. By setting the value to a text, it can be shown that the number is not present e.g. by "- -" or similar.

When tapped, the number will go to edit mode. In edit mode, events are passed to `callBack(self, event, touchState)`. Thereby, the call back function can use events to edit the number, e.g. sliding a finger up and down can increase and decrease the value. You can look in the LibGUI widget's loadable file for an example of this.

#### 

#### GUI.timer\(x, y, w, h, tmr\[, callBack\] \[, flags\]\)

Add a timer to the GUI.

If no `value` is present, then the model timer `tmr` will be shown. If `value` is a number, then it indicates the time in seconds, and it will be shown as **MM:SS**. The `value` can also be text, e.g. "- - : - -" to show that the timer is disabled.

When tapped, the timer will go to edit mode, as described above for number.

#### GUI.label\(x, y, w, h, title\[, flags\]\)

Add a text label to the GUI.

The label does not respond to any events, but its `title` and `flags` can be changed.

#### GUI.menu\(x, y, visibleCount, items\[, callBack\] \[, flags\]\)

Add a scrollable menu to the GUI. This function returns a table with each of the menu's line elements.

`visibleCount` is the number of visible menu items.

`items` is a table with the menu item texts.

When a menu item is tapped, it calls `callBack(self)`. Each menu element has a field `self.idx` giving the index in the menu, and this can be used by `callBack` to see which menu item was selected.

Notice that the menu's width is decided by the item texts and the font flags, and the height is decided by `visibleCount` and the font flags.



