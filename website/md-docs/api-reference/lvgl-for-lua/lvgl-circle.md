---
description: Display a solid or filled circle.
---

# lvgl.circle

## Syntax

lvgl.circle(\[parent], {settings})

parent:circle({settings})

## Parameters

See the API page for parameter description and common settings.

Note: 'w', 'h' and 'size' should not be used with lvgl.circle. Use 'radius' instead.

Circle specific settings:

<table><thead><tr><th width="124">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>thickness</td><td>Number</td><td>Sets the width of the line used to draw the arc.</td><td>1</td></tr><tr><td>filled</td><td>Boolean</td><td>If true the circle is filled with the 'color'value</td><td>false</td></tr><tr><td>radius</td><td>Number or Function</td><td>Sets the radius of the arc</td><td>0</td></tr><tr><td>opacity</td><td>Number or Function</td><td>Sets the opacity.<br>Note: range is 0 (transparent) to 255 (opaque).</td><td>255 (opaque)</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
