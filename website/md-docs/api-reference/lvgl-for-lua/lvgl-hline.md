---
description: Display a horizontal line.
---

# lvgl.hline

## Syntax

lvgl.hline(\[parent], {settings})

parent:hline({settings})

## Parameters

See the API page for parameter description and common settings.

The 'w' setting determinse the length of the line.

The 'h' setting determines the thickness of the line.

Hline specific settings:

<table><thead><tr><th width="134">Name</th><th>Type</th><th width="244">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>rounded</td><td>Boolean</td><td>If true then the end caps of the line are rounded.</td><td>false</td></tr><tr><td>opacity</td><td>Number or Function</td><td>Sets the opacity.<br>Note: range is 0 (transparent) to 255 (opaque)</td><td>255 (opaque)</td></tr><tr><td>dashGap</td><td>Number</td><td>Sets the gap size for drawing dashed lines.</td><td>0</td></tr><tr><td>dashWidth</td><td>Number</td><td>Sets the dash size for drawing dashed lines.<br>Note: both dashGap and dashWidth must be > 0 in order to draw dashed lines.</td><td>0</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
