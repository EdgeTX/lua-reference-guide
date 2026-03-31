---
description: Display one or more connected lines.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/lvgl-for-lua/lvgl.line
---

# lvgl.line

## Syntax

lvgl.line(\[parent], {settings})

parent:line({settings})

## Parameters

See the API page for parameter description and common settings.

The 'x, 'y, 'w' and 'h' settings are not used.

Line specific settings:

<table><thead><tr><th width="127">Name</th><th width="227">Type</th><th width="244">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>rounded</td><td>Boolean</td><td>If true then the end caps of the line are rounded.</td><td>false</td></tr><tr><td>thickness</td><td>Number</td><td>Sets the thickness of each line segment.</td><td>1</td></tr><tr><td>opacity</td><td>Number or Function</td><td>Sets the opacity.<br>Note: range is 0 (transparent) to 255 (opaque)</td><td>255 (opaque)</td></tr><tr><td>pts</td><td><p>Table or Function</p><p></p><p>Table of points. Each point must be a table with two number values ({x, y})</p></td><td>Defines the points used to draw the line segments. There must be at least two points.</td><td>nil</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
