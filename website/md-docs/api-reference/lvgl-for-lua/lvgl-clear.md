---
description: Delete LVGL objects.
---

# lvgl.clear

## Syntax

lvgl.clear(\[parent])

parent:clear()

## Parameters

See the API page for parameter description and common settings.

The 'settings' parameter is not used.

### Notes

If 'parent' is not set then the entire script UI is deleted. Use this when the UI changes dramatically (e.g. widget size changes).

When the 'parent' parameter is defined, only the child LVGL objects within the parent are deleted. Use this to remove and replace a specific set of objects.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
