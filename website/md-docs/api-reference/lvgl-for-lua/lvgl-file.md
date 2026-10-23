---
description: >-
  Display a button showing a filename. When tapped a popup file picker is
  opened. Uses EdgeTX styling.
---

# lvgl.file

## Syntax

lvgl.file(\[parent], {settings})

parent:file({settings})

## Parameters

See the API page for parameter description and common settings.

Choice specific settings:

<table><thead><tr><th width="129">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>title</td><td>String</td><td>Text to be displayed in the header of the popup menu.</td><td>Empty string</td></tr><tr><td>get</td><td>Function</td><td>Called to get the name of the currently selected file, when the popup menu is first opened.<br>Must return a string.</td><td>nil</td></tr><tr><td>set</td><td>Function</td><td>Called when the user taps on a file name.<br>The function is passed the file name selected (does not include file path).</td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr><tr><td>folder</td><td>String</td><td>Folder on SD card to browse for files,</td><td>nil</td></tr><tr><td>extension</td><td>String</td><td>Filter for extension matching.<br>Concatenate desired extensions into a single string.<br>E.G. ".png" will match only PNG image files. ".png.bmp" will match both PNG and BMP images.</td><td>nil</td></tr><tr><td>hideExtension</td><td>Boolean</td><td>Hide the file extension in the picker list.<br>If true the file extension is not included in when the 'set' function is called.</td><td>false</td></tr><tr><td>maxLen</td><td>Number</td><td>Limits the maximum file name length. If set, files with longer names are not shown in the picker list.</td><td>255</td></tr></tbody></table>

## Return values

LVGL object

## Notes

The popup menu is closed when the user selects an item, and the 'set' function is called.

If the user taps outside the menu or the RTN key is pressed, the popup menu is closed and the 'set' function is not called.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
