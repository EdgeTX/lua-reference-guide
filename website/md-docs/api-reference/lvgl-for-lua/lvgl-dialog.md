---
description: Display a dialog box.
---

# lvgl.dialog

## Syntax

lvgl.dialog({settings})

## Parameters

The lvgl.dialog function uses only the settings shown below. The common settings shown on the API page are not used.

<table><thead><tr><th width="120">Name</th><th width="201">Type</th><th width="341">Description</th><th>Default</th></tr></thead><tbody><tr><td>title</td><td>String</td><td>Text to be displayed in the header of the dialog box.</td><td>Empty string</td></tr><tr><td>close</td><td>Function</td><td>Called when the dialog box is closed.</td><td>nil</td></tr><tr><td>flexFlow</td><td>Flow type - lvgl.FLOW_COLUMN or lvgl.FLOW_ROW</td><td>Enable flex layout for this box.</td><td>not used</td></tr><tr><td>flexPad</td><td>Number</td><td>When flex layout is used, set the padding between rows or columns.<br>Recommended to use the lvgl.PAD_xxx values.</td><td>0</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
