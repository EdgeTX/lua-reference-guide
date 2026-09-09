# lcd.drawTriangle

`lcd.drawTriangle(x1, y1, x2, y2, x3, y3 [, flags])`

Draw a triangle

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x1` | yes | `integer` | coordinates of the three vertices |
| `y1` | yes | `integer` | coordinates of the three vertices |
| `x2` | yes | `integer` | coordinates of the three vertices |
| `y2` | yes | `integer` | coordinates of the three vertices |
| `x3` | yes | `integer` | coordinates of the three vertices |
| `y3` | yes | `integer` | coordinates of the three vertices |
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
