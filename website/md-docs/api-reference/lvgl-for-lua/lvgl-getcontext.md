---
description: >-
  For a widget, returns the local instance table created (and returned from) the
  script 'create()' function.
---

# lvgl.getContext

## Syntax

lvgl.getContext()

## Parameters

The function has no parameters.

## Return values

Widget scripts return a table of data local to the instance of the script from the script 'create()' function. This function retrieves this table for use in other functions.

Always returns nil for stand alone tool scripts.

## API Status

<table><thead><tr><th width="153"></th><th width="99" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
