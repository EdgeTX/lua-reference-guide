# lcd.drawLineWithClipping\(x1, y1, x2, y2, xmin, xmax, ymin, ymax, pattern \[, flags\]\)

Draw a line only inside a rectangle

@status current Introduced in 2.4.0

## Parameters

* `x1,y1,x2,y1` \(positive numbers\) coordinates of the start and end of the unclipped line
* `xmin,xmax,ymin,ymax` \(positive numbers\) the limits of the rectangle inside which the line is drawn
* `pattern` \(FORCE, ERASE, DOTTED\) please see [Lcd functions overview](https://github.com/EdgeTX/lua-reference-guide/tree/4528a8bc59edf04ef7d8ea8367b679d1c99f568e/part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html)
* `flags` \(optional\) please see [Lcd functions overview](https://github.com/EdgeTX/lua-reference-guide/tree/4528a8bc59edf04ef7d8ea8367b679d1c99f568e/part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html)

## Return value

none

