# API

LVGL objects are created and manipulated using the 'lvgl' functions.

Most of these functions follow the syntax below. A few function have only the optional 'parent' parameter.

```lua
lvgl.function([parent], {settings})
```

<table><thead><tr><th width="179">Parameter</th><th width="247">Notes</th><th>Description</th></tr></thead><tbody><tr><td>parent</td><td>Optional (with some exceptions)<br>If present must be an LVGL object</td><td>Parent object. If set then whatever LVGL objects are created by the function are set as children of 'parent'. If not set then objects are created in the top level script window.</td></tr><tr><td>settings</td><td>Mandatory (with some exceptions)<br>Must be a table</td><td>Contains all of the settings required to create the LVGL object.</td></tr></tbody></table>

Most of the functions return an LVGL object that can be used to update the UI or in other API calls.

API functions can also be called using Lua OO syntax.

For example the following two lines are equivalent.

```lua
lvgl.show(parent)
parent:show()
```

There are a number of settings that are common to all of the LVGL functions that take a 'settings' table parameter.

<table><thead><tr><th width="117">Name</th><th width="144">Type</th><th>Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>x</td><td>Number</td><td>Horizontal position of the object relative to the top left corner of the parent object.</td><td>0</td></tr><tr><td>y</td><td>Number</td><td>Vertical position of the object relative to the top left corner of the parent object.</td><td>0</td></tr><tr><td>w</td><td>Number</td><td>Width of the object</td><td>Auto size to fit content</td></tr><tr><td>h</td><td>Number</td><td>Height of the object</td><td>Auto size to fit content</td></tr><tr><td>color</td><td>Color or Function</td><td>Primary color for the object.</td><td>COLOR_THEME_SECONDARY1</td></tr><tr><td>pos</td><td>Function</td><td>Position of the object relative to the top left corner of the parent object.<br>Must return two values - x, y.</td><td>nil</td></tr><tr><td>size</td><td>Function</td><td>Size of the object. Must return two values - width, height.</td><td>nil</td></tr><tr><td>visible</td><td>Function</td><td>Controls visibility of the object. Must return a boolean - true if the object is shown, false to hide it.</td><td>nil</td></tr></tbody></table>

The functions associated with settings are called periodically by the firmware. Where a setting is defined using a function, the UI will automatically update whenever the function returns a different value.&#x20;

### A note on object width and height

Although width and height, and the size function, can be defined for all objects they may not be used in some cases. For example when creating a circle or arc object the radius property should be used instead.
