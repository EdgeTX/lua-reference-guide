# lcd.drawPoint\(x, y\)

Draw a single pixel at \(x,y\) position

@status current Introduced in 2.0.0

## Parameters

* `x` \(positive number\) x position
* `y` \(positive number\) y position
* `flags` \(optional\) please see [Lcd functions overview](https://github.com/EdgeTX/lua-reference-guide/tree/2c4596e02006c8ac7d351fcd785fdfc7a93ce548/part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html)

## Return value

none

### Notice

Taranis has an LCD display width of 212 pixels and height of 64 pixels. Position \(0,0\) is at top left. Y axis is negative, top line is 0, bottom line is 63. Drawing on an existing black pixel produces white pixel \(TODO check this!\)

