---
description: Create a container for managing object layout.
---

# lvgl.setting

## Syntax

lvgl.setting(\[parent], {settings})

parent:setting({settings})

## Parameters

See the API page for parameter description and common settings.

Setting specific settings:

<table><thead><tr><th width="120">Name</th><th width="201">Type</th><th width="341">Description</th><th>Default</th></tr></thead><tbody><tr><td>title</td><td>String or Function<br><br>(Function support available in 2.11.6 or later)</td><td>Text to be displayed on the left.</td><td>Empty string</td></tr></tbody></table>

## Notes

The setting object is designed to manage a single row in a page of user settings. It automatically includes the necesary padding for correctly displaying controls such as toggle, textEdit, button etc.

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
