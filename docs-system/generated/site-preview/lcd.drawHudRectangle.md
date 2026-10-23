# lcd.drawHudRectangle

`lcd.drawHudRectangle(pitch, roll, xmin, xmax, ymin, ymax [, flags])`

Draw a rectangle in perspective

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `pitch` | yes | `integer` | pitch and roll to define the orientation of the rectangle |
| `roll` | yes | `integer` | pitch and roll to define the orientation of the rectangle |
| `xmin` | yes | `integer` | the limits of the rectangle |
| `xmax` | yes | `integer` | the limits of the rectangle |
| `ymin` | yes | `integer` | the limits of the rectangle |
| `ymax` | yes | `integer` | the limits of the rectangle |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

None.

## Availability

- Since: `2.4.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
