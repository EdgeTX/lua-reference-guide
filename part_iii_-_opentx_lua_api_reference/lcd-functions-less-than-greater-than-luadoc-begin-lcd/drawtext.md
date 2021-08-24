# lcd.drawText\(x, y, text \[, flags\]\)

Draw a text beginning at \(x,y\)

@status current Introduced in 2.0.0, `SHADOWED` introduced in 2.2.1

## Parameters

* `x,y` \(positive numbers\) starting coordinate
* `text` \(string\) text to display
* `flags` \(optional\) please see [Lcd functions overview](https://github.com/EdgeTX/lua-reference-guide/tree/2c4596e02006c8ac7d351fcd785fdfc7a93ce548/part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) for drawing flags and colors, and [Appendix](../../part_vii_-_appendix/fonts.md) for available characters in each font set.
* `inversColor` \(optional with the INVERS flag\) overrides the inverse text color for INVERS

## Return value

none

