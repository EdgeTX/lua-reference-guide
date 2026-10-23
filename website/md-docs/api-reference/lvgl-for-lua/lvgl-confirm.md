---
description: Display a 'Yes' / 'No' confirmation dialog box.
---

# lvgl.confirm

## Syntax

lvgl.confirm({settings})

## Parameters

The lvgl.confirm function uses only the settings shown below. The common settings shown on the API page are not used.

<table><thead><tr><th width="120">Name</th><th width="103">Type</th><th width="341">Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>title</td><td>String</td><td>Text to be displayed in the header of the dialog box.</td><td>Empty string</td></tr><tr><td>message</td><td>String</td><td>Text to be displayed in the body of the dialog box</td><td>Empty string</td></tr><tr><td>confirm</td><td>Function</td><td>Called when the user taps the 'Yes' button.</td><td>nil</td></tr><tr><td>cancel</td><td>Function</td><td>Called when the user taps the 'No' button.</td><td>nil</td></tr></tbody></table>

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
