---
description: >-
  This section will discuss how interactive scripts receiving user inputs via
  key and touch events can be created.
---

# Using Key and Touch Events

The two Lua widgets **EventDemo** and **LibGUI** are provided on the SD card content for color screen radios. EventDemo is just a small widget showing off how key and especially touch events can be used. LibGUI contains a globally available library, and a widget showing how the library can be used by other widgets. This section will discuss these two widgets for color screen radios, but generally, what is stated about key events here also applies to the `run` function in Telemetry and One-Time scripts.

## EventDemo Widget

This widget uses the design pattern discussed in the [previous section,](saving-memory.md#widget-script-radios) so all of the action takes place in the file **loadable.lua**. The following code listing is an outline of the `refresh` function with comments explaining what is going on.

```lua
function widget.refresh(event, touchState)
  if event == nil then -- Widget mode
    -- Draw in non-fullscreen mode. The size equals zone.w by zone.h
  else -- Full screen mode
    -- Draw in fullscreen mode. The size equals LCD_W by LCD_H
    -- Process touch and key events
    if event ~= 0 then -- We got a new event
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

The library is implemented in the [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/libgui.lua.** The widget that demonstrates how to use the library is implemented in [loadable file](saving-memory.md#widget-script-radios) **/WIDGETS/LibGUI/loadable.lua**. **/WIDGETS/LibGUI/main.lua** contains a global function that loads the library and the standard function needed for a widget.

The global function `loadGUI()` returns a new `libGUI` object. This object can be used to create new `GUI`objects, which are used to create screens with elements like buttons, menus, labels, numbers that can be edited, and timers.

### libGUI Properties

`libGUI` has the following properties controlling global settings.

#### libGUI.flags

These are default drawing flags to be applied, unless other flags are given.

**Note:** these flags should not contain color values, as colors are added by the following.

#### libGUI.colors

This is a table of colors used for drawing the GUI elements. The following colors are available:

| Color | Default value | Used for |
| :--- | :--- | :--- |
| text | COLOR\_THEME\_PRIMARY3 | Text on labels, menus etc. |
| focusText | COLOR\_THEME\_PRIMARY2 | Text on buttons and numbers/timers being edited. |
| focusBackground | COLOR\_THEME\_FOCUS | Background on buttons and numbers/timers being edited. |
| active | COLOR\_THEME\_ACTIVE | Background on active toggle buttons and the border around selected elements. |

### libGUI Functions

`libGUI` provides the following functions.

#### libGUI.match\(x, ...\)

This is a small utility function that returns `true` if the first argument `x` matches any of the following arguments. It is useful for comparing values of `event`, e.g. if we want to test if the user pressed either of the following buttons, we can use:`libGUI.match(event, EVT_VIRTUAL_ENTER, EVT_VIRTUAL_EXIT, EVT_VIRTUAL_MENU)`

#### libGUI.newGUI\(\)

Creates a new `GUI` object. If an application has different screens, then a `GUI` for each screen can be created. `GUI` objects have the following properties.

| Property | Description |
| :--- | :--- |
| widgetRefresh | A function to refresh in widget mode. |
| fullScreenRefresh | A function to draw the screen background in full screen mode. GUI elements are drawn afterwards on top. |

`GUI` objects have the following functions.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Function</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">GUI.run(event, touchState)</td>
      <td style="text-align:left">Redraws the screen and processes key and touch events.</td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.SetEventHandler(event, f)</td>
      <td style="text-align:left">Sets a function to handle event. If no GUI element is being edited, then
        this can trap events before they are passed to the GUI, e.g. to press EXIT
        to leave the screen. If <code>f = nil</code>, then the event handler is
        removed.</td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.button (x, y, w, h, title, callBack, flags)</td>
      <td style="text-align:left">
        <p>Add a button to the GUI. The button has the following properties that
          can be changed:</p>
        <ul>
          <li>title</li>
          <li>noFocus (set to <code>false</code> to prevent it from receiving focus)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.toggleButton(x, y, w, h, title, value, callBack, flags)</td>
      <td style="text-align:left">
        <p>Add a toggle button to the GUI. The toggleButton has the following properties
          that can be changed:</p>
        <ul>
          <li>value (true/false)</li>
          <li>title</li>
          <li>noFocus (set to <code>false</code> to prevent it from receiving focus)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.number(x, y, w, h, value, callBack, flags)</td>
      <td style="text-align:left">
        <p>Add a number that can be edited to the GUI. The number has the following
          properties that can be changed:</p>
        <ul>
          <li>value (can also be text, e.g. to show &quot;-&quot; if disabled)</li>
          <li>noFocus (set to <code>false</code> to prevent it from receiving focus)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.label(x, y, w, h, title, flags)</td>
      <td style="text-align:left">
        <p>Add a text label to the GUI. The label has the following property that
          can be changed:</p>
        <ul>
          <li>title</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.timer(x, y, w, h, tmr, callBack, flags)</td>
      <td style="text-align:left">
        <p>Add a timer to the GUI. The timer has the following properties that can
          be changed:</p>
        <ul>
          <li>value. If nil, then the value of the timer tmr is shown. Otherwise, it
            shows value, which can be either a number (seconds) or text.</li>
          <li>noFocus (set to <code>false</code> to prevent it from receiving focus)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">GUI.menu(x, y, visibleCount, items, callBack, flags)</td>
      <td style="text-align:left">
        <p>Add a menu to the GUI.</p>
        <ul>
          <li>visibleCount is the number of visible menu items.</li>
          <li>items is a table with the menu items.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

