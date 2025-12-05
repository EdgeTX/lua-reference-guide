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

### Dynamically managing object size and position for different screens

EdgeTx supports both landscape and portrait orientation displays in a variety of resolutions (480x272, 480x320, 320x480, 320x240, 800x480, etc). Managing all these in a Lua script dynamically can be challenging.

To assist with this there are a number of things that can be used:

* Flex layouts can be used; but care should be taken as they are noticeably slower than using absolution position and size.
* When using the 'page' object the lvgl.PAGE\_BODY\_HEIGHT contant will give the size of the page body (minus the header). This can be used to manage the layout for the page content.
* The lvgl.UI\_ELEMENT\_HEIGHT constant defines the default height for buttons, toggles, sliders etc.
* The lvgl.LCD\_SCALE constant can be used to scale values for the current LCD size, when compared to the default 480x272 size. For example if a button needs to be 80 pixels wide on a 480x272 display then setting the width to 80 \* lvgl.LCD\_SCALE will ensure the size is adusted for the actual LCD size.&#x20;
* The lvgl.PERCENT\_SIZE value can be used to set the size and position of an object as a percentage of the parent size. For example setting width to lvgl.PERCENT\_SIZE+80 will size the object to 80% of the parent width. Setting x = lvgl.PERCENT\_SIZE+50 will set the X position to ½ of the parent width.
  * NOTE: this requires that the parent container has a defined size. If the parent size is the default auto size base on content then percentage sizing will fail. This results in a catch-22 where the parent need the child size; but the child first needs the parent size.
  * NOTE: PERCENT\_SIZE does not work for all objects. For example, images require a fixed width and height.
