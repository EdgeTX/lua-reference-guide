# lcd.drawGauge

`lcd.drawGauge(x, y, w, h, fill, maxfill [, flags])`

Draw a simple gauge that is filled based upon fill value

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | top left corner position |
| `y` | yes | `integer` | top left corner position |
| `w` | yes | `integer` | width in pixels |
| `h` | yes | `integer` | height in pixels |
| `fill` | yes | `integer` | amount of fill to apply |
| `maxfill` | yes | `integer` | total value of fill |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
