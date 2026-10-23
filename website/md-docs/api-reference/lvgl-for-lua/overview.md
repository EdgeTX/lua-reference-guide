# Overview

EdgeTX widgets and One-Time scipts can make use of LVGL controls and objects to create the script user interface. In addition to providing much better performance, this gives Lua scripts the same styles applied to firmware LVGL pages and controls.

The LVGL API can be used to add varios objects such as labels, rectangles, circles, buttons, toggle switches, sliders and more. Objects can be grouped, e.g. a rectangle can contain child labels or any other object. Objects can be moved, resized and updated as needed.

Many object properties can be set dynamically through functions in the Lua script - whenever the function returns a new value the objects property is automaticall changed. This removes the need for manually re-drawing the user interface.

### Limitations:

* Direct drawing via the 'lcd' API is not available for scripts using LVGL to create the UI.

### Activating the LVGL API

A script that wants to use LVGL to create the UI must return 'useLvgl = true' in the table returned by the script:

```lua
return {init = init, run = run, useLvgl=true}
```

Once activated a new 'lvgl' object will be available to use in the script. This is the primary interface to the LVGL API.

Scripts should check that 'lvgl' is not nil before use. If the 'lvgl' object is nil it is most likely the script is running on an earlier version of EdgeTX (prior to 2.11), or you forgot to set 'useLvgl = true'. Scripts should either display an error or fall back to using the lcd API in LVGL is not available.

### Usage patterns

#### One-Time scripts

One-Time scripts have only two functions. Prior to the LVGL API, the 'init' function would be used to set up the initial state for the script and the 'run' function would re-draw the UI whenever called as well as process key and touch events.

With the LVGL API, the 'init' function should still set up the initial state for the script; but should also create the UI from LVGL objects. The 'run' function may handle key and touch events; but in most cases the LVGL objects themselves will do the heavy lifting. When set up correctly the LVGL UI will be automatically updated as the local state is changed, and the script will be automatically updated as the user interacts with the LVGL objects.

#### Widget scripts

Widget scripts using LVGL should create their UI in the 'update' function using the widget size to determine what elements to create and how to lay them out.

The 'background' and 'run' functions should just update essential state changes that are not being managed directly by the LVGL objects.

#### Controls and focus

Controls such as 'button', 'toggle', 'textEdit', etc will automatically display a focus outline around the control when it has input focus. This outline is 2 pixels wide so enough space must be left between and around controls to display the outline.
