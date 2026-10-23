---
description: Add a toggle switch using the EdgeTX style.
---

# lvgl.toggle

## Syntax

lvgl.toggle(\[parent], {settings})

parent:toggle({settings})

## Parameters

See the API page for parameter description and common settings.

Toggle specific settings:

<table><thead><tr><th width="133">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>get</td><td>Function</td><td>Called to get the curent state of the toggle switch.<br>Must return a boolean or a number value. 0 or false if the toggle switch is off, 1 or true if it should be on.</td><td>nil</td></tr><tr><td>set</td><td>Function</td><td>Called when the user interacts with the toggle switch.<br>The function is passed a single number parameter - 0 if the toggle switch is off, 1 if it is on.</td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
