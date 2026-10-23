---
description: >-
  Display an image. The image will be centered in the frame (x, y, w, h). Images
  can be scaled to either fit entirely within the frame or completely fill the
  frame.
---

# lvgl.image

## Syntax

lvgl.image(\[parent], {settings})

parent:image({settings})

## Parameters

See the API page for parameter description and common settings.

Image specific settings:

<table><thead><tr><th width="120">Name</th><th width="126">Type</th><th width="335">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>file</td><td>String</td><td>File name of the image to display. Must include full path to image file on the SD card.</td><td>Empty string</td></tr><tr><td>fill</td><td>Boolean</td><td>If true the image is scaled to completely fill the frame. The image may be cropped.<br>If false it is scaled to fit entirely in the frame. The result may have empty borders.</td><td>false</td></tr></tbody></table>

## Notes:

Width (w) and height (h) are required.

## Return values

LVGL object

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
