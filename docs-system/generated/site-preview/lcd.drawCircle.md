# lcd.drawCircle

`lcd.drawCircle(x, y, r [, flags])`

Draw a circle at (x, y) of specified radius

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | center position |
| `y` | yes | `integer` | center position |
| `r` | yes | `integer` | radius in pixels |
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
