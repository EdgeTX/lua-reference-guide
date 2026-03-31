---
description: Add a text edit box using the EdgeTX style.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/lvgl-for-lua/lvgl.textedit
---

# lvgl.textEdit

## Syntax

lvgl.textEdit(\[parent], {settings})

parent:textEdit({settings})

## Parameters

See the API page for parameter description and common settings.

Text edit specific settings:

<table><thead><tr><th width="133">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>value</td><td>String</td><td>Sets the initial text that the user can edit.</td><td>Empty string</td></tr><tr><td>length</td><td>Number</td><td>Sets the maximum length of the text that can be edited.<br>Must be a number between 32 and 128.</td><td>32</td></tr><tr><td>set</td><td>Function</td><td>Called when the user edits the text.<br>The function is a string with the edited content.</td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
