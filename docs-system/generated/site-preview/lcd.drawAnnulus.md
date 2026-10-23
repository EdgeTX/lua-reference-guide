# lcd.drawAnnulus

`lcd.drawAnnulus(x, y, r1, r2, start, end [, flags])`

Draw an arc

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | coordinates of the center |
| `y` | yes | `integer` | coordinates of the center |
| `r1` | yes | `integer` | radii of the inside and outside of the annulus |
| `r2` | yes | `integer` | radii of the inside and outside of the annulus |
| `start` | yes | `integer` | start and end of the annulus |
| `end` | yes | `integer` | start and end of the annulus |
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
