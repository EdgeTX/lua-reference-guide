---
description: Display a text label.
---

# lvgl.rectangle

## Syntax

lvgl.rectangle(\[parent], {settings})

parent:rectangle({settings})

## Parameters

See the API page for parameter description and common settings.

Rectangle specific settings:

<table><thead><tr><th width="120">Name</th><th width="126">Type</th><th width="335">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>thickness</td><td>Number</td><td>Sets the width of the line used to draw the border.</td><td>1</td></tr><tr><td>filled</td><td>Boolean</td><td>If true the rectangle is filled with the 'color' value.</td><td>false</td></tr><tr><td>rounded</td><td>Number</td><td>If greater than 0 makes the corners rounded with a radius set this value.<br>When set to a value greater than 0, must also be >= thickness.</td><td>0</td></tr><tr><td>opacity</td><td>Number or Function</td><td>Sets the opacity.<br>Note: range is 0 (transparent) to 255 (opaque)</td><td>255 (opaque)</td></tr><tr><td>scrollDir</td><td>Scroll type - lvgl.SCROLL_xx</td><td>Sets the allowed scrolling directions if child objects extend beyond the rectangle boundaries.<br>Only valid for stand alone scripts.</td><td>lvgl.SCROLL_ALL</td></tr></tbody></table>

## Notes

When used in a stand alone tool script, the rectangle will automatically add scroll bars if any child objects are placed outside of the rectangle boundaries. For widgtes, child objects outside the rectangle bounds will be clipped.

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
