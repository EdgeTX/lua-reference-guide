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

<table><thead><tr><th width="120">Name</th><th width="196">Type</th><th width="333">Description</th><th>Default</th></tr></thead><tbody><tr><td>title</td><td>String or Function</td><td>Text to be displayed as the title in the header of the page.<br><br>Title can be a function in 2.11.4 or later.</td><td>Empty string</td></tr><tr><td>subtitle</td><td>String or Function</td><td>Text to be displayed as the sub-title in the header of the page.<br><br>Subtitle can be a function in 2.11.4 or later.</td><td>Empty string</td></tr><tr><td>icon</td><td>String</td><td>Full path to an image file on the SD card to be displayed as the icon in the 'back' button (top left corner).<br>If not set then the EdgeTX logo icon is used.<br>The icon file is a mask image and should be 30x30 pixels in size and be a grey-scale image. White pixels are transparent and black pixels are fully opaque.</td><td>Empty string</td></tr><tr><td>back</td><td>Function</td><td>Called when the user taps the 'back' button, or presses the RTN key. See button description below</td><td>nil</td></tr><tr><td>menu<br><br>(Added in 2.11.4)</td><td>Function</td><td>Called when the user taps the 'menu' button. See button description below</td><td>nil</td></tr><tr><td>prevButton<br><br>(Added in 2.11.4)</td><td>Table</td><td>If set this will add a 'prev' navigation button to the header.<br>The table should containg a 'press' function that will be called when the button is tapped.<br>The table may contiain an 'active' function that sets the enabled / disabled state of the button (return false to disable the button).</td><td>nil</td></tr><tr><td>nextButton<br><br>(Added in 2.11.4)</td><td>Table</td><td>If set this will add a 'next' navigation button to the header.<br>The table should containg a 'press' function that will be called when the button is tapped.<br>The table may contiain an 'active' function that sets the enabled / disabled state of the button (return false to disable the button).</td><td>nil</td></tr><tr><td>flexFlow</td><td>Flow type - lvgl.FLOW_COLUMN or lvgl.FLOW_ROW</td><td>Enable flex layout for this page.</td><td>not used</td></tr><tr><td>flexPad</td><td>Number</td><td>When flex layout is used, set the padding between rows or columns.<br>Recommended to use the lvgl.PAD_xxx values.</td><td>PAD_OUTLINE</td></tr><tr><td>scrollBar</td><td>Boolean</td><td>Sets the allowed scrolling directions if child objects extend beyond the box boundaries. Only valid for stand alone scripts.</td><td>true</td></tr><tr><td>scrollDir</td><td>Scroll type - lvgl.SCROLL_xx</td><td>Sets the allowed scrolling directions if child objects extend beyond the page boundaries.<br>Only valid for stand alone scripts.</td><td>lvgl.SCROLL_ALL</td></tr><tr><td>scrolled</td><td>Function</td><td>Called when the box content is scrolled. Passed two parameters 'x', and 'y' which are the current scroll position of the box window.</td><td>nil</td></tr><tr><td>scrollTo</td><td>Function</td><td>Function to override the box scroll position. Must return two values, 'x' and 'y' which are the position to scroll the box window to.</td><td>nil</td></tr><tr><td>align<br><br>(Added in 2.11.4)</td><td>Alignment type:<br>- LEFT, RIGHT, CENTER, VTOP, VBOTTOM. VCENTER</td><td>Sets the alignment when using flex layouts.<br><br>NOTE: If the box content is larger than the box size (requiring a scroll bar), then do not use the alignment options in the same direction as the scroll. If the flex layout is FLOW_COLUMN and the box has a vertical scroll bar then VCENTER and VBOTTOM alignment will not work. If the flex layout is FLOW_ROW and the box has a horizontal scroll bar then CENTER and RIGHT alignment will not work</td><td>CENTER | TOP</td></tr><tr><td>backButton<br><br>(Added in 2.11.4)</td><td>Boolean</td><td>If set to true displays an exit/back button in the header on the right side.</td><td>false</td></tr><tr><td>borderPad<br><br>(Added in 2.11.5)</td><td>Number or Table</td><td>Controls the border padding around the edges of the container.<br><br>Can be a number which sets uniform padding on all side. Or a table to set each side separately - e.g. {left=?, right=?, top=?, bottom=?}</td><td>PAD_OUTLINE If flexFlow is set, otherwise 0.</td></tr></tbody></table>

## Page action buttons

By default the 'page' object have a single button in the top left corner. If tapped this will call the 'back' function defined for the page.

To align with the 3.0 UI for EdgeTX, additional navigation buttons can be enabled for the page header.

Setting 'backButton' to true will display an exit/back button in the top rigth corner - if tapped this will call the 'back' function. Tapping the top left button will not call the 'back' function; but will call the 'menu' function instead.

Setting the 'prevButton' and 'nextButton properties will add two additional buttons to the header for touch screen navigation. These will call the 'press' functions set for each property when tapped. If both buttons are not needed you can choose to either not show the button (don't define the property), or use the 'active' function to disable the button when not needed.

```lua
  local pg = lvgl.page({title="Test Tool", subtitle="Page 1", backButton=true,
                        prevButton={press=function() ... end, active=function() return ... end},
                        nextButton={press=function() ... end},
                        })

```

<figure><img src="../../.gitbook/assets/Screenshot 2025-12-04 at 1.49.43 pm.png" alt=""><figcaption></figcaption></figure>

Note: the PAGE keys are not automatically mapped to the 'prev' and 'next' functions. The script should detect these keys in the 'run' function and handle as needed.

## Return values

LVGL object

## Notes

The 'page' object should be created as the top level LVGL object in the script window, and all other LVGL objects added as children of the 'page' object.

The page will automatically add scroll bars if any child objects are placed outside of the page boundaries.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td>Only available for One-Time scripts and widgets running in full screen mode.</td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
