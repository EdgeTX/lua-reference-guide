---
description: Display a text label.
---

# lvgl.label

## Syntax

lvgl.label(\[parent], {settings})

parent:label({settings})

## Parameters

See the API page for parameter description and common settings.

Label specific settings:

<table><thead><tr><th width="159">Name</th><th>Type</th><th>Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>text</td><td>String or Function</td><td>Set the text to be displayed on the label</td><td>Empty string</td></tr><tr><td>font</td><td>Font value or Function</td><td>Sets the font size. <br>E.G.:<br>- MIDSIZE<br>- DBLSIZE</td><td>STDSIZE</td></tr><tr><td>align</td><td>Text alignment value or function</td><td><p>Sets the justification for the text.<br>E.G.:<br> - RIGHT<br> - VCENTER<br><br>Notes:</p><p>RIGHT and CENTER alignment require the width for the label to be set.<br>LEFT, RIGHT and CENTER will align the text horizontally within the label bounding box (x,y,w,h).<br>VCENTER, VTOP and VBOTTOM will align the label bounding box vertically within the parent object.</p></td><td>LEFT</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
