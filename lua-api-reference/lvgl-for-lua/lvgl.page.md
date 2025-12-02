---
description: >-
  Create a page layout for a One-Time script using EdgeTX styling. The page
  layout has a menu bar at the top with title and sub-title lines as well as a
  'back' button in the top left corner.
---

# lvgl.page

## Syntax

lvgl.page({settings})

## Parameters

The lvgl.page function uses only the settings shown below. The common settings shown on the API page are not used.

<table><thead><tr><th width="120">Name</th><th width="196">Type</th><th width="333">Description</th><th>Default</th></tr></thead><tbody><tr><td>title</td><td>String or Function</td><td>Text to be displayed as the title in the header of the page.<br><br>Title can be a function in 2.11.4 or later.</td><td>Empty string</td></tr><tr><td>subtitle</td><td>String or Function</td><td>Text to be displayed as the sub-title in the header of the page.<br><br>Subtitle can be a function in 2.11.4 or later.</td><td>Empty string</td></tr><tr><td>icon</td><td>String</td><td>Full path to an image file on the SD card to be displayed as the icon in the 'back' button (top left corner).<br>If not set then the EdgeTX logo icon is used.<br>The icon file is a mask image and should be 30x30 pixels in size and be a grey-scale image. White pixels are transparent and black pixels are fully opaque.</td><td>Empty string</td></tr><tr><td>back</td><td>Function</td><td>Called when the user taps the 'back' button in the top left corner.</td><td>nil</td></tr><tr><td>flexFlow</td><td>Flow type - lvgl.FLOW_COLUMN or lvgl.FLOW_ROW</td><td>Enable flex layout for this page.</td><td>not used</td></tr><tr><td>flexPad</td><td>Number</td><td>When flex layout is used, set the padding between rows or columns.<br>Recommended to use the lvgl.PAD_xxx values.</td><td>0</td></tr><tr><td>scrollBar</td><td>Boolean</td><td>Sets the allowed scrolling directions if child objects extend beyond the box boundaries. Only valid for stand alone scripts.</td><td>true</td></tr><tr><td>scrollDir</td><td>Scroll type - lvgl.SCROLL_xx</td><td>Sets the allowed scrolling directions if child objects extend beyond the page boundaries.<br>Only valid for stand alone scripts.</td><td>lvgl.SCROLL_ALL</td></tr><tr><td>scrolled</td><td>Function</td><td>Called when the box content is scrolled. Passed two parameters 'x', and 'y' which are the current scroll position of the box window.</td><td>nil</td></tr><tr><td>scrollTo</td><td>Function</td><td>Function to override the box scroll position. Must return two values, 'x' and 'y' which are the position to scroll the box window to.</td><td>nil</td></tr><tr><td>align<br><br>(Added in 2.11.4)</td><td>Alignment type:<br>- LEFT, RIGHT, CENTER, VTOP, VBOTTOM. VCENTER</td><td>Sets the alignment when using flex layouts.<br><br>NOTE: If the box content is larger than the box size (requiring a scroll bar), then do not use the alignment options in the same direction as the scroll. If the flex layout is FLOW_COLUMN and the box has a vertical scroll bar then VCENTER and VBOTTOM alignment will not work. If the flex layout is FLOW_ROW and the box has a horizontal scroll bar then CENTER and RIGHT alignment will not work</td><td>CENTER | TOP</td></tr></tbody></table>

## Return values

LVGL object

## Notes

The 'page' object should be created as the top level LVGL object in the script window, and all other LVGL objects added as children of the 'page' object.

The page will automatically add scroll bars if any child objects are placed outside of the page boundaries.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
