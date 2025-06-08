---
description: >-
  Display a button showing an option value. When tapped a popup menu is opened
  with multiple options to choose from. Uses EdgeTX styling.
---

# lvgl.choice

## Syntax

lvgl.choice(\[parent], {settings})

parent:choice({settings})

## Parameters

See the API page for parameter description and common settings.

Choice specific settings:

<table><thead><tr><th width="124">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>title</td><td>String</td><td>Text to be displayed in the header of the popup menu.</td><td>Empty string</td></tr><tr><td>values</td><td>Table</td><td>Must contain a simple table of strings. Each string defines an options shown in the popup menu.</td><td>Empty list</td></tr><tr><td>get</td><td>Function</td><td>Called to get the index of the currently selected option, when the popup menu is first opened.<br>Must return a number between 1 and the number of values.</td><td>nil</td></tr><tr><td>set</td><td>Function</td><td>Called when the user taps on a menu item.<br>The function is passed a single parameter wihich is the index of the selected item (1 .. number of values)</td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr><tr><td>filter</td><td>Function</td><td>Allows the popup menu list to be filtered when the user opens the popup.<br>This function is called for each option in the values table. The index of the option is passed as a parameter to the function.<br>If the function returns true the option is shown in the popup, false will hide the option.</td><td>nil</td></tr><tr><td>popupWidth</td><td>Number</td><td>Set the width of the popup window.</td><td>0 (use default width)</td></tr></tbody></table>

## Return values

LVGL object

## Notes

The popup menu is closed when the user selects an item, and the 'set' function is called.

If the user taps outside the menu or the RTN key is pressed, the popup menu is closed and the 'set' function is not called.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
