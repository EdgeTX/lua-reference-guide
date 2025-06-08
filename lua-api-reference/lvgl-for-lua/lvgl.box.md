---
description: Create a container for managing object layout.
---

# lvgl.box

## Syntax

lvgl.box(\[parent], {settings})

parent:box({settings})

## Parameters

See the API page for parameter description and common settings.

Box specific settings:

<table><thead><tr><th width="113">Name</th><th>Type</th><th>Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>flexFlow</td><td>Flow type - lvgl.FLOW_COLUMN or lvgl.FLOW_ROW</td><td>Enable flex layout for this box.</td><td>not used</td></tr><tr><td>flexPad</td><td>Number</td><td>When flex layout is used, set the padding between rows or columns.<br>Recommended to use the lvgl.PAD_xxx values.</td><td>0</td></tr><tr><td>scrollBar</td><td>Boolean</td><td>Enables or disables scroll bars. Set to false to disable scroll bars.</td><td>true</td></tr><tr><td>scrollDir</td><td>Scroll type - lvgl.SCROLL_xx</td><td>Sets the allowed scrolling directions if child objects extend beyond the box boundaries.<br>Only valid for stand alone scripts.</td><td>lvgl.SCROLL_ALL</td></tr><tr><td>scrolled</td><td>Function</td><td>Called when the box content is scrolled. Passed two parameters 'x', and 'y' which are the current scroll position of the box window.</td><td>nil</td></tr><tr><td>scrollTo</td><td>Function</td><td>Function to override the box scroll position. Must return two values, 'x' and 'y' which are the position to scroll the box window to.</td><td>nil</td></tr></tbody></table>

## Notes

The box object is a helper for managing screen layouts.

When adding controls such as button, toggle, textEdit etc, be sure to leave enough space for the focus outline around the control.

When used in a stand alone tool script, the box will automatically add scroll bars if any child objects are placed outside of the box boundaries. For widgets, child objects outside the box bounds will be clipped.

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Return values

LVGL object

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
