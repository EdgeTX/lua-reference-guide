---
description: Add a momentary text button using the EdgeTX style.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/lvgl-for-lua/lvgl.momentarybutton
---

# lvgl.momentaryButton

## Syntax

lvgl.momentaryButton(\[parent], {settings})

parent:momentaryButton({settings})

## Parameters

See the API page for parameter description and common settings.

Button specific settings:

<table><thead><tr><th width="124">Name</th><th width="122">Type</th><th width="289">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>text</td><td>String or Function</td><td>Text to be displayed in the button.</td><td>Empty string</td></tr><tr><td>press</td><td>Function</td><td>Called when the user first taps on the button. </td><td>nil</td></tr><tr><td>release</td><td>Function</td><td>Called when the user releases the ENTER key or stops touching the screen. </td><td>nil</td></tr><tr><td>active</td><td>Function</td><td>Set the enabled / disabled state. Return value must be a boolean - true to enable the control, false to disable.</td><td>nil</td></tr><tr><td>color</td><td>Color or Function</td><td>Sets the background color for the button.</td><td>EdgeTx button style color - PRIMARY2 theme color.</td></tr><tr><td>textColor</td><td>Color or Function</td><td>Sets the text color for the button label.</td><td>EdgeTx button style color - SECONDARY1 theme color.</td></tr><tr><td>cornerRadius</td><td>Number</td><td>Sets the radius for the corners of the button.</td><td>EdgeTx button style radius.</td></tr><tr><td>font</td><td>Font value or Function</td><td>Sets the font size. <br>E.G.:<br>- MIDSIZE<br>- DBLSIZE</td><td>STDSIZE</td></tr></tbody></table>

## Notes

Unlike the standard button the press function is called immediately when the user taps on the screen or presses the ENTER key when the momentary button is selected. The button shows in the 'checked' state until the user releases the ENTER key or stops touching the screen.

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
