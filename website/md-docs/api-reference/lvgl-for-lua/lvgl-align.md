---
description: >-
  Display a button showing a text alignment name. When tapped a popup menu is
  opened to choose a text alignment from. Uses EdgeTX styling.
---

# lvgl.align

## Syntax

lvgl.align(\[parent], {settings})

parent:align({settings})

## Parameters

See the API page for parameter description and common settings.

Choice specific settings:

<table><thead><tr><th width="124">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>get</td><td>Function</td><td>Called to get the currently selected alignment, when the popup menu is first opened.</td><td>nil</td></tr><tr><td>set</td><td>Function</td><td>Called when the user taps on an alignment button.<br>The function is passed a single parameter wihich is the selected alignement value.</td><td>nil</td></tr></tbody></table>

## Notes

The popup menu is closed when the user selects an item, and the 'set' function is called.

If the user taps outside the menu or the RTN key is pressed, the popup menu is closed and the 'set' function is not called.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
