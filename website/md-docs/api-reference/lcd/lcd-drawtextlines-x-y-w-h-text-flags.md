# lcd.drawTextLines(x, y, w, h, text \[, flags])

Draw text inside rectangle (x,y,w,h) with line breaks

@status current Introduced in 2.5.0

## Parameters

* `x,y` (positive numbers) starting coordinate
* `w,h` (positive numbers) width and height of bounding rectangle
* `text` (string) text to display
* `flags` (optional) please see [Lcd functions overview](https://app.gitbook.com/s/-MfaayEzpdu0ABuVlosG-2579488400/part\_iii\_-\_opentx\_lua\_api\_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd\_functions-overview.html) for drawing flags and colors, and [Appendix](https://app.gitbook.com/s/-MfaayEzpdu0ABuVlosG-2579488400/part\_vii\_-\_appendix/fonts.md) for available characters in each font set. RIGHT, CENTER and VCENTER are not implemented.

## Return value

none
