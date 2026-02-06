---
description: Add a number edit box using the EdgeTX style.
---

# lvgl.numberEdit

## Syntax

lvgl.numberEdit(\[parent], {settings})

parent:numberEdit({settings})

## Parameters

See the API page for parameter description and common settings.

Number edit specific settings:

<table><thead><tr><th width="133">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>get</td><td>Function</td><td>Called to get the current value to display.</td><td>nil</td></tr><tr><td>set</td><td>Function</td><td>Called when the user interacts with the control.<br>The function is passed the new value.<br><br>Note: this function is called for every change in the number value. To only get the final value when the user is finished editing use the 'edited' function.</td><td>nil</td></tr><tr><td>edited<br><br>Added in 2.11.5</td><td>Function</td><td>Called after the user has finished editing the value.<br>The function is passed the final edited value.</td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr><tr><td>min</td><td>Number</td><td>Sets the minimum allowed value.</td><td>-1024</td></tr><tr><td>max</td><td>Number</td><td>Sets the maximum allowed value.</td><td>1024</td></tr><tr><td>display</td><td>Function</td><td>Can be used to override how the value is displayed in the control. The function is passed the current value as a parameter and must return a string to display the value.</td><td>nil</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
