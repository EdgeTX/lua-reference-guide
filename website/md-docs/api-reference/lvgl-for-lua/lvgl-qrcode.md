---
description: Display a QR code.
---

# lvgl.qrcode

## Syntax

lvgl.qrcode(\[parent], {settings})

parent:qrcode({settings})

## Parameters

See the API page for parameter description and common settings.

Note: 'w' and 'h' should be set to the same value for a QR code.

QR code specific settings:

<table><thead><tr><th width="120">Name</th><th width="126">Type</th><th width="335">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>data</td><td>String</td><td>Sets the URL or other content to be enccoded in the QR code.</td><td>Empty string</td></tr><tr><td>bgColor</td><td>Color</td><td>Sets the background color for the QR code image.</td><td>COLOR_THEME_SECONDARY3</td></tr></tbody></table>

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
