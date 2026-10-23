# lcd.drawFilledRectangle

`lcd.drawFilledRectangle(x, y, w, h [, flags [, opacity]])`

Draw a solid rectangle from top left corner (x,y) of specified width and height

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | top left corner position |
| `y` | yes | `integer` | top left corner position |
| `w` | yes | `integer` | width in pixels |
| `h` | yes | `integer` | height in pixels |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |
| `opacity` | no | `integer` | opacity defaults to 0 (only on radios with color display) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
