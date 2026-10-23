---
description: Update the settings for an LVGL object.
---

# lvgl.set

## Syntax

lvgl.set(\[parent], {settings})

parent:set({settings})

## Parameters

See the API page for parameter description and common settings.

See the function description pages for settings specific to each LVGL object type.

### Notes

This can be used to update one or more settings for an existing LVGL object. The 'settings' parameter should contain values relevant to the type of object being created.

This can be used to update settings that do not support being controlled by functions (e.g. rectangle thickness).

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
